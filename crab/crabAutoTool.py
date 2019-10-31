import os, sys, smtplib, subprocess, time
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from prettytable import PrettyTable
user=str(os.environ['USER'])
cmsswBase=str(os.environ['CMSSW_BASE'])
voms=bool(os.environ.get('VOMSINITVAR'))

cnts={}

def sendMailTo(main, error=False): #, sample, status):
        
    curTime=(time.strftime("%H:%M:%S"))
    curDate=(time.strftime("%d/%m/%Y"))

    fromaddr = "Heppy CRAB Auto-Tool"
    toaddr = user+"@cern.ch"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Heppy CRAB Production report ("+curDate+" ; "+curTime+") "
    if error:
        msg['Subject']+=" ABORTED"
    msg.attach(MIMEText(main, 'plain'))
    
    text = msg.as_string()

    #server = smtplib.SMTP('smtp.cern.ch', 587)
    #server.starttls()
    #server.login(toaddr, passw)
    server = smtplib.SMTP("localhost")
    server.sendmail(toaddr, toaddr, text)
    server.quit()

def checkStatusTask(task):
    
    p = subprocess.Popen(['crab','status', '-d',task],
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE)
    log, err = p.communicate()

    taskName=""
    ext=""
    jobInfos={"run":0,
              "done":0,
              "transfert":0,
              "wait":0,
              "fail":0,
              "total":0,
              }
    
    for line in log.splitlines(): #("\n"):
        
        if "Task name" in line:
            taskName=(line.split(":")[2])
            ext=''# taskName.split("_")[-1]
            #taskName=taskName[len(user)+6 : -1*(len(ext)+1) ]

        if "timed out" in line: #error of communication, bypass
            return taskName, ext, jobInfos

        if 'Warning:' in line: continue
        if len(line.split("("))>1 and "/" in line:
            tmp=line.split("(")[1][:-1]
            nJobs=int(tmp.split("/")[0])
            jobInfos["total"] = int(tmp.split("/")[1])
        
            if "running" in line:
                jobInfos["run"] = nJobs
            if "finished" in line or "transferred" in line :
                jobInfos["done"] = nJobs
            if "transferring" in line :
                jobInfos["transfert"] = nJobs
            if ("unsubmitted" in line) or ("idle" in line):
                jobInfos["wait"] += nJobs
            if "failed" in line:
                jobInfos["fail"] = nJobs

    #print taskName, ext, jobInfos
    return taskName, ext, jobInfos

def crabResubmit(task):
    os.system("crab resubmit -d "+task)
    #p = subprocess.Popen(['crab','resubmit', '-d',task],
    #                     stdout=subprocess.PIPE, 
    #                     stderr=subprocess.PIPE)
    #log, err = p.communicate()




def prepareReport(tasks):

    dataSetsNames=["DoubleEG","DoubleMuon","SingleElectron","SingleMuon","MuonEG","MET","JetHT"]
    types=["wait","run","transfert","fail","done","total"]

    messages={}
    errorState=-1
    summary={}

    sumjobInfos={"run":0,
                 "done":0,
                 "transfert":0,
                 "wait":0,
                 "fail":0,
                 "total":0,
             }



    for task in tasks:
        name, ext, jobInfos=checkStatusTask(task)
        for typ in sumjobInfos:
            sumjobInfos[typ] += jobInfos[typ]

        print name, ext, jobInfos
        isData=False
        
            #("$%2.2f"%CBYields[sig][cat]
        summary[name]= [("%-70s"%name)+"("+("%-7s"%ext)+")"]
        for t in types:
            summary[name].append("%5i"%jobInfos[t])
     
        
        if jobInfos["total"]==0:
            errorState=0
            messages[name]="ERROR : unable to retrieve the jobs for the task "+name+" ("+ext+"), manual check needed\n"
            continue

        if name+"_"+ext not in cnts.keys():
            cnts[name+"_"+ext] = [0, "run" ]

        if (jobInfos["done"]==jobInfos["total"]):
            errorState=-2
            messages[name]="DATASET "+name+" : production DONE\n"
            cnts[name+"_"+ext][1]="done"
        else:
            if jobInfos["fail"]>0:
                if cnts[name+"_"+ext][0]<24:
                    errorState=1
                    messages[name]="WARNING : pp data dataset "+name+" ("+ext+") shows failed jobs ("+str(jobInfos["fail"])+"/"+str(jobInfos["total"])+") -> automatic resubmission\n"
                    cnts[name+"_"+ext][0]+=1
                    crabResubmit(task)
                else:
                    errorState=2
                    messages[name]="ERROR : pp data dataset "+name+" ("+ext+") shows failed jobs ("+str(jobInfos["fail"])+"/"+str(jobInfos["total"])+") after 10 resubmission!! Manual action needed\n"

        

            


                    
    curTime=(time.strftime("%H:%M:%S"))
    curDate=(time.strftime("%d/%m/%Y"))
    report="Production report : "+curDate+" ("+curTime+")\n\n"
    for task in messages.keys():
        report+=messages[task]

    report+="\n\n\n\t\t Summary Table\n"
    x = PrettyTable()
    x.field_names = ['Dataset (ext)', 'nWait','nRun', 'nTran', 'nFail', 'nDone', 'nTot']

    for task in summary.keys():
        x.add_row( summary[task] )
    x.add_row( ['All'] +  ["%5i"%sumjobInfos[t] for t in types ] )

    report += x.get_string()
    return report
        



def crabAutoTool(reset=False, regTasks="analysis_*/*"):
   
    #ending cron job if credientials are timed-out / validated
    p = subprocess.Popen(['voms-proxy-info'],
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE)
    log, err = p.communicate()
    if "Proxy not found" in err:
        os.system("acrontab -r")
        sendMailTo("VOMS credential expired : cron job terminated",True)
        return
 
    pipe = subprocess.Popen("ls -d "+regTasks, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    tasks = [l.strip("\n") for l in pipe.stdout.readlines()]

    report = prepareReport(tasks)
    sendMailTo(report)
    #print report

    
    #ending cron job if all datasets are processed
    nDone=len(cnts)
    for i in cnts.keys():
        if cnts[i][1]=="done": nDone-=1
    if nDone==0:
        os.system("acrontab -r")


if len(sys.argv) > 1:
    crabAutoTool(sys.argv[1],sys.argv[2])
else:
    crabAutoTool()


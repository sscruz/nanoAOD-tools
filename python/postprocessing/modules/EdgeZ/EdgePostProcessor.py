#!/usr/bin/env python
import os
import sys
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import * 

import json



### SKIM 
cut = None

### SLIM FILE
outputSlim = os.environ['CMSSW_BASE']+"/python/PhysicsTools/NanoAODTools/postprocessing/modules/EdgeZ/OutputSlim.txt"
inputSlim  = os.environ['CMSSW_BASE']+"/python/PhysicsTools/NanoAODTools/postprocessing/modules/EdgeZ/InputSlim.txt"

from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.collectionMerger import collectionMerger
from PhysicsTools.NanoAODTools.postprocessing.modules.EdgeZ.skimNRecoLeps import SkimRecoLeps
from PhysicsTools.NanoAODTools.postprocessing.modules.EdgeZ.isoTrackAnalysis import IsoTrackAnalysis
from PhysicsTools.NanoAODTools.postprocessing.modules.common.TriggerBitFilter import TriggerBitFilter
from PhysicsTools.NanoAODTools.postprocessing.modules.EdgeZ.edgeFriends import edgeFriends, _susyEdgeTight, _susyEdgeLoose
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import createJMECorrector
from PhysicsTools.NanoAODTools.postprocessing.modules.EdgeZ.susyReweight import susyReweight



isoTrackAnalysis = IsoTrackAnalysis()


from PhysicsTools.NanoAODTools.postprocessing.modules.common.addFlags import AddFlags

from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import getCrabOption



doData=getCrabOption("doData",False)
doYear=getCrabOption("doYear",0)
doSMS =getCrabOption("doSMS",False)

if not 'IS_CRAB' in os.environ and not 'IS_RUN' in os.environ:



    print '[EdgeZ]: Submission step'
    from PhysicsTools.NanoAODTools.postprocessing.datasets.mc2016    import samples as mcSamples2016
    from PhysicsTools.NanoAODTools.postprocessing.datasets.data2016  import samples as dataSamples2016
    from PhysicsTools.NanoAODTools.postprocessing.datasets.mc2017    import samples as mcSamples2017
    from PhysicsTools.NanoAODTools.postprocessing.datasets.data2017  import samples as dataSamples2017
    from PhysicsTools.NanoAODTools.postprocessing.datasets.mc2018    import samples as mcSamples2018
    from PhysicsTools.NanoAODTools.postprocessing.datasets.data2018  import samples as dataSamples2018

    mcSamples   = eval('mcSamples%d'%doYear)
    if doSMS: 
        from PhysicsTools.NanoAODTools.postprocessing.datasets.signals  import signals2016,signals2017,signals2018

    
        mcSamples = eval('signals%d'%doYear)

    dataSamples = eval('dataSamples%d'%doYear)

    filteredSamples = [] 
    filterList = [#'WZTo2L2Q', 'ZZTo2L2Nu'
                  'TTJets_SingleLeptonFromT','TTJets_SingleLeptonFromT','TTTo2L2Nu','TTToSemiLeptonic',
                  'DYJetsToLL_M50',
                  'DYJetsToLL_M10to50',
                  'WWTo2L2Nu',
                  'WZTo3LNu',
                  'WJetsToLNu',
                  'T_tch', 'Tbar_tch', 'TW','TbarW',
                  'ZZTo4L', 'ZZTo2Q2Nu', 
                  'GluGluToContinToZZTo2e2mu', 'GluGluToContinToZZTo2e2nu', 'GluGluToContinToZZTo2e2tau',
                  'GluGluToContinToZZTo2mu2nu','GluGluToContinToZZTo2mu2tau','GluGluToContinToZZTo4e',
                  'GluGluToContinToZZTo4mu', 'GluGluToContinToZZTo4tau',
                  'TTZToLLNuNu','TTZToLLNuNu_m1to10',
                  'TTWToLNu', 
                  'WWW','WWZ','WZZ','ZZZ','TTHnobb'
    ]
    filterOut = ['DYJetsToLL_M50_1J','DYJetsToLL_M50_2J']
    for samp in mcSamples:
        for filt in filterOut : 
            if filt in samp.name: continue
        for filt in filterList: 
            if filt in samp.name: filteredSamples.append(samp)
    mcSamples = filteredSamples
    
    
    if doData:
        from PhysicsTools.NanoAODTools.postprocessing.datasets.triggers_13TeV_DATA2016 import triggers2016
        from PhysicsTools.NanoAODTools.postprocessing.datasets.triggers_13TeV_DATA2017 import triggers2017
        from PhysicsTools.NanoAODTools.postprocessing.datasets.triggers_13TeV_DATA2018 import triggers2018
        
        selectedSamples = dataSamples
        filtered = [] 
        for samp in selectedSamples:
            if '2017D' not in samp.name: continue
            filtered.append( samp)
        selectedSamples = filtered


        DatasetsAndTriggersMap = {}; DatasetsAndVetosMap = {} 
        DatasetsAndTriggersMap = {}; DatasetsAndVetosMap = {} 
        yeartriggers = eval('triggers%d'%doYear)

        if doYear in [2016, 2017]:
            # DoubleMuon > DoubleEG> MuonEG
            DatasetsAndTriggersMap["DoubleMuon"     ] = yeartriggers['triggers_mumu_iso'] + yeartriggers['triggers_3mu']
            DatasetsAndTriggersMap["DoubleEG"       ] = yeartriggers['triggers_ee'] + yeartriggers['triggers_3e'] + yeartriggers['triggers_ee_noniso']
            DatasetsAndTriggersMap["MuonEG"         ] = yeartriggers['triggers_mue'] + yeartriggers['triggers_2mu1e'] + yeartriggers['triggers_2e1mu'] + yeartriggers['triggers_mue_noiso']
            DatasetsAndTriggersMap["MET" ] = []
        
            DatasetsAndVetosMap["DoubleMuon"    ] = [] 
            DatasetsAndVetosMap["DoubleEG"      ] = DatasetsAndTriggersMap["DoubleMuon"  ] + DatasetsAndVetosMap["DoubleMuon"  ] 
            DatasetsAndVetosMap["MuonEG"        ] = DatasetsAndTriggersMap["DoubleEG"  ] + DatasetsAndVetosMap["DoubleEG"  ] 
            DatasetsAndVetosMap["MET"] = [] 
        
        else: 
            # DoubleMuon > EGamma > MuonEG
            DatasetsAndTriggersMap["DoubleMuon"     ] = yeartriggers['triggers_mumu_iso'] + yeartriggers['triggers_3mu']
            DatasetsAndTriggersMap["EGamma"         ] = yeartriggers['triggers_ee'] + yeartriggers['triggers_3e'] + yeartriggers['triggers_ee_noniso'] + yeartriggers['triggers_1e_iso']
            DatasetsAndTriggersMap["MuonEG"         ] = yeartriggers['triggers_mue'] + yeartriggers['triggers_2mu1e'] + yeartriggers['triggers_2e1mu'] + yeartriggers['triggers_mue_noiso']
            DatasetsAndTriggersMap["MET" ] = []
        
            DatasetsAndVetosMap["DoubleMuon"    ] = []
            DatasetsAndVetosMap["EGamma"        ] = DatasetsAndTriggersMap["DoubleMuon"] + DatasetsAndVetosMap["DoubleMuon"] 
            DatasetsAndVetosMap["MuonEG"        ] = DatasetsAndTriggersMap["EGamma"    ] + DatasetsAndVetosMap["EGamma"    ] 

            DatasetsAndVetosMap["MET"] = [] 

    
        for sample in selectedSamples:
            if   doYear == 2016: jsonFile='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
            elif doYear == 2017: jsonFile='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt'
            elif doYear == 2018: jsonFile='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/ReReco/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt'

            jsn = open( jsonFile ,'r')
            sample.options['json'] = json.loads ( jsn.read())
            sample.options['isData'] = True
            jsn.close()
            for smp, trig in DatasetsAndTriggersMap.iteritems():
                if smp in sample.name:
                    sample.options['triggers']     = trig
                    sample.options['vetotriggers'] = DatasetsAndVetosMap[smp]
                    
                    break

    else:
        selectedSamples=mcSamples
        for sample in selectedSamples: sample.options['isData'] = False



## definition of postprocessor 

# postprocessor is only read when we are in running mode 

if 'IS_CRAB' in os.environ or 'IS_RUN' in os.environ:

    from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis

    try:
        with open('options_sample.json','r') as sampoptjson: 
            sampOpt = json.loads(sampoptjson.read())
            sampoptjson.close()
    except: 
        raise RuntimeError("No options_sample.json found")


    addFlags = AddFlags([(('isData','F'), lambda ev : sampOpt['isData'] ),
                         (('year','i')  , lambda ev : int(sampOpt['year']) ),
                     ]) #more flags will be added below
    skimRecoLeps     = SkimRecoLeps(sampOpt['isData'] == True, nMinLeps=2)
    goodElec =  lambda x : _susyEdgeLoose(x, int(sampOpt['year']))
    goodMuon =  lambda x : _susyEdgeLoose(x, int(sampOpt['year']))



    goodLepProducer = collectionMerger(input=["Electron","Muon"], output="LepGood",
                                       maxObjects=10,
                                       selector=dict([("Electron", goodElec),
                                                      ("Muon", goodMuon)
                                                  ]),
                                       store=False
    )

    edgeFriends = edgeFriends("Edge", lambda lep : _susyEdgeTight(lep,int(sampOpt['year'])),
                              cleanJet = lambda lep,jet,dr : (jet.pt < 35 and dr < 0.4),
                              year = int(sampOpt['year'])
    )

    mod = [ goodLepProducer, skimRecoLeps, isoTrackAnalysis]

    era = sampOpt['name'].split(sampOpt['year'])[1][0] # lol 
    jmeUncert = createJMECorrector( not sampOpt['isData'], sampOpt['year'], era) 
    jmeUncertAK8 = createJMECorrector( not sampOpt['isData'], sampOpt['year'], era, jetType="AK8PFPuppi")
    print 'missing jecs!!'
    mod.extend([jmeUncert(),jmeUncertAK8()])

    if not sampOpt['isData']:
        # add pile-up weight before any skim
        puAutoWeight  = eval('puAutoWeight_%s'%sampOpt['year'])
        
        mod = [puAutoWeight()] + mod
        ## add xsection flag
        addFlags.flags.append(  (('xsec','F'), lambda ev : sampOpt['xsec'] ))
        if sampOpt['scan']:
            countScans = susyReweight( sampOpt['scan'] ) 
            mod = [countScans] + mod

    mod.append(addFlags)
    # now adding the edge part at the end 
    mod.append(edgeFriends)

    if 'triggers' in sampOpt:
        if not 'vetotriggers' in sampOpt:
            raise RuntimeError('[%s]: You have specified trigger requierments, but not veto triggers. Please include them (can be an empty list)')
        triggerBitFilter = TriggerBitFilter( triggers = sampOpt['triggers'],
                                             vetotriggers = sampOpt['vetotriggers'])
        mod = [triggerBitFilter] + mod



    jsonInput = sampOpt['json'] if 'json' in sampOpt else runsAndLumis()     
    POSTPROCESSOR=PostProcessor(".",inputFiles() if 'IS_CRAB' in os.environ else [],cut,inputSlim,mod,provenance=True,fwkJobReport=True,jsonInput=jsonInput, outputbranchsel=outputSlim)#,friend=True)
        


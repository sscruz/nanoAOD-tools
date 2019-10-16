import getpass
import os
import sys

import imp, os, json
from optparse import OptionParser,OptionGroup

parser = OptionParser()
g1 = OptionGroup(parser,"Analysis options")
g1.add_option("-c", "--cfg-file", dest="cfg_file", help="Config file containing PostProcessor instance", default="")
parser.add_option_group(g1)
g1.add_option("-o", "--option", dest="extraOptions", type="string", action="append", default=[], help="options to use for task preparation and in remote jobs")

(options,args) = parser.parse_args()


# global options 
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import _crabGlobalOptions
os.environ['IS_RUN']="true"
for opt in options.extraOptions:
    if "=" in opt:
        (key,val) = opt.split("=",1)
        _crabGlobalOptions[key] = val
    else:
        _crabGlobalOptions[opt] = True
_crabGlobalOptions["isCrab"] = True
optjsonfile = open('options.json','w')
optjsonfile.write(json.dumps(_crabGlobalOptions))
optjsonfile.close()

## create dummy sample json to run locally
options_sample = open('options_sample.json','w')

#from PhysicsTools.NanoAODTools.postprocessing.datasets.triggers_13TeV_DATA2017 import triggers2017
#yeartriggers = triggers2017

sampOpt = { 'isData' : True,
            'triggers' :  [],#yeartriggers['triggers_mue'] + yeartriggers['triggers_2mu1e'] + yeartriggers['triggers_2e1mu'] + yeartriggers['triggers_mue_noiso'], 
            'year' : '2018',
            'vetotriggers' :  [],#yeartriggers['triggers_ee'] + yeartriggers['triggers_3e'] + yeartriggers['triggers_ee_noniso'],
            'json':   None, # '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_29497-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt',
            'xsec' : 88.,
            'name' : 'TTbar'
            }   

options_sample.write(json.dumps( sampOpt))
options_sample.close()



handle = open(options.cfg_file,'r')
cfo = imp.load_source(options.cfg_file.split('/')[-1].rstrip('.py'), options.cfg_file, handle)


cfo.POSTPROCESSOR.inputFiles = [
    #'/afs/cern.ch/work/s/sesanche/private/TTH/CMSSW_10_2_15/src/myNanoProdMc2016_NANO.root'
    '/afs/cern.ch/work/s/sesanche/private/TTH/CMSSW_10_2_15/src/myNanoProdMc2018_NANO.root'
]


cfo.POSTPROCESSOR.run()


# clean up environ
del os.environ['IS_RUN']

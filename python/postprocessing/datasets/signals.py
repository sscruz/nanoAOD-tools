from PhysicsTools.NanoAODTools.postprocessing.datasets.componentContainer import  ComponentContainer


TChiWZ_2018              = ComponentContainer('TChiWZ', '/SMS-TChiWZ_ZToLL_mZMin-0p1_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_GridpackScan_102X_upgrade2018_realistic_v19-v2/NANOAODSIM', 1 )
TChiWZ_325to1000_2018    = ComponentContainer('TChiWZ_325to1000', '/SMS-TChiWZ_ZToLL_mZMin-0p1_mC1-325to1000_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_GridpackScan_102X_upgrade2018_realistic_v19-v1/NANOAODSIM', 1 )
TChiWZ_2017              = ComponentContainer('TChiWZ', '/SMS-TChiWZ_ZToLL_mZMin-0p1_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_GridpackScan_102X_mc2017_realistic_v7-v1/NANOAODSIM', 1 )
TChiWZ_325to1000_2017    = ComponentContainer('TChiWZ_325to1000', '/SMS-TChiWZ_ZToLL_mZMin-0p1_mC1-325to1000_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_GridpackScan_102X_mc2017_realistic_v7-v1/NANOAODSIM', 1 )
TChiWZ_2016              = ComponentContainer('TChiWZ', '/SMS-TChiWZ_ZToLL_mZMin-0p1_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_GridpackScan_102X_mcRun2_asymptotic_v7-v2/NANOAODSIM', 1 )
TChiWZ_325to1000_2016    = ComponentContainer('TChiWZ_325to1000', '/SMS-TChiWZ_ZToLL_mZMin-0p1_mC1-325to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_GridpackScan_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM', 1 )

fullSimSamples = [
    TChiWZ_2018          ,
    TChiWZ_325to1000_2018,
    TChiWZ_2017          ,
    TChiWZ_325to1000_2017,
    TChiWZ_2016          ,
    TChiWZ_325to1000_2016,
] 

for samp in [TChiWZ_2018 ,TChiWZ_325to1000_2018,TChiWZ_2017 ,TChiWZ_325to1000_2017,TChiWZ_2016 ,TChiWZ_325to1000_2016]:
    samp.options['scan']='TChiWZ'





TSlepslep_2018 = ComponentContainer("TSlepslep", "/SMS-TSlepSlep_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv5-PUFall18Fast_Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM",1)
TSlepslep_2017 = ComponentContainer("TSlepslep", "/SMS-TSlepSlep_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PUFall17Fast_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM",1)
TSlepslep_500To1300_2018 = ComponentContainer("TSlepslep_500To1300", "/SMS-TSlepSlep_mSlep-500To1300_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv5-PUFall18Fast_Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM",1)
TSlepslep_500To1300_2017 = ComponentContainer("TSlepslep_500To1300", "/SMS-TSlepSlep_mSlep-500To1300_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PUFall17Fast_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM",1)
TSlepslep_500To1300_2016 = ComponentContainer("TSlepslep_500To1300", "/SMS-TSlepSlep_mSlep-500To1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv5-PUSummer16v3Fast_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM",1)

for samp in [TSlepslep_2018,TSlepslep_2017,TSlepslep_500To1300_2018,TSlepslep_500To1300_2017,TSlepslep_500To1300_2016]:
    samp.options['scan']='TSlep'


TChiZZ_2017 = ComponentContainer("TChiZZ","/SMS-TChiZZ_ZToLL_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PUFall17Fast_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM",1)
TChiZZ_2016 = ComponentContainer("TChiZZ","/SMS-TChiZZ_ZToLL_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv5-PUSummer16v3Fast_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM",1)

for samp in [TChiZZ_2017,TChiZZ_2016]:
    samp.options['scan']='TChiZZ'




signals2016 = [
    TChiWZ_2016          ,
    TChiWZ_325to1000_2016,
    TSlepslep_500To1300_2016,
    TChiZZ_2016,
]
signals2017 = [
    TChiWZ_2017          ,
    TChiWZ_325to1000_2017,
    TSlepslep_2017,
    TSlepslep_500To1300_2017,
    TChiZZ_2017,
]
signals2018 = [
    TChiWZ_2018          ,
    TChiWZ_325to1000_2018,
    TSlepslep_2018,
    TSlepslep_500To1300_2018,
]

for samp in signals2016+signals2017+signals2018:
    samp.options['isData'] = False
    samp.options['isFastSim'] = True

for samp in fullSimSamples:
    samp.options['isFastSim'] = False

for samp in signals2016:
    samp.options['year']   = '2016'
    samp.name = samp.name + '_2016'
for samp in signals2017:
    samp.options['year']   = '2017'
    samp.name = samp.name + '_2017'
for samp in signals2018:
    samp.options['year']   = '2018'
    samp.name = samp.name + '_2018'
    

from PhysicsTools.NanoAODTools.postprocessing.datasets.componentContainer import  ComponentContainer

TTJets_SingleLeptonFromT = ComponentContainer('TTJets_SingleLeptonFromT','/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM', 831.76*(3*0.108)*(1-3*0.108) )
TTJets_SingleLeptonFromT_ext1 = ComponentContainer('TTJets_SingleLeptonFromT_ext1','/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM', 831.76*(3*0.108)*(1-3*0.108) )

TTJets_SingleLeptonFromTbar = ComponentContainer("TTJets_SingleLeptonFromTbar","/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", 831.76*(3*0.108)*(1-3*0.108))
TTJets_SingleLeptonFromTbar_ext1 = ComponentContainer("TTJets_SingleLeptonFromTbar_ext1","/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM", 831.76*(3*0.108)*(1-3*0.108))


TTJets_DiLepton     = ComponentContainer("TTJets_DiLepton","/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",831.76*((3*0.108)**2))
TTJets_DiLepton_ext = ComponentContainer("TTJets_DiLepton_ext","/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",831.76*((3*0.108)**2))



TT = [ TTJets_SingleLeptonFromT, TTJets_SingleLeptonFromT_ext1, TTJets_SingleLeptonFromTbar,TTJets_SingleLeptonFromTbar_ext1, TTJets_DiLepton, TTJets_DiLepton_ext ] 


DYJetsToLL_M10to50_LO = ComponentContainer("DYJetsToLL_M10to50_LO","/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",18610)

DYJetsToLL_M50_LO_ext = ComponentContainer("DYJetsToLL_M50_LO_ext","/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",2008.*3)
DYJetsToLL_M50_LO_ext2 = ComponentContainer("DYJetsToLL_M50_LO_ext2","/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext2-v1/NANOAODSIM",2008.*3)

DYJetsToLL_M50 = ComponentContainer("DYJetsToLL_M50","/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext2-v1/NANOAODSIM",2008.*3)
DYJetsToLL_M10to50     = ComponentContainer("DYJetsToLL_M10to50","/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",18610)
DYJetsToLL_M10to50_ext = ComponentContainer("DYJetsToLL_M10to50_ext","/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",18610)


WJetsToLNu_LO = ComponentContainer("WJetsToLNu_LO","/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",3* 20508.9)
WJetsToLNu_LO_ext1 = ComponentContainer("WJetsToLNu_LO_ext1","/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext2-v1/NANOAODSIM",3* 20508.9)

V =[ DYJetsToLL_M10to50_LO, DYJetsToLL_M50_LO_ext, DYJetsToLL_M50_LO_ext2, WJetsToLNu_LO, WJetsToLNu_LO_ext1]


t_tch = ComponentContainer("T_tch","/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",136.02)
t_tbarch = ComponentContainer("Tbar_tch","/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",80.95)
t_sch          = ComponentContainer('T_sch',"/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",(7.20+4.16)*0.108*3)

TW            = ComponentContainer('TW','/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM',35.6)
TbarW         = ComponentContainer('TbarW','/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM',35.6)

ST = [t_tch, t_tbarch, t_sch, TW, TbarW]



WWTo2L2Nu     = ComponentContainer("WWTo2L2Nu","/WWTo2L2Nu_13TeV-powheg/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",10.481)
WZTo3LNu = ComponentContainer("WZTo3LNu","/WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",4.666)
ZZTo4L   = ComponentContainer("ZZTo4L","/ZZTo4L_13TeV_powheg_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",1.256)
GluGluToContinToZZTo2e2mu     = ComponentContainer("GluGluToContinToZZTo2e2mu", "/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",0.00319)
GluGluToContinToZZTo2e2nu     = ComponentContainer("GluGluToContinToZZTo2e2nu", "/GluGluToContinToZZTo2e2nu_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",0.00319)
GluGluToContinToZZTo2e2tau    = ComponentContainer("GluGluToContinToZZTo2e2tau", "/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",0.00319)
GluGluToContinToZZTo2mu2nu    = ComponentContainer("GluGluToContinToZZTo2mu2nu", "/GluGluToContinToZZTo2mu2nu_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",0.00319)
GluGluToContinToZZTo2mu2tau   = ComponentContainer("GluGluToContinToZZTo2mu2tau", "/GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",0.00319)
GluGluToContinToZZTo4e        = ComponentContainer("GluGluToContinToZZTo4e", "/GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",0.00159)
GluGluToContinToZZTo4mu       = ComponentContainer("GluGluToContinToZZTo4mu", "/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",0.00159)
GluGluToContinToZZTo4tau      = ComponentContainer("GluGluToContinToZZTo4tau", "/GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",0.00159)

WpWpJJ = ComponentContainer("WpWpJJ","/WpWpJJ_EWK-QCD_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",0.03711)
#WWDouble = ComponentContainer("WWDouble","missing?")

WGToLNuG_amcatanlo_ext1  = ComponentContainer("WGToLNuG_amcatanlo_ext1",'/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM', 585.8)
WGToLNuG_amcatanlo_ext2  = ComponentContainer("WGToLNuG_amcatanlo_ext2",'/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext2-v1/NANOAODSIM', 585.8)
WGToLNuG_amcatanlo_ext3  = ComponentContainer("WGToLNuG_amcatanlo_ext3",'/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext3-v1/NANOAODSIM', 585.8)

ZGTo2LG = ComponentContainer("ZGTo2LG","/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",131.3)

VV = [WWTo2L2Nu, WZTo3LNu, ZZTo4L,GluGluToContinToZZTo2e2mu, GluGluToContinToZZTo2e2nu, GluGluToContinToZZTo2e2tau, GluGluToContinToZZTo2mu2nu, GluGluToContinToZZTo2mu2tau, GluGluToContinToZZTo4e, GluGluToContinToZZTo4mu, GluGluToContinToZZTo4tau, WpWpJJ,WGToLNuG_amcatanlo_ext1, WGToLNuG_amcatanlo_ext2,WGToLNuG_amcatanlo_ext3, ZGTo2LG ]


TTHnobb       = ComponentContainer("TTHnobb","/ttHToNonbb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",0.5085*(1-0.577))
TTWW = ComponentContainer("TTWW","/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",0.006977)
TTWToLNu  = ComponentContainer("TTWToLNu","/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext2-v1/NANOAODSIM",0.2043)
TTZToLLNuNu_ext = ComponentContainer("TTZToLLNuNu_ext","/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext2-v1/NANOAODSIM",0.2529)
TTZToLLNuNu_ext3= ComponentContainer("TTZToLLNuNu_ext3","/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext3-v1/NANOAODSIM",0.2529)
TTZToLLNuNu_m1to10 = ComponentContainer("TTZToLLNuNu_m1to10","/TTZToLL_M-1to10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv4-Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",0.05324)
TTGJets       = ComponentContainer("TTGJets","/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", 3.697)
TTGJets_ext1  = ComponentContainer("TTGJets_ext1","/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v2/NANOAODSIM", 3.697)

TTX = [ TTHnobb, TTWW, TTWToLNu, TTZToLLNuNu_ext, TTZToLLNuNu_ext3, TTZToLLNuNu_m1to10, TTGJets, TTGJets_ext1] 


THQ           = ComponentContainer("THQ","/THQ_Hincl_13TeV-madgraph-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",)
THW           = ComponentContainer("THW","/THW_Hincl_13TeV-madgraph-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",)
tZq = ComponentContainer("tZq_ll","/tZq_ll_4f_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",0.0758)
tWll = ComponentContainer("tWll", "/ST_tWll_5f_LO_13TeV-MadGraph-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",)
TTTT = ComponentContainer("TTTT","/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM", 0.009103)

Rares = [THQ, THW, tZq, tWll, TTTT] 


WWW = ComponentContainer("WWW","/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",0.2086)
WWZ = ComponentContainer("WWZ","/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",0.1651)
WZZ = ComponentContainer("WZZ","/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",0.05565)
ZZZ = ComponentContainer("ZZZ","/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",0.01398)

VVV = [WWW, WWZ, WZZ, ZZZ] 


samples = Rares + VVV + TTX + VV  + ST + V + TT 

for sample in samples: 
    sample.options['isData'] = False
    sample.options['year']   = '2016'
    sample.name = sample.name + '_2016'


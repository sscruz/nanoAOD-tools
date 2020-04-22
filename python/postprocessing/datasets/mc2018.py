from PhysicsTools.NanoAODTools.postprocessing.datasets.componentContainer import  ComponentContainer


QCD_Mu = [] # [ QCD_15to20_Mu, QCD_20to30_Mu, QCD_30to50_Mu, QCD_50to80_Mu, QCD_80to120_Mu, QCD_120to170_Mu, QCD_170to300_Mu, QCD_300to470_Mu, QCD_470to600_Mu,QCD_1000toInf_Mu]  #Still missing: #QCD_600to800_Mu, #QCD_800to1000_Mu



QCD_EM = [] #[QCD_15to20_EM, QCD_20to30_EM, QCD_30to50_EM, QCD_50to80_EM, QCD_80to120_EM, QCD_120to170_EM, QCD_300toInf_EM] #Still missing QCD_170to300_EM,
QCD_FR =  QCD_Mu + QCD_EM

TT_SL    = ComponentContainer('TTToSemiLeptonic', '/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM', 2*831.76*(3*0.108)*(1-3*0.108) )
TT_2L    = ComponentContainer('TTTo2L2Nu','/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM',831.76*((3*0.108)**2))
TT_SLTb  = ComponentContainer('TTJets_amc_SingleLeptFromTbar','/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM',831.76*(3*0.108)*(1-3*0.108))
#TT_SLT   = ComponentContainer('TTJets_amc_SingleLeptFromT','/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v6-v1/NANOAODSIM', 831.76*(3*0.108)*(1-3*0.108))
#TT_Had   = ComponentContainer('TTToHadronic', '/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM', 831.76*(1-3*0.108)*(1-3*0.108) )

TT = [TT_SL, TT_2L, TT_SLTb] # , TT_Had, ] #[  TT_SLT, ]


DY_M50     =  ComponentContainer('DYJetsToLL_M50_amc','/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM'   ,2008.*3)
DY_M50_ext2     =  ComponentContainer('DYJetsToLL_M50_amc_ext','/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19_ext2-v1/NANOAODSIM'   ,2008.*3)
DY_M10to50 =  ComponentContainer('DYJetsToLL_M10to50','/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM',  18610)
#DY_M50_mad =  ComponentContainer('DYJetsToLL_M50_LO','/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v2/NANOAODSIM'    ,2008.*3)




#DY_M50_HT70_100  = ComponentContainer('DYJetsToLL_M50_HT70To100', '/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM',0)
# print xsec misisng here
DY_M50_HT100_200 = ComponentContainer('DYJetsToLL_M50_HT100to200', '/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM', 1.23*147.40)
DY_M50_HT200_400 = ComponentContainer('DYJetsToLL_M50_HT200to400', '/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM',1.23*40.99)
#DY_M50_HT400_600 = ComponentContainer('DYJetsToLL_M50_HT400to600', '/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM',1.23*5.678)
DY_M50_HT400_600_ext2 = ComponentContainer('DYJetsToLL_M50_HT400to600_ext2', '/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19_ext2-v1/NANOAODSIM',1.23*5.678)
DY_M50_HT600_800 = ComponentContainer('DYJetsToLL_M50_HT600to800','/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM', 1.23*1.367)
DY_M50_HT800_1200 = ComponentContainer('DYJetsToLL_M50_HT800to1200','/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM',1.23*0.6304 )
DY_M50_HT2500_Inf = ComponentContainer('DYJetsToLL_M50_HT2500_Inf','/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM', 1.23*0.003565)


# dont know the xsec (and shouldnt contribute) 
#DY_0Jets  = ComponentContainer('DYJetsToLL_M50_0J', '/DYJetsToLL_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM',0)
# missing in nano DY_1Jets  = ComponentContainer('DYJetsToLL_M50_1J', '/DYJetsToLL_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v6-v1/NANOAODSIM',878)

# DY_M4to50 missing
WJets     = ComponentContainer('WJetsToLNu', '/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM',3* 20508.9)

V = [DY_M50, DY_M10to50, DY_M50_HT100_200, DY_M50_HT200_400, DY_M50_HT400_600_ext2, DY_M50_HT600_800, DY_M50_HT800_1200, 
     DY_M50_HT2500_Inf, DY_M50_ext2, WJets]#, DY_2Jets, W1Jet, W2Jet, W3Jet, W4Jet] DY_M50_mad, DY_M50_HT400_600, 


TTWToLNu    = ComponentContainer("TTWToLNu","/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19_ext1-v1/NANOAODSIM",0.2043)
#TTW_LO_ext  = ComponentContainer("TTW_LO_ext1","/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM",0.6105 )
#TTW_LO      = ComponentContainer("TTW_LO","/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v6-v1/NANOAODSIM", 0.6105 )    
#TTZ_LO_ext  = ComponentContainer("TTZ_LO_ext1", "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM",0.5297/0.692)
#TTZ_LO      = ComponentContainer("TTZ_LO", "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM", 0.5297/0.692)
TTZToLLNuNu = ComponentContainer("TTZToLLNuNu","/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19_ext1-v1/NANOAODSIM",0.2529)
TTZToQQ     = ComponentContainer("TTZToQQ","/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM",0.5297)
TTH_amc     = ComponentContainer("TTH_amc","/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM",0.5085*(1-0.577))
#TTH_pow     = ComponentContainer("TTH_pow","/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v6-v1/NANOAODSIM",0.5085*(1-0.577))
TTG         = ComponentContainer("TTGJets","/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM", 3.697)

ttV = [TTWToLNu, TTZToLLNuNu, TTZToQQ, TTH_amc, TTG]


tW_            = ComponentContainer('TW','/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19_ext1-v1/NANOAODSIM',35.6)
tbarW          = ComponentContainer('TbarW','/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19_ext1-v1/NANOAODSIM', 35.6)
#t_sch          = ComponentContainer('T_sch','/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19_ext1-v2/NANOAODSIM',(7.20+4.16)*0.108*3)
t_tbarch       = ComponentContainer('Tbar_tch','/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM',80.95)
t_tch          = ComponentContainer('T_tch','/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM',136.02)


ST = [tW_, tbarW, t_tch, t_tbarch] # t_sch, 



WWTo2L2Nu = ComponentContainer("WWTo2L2Nu","/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM",10.481)
#WW_DPS    = ComponentContainer("WW_DPS","/WWTo2L2Nu_DoubleScattering_13TeV-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM",1.921)
WZTo3LNu  = ComponentContainer("WZTo3LNu","/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM",4.666)
WZTo3LNu_ext  = ComponentContainer("WZTo3LNu_ext","/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19_ext1-v1/NANOAODSIM",4.666)
WZTo3LNu_pow  = ComponentContainer("WZTo3LNu_pow","/WZTo3LNu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19_ext1-v1/NANOAODSIM",4.452)

WZTo2L2Q  = ComponentContainer("WZTo2L2Q","/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM",5.60)
ZZTo2L2Q  = ComponentContainer('ZZTo2L2Q', '/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM',3.28)
ZZTo2Q2Nu = ComponentContainer('ZZTo2Q2Nu', '/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM',4.04)
ZZTo2L2Nu = ComponentContainer('ZZTo2L2Nu', '/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19_ext1-v1/NANOAODSIM',0.564)
ZZTo4L    = ComponentContainer('ZZTo4L', '/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19_ext1-v1/NANOAODSIM',1.256)
ZZTo4L_ext= ComponentContainer('ZZTo4L_ext', '/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19_ext2-v1/NANOAODSIM',1.256)

GGToZZTo2e2mu     = ComponentContainer('GluGluToContinToZZTo2e2mu'    ,  '/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM', 0.00319      )
GGToZZTo2e2nu     = ComponentContainer('GluGluToContinToZZTo2e2nu',  '/GluGluToContinToZZTo2e2nu_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM',0.00319        )
GGToZZTo2e2tau    = ComponentContainer('GluGluToContinToZZTo2e2tau'  ,'/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM',0.00319      )
GGToZZTo2mu2nu    = ComponentContainer('GluGluToContinToZZTo2mu2nu'  ,'/GluGluToContinToZZTo2mu2nu_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM',0.00319      )
GGToZZTo2mu2tau   = ComponentContainer('GluGluToContinToZZTo2mu2tau' ,'/GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM',0.00319)
GGToZZTo4e        = ComponentContainer('GluGluToContinToZZTo4e'      ,'/GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM',0.00159)
GGToZZTo4mu       = ComponentContainer('GluGluToContinToZZTo4mu'     ,'/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM',0.00159)
GGToZZTo4tau      = ComponentContainer('GluGluToContinToZZTo4tau', '/GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM',0.00159)

VH = ComponentContainer('VHToNonbb', '/VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM',0.9561)

VV = [WWTo2L2Nu, WZTo3LNu, WZTo3LNu_ext, WZTo3LNu_pow, WZTo2L2Q, ZZTo2L2Q, ZZTo2L2Nu, ZZTo2Q2Nu, ZZTo4L, ZZTo4L_ext, GGToZZTo2e2mu, GGToZZTo2e2nu, GGToZZTo2e2tau, GGToZZTo2mu2nu, GGToZZTo2mu2tau, GGToZZTo4e, GGToZZTo4mu, GGToZZTo4tau, VH] # WW_DPS, 


WWW =   ComponentContainer('WWW','/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19_ext1-v1/NANOAODSIM',0.2086)
WWZ =    ComponentContainer('WWZ','/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19_ext1-v1/NANOAODSIM',0.1651 )
WZZ =    ComponentContainer('WZZ','/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19_ext1-v1/NANOAODSIM',0.05565)
WZG =    ComponentContainer('WZG','/WZG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM',0.0412)
ZZZ =    ComponentContainer('ZZZ','/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19_ext1-v1/NANOAODSIM',0.01398)
ZG =    ComponentContainer('ZGTo2LG','/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19_ext1-v1/NANOAODSIM',1.)
WG =    ComponentContainer('WGToLNuG','/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM',1.)

VVV = [WWW, WWZ, WZZ, WZG, ZZZ, ZG, WG]

TTTT = ComponentContainer('TTTT','/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19_ext1-v1/NANOAODSIM', 0.009103)
tZq  = ComponentContainer('tZq_ll','/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19_ext1-v1/NANOAODSIM',0.0758)
TTZZ = ComponentContainer('TTZZ','/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19_ext1-v1/NANOAODSIM',0.001982)
TTZH = ComponentContainer('TTZH','/TTZH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19_ext1-v1/NANOAODSIM',0.001535)
TTWZ = ComponentContainer('TTWZ','/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19_ext1-v1/NANOAODSIM',0.001982)
TTWH = ComponentContainer('TTWH','/TTWH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19_ext1-v1/NANOAODSIM',0.001140)
TTHH = ComponentContainer('TTHH','/TTHH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19_ext1-v1/NANOAODSIM',0.0006666)
TTWW = ComponentContainer('TTWW','/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19_ext1-v1/NANOAODSIM',0.006977)

Rare = [tZq, TTZZ, TTZH, TTWZ, TTTT, TTWH, TTHH, TTWW]

samples = TT + V + ttV + ST + VV + VVV + Rare

for sample in samples:
    sample.options['isData'] = False
    sample.options['year']   = '2018'
    sample.name = sample.name + '_2018'
    sample.options['scan'] = None
    sample.options['isFastSim'] = False
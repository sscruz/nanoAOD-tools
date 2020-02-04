from PhysicsTools.NanoAODTools.postprocessing.datasets.componentContainer import  ComponentContainer



MuonEG=[
    ComponentContainer('MuonEG_Run2017B', '/MuonEG/Run2017B-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('MuonEG_Run2017C', '/MuonEG/Run2017C-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('MuonEG_Run2017D', '/MuonEG/Run2017D-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('MuonEG_Run2017E', '/MuonEG/Run2017E-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('MuonEG_Run2017F', '/MuonEG/Run2017F-Nano25Oct2019-v1/NANOAOD'),
    ]

DoubleMuon=[
    ComponentContainer('DoubleMuon_Run2017B', '/DoubleMuon/Run2017B-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('DoubleMuon_Run2017C', '/DoubleMuon/Run2017C-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('DoubleMuon_Run2017D', '/DoubleMuon/Run2017D-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('DoubleMuon_Run2017E', '/DoubleMuon/Run2017E-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('DoubleMuon_Run2017F', '/DoubleMuon/Run2017F-Nano25Oct2019-v1/NANOAOD')
    ]

DoubleElectron=[
    ComponentContainer('DoubleEG_Run2017B', '/DoubleEG/Run2017B-Nano25Oct2019-v1/NANOAOD'), 
    ComponentContainer('DoubleEG_Run2017C', '/DoubleEG/Run2017C-Nano25Oct2019-v1/NANOAOD'), 
    ComponentContainer('DoubleEG_Run2017D', '/DoubleEG/Run2017D-Nano25Oct2019-v1/NANOAOD'), 
    ComponentContainer('DoubleEG_Run2017E', '/DoubleEG/Run2017E-Nano25Oct2019-v1/NANOAOD'), 
    ComponentContainer('DoubleEG_Run2017F', '/DoubleEG/Run2017F-Nano25Oct2019-v1/NANOAOD'), 
]

MET=[
    ComponentContainer('MET_Run2017B', '/MET/Run2017B-Nano25Oct2019-v1/NANOAOD'), 
    ComponentContainer('MET_Run2017C', '/MET/Run2017C-Nano25Oct2019-v1/NANOAOD'), 
    ComponentContainer('MET_Run2017D', '/MET/Run2017D-Nano25Oct2019-v1/NANOAOD'), 
    ComponentContainer('MET_Run2017E', '/MET/Run2017E-Nano25Oct2019-v1/NANOAOD'), 
    ComponentContainer('MET_Run2017F', '/MET/Run2017F-Nano25Oct2019-v1/NANOAOD'), 
]



samples = MuonEG+DoubleMuon+DoubleElectron+MET#+Electron_noOverlapRemov  + SingleMuon+SingleElectron+

for sample in samples:
    sample.options['isData'] = True
    sample.options['year']   = '2017'
    sample.name = sample.name + '_2017'
    sample.options['scan'] = None
    sample.options['isFastSim'] = False

from PhysicsTools.NanoAODTools.postprocessing.datasets.componentContainer import  ComponentContainer



MuonEG = [
    ComponentContainer('MuonEG_Run2016B', '/MuonEG/Run2016B_ver2-Nano25Oct2019_ver2-v1/NANOAOD'),
    ComponentContainer('MuonEG_Run2016C', '/MuonEG/Run2016C-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('MuonEG_Run2016D', '/MuonEG/Run2016D-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('MuonEG_Run2016E', '/MuonEG/Run2016E-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('MuonEG_Run2016F', '/MuonEG/Run2016F-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('MuonEG_Run2016G', '/MuonEG/Run2016G-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('MuonEG_Run2016H', '/MuonEG/Run2016H-Nano25Oct2019-v1/NANOAOD'),
    ]
DoubleMuon = [
    ComponentContainer('DoubleMuon_Run2016B', '/DoubleMuon/Run2016B_ver2-Nano25Oct2019_ver2-v1/NANOAOD'),
    ComponentContainer('DoubleMuon_Run2016C', '/DoubleMuon/Run2016C-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('DoubleMuon_Run2016D', '/DoubleMuon/Run2016D-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('DoubleMuon_Run2016E', '/DoubleMuon/Run2016E-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('DoubleMuon_Run2016F', '/DoubleMuon/Run2016F-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('DoubleMuon_Run2016G', '/DoubleMuon/Run2016G-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('DoubleMuon_Run2016H', '/DoubleMuon/Run2016H-Nano25Oct2019-v1/NANOAOD'),
    ]
DoubleElectron = [
    ComponentContainer('DoubleEG_Run2016B', '/DoubleEG/Run2016B_ver2-Nano25Oct2019_ver2-v1/NANOAOD'),
    ComponentContainer('DoubleEG_Run2016C', '/DoubleEG/Run2016C-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('DoubleEG_Run2016D', '/DoubleEG/Run2016D-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('DoubleEG_Run2016E', '/DoubleEG/Run2016E-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('DoubleEG_Run2016F', '/DoubleEG/Run2016F-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('DoubleEG_Run2016G', '/DoubleEG/Run2016G-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('DoubleEG_Run2016H', '/DoubleEG/Run2016H-Nano25Oct2019-v1/NANOAOD'),
    ]

MET = [
    ComponentContainer('MET_Run2016B', '/MET/Run2016B_ver2-Nano25Oct2019_ver2-v1/NANOAOD'),
    ComponentContainer('MET_Run2016C', '/MET/Run2016C-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('MET_Run2016D', '/MET/Run2016D-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('MET_Run2016E', '/MET/Run2016E-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('MET_Run2016F', '/MET/Run2016F-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('MET_Run2016G', '/MET/Run2016G-Nano25Oct2019-v1/NANOAOD'),
    ComponentContainer('MET_Run2016H', '/MET/Run2016H-Nano25Oct2019-v1/NANOAOD'),
    ]



samples = MET+MuonEG+DoubleMuon+DoubleElectron # SingleMuon+SingleElectron+

for sample in samples:
    sample.options['isData'] = True
    sample.options['year']   = '2016'
    sample.name = sample.name + '_2016'
    sample.options['scan'] = None
    sample.options['isFastSim'] = False

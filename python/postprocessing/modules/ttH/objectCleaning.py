import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

import os
import itertools

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.tools     import deltaR
from PhysicsTools.NanoAODTools.postprocessing.modules.common.collectionSkimmer   import CollectionSkimmer
from PhysicsTools.NanoAODTools.postprocessing.modules.common.collectionMerger_v2 import CollectionMerger

_rootLeafType2rootBranchType = { 'UChar_t':'b', 'Char_t':'B', 'UInt_t':'i', 'Int_t':'I', 'Float_t':'F', 'Double_t':'D', 'ULong64_t':'l', 'Long64_t':'L', 'Bool_t':'O' }


class ObjectCleaning(Module):
    def __init__(self,
                 looseLeptonSelection      ,
                 FOLeptonSelection         , 
                 FOTauSelection            ,
                 jetSelection              ,
                 conePt                    ,
                 jetPts                    = [],
                 jetSel                    = {},
                 doJetSums                 = False,
                 cleanElectronsWithMuons   = 0.3,
                 cleanTausWithLooseLeptons = 0.3,
                 cleanJetsWithFOLeps       = True,
                 cleanJetsWithFOTaus       = True,
                 ):
        self.looseLeptonSelection      = looseLeptonSelection     
        self.FOLeptonSelection         = FOLeptonSelection        
        self.FOTauSelection            = FOTauSelection           
        self.jetSelection              = jetSelection             
        self.cleanElectronsWithMuons   = cleanElectronsWithMuons  
        self.cleanTausWithLooseLeptons = cleanTausWithLooseLeptons
        self.cleanJetsWithFOLeps       = cleanJetsWithFOLeps      
        self.cleanJetsWithFOTaus       = cleanJetsWithFOTaus      
        self.conePt                    = conePt
        #self.jetSel                    = jetSel
        #self.doJetSums                 = doJetSums
        #self.jetPts                    = jetPts

        self.systsJEC = {0:"_nom"  , 1:"_jesTotalUp", -1:"_jesTotalDown"}

        #self._helper_muonFO    = CollectionSkimmer("MuonFO","Muon", maxSize=20)
        #self._helper_elecFO    = CollectionSkimmer("ElecFO","Electron", maxSize=20)
        #self._helper_muonLoose = CollectionSkimmer("MuonLoose","Muon", maxSize=20)
        #self._helper_elecLoose = CollectionSkimmer("ElecLoose","Electron", maxSize=20)

        # self._helper_lepFO    = CollectionMerger("LepFO","Electron","Muon", maxSize=20)
        # self._helper_tausFO    = CollectionSkimmer("TausFO","Tau", maxSize=20)
        # self._helper_jetsSelec = CollectionSkimmer("JetSel","Jet", maxSize=20)
        # self._helper_lepLoose = CollectionMerger("LepLoose","Electron","Muon", maxSize=20)

        self._helpers = [ #self._helper_muonFO,
                          #self._helper_elecFO,
                          #self._helper_muonLoose,
                          #self._helper_elecLoose
                          #self._helper_tausFO,
                          #self._helper_jetsSelec,
                          #self._helper_lepFO,
                          #self._helper_lepLoose
                          ] 

    def beginJob(self):
        pass
    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self._in = inputTree
        for x in self._helpers: 
            x.initInputTree(inputTree)
            x.initOutputTree(wrappedOutputTree)

        # this should be removed in the future
        self.out = wrappedOutputTree
        _brlist = inputTree.GetListOfBranches()
        self.jetBranches = []; self.lepBranches = []; self.tauBranches = [] 
        branches = [( _brlist.At(i).GetName(), _brlist.At(i).FindLeaf(_brlist.At(i).GetName()).GetTypeName()) for i in xrange(_brlist.GetEntries())]
        # also checking if some branches were added in other modules 
        for branch in self.out._branches: 
            alreadyThere = False 
            for br2name, br2type in branches:
                if branch == br2name:
                    alreadyThere = True
            if not alreadyThere:
                branches.append( (branch, self.out._branches[branch].branch.FindLeaf(branch).GetTypeName()) ) 

        for brname, brtype in branches:
            # Jet type 
            if brname.startswith('Jet_'): 
                self.jetBranches.append( (brname.replace("Jet_",""), brtype))

            # Lepton type 
            if brname.startswith('Electron_'): 
                self.lepBranches.append( (brname.replace("Electron_",""), brtype))
            if brname.startswith('Muon_'): 
                if (brname.replace("Muon_",""), brtype) in self.lepBranches: continue
                self.lepBranches.append( (brname.replace("Muon_",""), brtype) )

            # Tau type
            if brname.startswith('Tau_'): 
                self.tauBranches.append( (brname.replace("Tau_",""), brtype))
            
        # build the collections
        for branch in self.jetBranches:
            self.out.branch('JetSel_%s'%branch[0], _rootLeafType2rootBranchType[branch[1]], lenVar="nJetSel")
        for branch in self.lepBranches:
            self.out.branch('LepFO_%s'%branch[0], _rootLeafType2rootBranchType[branch[1]], lenVar="nLepFO")
        for branch in self.lepBranches:
            self.out.branch('LepLoose_%s'%branch[0], _rootLeafType2rootBranchType[branch[1]], lenVar="nLepLoose")
        for branch in self.tauBranches:
            self.out.branch('TausFO_%s'%branch[0], _rootLeafType2rootBranchType[branch[1]], lenVar="nTausFO")

        self.out.branch('LepFO_conept'   ,'F', lenVar="nLepFO")
        self.out.branch('LepLoose_conept','F', lenVar="nLepLoose")
        self.out.branch('LepFO_jetBTagDeepCSV'   ,'F', lenVar="nLepFO")
        self.out.branch('LepLoose_jetBTagDeepCSV','F', lenVar="nLepLoose")


        # for pt in self.jetPts:
        #     for var in self.systsJEC:
        #         for sel in self.jetSel:
        #             self.out.branch( 'n%s%d'%(sel, int(pt))           + self.systsJEC[var], 'i')
        #         if self.doJetSums:
        #             self.out.branch( 'ht%d'%(int(pt))  + self.systsJEC[var] ,'F')
        #             self.out.branch( 'mht%d'%(int(pt))  + self.systsJEC[var],'F')

                
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

#    def initReaders(self):
#        for x in self._helpers:
#            for var in x._vars: 
#                setattr(self, var, self._in.arrayReader(x._iprefix + var))

    def analyze(self, event):
#        while any([x.initEvent(event) for x in self._helpers]):
#            x.initEvent(event)

            
            
        muon   = [ o for o in Collection(event, 'Muon')     ]
        elec   = [ o for o in Collection(event, 'Electron') ]
        taus   = [ o for o in Collection(event, 'Tau')      ]
        jets   = [ o for o in Collection(event, 'Jet')      ]

        muonLoose = filter(self.looseLeptonSelection, muon)
        elecLoose = filter(self.looseLeptonSelection, elec)

        
        # this could be external to the code somehow
        for lep in muonLoose+elecLoose:
            setattr(lep, 'conept', self.conePt(lep))
            setattr(lep, 'jetBTagDeepCSV', 0 if lep.jetIdx < 0 else jets[lep.jetIdx].btagDeepB)

        for jet in jets:
            if not hasattr(jet,'pt_nom'): 
                setattr(jet, 'pt_nom',jet.pt)


        
        # clean loose electrons with loose muons
        if self.cleanElectronsWithMuons: 
            toRemove_elecLoose = [] 
            for el in elecLoose:
                for mu in muonLoose:
                    if deltaR(el,mu) < self.cleanElectronsWithMuons: 
                        toRemove_elecLoose.append(el)
                        break # breaking just in case three leptons are quite close
            for el in toRemove_elecLoose: elecLoose.remove(el)


        # we define FOs on top of loose leptons
        muonFO    = filter(self.FOLeptonSelection, muonLoose)
        elecFO    = filter(self.FOLeptonSelection, elecLoose)
        tausFO    = filter(self.FOTauSelection,    taus)
        jetsSelec = filter(self.jetSelection,   jets)

        if len(muonFO)+len(elecFO) < 2: return False

        # we clean taus from loose leptons
        toRemove_tausFO = [] 
        if self.cleanTausWithLooseLeptons:
            for tau in tausFO:
                for lep in elecLoose+muonLoose:
                    if deltaR(tau,lep) < self.cleanTausWithLooseLeptons: 
                        toRemove_tausFO.append(tau)
                        break
        for tau in toRemove_tausFO: tausFO.remove(tau)

        # we clean jets from FO taus and leps. Here no deltaR but using the matching
        toRemove_jetsSelec = []
        if self.cleanJetsWithFOTaus:
            for tau in tausFO:
                if tau.jetIdx > -1 and jets[tau.jetIdx] in jetsSelec:
                    toRemove_jetsSelec.append( jets[tau.jetIdx] ) 
                    break
        for jet in toRemove_jetsSelec: jetsSelec.remove(jet)

        # we clean jets from FO taus and leps. Here no deltaR but using the matching
        toRemove_jetsSelec = []
        if self.cleanJetsWithFOLeps:
            for jet in jetsSelec:
                for i in range(1,3):
                    if getattr(jet,'electronIdx%d'%i) > -1:
                        if elec[getattr(jet,'electronIdx%d'%i)] in elecFO: 
                            toRemove_jetsSelec.append( jet ) 
                            break
                    if getattr(jet,'muonIdx%d'%i) > -1:
                        if muon[getattr(jet,'muonIdx%d'%i)] in muonFO: 
                            toRemove_jetsSelec.append( jet ) 
                            break
        for jet in toRemove_jetsSelec: jetsSelec.remove(jet)

        # everything that is commented here should be for the c++ impl
        # # writing out taus and jets
        # for x in tausFO:    
        #     self._helper_tausFO   ._impl.push_back(taus.index(x))
        # for x in jetsSelec: self._helper_jetsSelec._impl.push_back(jets.index(x))

        # # moving into tuples of (Collection index, pt, index). 
        # muonFO_idx = [(1, x.pt, muon.index(x)) for x in muonFO]
        # elecFO_idx = [(0, x.pt, elec.index(x)) for x in elecFO]

        # muonLoose_idx = []; elecLoose_idx = [] 
        # for x in  muonLoose:
        #     if x not in muonFO: muonLoose_idx.append( (1, x.pt, muon.index(x)) )
        # for x in  elecLoose:
        #     if x not in elecFO: elecLoose_idx.append( (0, x.pt, elec.index(x)) )

        # lepFO_idx    = muonFO_idx + elecFO_idx      ; lepFO_idx.sort(key = lambda x : x[1], reverse=True)
        # lepLoose_idx = muonLoose_idx + elecLoose_idx; lepLoose_idx.sort(key = lambda x : x[1], reverse=True)

        # for x in lepFO_idx    : self._helper_lepFO   ._impl.push_back(x[2],x[0])
        # for x in lepLoose_idx : self._helper_lepLoose._impl.push_back(x[2],x[0])
        

        jetsSelec.sort(key = lambda x : x.pt_nom, reverse=True)
        for branch in self.jetBranches:
            out = [] 
            branchName = branch[0]
            for  obj in jetsSelec: 
                out.append( getattr(obj, branchName ) )
            self.out.fillBranch("JetSel_%s"%branchName, out)
            
        for branch in self.tauBranches:
            out = [] 
            branchName = branch[0]
            for  obj in tausFO: 
                out.append( getattr(obj, branchName) ) 
            self.out.fillBranch("TausFO_%s"%branchName, out)
        

        lepFO = muonFO+elecFO
        lepFO.sort(key = lambda x : x.pt, reverse=True)
        for branch in self.lepBranches+[['conept'],['jetBTagDeepCSV']]:
            out = [] 
            branchName = branch[0]
            for obj in lepFO:
                out.append( getattr(obj, branchName) if hasattr(obj,branchName) else 0)
            self.out.fillBranch("LepFO_%s"%branchName, out)


        lepLoose = muonLoose+elecLoose
        lepLoose.sort(key = lambda x : x.pt, reverse=True)
        for branch in self.lepBranches+[['conept'],['jetBTagDeepCSV']]:
            out = [] 
            branchName = branch[0]
            for obj in lepLoose:
                if obj in lepFO: continue
                out.append( getattr(obj, branchName) if hasattr(obj,branchName) else 0)
            self.out.fillBranch("LepLoose_%s"%branchName, out)


        
        # if self.doJetSums:
        #     _mht  = {}; _ht = {}
        #     for pt in self.jetPts:
        #         for var in self.systsJEC:
        #             _mht['%s%d'%(var,int(pt))] = ROOT.TLorentzVector()
        #             _ht ['%s%d'%(var,int(pt))] = 0
        #             for l in lepFO+tausFO:
        #                 vl = ROOT.TLorentzVector(); vl.SetPtEtaPhiM( l.pt, 0, l.phi, 0)
        #                 _mht['%s%d'%(var,int(pt))] = _mht['%s%d'%(var,int(pt))] - vl
        #                 _ht ['%s%d'%(var,int(pt))] = _ht ['%s%d'%(var,int(pt))] + l.pt


        # allret = {} 
        # for pt in self.jetPts:
        #     for var in self.systsJEC:
        #         for sel in self.jetSel:
        #             namJ = 'n%s%d'%(sel, int(pt)) + self.systsJEC[var]       ;  allret[namJ] = 0
                    

        # for pt in self.jetPts:
        #     for var in self.systsJEC:
        #         for jet in jetsSelec:
        #             for sel in self.jetSel:
        #                 if not self.jetSel[sel](jet): continue
        #                 if hasattr(jet, 'pt%s'%self.systsJEC[var]) and getattr(jet,'pt%s'%self.systsJEC[var]) > pt:
        #                     namJ = 'n%s%d'%(sel, int(pt)) + self.systsJEC[var]
        #                     allret[namJ] = allret[namJ] + 1
        #                     vj = ROOT.TLorentzVector(); vj.SetPtEtaPhiM( jet.pt, 0, jet.phi, 0)
        #                     if abs(jet.eta) > 2.4: continue
        #                     _mht['%s%d'%(var,int(pt))] = _mht['%s%d'%(var,int(pt))] - vj
        #                     _ht ['%s%d'%(var,int(pt))] = _ht ['%s%d'%(var,int(pt))] + jet.pt
        #         allret['ht%d'%(int(pt))  + self.systsJEC[var]]  = _ht ['%s%d'%(var,int(pt))]
        #         allret['mht%d'%(int(pt))  + self.systsJEC[var]] = _mht['%s%d'%(var,int(pt))].Pt()
       
        # for key, val in allret.iteritems():
        #     self.out.fillBranch(key, val)
                    

        return True

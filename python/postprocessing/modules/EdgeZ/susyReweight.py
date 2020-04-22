import ROOT
import os
import numpy as np
ROOT.PyConfig.IgnoreCommandLineOptions = True
import array

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.modules.EdgeZ.edgeFriends import _susyEdgeTight, _susyEdgeLoose
from PhysicsTools.NanoAODTools.postprocessing.tools import deltaR, deltaPhi

def isInDecayOf( daught, mother, gens):
    isIn = False
    idx = gens.index(daught)
    while (idx > -1): 
        if idx != gens.index(mother): 
            idx = gens[idx].genPartIdxMother # mother is not the mother of daught, trying with the mother of daught
        else: 
            isIn = True
            break
    return isIn

def getRightParentage( gen, gens): 
    parentage = []
    idx = gens.index(gen)

    while (idx > -1):
        if abs(gens[idx].pdgId) == 6: return True
        if abs(gens[idx].pdgId) == 23: return True
        if abs(gens[idx].pdgId) == 24: return True
        if abs(gens[idx].pdgId) == 25: return True
        if abs(gens[idx].pdgId) > 99999: return True
        idx = gens[idx].genPartIdxMother
    return False

class susyReweight(Module):
    def __init__(self, model):
        self.model = model
        self.part1 = -1
        self.part2 = -1
        if self.model == "TChiWZ" or self.model == "TChiZZ" or self.model == "TChiHZ": 
            self.part1 = [1000023]
            self.part2 = [1000022]
            if self.model == "TChiWZ":
                self.partpt1 = [1000024,-1000024]
                self.partpt2 = [1000023]
            elif self.model in ["TChiZZ","TChiHZ"]:
                self.partpt1 = [1000025]
                self.partpt2 = [1000023]
                
        elif self.model == "T6bb": 
            self.part1 = [1000005]
            self.part2 = [1000023]
        elif self.model == "T5ZZ":
            self.part1 = [1000021]
            self.part2 = [1000022]
        elif self.model == "TSlep":
            self.part1 = [2000013,1000013,2000011,1000011]
            self.part2 = [1000022]
            self.partpt1 = [2000013,1000013,2000011,1000011]
            self.partpt2 = [-2000013,-1000013,-2000011,-1000011]
            
        else:
            raise RuntimeError("Unknown model %s"%self.model)

        self.sumWeights = {} 
        self.sumWeightsISR = {} 
        self.sumWeightsISRUp = {} 
        self.sumWeightsISRDn = {} 
    def beginJob(self):
	pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch( 'GenSusyMScan1_mass', 'F')
        self.out.branch( 'GenSusyMScan2_mass', 'F')
        self.out.branch( 'genWeight_isrWeight', 'F')
        self.out.branch( 'genWeight_isrWeight_up', 'F')
        self.out.branch( 'genWeight_isrWeight_dn', 'F')

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        outputFile.cd()
        runs_susy = ROOT.TTree("Runs_SUSY","Runs_SUSY")
        branches = []; branchesISR = []; branchesISRUp = []; branchesISRDn = []; 
        for point in self.sumWeights:
            branches.append( array.array( 'f', [self.sumWeights[point]]) ) 
            branchesISR.append( array.array( 'f', [self.sumWeightsISR[point]]) ) 
            branchesISRUp.append( array.array( 'f', [self.sumWeightsISRUp[point]]) ) 
            branchesISRDn.append( array.array( 'f', [self.sumWeightsISRDn[point]]) ) 
            runs_susy.Branch('sumWeights_%d_%d'%(point[0], point[1]), branches[-1], 'sumWeights_%d_%d/F'%(point[0], point[1])) # just for debug
            runs_susy.Branch('sumWeights_isr_%d_%d'%(point[0], point[1]), branchesISR[-1], 'sumWeights_isr_%d_%d/F'%(point[0], point[1]))
            runs_susy.Branch('sumWeights_isrUp_%d_%d'%(point[0], point[1]), branchesISRUp[-1], 'sumWeights_isrUp_%d_%d/F'%(point[0], point[1]))
            runs_susy.Branch('sumWeights_isrDn_%d_%d'%(point[0], point[1]), branchesISRDn[-1], 'sumWeights_isrDn_%d_%d/F'%(point[0], point[1]))
        runs_susy.Fill()
        runs_susy.Write()

    def doStrongISRRw(self,event):
        # https://indico.cern.ch/event/592621/contributions/2398559/attachments/1383909/2105089/16-12-05_ana_manuelf_isr.pdf
        nisr = 0 
        leps = [ x for x in Collection(event, "Electron")] + [ x for x in Collection(event, "Muon")]
        leps = filter( lambda x : _susyEdgeLoose(x, event.year) and _susyEdgeTight(x,event.year), leps)
        jets = [ x for x in Collection(event, "Jet")]
        gens = [ x for x in Collection(event, "GenPart")]
        
        jets = filter( lambda x : x.pt > 35 and abs(x.eta) < 2.4, jets)
        for jet in jets: 
            matched = False
            skip = False
            for lep in leps:
                if deltaR(jet,lep) < 0.4: 
                    skip = True
                    break
            if skip: continue
            for gen in gens:
                if abs(gen.pdgId) > 5 or gen.status != 23: continue
                if gen.genPartIdxMother < 0: continue 
                if deltaR( jet, gen) > 0.3: continue
                if not getRightParentage( gen, gens): continue
                matched = True
                break
                
            if not matched: 
                nisr = nisr + 1 
        
        if nisr == 0   : return (1,0         ) 
        elif nisr == 1 : return (0.920, 0.04 )
        elif nisr == 2 : return (0.821, 0.09 )
        elif nisr == 3 : return (0.715, 0.143)
        elif nisr == 4 : return (0.662, 0.169)
        elif nisr == 5 : return (0.561, 0.219)
        elif nisr >= 6 : return (0.511, 0.244)
        else: 
            print nisr
            raise RuntimeError("WTF") 
    
    def doEwkISRRw(self,event):
        # https://indico.cern.ch/event/616816/contributions/2489809/attachments/1418579/2174166/17-02-22_ana_isr_ewk.pdf
        gens = [ x for x in Collection(event, "GenPart")]
        gen1 = [ x for x in gens if x.status == 22 and x.pdgId in self.partpt1 ]
        gen2 = [ x for x in gens if x.status == 22 and x.pdgId in self.partpt2 ]
        if len(gen1) != 1 or len(gen2) != 1: 
            for gen in gens:
                if gen.status != 22: continue
                print gen.pdgId
            raise RuntimeError("Theres more or less than two produced sparticles")
        
        pt = (gen1[0].p4()+gen2[0].p4()).Pt()

        if    pt < 50: return 1,0
        elif  pt > 50 and pt <= 100 : return 1.052, 0.052
        elif pt > 100 and pt <= 150 : return 1.179, 0.179 
        elif pt > 150 and pt <= 200 : return 1.150, 0.150
        elif pt > 200 and pt <= 300 : return 1.057, 0.057
        elif pt > 300 and pt <= 400 : return 1.000, 0.000
        elif pt > 400 and pt <= 600 : return 0.912, 0.088 
        elif pt > 600              : return 0.783, 0.217
        else: 
            print pt 
            raise RuntimeError("WTF")

    def analyze(self, event):
        genparts = Collection(event, "GenPart")
        mass1 = -1; mass2 = -1
        for gen in genparts:
            if gen.pdgId in self.part1:
                mass1 = gen.mass
            if gen.pdgId in self.part2:
                mass2 = gen.mass
        if mass1 < 0 or mass2 < 0:
            print "Sparticles not found for model %s and particles %s ; %s"%(self.model, ','.join(map(lambda x :  '%d'%x, self.part1)), ','.join(map(lambda x :  '%d'%x, self.part1)))
            print 'Available pdgIds are', ','.join(['%d'%x.pdgId for x in genparts])
            raise RuntimeError
                
        # ISR reweighthing... Cleaning jets here as well, i hope its not too slow
        if self.model in ['T5ZZ', 'T6bb'] : isrW, isrWUp = self.doStrongISRRw(event)
        elif self.model in ['TChiWZ', 'TChiZZ','TChiHZ','TSlep']: isrW, isrWUp = self.doEwkISRRw(event)
        if (mass1, mass2) not in self.sumWeights: 
            self.sumWeights[(mass1,mass2)] = event.genWeight 
            self.sumWeightsISR[(mass1,mass2)] = event.genWeight*isrW
            self.sumWeightsISRUp[(mass1,mass2)] = event.genWeight*isrWUp
            self.sumWeightsISRDn[(mass1,mass2)] = event.genWeight*(isrW - (isrWUp-isrW))
        else:
            self.sumWeights[(mass1,mass2)]+= event.genWeight
            self.sumWeightsISR[(mass1,mass2)]+= event.genWeight*isrW
            self.sumWeightsISRUp[(mass1,mass2)] += event.genWeight*isrWUp
            self.sumWeightsISRDn[(mass1,mass2)] += event.genWeight*(isrW - (isrWUp-isrW))

        self.out.fillBranch("GenSusyMScan1_mass",mass1)
        self.out.fillBranch("GenSusyMScan2_mass",mass2)
        self.out.fillBranch('genWeight_isrWeight'   , event.genWeight*isrW  )
        self.out.fillBranch('genWeight_isrWeight_up', event.genWeight*isrWUp)
        self.out.fillBranch('genWeight_isrWeight_dn', event.genWeight*(isrW - (isrWUp-isrW)))
        return True
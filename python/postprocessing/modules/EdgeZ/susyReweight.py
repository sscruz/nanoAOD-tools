import ROOT
import os
import numpy as np
ROOT.PyConfig.IgnoreCommandLineOptions = True
import array

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class susyReweight(Module):
    def __init__(self, model):
        self.model = model
        self.part1 = -1
        self.part2 = -1
        if self.model == "TChiWZ" or self.model == "TChiZZ" or self.model == "TChiHZ": 
            self.part1 = 1000023
            self.part2 = 1000022
        elif self.model == "T6bb":
            self.part1 = 1000005
            self.part2 = 1000023
        elif self.model == "T5ZZ":
            self.part1 = 1000021
            self.part2 = 1000022
        else:
            raise RuntimeError("Unknown model %s"%self.model)

        self.sumWeights = {} 
    def beginJob(self):
	pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch( 'GenSusyMScan1_mass', 'F')
        self.out.branch( 'GenSusyMScan2_mass', 'F')

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        outputFile.cd()
        runs_susy = ROOT.TTree("Runs_SUSY","Runs_SUSY")
        branches = [] 
        for point in self.sumWeights:
            branches.append( array.array( 'f', [self.sumWeights[point]]) ) 
            runs_susy.Branch('sumWeights_%d_%d'%(point[0], point[1]), branches[-1], 'sumWeights_%d_%d/F'%(point[0], point[1]))
        runs_susy.Fill()
        runs_susy.Write()

    def analyze(self, event):
        genparts = Collection(event, "GenPart")
        mass1 = -1; mass2 = -1
        for gen in genparts:
            if gen.pdgId == self.part1:
                mass1 = gen.mass
            if gen.pdgId == self.part2:
                mass2 = gen.mass
        if mass1 < 0 or mass2 < 0:
            raise RuntimeError("Sparticles not found for model %s and particles %d, %d"%(self.model, self.part1, self.part2))

        if (mass1, mass2) not in self.sumWeights: 
            self.sumWeights[(mass1,mass2)] = event.genWeight 
        else:
            self.sumWeights[(mass1,mass2)]+= event.genWeight

        self.out.fillBranch("GenSusyMScan1_mass",mass1)
        self.out.fillBranch("GenSusyMScan2_mass",mass2)
        
        return True

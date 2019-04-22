import ROOT
import math, os,re
import numpy as np
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.tools import matchObjectCollection, matchObjectCollectionMultiple
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.JetReCalibrator import JetReCalibrator

class jetRecalib(Module):
    def __init__(self,  globalTag, jetType = "AK4PFchs"):

        if "AK4" in jetType : 
            self.jetBranchName = "Jet"
        elif "AK8" in jetType :
            self.jetBranchName = "FatJet"
            self.subJetBranchName = "SubJet"
        else:
            raise ValueError("ERROR: Invalid jet type = '%s'!" % jetType)
        self.rhoBranchName = "fixedGridRhoFastjetAll"
        self.lenVar = "n" + self.jetBranchName
        self.metBranchName = "MET"

        self.jesInputFilePath = os.environ['CMSSW_BASE'] + "/src/PhysicsTools/NanoAODTools/data/jme/"

        self.jetReCalibrator = JetReCalibrator(globalTag, jetType , True, self.jesInputFilePath, calculateSeparateCorrections = False, calculateType1METCorrection  = False)
	
        # load libraries for accessing JES scale factors and uncertainties from txt files
        for library in [ "libCondFormatsJetMETObjects", "libPhysicsToolsNanoAODTools" ]:
            if library not in ROOT.gSystem.GetLibraries():
                print("Load Library '%s'" % library.replace("lib", ""))
                ROOT.gSystem.Load(library)

    def beginJob(self):
	pass

    def endJob(self):
	pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("%s_pt_nom" % self.jetBranchName, "F", lenVar=self.lenVar)
        self.out.branch("%s_pt_nom"%self.metBranchName , "F")
        self.out.branch("%s_phi_nom"%self.metBranchName, "F")
            
                        
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        jets = Collection(event, self.jetBranchName )
        met = Object(event, "%s"%self.metBranchName) 

        jets_pt_nom = []
        ( met_px,         met_py         ) = ( met.pt*math.cos(met.phi), met.pt*math.sin(met.phi) )
        ( met_px_nom, met_py_nom ) = ( met_px, met_py )
        met_px_nom = met_px
        met_py_nom = met_py
                
        rho = getattr(event, self.rhoBranchName)
        
        for jet in jets:
	    jet_pt=jet.pt
	    jet_pt = self.jetReCalibrator.correct(jet,rho)
            jet_pt_nom           = jet_pt # don't smear resolution in data
            if jet_pt_nom < 0.0:
                jet_pt_nom *= -1.0
            jets_pt_nom    .append(jet_pt_nom)
            if jet_pt_nom > 15.:
                jet_cosPhi = math.cos(jet.phi)
                jet_sinPhi = math.sin(jet.phi)
                met_px_nom = met_px_nom - (jet_pt_nom - jet.pt)*jet_cosPhi
                met_py_nom = met_py_nom - (jet_pt_nom - jet.pt)*jet_sinPhi
        self.out.fillBranch("%s_pt_nom" % self.jetBranchName, jets_pt_nom)
        self.out.fillBranch("%s_pt_nom" %self.metBranchName, math.sqrt(met_px_nom**2 + met_py_nom**2))
        self.out.fillBranch("%s_phi_nom"%self.metBranchName, math.atan2(met_py_nom, met_px_nom))        

        return True


# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

jetRecalib2017B = lambda : jetRecalib("Fall17_17Nov2017B_V32_DATA")
jetRecalib2017C = lambda : jetRecalib("Fall17_17Nov2017C_V32_DATA")
jetRecalib2017DE = lambda : jetRecalib("Fall17_17Nov2017DE_V32_DATA")
jetRecalib2017F = lambda : jetRecalib("Fall17_17Nov2017F_V32_DATA")

jetRecalib2018B = lambda : jetRecalib("Autumn18_RunB_V8_DATA")
jetRecalib2018C = lambda : jetRecalib("Autumn18_RunC_V8_DATA")
jetRecalib2018D = lambda : jetRecalib("Autumn18_RunD_V8_DATA")
jetRecalib2018A = lambda : jetRecalib("Autumn18_RunA_V8_DATA")



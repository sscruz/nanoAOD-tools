import ROOT 
import os

from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class TriggerBitFilter(Module):
    def __init__(self, triggers=[], vetotriggers=[]):
        self.triggers = triggers
        self.vetotriggers = vetotriggers
        if "/hasfiredtriggers_cc.so" not in ROOT.gSystem.GetLibraries():
            ROOT.gROOT.ProcessLine(".L %s/src/PhysicsTools/NanoAODTools/data/hasfiredtriggers.cc+O" % os.environ['CMSSW_BASE'])


    def beginJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def _fires( self, ev, path):
        if not hasattr(ev,path): return False
        if ev.run == 1:  # is MC   
            return getattr( ev,path )
        return getattr(ROOT, 'fires_%s_%d'%(path,ev.year))( ev.run, getattr(ev,path))


    def analyze(self, event):
        # if no triggers are required, vetos are also not applied 
        if len(self.triggers) == 0: return True
        
        passesTrigger = False; passesVeto = True

        for trig in self.triggers:
            if self._fires(event,trig):
                passesTrigger = True
 
        if not passesTrigger: 
            return False

        for trig in self.vetotriggers:
            if self._fires(event,trig): 
                return False
        return True
        

triggerBitFilter = lambda x :  TriggerBitFilter()

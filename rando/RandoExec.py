
import sys

from graph_locations import locations as graphLocations
from rando.Restrictions import Restrictions
from rando.RandoServices import RandoServices
from rando.GraphBuilder import GraphBuilder
from rando.RandoSetup import RandoSetup
from rando.Filler import FrontFiller
from rando.FillerProgSpeed import FillerProgSpeed, FillerProgSpeedChozoSecondPhase
from rando.FillerRandom import FillerRandom, FillerRandomSpeedrun
from rando.Chozo import ChozoFillerFactory, ChozoWrapperFiller
from vcr import VCR

# entry point for rando execution ("randomize" method)
class RandoExec(object):
    def __init__(self, seedName, vcr):
        self.errorMsg = ""
        self.seedName = seedName
        self.vcr = vcr

    def getFillerFactory(self, progSpeed):
        if progSpeed == "basic":
            return lambda graphSettings, graph, restr, cont: FrontFiller(graphSettings.startAP, graph, restr, cont)
        elif progSpeed == "speedrun":
            return lambda graphSettings, graph, restr, cont: FillerRandomSpeedrun(graphSettings, graph, restr, cont)
        else:
            return lambda graphSettings, graph, restr, cont: FillerProgSpeed(graphSettings, graph, restr, cont)

    def createFiller(self, randoSettings, graphSettings, container):
        fact = self.getFillerFactory(randoSettings.progSpeed)
        if self.restrictions.split != "Chozo":
            return fact(graphSettings, self.areaGraph, self.restrictions, container)
        else:
            if randoSettings.progSpeed in ['basic', 'speedrun']:
                secondPhase = lambda graphSettings, graph, restr, cont, prog: FillerRandom(graphSettings.startAP, graph, restr, cont, diffSteps=100)
            else:
                secondPhase = lambda graphSettings, graph, restr, cont, prog: FillerProgSpeedChozoSecondPhase(graphSettings.startAP, graph, restr, cont)
            chozoFact = ChozoFillerFactory(graphSettings, self.areaGraph, self.restrictions, fact, secondPhase)
            return ChozoWrapperFiller(randoSettings, container, chozoFact)

    # processes settings to :
    # - create Restrictions and GraphBuilder objects
    # - create graph and item loc container using a RandoSetup instance: in area rando, if it fails, iterate on possible graph layouts
    # - create filler based on progression speed and run it
    # return (isStuck, itemLocs, progItemLocs)
    def randomize(self, randoSettings, graphSettings):
        self.restrictions = Restrictions(randoSettings)
        graphBuilder = GraphBuilder(graphSettings)
        container = None
        i = 0
        attempts = 500 if graphSettings.areaRando else 1
        while container is None and i < attempts:
            self.areaGraph = graphBuilder.createGraph()
            services = RandoServices(self.areaGraph, self.restrictions)
            setup = RandoSetup(graphSettings, graphLocations, services)
            container = setup.createItemLocContainer()
            if container is None:
                sys.stdout.write('*')
                sys.stdout.flush()
                i += 1
        if container is None:
            if graphSettings.areaRando:
                self.errorMsg = "Could not find an area layout with these settings"
            else:
                self.errorMsg = "Unable to process settings"
            return (True, [], [])
        graphBuilder.escapeGraph(container, self.areaGraph, randoSettings.maxDiff)
        self.areaGraph.printGraph()
        filler = self.createFiller(randoSettings, graphSettings, container)
        vcr = VCR(self.seedName, 'rando') if self.vcr == True else None
        ret = filler.generateItems(vcr=vcr)
        self.errorMsg = filler.errorMsg
        return ret
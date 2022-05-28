from bcdebug import debug
import App
from Custom.QBautostart.Libs.Races import Races
from Custom.QBautostart.Libs.LibConstruct import Construct

CONSTRUCT_SHIP = "ships.FedConstOpen"
RACE = "Federation"
lShipsToConstruct = [
	"FedOutpost",
	"FedStarbase",
	"Starbase220",
	"StarBase329",
	"DryDock",
	"FedStarbase",
	"pulsemine",
	"torpedomine",
	"CN_FedStarbase",
]

dConstructors = {}


def StartConstruction(pConstructionShip):
        debug(__name__ + ", StartConstruction")
        global dConstructors
        
        # go
        dConstructors[pConstructionShip.GetName()] = Construct(pConstructionShip, RACE, lShipsToConstruct, None, iIncConstructionPower = 10, iNumParallelConstructions = 4, bIsShip = 1, bUseRaceNames = 0)

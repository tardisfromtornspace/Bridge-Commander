from bcdebug import debug
import App
from Custom.QBautostart.Libs.Races import Races
from Custom.QBautostart.Libs.LibConstruct import Construct

CONSTRUCT_SHIP = "ships.EAExplorer"
RACE = "Federation"
lShipsToConstruct = [
	"B5JumpgateClosed",
]

dConstructors = {}


def StartConstruction(pConstructionShip):
        debug(__name__ + ", StartConstruction")
        global dConstructors
        
        # go
        dConstructors[pConstructionShip.GetName()] = Construct(pConstructionShip, RACE, lShipsToConstruct, None, iIncConstructionPower = 100, iNumParallelConstructions = 1, bIsShip = 1, bUseRaceNames = 0)

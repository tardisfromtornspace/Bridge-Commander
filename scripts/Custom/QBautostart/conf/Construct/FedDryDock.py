from bcdebug import debug
import App
from Custom.QBautostart.Libs.Races import Races
from Custom.QBautostart.Libs.LibConstruct import Construct

CONSTRUCT_SHIP = "ships.DryDock"
RACE = "Federation"

dConstructors = {}


def RemoveFromList(lList, toRemove):
        debug(__name__ + ", RemoveFromList")
        if toRemove in lList:
                lList.remove(toRemove)
        


# 1. Create a new Ship (race of construction ship, random ship), Place it inside and set its Hardpoints to 0 + Epsilon
# 2. Create Loops(class-loop!) set increases the ships HP points
# 3. When all Hardpoints are at 100%, let the ship fly out of the dock, set AI
# 4. Build a new ship
def StartConstruction(pConstructionShip):
        debug(__name__ + ", StartConstruction")
        global dConstructors
       
        sSetName = pConstructionShip.GetContainingSet().GetName()
        sConstructionLocation = pConstructionShip.GetName() + " Constructing Location"
        # add all Fed Ships to construct
        lShipsToConstruct = Races[RACE].GetShips()
        # remove some shuttles etc
        RemoveFromList(lShipsToConstruct, "MvamPrometheusVentral")
        RemoveFromList(lShipsToConstruct, "MvamPrometheusDorsal")
        RemoveFromList(lShipsToConstruct, "MvamPrometheusSaucer")
        RemoveFromList(lShipsToConstruct, "GalaxySaucer")
        RemoveFromList(lShipsToConstruct, "GalaxyStardrive")
        RemoveFromList(lShipsToConstruct, "Shuttle")
        RemoveFromList(lShipsToConstruct, "type9")
        RemoveFromList(lShipsToConstruct, "Type11")
        RemoveFromList(lShipsToConstruct, "deltaflyer")
        RemoveFromList(lShipsToConstruct, "sovereignyacht")
        RemoveFromList(lShipsToConstruct, "sovereignyachtwarp")
        RemoveFromList(lShipsToConstruct, "pulsemine")
        RemoveFromList(lShipsToConstruct, "torpedomine")
        # old ships
        RemoveFromList(lShipsToConstruct, "Ambassador")
        RemoveFromList(lShipsToConstruct, "EnterpriseNCC1701")
        RemoveFromList(lShipsToConstruct, "Miranda")
        RemoveFromList(lShipsToConstruct, "ExcelsiorP81")
        RemoveFromList(lShipsToConstruct, "C2excelsiorII")
        
        # Position
        kThis = App.Waypoint_Create(sConstructionLocation, sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslate(pConstructionShip.GetWorldLocation())
        kForward = App.TGPoint3()
        kForward.Set(pConstructionShip.GetWorldForwardTG())
        kUp = App.TGPoint3()
        kUp.Set(pConstructionShip.GetWorldUpTG())
        kThis.AlignToVectors(kForward, kUp)
        kThis.Update(0)
        
        # go
        dConstructors[pConstructionShip.GetName()] = Construct(pConstructionShip, RACE, lShipsToConstruct, sConstructionLocation, iIncConstructionPower = 10, iNumParallelConstructions = 8)
	dConstructors[pConstructionShip.GetName()].SetMode("Repair")

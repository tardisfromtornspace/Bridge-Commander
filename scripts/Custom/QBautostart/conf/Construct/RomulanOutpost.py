from bcdebug import debug
import App
from Custom.QBautostart.Libs.Races import Races
from Custom.QBautostart.Libs.LibConstruct import Construct

CONSTRUCT_SHIP = "ships.RomulanOutpost"
RACE = "Romulan"

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
        # add all Ships of same Race to construct
        lShipsToConstruct = Races[RACE].GetShips()
        # remove some shuttles etc
        RemoveFromList(lShipsToConstruct, "Reman Scimitar")
        RemoveFromList(lShipsToConstruct, "romulanshuttle")
        
        # Position
        kThis = App.Waypoint_Create(sConstructionLocation, sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kBaseLocation = pConstructionShip.GetWorldLocation()
        kThis.SetTranslateXYZ(kBaseLocation.GetX() - 50.0, kBaseLocation.GetY() + 6.0, kBaseLocation.GetZ() - 4.0)
        kForward = App.TGPoint3()
        kBaseForward = pConstructionShip.GetWorldForwardTG()
        kForward.SetXYZ(kBaseForward.GetY() * -1.0, kBaseForward.GetX(), kBaseForward.GetZ())
        kUp = App.TGPoint3()
        kUp.Set(pConstructionShip.GetWorldUpTG())
        kThis.AlignToVectors(kForward, kUp)
        kThis.Update(0)
        
        # go
        dConstructors[pConstructionShip.GetName()] = Construct(pConstructionShip, RACE, lShipsToConstruct, sConstructionLocation, iIncConstructionPower = 10, iNumParallelConstructions = 8)

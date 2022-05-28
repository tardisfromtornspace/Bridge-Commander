# This script handles Life Support system destruction

# by Sov

# Imports
import App
from Custom.DS9FX.DS9FXLib import DS9FXLifeSupportLib
from Custom.DS9FX.DS9FXLifeSupport import LifeSupport_dict
from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents

# Functions
def HandleDestroyedLifeSupport(pObject, pEvent):
    pSource = pEvent.GetSource()
    if not pSource:
        return 0
    
    pSys = App.ShipSubsystem_Cast(pSource)
    if not pSys:
        return 0

    pShip = pSys.GetParentShip()
    if not pShip:
        return 0
    
    pShipID = pShip.GetObjID()
    if not pShipID:
        return 0

    pShipType = DS9FXLifeSupportLib.GetShipType(pShip)
    if not pShipType:
        return 0

    if not pSys.GetName() == "Life Support":
        return 0

    if not LifeSupport_dict.dCrew.has_key(pShipID):
        return 0

    fCrew = DS9FXLifeSupportLib.GetShipMaxCrewCount(pShip, pShipType)
    if not fCrew:
        return 0
    
    pShip.ClearAI()
    LifeSupport_dict.dCrew[pShipID] = 0
    DS9FXLifeSupportLib.GroupCheck(pShip)
    DS9FXLifeSupportLib.PlayerCheck(pShipID)

    DS9FXGlobalEvents.Trigger_Ship_Dead_In_Space(pShip)
    DS9FXGlobalEvents.Trigger_Combat_Effectiveness(pShip)

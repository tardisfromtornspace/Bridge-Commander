# This script handles new ship creation and stores crew info in a dict

# by Sov

# Imports
import App
from Custom.DS9FX.DS9FXLib import DS9FXLifeSupportLib
from Custom.DS9FX.DS9FXLifeSupport import LifeSupport_dict
from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents

# Functions
def HandleShip(pObject, pEvent):    
    pNewShip = App.ShipClass_Cast(pEvent.GetDestination())
    if not pNewShip:
        return 0
    
    pShipID = pNewShip.GetObjID()
    if not pShipID:
        return 0

    pShip = DS9FXLifeSupportLib.GetShipType(pNewShip)
    if not pShip:
        return 0

    fCrew = DS9FXLifeSupportLib.GetShipMaxCrewCount(pNewShip, pShip)
    if not fCrew:
        return 0

    LifeSupport_dict.dCrew[pShipID] = fCrew

    DS9FXGlobalEvents.Trigger_Combat_Effectiveness(pNewShip)    


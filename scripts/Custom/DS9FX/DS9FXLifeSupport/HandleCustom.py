# This script listens to a custom event which must be fired by the new weapon or other form of script which inflicts damage,
# this is here for custom weapons or natural disasters (Badlands Plasma Storms I.E.)

# by Sov

# Imports
import App
from Custom.DS9FX.DS9FXLib import DS9FXLifeSupportLib
from Custom.DS9FX.DS9FXLifeSupport import LifeSupport_dict
from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents

# Functions
def HandleCustomDamage(pObject, pEvent):
    pDamage = 0
    try:
        pDamage = pEvent.GetFloat()
    except AttributeError:
        return 0

    if pDamage <= 0:
        return 0

    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    if not pShip:
        return 0

    pShipID = pShip.GetObjID()
    if not pShipID:
        return 0

    pHullMax = pShip.GetHull().GetMaxCondition()
    if not pHullMax:
        return 0

    if not LifeSupport_dict.dCrew.has_key(pShipID):
        return 0

    # To calculate properly we need the defined max crew value, not the current one...
    pShipType = DS9FXLifeSupportLib.GetShipType(pShip)
    if not pShipType:
        return 0

    fMaxCrew = DS9FXLifeSupportLib.GetShipMaxCrewCount(pShip, pShipType)
    if not fMaxCrew:
        return 0
    
    fModifier = float(pDamage)/float(pHullMax)
    fModifier = float(fModifier)*float(fMaxCrew)
    iModifier = int(fModifier)

    iNewCrew = LifeSupport_dict.dCrew[pShipID]
    iNewCrew = iNewCrew - iModifier
    if iNewCrew <= 0:
        iNewCrew = 0
        pShip.ClearAI()
        DS9FXLifeSupportLib.GroupCheck(pShip)
        DS9FXLifeSupportLib.PlayerCheck(pShipID)
        DS9FXGlobalEvents.Trigger_Ship_Dead_In_Space(pShip)

    LifeSupport_dict.dCrew[pShipID] = iNewCrew

    DS9FXGlobalEvents.Trigger_Combat_Effectiveness(pShip)

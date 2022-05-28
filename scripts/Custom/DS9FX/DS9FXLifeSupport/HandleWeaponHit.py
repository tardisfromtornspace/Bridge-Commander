# This script controls weapon firing on a ship and if needed decreases the current crew count...

# by Sov

# Imports
import App
from Custom.DS9FX.DS9FXLib import DS9FXLifeSupportLib
from Custom.DS9FX.DS9FXLifeSupport import LifeSupport_dict, HandlePlugins
from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents

# Functions
def HandleWeaponsFire(pObject, pEvent):    
    pHit = pEvent.IsHullHit()
    if not pHit == 1:
        return 0    

    pDamage = pEvent.GetDamage()
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

    fShieldStats = DS9FXLifeSupportLib.GetShieldPerc(pShip)
    if fShieldStats > 25:
        return 0

    pTechStats = HandlePlugins.RetriveStatus(pObject, pEvent)
    if not pTechStats:
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

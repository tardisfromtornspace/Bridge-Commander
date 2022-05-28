# This handles docking sequences, so replenish the crew count too...

# by Sov

# Imports
import App
from Custom.DS9FX.DS9FXLib import DS9FXLifeSupportLib
from Custom.DS9FX.DS9FXLifeSupport import LifeSupport_dict, AIBoarding, CaptureShip
from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents

# Functions
def HandleDockingSequence(pObject, pEvent):    
    pRepairedShip = App.ShipClass_Cast(pEvent.GetDestination())
    if not pRepairedShip:
        return 0
    
    pShipID = pRepairedShip.GetObjID()
    if not pShipID:
        return 0

    pShip = DS9FXLifeSupportLib.GetShipType(pRepairedShip)
    if not pShip:
        return 0

    if not LifeSupport_dict.dCrew.has_key(pShipID):
        return 0

    fCrew = DS9FXLifeSupportLib.GetShipMaxCrewCount(pRepairedShip, pShip)
    if not fCrew:
        return 0

    if CaptureShip.captureships.has_key(pShipID):
        del CaptureShip.captureships[pShipID]
    if AIBoarding.dCombat.has_key(pShipID):
        del AIBoarding.dCombat[pShipID]
    
    LifeSupport_dict.dCrew[pShipID] = fCrew

    DS9FXGlobalEvents.Trigger_Ship_Recrewed(None, pRepairedShip)
    DS9FXGlobalEvents.Trigger_Combat_Effectiveness(pRepairedShip)

# This will adjust ship combat effectiveness

# by Sov & SMBW

# Imports
import App
from Custom.DS9FX.DS9FXLib import DS9FXLifeSupportLib
from Custom.DS9FX.DS9FXLifeSupport import LifeSupport_dict
from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents

sys_dict = {} # Smbw: Added a global dict.

# Functions
def CheckCrew(pObject, pEvent):
    global sys_dict
    
    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    if not pShip:
        return 0

    pID = pShip.GetObjID()
    if not pID:
        return 0

    if not LifeSupport_dict.dCrew.has_key(pID):
        return 0
    
    pCrew = LifeSupport_dict.dCrew[pID]

    pType = DS9FXLifeSupportLib.GetShipType(pShip)
    if not pType:
        return 0

    pMaxCrew = DS9FXLifeSupportLib.GetShipMaxCrewCount(pShip, pType)
    if not pMaxCrew:
        return 0

    # Smbw: I think it's better using pPerc than pDiff:
    pPerc = int(float(pCrew)/float(pMaxCrew)*float(100))
    if pPerc >= 100:
        pPerc = 100

    elif pPerc <= 5:
        pPerc = 5

    if sys_dict.has_key(pID):
        pOldValue = sys_dict[pID]
    else:
        pOldValue = 100.0

    sys_dict[pID] = pPerc

    pSet = pShip.GetPropertySet()
    if not pSet:
        return 0

    pList = pSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
    if not pList:
        return 0

    pList.TGBeginIteration()

    for i in range(pList.TGGetNumItems()):
        pProp = App.SubsystemProperty_Cast(pList.TGGetNext().GetProperty())
        pSys = pShip.GetSubsystemByProperty(pProp)
        if not pSys:
            continue
        ProcessSystems(pSys, pPerc, pOldValue) # Smbw: Added a param (pOldValue).

    pList.TGDoneIterating()
    pList.TGDestroy()

    DS9FXGlobalEvents.Trigger_Combat_Effectiveness_Adjusted(pShip)

     
def ProcessSystems(pSys, pValue, pOldValue): # Smbw: Added some stuff here:    
    pValue = pValue / 100.0
    pOldValue = pOldValue / 100.0

    pSysProp = pSys.GetProperty()
    
    # Calculate a new disable percentage:
    DefDisPerc = ((pSysProp.GetDisabledPercentage()) - 1 + pOldValue) / pOldValue
        
    #newDisPerc = DefDisPerc + ((1.0 - pValue) * (1.0 - DefDisPerc))
    newDisPerc = (DefDisPerc * pValue) + 1 - pValue # same as above; less operations
    pSysProp.SetDisabledPercentage(newDisPerc)

    # Calculate repair points:
    SysCast = App.RepairSubsystem_Cast(pSys)
    if SysCast:
        pSysProp = SysCast.GetProperty()

        MaxRepPoints = pSysProp.GetMaxRepairPoints() / pOldValue
        newRepPoints = MaxRepPoints * pValue    
        pSysProp.SetMaxRepairPoints(newRepPoints)

    # Calculate the power output:
    SysCast = App.PowerSubsystem_Cast(pSys)
    if SysCast:
        pSysProp = SysCast.GetProperty()
        
        MaxPowerOut = pSysProp.GetPowerOutput() / ((0.4 * pOldValue) + 0.6)
        newPowerOut = ((pValue * 0.4) + 0.6) * MaxPowerOut
        pSysProp.SetPowerOutput(newPowerOut)

    # Calculate the sensor range:
    SysCast = App.SensorSubsystem_Cast(pSys)
    if SysCast:
        pSysProp = SysCast.GetProperty()

        MaxSensorRange = pSysProp.GetBaseSensorRange() / ((0.75 * pOldValue) + 0.25)
        newSensorRange = ((pValue * 0.75) + 0.25) * MaxSensorRange
        pSysProp.SetBaseSensorRange(newSensorRange)

    # Calculate shield recharge:
    SysCast = App.ShieldClass_Cast(pSys)
    if SysCast:
        pSysProp = SysCast.GetProperty()
        shields = [pSysProp.FRONT_SHIELDS, pSysProp.REAR_SHIELDS, pSysProp.TOP_SHIELDS, pSysProp.BOTTOM_SHIELDS, pSysProp.LEFT_SHIELDS, pSysProp.RIGHT_SHIELDS]
        
        for s in shields:
            MaxCharge = pSysProp.GetShieldChargePerSecond(s) / ((0.4 * pOldValue) + 0.6)
            newCharge = ((pValue * 0.4) + 0.6) * MaxCharge
            pSysProp.SetShieldChargePerSecond(s, newCharge)


def RemoveShip(pObject, pEvent):
    global sys_dict
    
    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    if not pShip:
        return 0

    pID = pShip.GetObjID()
    if not pID:
        return 0

    if sys_dict.has_key(pID):
        del sys_dict[pID]

def Clear():
    global sys_dict

    sys_dict = {}

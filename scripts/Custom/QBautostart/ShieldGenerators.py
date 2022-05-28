import App
import MissionLib
import Foundation


MODINFO = {     "Author": "\"Defiant\" erik@vontaene.de",
                "Version": "0.1",
                "License": "BSD",
                "Description": "Work around to use multiple shield generators in BC",
                "needBridge": 0
            }


# returns a list with all non-real-shieldgenerator shieldgenerators
def GetAllShieldGenerators(pShip):
        retList = []
        
        pPropSet = pShip.GetPropertySet()
        pShipSubSystemPropInstanceList = pPropSet.GetPropertiesByType(App.CT_SHIELD_PROPERTY)
        iNumItems = pShipSubSystemPropInstanceList.TGGetNumItems()
        pShipSubSystemPropInstanceList.TGBeginIteration()
        for i in range(iNumItems):
                pInstance = pShipSubSystemPropInstanceList.TGGetNext()
                pProperty = App.ShieldProperty_Cast(pInstance.GetProperty())
                if not pProperty.IsPrimary():
                        pSubSystem = pShip.GetSubsystemByProperty(pProperty)
                        pShieldGenerator = App.ShieldClass_Cast(pSubSystem)
                        retList.append(pShieldGenerator)
        
        pShipSubSystemPropInstanceList.TGDoneIterating()
        return retList


# sets up a ship for use with this script
def SetUpShip(pShip):
        # Make our "real" shield generator undestroyable
        pShields = pShip.GetShields()
                
        pShields.SetInvincible(0)
        pShields.GetProperty().SetDisabledPercentage(0.0)
        # and don't waste too much repair points on it
        pShields.GetProperty().SetRepairComplexity(0.0)
        

# changes the shield strength
def RedefineShieldGenerators(pShip, ShieldGenerators):        
        pShields = pShip.GetShields()
        NumTotalGenerators = len(ShieldGenerators)
        if NumTotalGenerators == 0:
                return
        
        # for every shield
        for Shield in range(App.ShieldClass.NUM_SHIELDS):
                ShieldMax = 0
                ShieldReload = 0
                NumDisabledGenerators = 0
                ShieldPercentage = pShields.GetSingleShieldPercentage(Shield)

                # for every shield generator
                for Generator in ShieldGenerators:
                        # don't use the disabled generators
                        if Generator.IsDisabled():
                                NumDisabledGenerators = NumDisabledGenerators + 1
                                continue
                        
                        # sum their values
                        ShieldMax = ShieldMax + Generator.GetMaxShields(Shield)
                        ShieldReload = ShieldReload + Generator.GetProperty().GetShieldChargePerSecond(Shield)
                # and set the values for this shield
                # some scripts in BC will report zero devision error if the value in shieldmax is 0, so work around
                if ShieldMax == 0.0:
                        ShieldMax = 0.1
                pShields.GetProperty().SetMaxShields(Shield, ShieldMax)
                pShields.GetProperty().SetShieldChargePerSecond(Shield, ShieldReload)
                PercentageShieldGeneratorsWorking = 1 - NumDisabledGenerators / float(NumTotalGenerators)
                pShields.SetCurShields(Shield, ShieldMax * PercentageShieldGeneratorsWorking * ShieldPercentage)


def SubsystemDisabled(pObject, pEvent):
        pDisabledObject = pEvent.GetSource()
        
        if pDisabledObject.IsTypeOf(App.CT_SHIELD_SUBSYSTEM):
                pShip = App.ShipClass_Cast(pEvent.GetDestination())

                ShieldGenerators = GetAllShieldGenerators(pShip)
                
                # check for multiple shield generators
                if len(ShieldGenerators) > 1:
                        RedefineShieldGenerators(pShip, ShieldGenerators)
        
        pObject.CallNextHandler(pEvent)


def SubsystemOperational(pObject, pEvent):
        pDisabledObject = pEvent.GetSource()
        
        if pDisabledObject.IsTypeOf(App.CT_SHIELD_SUBSYSTEM):
                pShip = App.ShipClass_Cast(pEvent.GetDestination())

                ShieldGenerators = GetAllShieldGenerators(pShip)
                
                # check for multiple shield generators
                if len(ShieldGenerators) > 1:
                        RedefineShieldGenerators(pShip, ShieldGenerators)
        
        pObject.CallNextHandler(pEvent)


def NewShip(pObject, pEvent):
        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if not pShip:
                return
        
        ShieldGenerators = GetAllShieldGenerators(pShip)
        
        # check for multiple shield generators
        if len(ShieldGenerators) > 1:
                SetUpShip(pShip)
                RedefineShieldGenerators(pShip, ShieldGenerators)
        
        pObject.CallNextHandler(pEvent)


# called by QBautostart extension when the player gets a new ship
def NewPlayerShip():
        pShip = MissionLib.GetPlayer()
        if not pShip:
                return
        
        ShieldGenerators = GetAllShieldGenerators(pShip)
        
        # check for multiple shield generators
        if len(ShieldGenerators) > 1:
                SetUpShip(pShip)
                RedefineShieldGenerators(pShip, ShieldGenerators)


def init():
	# Multiplayer check
	if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
		return
	
	pMission = MissionLib.GetMission()
	
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SUBSYSTEM_DISABLED, pMission ,  __name__ + ".SubsystemDisabled")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SUBSYSTEM_OPERATIONAL, pMission ,  __name__ + ".SubsystemOperational")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(Foundation.TriggerDef.ET_FND_CREATE_SHIP, pMission, __name__ + ".NewShip")

        NewPlayerShip()

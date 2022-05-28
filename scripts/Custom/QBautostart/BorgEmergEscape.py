import App
import MissionLib
import string
import ftb.ShipManager


MODINFO = { "needBridge": 0 }


def GetShipType(pShip):
        if pShip and pShip.GetScript():
                return string.split(pShip.GetScript(), '.')[-1]
        else:
                return None


def chance(iRand):
        if App.g_kSystemWrapper.GetRandomNumber(100) < iRand:
                return 1
        return 0


def BorgEmergEscape(pObject, pEvent):
        pObject = App.ObjectClass_Cast(pEvent.GetDestination())
        pShip = App.ShipClass_Cast(pObject)
        if not pShip or not pObject:
                pObject.CallNextHandler(pEvent)
                return
        ShipType = GetShipType(pShip)
        
        if (ShipType == "LowCube") and chance(20):
                pFTBCarrier = ftb.ShipManager.GetShip(pShip)
                pFTBLauncher = pFTBCarrier.GetLaunchers()
                numTypes = len(pFTBLauncher)
                for index in range(numTypes):
                        pFTBLauncher[index].LaunchShip("sphere")
        
        pObject.CallNextHandler(pEvent)


def init():
        pMission = MissionLib.GetMission()

	if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".BorgEmergEscape")

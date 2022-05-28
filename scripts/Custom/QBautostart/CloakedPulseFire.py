import App
import MissionLib
import Libs.LibCloakFire

# Credits for this Mod goes to edtheborg with his FTA 2.0 Mod.
# without him, this would have never existed!

MODINFO = {     "Author": "\"Defiant\" erik@bckobayashimaru.de",
                "Version": "0.1",
                "License": "BSD",
                "Description": "Allows the Player to fie Pulse Weapons while cloaked",
                "needBridge": 0
            }


def PlayerPulseFire(pObject, pEvent):
        pPlayer = MissionLib.GetPlayer()
        
        if pPlayer:
                pTarget = pPlayer.GetTarget()
                pTargetSubsystem = pPlayer.GetTargetSubsystem()
                pSet = pPlayer.GetContainingSet()
        
        if pPlayer and pPlayer.IsCloaked():
                Libs.LibCloakFire.PulseFire(pPlayer, pTarget, pTargetSubsystem, pSet)
        
        pObject.CallNextHandler(pEvent)


def init():
	pMission = MissionLib.GetMission()	
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_INPUT_FIRE_TERTIARY, pMission ,  __name__ + ".PlayerPulseFire")

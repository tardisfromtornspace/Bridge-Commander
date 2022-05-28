import App
import MissionLib
from Libs.LibQBautostart import *

MODINFO = {     "Author": "\"Defiant\" erik@bckobayashimaru.de",
                "needBridge": 0
            }

lSounds = [
"sfx/Custom/AssimilationBeam/FirstContactBorgSpeech.wav",
"sfx/Custom/AssimilationBeam/FirstContactBorgSpeech.wav",
"sfx/Custom/AssimilationBeam/FirstContactBorgSpeech.wav",
"sfx/Custom/AssimilationBeam/FirstContactBorgSpeech.wav",
"sfx/Custom/AssimilationBeam/FirstContactBorgSpeech.wav",
"sfx/Custom/AssimilationBeam/BasicSpeechVoyager.wav",
"sfx/Custom/AssimilationBeam/LowerShieldsSurrerShipsLowQ.wav",
"sfx/Custom/AssimilationBeam/ResistanceIsFutile.wav",
"sfx/Custom/AssimilationBeam/WeBorgYouAssimlitanceFutile.wav",
"sfx/Custom/AssimilationBeam/YourCultureLowQ.wav",
"sfx/Custom/AssimilationBeam/YourDefensiveCabilitiesLowQ.wav",
"sfx/Custom/AssimilationBeam/AddDistinctivenessLowQ.wav",
"sfx/Custom/AssimilationBeam/FreedomIrrelevantLowQ.wav",
]

lock = 0
NonSerializedObjects = ( "lock", )

def ObjectCreatedHandler(pObject, pEvent):
	global lock
	
	pObject.CallNextHandler(pEvent)
	
	pPlayer = MissionLib.GetPlayer()
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	if pShip and pPlayer and pShip.GetContainingSet() and pPlayer.GetContainingSet() and pShip.GetContainingSet().GetName() == pPlayer.GetContainingSet().GetName() and GetRaceFromShip(pShip):
		sRace = GetRaceFromShip(pShip)
		if sRace == "Borg" and len(lSounds) > 0 and not lock:
			lock = 1
			i = App.g_kSystemWrapper.GetRandomNumber(len(lSounds))
			sSound = lSounds[i]
			pSound = App.TGSound_Create(sSound, "BorgGreet", 0)
			pSound.SetSingleShot(1)
			App.g_kSoundManager.PlaySound("BorgGreet")
			
			pSeq = App.TGSequence_Create()
			pSeq.AppendAction(App.TGScriptAction_Create(__name__, "unlock"), 30)
			pSeq.Play()


def unlock(pAction):
	global lock
	lock = 0
	return 0


def init():
	global lock
	pMission = MissionLib.GetMission()
	lock = 0
	
	if App.g_kUtopiaModule.IsMultiplayer():
		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_CREATED_NOTIFY, pMission, __name__ + ".ObjectCreatedHandler")
	else:
		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_CREATED, pMission, __name__ + ".ObjectCreatedHandler")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".ObjectCreatedHandler")

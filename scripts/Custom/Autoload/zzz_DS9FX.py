# zzz_DS9FX.py: This file controls all core functions of DS9FX Xtended


import App
import Foundation
import MissionLib
import string
from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents
from Custom.DS9FX import DS9FXMutatorFunctions

pDS9FXVer = __import__("Custom.DS9FX.DS9FXVersionSignature")
pVer = pDS9FXVer.DS9FXVersion

mode = Foundation.MutatorDef("DS9FX " + pVer)
ET_EVENT = App.UtopiaModule_GetNextEventType()

Foundation.SystemDef("DeepSpace9", 1, dict = { "modes": [ mode ] } )
Foundation.SystemDef("DS9FXBadlands", 1, dict = { "modes": [ mode ] } )
Foundation.SystemDef("DS9FXQonos", 1, dict = { "modes": [ mode ] } )
Foundation.SystemDef("DS9FXChintoka", 1, dict = { "modes": [ mode ] } )
Foundation.SystemDef("DS9FXVela", 1, dict = { "modes": [ mode ] } )
Foundation.SystemDef("DS9FXCardassia", 1, dict = { "modes": [ mode ] } )
Foundation.SystemDef("DS9FXTrivas", 1, dict = { "modes": [ mode ] } )

class DS9FXMissionStart(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.MissionStartHandling(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXPlayerShipCreated(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.PlayerCreatedHandling(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXShipCreated(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.ShipCreatedHandling(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXEnteredSet(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXGlobalEvents.Trigger_App_Entered_Set(pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXAppEnteredSet(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.EnterSetHandling(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXQuitPrompt(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.QuitPromptHandling(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXExitGame(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.ExitGameHandling(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXExitProgram(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.ExitProgramHandling(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXObjectDestroyed(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXGlobalEvents.Trigger_App_Object_Destroyed(pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXAppObjectDestroyed(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.ObjectDestroyedHandling(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXObjectExploding(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXGlobalEvents.Trigger_App_Object_Exploding(pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXAppObjectExploding(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.ObjectExplodingHandling(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXSubsystemDestroyed(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXGlobalEvents.Trigger_App_Subsystem_Destroyed(pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXAppSubsystemDestroyed(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.SubsystemDestroyedHandling(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXWeaponHit(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.WeaponHitHandling(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXSetPlayer(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXGlobalEvents.Trigger_App_Set_Player(pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXAppSetPlayer(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.SetPlayerHandling(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXRepairShip(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.RepairShipHandling(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXInsideWormhole(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.InsideWormholeHandling(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXOutsideWormhole(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.OutsideWormholeHandling(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXStopManualEntry(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.StopManualEntryHandling(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXForceMissionPlaying(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.ForceMissionPlayingHandling(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXStopForcingMissionPlaying(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.StopForcingMissionPlayingHandling(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXStartDS9FXMission(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.StartDS9FXMissionHandling(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXEndDS9FXMission(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.EndDS9FXMissionHandling(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXLifeSupportShipRecrewed(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXLifeSupportShipDeadInSpace(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.HandleShipDeadInSpace(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXLifeSupportShipReactivated(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXLifeSupportShipTakenOver(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.HandleTakenOver(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXLifeSupportCombatEffectiveness(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.CombatEffectivenessHandling(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXLifeSupportCombatEffectivenessAdjusted(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXLifeSupportCustomDamage(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.LifeSupportCustomDamageHandling(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXMusicDone(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXGlobalEvents.Trigger_App_Music_Done(pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXAppMusicDone(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.MusicDoneHandling(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXMusicConditionChanged(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXGlobalEvents.Trigger_App_Music_Condition_Changed(pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXAppMusicConditionChanged(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.MusicConditionChangedHandling(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXMVAMSeperation(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.MVAMSeperationHandling(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXMVAMReintegration(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.MVAMReintegrationHandling(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

class DS9FXPrintConsole(Foundation.TriggerDef):
        def __init__(self, dict = {}):
                Foundation.TriggerDef.__init__(self, "DS9FXPrintConsole", ET_EVENT, dict = {})

        def __call__(self, pObject, pEvent):
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                DS9FXMutatorFunctions.KeyEventHandling(pObject, pEvent)
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

DS9FXMutatorFunctions.GameStart()                        
                        
DS9FXMissionStart('DS9FX Mission Start', App.ET_MISSION_START, dict = { 'modes': [ mode ] } )

DS9FXPlayerShipCreated('DS9FX Player Ship Created', Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP, dict = { 'modes': [ mode ] } )

DS9FXShipCreated('DS9FX Ship Created', Foundation.TriggerDef.ET_FND_CREATE_SHIP, dict = { 'modes': [ mode ] } )

DS9FXEnteredSet('DS9FX Entered Set', App.ET_ENTERED_SET, dict = { 'modes': [ mode ] } )

DS9FXAppEnteredSet('DS9FX App Entered Set', DS9FXGlobalEvents.ET_APP_ENTERED_SET, dict = { 'modes': [ mode ] } )

DS9FXQuitPrompt('DS9FX Quit Prompt', App.ET_QUIT, dict = { 'modes': [ mode ] } )

DS9FXExitGame('DS9FX Exit Game', App.ET_EXIT_GAME, dict = { 'modes': [ mode ] } )

DS9FXExitProgram('DS9FX Exit Program', App.ET_EXIT_PROGRAM, dict = { 'modes': [ mode ] } )

DS9FXObjectDestroyed('DS9FX Object Destroyed', App.ET_OBJECT_DESTROYED, dict = { 'modes': [ mode ] } )

DS9FXAppObjectDestroyed('DS9FX App Object Destroyed', DS9FXGlobalEvents.ET_APP_OBJECT_DESTROYED, dict = { 'modes': [ mode ] } )

DS9FXObjectExploding('DS9FX Object Exploding', App.ET_OBJECT_EXPLODING, dict = { 'modes': [ mode ] } )

DS9FXAppObjectExploding('DS9FX App Object Exploding', DS9FXGlobalEvents.ET_APP_OBJECT_EXPLODING, dict = { 'modes': [ mode ] } )

DS9FXSubsystemDestroyed('DS9FX Subsystem Destroyed', App.ET_SUBSYSTEM_DESTROYED, dict = { 'modes': [ mode ] } )

DS9FXAppSubsystemDestroyed('DS9FX App Subsystem Destroyed', DS9FXGlobalEvents.ET_APP_SUBSYSTEM_DESTROYED, dict = { 'modes': [ mode ] } )

DS9FXWeaponHit('DS9FX Weapon Hit', App.ET_WEAPON_HIT, dict = { 'modes': [ mode ] } )

DS9FXSetPlayer('DS9FX Set Player', App.ET_SET_PLAYER, dict = { 'modes': [ mode ] } )

DS9FXAppSetPlayer('DS9FX App Set Player', DS9FXGlobalEvents.ET_APP_SET_PLAYER, dict = { 'modes': [ mode ] } )

DS9FXRepairShip('DS9FX Repair Ship', DS9FXGlobalEvents.ET_REPAIR_SHIP, dict = { 'modes': [ mode ] } )

DS9FXInsideWormhole('DS9FX Inside Wormhole', DS9FXGlobalEvents.ET_INSIDE_WORMHOLE, dict = { 'modes': [ mode ] } )

DS9FXOutsideWormhole('DS9FX Outside Wormhole', DS9FXGlobalEvents.ET_OUTSIDE_WORMHOLE, dict = { 'modes': [ mode ] } )

DS9FXStopManualEntry('DS9FX Stop Manual Entry', DS9FXGlobalEvents.ET_STOP_MANUAL_ENTRY_TRIGGER, dict = { 'modes': [ mode ] } )

DS9FXForceMissionPlaying('DS9FX Force Mission Playing', DS9FXGlobalEvents.ET_FORCE_MISSION_PLAYING, dict = { 'modes': [ mode ] } )

DS9FXStopForcingMissionPlaying('DS9FX Stop Forcing Mission Playing', DS9FXGlobalEvents.ET_STOP_FORCING_MISSION_PLAYING, dict = { 'modes': [ mode ] } )

DS9FXStartDS9FXMission('DS9FX Start DS9FX Mission', DS9FXGlobalEvents.ET_DS9FX_MISSION_START, dict = { 'modes': [ mode ] } )

DS9FXEndDS9FXMission('DS9FX End DS9FX Mission', DS9FXGlobalEvents.ET_DS9FX_MISSION_END, dict = { 'modes': [ mode ] } )

DS9FXLifeSupportShipRecrewed('DS9FX Life Support Ship Recrewed', DS9FXGlobalEvents.ET_SHIP_RECREWED, dict = { 'modes': [ mode ] } )

DS9FXLifeSupportShipDeadInSpace('DS9FX Life Support Ship Dead In Space', DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, dict = { 'modes': [ mode ] } )

DS9FXLifeSupportShipReactivated('DS9FX Life Support Ship Reactivated', DS9FXGlobalEvents.ET_SHIP_REACTIVATED, dict = { 'modes': [ mode ] } )

DS9FXLifeSupportShipTakenOver('DS9FX Life Support Ship Taken Over', DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, dict = { 'modes': [ mode ] } )

DS9FXLifeSupportCombatEffectiveness('DS9FX Life Support Combat Effectiveness', DS9FXGlobalEvents.ET_COMBAT_EFFECTIVENESS, dict = { 'modes': [ mode ] } )

DS9FXLifeSupportCombatEffectivenessAdjusted('DS9FX Life Support Combat Effectiveness Adjusted', DS9FXGlobalEvents.ET_COMBAT_EFFECTIVENESS_ADJUSTED, dict = { 'modes': [ mode ] } )

DS9FXLifeSupportCustomDamage('DS9FX Life Support Custom Damage', DS9FXGlobalEvents.ET_CUSTOM_DAMAGE, dict = { 'modes': [ mode ] } )

DS9FXMusicDone('DS9FX Music Done', App.ET_MUSIC_DONE, dict = { 'modes': [ mode ] } )

DS9FXAppMusicDone('DS9FX App Music Done', DS9FXGlobalEvents.ET_APP_MUSIC_DONE, dict = { 'modes': [ mode ] } )

DS9FXMusicConditionChanged('DS9FX Music Condition Changed', App.ET_MUSIC_CONDITION_CHANGED, dict = { 'modes': [ mode ] } )

DS9FXAppMusicConditionChanged('DS9FX App Music Condition Changed', DS9FXGlobalEvents.ET_APP_MUSIC_CONDITION_CHANGED, dict = { 'modes': [ mode ] } )

DS9FXMVAMSeperation('DS9FX MVAM Seperation', DS9FXGlobalEvents.ET_MVAM_SEP, dict = { 'modes': [ mode ] } )

DS9FXMVAMReintegration('DS9FX MVAM Reintegration', DS9FXGlobalEvents.ET_MVAM_REIN, dict = { 'modes': [ mode ] } )

DS9FXPrintConsole(dict = {"modes": [mode]})

App.g_kKeyboardBinding.BindKey(App.WC_CAPS_P, App.TGKeyboardEvent.KS_NORMAL, ET_EVENT, App.KeyboardBinding.GET_INT_EVENT, 5000)

print "DS9FX Initializing..."

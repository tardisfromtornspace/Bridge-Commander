# Used by the autoload module

import App
import MissionLib
import Custom.DS9FX.DS9FXmain
from Custom.DS9FX.DS9FXBadlandsFX import VortexFX
from Custom.DS9FX.DS9FXGUIHandler import HelmHandler
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib, DS9FXCleanLeftover, DS9FXCometAlpha, DS9FXDisableEndCombat, DS9FXKillSets, DS9FXMirrorUniverse, DS9FXNebula, LogConsole, FixExitGame, FixNanoFXExplosions, Mvam_Wormhole_Fix, PopulateGroups, StabilizationCode, SetGamePlayerFix
from Custom.DS9FX.DS9FXLifeSupport import AIBoarding, CaptureShip, CombatEffectiveness, HandleCustom, HandleDocking, HandleExitGame, HandleLifeSupportDestruction, HandleLifeSupportText, HandleMissions, HandleMVAM, HandleNewShip, HandleShields, HandlePlugins, HandleWeaponHit
from Custom.DS9FX.DS9FXManualEntry import ManualEntryManager
from Custom.DS9FX.DS9FXMissions import MissionStatus, Warping, WormholeEntry
from Custom.DS9FX.DS9FXObjects import BorgShips
from Custom.DS9FX.DS9FXPulsarFX import PulsarManager
from Custom.DS9FX.DS9FXPulsarFX.SoundFX import SoundLoader
from Custom.DS9FX.DS9FXSoundManager import DynamicMusicHandling, MusicTypeSelector, SoundManager
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

#Added by Alex SL Gato
from Custom.DS9FX.DS9FXLib import DS9FXLifeSupportLib

bAllowPrint = 1
bWormholeNoEntry = 0
bForceMissionPlaying = 0
bPreventManualEntryHandler = 0
bMVAM = 0

# Loads anything at game start
def GameStart():
        SoundLoader.InsertSounds()

# ET_MISSION_START related
def MissionStartHandling(pObject, pEvent):
        global bForceMissionPlaying, bWormholeNoEntry, bPreventManualEntryHandler, bMVAM
        bWormholeNoEntry = 0
        bForceMissionPlaying = 0
        bPreventManualEntryHandler = 0
        bMVAM = 0
        SoundManager.RegisterDS9FXSounds()
        Custom.DS9FX.DS9FXmain.init()
        StabilizeBCTimer()
        HandleLifeSupportLabels(opt = "CreateLabel")
        HandleLifeSupportLabels(opt = "StartTimer")
        VortexFX.StartUpTimingProcess()
        HelmHandler.HelmMenuClosed()
        HandleLifeSupportPlugins()
        HandleMissions.ResetMission()
        DS9FXMirrorUniverse.MissionStart()
        Mvam_Wormhole_Fix.MissionStart()
        AIBoarding.MissionStart()
        PulsarManager.Start()

def StabilizeBCTimer():
        pSequence = App.TGSequence_Create()
        pAction = App.TGScriptAction_Create(__name__, "InitiateStabilizeBCTimer")
        pSequence.AddAction(pAction, None, 1)
        pSequence.Play()   

def InitiateStabilizeBCTimer(pAction):
        reload (DS9FXSavedConfig)
        if DS9FXSavedConfig.StabilizeBC == 1:
                StabilizationCode.StartUp()

        return 0

def HandleLifeSupportLabels(opt = "Specify"):
        reload (DS9FXSavedConfig)
        if not DS9FXSavedConfig.LifeSupport == 1:
                return
        if not DS9FXSavedConfig.LifeSupportCrewLabels == 1:
                return
        if opt == "CreateLabel":
                HandleLifeSupportText.CreateLabel()
        elif opt == "RemoveLabel":
                HandleLifeSupportText.RemoveLabel()
        elif opt == "StartTimer":
                HandleLifeSupportText.StartUpTimingProcess()
        else:
                return

def HandleLifeSupportPlugins():
        reload (DS9FXSavedConfig)
        if not DS9FXSavedConfig.LifeSupport == 1:
                return
        HandlePlugins.IsModActive()

# ET_FND_CREATE_PLAYER_SHIP related
def PlayerCreatedHandling(pObject, pEvent):
        global bMVAM
        if bMVAM:
                bMVAM = 0
                return 
        DS9FXKillSets.DisallowSetKilling()
        Custom.DS9FX.DS9FXmain.RestartTrigger()
        MakeASystemMenu()
        CleanTimer()
        SetGamePlayerFix.FixTransportingBug(pObject, pEvent, param = "PlayerCreated")
        PopulateGroups.AddNames()
        CaptureShip.Reset()
        DS9FXCleanLeftover.Clean()

def MakeASystemMenu():        
        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        if pMission.GetScript() == "QuickBattle.QuickBattle":
                try:                                
                        import Systems.DeepSpace9.DeepSpace9
                        Systems.DeepSpace9.DeepSpace9.XtendedMenu()
                except:
                        pass

                try:
                        import Systems.DS9FXBadlands.DS9FXBadlands
                        Systems.DS9FXBadlands.DS9FXBadlands.XtendedMenu()
                except:
                        pass
                
                try:
                        import Systems.DS9FXQonos.DS9FXQonos
                        Systems.DS9FXQonos.DS9FXQonos.XtendedMenu()
                except:
                        pass      
                
                try:
                        import Systems.DS9FXChintoka.DS9FXChintoka
                        Systems.DS9FXChintoka.DS9FXChintoka.XtendedMenu()
                except:
                        pass   
                
                try:
                        import Systems.DS9FXVela.DS9FXVela
                        Systems.DS9FXVela.DS9FXVela.XtendedMenu()
                except:
                        pass         
                
                try:
                        import Systems.DS9FXCardassia.DS9FXCardassia
                        Systems.DS9FXCardassia.DS9FXCardassia.XtendedMenu()
                except:
                        pass    

                try:
                        import Systems.DS9FXTrivas.DS9FXTrivas
                        Systems.DS9FXTrivas.DS9FXTrivas.XtendedMenu()
                except:
                        pass  
                
def CleanTimer():
        pSequence = App.TGSequence_Create()
        pAction = App.TGScriptAction_Create(__name__, "CleanDelay")
        pSequence.AddAction(pAction, None, 1)
        pSequence.Play()   

def CleanDelay(pAction):
        reload (DS9FXSavedConfig)
        if DS9FXSavedConfig.StabilizeBC == 1:
                App.g_kLODModelManager.Purge()
                App.g_kModelManager.Purge()

        return 0

# ET_FND_CREATE_SHIP related
def ShipCreatedHandling(pObject, pEvent):
        BorgShips.BorgShipCheck(pObject, pEvent)
        HandleLifeSupportNewShip(pObject, pEvent)
        HandleNoDamageThroughShields("ShipCreated", pObject, pEvent)

def HandleNoDamageThroughShields(param, pObject, pEvent):
        reload (DS9FXSavedConfig)
        if not DS9FXSavedConfig.NoDamageThroughShields == 1:
                return 		
	
        if param == "ShipCreated":
                HandleShields.ShipCreated(pObject, pEvent)
        elif param == "WeaponHit":
		#print "I  got hit"
		isthisPhased = 0 # Alex SL Gato: Taking into account phased weaponry
        	pWeaponType = pEvent.GetWeaponType()
		if pWeaponType == pEvent.TORPEDO: # Fixing how this mod conflicts with PhasedTorp
			try:
				pTorp=App.Torpedo_Cast(pEvent.GetSource())
				#print "Verifying what I have"
				#if not pTorp:
				#	print "Welp I guess there is no torp, something went wrong"
				#print(pTorp.GetName())
				#print "Now the ModuleName"
				#print(pTorp.GetModuleName())
				#print "Now the NetType"
				#print(pTorp.GetNetType())
				##12 = PHASEDPLASMA
				##pTorp.GetNetType() == Multiplayer.SpeciesToTorp.PHASEDPLASMA
				if pTorp.GetNetType() == 12:
					isthisPhased = 1
				#	print "Yup I think I am called Phased"
			except:
				isthisPhased = 0
		if isthisPhased == 0:
			print "Not phased, I'll protect it"
                	HandleShields.WeaponHit(pObject, pEvent)
		else:
			print "So I am phased I guess"

def HandleLifeSupportNewShip(pObject, pEvent):
        reload (DS9FXSavedConfig)
        if not DS9FXSavedConfig.LifeSupport == 1:
                return 
        HandleNewShip.HandleShip(pObject, pEvent)

# ET_ENTERED_SET related
def EnterSetHandling(pObject, pEvent):
        EnterSetHandler(pObject, pEvent)
        ShipManager(pObject, pEvent)
        HandleMusicEnterSet(pObject, pEvent)
        DS9FXKillSets.KillSets(pObject, pEvent)
        DS9FXDisableEndCombat.EvalCondition()
        DS9FXMirrorUniverse.DisableButtons()

def EnterSetHandler(pObject, pEvent):
        pPlayer = App.Game_GetCurrentPlayer()    
        if not pPlayer:
                return 0

        pSet = pPlayer.GetContainingSet()
        if not pSet:
                return 0

        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if not pShip:
                return 0

        if pShip.GetObjID() == pPlayer.GetObjID():
                if (pSet.GetName() == "DeepSpace91"):
                        ActivateSpecialDS9FXTriggers()
                        StartManualEntryHandler()
                elif (pSet.GetName() == "GammaQuadrant1"):
                        ActivateSpecialDS9FXTriggers()
                        StartManualEntryHandler()     
                elif (pSet.GetName() == "BajoranWormhole1"):
                        ActivateSpecialDS9FXTriggers()
                        StartManualEntryHandler()
                else:
                        ManualEntryManager.KillManualEntry()
                        ActivateNormalDS9FXTriggers()        
        else:
                return 0

def ActivateSpecialDS9FXTriggers():
        Custom.DS9FX.DS9FXmain.ActivateDS9FXButtons()

def StartManualEntryHandler():
        global bForceMissionPlaying, bWormholeNoEntry, bPreventManualEntryHandler
        if bForceMissionPlaying == 1 or bWormholeNoEntry == 1 or bPreventManualEntryHandler == 1:
                return 0
        ManualEntryManager.ManualEntryHandler()

def ActivateNormalDS9FXTriggers(): 
        Custom.DS9FX.DS9FXmain.EnterSetTrigger()
        Custom.DS9FX.DS9FXmain.ActivateDS9FXButtons()

def ShipManager(pObject, pEvent):
        global bWormholeNoEntry
        if not bWormholeNoEntry == 1:
                return 0

        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if not pShip:
                return 0

        pSet = pShip.GetContainingSet()
        if not pSet:
                return 0

        sSet = pSet.GetName()

        if sSet == "BajoranWormhole1":
                pSet.DeleteObjectFromSet(pShip.GetName())
        else:
                return 0

def HandleMusicEnterSet(pObject, pEvent):
        pPlayer = App.Game_GetCurrentPlayer()  
        if not pPlayer:
                return 0

        pSet = pPlayer.GetContainingSet()
        if not pSet:
                return 0

        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if not pShip:
                return 0

        if pShip.GetObjID() == pPlayer.GetObjID():
                DynamicMusicHandling.InjectDummyMusicName()
                MusicTypeSelector.SelectType("EnterSet")
                DynamicMusicHandling.RestoreMusicName()

# ET_QUIT related
def QuitPromptHandling(pObject, pEvent):
        DS9FXMirrorUniverse.RestoreProperSettings()

# ET_EXIT_GAME related
def ExitGameHandling(pObject, pEvent):
        PulsarManager.End()
        SoundManager.UnloadDS9FXSounds()
        DS9FXEnd()
        HandleLifeSupportExitGame()
        HandleLifeSupportLabels(opt = "RemoveLabel")
        CombatEffectiveness.Clear()
        SetGamePlayerFix.ResetList()
        FixExitGame.FixExiting()

def DS9FXEnd():
        Custom.DS9FX.DS9FXmain.DS9FXExit()

def HandleLifeSupportExitGame():
        reload (DS9FXSavedConfig)
        if not DS9FXSavedConfig.LifeSupport == 1:
                return 
        HandleExitGame.ResetLifeSupport()

# ET_EXIT_PROGRAM related
def ExitProgramHandling(pObject, pEvent):
        reload (DS9FXSavedConfig)        
        if DS9FXSavedConfig.ExitGameDebugMode == 1:
                LogConsole.Output()

# ET_OBJECT_DESTROYED related
def ObjectDestroyedHandling(pObject, pEvent):
        CleanNoDelay()
        CombatEffectiveness.RemoveShip(pObject, pEvent)
        SetGamePlayerFix.FixTransportingBug(pObject, pEvent, param = "ObjectKilled")

def CleanNoDelay():
        reload (DS9FXSavedConfig)
        if DS9FXSavedConfig.StabilizeBC == 1:
                App.g_kLODModelManager.Purge()
                App.g_kModelManager.Purge()
        else:
                return

# ET_OBJECT_EXPLODING related
def ObjectExplodingHandling(pObject, pEvent):
        FixNanoFXExplosions.FixExplosions(pObject, pEvent)

# ET_SUBSYSTEM_DESTROYED related
def SubsystemDestroyedHandling(pObject, pEvent):
        HandleLifeSupportSystemDestruction(pObject, pEvent)

def HandleLifeSupportSystemDestruction(pObject, pEvent):
        reload (DS9FXSavedConfig)
        if not DS9FXSavedConfig.LifeSupport == 1:
                return 
        HandleLifeSupportDestruction.HandleDestroyedLifeSupport(pObject, pEvent)

# ET_WEAPON_HIT related
def WeaponHitHandling(pObject, pEvent):
        CleanNoDelay()
        HandleLifeSupportWeaponHit(pObject, pEvent)
        HandleNoDamageThroughShields("WeaponHit", pObject, pEvent)
        HandleAIBoardings(pObject, pEvent)

def HandleLifeSupportWeaponHit(pObject, pEvent):
        reload (DS9FXSavedConfig)
        if not DS9FXSavedConfig.LifeSupport == 1:
                return 
        HandleWeaponHit.HandleWeaponsFire(pObject, pEvent)

def HandleAIBoardings(pObject, pEvent):
        reload (DS9FXSavedConfig)
        if not DS9FXSavedConfig.LifeSupport == 1:
                return
        if not DS9FXSavedConfig.AIBoardings == 1:
                return
        AIBoarding.Boarding(pObject, pEvent)

# ET_SET_PLAYER related
def SetPlayerHandling(pObject, pEvent):
        DS9FXCometAlpha.IdentityCheck(pObject, pEvent)
        ManualEntrySetPlayerHandler()
        SetGamePlayerFix.FixTransportingBug(pObject, pEvent, param = "SetPlayer")

def ManualEntrySetPlayerHandler():
        pPlayer = MissionLib.GetPlayer()
        if not pPlayer:
                return

        pSet = pPlayer.GetContainingSet()
        if not pSet:
                return

        if (pSet.GetName() == "DeepSpace91") or (pSet.GetName() == "GammaQuadrant1") or (pSet.GetName() == "BajoranWormhole1"):
                StartManualEntryHandler()

# ET_REPAIR_SHIP related
def RepairShipHandling(pObject, pEvent):
        HandleLifeSupportDocking(pObject, pEvent)

def HandleLifeSupportDocking(pObject, pEvent):
        reload (DS9FXSavedConfig)
        if not DS9FXSavedConfig.LifeSupport == 1:
                return 
        HandleDocking.HandleDockingSequence(pObject, pEvent)

# ET_INSIDE_WORMHOLE related
def InsideWormholeHandling(pObject, pEvent):
        global bWormholeNoEntry
        bWormholeNoEntry = 1
        DS9FXKillSets.bDeleteSets = 0
        DS9FXMirrorUniverse.MirrorUniverse()
        Mvam_Wormhole_Fix.Deactivate()

# ET_OUTSIDE_WORMHOLE related
def OutsideWormholeHandling(pObject, pEvent):
        global bWormholeNoEntry, bPreventManualEntryHandler 
        bWormholeNoEntry = 0
        bPreventManualEntryHandler = 0
        DS9FXKillSets.bDeleteSets = 1
        DS9FXKillSets.KillSetsDelay(None)
        StartManualEntryHandler()
        DS9FXMirrorUniverse.TriggerSurprise()
        DS9FXNebula.SetupCheck()
        Mvam_Wormhole_Fix.Reactivate()

# ET_STOP_MANUAL_ENTRY related
def StopManualEntryHandling(pObject, pEvent):
        global bPreventManualEntryHandler
        bPreventManualEntryHandler = 1
        ManualEntryManager.KillManualEntry()

# ET_FORCE_MISSION_PLAYING related
def ForceMissionPlayingHandling(pObject, pEvent):
        global bForceMissionPlaying
        bForceMissionPlaying = 1
        ManualEntryManager.KillManualEntry()
        WormholeEntry.KillWormholeEntry()
        Warping.DisableGammaWarping()

# ET_STOP_FORCING_MISSION_PLAYING related
def StopForcingMissionPlayingHandling(pObject, pEvent):
        global bForceMissionPlaying
        bForceMissionPlaying = 0
        StartManualEntryHandler()
        WormholeEntry.AllowWormholeEntry()
        Warping.EnableGammaWarping()

# ET_START_DS9FX_MISSION related
def StartDS9FXMissionHandling(pObject, pEvent):
        HandleDS9FXMission(var = "Start")
        HandleMissions.MissionName(pObject, pEvent)
        MissionStatus.Setup(pObject, pEvent)
        DS9FXMirrorUniverse.InMission(1)

def HandleDS9FXMission(var = None):
        if var is None:
                return

        reload (DS9FXSavedConfig)
        if not DS9FXSavedConfig.KillRandomFleetsDuringMission == 1:
                return

        if var == "Start":
                Custom.DS9FX.DS9FXmain.DeleteRandomAttackTimer(None, None)
        elif var == "End":
                Custom.DS9FX.DS9FXmain.HandleRandomAttackTimer()
        else:
                return

# ET_END_DS9FX_MISSION related
def EndDS9FXMissionHandling(pObject, pEvent):
        HandleDS9FXMission(var = "End")
        HandleMissions.ResetMission()
        MissionStatus.Reset()
        DS9FXMirrorUniverse.InMission(0)

# ET_SHIP_DEAD_IN_SPACE related
def HandleShipDeadInSpace(pObject, pEvent):
        HandleMissions.MissionFailureCheck(pObject, pEvent)

# ET_SHIP_TAKEN_OVER related
def HandleTakenOver(pObject, pEvent):
        HandleMissions.MissionFailureCheck(pObject, pEvent)

# ET_COMBAT_EFFECTIVENESS related
def CombatEffectivenessHandling(pObject, pEvent):
        HandleCombatEffectiveness(pObject, pEvent)

def HandleCombatEffectiveness(pObject, pEvent):
        reload (DS9FXSavedConfig)
        if not DS9FXSavedConfig.LifeSupport == 1:
                return
        if not DS9FXSavedConfig.LifeSupportCombatEffectiveness == 1:
                return
        CombatEffectiveness.CheckCrew(pObject, pEvent)

# ET_LIFE_SUPPORT_CUSTOM_DAMAGE related
def LifeSupportCustomDamageHandling(pObject, pEvent):
        HandleLifeSupportCustomDamage(pObject, pEvent)

def HandleLifeSupportCustomDamage(pObject, pEvent):
        reload (DS9FXSavedConfig)
        if not DS9FXSavedConfig.LifeSupport == 1:
                return 
        HandleCustom.HandleCustomDamage(pObject, pEvent)

# ET_MUSIC_DONE related
def MusicDoneHandling(pObject, pEvent):
        HandleMusicDone()

def HandleMusicDone():
        DynamicMusicHandling.InjectDummyMusicName()
        MusicTypeSelector.SelectType("MusicDone")
        DynamicMusicHandling.RestoreMusicName()

# ET_MUSIC_CONDITION_CHANGED related
def MusicConditionChangedHandling(pObject, pEvent):
        HandleMusicConChanged()

def HandleMusicConChanged():
        DynamicMusicHandling.RestoreMusicName()
        MusicTypeSelector.SelectType("MusicConChanged")

# ET_MVAM_SEP related
def MVAMSeperationHandling(pObject, pEvent):
        reload (DS9FXSavedConfig)
        if not DS9FXSavedConfig.LifeSupport == 1:
                return
        HandleMVAM.HandleSep(pObject, pEvent)

# ET_MVAM_REIN related
def MVAMReintegrationHandling(pObject, pEvent):
        reload (DS9FXSavedConfig)
        if not DS9FXSavedConfig.LifeSupport == 1:
                return
        HandleMVAM.HandleRein(pObject, pEvent)

# ET_EVENT related
def KeyEventHandling(pObject, pEvent):
        global bAllowPrint

        if not hasattr(pEvent, 'GetInt'):
                return 0

        Int = pEvent.GetInt()

        if (Int == 5000):
                if bAllowPrint == 1:
                        ConsolePrintOut()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def ConsolePrintOut():
        global bAllowPrint

        reload (DS9FXSavedConfig)        
        if DS9FXSavedConfig.DebugMode == 1:
                bAllowPrint = 0

                App.TopWindow_GetTopWindow().ToggleConsole()

                pTopWindow = App.TopWindow_GetTopWindow()
                pConsole = pTopWindow.FindMainWindow(App.MWT_CONSOLE)
                pCon = App.TGConsole_Cast(pConsole.GetFirstChild())
                pCon.AddConsoleString("### Console Dump...")
                pCon.EvalString("### Saved!")

                import Custom.DS9FX.DS9FXLib.PrintConsole

                Custom.DS9FX.DS9FXLib.PrintConsole.Print()

                App.TopWindow_GetTopWindow().ToggleConsole()

                pSequence = App.TGSequence_Create()
                pAction = App.TGScriptAction_Create(__name__, "RestorebAllowPrint")
                pSequence.AddAction(pAction, None, 1)
                pSequence.Play()   

        else:
                return

def RestorebAllowPrint(pAction):
        global bAllowPrint
        bAllowPrint = 1

        return 0
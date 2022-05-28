pModule = __import__("Custom.UnifiedMainMenu.ConfigModules.Options.BCSTheBeginning")
pOption = pModule.SRCutscene
CutScene = pOption

pEngineering = pModule.EngineeringOption
EngineeringOption = int(pEngineering)

#############################################################################
# SilentRunning.py
# v0.1 by Lost_Jedi -- 8/27/2005
# v0.2 by Wowbagger -- 8/29/2005
# v0.2.1 Updated by USS Sovereign -- 01/09/2005
# v0.2.2 Updated by Lost_Jedi -- 01/09/2005
# v0.3 Updated by USS Sovereign -- 03/09/2005
# v0.4 Updated by Wowbagger -- 07/09/2005... or 9/7/05 if you're an Imperialist
# American like me.
# v0.4.1 Updated by Wowbagger -- 9/11/2005: 0.4.1 is dedicated to the memory of
# those who fell.
# V0.4.2 Updated By Lost_Jedi -- 13/11/2005
# v0.5 updated by USS Sovereign -- 19/11/2005
# v0.5.1 updated by USS Sovereign -- 30/10/2005
# v0.5.2 updated by Wowbagger -- 2/19/2006
# A Joint Project of lost_jedi, Wowbagger and USS Sovereign. 
#
# Drops power levels and thereby hides player ship from enemy sensors
# for a limited amount of time.
#
# Wowbagger's notes:
# USS Sovereign's notes:
# Wowbagger yet again deleted qbr restart handlers, smacks wowbagger!
# Also implemented engineering menu fix!
#############################################################################
# CUSTOMIZATION DATA
# ConfigFile: Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs.BCSTBConfig
# Variable = "SRCutsceneDefault"
# States:           SRCutsceneDefault = "ON"    -- Turns the cutscene ON                                     
#                   SRCutsceneDefault = "OFF"   -- Turns the cutscene OFF                                     
####################################################################################
# Imports
import App
import Foundation
import Bridge.EngineerMenuHandlers
import Bridge.BridgeUtils
import Libs.LibEngineering
import MissionLib
import Custom.NanoFXv2.NanoFX_Lib
import Libs.LibEngineering
import Libs.BCSTNGLib

# Mod Info Block.  Used for MP loading.
MODINFO = {     "Author": "\"BCS:TNG\" <http://bcscripterstng.forumsplace.com/>",
                "Version": "0.5.3",
                "License": "GPL",
                "Description": "Silent Running",
                "needBridge": 0
            }

# Variables
global i
i = 0
dict_PowerLevels = {}


## Section I: Initialization
# Add the buttton.
def init():
                global pMenu, pButtonMax, pButtonAvg, pButtonElp, pButtonSil

                # as we all agreed, disable these mods in MP to prevent cheating ;) -- USS Sovereign
                if App.g_kUtopiaModule.IsMultiplayer():
                        return

                if not Libs.LibEngineering.CheckActiveMutator("BCS:TB: Silent Running"):
                        return

                # Start with the menu.
                if EngineeringOption == 1:
                        pMenu       = Libs.BCSTNGLib.CreateEngineerMenu("Silent Running", "Engineer")
                else:
                        pBrexMenu   = Libs.LibEngineering.GetBridgeMenu("Engineering")
                        pMenu       = App.STMenu_CreateW(App.TGString("Silent Running"))
                        pBrexMenu.PrependChild(pMenu)

                # Now the subbuttons, with actual functions involved. Make certain to add in reverse order of desired appearence.
                pButtonElp  = Libs.BCSTNGLib.CreateButton("Elapsed Time: N/A", "Engineer", __name__ + ".PassClick", "Silent Running")
                pButtonAvg  = Libs.BCSTNGLib.CreateButton("Average Time To Detection: N/A", "Engineer", __name__ + ".PassClick", "Silent Running")
                pButtonMax  = Libs.BCSTNGLib.CreateButton("Maximum Time To Detection: N/A", "Engineer", __name__ + ".PassClick", "Silent Running")
                pButtonSil  = Libs.BCSTNGLib.CreateButton("Enable Silent Running", "Engineer", __name__ + ".SilentRunning", "Silent Running")

    
## Section II: Main Code
# Engineering, go to Silent Running.
def SilentRunning(pObject, pEvent): 
                global i, CorePower, MainPower, MainPowerCap, BatteryPower, pDetectionTimer, pCountdownTimer, dict_PowerLevels, pConditionSilentAndDeep, pConditionNotShot, iStartingSeconds, iIterationSeconds, iAverage, iPreviousPAPU, pButtonMax, pButtonAvg, pButtonElp, pButtonSil, pMenu, iTimeElapsed, pPlayer
                pGame	        = App.Game_GetCurrentGame()
                pEpisode	= pGame.GetCurrentEpisode()
                pMission	= pEpisode.GetCurrentMission()
                pPlayer         = MissionLib.GetPlayer()
                pPower          = pPlayer.GetPowerSubsystem()
                pWarp           = pPlayer.GetWarpEngineSubsystem()

                # (Alternate function for same button)
                if i == 1:
                        EndSilent(None)
                        return
                        
                # If we are doing in system warp then we cannot initiate SR. I tried dozens of solutions and this is the best one. - by USS Sovereign, I'm damn good :)
                # How does it work? It initializes SR but the ship powers up immediately. To remake this I have to make some serious modifications. 
                # Meaning new functions to the script and the console report is not very clean but this requires (I repeat it again) new function
                # or new def of EndSilentRunning. This is just a prototype or a release candidate. It's up to you guys.
                if pPlayer.IsDoingInSystemWarp():
                        QuickEndSilent(None, None)
                        return

                # Confirming that we are distant enough from enemy fleet to enter silent mode, sir.    
                pConditionFarEnoughAway = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 100.0, pPlayer.GetName(), pMission.GetEnemyGroup())
                if (pConditionFarEnoughAway.GetStatus() == 1):
                        print "SR: Too close."
                        return

                # Bridge to Engineering.  Status report.
                #CorePower       = pPower.GetCondition()
                CorePower       = pPower.GetPowerOutput()
                MainPower       = pPower.GetMainBatteryPower()
                MainPowerCap    = pPower.GetMainConduitCapacity()
                BatteryPower    = pPower.GetBackupBatteryPower()
                try:
                        dict_PowerLevels["Impulse"] = pPlayer.GetImpulseEngineSubsystem().GetPowerPercentageWanted() * 1.66 # Engines have something funny about them with PL's.
                        if dict_PowerLevels["Impulse"] > 1.50:
                                dict_PowerLevels["Impulse"] = 1.50
                except AttributeError:
                        dict_PowerLevels["Impulse"] = 0
                try:
                        dict_PowerLevels["Shields"] = pPlayer.GetShields().GetPowerPercentageWanted()                 
                except AttributeError:
                        dict_PowerLevels["Shields"] = 0
                try:
                        dict_PowerLevels["Sensors"] = pPlayer.GetSensorSubsystem().GetPowerPercentageWanted()        
                except AttributeError:
                        dict_PowerLevels["Sensors"] = 0
                try:
                        dict_PowerLevels["Phasers"] = pPlayer.GetPhaserSystem().GetPowerPercentageWanted()            
                except AttributeError:
                        dict_PowerLevels["Phasers"] = 0
                try:
                        dict_PowerLevels["Torpedoes"] = pPlayer.GetTorpedoSystem().GetPowerPercentageWanted()
                except AttributeError:
                        dict_PowerLevels["Torpedoes"] = 0
                try:
                        dict_PowerLevels["Pulses"]  = pPlayer.GetPulseWeaponSystem().GetPowerPercentageWanted()       
                except AttributeError:
                        dict_PowerLevels["Pulses"] = 0

                
                # Engineering responding, captain.  All systems powering down.
                #pPower.SetCondition(0)
                pPower.GetProperty().SetPowerOutput(CorePower - CorePower)
                pPower.SetMainBatteryPower(MainPower/15)
                pPower.GetProperty().SetMainConduitCapacity(MainPower - MainPower)                      # This line's brilliant idea by USS Sovereign.
                # None of the below SPTS()'s work.  Thought you might like to know that.
                Bridge.EngineerMenuHandlers.SetPowerToSubsystem(pPlayer.GetShields(), 0.00)             # At most, you can get hit by one torpedo before your shields automatically go back to 100%.  This way saves power. 
                Bridge.EngineerMenuHandlers.SetPowerToSubsystem(pPlayer.GetSensorSubsystem(), 0.05)     # Saving backup power with this, and preventing the CPU from automatically compensating for lack of power.
                Bridge.EngineerMenuHandlers.SetPowerToSubsystem(pPlayer.GetPhaserSystem(), 0.00)        # Well, you won't be needing guns, will you?
                Bridge.EngineerMenuHandlers.SetPowerToSubsystem(pPlayer.GetTorpedoSystem(), 0.00)       #       "       "       "       "       "  <--Those are ditto marks, BTW.
                Bridge.EngineerMenuHandlers.SetPowerToSubsystem(pPlayer.GetPulseWeaponSystem(), 0.00)   #       "       "       "       "       "
                Bridge.BridgeUtils.DisableButton(None, "Helm", "Set Course")
                Bridge.BridgeUtils.DisableWarpButton()

                # Captain, the enemy ships seem to be having some trouble pinpointing our location.
                iNumShips = MakeShipInvisible(pPlayer)

                # Keep an eye out for anything that might let them find us.
                pConditionSilentAndDeep = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 50.0, pPlayer.GetName(), pMission.GetEnemyGroup())  # Make sure no one's sensors have caught us yet.
                #pConditionNotShot = App.ConditionScript_Create("Conditions.ConditionAttacked", "ConditionAttacked", pPlayer.GetName(), 0.001, 0.001, 1) # If we're hit by a random torpedo, it's over.
                pSaffiButton = GetMenuButton("Commander", "End Combat")

                        
                pSaffiQBR = GetQBRMenuButton("Commander", "Configure")
        
                if pSaffiButton:
                        pSaffiButton.AddPythonFuncHandlerForInstance(App.ET_ST_BUTTON_CLICKED, __name__ + ".QuickEndSilent")
                        
                if pSaffiQBR:
                        pSaffiQBR.AddPythonFuncHandlerForInstance(App.ET_ST_BUTTON_CLICKED, __name__ + ".QuickEndSilent")
                        
                MissionLib.CallFunctionWhenConditionChanges(pMission, __name__, "EndSilent", pConditionSilentAndDeep)
                #MissionLib.CallFunctionWhenConditionChanges(pMission, __name__, "EndSilent", pConditionNotShot)
                pPlayer.AddPythonFuncHandlerForInstance(App.ET_WEAPON_FIRED, __name__ + ".EndSilent")        
                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ShipExploding")
                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SET_PLAYER, pMission, __name__ + ".QuickEndSilent")

                # Enemy sensor sweeps *will* eventually find us, sir.
                iStartingSeconds = App.g_kSystemWrapper.GetRandomNumber(600) + 1
                try:
                        iStartingSeconds = iStartingSeconds/iNumShips         
                        iAverage = 300/iNumShips
                        iTimeElapsed = 0
                        #print "Seconds to Detection: ", iStartingSeconds            
                except ZeroDivisionError:                                   
                        #print "Seconds to Detection: ", iStartingSeconds            
                        iAverage = 300
                        iTimeElapsed = 0
                
                #print "Starting:  Available: ", pPower.GetAvailablePower(), "Dispensed: ", pPower.GetPowerDispensed()

                # Checker.  We need this.
                if pPower.GetBackupConduitCapacity()  == 0:
                        pPower.GetBackupConduitCapacity(0.00000000000001)

                # This is me being nice--a variant of the iPAPU line in CountdownIncrement(), this just gives people an
                # extra one second to get set before the computer starts causing them lots of power-based pain.
                iPercentAvailablePowerUsed = pPower.GetBackupConduitCapacity()/pPower.GetBackupConduitCapacity() * 100 - 50

                # We need this variable in CountdownIncrement()
                iPreviousPAPU = 0

                # Build the timer.
                pCountdownTimer = MissionLib.CreateTimer(Libs.LibEngineering.GetEngineeringNextEventType(), __name__ + ".CountdownIncrement", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)

                # Button status updating... program complete.  Execute when ready.
                # Tee hee.  Why recalculate when you can piggyback?
                pButtonSil.SetName(App.TGString("End Silent Running"))
                pButtonMax.SetName(App.TGString(str(int(iAverage + 300)) + " (Max.) Time To Detection"))
                pButtonAvg.SetName(App.TGString(str(int(iAverage)) + " (Avg.) Time To Detection"))
                pButtonElp.SetName(App.TGString(str(iTimeElapsed) + " Seconds Elapsed"))

                # Their sensor arrays don't matter; steady as she goes, CONN.  Power up on my mark.
                i = 1


# Reevaluates time left every second to detection based on current power levels.
def CountdownIncrement(pObject, pEvent):
                global pMenu, pButtonMax, pButtonAvg, pButtonElp, pCountdownTimer, iAverage, iStartingSeconds, iIterationSeconds, iPreviousPAPU, iTimeElapsed
                pPlayer         = MissionLib.GetPlayer()
                pPower          = pPlayer.GetPowerSubsystem()

                if pPower.GetBackupConduitCapacity()  == 0:
                        pPower.GetProperty().SetBackupConduitCapacity(0.00000000000001)
                
                # Yields the absolute value of the distance from 50% usage.
                iPercentAvailablePowerUsed = pPower.GetPowerDispensed()/pPower.GetBackupConduitCapacity() * 100 - 50

                # Info Dump #1
                #print "Available: ", pPower.GetBackupConduitCapacity(), "Dispensed: ", pPower.GetPowerDispensed(), "iPAPU: ", iPercentAvailablePowerUsed, "Previous iPAPU: ", iPreviousPAPU, "Seconds Left: ", iStartingSeconds, "Average Left: ", iAverage
                
                # Recalculate the total number of seconds the player *would* have had if he had started out with this power level,
                # having already subtracted those seconds he would have then proceeded to use.  Make sure not to double adjust each
                # iteration, by adding in a checker to see precisely how much the PAPU has changed since the last iteration.
                # Do not ask the machine why it works; just believe it.  Computers are always right.  You will listen to your computer.  Stare into your monitor's pixels...  you are getting sleepy...
                iStartingSeconds = iStartingSeconds * (1 - ((iPercentAvailablePowerUsed/100) - (iPreviousPAPU/100))) - 1

                # Do the exact same thing here so we can put this number on the big board.
                iAverage = iAverage * (1 - ((iPercentAvailablePowerUsed/100) - (iPreviousPAPU/100))) - 1

                # Check if we've finally been detected.
                if iStartingSeconds <= 0:
                        EndSilent(None, None)
                        return
                    
                # Okay, we're good.  Keep going.        
                # Necessary for the next recalculation of iStartingSeconds
                iPreviousPAPU = iPercentAvailablePowerUsed

                # Change the button name to reflect our new average.
                iPostedAverage = int(iAverage + 0) # int() requires addition.  I don't know why.  I just don't question it.
                iTimeElapsed = iTimeElapsed + 1

                pButtonMax.SetName(App.TGString(str(int(iAverage + 300)) + " (Max.) Time To Detection"))
                pButtonAvg.SetName(App.TGString(str(int(iAverage)) + " (Avg.) Time To Detection"))
                pButtonElp.SetName(App.TGString(str(iTimeElapsed) + " Seconds Elapsed"))      

                # Rebuild the timer.
                pCountdownTimer = MissionLib.CreateTimer(Libs.LibEngineering.GetEngineeringNextEventType(), __name__ + ".CountdownIncrement", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)

                           
# MARK!        
def EndSilent(bStatus, pObject = None):
                global i, CorePower, MainPower, MainPowerCap, BatteryPower, pDetectionTimer, pCountdownTimer, pMenu, pButtonMax, pButtonAvg, pButtonElp, pButtonSil, dict_PowerLevels, pConditionSilentAndDeep, pConditionNotShot, pPlayer
                pGame	        = App.Game_GetCurrentGame()
                pEpisode	= pGame.GetCurrentEpisode()
                pMission	= pEpisode.GetCurrentMission()
                pFriendlyGroup  = pMission.GetFriendlyGroup()
                pPower          = pPlayer.GetPowerSubsystem()
                pHull           = pPlayer.GetHull()
                pWarp           = pPlayer.GetWarpEngineSubsystem()


                # Reset target list.
                pFriendlyGroup.AddName(pPlayer.GetName())
                pPlayer.SetTargetable(1)

                # Reset visibility.
                MakeShipVisible(pPlayer)

                # Reset power levels.
                #pPower.SetCondition(CorePower)
                pPower.GetProperty().SetPowerOutput(CorePower)
                pPower.SetMainBatteryPower(MainPower)
                pPower.GetProperty().SetMainConduitCapacity(MainPowerCap)

                # Reset subsystem power levels.
                Bridge.EngineerMenuHandlers.SetPowerToSubsystem(pPlayer.GetImpulseEngineSubsystem(), 1.25)          # Impulse is just too screwy too often to trust to the dictionary.
                Bridge.EngineerMenuHandlers.SetPowerToSubsystem(pPlayer.GetShields(), dict_PowerLevels["Shields"])                  
                Bridge.EngineerMenuHandlers.SetPowerToSubsystem(pPlayer.GetSensorSubsystem(), dict_PowerLevels["Sensors"])
                Bridge.EngineerMenuHandlers.SetPowerToSubsystem(pPlayer.GetPhaserSystem(), dict_PowerLevels["Phasers"])             
                Bridge.EngineerMenuHandlers.SetPowerToSubsystem(pPlayer.GetTorpedoSystem(), dict_PowerLevels["Torpedoes"])          
                Bridge.EngineerMenuHandlers.SetPowerToSubsystem(pPlayer.GetPulseWeaponSystem(), dict_PowerLevels["Pulses"])         
                Bridge.BridgeUtils.EnableButton(None, "Helm", "Set Course")
                Bridge.BridgeUtils.RestoreWarpButton()

                # Reset timers.
                try:
                    App.g_kTimerManager.DeleteTimer(pDetectionTimer.GetObjID())
                    App.g_kRealtimeTimerManager.DeleteTimer(pDetectionTimer.GetObjID())
                    pDetectionTimer = None
                except:
                    print "SR: pDetectionTimer already deleted.  Proceed."

                try:
                    App.g_kTimerManager.DeleteTimer(pCountdownTimer.GetObjID())
                    App.g_kRealtimeTimerManager.DeleteTimer(pCountdownTimer.GetObjID())
                    pCountdownTimer = None
                except:
                    print "SR: pCountdownTimer already deleted.  Proceed."

                # Reset listeners.
                if pConditionSilentAndDeep:
                        MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "EndSilent")
                pSaffiButton = GetMenuButton("Commander", "End Combat")

                pSaffiQBR = GetQBRMenuButton("Commander", "Configure")
        
                if pSaffiQBR:
                        pSaffiQBR.RemoveHandlerForInstance(App.ET_ST_BUTTON_CLICKED, __name__ + ".QuickEndSilent")

                if pSaffiButton:
                        pSaffiButton.RemoveHandlerForInstance(App.ET_ST_BUTTON_CLICKED, __name__ + ".QuickEndSilent")
                
                pPlayer.RemoveHandlerForInstance(App.ET_WEAPON_FIRED, __name__ + ".EndSilent")        
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ShipExploding")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_SET_PLAYER, pMission, __name__ + ".QuickEndSilent")

                # Reset buttons.       
                pButtonSil.SetName(App.TGString("Resetting Silent Running"))
                pButtonMax.SetName(App.TGString("Maximum Time To Detection: N/A"))
                pButtonAvg.SetName(App.TGString("Average Time To Detection: N/A"))
                pButtonElp.SetName(App.TGString("Elapsed Time: N/A"))
                i = 0

                # Disable the button for a while.
                pButtonSil.SetDisabled()
                pDisabilityTimer = MissionLib.CreateTimer(Libs.LibEngineering.GetEngineeringNextEventType(), __name__ + ".ReenableButton", App.g_kUtopiaModule.GetGameTime() + 30, 0, 0)


## Section III: Handlers and Hamburger Helpers
## Does that name make sense?  Only if you play it backwards.  Then it says, "CaptainKeyes is dead."
# No power flow = no sensor lock = no target.  Unless you have blind fire.
def MakeShipInvisible(pShip):
                pGame	        = App.Game_GetCurrentGame()
                pEpisode	= pGame.GetCurrentEpisode()
                pMission	= pEpisode.GetCurrentMission()
                pSet            = pShip.GetContainingSet()
                pFriendlyGroup  = pMission.GetFriendlyGroup()
                pEnemyGroup     = pMission.GetEnemyGroup()
                lpEnemies       = pEnemyGroup.GetActiveObjectTupleInSet(pSet)

                # Make the ship disappear.
                pShip.SetTargetable(0)
                pFriendlyGroup.RemoveName(pShip.GetName()) # QB ships can blind fire on vessels.  Fortunately, they only attack Friendlies.

                # Play the sound.
                pSound = App.TGSound_Create("sfx/Custom/SilentRunning/v0.4 SFX/BrexPowerDown3.wav", "InvisibleSound", 0)
                pSound.SetSFX(0)
                pSound.SetInterface(1)
                App.g_kSoundManager.PlaySound("InvisibleSound")
                
                
                # Set to Red Alert condition.  Dark bridges are cool.
                RedAlert = App.TGIntEvent_Create()
                RedAlert.SetDestination(App.Game_GetCurrentGame().GetPlayer())
                RedAlert.SetEventType(App.ET_SET_ALERT_LEVEL)
                RedAlert.SetInt(App.Game_GetCurrentGame().GetPlayer().RED_ALERT)
                App.g_kEventManager.AddEvent(RedAlert)
                
                # If cutscene is enabled then start the Cutscene for Silent Running
                if CutScene == "ON":
                        pSequence = App.TGSequence_Create ()
                        pSequence.AppendAction (App.TGScriptAction_Create("MissionLib", "StartCutscene"))
                        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
                        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pShip.GetContainingSet().GetName ()))
                        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", pShip.GetContainingSet().GetName(), pShip.GetName ()))
                        pSequence.AddAction(Custom.NanoFXv2.NanoFX_Lib.CreateFlickerSeq(pShip, 1.50, sStatus = "Off"), App.TGAction_CreateNull(), 1.0)
                        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pShip.GetContainingSet().GetName ()))
                        if App.g_kSetManager.GetSet("bridge"):
                                pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "bridge")
                                pSequence.AppendAction(pAction)
                        pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "EndCutscene"))
                        pSequence.Play()
                    
                # If cutscene has been disabled then
                if CutScene == "OFF":
                        pSequence = App.TGSequence_Create ()
                        pSequence.AddAction(Custom.NanoFXv2.NanoFX_Lib.CreateFlickerSeq(pShip, 1.50, sStatus = "Off"), App.TGAction_CreateNull(), 1.0)
                        if App.g_kSetManager.GetSet("bridge"):
                                pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "bridge")
                                pSequence.AppendAction(pAction)
                        #pSequence.AddAction (App.TGScriptAction_Create("MissionLib", "StartCutscene"))
                        #pSequence.AddAction(App.TGScriptAction_Create("MissionLib", "EndCutscene"))
                        pSequence.Play()            

                # Rotate through all enemy targets to make them lose the invisible one.
                # Enemies targeting the invisible ship will now target their next target.
                n = 0
                iNumShips = 0
                for pEnemy in lpEnemies:
                        while n + 1 < len(lpEnemies):
                            pEnemy.SetTarget(pEnemy.GetNextTarget())
                            n = n + 1
                            
                        iNumShips = iNumShips + 1

                # As long as we were iterating, I figured we might as well get this done, too.
                return iNumShips


# The opposite of MakeShipInvisible.  My, what a bright young lad you are!
def MakeShipVisible(pShip):
                # Play the sound.
                pSound = App.TGSound_Create("sfx/Custom/SilentRunning/v0.4 SFX/BrexPowerUp3.mp3", "VisibleSound", 0)
                pSound.SetSFX(0)
                pSound.SetInterface(1)
                App.g_kSoundManager.PlaySound("VisibleSound")

                pSequence = App.TGSequence_Create()
                pSequence.AddAction(Custom.NanoFXv2.NanoFX_Lib.CreateFlickerSeq(pShip, 1.5, sStatus = "On"), App.TGAction_CreateNull(), 1.0)
                pSequence.Play()
                        
                return 0    # Clear proof that Nano also codes in C, C++, and/or C#.  :)



## Section IV: Second-Level Handlers and QB Infrastructure
# Re-enables the button after EndSilent().  Mostly for game balance.
def ReenableButton(pObject, pEvent):
                global pButtonSil
                pButtonSil.SetName(App.TGString("Enable Silent Running"))
                pButtonSil.SetEnabled()


# Handler for clicking non-clickable menu buttons.
def PassClick(pObject, pEvent):
                return

    
# A quickie to ensure that the button is promptly reenabled.
def QuickEndSilent(pObject, pEvent):
                EndSilent(None)
                ReenableButton(None, None)


# Checks on anything in the set that is exploding.        
def ShipExploding(pObject, pEvent):
                pPlayer = App.Game_GetCurrentGame().GetPlayer()

                # Get the ship that is exploding.
                pShip = App.ShipClass_Cast(pEvent.GetDestination())
                if (pShip != None):
                        iShipID = pShip.GetObjID()
                        if pPlayer and pShip.GetName() == pPlayer.GetName():
                                # It's us.  Reset SR.
                                EndSilent(None)
                                ReenableButton(None, None)


# From the Menu Cleanup Brigade Lib, by Wowbagger:
def GetMenuButton(sMenuName, sButtonName):
                pMenu = GetBridgeMenu(sMenuName)
                if not pMenu:
                        #print "No Such Menu  " + sButtonName + ".  You order the cheeseburger which exists not."
                        return

                # Grab the starting button.    
                pButton = pMenu.GetButton(sButtonName)
                if not pButton:
                        pButton = pMenu.GetSubmenu(sButtonName)
                        if not pButton: 
                                #print "No Such Button as " + sButtonName + ".  Any button you see is merely the product of a deranged imagination.  Mine, to be precise."
                                return
                return pButton


# From ATP_GUIUtils:
def GetBridgeMenu(menuName):
                pTactCtrlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
                pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
                if(pDatabase is None):
                        return
                return pTactCtrlWindow.FindMenu(pDatabase.GetString(menuName))

# new addon added qbr restart menu handelers

# get the qbr menu button 

def GetQBRMenuButton(sMenuName, sButtonName):
        pMenu = GetBridgeMenu(sMenuName)
        if not pMenu:
                return

        # Grab the starting button.    
        pButton = pMenu.GetButton(sButtonName)
        if not pButton:
                pButton = pMenu.GetSubmenu(sButtonName)
                if not pButton: 
                        return
        return pButton


# From ATP_GUIUtils to get qbr button modified by USS Sovereign

def GetQBRBridgeMenu(menuName):
	pTactCtrlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/QBRrestart.tgl")
	if(pDatabase is None):
		return
	return pTactCtrlWindow.FindMenu(pDatabase.GetString(menuName))

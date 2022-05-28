from bcdebug import debug
pModule = __import__("Custom.UnifiedMainMenu.ConfigModules.Options.BCSTheBeginning")
pOption = pModule.ESRHullCustomizationOption
CustomizationOption = int(pOption)

pEngineering = pModule.EngineeringOption
EngineeringOption = int(pEngineering)

##################################################################################################
# Emergency Repair v0.8.4 -- Last Updated by Wowbagger 26/02/2006
#
# Shuts down damaged systems to hasten repairs.
#
# CREDITS: Defiant for QBautostart, Tuvok 1101 for the idea.
#
# CODERS: USS Sovereign and Wowbagger
#
# Permission Issues: Ask before modifying!  Seriously!  Only BCS: TNG can
# modify it without express permission (unless and until we disband).  We were
# recently quite badly robbed of code by an unnamed coder who has since
# apologized, but we really do read virtually everything on BCU and BCF--and we
# *know* our code.  (Code borrowing: Give us a little credit in your comments
# and the readme.  We really couldn't care less, and would in fact be honored,
# if you learned scripting by piecing together bits of our code in new ways.
# All we want is credit for any code closely based on ours.)
#
# Update notes by Wowbagger 2/15/06:
# Modified ESR for UMM compatibility, solving most customization issues forever.
# Finally.
#
# Update notes -- USS Sovereign 24/02/2006
# Removed UMM menu fix and implemented Engineering menu fix!
#
# Update notes by Wowbagger 2/25/06:
# Right back atcha' Sov!  Reimplemented UMM menu fix using BCSTNGLib fix.
###################################################################################################
###############################################################################################################################
# CUSTOMIZATION DATA
# ConfigFile: Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs.BCSTBConfig
# Variable = "ESRHullCustomizationOptionDefault"
# States:   1:  No Hull Repair allowed.
#           2:  Hull Repair shuts down all shields during repair. 
#           3:  Hull Repair drains 50% of shield power and shuts down all engines during repair.  (Wowbagger's Recommendation!)
#           4:  Hull Repair drains 50% of shield power during repair.  (CaptainKeyes's Recommendation!)
#           5:  Hull Repair shuts down all engines during repair and for twenty seconds thereafter.
#           6:  Hull Repair shuts down all engines during repair.  
#           7:  Hull Repair shuts down all sensors during repair.  (USS Sovereign's Recommendation!)
###############################################################################################################################

### Preloads
## Imports
import App
import MissionLib
import Libs.LibEngineering
import Bridge.BridgeUtils
import Bridge.EngineerMenuHandlers
import AI.Player.Stay
import Libs.BCSTNGLib

## Vars
bButtonFunctionSignal	= 0
dESR                    = {}
pHullButton             = None # Due to custom option #1, pHullButton needs a special declaration.
SUBSYSTEM_SET_CONDITION = 194
SET_SHIELD_CONDITION = 199

## Mod Info Block.  Used for MP loading.
MODINFO = {     "Author": "\"BCS:TNG\" <http://bcscripterstng.forumsplace.com/>",
                "Version": "0.8.2",
                "License": "GPL",
                "Description": "Emergency Repair",
                "needBridge": 0
            }


### Main Loop
## Section I: Initialization
# Initialization -- Make the menu.
def init():
                debug(__name__ + ", init")
                global bButtonFunctionSignal, pECSMaster, pPowerButton, pImpulseButton, pSensorsButton, pCloakingDeviceButton, pShieldsButton, pShieldFacesButton, pPhasersButton, pTorpedoesButton, pPulseWeaponsButton, pTractorsButton, pHullButton, pCancel
                pGame           = App.Game_GetCurrentGame()
                pEpisode        = pGame.GetCurrentEpisode()
                pMission        = pEpisode.GetCurrentMission()
                pPlayer 	= MissionLib.GetPlayer()		
                pPower   	= pPlayer.GetPowerSubsystem()
                pImpulse        = pPlayer.GetImpulseEngineSubsystem()
                pShields	= pPlayer.GetShields()
                pSensors        = pPlayer.GetSensorSubsystem()
                pPhasers        = pPlayer.GetPhaserSystem()
                pTorpedoes      = pPlayer.GetTorpedoSystem()
                pPulseWeapons   = pPlayer.GetPulseWeaponSystem()
                pTractors	= pPlayer.GetTractorBeamSystem()
                pCloakingDevice = pPlayer.GetCloakingSubsystem()
                pHull 		= pPlayer.GetHull()
                bButtonFunctionSignal = 0

                # as we all agreed, disable these mods in MP to prevent cheating ;) -- USS Sovereign
                #if App.g_kUtopiaModule.IsMultiplayer():
                #        return

                if not Libs.LibEngineering.CheckActiveMutator("BCS:TB: Emergency Repair"):
                        return

                # Get the dict working at default levels.
                ResetDESR()

                # Power up our customized globals.
                CheckCustomisedGlobalsForHullRepair()
                
                if not pPlayer:
                        print "Stop the madness!"
                        return

                # Add the ECS (Emergency Core Shutdown; even with all the systems in it, and
                # the "official" name change that's the name.  Cope) menu to Brex's list.
                pBridge = App.g_kSetManager.GetSet('bridge')
                pBrexMenu = Bridge.BridgeUtils.GetBridgeMenu('Engineer')

                if EngineeringOption == 1:
                        pECSMaster = Libs.BCSTNGLib.CreateEngineerMenu("Emergency Repair", "Engineer")
                else:
                        pECSMaster = App.STMenu_CreateW(App.TGString("Emergency Repair"))
                        pBrexMenu.InsertChild(-1, pECSMaster, 0, 0, 0)

                # Build buttons in order opposite of that desired in the menu.
                pCancel = Libs.LibEngineering.CreateMenuButton("Cancel Repairs", "Engineer", __name__ + ".CancelRepairs", 0, pECSMaster)
                # NEW, a way to cancel or disable repairs or you can just also click on the active button cause this just also forces the system back online
                # P.S. no need for an if statement :)  --USS Sovereign 
		pCloakingDeviceButton = None
                if pCloakingDevice:
                        pCloakingDeviceButton	 = Libs.LibEngineering.CreateMenuButton("Cloaking Device" + " Status: Online", "Engineer", __name__ + ".CloakingDevice", 0, pECSMaster)
                if pTractors:
                        pTractorsButton	 	 = Libs.LibEngineering.CreateMenuButton("Tractors" + " Status: Online", "Engineer", __name__ + ".Tractors", 0, pECSMaster)
                if pPulseWeapons:
                        pPulseWeaponsButton 	 = Libs.LibEngineering.CreateMenuButton("Pulse Weapons" + " Status: Online", "Engineer", __name__ + ".PulseWeapons", 0, pECSMaster)   # No pulse weapons on the starting QB Galaxy class, so we improvise.
                if pTorpedoes:
                        pTorpedoesButton    	 = Libs.LibEngineering.CreateMenuButton("Torpedoes" + " Status: Online", "Engineer", __name__ + ".Torpedoes", 0, pECSMaster)
                if pPhasers:
                        pPhasersButton     	 = Libs.LibEngineering.CreateMenuButton("Phasers" + " Status: Online", "Engineer", __name__ + ".Phasers", 0, pECSMaster)
                if pImpulse:
                        pImpulseButton           = Libs.LibEngineering.CreateMenuButton("Engines" + " Status: Online", "Engineer", __name__ + ".Impulse", 0, pECSMaster)
                if pSensors:
                        pSensorsButton     	 = Libs.LibEngineering.CreateMenuButton("Sensors" + " Status: Online", "Engineer", __name__ + ".Sensors", 0, pECSMaster)
                if pPower:
                        pPowerButton       	 = Libs.LibEngineering.CreateMenuButton(str(pPower.GetName()) + " Status: Online", "Engineer", __name__ + ".Power", 0, pECSMaster)        
                if pHull:
                        if CustomizationOption != 1:
                                pHullButton 		 = Libs.LibEngineering.CreateMenuButton("Hull" + " Status: Online", "Engineer", __name__ + ".Hull", 0, pECSMaster)
                if pShields:
                        pShieldsButton     	 = Libs.LibEngineering.CreateMenuButton("Shield Generator" + " Status: Online", "Engineer", __name__ + ".Shields", 0, pECSMaster)
                        # Shield faces have their own rules.  The complete script is just after standard ESR, out of the way of the things that make sense.
                        pShieldFacesButton       = Libs.LibEngineering.CreateMenuButton("Shield Recharge", "Engineer", __name__ + ".ShieldFaces", 0, pECSMaster)
        
                # Cancel button is disabled by default
                pCancel.SetDisabled()

                # If we change players, we're going to need to rebuild this menu.  Send us to EBO(), where many disparate parts of this script finally meet.
                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SET_PLAYER, pMission, __name__ + ".EvaluateBackOnline")


## Section II: Direct System Handlers
## Handles clicks from the menu, defining what we want repaired and how.
def Shields(pObject, pEvent):
                debug(__name__ + ", Shields")
                global bButtonFunctionSignal, pShieldsButton, dESR, pPowerButton, pImpulseButton, pSensorsButton, pCloakingDeviceButton, pShieldFacesButton, pPhasersButton, pTorpedoesButton, pPulseWeaponsButton, pTractorsButton, pHullButton, pCancel
                sContinue = EvaluateBackOnline()
                if sContinue == "FALSE":
                        return

                pPlayer = MissionLib.GetPlayer()
                pShipSet = pPlayer.GetPropertySet()
                pSystemRepair = pPlayer.GetShields()

                ResetDESR()
                dESR["pSystemRepair"] = pSystemRepair
                dESR["pShipList"] = pShipSet.GetPropertiesByType(App.CT_SHIELD_PROPERTY)
                dESR["pButton"] = pShieldsButton
                dESR["pPlayer"] = MissionLib.GetPlayer()
                if pSystemRepair != None:
                        dESR["bIsCritical"] = pSystemRepair.IsCritical()
                        dESR["sSubsystemName"] = pSystemRepair.GetName()
                else:
                        dESR["bIsCritical"] = 0
			return
		    
                SetDisabledButtons()                
                bButtonFunctionSignal = 1
                ESREmergencyRepair()


def Hull(pObject, pEvent):
                debug(__name__ + ", Hull")
                global bButtonFunctionSignal, pHullButton, dESR, pPowerButton, pImpulseButton, pSensorsButton, pCloakingDeviceButton, pShieldsButton, pShieldFacesButton, pPhasersButton, pTorpedoesButton, pPulseWeaponsButton, pTractorsButton, pCancel, g_sSecondaryFunction, g_sTertiaryFunction
                sContinue = EvaluateBackOnline()
                if sContinue == "FALSE":
                        return

                pPlayer = MissionLib.GetPlayer()
                pShipSet = pPlayer.GetPropertySet()
                pSystemRepair = pPlayer.GetHull()

                ResetDESR()

                # Hull fix is in here, compare max and current condition
                # if hull is at full power send us to EvaluateBackOnline
                # that's all so simple yet genious :)
                pHull = pPlayer.GetHull()
                pHullCon = pHull.GetCondition()
                pHullMax = pHull.GetMaxCondition()

                if pHullCon == pHullMax:
                    EvaluateBackOnline()
                    return
                    
                dESR["pSystemRepair"] = pSystemRepair
                dESR["iIterationAcceleration"] = 2.3  # CT_HULL_PROPERTY also covers bridges and shuttle bays.  Plus, it takes *forever.*  It's not fair to the player to be left vulnerable for nearly 400 seconds for repairs.
                dESR["bAddPointsInProgress"] = 1
                dESR["bIsSystemShutDown"] = 0
                dESR["pShipList"] = pShipSet.GetPropertiesByType(App.CT_HULL_PROPERTY)
                dESR["pButton"] = pHullButton
                dESR["pPlayer"] = MissionLib.GetPlayer()
                dESR["sSecondaryFunction"] = g_sSecondaryFunction
                dESR["sTertiaryFunction"] = g_sTertiaryFunction
                if pSystemRepair != None:
                        dESR["bIsCritical"] = pSystemRepair.IsCritical()
                        dESR["sSubsystemName"] = pSystemRepair.GetName()
                else:
                        dESR["bIsCritical"] = 0
			return

                SetDisabledButtons()
                Bridge.BridgeUtils.DisableButton(None, "Helm", "Set Course")
        	Bridge.BridgeUtils.DisableWarpButton()
                
                bButtonFunctionSignal = 1
                ESREmergencyRepair()

                # Normally, secondary, tertiary, recovery, and endrecovery functions are placed directly below their root function.
                # However, with, at this writing, EIGHTEEN (18!) different functions of those types with the root of Hull, they
                # have been moved closer to the bottom of ESR, just above our bank of helper functions.


def Power(pObject, pEvent):
                debug(__name__ + ", Power")
                global bButtonFunctionSignal, pPowerButton, dESR, pImpulseButton, pSensorsButton, pCloakingDeviceButton, pShieldsButton, pShieldFacesButton, pPhasersButton, pTorpedoesButton, pPulseWeaponsButton, pTractorsButton, pHullButton, pCancel
                sContinue = EvaluateBackOnline()
                if sContinue == "FALSE":
                        return

                pPlayer = MissionLib.GetPlayer()
                pShipSet = pPlayer.GetPropertySet()
                pSystemRepair = pPlayer.GetPowerSubsystem()

                ResetDESR()
                dESR["pSystemRepair"] = pSystemRepair
                dESR["pShipList"] = pShipSet.GetPropertiesByType(App.CT_POWER_PROPERTY)
                dESR["pButton"] = pPowerButton
                dESR["pPlayer"] = MissionLib.GetPlayer()
                if pSystemRepair != None:
                        dESR["bIsCritical"] = pSystemRepair.IsCritical()
                        dESR["sSubsystemName"] = pSystemRepair.GetName()
                else:
                        dESR["bIsCritical"] = 0
			return

                SetDisabledButtons()
                bButtonFunctionSignal = 1
                ESREmergencyRepair()

                
def Sensors(pObject, pEvent):
                debug(__name__ + ", Sensors")
                global bButtonFunctionSignal, pSensorsButton, dESR, pPowerButton, pImpulseButton, pCloakingDeviceButton, pShieldsButton, pShieldFacesButton, pPhasersButton, pTorpedoesButton, pPulseWeaponsButton, pTractorsButton, pHullButton, pCancel
                sContinue = EvaluateBackOnline()
                if sContinue == "FALSE":
                        return

                pPlayer = MissionLib.GetPlayer()
                pShipSet = pPlayer.GetPropertySet()
                pSystemRepair = pPlayer.GetSensorSubsystem()

                ResetDESR()
                dESR["pSystemRepair"] = pSystemRepair
                dESR["pShipList"] = pShipSet.GetPropertiesByType(App.CT_SENSOR_PROPERTY)
                dESR["pButton"] = pSensorsButton
                dESR["pPlayer"] = MissionLib.GetPlayer()
                if pSystemRepair != None:
                        dESR["bIsCritical"] = pSystemRepair.IsCritical()
                        dESR["sSubsystemName"] = pSystemRepair.GetName()
                else:
                        dESR["bIsCritical"] = 0
			return

		SetDisabledButtons()            
                bButtonFunctionSignal = 1
                ESREmergencyRepair()

                
def Impulse(pObject, pEvent):
                debug(__name__ + ", Impulse")
                global bButtonFunctionSignal, pImpulseButton, dESR, pPowerButton, pSensorsButton, pCloakingDeviceButton, pShieldsButton, pShieldFacesButton, pPhasersButton, pTorpedoesButton, pPulseWeaponsButton, pTractorsButton, pHullButton, pCancel
                sContinue = EvaluateBackOnline()
                if sContinue == "FALSE":
                        return

                pPlayer = MissionLib.GetPlayer()
                pShipSet = pPlayer.GetPropertySet()
		pSystemRepair = pPlayer.GetImpulseEngineSubsystem()

                ResetDESR()
                dESR["pSystemRepair"] = pSystemRepair
                dESR["pShipList"] = pShipSet.GetPropertiesByType(App.CT_ENGINE_PROPERTY)
                dESR["pButton"] = pImpulseButton
                dESR["pPlayer"] = MissionLib.GetPlayer()
                if pSystemRepair != None:
                        dESR["bIsCritical"] = pSystemRepair.IsCritical()
                        dESR["sSubsystemName"] = "Engines"
                else:
                        dESR["bIsCritical"] = 0
			return

                # Disable both the buttons and warp menu.
                SetDisabledButtons()
                Bridge.BridgeUtils.DisableButton(None, "Helm", "Set Course")
        	Bridge.BridgeUtils.DisableWarpButton()
             
                bButtonFunctionSignal = 1
                ESREmergencyRepair()

                
def Phasers(pObject, pEvent):
                debug(__name__ + ", Phasers")
                global bButtonFunctionSignal, pPhasersButton, dESR, pPowerButton, pImpulseButton, pSensorsButton, pCloakingDeviceButton, pShieldsButton, pShieldFacesButton, pTorpedoesButton, pPulseWeaponsButton, pTractorsButton, pHullButton, pCancel
                sContinue = EvaluateBackOnline()
                if sContinue == "FALSE":
                        return

                pPlayer = MissionLib.GetPlayer()
                pShipSet = pPlayer.GetPropertySet()
                pSystemRepair = pPlayer.GetPhaserSystem()

                ResetDESR()
                dESR["pSystemRepair"] = pSystemRepair
                dESR["pShipList"] = pShipSet.GetPropertiesByType(App.CT_PHASER_PROPERTY)
                dESR["pButton"] = pPhasersButton
                dESR["pPlayer"] = MissionLib.GetPlayer()
                if pSystemRepair != None:
                        dESR["bIsCritical"] = pSystemRepair.IsCritical()
                        dESR["sSubsystemName"] = pSystemRepair.GetName()
                else:
                        dESR["bIsCritical"] = 0
			return
		    
                SetDisabledButtons()
                bButtonFunctionSignal = 1
                ESREmergencyRepair()

                
def Torpedoes(pObject, pEvent):
                debug(__name__ + ", Torpedoes")
                global bButtonFunctionSignal, pTorpedoesButton, dESR, pPowerButton, pImpulseButton, pSensorsButton, pCloakingDeviceButton, pShieldsButton, pShieldFacesButton, pPhasersButton, pPulseWeaponsButton, pTractorsButton, pHullButton, pCancel
                sContinue = EvaluateBackOnline()
                if sContinue == "FALSE":
                        return

                pPlayer = MissionLib.GetPlayer()
                pShipSet = pPlayer.GetPropertySet()
                pSystemRepair = pPlayer.GetTorpedoSystem()

                ResetDESR()
                dESR["pSystemRepair"] = pSystemRepair
                dESR["pShipList"] = pShipSet.GetPropertiesByType(App.CT_TORPEDO_TUBE_PROPERTY)
                dESR["pButton"] = pTorpedoesButton
                dESR["pPlayer"] = MissionLib.GetPlayer()
                if pSystemRepair != None:
                        dESR["bIsCritical"] = pSystemRepair.IsCritical()
                        dESR["sSubsystemName"] = pSystemRepair.GetName()
                else:
                        dESR["bIsCritical"] = 0
			return

                SetDisabledButtons()
                bButtonFunctionSignal = 1
                ESREmergencyRepair()

                
def PulseWeapons(pObject, pEvent):
                debug(__name__ + ", PulseWeapons")
                global bButtonFunctionSignal, pPulseWeaponsButton, dESR, pPowerButton, pImpulseButton, pSensorsButton, pCloakingDeviceButton, pShieldsButton, pShieldFacesButton, pPhasersButton, pTorpedoesButton, pTractorsButton, pHullButton, pCancel
                sContinue = EvaluateBackOnline()
                if sContinue == "FALSE":
                        return

                pPlayer = MissionLib.GetPlayer()
                pShipSet = pPlayer.GetPropertySet()
                pSystemRepair = pPlayer.GetPulseWeaponSystem()

                ResetDESR()
                dESR["pSystemRepair"] = pSystemRepair
                dESR["pShipList"] = pShipSet.GetPropertiesByType(App.CT_PULSE_WEAPON_PROPERTY)
                dESR["pButton"] = pPulseWeaponsButton
                dESR["pPlayer"] = MissionLib.GetPlayer()
                if pSystemRepair != None:
                        dESR["bIsCritical"] = pSystemRepair.IsCritical()
                        dESR["sSubsystemName"] = pSystemRepair.GetName()
                else:
                        dESR["bIsCritical"] = 0
			return
		    
                SetDisabledButtons()
                bButtonFunctionSignal = 1
                ESREmergencyRepair()


def Tractors(pObject, pEvent):
                debug(__name__ + ", Tractors")
                global bButtonFunctionSignal, pTractorsButton, dESR, pPowerButton, pImpulseButton, pSensorsButton, pCloakingDeviceButton, pShieldsButton, pShieldFacesButton, pPhasersButton, pTorpedoesButton, pPulseWeaponsButton, pHullButton, pCancel
                sContinue = EvaluateBackOnline()
                if sContinue == "FALSE":
                        return

                pPlayer = MissionLib.GetPlayer()
                pShipSet = pPlayer.GetPropertySet()
                pSystemRepair = pPlayer.GetTractorBeamSystem()

                ResetDESR()
                dESR["pSystemRepair"] = pSystemRepair
                dESR["pShipList"] = pShipSet.GetPropertiesByType(App.CT_TRACTOR_BEAM_PROPERTY)
                dESR["pButton"] = pTractorsButton
                dESR["pPlayer"] = MissionLib.GetPlayer()
                if pSystemRepair != None:
                        dESR["bIsCritical"] = pSystemRepair.IsCritical()
                        dESR["sSubsystemName"] = pSystemRepair.GetName()
                else:
                        dESR["bIsCritical"] = 0
			return
		    
                SetDisabledButtons()
                bButtonFunctionSignal = 1
                ESREmergencyRepair()


def CloakingDevice(pObject, pEvent):
                debug(__name__ + ", CloakingDevice")
                global bButtonFunctionSignal, pCloakingDeviceButton, dESR, pPowerButton, pImpulseButton, pSensorsButton, pShieldsButton, pShieldFacesButton, pPhasersButton, pTorpedoesButton, pPulseWeaponsButton, pTractorsButton, pHullButton, pCancel
                sContinue = EvaluateBackOnline()
                if sContinue == "FALSE":
                        return

                pPlayer = MissionLib.GetPlayer()
                pShipSet = pPlayer.GetPropertySet()
                pSystemRepair = pPlayer.GetCloakingSubsystem()

                ResetDESR()
                dESR["pSystemRepair"] = pSystemRepair
                dESR["pShipList"] = pShipSet.GetPropertiesByType(App.CT_CLOAKING_SUBSYSTEM_PROPERTY)
                dESR["pButton"] = pCloakingDeviceButton
                dESR["pPlayer"] = MissionLib.GetPlayer()
                if pSystemRepair != None:
                        dESR["bIsCritical"] = pSystemRepair.IsCritical()
                        dESR["sSubsystemName"] = pSystemRepair.GetName()
                else:
                        dESR["bIsCritical"] = 0
			return

                SetDisabledButtons()
                bButtonFunctionSignal = 1
                ESREmergencyRepair()


def ShieldFaces(pObject, pEvent):
                debug(__name__ + ", ShieldFaces")
                global bButtonFunctionSignal, pShieldFacesButton, dESR, pPowerButton, pImpulseButton, pSensorsButton, pCloakingDeviceButton, pShieldsButton, pPhasersButton, pTorpedoesButton, pPulseWeaponsButton, pTractorsButton, pHullButton, pCancel
                sContinue = EvaluateBackOnline()
                if sContinue == "FALSE":
                        return

                pPlayer = MissionLib.GetPlayer()
                pShipSet = pPlayer.GetPropertySet()
                pSystemRepair = pPlayer.GetShields()

                ResetDESR()
                dESR["pSystemRepair"] = pSystemRepair
                dESR["pButton"] = pShieldFacesButton
                dESR["iIterationAcceleration"] = 5
                dESR["pPlayer"] = pPlayer

                if pSystemRepair.IsOn() == 0:
                        print "ER: ...Right.  We'll recharge those inactive shields... anytime.  Don't mind me; just making a phone call to a place where you'll have lots of friends..."  
                        return
                    
                SetDisabledButtons()                    
                bButtonFunctionSignal = 2
                ShieldsEmergencyRepair()

         
## Section III: ESR: Emergency System Repair.
def ESREmergencyRepair():
                debug(__name__ + ", ESREmergencyRepair")
                global bButtonFunctionSignal, dESR
                pGame                   = App.Game_GetCurrentGame()
                pEpisode                = pGame.GetCurrentEpisode()
                pMission                = pEpisode.GetCurrentMission()
                pPlayer                 = dESR["pPlayer"]
                pButton                 = dESR["pButton"]
                pShipList               = dESR["pShipList"]
                pSystemShutdown         = dESR["pSystemShutdown"]
                pSystemShutdownList     = dESR["pSystemShutdownList"]
                pSystemRepair           = dESR["pSystemRepair"]
                iIterationAccelerator   = dESR["iIterationAcceleration"]
                sSubsystemName          = dESR["sSubsystemName"]
                sSecondaryFunction      = dESR["sSecondaryFunction"]
                bIsSystemShutDown       = dESR["bIsSystemShutDown"]
		RepairSubsystem         = pPlayer.GetRepairSubsystem()
                iParentCurrCon          = 0                                                             # That stands for Integer: Parent Subsystem Current Condition
                iParentMaxCon           = 0                                                             # You can figure this one out yourself.
                dCurrConList            = {}
                dShutdownCurrCon        = {}
                dESR["dCurrConList"]    = dCurrConList

                # Play sound A.
                pSound = App.TGSound_Create("sfx/Interface/ShutDown.wav", "ShutdownSound", 0)
                pSound.SetSFX(0)
                pSound.SetInterface(1)
                App.g_kSoundManager.PlaySound("ShutdownSound")

                # Play sound B.
                Database = pMission.SetDatabase("data/TGL/Bridge Crew General.tgl")
                Sequence = App.TGSequence_Create()
                pSet = App.g_kSetManager.GetSet("bridge")
                pEngineer = App.CharacterClass_GetObject(pSet, "Engineer")
                Sequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SAY_LINE, "ge151", None, 0, Database))
                Sequence.Play()

                # Program escape handlers in case we get a sudden termination.
                pSaffiButton = GetMenuButton("Commander", "End Combat")
                pSaffiQBR = GetQBRMenuButton("Commander", "Configure")
                if pSaffiButton:
                        pSaffiButton.AddPythonFuncHandlerForInstance(App.ET_ST_BUTTON_CLICKED, __name__ + ".EvaluateBackOnline")

                if pSaffiQBR:
                        pSaffiQBR.AddPythonFuncHandlerForInstance(App.ET_ST_BUTTON_CLICKED, __name__ + ".EvaluateBackOnline")
                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ShipExploding")

                #MovedLine: App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SET_PLAYER, pMission, __name__ + ".EvaluateBackOnline")

                # See if we have to do anything special while shutting down this system.
                if sSecondaryFunction:
                        pExecute = MissionLib.CreateTimer(Libs.LibEngineering.GetEngineeringNextEventType(), __name__ + sSecondaryFunction, App.g_kUtopiaModule.GetGameTime() + 0, 0, 0)

                # If we're shutting down the shields, we're going to shut down *everything*--not just the generator.  So 
                # we'll deal with that by giving the shields a free refill.  It's called "marketing."
                if pShipList:
                        if pSystemRepair.GetName() == pPlayer.GetShields().GetName():
                                StoreShieldData()

                # Shutdown the system and prepare for further repairs.
                if pShipList:
                        iNumItems = pShipList.TGGetNumItems()
                        pShipList.TGBeginIteration()
                        for i in range(iNumItems):
                                pShipProperty   = App.SubsystemProperty_Cast(pShipList.TGGetNext().GetProperty())
                                pChildSubsystem = pPlayer.GetSubsystemByProperty(pShipProperty)
                                iCurrCon        = pChildSubsystem.GetCondition()

                                if iCurrCon > 0:                                                        # If the system has been destroyed, just skip the rest.
                                        iMaxCon             = pChildSubsystem.GetMaxCondition()
                                        iParentCurrCon      = iParentCurrCon + iCurrCon
                                        iParentMaxCon       = iParentMaxCon + iMaxCon

                                        if bIsSystemShutDown == 1:                                      # It only matters for one subsystem, but sometimes we will want to keep the repairing system online.
                                                #pChildSubsystem.GetProperty().SetCritical(0)            # It probably isn't critical anyhow, but, hey, why mess with what works?
                                                #pChildSubsystem.GetProperty().SetTargetable(0)          # No power signature = no pinpointing by enemy sensors = no targeting.
						SetSubsystemCondition(pPlayer.GetObjID(), pChildSubsystem, pSystemRepair.GetDisabledPercentage() + 0.1)
                                dCurrConList[pChildSubsystem.GetName()] = iCurrCon                      # Store that condition to our brand spickkity new dictionary.
                        pShipList.TGDoneIterating()        

                # If we would like to shut down a system other than the system under repair, it runs through here.
                # This is mostly for hull repairs, where we repair the hull but shut down the shield generators.

                # NOTE: As with so much of this code has been since the days when all ESR (then-ECS) did was shut 
                # down the warp core, we are currently in the process of phasing out this bit of code and relegating
                # it to the Secondary and Tertiary function system (currently in use for the hull systems).  See
                # HullTertiary3HalfShieldsEngines() for an example.
                if pSystemShutdownList != None:
                        iNumItems = pSystemShutdownList.TGGetNumItems()
                        pSystemShutdownList.TGBeginIteration()
                        for i in range(iNumItems):
                                pShipProperty   = App.SubsystemProperty_Cast(pSystemShutdownList.TGGetNext().GetProperty())
                                pChildSubsystem = pPlayer.GetSubsystemByProperty(pShipProperty)
                                iCurrCon        = pChildSubsystem.GetCondition()

                                dShutdownCurrCon[pChildSubsystem.GetName()] = pChildSubsystem.GetCondition()
                                #pChildSubsystem.GetProperty().SetCritical(0)
                                #pChildSubsystem.GetProperty().SetTargetable(0)
				SetSubsystemCondition(pPlayer.GetObjID(), pChildSubsystem, pChildSubsystem.GetDisabledPercentage() + 0.1)
                        pSystemShutdownList.TGDoneIterating()

                        # We have to do the same thing for secondary shield shutdowns as for primaries.
                        if pSystemShutdown.GetName() == pPlayer.GetShields().GetName():
                                StoreShieldData()

                # If the system has been destroyed, we should know by now.
                if iParentMaxCon <= 0:
                        dESR["dCurrConList"] = dCurrConList
                        ESRBackOnline()
                        return

                # Now fix stuff that require the button and the parent.
                iIterationTime  = (iParentMaxCon)/(12000)/(iIterationAccelerator)                                               # Unlike earlier versions of this script, iteration time is not based in any way on the system's current condition, but solely on overall system complexity.
		SetSubsystemCondition(pPlayer.GetObjID(), RepairSubsystem, RepairSubsystem.GetDisabledPercentage() + 0.1)
                bIsTargetable = RepairSubsystem.GetProperty().IsTargetable()
                RepairSubsystem.GetProperty().SetTargetable(0)

                # Button name data time!
                # The int function demands (quite irrationally) to have addition involved.
                iNewStatus = int((iParentCurrCon/iParentMaxCon) * 100 + 0)
                iTimeLeft = int((100-iNewStatus) * iIterationTime)
                if iTimeLeft < iIterationTime:
                        iTimeLeft = "< " + str(int(iIterationTime + 0))

                # Name the button.
                pButton.SetName(App.TGString(str(iNewStatus) + "%/" + str(iTimeLeft) + " sec/" + str(sSubsystemName)))

                # We need these later on.  I hate globals, but, as Sneaker says, those are the rules.
                dESR["iParentMaxCon"] = iParentMaxCon
                dESR["iIterationTime"] = iIterationTime
                dESR["bIsTargetable"] = bIsTargetable
                dESR["dCurrConList"] = dCurrConList
                dESR["iIterationAcceleration"] = iIterationAccelerator
                dESR["dShutdownCurrCon"] = dShutdownCurrCon

                # If we're over 100%, force us back online.
                if iParentCurrCon/iParentMaxCon >= 1.0:
                        ESRBackOnline()
                        return

                # Set up a timer to call the incremental repairs (10% every iteration).
                pIncrementTimer = MissionLib.CreateTimer(Libs.LibEngineering.GetEngineeringNextEventType(), __name__ + ".ESRRepairIncrement", App.g_kUtopiaModule.GetGameTime() + iIterationTime, 0, 0)

                dESR["pIncrementTimer"] = pIncrementTimer


def ESRRepairIncrement(pObject, pEvent):
                debug(__name__ + ", ESRRepairIncrement")
                global dESR
                pPlayer                 = dESR["pPlayer"]
                pButton                 = dESR["pButton"]
                pShipList               = dESR["pShipList"]
                iParentMaxCon           = dESR["iParentMaxCon"]
                dCurrConList            = dESR["dCurrConList"]
                pSystemShutdownList     = dESR["pSystemShutdownList"]
                pSystemRepair           = dESR["pSystemRepair"]
                sSubsystemName          = dESR["sSubsystemName"]
                iIterationAccelerator   = dESR["iIterationAcceleration"]
                sSecondaryFunction      = dESR["sSecondaryFunction"]
                bAddPointsInProgress    = dESR["bAddPointsInProgress"]
		RepairSubsystem         = pPlayer.GetRepairSubsystem()                

    		# Give us 1% of the parent's aggregate condition to use as "points," awarded to the children for repairs.
		if not iParentMaxCon:
			return
                iParentPoints = iParentMaxCon/100
		
		# Set various things up for each child subsystem.
                if pShipList:
                        pShipList.TGBeginIteration()                                                    # Ha!  Iterate!  I said iterate, you Commie subversive!
                        iNumItems = pShipList.TGGetNumItems()
                        iParentCurrCon = 0                                                              # Re-zero the Current Condition Aggregate.
                        for i in range(iNumItems):
                                pShipProperty   = App.SubsystemProperty_Cast(pShipList.TGGetNext().GetProperty())
                                pChildSubsystem = pPlayer.GetSubsystemByProperty(pShipProperty)
                                iCurrCon        = dCurrConList[pChildSubsystem.GetName()]               # Restore the value from setup or the last iteration (or is it traversal?  CPL syntax is so confusing).

                                if iCurrCon > 0:                                                        # Is the system still in one piece?  Or any piece, for that matter?
                                        iMaxCon             = pChildSubsystem.GetMaxCondition()
                                        iParentCurrCon      = iParentCurrCon + iCurrCon
                                        iSubsystemMaxPoints = iMaxCon - iCurrCon                        # The largest number of points this child would be able to absorb.  He might not get all of it; see below.
                                        
                                        if iSubsystemMaxPoints > iParentPoints:
                                                n = -(iParentPoints - iSubsystemMaxPoints)              # Finds the positive difference between PP and SMP.
                                                iSubsystemMaxPoints = iSubsystemMaxPoints - n           # Slaps SMP on the wrist for trying to take more than PP. has right now.
                                                    
                                        iParentPoints       = iParentPoints - iSubsystemMaxPoints       # Take those points away from our total...
                                        iCurrCon            = iCurrCon + iSubsystemMaxPoints            # ... and assign them to the subsystem.
                                        dCurrConList[pChildSubsystem.GetName()] = iCurrCon              # And send our new status back to the dictionary.

                                        if bAddPointsInProgress == 1:                                   # If the system's not shut down, apply the repair points immediately.
						SetSubsystemCondition(pPlayer.GetObjID(), pChildSubsystem, iCurrCon)
                        pShipList.TGDoneIterating()

                # Now fix stuff that require the button and the parent.
                iIterationTime  = (iParentMaxCon)/(11000)/(iIterationAccelerator)                                            # Unlike earlier versions of this script, iteration time is not based in any way on the system's current condition, but solely on overall system complexity.

                # If we're over 100%, force us back online.
                if iParentCurrCon/iParentMaxCon >= 1.0:
                        ESRBackOnline()
                        return

                # Button name data time!
                # The int function demands (quite irrationally) to have addition involved.
                iNewStatus = int((iParentCurrCon/iParentMaxCon) * 100 + 0)
                iTimeLeft = int((100-iNewStatus) * iIterationTime)
                if iTimeLeft < iIterationTime:
                        iTimeLeft = "< " + str(int(iIterationTime + 0))

                # Name the button.
                pButton.SetName(App.TGString(str(iNewStatus) + "%/" + str(iTimeLeft) + " sec/" + str(sSubsystemName)))

                #print iParentMaxCon, dCurrConList, sSubsystemName, iParentCurrCon, iParentMaxCon, iNewStatus

                # Set up a timer to call the incremental repairs (10% every iteration).
                pIncrementTimer = MissionLib.CreateTimer(Libs.LibEngineering.GetEngineeringNextEventType(), __name__ + ".ESRRepairIncrement", App.g_kUtopiaModule.GetGameTime() + iIterationTime, 0, 0)



def ESRBackOnline():
                debug(__name__ + ", ESRBackOnline")
                global dESR, bButtonFunctionSignal, pPowerButton, pImpulseButton, pSensorsButton, pCloakingDeviceButton, pShieldsButton, pShieldFacesButton, pPhasersButton, pTorpedoesButton, pPulseWeaponsButton, pTractorsButton, pHullButton, pCancel
                pPlayer                 = dESR["pPlayer"]
                pButton                 = dESR["pButton"]
                pShipList               = dESR["pShipList"]
                iParentMaxCon           = dESR["iParentMaxCon"]
                dCurrConList            = dESR["dCurrConList"]
                pIncrementTimer         = dESR["pIncrementTimer"]
                bIsTargetable           = dESR["bIsTargetable"]
                bIsCritical             = dESR["bIsCritical"]
                pSystemShutdown         = dESR["pSystemShutdown"]
                pSystemShutdownList     = dESR["pSystemShutdownList"]
                pSystemRepair           = dESR["pSystemRepair"]
                sSubsystemName          = dESR["sSubsystemName"]
                dShutdownCurrCon        = dESR["dShutdownCurrCon"]
                sRecoveryFunction       = dESR["sRecoveryFunction"]
                sTertiaryFunction       = dESR["sTertiaryFunction"]
		RepairSubsystem         = pPlayer.GetRepairSubsystem()        

                # Allows access to other ESR menus.
                bButtonFunctionSignal = 0
		
		# Play the sounds!
		pGame = App.Game_GetCurrentGame()
     		pEpisode = pGame.GetCurrentEpisode()
     		pMission = pEpisode.GetCurrentMission()
     		Database = pMission.SetDatabase("data/TGL/Bridge Crew General.tgl")
     	  	Sequence = App.TGSequence_Create()
     		pSet = App.g_kSetManager.GetSet("bridge")
     		pEngineer = App.CharacterClass_GetObject(pSet, "Engineer")
     	        Sequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SAY_LINE, "ge111", None, 0, Database))
     	        Sequence.Play()		

                pSound = App.TGSound_Create("sfx/Interface/SystemsOnline.wav", "StartupSound", 0)
                pSound.SetSFX(0)
                pSound.SetInterface(1)
                App.g_kSoundManager.PlaySound("StartupSound")

                # Delete the timer.
                try:
                    App.g_kTimerManager.DeleteTimer(pIncrementTimer.GetObjID())
                    App.g_kRealtimeTimerManager.DeleteTimer(pIncrementTimer.GetObjID())
                    pIncrementTimer = None
                except AttributeError:
                    pass
                    #print "Timer already deleted.  Proceed."
            
                # Reenable those doggone buttons. This took a while to be completed, easy coding but damn do you guys realize how many damn buttons are there?
                SetEnabledButtons()

                # Restore warp button if we used Hull repair option or engine repair option
                Bridge.BridgeUtils.EnableButton(None, "Helm", "Set Course")
        	Bridge.BridgeUtils.RestoreWarpButton()
    
                # Reset handlers.
                pSaffiButton = GetMenuButton("Commander", "End Combat")
                pSaffiQBR = GetQBRMenuButton("Commander", "Configure")
                if pSaffiButton:
                        pSaffiButton.RemoveHandlerForInstance(App.ET_ST_BUTTON_CLICKED, __name__ + ".EvaluateBackOnline")
                if pSaffiQBR:
                        pSaffiQBR.RemoveHandlerForInstance(App.ET_ST_BUTTON_CLICKED, __name__ + ".EvaluateBackOnline")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ShipExploding")
                #LineObsolete: App.g_kEventManager.RemoveBroadcastHandler(App.ET_SET_PLAYER, pMission, __name__ + ".EvaluateBackOnline")
              
		# Reenergize all subsystems.
                if pShipList:
                        pShipList.TGBeginIteration()
                        iNumItems = pShipList.TGGetNumItems()
                        for i in range(iNumItems):
                                pShipProperty = App.SubsystemProperty_Cast(pShipList.TGGetNext().GetProperty())
                                pChildSubsystem = pPlayer.GetSubsystemByProperty(pShipProperty)

                                iCurrCon = dCurrConList[pChildSubsystem.GetName()]                      # Grab our Child Subsystem Current Condition Value from the list.
				SetSubsystemCondition(pPlayer.GetObjID(), pChildSubsystem, iCurrCon)
                                if iCurrCon > 0:                                                        # Wouldn't want the enemy targeting a destroyed system, would we?
                                        pChildSubsystem.GetProperty().SetTargetable(1)                  # Restore the system to normal.
                                        pChildSubsystem.GetProperty().SetCritical(bIsCritical)                                   
                        pShipList.TGDoneIterating()


                # If we're turning the shield generator back on, we'd better make sure we still have shields.
                if pShipList:
                        if pSystemRepair.GetName() == pPlayer.GetShields().GetName():
                                RestoreShieldData()

                # If we had shut down a different system, reboot it.
                # This is mostly for hull repairs, where the system repaired and the system shut down are different:
                if pSystemShutdownList != None:
                        iNumItems = pSystemShutdownList.TGGetNumItems()
                        pSystemShutdownList.TGBeginIteration()
                        for i in range(iNumItems):
                                pShipProperty   = App.SubsystemProperty_Cast(pSystemShutdownList.TGGetNext().GetProperty())
                                pChildSubsystem = pPlayer.GetSubsystemByProperty(pShipProperty)
                                iCurrCon        = pChildSubsystem.GetCondition()

                                iCurrCon = dShutdownCurrCon[pChildSubsystem.GetName()]
                                #pChildSubsystem.GetProperty().SetCritical(0)                            # Note that system criticality extensions are NOT built into the secondary system shutdown framework.
                                #pChildSubsystem.GetProperty().SetTargetable(1)
				SetSubsystemCondition(pPlayer.GetObjID(), pChildSubsystem, iCurrCon)
                        pSystemShutdownList.TGDoneIterating()  

                        # We have to do the same thing for secondary shield shutdowns as for primaries.
                        if pSystemShutdown.GetName() == pPlayer.GetShields().GetName():
                                #print "Secondary Restorifying"
                                RestoreShieldData()

                # Replace the repair teams.
		SetSubsystemCondition(pPlayer.GetObjID(), RepairSubsystem, RepairSubsystem.GetMaxCondition())
		RepairSubsystem.GetProperty().SetTargetable(bIsTargetable)
		
		# Rename the button.
		pButton.SetName(App.TGString(str(sSubsystemName) + " Status: Online"))

                # If we need to terminate the secondary function begun in ESR(), do so now.
                if sTertiaryFunction:
                        pExecute = MissionLib.CreateTimer(Libs.LibEngineering.GetEngineeringNextEventType(), __name__ + sTertiaryFunction, App.g_kUtopiaModule.GetGameTime() + 0, 0, 0)

                # See if we have to do anything special to restore this system.
                if sRecoveryFunction:
                        pExecute = MissionLib.CreateTimer(Libs.LibEngineering.GetEngineeringNextEventType(), __name__ + sRecoveryFunction, App.g_kUtopiaModule.GetGameTime() + 0, 0, 0)

                if not (sTertiaryFunction) and not (sRecoveryFunction):
                        ResetDESR()

		#Scaffold: print "ER: Done."



# SPECIAL: Shields.

# Ladies and Gentleman of the supposed jury, the following section of code is on trial for making absolutely no sense.  Well, I would like you to consider this.
# This is a picture of the creature known as Chewbacca.  Chewbacca is from the planet Kashyyk, but he lives on Endor.  *This does not make sense.*  Why would an
# eight-foot-tall Wookie live with a bunch of two-foot-tall Ewoks?  I'll tell you: IT DOES NOT MAKE SENSE!
# Now, Ladies and Gentleman of the supposed jury, you may wonder why I'm talking about Chewbacca in my source code when the clear issue is the clarity of my code.
# You may even be wondering why I'm addressing you, because you do not exist.  I'll tell you: IT DOES NOT MAKE SENSE!  You heard me: I AM NOT MAKING ANY SENSE!
# I do not make sense, you do not make sense, that fat guy in the back corner of the courtroom does not make sense, and, above all, this code **DOES NOT MAKE ANY SENSE!**
# If Chewbacca lived on Endor, you must aquit.  The defense rests.

## Section IV: Secondary Repair Function for Shield Recharging.
# Note: No compatibility with secondary system shutdown functions.  I got lazy.
def ShieldsEmergencyRepair():
                debug(__name__ + ", ShieldsEmergencyRepair")
                global bButtonFunctionSignal, dESR
                pGame                   = App.Game_GetCurrentGame()
                pEpisode                = pGame.GetCurrentEpisode()
                pMission                = pEpisode.GetCurrentMission()
                pPlayer                 = dESR["pPlayer"]
                pButton                 = dESR["pButton"]
                pSystemRepair           = dESR["pSystemRepair"]
                iIterationAccelerator   = dESR["iIterationAcceleration"]
                iParentMaxCon           = dESR["iParentMaxCon"]
		RepairSubsystem         = pPlayer.GetRepairSubsystem()
                pShields                = pPlayer.GetShields()
                dShieldStatus           = {}
                dShieldCharge           = {}
                iParentCurrCon          = 0                                                             # That stands for Integer: Parent Subsystem Current Condition
                iParentMaxCon           = 0                                                             # Seriously.  You can figure this out.

                # Play sound A.
                pSound = App.TGSound_Create("sfx/Interface/ShutDown.wav", "ShutdownSound", 0)
                pSound.SetSFX(0)
                pSound.SetInterface(1)
                App.g_kSoundManager.PlaySound("ShutdownSound")

                # Play sound B. - you really messed up the database over here it's not bridge crew general it's my custom tgl file for some reason bc won't play it but it plays it now.
                Database = pMission.SetDatabase("data/TGL/ER.tgl")
                Sequence = App.TGSequence_Create()
                pSet = App.g_kSetManager.GetSet("bridge")
                pEngineer = App.CharacterClass_GetObject(pSet, "Engineer")
                Sequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SAY_LINE, "Pwr", None, 0, Database))
                Sequence.Play()

                # Program escape handlers in case we get a sudden termination.
                pSaffiButton = GetMenuButton("Commander", "End Combat")
                if pSaffiButton:
                        pSaffiButton.AddPythonFuncHandlerForInstance(App.ET_ST_BUTTON_CLICKED, __name__ + ".EvaluateBackOnline")
                        
                pSaffiQBR = GetQBRMenuButton("Commander", "Configure")
                if pSaffiQBR:
                        pSaffiQBR.AddPythonFuncHandlerForInstance(App.ET_ST_BUTTON_CLICKED, __name__ + ".EvaluateBackOnline")      
                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ShipExploding")
                #LineMoved: App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SET_PLAYER, pMission, __name__ + ".EvaluateBackOnline")

                # You lose your shields.
                for pShield in range(App.ShieldClass.NUM_SHIELDS):
                        iCurrCon                    = pShields.GetCurShields(pShield)
                        iMaxCon                     = pShields.GetMaxShields(pShield)
                        iParentCurrCon              = iParentCurrCon + iCurrCon
                        iParentMaxCon               = iParentMaxCon + iMaxCon

                        iCharge                     = pShields.GetProperty().GetShieldChargePerSecond(pShield)
                        dShieldStatus[pShield]      = iCurrCon
                        dShieldCharge[pShield]      = iCharge

                        # Cut shields and recharge rates.
			SetShieldCondition(pPlayer, pShield, 0, 0)

                # Now fix stuff that require the button and the parent.
                iIterationTime  = (iParentMaxCon)/(13000)/(iIterationAccelerator)                                               # Unlike earlier versions of this script, iteration time is not based in any way on the system's current condition, but solely on overall system complexity.
		SetSubsystemCondition(pPlayer.GetObjID(), RepairSubsystem, RepairSubsystem.GetDisabledPercentage () + 0.1)
                bIsTargetable = RepairSubsystem.GetProperty().IsTargetable()
                RepairSubsystem.GetProperty().SetTargetable(0)

                # Button name data time!
                # The int function demands (quite irrationally) to have addition involved.
                iNewStatus = int((iParentCurrCon/iParentMaxCon) * 100 + 0)
                iTimeLeft = int((100-iNewStatus) * iIterationTime)
                if iTimeLeft < iIterationTime:
                        iTimeLeft = "< " + str(int(iIterationTime + 0))

                # Name the button.
                pButton.SetName(App.TGString(str(iNewStatus) + "%/" + str(iTimeLeft) + " sec/" + "Shield Recharge"))

                # We need these later on.  I hate globals, but, as Sneaker says, those are the rules.
                dESR["iParentMaxCon"]   = iParentMaxCon
                dESR["iIterationTime"]  = iIterationTime
                dESR["bIsTargetable"]   = bIsTargetable
                dESR["dShieldStatus"]   = dShieldStatus
                dESR["dShieldCharge"]   = dShieldCharge

                # If we're over 100%, force us back online.
                # A bugfix it shouldn't be ESRBackOnline it should be ShieldsBackOnline wowy :)
                if iParentCurrCon/iParentMaxCon >= 1.0:
                        ShieldsBackOnline()
                        return             

                # Set up a timer to call the incremental repairs (10% every iteration).
                pIncrementTimer = MissionLib.CreateTimer(Libs.LibEngineering.GetEngineeringNextEventType(), __name__ + ".ShieldsRepairIncrement", App.g_kUtopiaModule.GetGameTime() + iIterationTime, 0, 0)

                dESR["pIncrementTimer"] = pIncrementTimer


def ShieldsRepairIncrement(pObject, pEvent):
                debug(__name__ + ", ShieldsRepairIncrement")
                global dESR
                pPlayer                 = dESR["pPlayer"]
                pButton                 = dESR["pButton"]
                pShipList               = dESR["pShipList"]
                iParentMaxCon           = dESR["iParentMaxCon"]
                dShieldStatus           = dESR["dShieldStatus"]
                dShieldCharge           = dESR["dShieldCharge"]
                pSystemShutdownList     = dESR["pSystemShutdownList"]
                pSystemRepair           = dESR["pSystemRepair"]
	        iIterationAccelerator   = dESR["iIterationAcceleration"]
                bWaitBeforeStartup      = dESR["bWaitBeforeStartup"]
                pShields                = pPlayer.GetShields()
		RepairSubsystem         = pPlayer.GetRepairSubsystem()
                iParentCurrCon          = 0                                                             # That stands for Integer: Parent Subsystem Current Condition

    		# Give us 1% of the parent's aggregate condition to use as "points," awarded to the children for repairs.
		try:
			iParentPoints = iParentMaxCon/100
		except:
			print "ESR, ShieldsRepairIncrement failure: iParentMaxCon=", iParentMaxCon
			return

		# You regain some shields, using the 'points' system.
		for pShield in range(App.ShieldClass.NUM_SHIELDS):
                        iCurrCon            = dShieldStatus[pShield]
                        iMaxCon             = pShields.GetMaxShields(pShield)
                        iParentCurrCon      = iParentCurrCon + iCurrCon
                        iSubsystemMaxPoints = iMaxCon - iCurrCon                            # The largest number of points this child would be able to absorb.  He might not get all of it; see below.

                        if iSubsystemMaxPoints > iParentPoints:
                                n = -(iParentPoints - iSubsystemMaxPoints)                  # Finds the positive difference between PP and SMP.
                                iSubsystemMaxPoints = iSubsystemMaxPoints - n               # Slaps SMP on the wrist for trying to take more than PP has right now.
                                                
                        iParentPoints       = iParentPoints - iSubsystemMaxPoints           # Take those points away from our total...
                        iCurrCon            = iCurrCon + iSubsystemMaxPoints                # ... and assign them to the subsystem.
                        dShieldStatus[pShield] = iCurrCon

                # Now fix stuff that require the button and the parent.
                iIterationTime  = (iParentMaxCon)/(13000)/(iIterationAccelerator)                                               # Unlike earlier versions of this script, iteration time is not based in any way on the system's current condition, but solely on overall system complexity.

                # If we're over 100%, force us back online... unless this is a shield recharge based a generator shutdown.
                if (iParentCurrCon/iParentMaxCon >= 1.0) and (bWaitBeforeStartup == 0):
                        ShieldsBackOnline()
                        return

                # Button name data time!
                # The int function demands (quite irrationally) to have addition involved.
                iNewStatus = int((iParentCurrCon/iParentMaxCon) * 100 + 0)
                iTimeLeft = int((100-iNewStatus) * iIterationTime)
                if iTimeLeft < iIterationTime:
                        iTimeLeft = "< " + str(int(iIterationTime + 0))

                # Name the button.
                pButton.SetName(App.TGString(str(iNewStatus) + "%/" + str(iTimeLeft) + " sec/" + "Shield Recharge"))

                #print iParentMaxCon, dCurrConList, sSubsystemName, iParentCurrCon, iParentMaxCon, iNewStatus

                # Set up a timer to call the incremental repairs (10% every iteration).
                pIncrementTimer = MissionLib.CreateTimer(Libs.LibEngineering.GetEngineeringNextEventType(), __name__ + ".ShieldsRepairIncrement", App.g_kUtopiaModule.GetGameTime() + iIterationTime, 0, 0)


def ShieldsBackOnline():
                debug(__name__ + ", ShieldsBackOnline")
                global dESR, bButtonFunctionSignal, pPowerButton, pImpulseButton, pSensorsButton, pCloakingDeviceButton, pShieldsButton, pShieldFacesButton, pPhasersButton, pTorpedoesButton, pPulseWeaponsButton, pTractorsButton, pHullButton, pCancel0
                pPlayer             = dESR["pPlayer"]
                pButton             = dESR["pButton"]
                pShipList           = dESR["pShipList"]
                iParentMaxCon       = dESR["iParentMaxCon"]
                dCurrConList        = dESR["dCurrConList"]
                dShieldStatus       = dESR["dShieldStatus"]
                dShieldCharge       = dESR["dShieldCharge"]
                pIncrementTimer     = dESR["pIncrementTimer"]
                bIsTargetable       = dESR["bIsTargetable"]
                bIsCritical         = dESR["bIsCritical"]
                pSystemShutdownList = dESR["pSystemShutdownList"]
                pSystemRepair       = dESR["pSystemRepair"]
                sSubsystemName      = pSystemRepair.GetName()
                pShields            = pPlayer.GetShields()
		RepairSubsystem     = pPlayer.GetRepairSubsystem()        

                # Allows access to other ESR menus.
                bButtonFunctionSignal = 0
		
		# Play the sounds! (Sound A)
		pGame = App.Game_GetCurrentGame()
     		pEpisode = pGame.GetCurrentEpisode()
     		pMission = pEpisode.GetCurrentMission()
     		Database = pMission.SetDatabase("data/TGL/Bridge Crew General.tgl")
     	  	Sequence = App.TGSequence_Create()
     		pSet = App.g_kSetManager.GetSet("bridge")
     		pEngineer = App.CharacterClass_GetObject(pSet, "Engineer")
     	        Sequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SAY_LINE, "ge111", None, 0, Database))
     	        Sequence.Play()		

                # Sound B
                pSound = App.TGSound_Create("sfx/Interface/SystemsOnline.wav", "StartupSound", 0)
                pSound.SetSFX(0)
                pSound.SetInterface(1)
                App.g_kSoundManager.PlaySound("StartupSound")

                # Delete the timer.
                try:
                    App.g_kTimerManager.DeleteTimer(pIncrementTimer.GetObjID())
                    App.g_kRealtimeTimerManager.DeleteTimer(pIncrementTimer.GetObjID())
                    pIncrementTimer = None
                except AttributeError:
                    pass
                    #print "ESR: Timer already deleted.  Proceed."

                # Just get those doggone buttons online.
                SetEnabledButtons()

                # Reset handlers.
                pSaffiButton = GetMenuButton("Commander", "End Combat")
                pSaffiQBR = GetQBRMenuButton("Commander", "Configure")
                if pSaffiButton:
                        pSaffiButton.RemoveHandlerForInstance(App.ET_ST_BUTTON_CLICKED, __name__ + ".EvaluateBackOnline")
                if pSaffiQBR:
                        pSaffiQBR.RemoveHandlerForInstance(App.ET_ST_BUTTON_CLICKED, __name__ + ".EvaluateBackOnline")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ShipExploding")
                #LineObsolete: App.g_kEventManager.RemoveBroadcastHandler(App.ET_SET_PLAYER, pMission, __name__ + ".EvaluateBackOnline")
                
                # You regain some shields, using the 'points' system.
                iParentCurrCon = 0
                for pShield in range(App.ShieldClass.NUM_SHIELDS):
                        iCurrCon    = dShieldStatus[pShield]
                        iCharge     = dShieldCharge[pShield]
			
			SetShieldCondition(pPlayer, pShield, iCurrCon, iCharge)

                # Replace the repair teams.
		SetSubsystemCondition(pPlayer.GetObjID(), RepairSubsystem, RepairSubsystem.GetMaxCondition())
		RepairSubsystem.GetProperty().SetTargetable(bIsTargetable)
		
		# Rename the button.
		pButton.SetName(App.TGString("Shield Recharge"))

		# Set dESR back to its original None elements.
		ResetDESR()

		#print "ER: Done."


## Section VI: Hull Repair Function Attachments
# I love customization.  Here's 14 functions, no five of which will you ever use in the same install of this script.
# NOTE: Many operations inside these functions can and eventually should be condensed into unique and separate functions.
# However, although it wastes space to repeat the same operation in three or four functions, I am too overworked to fix it
# at this time.
def HullSecondary2ShieldsAll(pObject, pEvent):
                debug(__name__ + ", HullSecondary2ShieldsAll")
                global dESR, dAuxilliary
                dAuxilliary = {}
                dAuxilliary["pPlayer"] = dESR["pPlayer"]
                pPlayer = dAuxilliary["pPlayer"]
                pShields = pPlayer.GetShields()

                # This gets awkward if the shields aren't actually on.
                pShields.TurnOn()
                
                for pShield in range(App.ShieldClass.NUM_SHIELDS):
                        iCurrCon                    = pShields.GetCurShields(pShield)
                        iCharge                     = pShields.GetProperty().GetShieldChargePerSecond(pShield)

                        # Store the info into the auxilliary as a tuple.  In a perfect world, this would be a nested
                        # dictionary, but it's only two items and I'm lazy.
                        # Also, we can't use StoreShieldData(), because that uses dESR, which is reset between this
                        # function and the HullTertiary2ShieldsFull(), which is what this function links up with.
                        dAuxilliary[pShield] = iCurrCon, iCharge

                        # Cut shields and recharge rates.
			SetShieldCondition(pPlayer, pShield, 0, 0)


def HullTertiary2ShieldsAll(pObject, pEvent):
                debug(__name__ + ", HullTertiary2ShieldsAll")
                global dESR, dAuxilliary
                try:
                    pPlayer = dAuxilliary["pPlayer"]
                except:
                    pPlayer = MissionLib.GetPlayer()
                    print "No dAuxilliary"
                pShields = pPlayer.GetShields()
                
                for pShield in range(App.ShieldClass.NUM_SHIELDS):
                        iCurrCon                    = pShields.GetCurShields(pShield)
                        iCharge                     = pShields.GetProperty().GetShieldChargePerSecond(pShield)

                        # Cut shields and recharge rates.
			SetShieldCondition(pPlayer, pShield, dAuxilliary[pShield][0], dAuxilliary[pShield][1])

                ResetDESR()


def HullSecondary3HalfShieldsEngines(pObject, pEvent):
                debug(__name__ + ", HullSecondary3HalfShieldsEngines")
                global dESR, dAuxilliary
                dAuxilliary             = {}
                dShutdownCurrCon        = {}
                dAuxilliary["pPlayer"]  = dESR["pPlayer"]
                pPlayer                 = dAuxilliary["pPlayer"]
                pShipSet                = pPlayer.GetPropertySet()
                pShields                = pPlayer.GetShields() 
                pSystemShutdown         = pPlayer.GetImpulseEngineSubsystem()
                pSystemShutdownList     = pShipSet.GetPropertiesByType(App.CT_ENGINE_PROPERTY)
                dAuxilliary["dShutdownCurrCon"]     = dShutdownCurrCon
                dAuxilliary["pSystemShutdown"]      = pSystemShutdown
                dAuxilliary["pSystemShutdownList"]  = pSystemShutdownList
                                
                for pShield in range(App.ShieldClass.NUM_SHIELDS):
                        iCurrCon                    = pShields.GetCurShields(pShield)
                        iCharge                     = pShields.GetProperty().GetShieldChargePerSecond(pShield)

                        # Cut shields and recharge rates.
			SetShieldCondition(pPlayer, pShield, iCurrCon/2, iCharge/2)

                # Shut down the secondary system.  In this case: Engines.
                if pSystemShutdownList != None:
                        iNumItems = pSystemShutdownList.TGGetNumItems()
                        pSystemShutdownList.TGBeginIteration()
                        for i in range(iNumItems):
                                pShipProperty   = App.SubsystemProperty_Cast(pSystemShutdownList.TGGetNext().GetProperty())
                                pChildSubsystem = pPlayer.GetSubsystemByProperty(pShipProperty)
                                iCurrCon        = pChildSubsystem.GetCondition()

                                dShutdownCurrCon[pChildSubsystem.GetName()] = pChildSubsystem.GetCondition()
                                #pChildSubsystem.GetProperty().SetCritical(0)
                                #pChildSubsystem.GetProperty().SetTargetable(0)
				SetSubsystemCondition(pPlayer.GetObjID(), pChildSubsystem, pChildSubsystem.GetDisabledPercentage() + 0.1)
                        pSystemShutdownList.TGDoneIterating() 

                kZero = App.TGPoint3()
                kZero.SetXYZ(0.0, 0.0, 0.0)
                pPlayer.SetVelocity(kZero)
                

def HullTertiary3HalfShieldsEngines(pObject, pEvent):
                debug(__name__ + ", HullTertiary3HalfShieldsEngines")
                global dESR, dAuxilliary
                try:
                    pPlayer = dAuxilliary["pPlayer"]
                except:
                    pPlayer = MissionLib.GetPlayer()

                pShields            = pPlayer.GetShields()
                pSystemShutdownList = dAuxilliary["pSystemShutdownList"]
                pSystemShutdown     = dAuxilliary["pSystemShutdown"]
                dShutdownCurrCon    = dAuxilliary["dShutdownCurrCon"]
            
                for pShield in range(App.ShieldClass.NUM_SHIELDS):
                        iCurrCon                    = pShields.GetCurShields(pShield)
                        iCharge                     = pShields.GetProperty().GetShieldChargePerSecond(pShield)

                        # Cut shields and recharge rates.
			SetShieldCondition(pPlayer, pShield, iCurrCon * 2, iCharge * 2)

                if pSystemShutdownList != None:
                        iNumItems = pSystemShutdownList.TGGetNumItems()
                        pSystemShutdownList.TGBeginIteration()
                        for i in range(iNumItems):
                                pShipProperty   = App.SubsystemProperty_Cast(pSystemShutdownList.TGGetNext().GetProperty())
                                pChildSubsystem = pPlayer.GetSubsystemByProperty(pShipProperty)
                                iCurrCon        = pChildSubsystem.GetCondition()

                                iCurrCon = dShutdownCurrCon[pChildSubsystem.GetName()]
                                #pChildSubsystem.GetProperty().SetCritical(0)                            
                                #pChildSubsystem.GetProperty().SetTargetable(1)
				SetSubsystemCondition(pPlayer.GetObjID(), pChildSubsystem, iCurrCon)
                        pSystemShutdownList.TGDoneIterating()  

                ResetDESR()


def HullSecondary4HalfShieldsOnly(pObject, pEvent):
                debug(__name__ + ", HullSecondary4HalfShieldsOnly")
                global dESR, dAuxilliary
                dAuxilliary = {}
                dAuxilliary["pPlayer"] = dESR["pPlayer"]
                pPlayer = dAuxilliary["pPlayer"]
                pShields = pPlayer.GetShields()
                
                for pShield in range(App.ShieldClass.NUM_SHIELDS):
                        iCurrCon                    = pShields.GetCurShields(pShield)
                        iCharge                     = pShields.GetProperty().GetShieldChargePerSecond(pShield)

                        # Cut shields and recharge rates.
			SetShieldCondition(pPlayer, pShield, iCurrCon/2, iCharge/2)


def HullTertiary4HalfShieldsOnly(pObject, pEvent):
                debug(__name__ + ", HullTertiary4HalfShieldsOnly")
                global dESR, dAuxilliary
                try:
                    pPlayer = dAuxilliary["pPlayer"]
                except:
                    pPlayer = MissionLib.GetPlayer()
                pShields = pPlayer.GetShields()
                
                for pShield in range(App.ShieldClass.NUM_SHIELDS):
                        iCurrCon                    = pShields.GetCurShields(pShield)
                        iCharge                     = pShields.GetProperty().GetShieldChargePerSecond(pShield)

                        # Cut shields and recharge rates.
			SetShieldCondition(pPlayer, pShield, iCurrCon * 2, iCharge * 2)

                ResetDESR()


def HullSecondary5Engines20(pObject, pEvent):
                debug(__name__ + ", HullSecondary5Engines20")
                global dESR, dAuxilliary
                dAuxilliary = {}
                dShutdownCurrCon = {}
                dAuxilliary["pPlayer"] = dESR["pPlayer"]
                pPlayer = dAuxilliary["pPlayer"]
                pShipSet = pPlayer.GetPropertySet()
                pSystemShutdown = pPlayer.GetImpulseEngineSubsystem()
                pSystemShutdownList = pShipSet.GetPropertiesByType(App.CT_ENGINE_PROPERTY)
                dAuxilliary["pSystemShutdown"] = pSystemShutdown
                dAuxilliary["pSystemShutdownList"]  = pSystemShutdownList
                dAuxilliary["dShutdownCurrCon"]     = dShutdownCurrCon
                dAuxilliary["sSubsystemName"]       = dESR["sSubsystemName"]
                dAuxilliary["pButton"]              = dESR["pButton"]
                dESR["sRecoveryFunction"]           = ".HullRecovery5Engines20"

                if pSystemShutdownList != None:
                        iNumItems = pSystemShutdownList.TGGetNumItems()
                        pSystemShutdownList.TGBeginIteration()
                        for i in range(iNumItems):
                                pShipProperty   = App.SubsystemProperty_Cast(pSystemShutdownList.TGGetNext().GetProperty())
                                pChildSubsystem = pPlayer.GetSubsystemByProperty(pShipProperty)
                                iCurrCon        = pChildSubsystem.GetCondition()

                                dShutdownCurrCon[pChildSubsystem.GetName()] = pChildSubsystem.GetCondition()
                                #pChildSubsystem.GetProperty().SetCritical(0)
                                #pChildSubsystem.GetProperty().SetTargetable(0)
				SetSubsystemCondition(pPlayer.GetObjID(), pChildSubsystem, pChildSubsystem.GetDisabledPercentage() + 0.1)
                        pSystemShutdownList.TGDoneIterating() 

                kZero = App.TGPoint3()
                kZero.SetXYZ(0.0, 0.0, 0.0)
                pPlayer.SetVelocity(kZero)
                

# THERE IS NO TERTIARY FUNCTION for Configuration 5Engines20
def HullRecovery5Engines20(pObject, pEvent):
                debug(__name__ + ", HullRecovery5Engines20")
                global dESR, dAuxilliary, pCancel
                dAuxilliary["pPlayer"]          = dESR["pPlayer"]
                pPlayer                         = dAuxilliary["pPlayer"]
                sSubsystemName                  = dAuxilliary["sSubsystemName"]
                pButton                         = dAuxilliary["pButton"]
                pShipSet                        = pPlayer.GetPropertySet()
                pSystemShutdown                 = pPlayer.GetImpulseEngineSubsystem()
                pSystemShutdownList             = pShipSet.GetPropertiesByType(App.CT_ENGINE_PROPERTY)
                dShutdownCurrCon                = dAuxilliary["dShutdownCurrCon"] 
                dAuxilliary["pSystemShutdown"]  = pSystemShutdown
                dAuxilliary["pSystemShutdownList"] = pSystemShutdownList

                # Okay, we're good.  You can reset dESR now.
                ResetDESR()

                # Disable all buttons again.
                SetDisabledButtons()
                pCancel.SetDisabled()

                kZero = App.TGPoint3()
                kZero.SetXYZ(0.0, 0.0, 0.0)
                pPlayer.SetVelocity(kZero)

                pRecoveryTimer = MissionLib.CreateTimer(Libs.LibEngineering.GetEngineeringNextEventType(), __name__ + ".HullEndRecovery5Engines20", App.g_kUtopiaModule.GetGameTime() + 20, 0, 0)
                
                pButton.SetName(App.TGString(str(sSubsystemName) + " Status: Recovering"))
                

def HullEndRecovery5Engines20(pObject, pEvent):
                debug(__name__ + ", HullEndRecovery5Engines20")
                global dAuxilliary
                pPlayer             = dAuxilliary["pPlayer"]
                pButton             = dAuxilliary["pButton"]
                sSubsystemName      = dAuxilliary["sSubsystemName"]
                pSystemShutdownList = dAuxilliary["pSystemShutdownList"]
                pSystemShutdown     = dAuxilliary["pSystemShutdown"]
                dShutdownCurrCon    = dAuxilliary["dShutdownCurrCon"]

                pSound = App.TGSound_Create("sfx/Interface/SystemsOnline.wav", "StartupSound", 0)
                pSound.SetSFX(0)
                pSound.SetInterface(1)
                App.g_kSoundManager.PlaySound("StartupSound")

                SetEnabledButtons()

                if pSystemShutdownList != None:
                        iNumItems = pSystemShutdownList.TGGetNumItems()
                        pSystemShutdownList.TGBeginIteration()
                        for i in range(iNumItems):
                                pShipProperty   = App.SubsystemProperty_Cast(pSystemShutdownList.TGGetNext().GetProperty())
                                pChildSubsystem = pPlayer.GetSubsystemByProperty(pShipProperty)
                                iCurrCon        = pChildSubsystem.GetCondition()

                                iCurrCon = dShutdownCurrCon[pChildSubsystem.GetName()]
                                #pChildSubsystem.GetProperty().SetCritical(0)                            
                                #pChildSubsystem.GetProperty().SetTargetable(1)
				SetSubsystemCondition(pPlayer.GetObjID(), pChildSubsystem, iCurrCon)
                        pSystemShutdownList.TGDoneIterating()
                        
                pButton.SetName(App.TGString(str(sSubsystemName) + " Status: Online"))
                ResetDESR()


def HullSecondary6EnginesAll(pObject, pEvent):
                debug(__name__ + ", HullSecondary6EnginesAll")
                global dESR, dAuxilliary
                dAuxilliary                         = {}
                dShutdownCurrCon                    = {}
                dAuxilliary["pPlayer"]              = dESR["pPlayer"]
                pPlayer                             = dAuxilliary["pPlayer"]
                pShipSet                            = pPlayer.GetPropertySet()
                pSystemShutdown                     = pPlayer.GetImpulseEngineSubsystem()
                pSystemShutdownList                 = pShipSet.GetPropertiesByType(App.CT_ENGINE_PROPERTY)
                dAuxilliary["pSystemShutdown"]      = pSystemShutdown
                dAuxilliary["pSystemShutdownList"]  = pSystemShutdownList
                dAuxilliary["dShutdownCurrCon"]     = dShutdownCurrCon

                if pSystemShutdownList != None:
                        iNumItems = pSystemShutdownList.TGGetNumItems()
                        pSystemShutdownList.TGBeginIteration()
                        for i in range(iNumItems):
                                pShipProperty   = App.SubsystemProperty_Cast(pSystemShutdownList.TGGetNext().GetProperty())
                                pChildSubsystem = pPlayer.GetSubsystemByProperty(pShipProperty)
                                iCurrCon        = pChildSubsystem.GetCondition()

                                dShutdownCurrCon[pChildSubsystem.GetName()] = pChildSubsystem.GetCondition()
                                #pChildSubsystem.GetProperty().SetCritical(0)
                                #pChildSubsystem.GetProperty().SetTargetable(0)
				SetSubsystemCondition(pPlayer.GetObjID(), pChildSubsystem, pChildSubsystem.GetDisabledPercentage() + 0.1)
                        pSystemShutdownList.TGDoneIterating()

                kZero = App.TGPoint3()
                kZero.SetXYZ(0.0, 0.0, 0.0)
                pPlayer.SetVelocity(kZero)


def HullTertiary6EnginesAll(pObject, pEvent):
                debug(__name__ + ", HullTertiary6EnginesAll")
                global dESR, dAuxilliary
                try:
                    pPlayer = dAuxilliary["pPlayer"]
                except:
                    pPlayer = MissionLib.GetPlayer()
                dShutdownCurrCon    = dAuxilliary["dShutdownCurrCon"] 
                pSystemShutdownList = dAuxilliary["pSystemShutdownList"]
                pSystemShutdown     = dAuxilliary["pSystemShutdownList"]

                if pSystemShutdownList != None:
                        iNumItems = pSystemShutdownList.TGGetNumItems()
                        pSystemShutdownList.TGBeginIteration()
                        for i in range(iNumItems):
                                pShipProperty   = App.SubsystemProperty_Cast(pSystemShutdownList.TGGetNext().GetProperty())
                                pChildSubsystem = pPlayer.GetSubsystemByProperty(pShipProperty)
                                iCurrCon        = pChildSubsystem.GetCondition()

                                iCurrCon = dShutdownCurrCon[pChildSubsystem.GetName()]
                                #pChildSubsystem.GetProperty().SetCritical(0)                            
                                #pChildSubsystem.GetProperty().SetTargetable(1)
				SetSubsystemCondition(pPlayer.GetObjID(), pChildSubsystem, iCurrCon)
                        pSystemShutdownList.TGDoneIterating()

                ResetDESR()


def HullSecondary7SensorsAll(pObject, pEvent):
                debug(__name__ + ", HullSecondary7SensorsAll")
                global dESR, dAuxilliary
                dAuxilliary                         = {}
                dShutdownCurrCon                    = {}
                dAuxilliary["pPlayer"]              = dESR["pPlayer"]
                pPlayer                             = dAuxilliary["pPlayer"]
                pShipSet                            = pPlayer.GetPropertySet()
                pSystemShutdown                     = pPlayer.GetSensorSubsystem()
                pSystemShutdownList                 = pShipSet.GetPropertiesByType(App.CT_SENSOR_PROPERTY)
                dAuxilliary["pSystemShutdown"]      = pSystemShutdown
                dAuxilliary["pSystemShutdownList"]  = pSystemShutdownList
                dAuxilliary["dShutdownCurrCon"]     = dShutdownCurrCon

                if pSystemShutdownList != None:
                        iNumItems = pSystemShutdownList.TGGetNumItems()
                        pSystemShutdownList.TGBeginIteration()
                        for i in range(iNumItems):
                                pShipProperty   = App.SubsystemProperty_Cast(pSystemShutdownList.TGGetNext().GetProperty())
                                pChildSubsystem = pPlayer.GetSubsystemByProperty(pShipProperty)
                                iCurrCon        = pChildSubsystem.GetCondition()

                                dShutdownCurrCon[pChildSubsystem.GetName()] = pChildSubsystem.GetCondition()
                                #pChildSubsystem.GetProperty().SetCritical(0)
                                #pChildSubsystem.GetProperty().SetTargetable(0)
				SetSubsystemCondition(pPlayer.GetObjID(), pChildSubsystem, pChildSubsystem.GetDisabledPercentage() + 0.1)
                        pSystemShutdownList.TGDoneIterating()
                        

def HullTertiary7SensorsAll(pObject, pEvent):
                debug(__name__ + ", HullTertiary7SensorsAll")
                global dESR, dAuxilliary
                try:
                    pPlayer = dAuxilliary["pPlayer"]
                except:
                    pPlayer = MissionLib.GetPlayer()
                pSystemShutdownList = dAuxilliary["pSystemShutdownList"]
                pSystemShutdown     = dAuxilliary["pSystemShutdownList"]
                dShutdownCurrCon    = dAuxilliary["dShutdownCurrCon"]

                if pSystemShutdownList != None:
                        iNumItems = pSystemShutdownList.TGGetNumItems()
                        pSystemShutdownList.TGBeginIteration()
                        for i in range(iNumItems):
                                pShipProperty   = App.SubsystemProperty_Cast(pSystemShutdownList.TGGetNext().GetProperty())
                                pChildSubsystem = pPlayer.GetSubsystemByProperty(pShipProperty)
                                iCurrCon        = pChildSubsystem.GetCondition()

                                iCurrCon = dShutdownCurrCon[pChildSubsystem.GetName()]
                                #pChildSubsystem.GetProperty().SetCritical(0)                            
                                #pChildSubsystem.GetProperty().SetTargetable(1)
				SetSubsystemCondition(pPlayer.GetObjID(), pChildSubsystem, iCurrCon)
                        pSystemShutdownList.TGDoneIterating()

                ResetDESR()



## Section V: Utilities
# Defines the defaults for every possible key.  Resets after every function.
# DO NOT SET any entry equal to anything other than None unless you know what
# you are doing.  Which, if you haven't fallen asleep by now, on line 1476, you
# probably do.  Carry on.
# This function is necessary because not all Direct Handlers define all these
# attributes, so we need to have something the game can grab for "if" clauses
# without raising a KeyError.
def ResetDESR():
                debug(__name__ + ", ResetDESR")
                global dESR
                dESR = {}
                dESR["iParentMaxCon"] = None
                dESR["pIncrementTimer"] = None
                dESR["iIterationTime"] = None
                dESR["dCurrConList"] = None
                dESR["pSystemRepair"] = None
                dESR["pSystemShutdownList"] = None
                dESR["pShipList"] = None
                dESR["pButton"] = None
                dESR["pPlayer"] = MissionLib.GetPlayer()    # dESR has, on occasion, inexplicably reverter pPlayer to None.  So we're going to keep this as a default.
                dESR["iShutdownCurrCon"] = None
                dESR["dShieldStatus"] = None
                dESR["dShieldCharge"] = None
                dESR["pSystemShutdown"] = None
                dESR["bIsTargetable"] = 1
                dESR["bIsCritical"] = 0
                dESR["iIterationAcceleration"] = 1
                dESR["bWaitBeforeStartup"] = 0
                dESR["sSubsystemName"] = None
                dESR["sSecondaryFunction"] = None
                dESR["sRecoveryFunction"] = None
                dESR["HRMaxAccel"] = 0
                dESR["HRMaxSpeed"] = 0
                dESR["sTertiaryFunction"] = None
                dESR["dShutdownCurrCon"] = None
                dESR["bAddPointsInProgress"] = 0
                dESR["bIsSystemShutDown"] = 1


# Decides which reboot to use, if any.
def EvaluateBackOnline(pObject = None, pEvent = None):
                debug(__name__ + ", EvaluateBackOnline")
                global bButtonFunctionSignal

                if bButtonFunctionSignal == 0:
                        GameRestart()
                        return "TRUE"
                
                if bButtonFunctionSignal == 1:
                        ESRBackOnline()
                        GameRestart()
                        
                if bButtonFunctionSignal == 2:
                        ShieldsBackOnline()
                        GameRestart()


                return "FALSE"

                
# Based on that number we received in Line #1 of this code, this will determine 
# which functions will run through Hull Repair's secondary and tertiary slots.
def CheckCustomisedGlobalsForHullRepair():
                debug(__name__ + ", CheckCustomisedGlobalsForHullRepair")
                global CustomizationOption, g_sSecondaryFunction, g_sTertiaryFunction

                #       1) No Hull Repair allowed. (Short Name: 1NoHull)
                #       2) Hull Repair shuts down all shields during repair.  (Short Name: 2ShieldsAll)
                #       3) Hull Repair drains 50% of shield power and shuts down all engines during repair.  (Short Name: 3HalfShieldsEngines)
                #       4) Hull Repair drains 50% of shield power during repair.  (Short Name: 4HalfShieldsOnly)
                #       5) Hull Repair shuts down all engines during repair and for twenty seconds thereafter.  (Short Name: 5Engines20)
                #       6) Hull Repair shuts down all engines during repair.  (Short Name: 6EnginesAll)
                #       7) Hull Repair shuts down all sensors during repair.  (Short Name: 7SensorsAll)

                if CustomizationOption == 1:
                        g_sSecondaryFunction = None
                        g_sTertiaryFunction  = None

                if CustomizationOption == 2:
                        g_sSecondaryFunction = ".HullSecondary2ShieldsAll"
                        g_sTertiaryFunction  = ".HullTertiary2ShieldsAll"

                if CustomizationOption == 3:
                        g_sSecondaryFunction = ".HullSecondary3HalfShieldsEngines"
                        g_sTertiaryFunction  = ".HullTertiary3HalfShieldsEngines"
                        
                if CustomizationOption == 4:
                        g_sSecondaryFunction = ".HullSecondary4HalfShieldsOnly"
                        g_sTertiaryFunction  = ".HullTertiary4HalfShieldsOnly"

                if CustomizationOption == 5:
                        g_sSecondaryFunction = ".HullSecondary5Engines20"
                        g_sTertiaryFunction  = None

                if CustomizationOption == 6:
                        g_sSecondaryFunction = ".HullSecondary6EnginesAll"
                        g_sTertiaryFunction  = ".HullTertiary6EnginesAll"

                if CustomizationOption == 7:
                        g_sSecondaryFunction = ".HullSecondary7SensorsAll"
                        g_sTertiaryFunction  = ".HullTertiary7SensorsAll"
                        

def StoreShieldData():
                debug(__name__ + ", StoreShieldData")
                global dESR
                pPlayer                 = dESR["pPlayer"]
                pButton                 = dESR["pButton"]
                pSystemRepair           = dESR["pSystemRepair"]
                iIterationAccelerator   = dESR["iIterationAcceleration"]
                iParentMaxCon           = dESR["iParentMaxCon"]
                pShields                = pPlayer.GetShields()
                dShieldStatus           = {}
                dShieldCharge           = {}

                for pShield in range(App.ShieldClass.NUM_SHIELDS):
                        iCurrCon                    = pShields.GetCurShields(pShield)
                        iCharge                     = pShields.GetProperty().GetShieldChargePerSecond(pShield)
                        dShieldStatus[pShield]      = iCurrCon
                        dShieldCharge[pShield]      = iCharge

                dESR["dShieldStatus"]   = dShieldStatus
                dESR["dShieldCharge"]   = dShieldCharge
                

# Just a simple definition in order for the player to be able to cancel the repairs it returns you to evaluatebackonline part of this script
def CancelRepairs(pObject = None, pEvent = None):
                debug(__name__ + ", CancelRepairs")
                EvaluateBackOnline()
                
                
# Resets the shields after the shield generator returns to normal.
def RestoreShieldData():
                debug(__name__ + ", RestoreShieldData")
                global dESR
                pPlayer       = dESR["pPlayer"]
                dShieldStatus = dESR["dShieldStatus"]
                dShieldCharge = dESR["dShieldCharge"]
                pShields      = pPlayer.GetShields()
                
                for pShield in range(App.ShieldClass.NUM_SHIELDS):
                        iCurrCon    = dShieldStatus[pShield]
                        iCharge     = dShieldCharge[pShield]

			SetShieldCondition(pPlayer, pShield, iCurrCon, iCharge)


# Checks on anything in the set that is exploding.        
def ShipExploding(pObject, pEvent):
                debug(__name__ + ", ShipExploding")
                pPlayer = App.Game_GetCurrentGame().GetPlayer()

                # Get the ship that is exploding.
                pShip = App.ShipClass_Cast(pEvent.GetDestination())
                if (pShip != None):
                        iShipID = pShip.GetObjID()
                        if pPlayer and pShip.GetName() == pPlayer.GetName():
                                # It's us.  Reset.
                                EvaluateBackOnline()

        
# From the MenuLib_EFX, written for a secret mod project by Wowbagger:
def GetMenuButton(sMenuName, sButtonName):
                debug(__name__ + ", GetMenuButton")
                pMenu = GetBridgeMenu(sMenuName)
                if not pMenu:
                        #print "ML-E: There is no menu " + sMenuName + ".  And stop getting down on your knees and screaming, 'IT'S REAL!  REEEAAAL!'  You're not cool enough to be Avery Brooks."
                        return

                # Grab the starting button.    
                pButton = pMenu.GetButton(sButtonName)
                if not pButton:
                        pButton = pMenu.GetSubmenu(sButtonName)
                        if not pButton: 
                                #print "ML-E: There is no button " + sButtonName + ".  Any button you see is merely the product of a deranged imagination.  Mine, to be precise."
                                return
                return pButton


# From ATP_GUIUtils:
def GetBridgeMenu(menuName):
                debug(__name__ + ", GetBridgeMenu")
                pTactCtrlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
                pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
                if(pDatabase is None):
                        return
                return pTactCtrlWindow.FindMenu(pDatabase.GetString(menuName))


# A redirect from the Direct Handlers to... uh... Indirectly Handle... the issue of button enablement.  Basically, shortens
# some of Sovvy's code.  Sadly, this would mean eliminating his comments.  I have, however, decided that the comments are
# amusing enough to keep.  Call me Chan Tanaka, but there you go.  They're at the bottom of this function.
def SetDisabledButtons():
                debug(__name__ + ", SetDisabledButtons")
                global dESR, pShieldsButton, pPowerButton, pImpulseButton, pSensorsButton, pCloakingDeviceButton, pShieldFacesButton, pPhasersButton, pTorpedoesButton, pPulseWeaponsButton, pTractorsButton, pHullButton, pCancel
                pPlayer         = MissionLib.GetPlayer()

                # If the subsystems exist, then presumably the buttons do, too.
		pPower   	= pPlayer.GetPowerSubsystem()
                pImpulse        = pPlayer.GetImpulseEngineSubsystem()
                pShields	= pPlayer.GetShields()
                pSensors        = pPlayer.GetSensorSubsystem()
                pPhasers        = pPlayer.GetPhaserSystem()
                pTorpedoes      = pPlayer.GetTorpedoSystem()
                pPulseWeapons   = pPlayer.GetPulseWeaponSystem()
                pTractors	= pPlayer.GetTractorBeamSystem()
                pCloakingDevice = pPlayer.GetCloakingSubsystem()
                pHull 		= pPlayer.GetHull()
                pActiveButton   = dESR["pButton"]

                # Disable ALL buttons.
                if pPower:
                    pPowerButton.SetDisabled()
                if pImpulse:
                    pImpulseButton.SetDisabled()
                if pSensors:
                    pSensorsButton.SetDisabled()
                if pCloakingDevice and pCloakingDeviceButton:
                    pCloakingDeviceButton.SetDisabled()
                if pShields:
                    pShieldFacesButton.SetDisabled()
                if pPhasers:
                    pPhasersButton.SetDisabled()
                if pTorpedoes:
                    pTorpedoesButton.SetDisabled()
                if pPulseWeapons:
                    pPulseWeaponsButton.SetDisabled()
                if pTractors:
                    pTractorsButton.SetDisabled()
                if pHullButton:
                    pHullButton.SetDisabled()
                if pShields:
                    pShieldsButton.SetDisabled()

                # Enable the active button and the Cancel button.
                if pActiveButton != None:
                        pActiveButton.SetEnabled()
                pCancel.SetEnabled()

# Old Sovvy Comments:
# 1) man a lot of buttons, i figured that out when i started writing all of them to be disabled.
# 2) Disable the warp button as well as all other buttons expect hull repair button
# P.S. I thank God for cut & paste :)
# Gee look I'm stealing my own code. Oh I must contact Janeway and tell him that. No seriously what you did is outrageous and totally not fair.
# Oh wowbaggers gonna freak out look at how many globals we have, oh well
# 3) oh glory be, this is gonna take a while
# I've got time, but hmmm. I'm hungry *takes a quick snack*
# 4) man i missed sensors how could have this happene
# 5) Disable also warp button
# I'm back took a quick snack, now to complete this script.
# 6) Wowbagger's gonna kill me, no he won't :) or will he
# No matter, he has to kill all of us cause of last week's party and he was away hehe take that
# Today I'm in some kind of strange mood. I can write stupidity and I do that most of the time so nothing's wrong with me.
# Hm? Phasers and Phaser who contacted me, fire phaser *they launch phaser out of the torpedo tube, he's screaming so that the Borg simply decide to withdraw and they just say: what a naughty Borg we've been, what a naughty Borg we've been*
# 7) Okay this is really starting to get weird. It seems to never end. Oh what such lovely colors!!!
# no don't mind me and if you some wonder I don't do drugs :)
# 8) *phone rings, have to pick up and see who is it. Probably my GF, oh boy, what does she want know.*
# It's just a joke, hope she never reads this, no she won't
# 9) Okay this is really not fair. Damn how many of these subsystems exist in game, lol 11 buttons I think over here still need to make a cancel button. it won't be so difficult but it will be
# I don't know what it will be, I don't care, see if i really do care. Wowbagger cares about it lol
# Just a side note, this mostly turned out to be bugfixing and other main feature is disabling buttons. Things I had planned will go it later versions, it'll do for now.
# 10) closing near the end. hurray!!!!!!!!!!!!!!!!!!!
# :( just remembered, to say it as Master Yoda of Star Wars would say it: "Damn Globals forgot I have. This leads to the Dark Side of the Force.
# Be aware of the Dark Side. Mistakes lead to Pain, Pain leads to Suffering, Suffering leads to Hate, Hate leads to Anger, Anger leads to Hunger and Hunger is caused by an empty stomach!"
# I will never go to the Dark Side, I'm a BCS: TNG Scripter :)  (Wowbagger Adds: But *I* am a jelly doughnut!  Ich ben ein Berliner!)
# 11) I just love those wowbaggers quotes, funny very funny. We won't go to the dark side. Or are you all already there?
# Proud to be Croat (Hrvat - on Croatian)

# Enables the entire menu.  Almost.
def SetEnabledButtons():
                debug(__name__ + ", SetEnabledButtons")
                global dESR, pShieldsButton, pPowerButton, pImpulseButton, pSensorsButton, pCloakingDeviceButton, pShieldFacesButton, pPhasersButton, pTorpedoesButton, pPulseWeaponsButton, pTractorsButton, pHullButton, pCancel
                pPlayer         = MissionLib.GetPlayer()
                pPower   	= pPlayer.GetPowerSubsystem()
                pImpulse        = pPlayer.GetImpulseEngineSubsystem()
                pShields	= pPlayer.GetShields()
                pSensors        = pPlayer.GetSensorSubsystem()
                pPhasers        = pPlayer.GetPhaserSystem()
                pTorpedoes      = pPlayer.GetTorpedoSystem()
                pPulseWeapons   = pPlayer.GetPulseWeaponSystem()
                pTractors	= pPlayer.GetTractorBeamSystem()
                pCloakingDevice = pPlayer.GetCloakingSubsystem()
                pHull 		= pPlayer.GetHull()
                if pPower:
                    pPowerButton.SetEnabled()
                if pImpulse:
                    pImpulseButton.SetEnabled()
                if pSensors:
                    pSensorsButton.SetEnabled()
                if pCloakingDevice:
                    pCloakingDeviceButton.SetEnabled()
                if pShields:
                    pShieldFacesButton.SetEnabled()
                if pPhasers:
                    pPhasersButton.SetEnabled()
                if pTorpedoes:
                    pTorpedoesButton.SetEnabled()
                if pPulseWeapons:
                    pPulseWeaponsButton.SetEnabled()
                if pTractors:
                    pTractorsButton.SetEnabled()
                if pHullButton: # Note that the hull button does not necessarily exist.
                    pHullButton.SetEnabled()
                if pShields:
                    pShieldsButton.SetEnabled()
                pCancel.SetDisabled()


# Bugfix by USS Sovereign, the only way to fix the problem where some menus don't show up is have it reload itself each time the button is clicked.
# What you see over here is absolute copy of def init().  Almost. - Yeah it's almost now but oh well as I said I would have come up to this solution
# but I worked for 2 days over 12 hours bugfixing the original and was tired of it. So Nice work on this Wowy! - Sovvy
def GameRestart():
                debug(__name__ + ", GameRestart")
                global bButtonFunctionSignal, pECSMaster, pPowerButton, pImpulseButton, pSensorsButton, pCloakingDeviceButton, pShieldsButton, pShieldFacesButton, pPhasersButton, pTorpedoesButton, pPulseWeaponsButton, pTractorsButton, pHullButton, pCancel
                pGame           = App.Game_GetCurrentGame()
                pEpisode        = pGame.GetCurrentEpisode()
                pMission        = pEpisode.GetCurrentMission()
                pPlayer 	= MissionLib.GetPlayer()		
                pPower   	= pPlayer.GetPowerSubsystem()
                pImpulse        = pPlayer.GetImpulseEngineSubsystem()
                pShields	= pPlayer.GetShields()
                pSensors        = pPlayer.GetSensorSubsystem()
                pPhasers        = pPlayer.GetPhaserSystem()
                pTorpedoes      = pPlayer.GetTorpedoSystem()
                pPulseWeapons   = pPlayer.GetPulseWeaponSystem()
                pTractors	= pPlayer.GetTractorBeamSystem()
                pCloakingDevice = pPlayer.GetCloakingSubsystem()
                pHull 		= pPlayer.GetHull()
                bButtonFunctionSignal = 0

                # Get the dict working at default levels.
                ResetDESR()

                if not pPlayer:
                        print "Stop the madness!"
                        return

                # Grab stats from the last menu.  We'll need them.  Well, it.  Singular and all that.  From ille, illa, illud.
                pBridge = App.g_kSetManager.GetSet('bridge')
                pBrexMenu = Bridge.BridgeUtils.GetBridgeMenu('Engineer')
		if not pBrexMenu:
			return
                iPos = pBrexMenu.FindPos(pECSMaster)
                bOpen = pECSMaster.IsOpened()
                #Scaffold: print iPos

                # Now, kill the old menu.
                RemovePreviousMenu()

                # Add the ECS (Emergency Core Shutdown; even with all the systems in it, and
                # the "official" name change that's the name.  Cope) menu to Brex's list.
                #   As long as the Engineering Button Fix is active, there will be other
                # buttons at the bottom.  Therefore, we can use the old InsertChild() to
                # the same effect.
                pECSMaster = App.STMenu_CreateW(App.TGString("Emergency Repair"))
                pBrexMenu.InsertChild(iPos, pECSMaster, 0, 0, 0)
                #pECSMaster = Libs.BCSTNGLib.CreateEngineerMenu("Emergency Repair", "Engineer")

                if bOpen == 1:
                        pECSMaster.Open()

                # Build buttons in order opposite of that desired in the menu.
                pCancel = Libs.LibEngineering.CreateMenuButton("Cancel Repairs", "Engineer", __name__ + ".CancelRepairs", 0, pECSMaster)
                # NEW, a way to cancel or disable repairs or you can just also click on the active button cause this just also forces the system back online
                # P.S. no need for an if statement :) 
		pCloakingDeviceButton = None
                if pCloakingDevice:
                        pCloakingDeviceButton	 = Libs.LibEngineering.CreateMenuButton("Cloaking Device Status: Online", "Engineer", __name__ + ".CloakingDevice", 0, pECSMaster)
                if pTractors:
                        pTractorsButton	 	 = Libs.LibEngineering.CreateMenuButton("Tractors Status: Online", "Engineer", __name__ + ".Tractors", 0, pECSMaster)
                if pPulseWeapons:
                        pPulseWeaponsButton 	 = Libs.LibEngineering.CreateMenuButton("Pulse Weapons Status: Online", "Engineer", __name__ + ".PulseWeapons", 0, pECSMaster)   # No pulse weapons on the starting QB Galaxy class, so we improvise.
                if pTorpedoes:
                        pTorpedoesButton    	 = Libs.LibEngineering.CreateMenuButton("Torpedoes Status: Online", "Engineer", __name__ + ".Torpedoes", 0, pECSMaster)
                if pPhasers:
                        pPhasersButton     	 = Libs.LibEngineering.CreateMenuButton("Phasers Status: Online", "Engineer", __name__ + ".Phasers", 0, pECSMaster)
                if pImpulse:
                        pImpulseButton           = Libs.LibEngineering.CreateMenuButton("Engines Status: Online", "Engineer", __name__ + ".Impulse", 0, pECSMaster)
                if pSensors:
                        pSensorsButton     	 = Libs.LibEngineering.CreateMenuButton("Sensors Status: Online", "Engineer", __name__ + ".Sensors", 0, pECSMaster)
                if pPower:
                        pPowerButton       	 = Libs.LibEngineering.CreateMenuButton(str(pPower.GetName()) + " Status: Online", "Engineer", __name__ + ".Power", 0, pECSMaster)        
                if pHull:
                        if CustomizationOption != 1:
                                pHullButton 		 = Libs.LibEngineering.CreateMenuButton("Hull" + " Status: Online", "Engineer", __name__ + ".Hull", 0, pECSMaster)
                if pShields:
                        pShieldsButton     	 = Libs.LibEngineering.CreateMenuButton("Shield Generator" + " Status: Online", "Engineer", __name__ + ".Shields", 0, pECSMaster)
                        pShieldFacesButton       = Libs.LibEngineering.CreateMenuButton("Shield Recharge", "Engineer", __name__ + ".ShieldFaces", 0, pECSMaster)
                # Shield faces have their own rules.  The complete script is at the very END of ESR, out of the way of the things that make sense.
                # Yes shields have their own rules, but what if the ship has no shield generator well let's just say this button has no meaning.
        
                # Cancel button is disabled by default
                pCancel.SetDisabled()


# Sovvie's Adds: Well I know there's a function in EFX menu lib but it doesn't work and it works only for single buttons not
# for drop down menus like this. And I don't mind you borrowing this. But remember in order for this code to work you
# need a tgl string for it ;)
# And I forgot there are actually 2 menu deleting functions. I was refering to the one that deletes single buttons. Oh well this is a function that
# works for any specific menu. You can delete whole string or just button in the drop down menu, just add one more line of code. If you want to know how
# just ask!
# Wowie Adds: Thanks!  You just earned yourself 3 Wowie Points!
def RemovePreviousMenu():
        debug(__name__ + ", RemovePreviousMenu")
        g_pDatabase = App.g_kLocalizationManager.Load("data/TGL/ERmenustring.tgl")
        pBridge = App.g_kSetManager.GetSet("bridge")
        g_pBrex	= App.CharacterClass_GetObject(pBridge, "Engineer")
        pBrexMenu = g_pBrex.GetMenu()
	if (pBrexMenu != None):
		pERButton = pBrexMenu.GetSubmenu("Emergency Repair")
		if (pERButton != None):
			pBrexMenu.DeleteChild(pERButton)


# new addon added qbr restart menu handelers
# get the qbr menu button 
def GetQBRMenuButton(sMenuName, sButtonName):
        debug(__name__ + ", GetQBRMenuButton")
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
	debug(__name__ + ", GetQBRBridgeMenu")
	pTactCtrlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/QBRrestart.tgl")
	if(pDatabase is None):
		return
	return pTactCtrlWindow.FindMenu(pDatabase.GetString(menuName))


def SetSubsystemCondition(iShipObjID, pSubsystem, iNewCondition):
	debug(__name__ + ", SetSubsystemCondition")
	if pSubsystem.IsCritical() and iNewCondition < 1:
		iNewCondition = 1
	
	pSubsystem.SetCondition(iNewCondition)
	if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
		return
        # Setup the stream.
        # Allocate a local buffer stream.
        kStream = App.TGBufferStream()
        # Open the buffer stream with a 256 byte buffer.
        kStream.OpenBuffer(256)
        # Write relevant data to the stream.
        # First write message type.
        kStream.WriteChar(chr(SUBSYSTEM_SET_CONDITION))
        
        # send Message
        kStream.WriteInt(iShipObjID)
	sSubsystenName = pSubsystem.GetName()
        for i in range(len(sSubsystenName)):
                kStream.WriteChar(sSubsystenName[i])
        # set the last char:
        kStream.WriteChar('\0')
        kStream.WriteInt(iNewCondition)

        pMessage = App.TGMessage_Create()
        # Yes, this is a guaranteed packet
        pMessage.SetGuaranteed(1)
        # Okay, now set the data from the buffer stream to the message
        pMessage.SetDataFromStream(kStream)
        # Send the message to everybody but me.  Use the NoMe group, which
        # is set up by the multiplayer game.
        # TODO: Send it to asking client only
        pNetwork = App.g_kUtopiaModule.GetNetwork()
        if not App.IsNull(pNetwork):
                pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
        # We're done.  Close the buffer.
        kStream.CloseBuffer()


def SetShieldCondition(pShip, iShield, iCond, iCharge):
	debug(__name__ + ", SetShieldCondition")
	print "Setting Shield ", iShield, "to", iCharge

	pShields = pShip.GetShields()
	pShields.SetCurShields(iShield, iCond)
	if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
		pShields.GetProperty().SetShieldChargePerSecond(iShield, iCharge)
		return
        # Setup the stream.
        # Allocate a local buffer stream.
        kStream = App.TGBufferStream()
        # Open the buffer stream with a 256 byte buffer.
        kStream.OpenBuffer(256)
        # Write relevant data to the stream.
        # First write message type.
        kStream.WriteChar(chr(SET_SHIELD_CONDITION))
        
        # send Message
        kStream.WriteInt(pShip.GetObjID())
        kStream.WriteInt(iShield)
	kStream.WriteInt(iCond)

        pMessage = App.TGMessage_Create()
        # Yes, this is a guaranteed packet
        pMessage.SetGuaranteed(1)
        # Okay, now set the data from the buffer stream to the message
        pMessage.SetDataFromStream(kStream)
        # Send the message to everybody but me.  Use the NoMe group, which
        # is set up by the multiplayer game.
        # TODO: Send it to asking client only
        pNetwork = App.g_kUtopiaModule.GetNetwork()
        if not App.IsNull(pNetwork):
                pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
        # We're done.  Close the buffer.
        kStream.CloseBuffer()


from bcdebug import debug
#########################################################
# VentNanoPlasma FX                                     
#   Vents a ships plasma                                
#                                                       
#       Created by BCS:TNG                              
#               v0.0.1 Lost_Jedi                        
#               v0.0.2 Lost_Jedi                        
#                   - Geez this is crap                 
#               v0.0.3 Lost_Jedi                        
#                   - OK it doesn't crash anymore...    
#               v0.0.4 Lost_Jedi                        
#                   - Well it should have the features but boy...
#                       Wowie will go nuts when he sees how bad the
#                       source code is!
#
#               v0.5 Wowbagger
#                   - You bet I'm agitated!  I may be surrounded by
#                   insanity, but I'm not insane.  And I won't let
#                   you or anyone else tell me I am.  (pause) You can
#                   destroy my mind, but you can't change the truth.
#                   I didn't kill that man... and that's what's driving
#                   you crazy.
#                   - Tidied up.
#                   - Unalaterally changed version numbering system.  Not like
#                   CK did, but a good bit anyhow.  Let's face it: we're never going
#                   to reach v0.9.9, much less v1.0.0, at the rate we're going.  Let's
#                   save the tiny numerical changes for when it really is a small change
#                   for the version.  Is that okay?
#                   - Fixed plasma level carryover problem when player is changed.
#               v0.6 USS Sovereign
#                   - reworked the menu and fixed several issues with the mod
#                   UPDATE NOTE 26/03/2006
#                   - Moved it to Brex's menu and implemented Engineering menu fix
#
#                                                       
#########################################################

pModule = __import__("Custom.UnifiedMainMenu.ConfigModules.Options.BCSTheBeginning")

pEngineering = pModule.EngineeringOption
EngineeringOption = int(pEngineering)

import App
import MissionLib
import Libs.LibEngineering
import Libs.BCSTNGLib
import Foundation

# Mod Info Block.  Used for MP loading.
MODINFO = {     "Author": "\"BCS:TNG\" <http://bcscripterstng.forumsplace.com/>",
                "Version": "0.6",
                "License": "GPL",
                "Description": "Vent Plasma Overrides",
                "needBridge": 0
            }

# Setup Constants
FALSE = 0
TRUE = 1
DEBUG = TRUE

global StartRefil, WarpPlasmaMax, RefilRate, WarpPlasmaContent, WarpPlasmaTimeTimer
global VentAgain, bRefilStats, TimeTimer, TimeEvent, WarpPlasmaTimeEvent, iWaitTime

StartRefil = FALSE
WarpPlasmaMax = 10                                                          # Const for the how much warp plasma is in the ship
RefilRate = 0.05                                                            # How quick does the nacelle refuil itself every second
WarpPlasmaContent = 0
WarpPlasmaTimeTimer = None                                                  # Object
WarpPlasmaTimeEvent = Libs.LibEngineering.GetEngineeringNextEventType()      # Event
iWaitTime = 0.00                                                            # Max time to vent before revent
VentAgain = TRUE
bRefilStats = None
TimeTimer = None                                                            # Object
TimeEvent = Libs.LibEngineering.GetEngineeringNextEventType()                # Event


# Startup the mod. Thanks defiant! :)
def init():
    debug(__name__ + ", init")
    global WarpPlasmaContent, WarpPlasmaMax
    pGame	= App.Game_GetCurrentGame()
    pEpisode	= pGame.GetCurrentEpisode()
    pMission	= pEpisode.GetCurrentMission()

    # as we all agreed, disable these mods in MP to prevent cheating ;) -- USS Sovereign
    #if App.g_kUtopiaModule.IsMultiplayer():
    #    return

    # By USS Sovereign, checks if the mutator is active if it isn't it won't load and execute :)
    if not Libs.LibEngineering.CheckActiveMutator("BCS:TB: Targetable Plasma Streams"):
        return
        
    BuildVPSMenu()
    WarpPlasmaContent = WarpPlasmaMax
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SET_PLAYER, pMission, __name__ + ".InstantRefill")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_MISSION_START, pMission, __name__ + ".InstantRefil")

    return


# Build the menu
def BuildVPSMenu():
                debug(__name__ + ", BuildVPSMenu")
                global bOpenVents, bCloseVents, bdebug, bRefilStats

                if EngineeringOption == 1:
                    pMenu = Libs.BCSTNGLib.CreateEngineerMenu("Plasma Vents", "Engineer")

                else:
                    pMenu = CreateMenu("Plasma Vents", "Engineer")
                    
                bRefilStats = CreateButton("Status: " + "100%", "Engineer", __name__ + ".nothing", "Plasma Vents")
                bCloseVents = CreateButton("Close Plasma Vents", "Engineer", __name__ + ".CloseVents", "Plasma Vents")
                bOpenVents = CreateButton("Open Plasma Vents", "Engineer", __name__ + ".OpenVents", "Plasma Vents")

# do nothing :P               
def nothing(pObject, pEvent):
                debug(__name__ + ", nothing")
                return

# Open the plasma vents
def OpenVents(pObject = None,pEvent = None):
                debug(__name__ + ", OpenVents")
                global VentAgain
                if VentAgain == TRUE:
                    VentPlasma(App.Game_GetCurrentPlayer())
                    ### Play an sound of acknowkldgemtn
                    pSound = App.TGSound_Create("Custom/QBautostart/TPSDATA/YES.wav", "TPSOK", 0)
                    pSound.SetSFX(0)
                    pSound.SetInterface(1)
                    App.g_kSoundManager.PlaySound("TPSOK")
                    
                else:
                    ### Play an error beep sound
                    pSound = App.TGSound_Create("Custom/QBautostart/TPSDATA/NO.wav", "TPSERROR", 0)
                    pSound.SetSFX(0)
                    pSound.SetInterface(1)
                    App.g_kSoundManager.PlaySound("TPSERROR")

                return

            
# Stops player streams
def CloseVents(pObject = None,pEvent = None):
                debug(__name__ + ", CloseVents")
                global VentAgain
                from Custom.QBautostart.TargetablePlasmaStreams import StopPlayerStreams

                StopPlayerStreams()
                VentAgain = FALSE
                OKToRefil()

                return


# Timer event for the refuilling of the engine
def RefilEngineTicker(pObject = None,pEvent = None):
                debug(__name__ + ", RefilEngineTicker")
                global WarpPlasmaMax, RefilRate, WarpPlasmaContent, bRefilStats, WarpPlasmaTimeTimer, WarpPlasmaTimeEvent

                WarpPlasmaContent = WarpPlasmaContent + RefilRate

                if ((WarpPlasmaContent/WarpPlasmaMax) * 100) > 100.0:
                        bRefilStats.SetName(App.TGString("Status: 100%"))
                else:
                        bRefilStats.SetName(App.TGString("Status: " + str(round(((WarpPlasmaContent/WarpPlasmaMax)*100),2)) + "%"))
                    
                if WarpPlasmaContent >= WarpPlasmaMax:
                        # It's been refilled
                        OKToVent()
                        global StartRefil
                        StartRefil = FALSE
                else:
                        WarpPlasmaTimeTimer = MissionLib.CreateTimer(WarpPlasmaTimeEvent, __name__ + ".RefilEngineTicker", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)

                        
# Set ok to vent
def OKToVent():
                debug(__name__ + ", OKToVent")
                global VentAgain
                VentAgain = TRUE

# Set ok to refil
def OKToRefil(pObject = None, pEvent = None):
                debug(__name__ + ", OKToRefil")
                global StartRefil
                StartRefil = TRUE
                global WarpPlasmaTimeTimer, WarpPlasmaTimeEvent   
                WarpPlasmaTimeTimer = MissionLib.CreateTimer(WarpPlasmaTimeEvent, __name__ + ".RefilEngineTicker", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)



# Create a menu button
def CreateButton(name, eventNumber, eventMenu):
                debug(__name__ + ", CreateButton")
                myButton = None
                event = App.TGIntEvent_Create()
                event.SetEventType(eventNumber)
                event.SetDestination(eventMenu)
                myButton = App.STButton_Create(name, event)
               
                return myButton


# Vent Plama call
def VentPlasma(pShip):
                debug(__name__ + ", VentPlasma")
                if not pShip:
                    return FALSE
                if(MleoVent(pShip) == FALSE):
                    cout("VentPlasmaBCS: NanoFX v2.0 or Later not installed")
                    return FALSE
                else:
                    return TRUE

def MleoVent(pShip):
                debug(__name__ + ", MleoVent")
                global iWaitTime
                iWaitTime = 0
                
                # This code was *stolen* and then altered abit from Mleo's vent plasma mod. (heh but we have permission :P)
                import Custom.NanoFXv2.NanoFX_Lib
                import Custom.NanoFXv2.NanoFX_ScriptActions

                pTargetObject = pShip
                if not pTargetObject:
                        return

                vEmitPos      = pShip.GetWorldForwardTG()
                vEmitDir      = pShip.GetWorldUpTG()
                pSet 	      = pShip.GetContainingSet()
                pAttachTo     = pSet.GetEffectRoot()
                pEmitFrom     = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())
                fPlasmaColor  = Custom.NanoFXv2.NanoFX_Lib.GetOverrideColor(pShip, "PlasmaFX")
                if (fPlasmaColor == None):
                        sRace	      = Custom.NanoFXv2.NanoFX_Lib.GetSpeciesName(pShip)
                        fPlasmaColor  = Custom.NanoFXv2.NanoFX_Lib.GetRaceTextureColor(sRace)

                sFile = "scripts/Custom/NanoFXv2/SpecialFX/Gfx/Plasma/Plasma.tga"

                Seq = App.TGSequence_Create()   # Create a sequence
                pWarpSys = pShip.GetWarpEngineSubsystem()
                if pWarpSys:
                        # determine how many warp subsystems
                        iNumWarp = pWarpSys.GetNumChildSubsystems()
                        # for each warp engine on the ship make it vent plasma
                        for iEng in range(iNumWarp):
                                pWarpChild = pWarpSys.GetChildSubsystem(iEng)
                                if pWarpChild:
                                    if pWarpChild.GetCondition() > 0 or pWarpChild.IsDisabled() == 0:
                                        ### Its not destroyed or disabled
                                        fVentTime = App.g_kSystemWrapper.GetRandomNumber(25) + 60.0
                                        if fVentTime > iWaitTime:
                                            iWaitTime = fVentTime   # Take the largest wait time
                                        
                                        pPlasma = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(	sFile,
                                                                                                                App.TGModelUtils_CastNodeToAVObject(pShip.GetNode()), 
                                                                                                        pShip.GetContainingSet().GetEffectRoot(), 
                                                                                                        pShip.GetRadius() * 0.10, 
                                                                                                        pWarpChild.GetPosition(), 
                                                                                                        App.NiPoint3(0, 0, 0),
                                                                                                        bInheritVel = 0,
                                                                                                        fFrequency = 0.03,
                                                                                                        fLifeTime = fVentTime,
                                                                                                        fEmitVel = 0.1,
                                                                                                        fVariance = 150.0,
                                                                                                        iTiming = 72,
                                                                                                        sType = "Plasma",
                                                                                                        fRed = fPlasmaColor[0], 
                                                                                                        fGreen = fPlasmaColor[1], 
                                                                                                        fBlue = fPlasmaColor[2],
                                                                                                        fBrightness = 0.10) 
                                Seq.AddAction(pPlasma)

                                pPlasma = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(	sFile,
                                                                                                        App.TGModelUtils_CastNodeToAVObject(pShip.GetNode()), 
                                                                                                        pShip.GetContainingSet().GetEffectRoot(), 
                                                                                                        pShip.GetRadius() * 0.05, 
                                                                                                        pWarpChild.GetPosition(), 
                                                                                                        App.NiPoint3(0, 0, 0),
                                                                                                        bInheritVel = 0,
                                                                                                        fFrequency = 0.03,
                                                                                                        fLifeTime = fVentTime,
                                                                                                        fEmitVel = 0.1,
                                                                                                        fVariance = 150.0,
                                                                                                        iTiming = 32,
                                                                                                        sType = "Plasma",
                                                                                                        fRed = fPlasmaColor[0], 
                                                                                                        fGreen = fPlasmaColor[1], 
                                                                                                        fBlue = fPlasmaColor[2],
                                                                                                        fBrightness = 0.60)
                                Seq.AddAction(pPlasma)

                                sSound = "Plasma"
                                
                                ### Add an action to play the sound. ###
                                if pShip.GetName() == "Player" or pShip.GetName() == "player":
                                        ### Vent Sounds ###
                                        pSound = App.TGSoundAction_Create("Player_Burst.wav", 0, pSet.GetName())
                                        pSound.SetNode(pShip.GetNode())
                                        Seq.AddAction(pSound)
                                        pSound = App.TGSoundAction_Create("Player_Vent.wav", 0, pSet.GetName())
                                        pSound.SetNode(pShip.GetNode())
                                        Seq.AddAction(pSound)
                                        pSound = App.TGSoundAction_Create("Player_Seal.wav", 0, pSet.GetName())
                                        pSound.SetNode(pShip.GetNode())
                                        Seq.AddAction(pSound, App.TGAction_CreateNull(), fVentTime)
                                        
                                ### BCS:TNG Targetable Plasma Streams Insert                              
                                from Custom.QBautostart.TargetablePlasmaStreams import AppendPlasmaTracker
                                AppendPlasmaTracker(pWarpChild, fVentTime, pShip, Seq)
                                ###
                                
                                Seq.Play()
                                
                global VentAgain, WarpPlasmaContent, bRefilStats, TimeTimer, TimeEvent
                VentAgain = FALSE
                WarpPlasmaContent = 0
                bRefilStats.SetName(App.TGString("Status: 0%"))
                TimeTimer = MissionLib.CreateTimer(TimeEvent, __name__ + ".OKToRefil", App.g_kUtopiaModule.GetGameTime() + iWaitTime, 0, 0)

                return
            

# Outputs data to the console.
def cout(sString):
                debug(__name__ + ", cout")
                if DEBUG == TRUE:
                    print sString
                return


# Like the coffee, this function gives you a full plasma vent instantly.  Bet you didn't know that about instant coffee, eh?
def InstantRefill(pObject, pEvent):
                debug(__name__ + ", InstantRefill")
                global WarpPlasmaContent, WarpPlasmaMax, bRefilStats
                WarpPlasmaContent = WarpPlasmaMax
                bRefilStats.SetName(App.TGString("Status: 100%")) 
                return

# from BCS: TNG Library a new and easier way to create a button
def CreateButton(sButtonName, sMenuName, Function, sToButton = None, EventInt = 0):        
        debug(__name__ + ", CreateButton")
        pMenu = GetBridgeMenu(sMenuName)

        if sToButton:
                pToButton = pMenu.GetSubmenu(sToButton)
        
        ET_EVENT = App.Mission_GetNextEventType()

        pMenu.AddPythonFuncHandlerForInstance(ET_EVENT, Function)

        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_EVENT)
        pEvent.SetDestination(pMenu)
        pEvent.SetInt(EventInt)
        pButton = App.STButton_CreateW(App.TGString(sButtonName), pEvent)
    
        if not pToButton:
                pMenu.PrependChild(pButton)
        else:
                pToButton.PrependChild(pButton)

        return pButton

# Also from our new library
def CreateMenu(sNewMenuName, sBridgeMenuName):
	debug(__name__ + ", CreateMenu")
	pMenu = GetBridgeMenu(sBridgeMenuName)
       	pNewMenu = App.STMenu_Create(sNewMenuName)
	pMenu.PrependChild(pNewMenu)

        return pNewMenu

# Also from our new library
def GetBridgeMenu(menuName):
	debug(__name__ + ", GetBridgeMenu")
	pTactCtrlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	if(pDatabase is None):
		return
	App.g_kLocalizationManager.Unload(pDatabase)
	return pTactCtrlWindow.FindMenu(pDatabase.GetString(menuName))

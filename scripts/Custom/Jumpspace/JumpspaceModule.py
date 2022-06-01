# by Mario aka USS Sovereign

# Meet the future!!! This is what will hopefully drive all alternative means of travel anyone can think of.

# All rights reserved. Do not modify this or any part of the mod without extreme permission from the authors!


# Version signature
VERSION = '20070905'

# Imports
import App
import MissionLib
import loadspacehelper
import nt
import string
from Custom.Jumpspace.Libs import DS9FXMenuLib
from Custom.Jumpspace.Libs import LoadFlash
from Custom.Jumpspace.Libs import AimForGoodPos
from Custom.Jumpspace.Libs import AimForGoodPosExit
from Custom.Jumpspace.Libs import EngineStats
from Custom.Jumpspace.Libs import EngineStatsETA
from Custom.Jumpspace.Libs import EngineStatsIdealETA
from Custom.Jumpspace.Libs import EngineStatsMenuCalc
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import JumpspaceConfiguration

# Events
ET_ENGAGE = App.UtopiaModule_GetNextEventType()
ET_UPDATE_SLIDER = App.UtopiaModule_GetNextEventType()
ET_REFRESH = App.UtopiaModule_GetNextEventType()
ET_CLOSE = App.UtopiaModule_GetNextEventType()

# Vars
bMenu = None
bInterceptMenu = None
bNavPointButton = None
bInterceptButton = None
bButton = None
pTimer = None
pTimerETA = None
pTimerIdealETA = None
pTimerEngineStats = None
pPane = None
pMainPane = None
pSelectedSpeed = None
pTotalEngineStatsText = None
pETAText = None
pIdealETAText = None 
pSelectedSpeedText = None
pSlider = None
pDefault = None
pSupported = 0
pButtonCondition = 1

# Pane ID
pPaneID = None

# Cloaked?
pWasCloaked = 0

# Navpoint default distance
dist = 1500

# List of asteroid scripts
sAsteroidList = ["ships.Asteroid", "ships.Asteroid1", "ships.Asteroid2", "ships.Asteroid3", "ships.Asteroidh1", "ships.Asteroidh2", "ships.Asteroidh3"]

# List of hull properties Jumpspace looks for
sJumpspaceList = ['Jumpspace Drive 1', 'Jumpspace Drive 2', 'Jumpspace Drive 3', 'Jumpspace Drive 4', 'Jumpspace Drive 5', 'Jumpspace Drive 6', 'Jumpspace Drive 7', 'Jumpspace Drive 8', 'Jumpspace Drive 9', 'Jumpspace Drive 10', 'Jumpspace Drive 11', 'Jumpspace Drive 12', 'Jumpspace Drive 13', 'Jumpspace Drive 14', 'Jumpspace Drive 15', 'Jumpspace Drive 16', 'Jumpspace Drive 17', 'Jumpspace Drive 18', 'Jumpspace Drive 19', 'Jumpspace Drive 20']

# Drive Condition List
lStats = []
lStatsETA = []
lStatsIdealETA = []
lStatsEngines = []

# Path
sPath = "scripts\\Custom\\Jumpspace\\Libs\\EngineStats.py"
sPathETA = "scripts\\Custom\\Jumpspace\\Libs\\EngineStatsETA.py"
sPathIdealETA = "scripts\\Custom\\Jumpspace\\Libs\\EngineStatsIdealETA.py"
sPathStats = "scripts\\Custom\\Jumpspace\\Libs\\EngineStatsMenuCalc.py"

# Tunnel Engine noise is hardcoded and not customizable
pJumpspaceEngineSound = App.TGSound_Create("scripts/Custom/Jumpspace/SFX/Jumpspaceenginenoise.wav", "JumpspaceEngineSound", 0)
pJumpspaceEngineSound.SetSFX(0) 
pJumpspaceEngineSound.SetInterface(1)
pJumpspaceEngineSound.SetLooping(1)


# Main function called by the zzzJumpspaceMode.py
def init():
        global bMenu, bInterceptMenu, bNavPointButton, bInterceptButton, bButton, pSupported, pButtonCondition

        if not pSupported == 1:
            return

        # Reset stats
        pButtonCondition = 1

        # Remove any existing buttons
        RemoveMenu()

        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()

        # Navpoint exists?
        try:
            pSet.DeleteObjectFromSet("Jumpspace Navpoint")
        except:
            pass

        # Handler active?
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_MOUSE, pMission, __name__ + ".MoveNavpoint")
        except:
            pass

        JumpspaceInstalled = HasJumpspace(pPlayer)
        if not JumpspaceInstalled == 'Jumpspace Installed':
            return

        # Create menus and buttons
        bMenu = DS9FXMenuLib.CreateMenu("Jumpspace Details", "Helm", 2, 0)
        bButton = DS9FXMenuLib.CreateButton("Jumpspace Drive", "Helm", __name__ + ".JumpspaceGUI", "Jumpspace Details")
        bInterceptMenu = App.STMenu_CreateW(App.TGString("Intercept Options"))
	bMenu.PrependChild(bInterceptMenu)
        bInterceptButton = DS9FXMenuLib.CreateBridgeMenuButton("Jumpspace Intercept", "Helm", __name__ + ".JumpspaceInterceptStats", bInterceptMenu)
        bNavPointButton = DS9FXMenuLib.CreateBridgeMenuButton("Initiate Navpoint Mode", "Helm", __name__ + ".JumpspaceNavpoint", bInterceptMenu)
        
        # Button properties
        NormalColor = App.TGColorA() 
	NormalColor.SetRGBA(0.8, 0.6, 0.8, 1.0)
	HilightedColor = App.TGColorA() 
	HilightedColor.SetRGBA(0.92, 0.76, 0.92, 1.0)
	NormalColor2 = App.TGColorA() 
	NormalColor2.SetRGBA(0.5, 0.5, 1.0, 1.0)
	HilightedColor2 = App.TGColorA() 
	HilightedColor2.SetRGBA(0.61, 0.61, 1.0, 1.0)
	DisabledColor = App.TGColorA() 
	DisabledColor.SetRGBA(0.25, 0.25, 0.25, 1.0)
	bButton.SetUseUIHeight(0)
	bButton.SetNormalColor(NormalColor)
        bButton.SetHighlightedColor(HilightedColor)
        bButton.SetSelectedColor(NormalColor)
        bButton.SetDisabledColor(DisabledColor)
        bButton.SetColorBasedOnFlags()
        bButton.SetDisabled()
        bInterceptButton.SetUseUIHeight(0)
	bInterceptButton.SetNormalColor(NormalColor2)
        bInterceptButton.SetHighlightedColor(HilightedColor2)
        bInterceptButton.SetSelectedColor(NormalColor2)
        bInterceptButton.SetDisabledColor(DisabledColor)
        bInterceptButton.SetColorBasedOnFlags()
        bNavPointButton.SetUseUIHeight(0)
	bNavPointButton.SetNormalColor(NormalColor2)
        bNavPointButton.SetHighlightedColor(HilightedColor2)
        bNavPointButton.SetSelectedColor(NormalColor2)
        bNavPointButton.SetDisabledColor(DisabledColor)
        bNavPointButton.SetColorBasedOnFlags()

        # Resolve the small issue when the warp button is enabled and Jumpspace is not
        ClearCourseSetting(None)


# Just activate needed handlers
def handlers():
        global pSupported

        # Check if this is the supported game type
        pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()

        if pMission.GetScript() == "QuickBattle.QuickBattle":
            print 'Jumpspace: Quick Battle is running... Mod is starting up...'
            pSupported = 1
            # Possible bugfix
            init()
        elif pMission.GetScript() == "Custom.QuickBattleGame.QuickBattle":
            print 'Jumpspace: Quick Battle Replacement is running... Mod is starting up...'
            pSupported = 1
            # Possible bugfix
            init()
	else:
	    print 'Jumpspace: Unsupported game type is running... Mod is shutting down...'
	    pSupported = 0
	    return
	
        # Detect course set event
        pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SET_COURSE, pMission, __name__ + ".CourseSet")


# Disable button 
def disablebutton():
        global bButton, pSupported, pButtonCondition, bNavPointButton

        if not pSupported == 1:
            return

        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()
                
        # Navpoint deleted
        try:
            pSet.DeleteObjectFromSet("Jumpspace Navpoint")
        except:
            pass
                
        # Handler deactivated
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_MOUSE, pMission, __name__ + ".MoveNavpoint")
        except:
            pass
                
        # No need to trigger this function more then it's necessary
        if not pButtonCondition == 1:
            # Change button stats and delete the navpoint
            pButtonCondition = 1
            if hasattr(bNavPointButton, 'SetName'):
                bNavPointButton.SetName(App.TGString("Initiate Navpoint Mode"))
            
        if bButton is None:
            return

        if hasattr(bButton, 'SetDisabled'):
            if bButton.IsEnabled():
                bButton.SetDisabled()


# Delete navpoint when exiting
def delnavpoint():
        global pSupported, pButtonCondition, bNavPointButton
        
        if not pSupported == 1:
            return

        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()
            
        # Navpoint deleted
        try:
            pSet.DeleteObjectFromSet("Jumpspace Navpoint")
        except:
            pass
            
        # Handler deactivated
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_MOUSE, pMission, __name__ + ".MoveNavpoint")
        except:
                pass
            
        # No need to trigger this function more then it's necessary
        if not pButtonCondition == 1:
            # Change button stats and delete the navpoint
            pButtonCondition = 1
            if hasattr(bNavPointButton, 'SetName'):
                bNavPointButton.SetName(App.TGString("Initiate Navpoint Mode"))


# Quitting QB deactivate handlers
def quitting():
        global pMainPane, pPane, pSupported

        if not pSupported == 1:
            return
    
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        try:
            App.g_kSoundManager.StopSound("JumpspaceEngineSound")
        except:
            pass
        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_SET_COURSE, pMission, __name__ + ".CourseSet")
        except:
            pass
        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".FixDarkScreen")
        except:
            pass
        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_DESTROYED, pMission, __name__ + ".FixDarkScreenExplosions")
        except:
            pass
        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_MOUSE, pMission, __name__ + ".MoveNavpoint")
        except:
            pass
        try:
            App.g_kEventManager.RemoveBroadcastHandler(ET_ENGAGE, pMission, __name__ + ".JumpspaceStats")
        except:
            pass
        try:
            App.g_kEventManager.RemoveBroadcastHandler(ET_UPDATE_SLIDER, pMission, __name__ + ".UpdateSlider")
        except:
            pass
        try:
            App.g_kEventManager.RemoveBroadcastHandler(ET_REFRESH, pMission, __name__ + ".UpdateStats")
        except:
            pass
        try:
            App.g_kEventManager.RemoveBroadcastHandler(ET_CLOSE, pMission, __name__ + ".CloseGUI")
        except:
            pass

        if not pPane == None:
                # Let's not cause any crashes
                pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
                try:
                    # Just destroy the window, we don't need it anymore.
                    App.g_kFocusManager.RemoveAllObjectsUnder(pPane)

                    pTCW.DeleteChild(pPane)

                    pPane = None
                    
                except:
                    pass


# Course is set                
def CourseSet(pObject, pEvent):
        global bButton, pDest

        # Compare events
        if not (pEvent.GetInt() == App.CharacterClass.EST_SET_COURSE_INTERCEPT):

            # Hack into the set course destination
            pWarp = App.SortedRegionMenu_GetWarpButton()
            pDest = pWarp.GetDestination()

            # Incompatibility fix for hyperdrive & jumpspace
            if hasattr(bButton, 'SetEnabled'):
                if not bButton.IsEnabled():
                    bButton.SetEnabled()

        # Pass event onto the next handler
        pObject.CallNextHandler(pEvent)


# Create a navpoint
def JumpspaceNavpoint(pObject, pEvent):
        global pButtonCondition, bNavPointButton, dist

        # Reset dist
        dist = 1500
        
        if pButtonCondition == 1:
            # Button stats changed and name
            pButtonCondition = 0
            bNavPointButton.SetName(App.TGString("Stop Navpoint Mode"))
            
            # Create the navpoint
            pPlayer = MissionLib.GetPlayer()
            pSet = pPlayer.GetContainingSet()
            pLoc = pPlayer.GetWorldLocation()
            strNav = "Jumpspace Navpoint"
            pNav = loadspacehelper.CreateShip("Distortion", pSet, strNav, None)

            fNav = MissionLib.GetShip(strNav, pSet) 
            fNav.SetTranslateXYZ(pLoc.GetX() + 150, pLoc.GetY() + 150, pLoc.GetZ())
            fNav.UpdateNodeOnly()
            fNav.SetHidden(1)
            fNav.SetInvincible(1)
            fNav.SetHurtable(0)

            # Remove the nav point from the proximity manager
            ProximityManager = pSet.GetProximityManager()
            ProximityManager.RemoveObject(fNav)
            
            # Setup a handler
            pGame = App.Game_GetCurrentGame()
            pEpisode = pGame.GetCurrentEpisode()
            pMission = pEpisode.GetCurrentMission()
            App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_MOUSE, pMission, __name__ + ".MoveNavpoint")

        else:
            # Change button stats and delete the navpoint
            pButtonCondition = 1
            bNavPointButton.SetName(App.TGString("Initiate Navpoint Mode"))
            pPlayer = MissionLib.GetPlayer()
            pSet = pPlayer.GetContainingSet()
            
            # Navpoint deleted
            try:
                pSet.DeleteObjectFromSet("Jumpspace Navpoint")
            except:
                pass
            
            # Handler deactivated
            pGame = App.Game_GetCurrentGame()
            pEpisode = pGame.GetCurrentEpisode()
            pMission = pEpisode.GetCurrentMission()

            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_MOUSE, pMission, __name__ + ".MoveNavpoint")
            except:
                pass


# Move the navpoint by converting mouse xy to 3d xyz
def MoveNavpoint(pObject, pEvent):
        global dist

        # Has attr?
        if not hasattr(pEvent, 'GetButtonNum') and hasattr(pEvent, 'GetFlags'):
            return

        # Tactical mode?
        if not App.TopWindow_GetTopWindow().IsTacticalVisible():
            return

        # Grab mouse button number and flag
        eButton = pEvent.GetButtonNum()
        eFlag = pEvent.GetFlags()
        
        if eButton == 2048 and eFlag == 2816:
            pass

        elif eButton == 4096 and eFlag == 4864:
            dist = dist + 1000
            if dist > 11500:
                dist = 1500

        else:
            return

        # Admiral Ames was a very smart guy!
        eX = pEvent.GetX() * (dist) - (dist/2)
        eY = pEvent.GetY() * (-dist) + (dist/2)

        # Grab some values
        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()
        pLoc = pPlayer.GetWorldLocation()
        pGame = App.Game_GetCurrentGame()
        pCamera = pGame.GetPlayerCamera()
        pFwdCam = pCamera.GetWorldForwardTG()
        pUpCam = pCamera.GetWorldUpTG()
        pRightCam = pCamera.GetWorldRightTG()

        # Calculate the xyz's
        cordX = dist * pFwdCam.GetX() + eX * pRightCam.GetX() + eY * pUpCam.GetX()
        cordY = dist * pFwdCam.GetY() + eX * pRightCam.GetY() + eY * pUpCam.GetY()
        cordZ = dist * pFwdCam.GetZ() + eX * pRightCam.GetZ() + eY * pUpCam.GetZ()

        # Translate the navpoint finally
        fNav = MissionLib.GetShip("Jumpspace Navpoint", pSet) 
        fNav.SetTranslateXYZ(pLoc.GetX() + cordX, pLoc.GetY() + cordY, pLoc.GetZ() + cordZ)
        fNav.UpdateNodeOnly()


# The newest addition to the jumpspace family in system jumpspace intercept, fast as hell on great distances
def JumpspaceInterceptStats(pObject, pEvent):
        global lStats

        # Reset lstats
        lStats = []
        
        # Grab values
        pPlayer = MissionLib.GetPlayer()
        pIterator = pPlayer.StartGetSubsystemMatch(App.CT_HULL_SUBSYSTEM)
	pSystem = pPlayer.GetNextSubsystemMatch(pIterator)

	# Add the stats of each engine into the list
        while (pSystem != None):
		if pSystem.GetName() in sJumpspaceList:
                   pStats = pSystem.GetConditionPercentage() * 100.0
                   pDisabled = pSystem.GetDisabledPercentage() * 100.0
                   if pStats <= pDisabled:
                       # Engine is disabled, treat it like it's destroyed
                       pStats = 0.0
                       
                   lStats.append(pStats)
                   
		pSystem = pPlayer.GetNextSubsystemMatch(pIterator)

        pPlayer.EndGetSubsystemMatch(pIterator)

        file = nt.open(sPath, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
        nt.write(file, "# Do not Edit this file, Jumpspace uses it to store data\n")
        i = 0
        # Write stats into the file
        for stat in lStats:
            i = i + 1
            nt.write(file, "\nJumpspaceDrive" + str(i) + " = " + str(stat))

        # We need to write all 20 lines into that file
        nTotal = i
        nCount = 20
        loop = 1
        while loop == 1:
            i = i + 1
            nt.write(file, "\nJumpspaceDrive" + str(i) + " = " + "0.0")
            # Kill the loop
            if i >= nCount:
                loop = 0

        # Close file
        nt.close(file)

        # Reload EngineStats to get the latest engine status
        reload(EngineStats)

        iTotal = EngineStats.JumpspaceDrive1 + EngineStats.JumpspaceDrive2 + EngineStats.JumpspaceDrive3 + EngineStats.JumpspaceDrive4 + EngineStats.JumpspaceDrive5 + EngineStats.JumpspaceDrive6 + EngineStats.JumpspaceDrive7 + EngineStats.JumpspaceDrive8 + EngineStats.JumpspaceDrive9  + EngineStats.JumpspaceDrive10 + EngineStats.JumpspaceDrive11 + EngineStats.JumpspaceDrive12 + EngineStats.JumpspaceDrive13 + EngineStats.JumpspaceDrive14 + EngineStats.JumpspaceDrive15 + EngineStats.JumpspaceDrive16 + EngineStats.JumpspaceDrive17 + EngineStats.JumpspaceDrive18 + EngineStats.JumpspaceDrive19 + EngineStats.JumpspaceDrive20 

        pTotal = iTotal / nTotal

        # Can't jump if the engines are below 1%
        if pTotal < 1.0:
            print 'Jumpspace: Jumpspace Engines are badly damaged, cannot intercept target'
            return

        # GUI was open? Try to kill it!
        CloseGUI(None, None)

        # Engine stats is OK, let's start the next phase. See if we actually are targetting something
        InterceptTargetCheck()


# Are we targetting something?!
def InterceptTargetCheck():
        global bInterceptButton
        
        pPlayer = MissionLib.GetPlayer()
        pTargetShip = App.ShipClass_Cast(pPlayer.GetTarget())
        pTargetPlanet = App.Planet_Cast(pPlayer.GetTarget())

        if pTargetPlanet:
            if not DistanceCheck(pTargetPlanet) >= 400:
                bInterceptButton.SetName(App.TGString("TOO CLOSE"))
                pSequence = App.TGSequence_Create()
                pAction = App.TGScriptAction_Create(__name__, "ResetButtonString", bInterceptButton)
                pSequence.AddAction(pAction, None, 1)
                pSequence.Play()
                # print 'Jumpspace: Planet is too close...'
                return
            
            InterceptTarget(pTargetPlanet, IsPlanet = 1)

        elif pTargetShip:
            if not DistanceCheck(pTargetShip) >= 250:
                bInterceptButton.SetName(App.TGString("TOO CLOSE"))
                pSequence = App.TGSequence_Create()
                pAction = App.TGScriptAction_Create(__name__, "ResetButtonString", bInterceptButton)
                pSequence.AddAction(pAction, None, 1)
                pSequence.Play()
                # print 'Jumpspace: Ship is too close...'
                return
            
            InterceptTarget(pTargetShip, IsPlanet = 0)

        else:
            bInterceptButton.SetName(App.TGString("NO TARGET"))
            pSequence = App.TGSequence_Create()
            pAction = App.TGScriptAction_Create(__name__, "ResetButtonString", bInterceptButton)
            pSequence.AddAction(pAction, None, 1)
            pSequence.Play()
            # print 'Jumpspace: No target...'
            return


# Reset button string warning
def ResetButtonString(pAction, pButton):
        try:
            pButton.SetName(App.TGString("Jumpspace Intercept"))
        except:
            pass

        return 0
    

# Checks distance between the player and the given object
def DistanceCheck(pObject):
	pPlayer = App.Game_GetCurrentGame().GetPlayer()
	vDifference = pObject.GetWorldLocation()
	vDifference.Subtract(pPlayer.GetWorldLocation())

	return vDifference.Length()


# Let's intercept our target
def InterceptTarget(pTarget, IsPlanet):
        global pWasCloaked
        
        # Grab values and start the prescripted sequence
        pPlayer = App.Game_GetCurrentPlayer()    
        pSequence = App.TGSequence_Create ()
        pSequence.AddAction(App.TGScriptAction_Create("MissionLib", "StartCutscene"))
        pSequence.AddAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
        pSequence.AddAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))
        pSequence.AddAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", pPlayer.GetContainingSet().GetName(), pPlayer.GetName ()))
        pSequence.AddAction(App.TGScriptAction_Create(__name__, "PositionPlayerIntercept", pTarget, IsPlanet))
        pSequence.Play()

        # I have to grab the player over here and see if he's actually cloaked
        pWasCloaked = 0
        if pPlayer.IsCloaked():
            pWasCloaked = 1
            pCloak = pPlayer.GetCloakingSubsystem()
            if pCloak:
                pCloak.InstantDecloak()
            

# Redirect function
def PositionPlayerIntercept(pAction, pTarget, IsPlanet):
        # Initiate search AI
        InitiateSearchAI()

        # Start the supplimentary function
        AdditionalPosAndCheckIntercept(None, pTarget, IsPlanet)

        return 0
        

# Do the additional sweep to aid the 360 degree spin
def AdditionalPosAndCheckIntercept(pAction, pTarget, IsPlanet):
        global pDefault
    
        # Positioning function
        AimForGoodPos.GoodAim()

        # Check aim
        sAim = AimForGoodPos.CheckGoodAim()
        
        # Good Aim
        if sAim == 'TRUE':               
                # Who the hell knows, something still might go wrong. Better be safe then sorry!
                pGame = App.Game_GetCurrentGame()
                pGame.SetGodMode(1)
                # Collision settings
                pDefault = App.ProximityManager_GetPlayerCollisionsEnabled()
                App.ProximityManager_SetPlayerCollisionsEnabled(0)

                # Grab player and set 
                pPlayer = MissionLib.GetPlayer()
                pSet = pPlayer.GetContainingSet()

                # Create & allign cam placement
                pCamPlacement = App.PlacementObject_Create(pPlayer.GetName() + str(pSet.GetName()) + str(App.g_kUtopiaModule.GetGameTime()), pPlayer.GetContainingSet().GetName (), None)
                pPlayerLoc = pPlayer.GetWorldLocation()
                pPlayerX = pPlayerLoc.GetX()
                cordX = pPlayerX + pPlayer.GetWorldBackwardTG().GetX() + 1
                pPlayerY = pPlayerLoc.GetY()
                cordY = pPlayerY + pPlayer.GetWorldBackwardTG().GetY()
                pPlayerZ = pPlayerLoc.GetZ()
                cordZ = pPlayerZ + pPlayer.GetWorldBackwardTG().GetZ() + 1
                pPlayerBackward = pPlayer.GetWorldBackwardTG()
                pPlayerDown = pPlayer.GetWorldUpTG()
                pCamPlacement.SetTranslateXYZ(cordX, cordY, cordZ)
                pCamPlacement.AlignToVectors(pPlayerBackward, pPlayerDown)
                pCamPlacement.UpdateNodeOnly()

                # All in one, entry and exiting no set swapping
                pSequence = App.TGSequence_Create()
                pAction = App.TGScriptAction_Create("MissionLib", "StartCutscene")
                pSequence.AddAction(pAction, None, 0) 
                pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0)
                pSequence.AddAction(pAction, None, 0) 
                pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ())
                pSequence.AddAction(pAction, None, 0)
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "TargetWatch", pPlayer.GetContainingSet().GetName (), pCamPlacement.GetName(), pPlayer.GetName(), 0))
                pAction = App.TGScriptAction_Create(__name__, "MoveForwardAI")
                pSequence.AddAction(pAction, None, 1.5)
                pAction = App.TGScriptAction_Create(__name__, "EnteringFlash")
                pSequence.AddAction(pAction, None, 1.5)
                pAction = App.TGScriptAction_Create(__name__, "MaxSpeed")
                pSequence.AddAction(pAction, None, 1.5)
                pAction = App.TGScriptAction_Create(__name__, "JumpspaceFlash")
                pSequence.AddAction(pAction, None, 2.5)
                pAction = App.TGScriptAction_Create(__name__, "HidePlayer")
                pSequence.AddAction(pAction, None, 4.5)
                pAction = App.TGScriptAction_Create(__name__, "RestoreSpeedValues")
                pSequence.AddAction(pAction, None, 5.5)
                pAction = App.TGScriptAction_Create(__name__, "ClearAIs")
                pSequence.AddAction(pAction, None, 5.5)
                pAction = App.TGScriptAction_Create(__name__, "SwapPlayerPos", pTarget, IsPlanet)
                pSequence.AddAction(pAction, None, 5.5)
                pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", pPlayer.GetContainingSet().GetName(), pPlayer.GetName())
                pSequence.AddAction(pAction, None, 6)
                pAction = App.TGScriptAction_Create(__name__, "JumpspaceFlashExit")
                pSequence.AddAction(pAction, None, 6.5)
                pAction = App.TGScriptAction_Create(__name__, "MoveForwardAI")
                pSequence.AddAction(pAction, None, 6.5)
                pAction = App.TGScriptAction_Create(__name__, "ExitingFlash")
                pSequence.AddAction(pAction, None, 7)
                pAction = App.TGScriptAction_Create(__name__, "UnhidePlayer")
                pSequence.AddAction(pAction, None, 8)
                pAction = App.TGScriptAction_Create(__name__, "ClearAIs")
                pSequence.AddAction(pAction, None, 10)
                pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pPlayer.GetContainingSet().GetName())
                pSequence.AddAction(pAction, None, 10)
                pAction = App.TGScriptAction_Create("MissionLib", "EndCutscene")
                pSequence.AddAction(pAction, None, 10)
                pAction = App.TGScriptAction_Create(__name__, "BackToNormal")
                pSequence.AppendAction(pAction)

                pSequence.Play()

        # Bad Aim, repeat process
        else:
                # Use sequence counter
                pSequence = App.TGSequence_Create()
                pAction = App.TGScriptAction_Create(__name__, "AdditionalPosAndCheckIntercept", pTarget, IsPlanet)
                pSequence.AddAction(pAction, None, 1)
                pSequence.Play()

        return 0


# Swap players position
def SwapPlayerPos(pAction, pTarget, IsPlanet):
    
        pPlayer = MissionLib.GetPlayer()
        
        # Target is planet
        if IsPlanet == 1:
                fRadius = pTarget.GetAtmosphereRadius() * 3
                
                pLocation = pTarget.GetWorldLocation()

                pTargetX = pLocation.GetX()
                    
                pTargetY = pLocation.GetY()
                    
                pTargetZ = pLocation.GetZ()

                # Take into account the atmosphere, given the fact that the planet was properly scripted...
                RateX = GetRandomRate(5, 200)

                RateY = GetRandomRate(5, 200)

                RateZ = GetRandomRate(5, 200)

                pXCoord = pTargetX + RateX + fRadius

                pYCoord = pTargetY + RateY + fRadius

                pZCoord = pTargetZ + RateZ + fRadius

                pPlayer.SetTranslateXYZ(pXCoord, pYCoord, pZCoord)

                pPlayer.UpdateNodeOnly() 

                # Update proximity manager info for player
                ProximityManager = pPlayer.GetContainingSet().GetProximityManager() 
                if (ProximityManager): 
                        ProximityManager.UpdateObject(pPlayer)

                # Kill the navpoint mode
                ResetNavpoints()
                        

        # Target can only be a ship
        else:
                fRadius = pTarget.GetRadius() * 2
                
                pLocation = pTarget.GetWorldLocation()

                pTargetX = pLocation.GetX()
                    
                pTargetY = pLocation.GetY()
                    
                pTargetZ = pLocation.GetZ()

                # Luckily ships don't have atmospheres
                RateX = GetRandomRate(5, 50)

                RateY = GetRandomRate(5, 50)

                RateZ = GetRandomRate(5, 50)

                pXCoord = pTargetX + RateX + fRadius

                pYCoord = pTargetY + RateY + fRadius

                pZCoord = pTargetZ + RateZ + fRadius

                pPlayer.SetTranslateXYZ(pXCoord, pYCoord, pZCoord)

                pPlayer.UpdateNodeOnly() 

                # Update proximity manager info for player
                ProximityManager = pPlayer.GetContainingSet().GetProximityManager() 
                if (ProximityManager): 
                        ProximityManager.UpdateObject(pPlayer)

                # Kill the navpoint mode
                ResetNavpoints()
                        
        return 0


# Reset navpoints after in system jump
def ResetNavpoints():
        global pButtonCondition
        
        # Change button stats and delete the navpoint
        pButtonCondition = 1
        bNavPointButton.SetName(App.TGString("Initiate Navpoint Mode"))
        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()
            
        # Navpoint deleted
        try:
            pSet.DeleteObjectFromSet("Jumpspace Navpoint")
        except:
            pass
            
        # Handler deactivated
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_MOUSE, pMission, __name__ + ".MoveNavpoint")
        except:
            pass    


# Create the GUI window       
def JumpspaceGUI(pObject, pEvent):
        global pMainPane, pPane

        if not pPane == None:
            return

        # DS9FX code
        pPane = App.TGPane_Create(1.0, 1.0) 
	pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
	pTCW.AddChild(pPane, 0, 0) 
	pMainPane = App.TGPane_Create(0.4, 0.4) 
	pPane.AddChild(pMainPane, 0.35, 0.10)
                
        # Grab some values
        pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()

        # Setup Events
	App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_ENGAGE, pMission, __name__ + ".JumpspaceStats")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_UPDATE_SLIDER, pMission, __name__ + ".UpdateSlider")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_REFRESH, pMission, __name__ + ".UpdateStats")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_CLOSE, pMission, __name__ + ".CloseGUI")

        # Create Entries now
        CreateEntries(None, None)


# Create buttons, windows, entries...
def CreateEntries(pObject, pEvent):
        global pMainPane, pPane, pSelectedSpeed, pTotalEngineStatsText, pETAText, pIdealETAText, pSelectedSpeedText, pSlider, pDetailsWindow, pFunctionsWindow, pSliderWindow, pOptionsWindow

        # We need 3 windows
        pDetailsWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Ship/Speed Details"), 0.0, 0.0, None, 1, 0.19, 0.20, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pDetailsWindow, 0, 0)

        pFunctionsWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Function Selection"), 0.0, 0.0, None, 1, 0.19, 0.19, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pFunctionsWindow , 0, 0.21)
        
        pSliderWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Speed Selector"), 0.0, 0.0, None, 1, 0.19, 0.20, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pSliderWindow, 0.21, 0)

        pOptionsWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Engage Jumpspace"), 0.0, 0.0, None, 1, 0.19, 0.19, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pOptionsWindow, 0.21, 0.21)

        # Check for specified max speed
        pPlayer = MissionLib.GetPlayer()
        pModule = __import__(pPlayer.GetScript())

        # Is there a customization for this ship available?
        if hasattr(pModule, "JumpspaceCustomizations"):
            pCustomization = pModule.JumpspaceCustomizations()
            
            # Customization exists, but does the speed entry exist?!
            if pCustomization.has_key('MaxSpeed'):
                pMaxSpeed = pCustomization['MaxSpeed']
                pMaxSpeed = pMaxSpeed + 0.0
                if pMaxSpeed > 10.0:
                    pMaxSpeed = 10.0

            # It doesn't exist!
            else:
 		pMaxSpeed = 10.0

 	# No customizations of any kind...
	else:
		pMaxSpeed = 10.0

        pSelectedSpeed = pMaxSpeed
        fMaxSpeed = pMaxSpeed / 10.0
        pSelectedSpeed = float(str(pSelectedSpeed)[0:3+1])
        strSpeed = float(str(pMaxSpeed)[0:3+1])
        fMaxSpeed = float(str(fMaxSpeed)[0:3+1])

	pSelectedSpeedText = App.TGParagraph_CreateW(App.TGString("Selected Speed: " + str(pSelectedSpeed)), pDetailsWindow.GetMaximumInteriorWidth(), None, '', pDetailsWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pDetailsWindow.AddChild(pSelectedSpeedText, 0, 0.01)

        pMaxSpeedText = App.TGParagraph_CreateW(App.TGString("Max Speed: " + str(strSpeed)), pDetailsWindow.GetMaximumInteriorWidth(), None, '', pDetailsWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pDetailsWindow.AddChild(pMaxSpeedText, 0, 0.04)

        # We need to calculate the ETA & the engine stats
        pETA = ReturnETA(pSelectedSpeed)
        pIdealETA = ReturnIdealETA(pSelectedSpeed)
                    
        pETAText = App.TGParagraph_CreateW(App.TGString("ETA: " + pETA + " seconds"), pDetailsWindow.GetMaximumInteriorWidth(), None, '', pDetailsWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pDetailsWindow.AddChild(pETAText, 0, 0.07)

        pIdealETAText = App.TGParagraph_CreateW(App.TGString("Ideal ETA: " + pIdealETA + " seconds"), pDetailsWindow.GetMaximumInteriorWidth(), None, '', pDetailsWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pDetailsWindow.AddChild(pIdealETAText, 0, 0.10)

        pTotalEngineStats = ReturnEngineStats()

        pTotalEngineStatsText = App.TGParagraph_CreateW(App.TGString("Engine Status: " + pTotalEngineStats + "%"), pDetailsWindow.GetMaximumInteriorWidth(), None, '', pDetailsWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pDetailsWindow.AddChild(pTotalEngineStatsText, 0, 0.13)

        pEvent = App.TGStringEvent_Create()
        pEvent.SetEventType(ET_REFRESH)
        pEvent.SetString("SovRefresh")
        pButton = App.STRoundedButton_CreateW(App.TGString("Refresh Details"), pEvent, 0.13125, 0.034583)
        NormalColor = App.TGColorA() 
	NormalColor.SetRGBA(0.8, 0.6, 0.8, 1.0)
	HilightedColor = App.TGColorA() 
	HilightedColor.SetRGBA(0.92, 0.76, 0.92, 1.0)
	DisabledColor = App.TGColorA() 
	DisabledColor.SetRGBA(0.25, 0.25, 0.25, 1.0)
	pButton.SetNormalColor(NormalColor)
        pButton.SetHighlightedColor(HilightedColor)
        pButton.SetSelectedColor(NormalColor)
        pButton.SetDisabledColor(DisabledColor)
        pButton.SetColorBasedOnFlags()
        pFunctionsWindow.AddChild(pButton, 0.02, 0.03)

        pEvent = App.TGStringEvent_Create()
        pEvent.SetEventType(ET_CLOSE)
        pEvent.SetString("SovClose")
        pButton = App.STRoundedButton_CreateW(App.TGString("Close"), pEvent, 0.13125, 0.034583)
        NormalColor = App.TGColorA() 
	NormalColor.SetRGBA(0.8, 0.6, 0.8, 1.0)
	HilightedColor = App.TGColorA() 
	HilightedColor.SetRGBA(0.92, 0.76, 0.92, 1.0)
	DisabledColor = App.TGColorA() 
	DisabledColor.SetRGBA(0.25, 0.25, 0.25, 1.0)
	pButton.SetNormalColor(NormalColor)
        pButton.SetHighlightedColor(HilightedColor)
        pButton.SetSelectedColor(NormalColor)
        pButton.SetDisabledColor(DisabledColor)
        pButton.SetColorBasedOnFlags()
        pFunctionsWindow.AddChild(pButton, 0.02, 0.09)

        pSlider = CreateSlidebar(App.TGString("Speed Bar"), ET_UPDATE_SLIDER, fMaxSpeed)
        pSlider.Resize(0.16, 0.04, 0)
        pSliderWindow.AddChild(pSlider, 0.01, 0.06, 0)

        pEvent = App.TGStringEvent_Create()
        pEvent.SetEventType(ET_ENGAGE)
        pEvent.SetString("SovEngage")
        pButton = App.STRoundedButton_CreateW(App.TGString("Engage"), pEvent, 0.15, 0.06)
        NormalColor = App.TGColorA() 
	NormalColor.SetRGBA(0.8, 0.6, 0.8, 1.0)
	HilightedColor = App.TGColorA() 
	HilightedColor.SetRGBA(0.92, 0.76, 0.92, 1.0)
	DisabledColor = App.TGColorA() 
	DisabledColor.SetRGBA(0.25, 0.25, 0.25, 1.0)
	pButton.SetNormalColor(NormalColor)
        pButton.SetHighlightedColor(HilightedColor)
        pButton.SetSelectedColor(NormalColor)
        pButton.SetDisabledColor(DisabledColor)
        pButton.SetColorBasedOnFlags()
        pOptionsWindow.AddChild(pButton, 0.02, 0.05)


        # Glass background for pMainPane
	pGraphicsMode = App.GraphicsModeInfo_GetCurrentMode() 
	pLCARS = pGraphicsMode.GetLcarsString() 
	pGlass = App.TGIcon_Create(pLCARS, 120) 
	pGlass.Resize(pMainPane.GetWidth(), pMainPane.GetHeight()) 
	pMainPane.AddChild(pGlass, 0, 0)

	pDetailsWindow.InteriorChangedSize()
        pDetailsWindow.Layout()
        pFunctionsWindow.InteriorChangedSize()
        pFunctionsWindow.Layout()
        pSliderWindow.InteriorChangedSize()
        pSliderWindow.Layout()
        pOptionsWindow.InteriorChangedSize()
        pOptionsWindow.Layout()
        pMainPane.Layout()
        pPane.Layout()

        # Now show the pane
        pPane.SetVisible()


# Update stats
def UpdateStats(pObject, pEvent):
        global pMainPane, pPane, pTotalEngineStatsText, pETAText, pIdealETAText, pDetailsWindow, pFunctionsWindow, pSliderWindow, pOptionsWindow

        pETA = ReturnETA(pSelectedSpeed)
        pIdealETA = ReturnIdealETA(pSelectedSpeed)
        pTotalEngineStats = ReturnEngineStats()

        pETAText.SetString("ETA: " + pETA + " seconds")
        pIdealETAText.SetString("Ideal ETA: " + pIdealETA + " seconds")
        pTotalEngineStatsText.SetString("Engine Status: " + pTotalEngineStats + "%")

        pDetailsWindow.InteriorChangedSize()
        pDetailsWindow.Layout()
        pFunctionsWindow.InteriorChangedSize()
        pFunctionsWindow.Layout()
        pSliderWindow.InteriorChangedSize()
        pSliderWindow.Layout()
        pOptionsWindow.InteriorChangedSize()
        pOptionsWindow.Layout()
        pMainPane.Layout()
        pPane.Layout()

        pObject.CallNextHandler(pEvent)


# Update sliderbar
def UpdateSlider(pObject, pEvent):
        global pMainPane, pPane, pSelectedSpeed, pTotalEngineStatsText, pETAText, pIdealETAText, pSelectedSpeedText, pSlider, pDetailsWindow, pFunctionsWindow, pSliderWindow, pOptionsWindow

        try:
            fValue = pEvent.GetFloat()

        except AttributeError:
            return

        if fValue < 0.01:
            fValue = 0.01
        
        fSpeed = fValue * 10.0

        fSpeed = float(str(fSpeed)[0:3+1])

        pSelectedSpeed = fSpeed

        pETA = ReturnETA(pSelectedSpeed)
        pIdealETA = ReturnIdealETA(pSelectedSpeed)
        pTotalEngineStats = ReturnEngineStats()

        pSelectedSpeedText.SetString("Selected Speed: " + str(pSelectedSpeed))
        pETAText.SetString("ETA: " + pETA + " seconds")
        pIdealETAText.SetString("Ideal ETA: " + pIdealETA + " seconds")
        pTotalEngineStatsText.SetString("Engine Status: " + pTotalEngineStats + "%")

        pSlider.Resize(0.16, 0.04, 0)
        pSlider.SetValue(fValue)

        pDetailsWindow.InteriorChangedSize()
        pDetailsWindow.Layout()
        pFunctionsWindow.InteriorChangedSize()
        pFunctionsWindow.Layout()
        pSliderWindow.InteriorChangedSize()
        pSliderWindow.Layout()
        pOptionsWindow.InteriorChangedSize()
        pOptionsWindow.Layout()
        pMainPane.Layout()
        pPane.Layout()

        pObject.CallNextHandler(pEvent)
    

# Close GUI
def CloseGUI(pObject, pEvent):
        global pMainPane, pPane

        # A bugfix
        try:
                pGame = App.Game_GetCurrentGame()
                pEpisode = pGame.GetCurrentEpisode()
                pMission = pEpisode.GetCurrentMission()

                App.g_kEventManager.RemoveBroadcastHandler(ET_ENGAGE, pMission, __name__ + ".JumpspaceStats")
                App.g_kEventManager.RemoveBroadcastHandler(ET_UPDATE_SLIDER, pMission, __name__ + ".UpdateSlider")
                App.g_kEventManager.RemoveBroadcastHandler(ET_REFRESH, pMission, __name__ + ".UpdateStats")
                App.g_kEventManager.RemoveBroadcastHandler(ET_CLOSE, pMission, __name__ + ".CloseGUI")
	   
        except:
                pass

        # Bugfix for game crash
        if not pPane is None:
            pTCW = App.TacticalControlWindow_GetTacticalControlWindow()

            # Just destroy the window, we don't need it anymore.
            App.g_kFocusManager.RemoveAllObjectsUnder(pPane)

            pTCW.DeleteChild(pPane)

            pPane = None
            
            pMainPane = None
        

# Calculates and returns the ETA
def ReturnETA(pSelectedSpeed):
        global lStatsETA, pTimerETA

        # Reset vars
        lStatsETA = []
        pTimerETA = None
        
        # Grab values
        pPlayer = MissionLib.GetPlayer()
        pIterator = pPlayer.StartGetSubsystemMatch(App.CT_HULL_SUBSYSTEM)
	pSystem = pPlayer.GetNextSubsystemMatch(pIterator)

	# Add the stats of each engine into the list
        while (pSystem != None):
		if pSystem.GetName() in sJumpspaceList:
                   pStats = pSystem.GetConditionPercentage() * 100.0
                   pDisabled = pSystem.GetDisabledPercentage() * 100.0
                   if pStats <= pDisabled:
                       # Engine is disabled, treat it like it's destroyed
                       pStats = 0.0
                       
                   lStatsETA.append(pStats)
                   
		pSystem = pPlayer.GetNextSubsystemMatch(pIterator)

        pPlayer.EndGetSubsystemMatch(pIterator)

        file = nt.open(sPathETA, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
        nt.write(file, "# Do not Edit this file, Jumpspace uses it to store data\n")
        i = 0
        # Write stats into the file
        for stat in lStatsETA:
            i = i + 1
            nt.write(file, "\nJumpspaceDrive" + str(i) + " = " + str(stat))

        # We need to write all 20 lines into that file
        nTotal = i
        nCount = 20
        loop = 1
        while loop == 1:
            i = i + 1
            nt.write(file, "\nJumpspaceDrive" + str(i) + " = " + "0.0")
            # Kill the loop
            if i >= nCount:
                loop = 0

        # Close file
        nt.close(file)

        # Reload EngineStats to get the latest engine status
        reload(EngineStatsETA)

        iTotal = EngineStatsETA.JumpspaceDrive1 + EngineStatsETA.JumpspaceDrive2 + EngineStatsETA.JumpspaceDrive3 + EngineStatsETA.JumpspaceDrive4 + EngineStatsETA.JumpspaceDrive5 + EngineStatsETA.JumpspaceDrive6 + EngineStatsETA.JumpspaceDrive7 + EngineStatsETA.JumpspaceDrive8 + EngineStatsETA.JumpspaceDrive9  + EngineStatsETA.JumpspaceDrive10 + EngineStatsETA.JumpspaceDrive11 + EngineStatsETA.JumpspaceDrive12 + EngineStatsETA.JumpspaceDrive13 + EngineStatsETA.JumpspaceDrive14 + EngineStatsETA.JumpspaceDrive15 + EngineStatsETA.JumpspaceDrive16 + EngineStatsETA.JumpspaceDrive17 + EngineStatsETA.JumpspaceDrive18 + EngineStatsETA.JumpspaceDrive19 + EngineStatsETA.JumpspaceDrive20 

        pTotal = iTotal / nTotal

        # Can't jump if the engines are below 1%, return Engines Disabled ETA
        if pTotal < 1.0:
            return ' '

        # Damn, all of this to get that... It's finally done!!!
        pTimerETA = 100000.0 / pTotal
        
        pTimerETA = pTimerETA / pSelectedSpeed

        pTimerETA = float(str(pTimerETA)[0:3+1])

        pTimerETA = str(pTimerETA)

        return pTimerETA


# Returns ideal ETA
def ReturnIdealETA(pSelectedSpeed):
        global lStatsIdealETA, pTimerIdealETA

        # Reset vars
        lStatsIdealETA = []
        pTimerIdealETA = None
        
        # Grab values
        pPlayer = MissionLib.GetPlayer()
        pIterator = pPlayer.StartGetSubsystemMatch(App.CT_HULL_SUBSYSTEM)
	pSystem = pPlayer.GetNextSubsystemMatch(pIterator)

	# Add the stats of each engine into the list
        while (pSystem != None):
		if pSystem.GetName() in sJumpspaceList:
                   pStats = 100.0
                       
                   lStatsIdealETA.append(pStats)
                   
		pSystem = pPlayer.GetNextSubsystemMatch(pIterator)

        pPlayer.EndGetSubsystemMatch(pIterator)

        file = nt.open(sPathIdealETA, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
        nt.write(file, "# Do not Edit this file, Jumpspace uses it to store data\n")
        i = 0
        # Write stats into the file
        for stat in lStatsIdealETA:
            i = i + 1
            nt.write(file, "\nJumpspaceDrive" + str(i) + " = " + str(stat))

        # We need to write all 20 lines into that file
        nTotal = i
        nCount = 20
        loop = 1
        while loop == 1:
            i = i + 1
            nt.write(file, "\nJumpspaceDrive" + str(i) + " = " + "0.0")
            # Kill the loop
            if i >= nCount:
                loop = 0

        # Close file
        nt.close(file)

        # Reload EngineStats to get the latest engine status
        reload(EngineStatsIdealETA)

        iTotal = EngineStatsIdealETA.JumpspaceDrive1 + EngineStatsIdealETA.JumpspaceDrive2 + EngineStatsIdealETA.JumpspaceDrive3 + EngineStatsIdealETA.JumpspaceDrive4 + EngineStatsIdealETA.JumpspaceDrive5 + EngineStatsIdealETA.JumpspaceDrive6 + EngineStatsIdealETA.JumpspaceDrive7 + EngineStatsIdealETA.JumpspaceDrive8 + EngineStatsIdealETA.JumpspaceDrive9  + EngineStatsIdealETA.JumpspaceDrive10 + EngineStatsIdealETA.JumpspaceDrive11 + EngineStatsIdealETA.JumpspaceDrive12 + EngineStatsIdealETA.JumpspaceDrive13 + EngineStatsIdealETA.JumpspaceDrive14 + EngineStatsIdealETA.JumpspaceDrive15 + EngineStatsIdealETA.JumpspaceDrive16 + EngineStatsIdealETA.JumpspaceDrive17 + EngineStatsIdealETA.JumpspaceDrive18 + EngineStatsIdealETA.JumpspaceDrive19 + EngineStatsIdealETA.JumpspaceDrive20 

        pTotal = iTotal / nTotal

        # Damn, all of this to get that... It's finally done!!!
        pTimerIdealETA = 100000.0 / pTotal
        
        pTimerIdealETA = pTimerIdealETA / pSelectedSpeed

        pTimerIdealETA = float(str(pTimerIdealETA)[0:3+1])

        pTimerIdealETA = str(pTimerIdealETA)

        return pTimerIdealETA


# Return Engine Stats (Too many calculations need to be done)
def ReturnEngineStats():
        global lStatsEngines, pTimerEngineStats

        # Reset vars
        lStatsEngines = []
        pTimerEngineStats = None
        
        # Grab values
        pPlayer = MissionLib.GetPlayer()
        pIterator = pPlayer.StartGetSubsystemMatch(App.CT_HULL_SUBSYSTEM)
	pSystem = pPlayer.GetNextSubsystemMatch(pIterator)

	# Add the stats of each engine into the list
        while (pSystem != None):
		if pSystem.GetName() in sJumpspaceList:
                   pStats = pSystem.GetConditionPercentage() * 100.0
                   pDisabled = pSystem.GetDisabledPercentage() * 100.0
                   if pStats <= pDisabled:
                       # Engine is disabled, treat it like it's destroyed
                       pStats = 0.0
                       
                   lStatsEngines.append(pStats)
                   
		pSystem = pPlayer.GetNextSubsystemMatch(pIterator)

        pPlayer.EndGetSubsystemMatch(pIterator)

        file = nt.open(sPathStats, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
        nt.write(file, "# Do not Edit this file, Jumpspace uses it to store data\n")
        i = 0
        # Write stats into the file
        for stat in lStatsEngines:
            i = i + 1
            nt.write(file, "\nJumpspaceDrive" + str(i) + " = " + str(stat))

        # We need to write all 20 lines into that file
        nTotal = i
        nCount = 20
        loop = 1
        while loop == 1:
            i = i + 1
            nt.write(file, "\nJumpspaceDrive" + str(i) + " = " + "0.0")
            # Kill the loop
            if i >= nCount:
                loop = 0

        # Close file
        nt.close(file)

        # Reload EngineStats to get the latest engine status
        reload(EngineStatsMenuCalc)

        iTotal = EngineStatsMenuCalc.JumpspaceDrive1 + EngineStatsMenuCalc.JumpspaceDrive2 + EngineStatsMenuCalc.JumpspaceDrive3 + EngineStatsMenuCalc.JumpspaceDrive4 + EngineStatsMenuCalc.JumpspaceDrive5 + EngineStatsMenuCalc.JumpspaceDrive6 + EngineStatsMenuCalc.JumpspaceDrive7 + EngineStatsMenuCalc.JumpspaceDrive8 + EngineStatsMenuCalc.JumpspaceDrive9  + EngineStatsMenuCalc.JumpspaceDrive10 + EngineStatsMenuCalc.JumpspaceDrive11 + EngineStatsMenuCalc.JumpspaceDrive12 + EngineStatsMenuCalc.JumpspaceDrive13 + EngineStatsMenuCalc.JumpspaceDrive14 + EngineStatsMenuCalc.JumpspaceDrive15 + EngineStatsMenuCalc.JumpspaceDrive16 + EngineStatsMenuCalc.JumpspaceDrive17 + EngineStatsMenuCalc.JumpspaceDrive18 + EngineStatsMenuCalc.JumpspaceDrive19 + EngineStatsMenuCalc.JumpspaceDrive20 

        pTotal = iTotal / nTotal

        pTotal = str(pTotal)

        return pTotal

        
# Calculate the stats of the drive engines and the time it'll take us to get to the destination
def JumpspaceStats(pObject, pEvent):
        global lStats, pTimer, pSelectedSpeed

        # Reset vars
        lStats = []
        pTimer = None
        
        # Grab values
        pPlayer = MissionLib.GetPlayer()
        pIterator = pPlayer.StartGetSubsystemMatch(App.CT_HULL_SUBSYSTEM)
	pSystem = pPlayer.GetNextSubsystemMatch(pIterator)

	# Add the stats of each engine into the list
        while (pSystem != None):
		if pSystem.GetName() in sJumpspaceList:
                   pStats = pSystem.GetConditionPercentage() * 100.0
                   pDisabled = pSystem.GetDisabledPercentage() * 100.0
                   if pStats <= pDisabled:
                       # Engine is disabled, treat it like it's destroyed
                       pStats = 0.0
                       
                   lStats.append(pStats)
                   
		pSystem = pPlayer.GetNextSubsystemMatch(pIterator)

        pPlayer.EndGetSubsystemMatch(pIterator)

        file = nt.open(sPath, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
        nt.write(file, "# Do not Edit this file, Jumpspace uses it to store data\n")
        i = 0
        # Write stats into the file
        for stat in lStats:
            i = i + 1
            nt.write(file, "\nJumpspaceDrive" + str(i) + " = " + str(stat))

        # We need to write all 20 lines into that file
        nTotal = i
        nCount = 20
        loop = 1
        while loop == 1:
            i = i + 1
            nt.write(file, "\nJumpspaceDrive" + str(i) + " = " + "0.0")
            # Kill the loop
            if i >= nCount:
                loop = 0

        # Close file
        nt.close(file)

        # Reload EngineStats to get the latest engine status
        reload(EngineStats)

        iTotal = EngineStats.JumpspaceDrive1 + EngineStats.JumpspaceDrive2 + EngineStats.JumpspaceDrive3 + EngineStats.JumpspaceDrive4 + EngineStats.JumpspaceDrive5 + EngineStats.JumpspaceDrive6 + EngineStats.JumpspaceDrive7 + EngineStats.JumpspaceDrive8 + EngineStats.JumpspaceDrive9  + EngineStats.JumpspaceDrive10 + EngineStats.JumpspaceDrive11 + EngineStats.JumpspaceDrive12 + EngineStats.JumpspaceDrive13 + EngineStats.JumpspaceDrive14 + EngineStats.JumpspaceDrive15 + EngineStats.JumpspaceDrive16 + EngineStats.JumpspaceDrive17 + EngineStats.JumpspaceDrive18 + EngineStats.JumpspaceDrive19 + EngineStats.JumpspaceDrive20 

        pTotal = iTotal / nTotal

        # Can't jump if the engines are below 1%
        if pTotal < 1.0:
            print 'Jumpspace: Jumpspace Engines are badly damaged, cannot initiate the jump'
            return

        # Damn, all of this to get that... It's finally done!!!
        pTimer = 100000.0 / pTotal
        
        pTimer = pTimer / pSelectedSpeed

        pTimer = float(str(pTimer)[0:3+1])

        # All OK, Kill the GUI
        CloseGUI(None, None)

        DS9FXMusicBugfix()
        
        PreEngage(None, None)


# When entering DS9FX Set the music is not terminated so fix it
def DS9FXMusicBugfix():
        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet().GetName()

        if pSet == 'DeepSpace91':
            # Stop Overriding music
            import DynamicMusic
            DynamicMusic.StopOverridingMusic()

                        
# Check if the ship is actually equiped with jumpspace drive
def HasJumpspace(pShip):        
        # Grab values
        pIterator = pShip.StartGetSubsystemMatch(App.CT_HULL_SUBSYSTEM)
	pSystem = pShip.GetNextSubsystemMatch(pIterator)

	# No ship has 20 engines! Right?!
        while (pSystem != None):
		if pSystem.GetName() in sJumpspaceList:
                    pStats = pSystem.GetConditionPercentage() * 100.0
                    if pStats >= 1.1:
                        # What's this? Jumpspace is installed!
                        return 'Jumpspace Installed'
                        break
		pSystem = pShip.GetNextSubsystemMatch(pIterator)

        pShip.EndGetSubsystemMatch(pIterator)


# Jumpspace sequence initiated
def PreEngage(pObject, pEvent):
        # Grab values and start the prescripted sequence
        pPlayer = App.Game_GetCurrentPlayer()    
        pSequence = App.TGSequence_Create ()
        pSequence.AddAction(App.TGScriptAction_Create("MissionLib", "StartCutscene"))
        pSequence.AddAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
        pSequence.AddAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))
        pSequence.AddAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", pPlayer.GetContainingSet().GetName(), pPlayer.GetName ()))
        pSequence.AddAction(App.TGScriptAction_Create(__name__, "PositionPlayerOldSet"))
        pSequence.Play()


# Redirect function
def PositionPlayerOldSet(pAction):
        # Initiate search AI
        InitiateSearchAI()

        # Start the supplimentary function
        AdditionalPosAndCheck(None, None)

        return 0
        

# Do the additional sweep to aid the 360 degree spin
def AdditionalPosAndCheck(pObject, pEvent):
        global pDefault
    
        # Positioning function
        AimForGoodPos.GoodAim()

        # Check aim
        sAim = AimForGoodPos.CheckGoodAim()
        
        # Good Aim
        if sAim == 'TRUE':               
                # Who the hell knows, something still might go wrong. Better be safe then sorry!
                pGame = App.Game_GetCurrentGame()
                pGame.SetGodMode(1)
                # Collision settings
                pDefault = App.ProximityManager_GetPlayerCollisionsEnabled()
                App.ProximityManager_SetPlayerCollisionsEnabled(0)

                # Grab player and set 
                pPlayer = MissionLib.GetPlayer()
                pSet = pPlayer.GetContainingSet()

                # Create & allign cam placement
                pCamPlacement = App.PlacementObject_Create(pPlayer.GetName() + str(pSet.GetName()) + str(App.g_kUtopiaModule.GetGameTime()), pPlayer.GetContainingSet().GetName (), None)
                pPlayerLoc = pPlayer.GetWorldLocation()
                pPlayerX = pPlayerLoc.GetX()
                cordX = pPlayerX + pPlayer.GetWorldBackwardTG().GetX() + 1
                pPlayerY = pPlayerLoc.GetY()
                cordY = pPlayerY + pPlayer.GetWorldBackwardTG().GetY()
                pPlayerZ = pPlayerLoc.GetZ()
                cordZ = pPlayerZ + pPlayer.GetWorldBackwardTG().GetZ() + 1
                pPlayerBackward = pPlayer.GetWorldBackwardTG()
                pPlayerDown = pPlayer.GetWorldUpTG()
                pCamPlacement.SetTranslateXYZ(cordX, cordY, cordZ)
                pCamPlacement.AlignToVectors(pPlayerBackward, pPlayerDown)
                pCamPlacement.UpdateNodeOnly()
                
                pSequence = App.TGSequence_Create()
                pAction = App.TGScriptAction_Create("MissionLib", "StartCutscene")
                pSequence.AddAction(pAction, None, 0) 
                pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0)
                pSequence.AddAction(pAction, None, 0) 
                pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ())
                pSequence.AddAction(pAction, None, 0)
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "TargetWatch", pPlayer.GetContainingSet().GetName (), pCamPlacement.GetName(), pPlayer.GetName(), 0))
                pAction = App.TGScriptAction_Create(__name__, "MoveForwardAI")
                pSequence.AddAction(pAction, None, 1.5)
                pAction = App.TGScriptAction_Create(__name__, "EnteringFlash")
                pSequence.AddAction(pAction, None, 1.5)
                pAction = App.TGScriptAction_Create(__name__, "MaxSpeed")
                pSequence.AddAction(pAction, None, 1.5)
                pAction = App.TGScriptAction_Create(__name__, "JumpspaceFlash")
                pSequence.AddAction(pAction, None, 2.5)
                pAction = App.TGScriptAction_Create(__name__, "HidePlayer")
                pSequence.AddAction(pAction, None, 4.5)
                pAction = App.TGScriptAction_Create(__name__, "RestoreSpeedValues")
                pSequence.AddAction(pAction, None, 5.5)
                pAction = App.TGScriptAction_Create(__name__, "SwapSets")
                pSequence.AddAction(pAction, None, 5.5)
                pAction = App.TGScriptAction_Create(__name__, "UnhidePlayer")
                pSequence.AddAction(pAction, None, 6)
                pAction = App.TGScriptAction_Create(__name__, "DisableHelmMenu")
                pSequence.AddAction(pAction, None, 6.5)
                pAction = App.TGScriptAction_Create(__name__, "ClearAIs")
                pSequence.AddAction(pAction, None, 6.5)
                pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pPlayer.GetContainingSet().GetName())
                pSequence.AddAction(pAction, None, 7)
                pAction = App.TGScriptAction_Create("MissionLib", "EndCutscene")
                pSequence.AddAction(pAction, None, 7)
                pAction = App.TGScriptAction_Create(__name__, "BackToNormal")
                pSequence.AppendAction(pAction)
                
                pSequence.Play()

        # Bad Aim, repeat process
        else:     
                MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".AdditionalPosAndCheck", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)
                

# Exiting sequence
def CutsceneExit(pObject, pEvent):
        # Adjust Aim
        AimForGoodPosExit.GoodAim()
    
        # Start the cutscene
        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()

        # Create exit placement position for camera to see the flash
        pCamPlacement = App.PlacementObject_Create(pPlayer.GetName() + str(pSet.GetName()) + str(App.g_kUtopiaModule.GetGameTime()), pPlayer.GetContainingSet().GetName (), None)
        pPlayerLoc = pPlayer.GetWorldLocation()
        pPlayerX = pPlayerLoc.GetX()
        cordX = pPlayerX + pPlayer.GetWorldBackwardTG().GetX() + 1
        pPlayerY = pPlayerLoc.GetY()
        cordY = pPlayerY + pPlayer.GetWorldBackwardTG().GetY()
        pPlayerZ = pPlayerLoc.GetZ()
        cordZ = pPlayerZ + pPlayer.GetWorldBackwardTG().GetZ() + 1
        pPlayerBackward = pPlayer.GetWorldBackwardTG()
        pPlayerDown = pPlayer.GetWorldUpTG()
        pCamPlacement.SetTranslateXYZ(cordX, cordY, cordZ)
        pCamPlacement.AlignToVectors(pPlayerBackward, pPlayerDown)
        pCamPlacement.UpdateNodeOnly()

        # Initiate scripted sequences
        pSequence = App.TGSequence_Create ()
        pAction = App.TGScriptAction_Create(__name__, "HidePlayer")
        pSequence.AddAction(pAction, None, 0)
        pAction = App.TGScriptAction_Create("MissionLib", "StartCutscene")
        pSequence.AddAction(pAction, None, 0.5) 
        pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0)
        pSequence.AddAction(pAction, None, 0.5) 
        pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ())
        pSequence.AddAction(pAction, None, 0.5) 
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "TargetWatch", pPlayer.GetContainingSet().GetName (), pCamPlacement.GetName(), pPlayer.GetName(), 0))
        # A bug, sometimes the game doesn't make the new set rendered and we miss the exit sequence
        if App.g_kSetManager.GetSet(pSet.GetName()):
            pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", pSet.GetName())
            pSequence.AddAction(pAction, None, 0.5)       
        pAction = App.TGScriptAction_Create(__name__, "JumpspaceFlashExit")
        pSequence.AddAction(pAction, None, 1)
        pAction = App.TGScriptAction_Create(__name__, "MoveForwardAI")
        pSequence.AddAction(pAction, None, 1)
        pAction = App.TGScriptAction_Create(__name__, "ExitingFlash")
        pSequence.AddAction(pAction, None, 2)
        pAction = App.TGScriptAction_Create(__name__, "MaxSpeedExit")
        pSequence.AddAction(pAction, None, 2.5)
        pAction = App.TGScriptAction_Create(__name__, "UnhidePlayer")
        pSequence.AddAction(pAction, None, 2.5)
        pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", pPlayer.GetContainingSet().GetName(), pPlayer.GetName ())
        pSequence.AddAction(pAction, None, 4)
        pAction = App.TGScriptAction_Create(__name__, "RestoreSpeedValues")
        pSequence.AddAction(pAction, None, 5)
        pAction = App.TGScriptAction_Create(__name__, "ClearCourseSetting")
        pSequence.AddAction(pAction, None, 5)
        pAction = App.TGScriptAction_Create(__name__, "EnableHelmMenu")
        pSequence.AddAction(pAction, None, 5)         
        pAction = App.TGScriptAction_Create(__name__, "StopShip")
        pSequence.AddAction(pAction, None, 5)
        pAction = App.TGScriptAction_Create(__name__, "TransferPlayer")
        pSequence.AddAction(pAction, None, 5)
        pAction = App.TGScriptAction_Create(__name__, "ClearAIs")
        pSequence.AddAction(pAction, None, 5)
        pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pPlayer.GetContainingSet().GetName ())
        pSequence.AddAction(pAction, None, 5)
        if App.g_kSetManager.GetSet("bridge"):
                pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "bridge")
                pSequence.AddAction(pAction, None, 5)
        pAction = App.TGScriptAction_Create("MissionLib", "EndCutscene")
        pSequence.AddAction(pAction, None, 5)
        pAction = App.TGScriptAction_Create(__name__, "GameCrashFix")
        pSequence.AddAction(pAction, None, 6)
        pAction = App.TGScriptAction_Create(__name__, "BackToNormal")
        pSequence.AppendAction(pAction)
            
        pSequence.Play()


# Entering sound
def EnteringFlash(pAction):
        # Check for custom sounds
        pPlayer = MissionLib.GetPlayer()
        pModule = __import__(pPlayer.GetScript())

        # Is there a customization for this ship available?
        if hasattr(pModule, "JumpspaceCustomizations"):
            pCustomization = pModule.JumpspaceCustomizations()
            
            # Customization exists, but does the sound entry exist?!
            if pCustomization.has_key('EntrySound'):
                pSound = "scripts/Custom/Jumpspace/SFX/" + pCustomization['EntrySound']

                pEnterSound = App.TGSound_Create(pSound, "Enter", 0)
                pEnterSound.SetSFX(0) 
                pEnterSound.SetInterface(1)

            # No sound entry found
            else:
                pEnterSound = App.TGSound_Create("scripts/Custom/Jumpspace/SFX/enterjumpspace.wav", "Enter", 0)
                pEnterSound.SetSFX(0) 
                pEnterSound.SetInterface(1)

        # No customizations of any kind available for this ship.
        else:
            pEnterSound = App.TGSound_Create("scripts/Custom/Jumpspace/SFX/enterjumpspace.wav", "Enter", 0)
            pEnterSound.SetSFX(0) 
            pEnterSound.SetInterface(1)

        App.g_kSoundManager.PlaySound("Enter")

        return 0


# Exiting sound
def ExitingFlash(pAction):
        # Check for custom sounds
        pPlayer = MissionLib.GetPlayer()
        pModule = __import__(pPlayer.GetScript())

        # Is there a customization for this ship available?
        if hasattr(pModule, "JumpspaceCustomizations"):
            pCustomization = pModule.JumpspaceCustomizations()
            
            # Customization exists, but does the sound entry exist?!
            if pCustomization.has_key('ExitSound'):
                pSound = "scripts/Custom/Jumpspace/SFX/" + pCustomization['ExitSound']

            	pExitSound = App.TGSound_Create(pSound, "Exit", 0)
            	pExitSound.SetSFX(0) 
            	pExitSound.SetInterface(1)

            # No sound entry found
            else:
            	pExitSound = App.TGSound_Create("scripts/Custom/Jumpspace/SFX/exitjumpspace.wav", "Exit", 0)
            	pExitSound.SetSFX(0) 
            	pExitSound.SetInterface(1)

        # No customizations of any kind available for this ship.
        else:
            pExitSound = App.TGSound_Create("scripts/Custom/Jumpspace/SFX/exitjumpspace.wav", "Exit", 0)
            pExitSound.SetSFX(0) 
            pExitSound.SetInterface(1)

    
        App.g_kSoundManager.PlaySound("Exit")

        return 0

         
# Sets up a max speed
def MaxSpeed(pAction):
        global pSpeed, pAccel, pPowerSetting

        pPlayer = MissionLib.GetPlayer()
        pImpulseSys = pPlayer.GetImpulseEngineSubsystem()
        pImpulse = pPlayer.GetImpulseEngineSubsystem().GetProperty()
	pSpeed = pImpulse.GetMaxSpeed()
	pAccel = pImpulse.GetMaxAccel()
	pPowerSetting = pImpulseSys.GetPowerPercentageWanted()

	pImpulse.SetMaxSpeed(200)

	pImpulse.SetMaxAccel(50)

	pImpulseSys.SetPowerPercentageWanted(1.0)

	pNewSpeed = pPlayer.GetImpulseEngineSubsystem().GetProperty().GetMaxSpeed()

	pPlayer.SetSpeed(pNewSpeed, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

	return 0


# Sets up a max speed
def MaxSpeedExit(pAction):
        global pSpeed, pAccel, pPowerSetting

        pPlayer = MissionLib.GetPlayer()
        pImpulseSys = pPlayer.GetImpulseEngineSubsystem()
        pImpulse = pPlayer.GetImpulseEngineSubsystem().GetProperty()
	pSpeed = pImpulse.GetMaxSpeed()
	pAccel = pImpulse.GetMaxAccel()
	pPowerSetting = pImpulseSys.GetPowerPercentageWanted()

	pImpulse.SetMaxSpeed(50)

	pImpulse.SetMaxAccel(25)

	pImpulseSys.SetPowerPercentageWanted(1.0)

	pNewSpeed = pPlayer.GetImpulseEngineSubsystem().GetProperty().GetMaxSpeed()

	pPlayer.SetSpeed(pNewSpeed, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

	return 0


# Restores original speed values
def RestoreSpeedValues(pAction):
        global pSpeed, pAccel, pPowerSetting

        pPlayer = MissionLib.GetPlayer()
        pImpulseSys = pPlayer.GetImpulseEngineSubsystem()
        pImpulse = pPlayer.GetImpulseEngineSubsystem().GetProperty()

        pImpulse.SetMaxSpeed(pSpeed)

	pImpulse.SetMaxAccel(pAccel)

	pImpulseSys.SetPowerPercentageWanted(pPowerSetting)

	pPlayer.SetSpeed(pSpeed, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)
	
	pPlayer.SetVelocity(App.TGPoint3_GetModelForward())

	return 0


# Make the ship speed up
def SpeedUp(pAction):
        pPlayer = MissionLib.GetPlayer()
        pImpulse = pPlayer.GetImpulseEngineSubsystem().GetProperty()
        pSpeed = pImpulse.GetMaxSpeed()

        pPlayer.SetSpeed(pSpeed, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        return 0


# Stops a ship
def StopShip(pAction):
        pPlayer = MissionLib.GetPlayer()

        pPlayer.SetSpeed(0, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        return 0        


# Sets a DS9FX AI to move the ship forward
def MoveForwardAI(pAction):
        pPlayer = MissionLib.GetPlayer()
        import Custom.Jumpspace.Libs.DS9FXWormholeExitingSeqAI
        pPlayerCast = App.ShipClass_Cast(pPlayer)
        pPlayerCast.SetAI(Custom.Jumpspace.Libs.DS9FXWormholeExitingSeqAI.CreateAI(pPlayerCast))

        return 0


# 360 degree spin & search
def InitiateSearchAI():
        pPlayer = MissionLib.GetPlayer()
        import Custom.Jumpspace.Libs.JumpspaceSearchSafePosition
        pPlayerCast = App.ShipClass_Cast(pPlayer)
        pPlayerCast.SetAI(Custom.Jumpspace.Libs.JumpspaceSearchSafePosition.CreateAI(pPlayerCast))

        return 0


# Clears AI and stops the ship
def ClearAIs(pAction):        
        pPlayer = MissionLib.GetPlayer()        
        import Custom.Jumpspace.Libs.DS9FXStayAI
        pPlayerCast = App.ShipClass_Cast(pPlayer)
        pPlayerCast.SetAI(Custom.Jumpspace.Libs.DS9FXStayAI.CreateAI(pPlayerCast))

        # Clear AI's
        pPlayer.ClearAI()

        import AI.Player.Stay
	MissionLib.SetPlayerAI("Helm", AI.Player.Stay.CreateAI(pPlayer))

        return 0


# Restore settings back to normal
def BackToNormal(pAction):
	global pDefault, pWasCloaked

	# Restore things back to normal
        pGame = App.Game_GetCurrentGame()
        pGame.SetGodMode(0)
        # Collision settings
        App.ProximityManager_SetPlayerCollisionsEnabled(pDefault)

        pPlayer = MissionLib.GetPlayer()
        
        if pWasCloaked == 1:
            pCloak = pPlayer.GetCloakingSubsystem()
            if pCloak:
                pCloak.InstantCloak()

        return 0


# Swaps sets        
def SwapSets(pAction):
        Engage(None, None)

        return 0


# Hides player
def HidePlayer(pAction):
        pPlayer = MissionLib.GetPlayer()
        pPlayer.SetHidden(1)

        return 0


# Unhides player
def UnhidePlayer(pAction):
        pPlayer = MissionLib.GetPlayer()
        pPlayer.SetHidden(0)

        return 0


# Flash animation properties
def JumpspaceFlash(pAction):
            
        pPlayer = MissionLib.GetPlayer()
            
        # Load texture GFX
        LoadFlash.StartGFX()
        # Create flash
        LoadFlash.CreateGFX(pPlayer)

        return 0
def JumpspaceFlashExit(pAction):
        # print 'Jumpspace exit should be starting now...'    
        pPlayer = MissionLib.GetPlayer()
            
        # Load texture GFX
        LoadFlash.EndFlashGFX()
        # Create flash
        LoadFlash.B5CreateGFX(pPlayer)

        return 0

        
# Here we go baby!
def Engage(pObject, pEvent):
        global bButton, pDest, pDestName, pTimer, pWasCloaked

        # Resolve the dark screen problem after a new object is created in the jumpspace\hyperdrive set
        pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".FixDarkScreen")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_DESTROYED, pMission, __name__ + ".FixDarkScreenExplosions")

        # Clear players target first
        import TacticalInterfaceHandlers
	TacticalInterfaceHandlers.ClearTarget(None, None)

        # Disable the button
        bButton.SetDisabled()

        # Grab & initialize the dummy set
        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()
        pWasCloaked = 0

        if App.g_kSetManager.GetSet("JumpspaceTunnel1"):
            
                pDummySet = App.g_kSetManager.GetSet("JumpspaceTunnel1")

        else:
        
                pDummy = __import__("Systems.JumpspaceTunnel.JumpspaceTunnel1")
            
                pDummy.Initialize()

                pDummySet = pDummy.GetSet()

        pSys = __import__(pDest)

        pDestName = pSys.GetSetName()

        # Do the transfer
        for kShip in pSet.GetClassObjectList(App.CT_SHIP):
                # WTF, where did these asteroids come from... Time to filter them out
                fShip = App.ShipClass_GetObject(pSet, kShip.GetName())
                fScript = fShip.GetScript()
                if fScript in sAsteroidList:
                    # print 'Asteroid detected, skipping'
                    continue

                # Jumpspace ability?!
                JumpspaceInstalled = HasJumpspace(fShip)
                if not JumpspaceInstalled == 'Jumpspace Installed':
                    # For those we leave behind...
                    pWarp = fShip.GetWarpEngineSubsystem()
                    if pWarp:
                        DisableWarp(fShip, pWarp)
                    continue
                
		pSet.RemoveObjectFromSet(kShip.GetName())
		if kShip.GetName() == pPlayer.GetName():
                    if pPlayer.IsCloaked():
                        pWasCloaked = 1
                        pCloak = pPlayer.GetCloakingSubsystem()
                        if pCloak:
                            pCloak.InstantDecloak()
		pDummySet.AddObjectToSet(kShip, kShip.GetName())

                # Get location of the player
		pLocation = pPlayer.GetWorldLocation() 

                # New way to choose new location
                kShipX = pLocation.GetX()
                
                kShipY = pLocation.GetY()
                
                kShipZ = pLocation.GetZ()

                RateX = GetRandomRate(100, 25)

                RateY = GetRandomRate(100, 25)

                RateZ = GetRandomRate(100, 25)

                pXCoord = kShipX + RateX

                pYCoord = kShipY + RateY

                pZCoord = kShipZ + RateZ

                kShip.SetTranslateXYZ(pXCoord, pYCoord, pZCoord)

                kShip.UpdateNodeOnly() 


                # Update proximity manager info
                ProximityManager = pDummySet.GetProximityManager() 
                if (ProximityManager): 
                        ProximityManager.UpdateObject(kShip)
                        

        # Purge memory when transfering between sets
        App.g_kLODModelManager.Purge()

        scale = 1000

        # Create the tunnel
        TunnelString = "Jumpspace Outer"
        pTunnel = loadspacehelper.CreateShip("jumpspace", pDummySet, TunnelString, "Player Start")
       
        # Get the ship and rotate it like the Bajoran Wormhole in DS9Set
        fTunnel = MissionLib.GetShip(TunnelString, pDummySet) 
        vCurVelocity = App.TGPoint3()
        vCurVelocity.SetXYZ(0, 0.8, 0)
        fTunnel.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        # Invincible
        fTunnel.SetInvincible(1)
        fTunnel.SetHurtable(0)
        fTunnel.SetTargetable(0)

        # Very large ;)
        fTunnel.SetScale(scale)
        
        # Create the tunnel
        TunnelString2 = "Jumpspace Inner"
        pTunnel2 = loadspacehelper.CreateShip("jumpspace", pDummySet, TunnelString2, "Player Start")
       
        # Get the ship and rotate it like the Bajoran Wormhole in DS9Set
        fTunnel2 = MissionLib.GetShip(TunnelString2, pDummySet)
        # Disable collisions with the 2 models
        fTunnel2.EnableCollisionsWith(fTunnel, 0)
        vCurVelocity = App.TGPoint3()
        vCurVelocity.SetXYZ(0, 0.8, 0)
        fTunnel2.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        # Invincible
        fTunnel2.SetInvincible(1)
        fTunnel2.SetHurtable(0)
        fTunnel2.SetTargetable(0)

        # Very large ;)
        fTunnel2.SetScale(scale)

	# Custom tunnel textures?
        pModule = __import__(pPlayer.GetScript())

        # Is there a customization for this ship available?
        if hasattr(pModule, "JumpspaceCustomizations"):
            pCustomization = pModule.JumpspaceCustomizations()
            
            # Customization exists, but does the tunnel texture entry exist?!
            if pCustomization.has_key('TunnelTexture'):
                # Bingo, replace textures for both tunnels then
                GFX = "scripts/Custom/Jumpspace/GFX/" + pCustomization['TunnelTexture']

 		fTunnel.ReplaceTexture(GFX, "outer_glow")
		fTunnel2.ReplaceTexture(GFX, "outer_glow")

		fTunnel.RefreshReplacedTextures()
            	fTunnel2.RefreshReplacedTextures()

            # There's no gfx defined, use the user specified defaults
            else:
                reload(JumpspaceConfiguration)

                if JumpspaceConfiguration.TunnelGFX == 'Default':
                    pass
                else:
                    GFX = "scripts/Custom/Jumpspace/GFX/" + JumpspaceConfiguration.TunnelGFX

                    fTunnel.ReplaceTexture(GFX, "outer_glow")
                    fTunnel2.ReplaceTexture(GFX, "outer_glow")

                    fTunnel.RefreshReplacedTextures()
                    fTunnel2.RefreshReplacedTextures()

        # There no customization check for default presets
        else:
            reload(JumpspaceConfiguration)

            if JumpspaceConfiguration.TunnelGFX == 'Default':
                pass
            else:
                GFX = "scripts/Custom/Jumpspace/GFX/" + JumpspaceConfiguration.TunnelGFX

                fTunnel.ReplaceTexture(GFX, "outer_glow")
		fTunnel2.ReplaceTexture(GFX, "outer_glow")

		fTunnel.RefreshReplacedTextures()
            	fTunnel2.RefreshReplacedTextures()
            	
        # Disable player collision with the cone
        fTunnel.EnableCollisionsWith(pPlayer, 0)
        fTunnel2.EnableCollisionsWith(pPlayer, 0)

        # Disable any ship collisions with the cone
        for kShip in pDummySet.GetClassObjectList(App.CT_SHIP):
            pShip = App.ShipClass_GetObject(pDummySet, kShip.GetName())
            fTunnel.EnableCollisionsWith(pShip, 0)
            fTunnel2.EnableCollisionsWith(pShip, 0)

        fTunnel.SetCollisionsOn(0)
        fTunnel2.SetCollisionsOn(0)
        
        # Position the tunnel so that it appears you're inside it
        pPlayerBackward = pPlayer.GetWorldBackwardTG()
        pPlayerDown = pPlayer.GetWorldDownTG()
        pPlayerPosition = pPlayer.GetWorldLocation()

        fTunnel.AlignToVectors(pPlayerBackward, pPlayerDown)
        fTunnel.SetTranslate(pPlayerPosition)
        fTunnel.UpdateNodeOnly()

        fTunnel2.AlignToVectors(pPlayerBackward, pPlayerDown)
        fTunnel2.SetTranslate(pPlayerPosition)
        fTunnel2.UpdateNodeOnly()

        # Switch backdrop
        SwapBackdrops()

        # Interface fix
        App.InterfaceModule_DoTheRightThing()

        reload(JumpspaceConfiguration)

        if JumpspaceConfiguration.LoopSound == 1:
            # Play the loop sound
            App.g_kSoundManager.PlaySound("JumpspaceEngineSound")

        if JumpspaceConfiguration.Prints == 1:
            # Print the destination
            DestinationOutput(None, None)

        # Speed the ship up
        SpeedUp(None)
        
        # Timer to call in the next sequence
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".ExitingRedirect", App.g_kUtopiaModule.GetGameTime() + pTimer, 0, 0)


# Switch set backdrops over here
def SwapBackdrops():
        # Grab the player and the ship script
        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()
        pModule = __import__(pPlayer.GetScript())

        # Remove all backdrops from the set first
        for kBackdrop in pSet.GetClassObjectList(App.CT_BACKDROP):
            pSet.RemoveBackdropFromSet(kBackdrop)
            
        if hasattr(pModule, "JumpspaceCustomizations"):
            pCustomization = pModule.JumpspaceCustomizations()
                    
            # Customization exists but does the backdrop entry exist?
            if pCustomization.has_key('BackdropTexture'):
                # Ship is scripted to turn off the backdrop texture?
                if pCustomization['BackdropTexture'] == "Off":
                    pass
                else:
                    # Replace the default texture then
                    Backdrop = "scripts/Custom/Jumpspace/GFX/" + pCustomization['BackdropTexture']
                    kThis = App.StarSphere_Create()
                    kThis.SetName("Backdrop stars")
                    kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
                    kForward = App.TGPoint3()
                    kForward.SetXYZ(0.185766, 0.947862, -0.258937)
                    kUp = App.TGPoint3()
                    kUp.SetXYZ(0.049823, 0.254099, 0.965894)
                    kThis.AlignToVectors(kForward, kUp)
                    kThis.SetTextureFileName(Backdrop)
                    kThis.SetTargetPolyCount(256)
                    kThis.SetHorizontalSpan(1.000000)
                    kThis.SetVerticalSpan(1.000000)
                    kThis.SetSphereRadius(300.000000)
                    kThis.SetTextureHTile(22.000000)
                    kThis.SetTextureVTile(11.000000)
                    kThis.Rebuild()
                    pSet.AddBackdropToSet(kThis,"Backdrop stars")
                    kThis.Update(0)
                    kThis = None                                   

            # There's no gfx defined, use the user specified defaults
            else:
                reload(JumpspaceConfiguration)

                if JumpspaceConfiguration.BackdropGFX == 'Default':
                    kThis = App.StarSphere_Create()
                    kThis.SetName("Backdrop stars")
                    kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
                    kForward = App.TGPoint3()
                    kForward.SetXYZ(0.185766, 0.947862, -0.258937)
                    kUp = App.TGPoint3()
                    kUp.SetXYZ(0.049823, 0.254099, 0.965894)
                    kThis.AlignToVectors(kForward, kUp)
                    kThis.SetTextureFileName("data/jumpspaceback.tga")
                    kThis.SetTargetPolyCount(256)
                    kThis.SetHorizontalSpan(1.000000)
                    kThis.SetVerticalSpan(1.000000)
                    kThis.SetSphereRadius(300.000000)
                    kThis.SetTextureHTile(22.000000)
                    kThis.SetTextureVTile(11.000000)
                    kThis.Rebuild()
                    pSet.AddBackdropToSet(kThis,"Backdrop stars")
                    kThis.Update(0)
                    kThis = None
                elif JumpspaceConfiguration.BackdropGFX == 'Off':
                    pass
                else:
                    Backdrop = "scripts/Custom/Jumpspace/GFX/" + JumpspaceConfiguration.BackdropGFX
                    kThis = App.StarSphere_Create()
                    kThis.SetName("Backdrop stars")
                    kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
                    kForward = App.TGPoint3()
                    kForward.SetXYZ(0.185766, 0.947862, -0.258937)
                    kUp = App.TGPoint3()
                    kUp.SetXYZ(0.049823, 0.254099, 0.965894)
                    kThis.AlignToVectors(kForward, kUp)
                    kThis.SetTextureFileName(Backdrop)
                    kThis.SetTargetPolyCount(256)
                    kThis.SetHorizontalSpan(1.000000)
                    kThis.SetVerticalSpan(1.000000)
                    kThis.SetSphereRadius(300.000000)
                    kThis.SetTextureHTile(22.000000)
                    kThis.SetTextureVTile(11.000000)
                    kThis.Rebuild()
                    pSet.AddBackdropToSet(kThis,"Backdrop stars")
                    kThis.Update(0)
                    kThis = None                

        # There no customization check for default presets
        else:
                reload(JumpspaceConfiguration)

                if JumpspaceConfiguration.BackdropGFX == 'Default':
                    kThis = App.StarSphere_Create()
                    kThis.SetName("Backdrop stars")
                    kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
                    kForward = App.TGPoint3()
                    kForward.SetXYZ(0.185766, 0.947862, -0.258937)
                    kUp = App.TGPoint3()
                    kUp.SetXYZ(0.049823, 0.254099, 0.965894)
                    kThis.AlignToVectors(kForward, kUp)
                    kThis.SetTextureFileName("data/jumpspaceback.tga")
                    kThis.SetTargetPolyCount(256)
                    kThis.SetHorizontalSpan(1.000000)
                    kThis.SetVerticalSpan(1.000000)
                    kThis.SetSphereRadius(300.000000)
                    kThis.SetTextureHTile(22.000000)
                    kThis.SetTextureVTile(11.000000)
                    kThis.Rebuild()
                    pSet.AddBackdropToSet(kThis,"Backdrop stars")
                    kThis.Update(0)
                    kThis = None
                elif JumpspaceConfiguration.BackdropGFX == 'Off':
                    pass
                else:
                    Backdrop = "scripts/Custom/Jumpspace/GFX/" + JumpspaceConfiguration.BackdropGFX
                    kThis = App.StarSphere_Create()
                    kThis.SetName("Backdrop stars")
                    kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
                    kForward = App.TGPoint3()
                    kForward.SetXYZ(0.185766, 0.947862, -0.258937)
                    kUp = App.TGPoint3()
                    kUp.SetXYZ(0.049823, 0.254099, 0.965894)
                    kThis.AlignToVectors(kForward, kUp)
                    kThis.SetTextureFileName(Backdrop)
                    kThis.SetTargetPolyCount(256)
                    kThis.SetHorizontalSpan(1.000000)
                    kThis.SetVerticalSpan(1.000000)
                    kThis.SetSphereRadius(300.000000)
                    kThis.SetTextureHTile(22.000000)
                    kThis.SetTextureVTile(11.000000)
                    kThis.Rebuild()
                    pSet.AddBackdropToSet(kThis,"Backdrop stars")
                    kThis.Update(0)
                    kThis = None


# Exit in the desired set
def Exiting(pObject, pEvent):
        global pDest, pDefault, pWasCloaked

        pGame = App.Game_GetCurrentGame()
        pGame.SetGodMode(1)

        # Collision settings
        pDefault = App.ProximityManager_GetPlayerCollisionsEnabled()
        App.ProximityManager_SetPlayerCollisionsEnabled(0)

        # Clear players target first
        import TacticalInterfaceHandlers
	TacticalInterfaceHandlers.ClearTarget(None, None)
        
        # Now the magic happens
        pPlayer = MissionLib.GetPlayer()
        pPlayerName = pPlayer.GetName()
        pSet = pPlayer.GetContainingSet()
        fRadius = pPlayer.GetRadius() * 2.0
        pWasCloaked = 0

        pSys = __import__(pDest)

        pSysName = pSys.GetSetName()

        if App.g_kSetManager.GetSet(pSysName):

            pModule = App.g_kSetManager.GetSet(pSysName)

        else:
            
            # Import the dest set & initialize it
            pSys.Initialize()
            
            pModule = pSys.GetSet()

        pSet.RemoveObjectFromSet(pPlayerName)
        if pPlayer.IsCloaked():
            pWasCloaked = 1
            pCloak = pPlayer.GetCloakingSubsystem()
            if pCloak:
                pCloak.InstantDecloak()
        pModule.AddObjectToSet(pPlayer, pPlayerName)

        # Avoiding any potential problems
        try:
                        
                pPlacement = App.PlacementObject_GetObject(pModule, "Player Start")               
                pPlayer.SetTranslate(pPlacement.GetWorldLocation())
                pPlayer.SetMatrixRotation(pPlacement.GetWorldRotation())                
                                
                pPlayer.UpdateNodeOnly()

        # No Player Start Location, use random coordinates
        except:
                        
                vLocation = pPlayer.GetWorldLocation() 
                vForward = pPlayer.GetWorldForwardTG()
                        
                kPoint = App.TGPoint3()
                ChooseNewLocation(vLocation, vForward) 
		kPoint.Set(vLocation) 
		kPoint.Add(vForward) 

                while pModule.IsLocationEmptyTG(kPoint, fRadius, 1) == 0: 
                        ChooseNewLocation(vLocation, vForward) 
                        kPoint.Set(vLocation) 
                        kPoint.Add(vForward)

                pPlayer.SetTranslate(kPoint) 
         
                pPlayer.UpdateNodeOnly()


        # Update proximity manager info
        ProximityManager = pModule.GetProximityManager() 
        if (ProximityManager): 
            ProximityManager.UpdateObject(pPlayer)
                        

        # Purge memory when transfering between sets
        App.g_kLODModelManager.Purge()

        # Deactivate the fix, we don't need it anymore
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        
        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".FixDarkScreen")
        except:
            pass
        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_DESTROYED, pMission, __name__ + ".FixDarkScreenExplosions")
        except:
            pass

        # Restore warp and force ai's back on
        for kShip in pModule.GetClassObjectList(App.CT_SHIP):
            fShip = App.ShipClass_GetObject(pModule, kShip.GetName())
            pWarp = fShip.GetWarpEngineSubsystem()
            if pWarp:
                EnableWarp(fShip, pWarp)

        # Make sure we execute everything in a timely manner by delaying the exiting sequence
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".CutsceneExit", App.g_kUtopiaModule.GetGameTime() + 0.1, 0, 0)

        # Delay AI ships
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".AIExit", App.g_kUtopiaModule.GetGameTime() + 7, 0, 0)


# AI exits now
def AIExit(pObject, pEvent):
        global pDest
        
        # Now the magic happens
        pPlayer = MissionLib.GetPlayer()
        pSet = App.g_kSetManager.GetSet('JumpspaceTunnel1')

        pSys = __import__(pDest)

        pSysName = pSys.GetSetName()

        if App.g_kSetManager.GetSet(pSysName):

            pModule = App.g_kSetManager.GetSet(pSysName)

        else:
            
            # Import the dest set & initialize it
            pSys.Initialize()
            
            pModule = pSys.GetSet()

        # Delete models from memory, we no longer need them until the next trip
        pSet.DeleteObjectFromSet("Jumpspace Outer")
        pSet.DeleteObjectFromSet("Jumpspace Inner")

        # Do the transfer
        for kShip in pSet.GetClassObjectList(App.CT_SHIP):
                # WTF, where did these asteroids come from... Time to filter them out
                fShip = App.ShipClass_GetObject(pSet, kShip.GetName())
                fScript = fShip.GetScript()
                if fScript in sAsteroidList:
                    # print 'Asteroid detected, skipping'
                    continue
                
		pSet.RemoveObjectFromSet(kShip.GetName()) 
		pModule.AddObjectToSet(kShip, kShip.GetName())
		
                # Get location of the player
		pLocation = pPlayer.GetWorldLocation() 

                # Position all ships near the player
                kShipX = pLocation.GetX()
                
                kShipY = pLocation.GetY()
                
                kShipZ = pLocation.GetZ()

                RateX = GetRandomRate(100, 25)

                RateY = GetRandomRate(100, 25)

                RateZ = GetRandomRate(100, 25)

                pXCoord = kShipX + RateX

                pYCoord = kShipY + RateY

                pZCoord = kShipZ + RateZ

                kShip.SetTranslateXYZ(pXCoord, pYCoord, pZCoord)

                kShip.UpdateNodeOnly() 

                # Update proximity manager info
                ProximityManager = pModule.GetProximityManager() 
                if (ProximityManager): 
                        ProximityManager.UpdateObject(kShip)

                # Play the sounds
                pModules = __import__(fScript)
                # Is there a customization for this ship available?
                if hasattr(pModules, "JumpspaceCustomizations"):
                    pCustomization = pModules.JumpspaceCustomizations()
                    
                    # Customization exists, but does the sound entry exist?!
                    if pCustomization.has_key('ExitSound'):
                        pSound = "scripts/Custom/Jumpspace/SFX/" + pCustomization['ExitSound']

                        pExitSound = App.TGSound_Create(pSound, "Exit", 0)
                        pExitSound.SetSFX(0) 
                        pExitSound.SetInterface(1)
                        pExitSound.SetVolume(0.2)

                    # No sound entry found
                    else:
                        pExitSound = App.TGSound_Create("scripts/Custom/Jumpspace/SFX/exitjumpspace.wav", "Exit", 0)
                        pExitSound.SetSFX(0) 
                        pExitSound.SetInterface(1)
                        pExitSound.SetVolume(0.2)

                # No customizations of any kind available for this ship.
                else:
                    pExitSound = App.TGSound_Create("scripts/Custom/Jumpspace/SFX/exitjumpspace.wav", "Exit", 0)
                    pExitSound.SetSFX(0) 
                    pExitSound.SetInterface(1)
                    pExitSound.SetVolume(0.2)
            
                App.g_kSoundManager.PlaySound("Exit")

      
# Redirect function
def ExitingRedirect(pObject, pEvent):
        # Tap in over here and stop the loop sound
        try:
            App.g_kSoundManager.StopSound("JumpspaceEngineSound")
        except:
            pass
    
        Exiting(None, None)

            
# Clears set course menu
def ClearCourseSetting(pAction):
        pButton = App.SortedRegionMenu_GetWarpButton()
	if (pButton != None):
		pButton.SetDestination(None)

        return 0


# Disable helm menu, just like warping
def DisableHelmMenu(pAction):
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pHelmMenu = pTacticalControlWindow.FindMenu(pDatabase.GetString("Helm"))
	App.g_kLocalizationManager.Unload(pDatabase)

	pHelmMenu.SetDisabled()

	return 0


# Enable helm menu
def EnableHelmMenu(pAction):
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pHelmMenu = pTacticalControlWindow.FindMenu(pDatabase.GetString("Helm"))
	App.g_kLocalizationManager.Unload(pDatabase)

	pHelmMenu.SetEnabled()

	return 0


# Clever way of fixing the smash into planet bug.
def TransferPlayer(pAction):
        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()
        fRadius = pPlayer.GetRadius() * 2.0
        try:
                                
            pPlacement = App.PlacementObject_GetObject(pSet, "Player Start")               
            pPlayer.SetTranslate(pPlacement.GetWorldLocation())
            pPlayer.SetMatrixRotation(pPlacement.GetWorldRotation())                
                                        
            pPlayer.UpdateNodeOnly()

        # No Player Start Location, use random coordinates
        except:
                                
            vLocation = pPlayer.GetWorldLocation() 
            vForward = pPlayer.GetWorldForwardTG()
                        
            kPoint = App.TGPoint3()
            ChooseNewLocation(vLocation, vForward) 
	    kPoint.Set(vLocation) 
	    kPoint.Add(vForward) 

            while pSet.IsLocationEmptyTG(kPoint, fRadius, 1) == 0: 
                    ChooseNewLocation(vLocation, vForward) 
                    kPoint.Set(vLocation) 
                    kPoint.Add(vForward)

            pPlayer.SetTranslate(kPoint) 
         
            pPlayer.UpdateNodeOnly()

        # Update proximity manager info
        ProximityManager = pSet.GetProximityManager() 
        if (ProximityManager): 
            ProximityManager.UpdateObject(pPlayer)

        return 0


# Disable warp on ships we leave behind
def DisableWarp(pShip, pSubsystem, bIsChild = 0):
        if (bIsChild != 0) or (pSubsystem.GetNumChildSubsystems() == 0):
                fStats = pSubsystem.GetProperty().GetDisabledPercentage()
                pSubsystem.GetProperty().SetDisabledPercentage(2.0)

	for i in range(pSubsystem.GetNumChildSubsystems()):
		pChild = pSubsystem.GetChildSubsystem(i)

		if (pChild != None):
			DisableWarp(pShip, pChild, 1)        


# Enable warp on ships we've tampered with, check the unique signature that we leave on those ships
def EnableWarp(pShip, pSubsystem, bIsChild = 0):
        if (bIsChild != 0) or (pSubsystem.GetNumChildSubsystems() == 0):
                fStats = pSubsystem.GetProperty().GetDisabledPercentage()
                if fStats > 1.0:
                    pSubsystem.GetProperty().SetDisabledPercentage(0.5)
                    # This is our ship which also means that it's ai might not respond, let's fix this
                    pGame = App.Game_GetCurrentGame()
                    pEpisode = pGame.GetCurrentEpisode()
                    pMission = pEpisode.GetCurrentMission()
                    pEnemy = pMission.GetEnemyGroup()	
                    pNeutral = pMission.GetNeutralGroup()	
                    pFriendly = pMission.GetFriendlyGroup()

                    if (pFriendly.IsNameInGroup(pShip.GetName())):
                        FriendlyAI(pShip)

                    elif (pNeutral.IsNameInGroup(pShip.GetName())):
                        NeutralAI(pShip)

                    elif (pEnemy.IsNameInGroup(pShip.GetName())):
                        EnemyAI(pShip)
                    
	for i in range(pSubsystem.GetNumChildSubsystems()):
		pChild = pSubsystem.GetChildSubsystem(i)

		if (pChild != None):
			 EnableWarp(pShip, pChild, 1)


# Assign Friendly AI
def FriendlyAI(pShip):
        NoQBR = None
        import QuickBattle.QuickBattle
        try:
            import Custom.QuickBattleGame.QuickBattle
        except:
            NoQBR = 'NoQBR'

        if NoQBR == 'NoQBR':
            if QuickBattle.QuickBattle.pFriendlies:
		if (pShip.GetShipProperty().IsStationary() == 1):

			import QuickBattle.StarbaseFriendlyAI
			pShip.SetAI(QuickBattle.StarbaseFriendlyAI.CreateAI(pShip))
		else:
			import QuickBattle.QuickBattleFriendlyAI
			pShip.SetAI(QuickBattle.QuickBattleFriendlyAI.CreateAI(pShip))

        else:
            if QuickBattle.QuickBattle.pFriendlies:
                    if (pShip.GetShipProperty().IsStationary() == 1):

                            import QuickBattle.StarbaseFriendlyAI
                            pShip.SetAI(QuickBattle.StarbaseFriendlyAI.CreateAI(pShip))
                    else:
                            import QuickBattle.QuickBattleFriendlyAI
                            pShip.SetAI(QuickBattle.QuickBattleFriendlyAI.CreateAI(pShip))

            elif Custom.QuickBattleGame.QuickBattle.pFriendlies:
                    if (pShip.GetShipProperty().IsStationary() == 1):

                            import Custom.QuickBattleGame.StarbaseFriendlyAI
                            pShip.SetAI(Custom.QuickBattleGame.StarbaseFriendlyAI.CreateAI(pShip))
                    else:
                            import Custom.QuickBattleGame.QuickBattleFriendlyAI
                            pShip.SetAI(Custom.QuickBattleGame.QuickBattleFriendlyAI.CreateAI(pShip, 1, 1))


# Assign Enemy AI
def EnemyAI(pShip):
        NoQBR = None
        import QuickBattle.QuickBattle
        try:
            import Custom.QuickBattleGame.QuickBattle
        except:
            NoQBR = 'NoQBR'

        if NoQBR == 'NoQBR':
            if QuickBattle.QuickBattle.pEnemies:
		if (pShip.GetShipProperty().IsStationary() == 1):

			import QuickBattle.StarbaseAI
			pShip.SetAI(QuickBattle.StarbaseAI.CreateAI(pShip))
		else:
			import QuickBattle.QuickBattleAI
			pShip.SetAI(QuickBattle.QuickBattleAI.CreateAI(pShip))

	else:
            if QuickBattle.QuickBattle.pEnemies:
                    if (pShip.GetShipProperty().IsStationary() == 1):

                            import QuickBattle.StarbaseAI
                            pShip.SetAI(QuickBattle.StarbaseAI.CreateAI(pShip))
                    else:
                            import QuickBattle.QuickBattleAI
                            pShip.SetAI(QuickBattle.QuickBattleAI.CreateAI(pShip))

            elif Custom.QuickBattleGame.QuickBattle.pEnemies:
                    if (pShip.GetShipProperty().IsStationary() == 1):

                            import Custom.QuickBattleGame.StarbaseAI
                            pShip.SetAI(Custom.QuickBattleGame.StarbaseAI.CreateAI(pShip))
                    else:
                            import Custom.QuickBattleGame.QuickBattleAI
                            pShip.SetAI(Custom.QuickBattleGame.QuickBattleAI.CreateAI(pShip, 1, 1))	


# Assign Neutral AI
def NeutralAI(pShip):
        NoQBR = None
        import QuickBattle.QuickBattle
        try:
            import Custom.QuickBattleGame.QuickBattle
        except:
            NoQBR = 'NoQBR'

        if NoQBR == 'NoQBR':
            return

        if Custom.QuickBattleGame.QuickBattle.pNeutrals:
		if (pShip.GetShipProperty().IsStationary() == 1):

			import Custom.QuickBattleGame.StarbaseNeutralAI
			pShip.SetAI(Custom.QuickBattleGame.StarbaseNeutralAI.CreateAI(pShip))
		else:
			import Custom.QuickBattleGame.NeutralAI
			pShip.SetAI(Custom.QuickBattleGame.NeutralAI.CreateAI(pShip, 1, 1))


# Returns a random number
def GetRandomRate(Max, Number):
    
        return App.g_kSystemWrapper.GetRandomNumber(Max) + Number


# Tell the user where's he headed
def DestinationOutput(pObject, pEvent):
        global pPaneID
        
        # Attach a pane
        pPane = App.TGPane_Create(1.0, 1.0)
        App.g_kRootWindow.PrependChild(pPane)

        # Create a sequence and play it
        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)
        pSequence.AppendAction(TextSequence(pPane))
        pPaneID = pPane.GetObjID()
        pSequence.Play()


# Print the text to the screen
def TextSequence(pPane):
        global pTimer
        
        # Sequence 
        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)
            
        # Print the destination
        pLine = "Destination: " + pDestName
        pAction = LineAction(pLine, pPane, 2, pTimer, 16)
        pSequence.AddAction(pAction, None, 0)
        # ETA Counter
        sETA = pTimer
        sETA = int(sETA)
        pLine = "ETA: " + str(sETA) + " seconds"
        pAction = LineAction(pLine, pPane, 4, 0.8, 16)
        pSequence.AddAction(pAction, None, 0)
        sETA = sETA - 1
        fTime = 0.8
        while sETA > 0:
            pLine = "ETA: " + str(sETA) + " seconds"
            pAction = LineAction(pLine, pPane, 4, 0.8, 16)
            pSequence.AddAction(pAction, None, fTime)
            sETA = sETA - 1
            fTime = fTime + 1
        pAction = App.TGScriptAction_Create(__name__, "KillPane")
        pSequence.AppendAction(pAction, 1)
        pSequence.Play()


# Add a line action 
def LineAction(sLine, pPane, fPos, duration, fontSize):
	fHeight = fPos * 0.0375
	App.TGCreditAction_SetDefaultColor(0.65, 0.65, 1.0, 1.0)
	pAction = App.TGCreditAction_CreateSTR(sLine, pPane, 0.0, fHeight, duration, 0.25, 0.5, fontSize)
	return pAction


# Kill the pane, just a reuse of the code from DS9FX
def KillPane(pAction):
        global pPaneID
        
        pPane = App.TGPane_Cast(App.TGObject_GetTGObjectPtr(pPaneID))
	App.g_kRootWindow.DeleteChild(pPane)
		
	pPaneID = App.NULL_ID
	
	return 0


# When a new object is created in the jumpspace set it collides with the massive tunnel thus darkening the screen
def FixDarkScreen(pObject, pEvent):
        pPlayer = App.Game_GetCurrentPlayer()    
        pSet = pPlayer.GetContainingSet()

        if (pSet.GetName() == "JumpspaceTunnel1"):            
            fTunnel = MissionLib.GetShip("Jumpspace Outer", pSet) 
            fTunnel2 = MissionLib.GetShip("Jumpspace Inner", pSet) 
            
            # Disable player collision with the cone
            try:        
                fTunnel.EnableCollisionsWith(pPlayer, 0)
            except:
                pass
            try:
                fTunnel2.EnableCollisionsWith(pPlayer, 0)
            except:
                pass

            # Disable any ship collisions with the cone
            for kShip in pSet.GetClassObjectList(App.CT_SHIP):
                pShip = App.ShipClass_GetObject(pSet, kShip.GetName())
                try:
                    fTunnel.EnableCollisionsWith(pShip, 0)
                except:
                    pass
                try:
                    fTunnel2.EnableCollisionsWith(pShip, 0)
                except:
                    pass

            try:
                fTunnel.SetCollisionsOn(0)
            except:
                pass
            try: 
                fTunnel2.SetCollisionsOn(0)
            except:
                pass


# When a ship explodes, sometimes also the dark screen will show up
def FixDarkScreenExplosions(pObject, pEvent):
        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()
        
        pSet.DeleteObjectFromSet('Jumpspace Outer')
        pSet.DeleteObjectFromSet('Jumpspace Inner')

        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".FixDarkScreenExplosionsDelay", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)


# Event delayed
def FixDarkScreenExplosionsDelay(pObject, pEvent):
        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()

        scale = 1000
               
        # Create the tunnel
        TunnelString = "Jumpspace Outer"
        pTunnel = loadspacehelper.CreateShip("jumpspace", pSet, TunnelString, "Player Start")
       
        # Get the ship and rotate it like the Bajoran Wormhole in DS9Set
        fTunnel = MissionLib.GetShip(TunnelString, pSet) 
        vCurVelocity = App.TGPoint3()
        vCurVelocity.SetXYZ(0, 0.8, 0)
        fTunnel.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        # Invincible
        fTunnel.SetInvincible(1)
        fTunnel.SetHurtable(0)
        fTunnel.SetTargetable(0)

        # Very large ;)
        fTunnel.SetScale(scale)
        
        # Create the tunnel
        TunnelString2 = "Jumpspace Inner"
        pTunnel2 = loadspacehelper.CreateShip("jumpspace", pSet, TunnelString2, "Player Start")
       
        # Get the ship and rotate it like the Bajoran Wormhole in DS9Set
        fTunnel2 = MissionLib.GetShip(TunnelString2, pSet)
        # Disable collisions with the 2 models
        fTunnel2.EnableCollisionsWith(fTunnel, 0)
        vCurVelocity = App.TGPoint3()
        vCurVelocity.SetXYZ(0, 0.8, 0)
        fTunnel2.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        # Invincible
        fTunnel2.SetInvincible(1)
        fTunnel2.SetHurtable(0)
        fTunnel2.SetTargetable(0)

        # Very large ;)
        fTunnel2.SetScale(scale)

	# Custom tunnel textures?
        pModule = __import__(pPlayer.GetScript())

        # Is there a customization for this ship available?
        if hasattr(pModule, "JumpspaceCustomizations"):
            pCustomization = pModule.JumpspaceCustomizations()
            
            # Customization exists, but does the tunnel texture entry exist?!
            if pCustomization.has_key('TunnelTexture'):
                # Bingo, replace textures for both tunnels then
                GFX = "scripts/Custom/Jumpspace/GFX/" + pCustomization['TunnelTexture']

 		fTunnel.ReplaceTexture(GFX, "outer_glow")
		fTunnel2.ReplaceTexture(GFX, "outer_glow")

		fTunnel.RefreshReplacedTextures()
            	fTunnel2.RefreshReplacedTextures()
            	

        # Disable player collision with the cone
        fTunnel.EnableCollisionsWith(pPlayer, 0)
        fTunnel2.EnableCollisionsWith(pPlayer, 0)

        # Disable any ship collisions with the cone
        for kShip in pSet.GetClassObjectList(App.CT_SHIP):
            pShip = App.ShipClass_GetObject(pSet, kShip.GetName())
            fTunnel.EnableCollisionsWith(pShip, 0)
            fTunnel2.EnableCollisionsWith(pShip, 0)

        fTunnel.SetCollisionsOn(0)
        fTunnel2.SetCollisionsOn(0)
        
        # Position the tunnel so that it appears you're inside it
        pPlayerBackward = pPlayer.GetWorldBackwardTG()
        pPlayerDown = pPlayer.GetWorldDownTG()
        pPlayerPosition = pPlayer.GetWorldLocation()

        fTunnel.AlignToVectors(pPlayerBackward, pPlayerDown)
        fTunnel.SetTranslate(pPlayerPosition)
        fTunnel.UpdateNodeOnly()

        fTunnel2.AlignToVectors(pPlayerBackward, pPlayerDown)
        fTunnel2.SetTranslate(pPlayerPosition)
        fTunnel2.UpdateNodeOnly()        


# From QB.py
def ChooseNewLocation(vOrigin, vOffset): 
	# Add some random amount to vOffset 
	fUnitRandom = (App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0 
	fUnitRandom = fUnitRandom * (App.g_kSystemWrapper.GetRandomNumber (50) + 1) 
 
	vOffset.SetX( vOffset.GetX() + fUnitRandom ) 
 
 
	fUnitRandom = (App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0 
	fUnitRandom = fUnitRandom * (App.g_kSystemWrapper.GetRandomNumber (50) + 1) 
 
	vOffset.SetY( vOffset.GetY() + fUnitRandom ) 
 
	fUnitRandom = (App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0 
	fUnitRandom = fUnitRandom * (App.g_kSystemWrapper.GetRandomNumber (50) + 1) 
 
	vOffset.SetZ( vOffset.GetZ() + fUnitRandom ) 
 
	return 0 


# Somehow this piece of code prevents a game crash which sometimes occurs
def GameCrashFix(pAction):

        pTop = App.TopWindow_GetTopWindow()
        pTop.ForceTacticalVisible()
        pTop.ForceBridgeVisible()

        return 0


# Removes a menu button
def RemoveMenu():
        global bButton
        pBridge = App.g_kSetManager.GetSet("bridge")
        pHelm = App.CharacterClass_GetObject(pBridge, "Helm")
        pMenu = pHelm.GetMenu()
	if (pMenu != None):
		pButton = pMenu.GetSubmenu("Jumpspace Details")
		if (pButton != None):
			pMenu.DeleteChild(pButton)
			bButton = None


# From CWS 2.0
def CreateSlidebar (pName, eType, fMaxSpeed):
        global maxWarp, cruiseWarp
        
	pTopWindow = App.TopWindow_GetTopWindow()
	pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

	pBar = App.STNumericBar_Create()

        ##### Set Our Range. 
	pBar.SetRange(0.0, fMaxSpeed)
	pBar.SetKeyInterval(0.01)
	pBar.SetMarkerValue(fMaxSpeed)
	pBar.SetValue(fMaxSpeed)
	pBar.SetUseMarker(0)
	pBar.SetUseAlternateColor(0)
	pBar.SetUseButtons(0)

	NormalColor = App.TGColorA() 
	NormalColor.SetRGBA(0.5, 0.5, 1.0, 1.0)
	EmptyColor = App.TGColorA() 
	EmptyColor.SetRGBA(0.5, 0.5, 0.5, 1.0)

	pBar.SetNormalColor(NormalColor)
	pBar.SetEmptyColor(EmptyColor)
	pText = pBar.GetText()
	pText.SetStringW(pName)

	pBar.Resize(0.25, 0.04, 0)

	pEvent = App.TGFloatEvent_Create()
	pEvent.SetDestination(pOptionsWindow)
	pEvent.SetFloat(fMaxSpeed)
	pEvent.SetEventType(eType)

	pBar.SetUpdateEvent(pEvent)

	return pBar


# Sometimes BC doesn't acknowledge AI so we 'force' him to do so       
def CreateAI(pShip):
	pPlayer = MissionLib.GetPlayer()

        Random = lambda fMin, fMax : App.g_kSystemWrapper.GetRandomNumber((fMax - fMin) * 1000.0) / 1000.0 - fMin
        # Range values used in the AI.
        fInRange = 150.0 + Random(-25, 20)

	#########################################
	# Creating PlainAI Intercept at (279, 253)
	pIntercept = App.PlainAI_Create(pShip, "Intercept")
	pIntercept.SetScriptModule("Intercept")
	pIntercept.SetInterruptable(1)
	pScript = pIntercept.GetScriptInstance()
	pScript.SetTargetObjectName(pPlayer.GetName())
	# Done creating PlainAI Intercept
	#########################################
	#########################################
	# Creating ConditionalAI ConditionIntercept at (148, 273)
	## Conditions:
	#### Condition HaveToIntercept
	pHaveToIntercept = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", fInRange, pPlayer.GetName(), pShip.GetName())
	## Evaluation function:
	def EvalFunc(bHaveToIntercept):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if not bHaveToIntercept:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pConditionIntercept = App.ConditionalAI_Create(pShip, "ConditionIntercept")
	pConditionIntercept.SetInterruptable(1)
	pConditionIntercept.SetContainedAI(pIntercept)
	pConditionIntercept.AddCondition(pHaveToIntercept)
	pConditionIntercept.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI ConditionIntercept
	#########################################
	#########################################
	# Creating PlainAI Follow at (280, 181)
	pFollow = App.PlainAI_Create(pShip, "Follow")
	pFollow.SetScriptModule("FollowObject")
	pFollow.SetInterruptable(1)
	pScript = pFollow.GetScriptInstance()
	pScript.SetFollowObjectName(pPlayer.GetName())
	pScript.SetRoughDistances(10,20,30)
	# Done creating PlainAI Follow
	#########################################
	#########################################
	# Creating ConditionalAI PlayerInSameSet at (164, 201)
	## Conditions:
	#### Condition InSet
	pInSet = App.ConditionScript_Create("Conditions.ConditionAllInSameSet", "ConditionAllInSameSet", pShip.GetName(), pPlayer.GetName())
	## Evaluation function:
	def EvalFunc(bInSet):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bInSet:
			# Player is in the same set as we are.
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pPlayerInSameSet = App.ConditionalAI_Create(pShip, "PlayerInSameSet")
	pPlayerInSameSet.SetInterruptable(1)
	pPlayerInSameSet.SetContainedAI(pFollow)
	pPlayerInSameSet.AddCondition(pInSet)
	pPlayerInSameSet.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI PlayerInSameSet
	#########################################
	#########################################
	# Creating CompoundAI FollowWarp at (281, 125)
	import AI.Compound.FollowThroughWarp
	pFollowWarp = AI.Compound.FollowThroughWarp.CreateAI(pShip, pPlayer.GetName())
	# Done creating CompoundAI FollowWarp
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (47, 125)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (139, 132)
	pPriorityList.AddAI(pConditionIntercept, 1)
	pPriorityList.AddAI(pPlayerInSameSet, 2)
	pPriorityList.AddAI(pFollowWarp, 3)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (6, 188)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pPriorityList)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	return pAvoidObstacles

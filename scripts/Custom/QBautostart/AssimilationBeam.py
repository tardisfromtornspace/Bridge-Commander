from bcdebug import debug
##############################################################################
#   AssimilationBeam.py 
#   By BCS:TNG
#   Last Update by Wowbagger - 3/4/05 - v0.3.2
#
#   Creates a button that allows a Borg ship with an engaged tractor beam to
#   assimilate a target vessel.  Resistance is Futile.  Now with sounds!
#
#   Born of an idea on Bridge Commander Universe, someone had the idea of
#   adding damage textures to a target ship to make it look "Borgified."
#   I have no idea how to do this, but if somebody else wants to, go for it.
#
#   Credits: Thanks to Defiant for QBA, and to Apollo, Armada I and Armada II
#   for the sounds.  And that really cool guy on Google who had last updated
#   his site in 1998.  That was nice, too.
##############################################################################

## Section I: Globals and Mod Data
# Imports
import App
import MissionLib
import Conditions.ConditionFiringTractorBeam
import Libs.LibEngineering
import string
import Foundation


# Mod Info Block.  Used for MP loading.
MODINFO = {     "Author": "\"BCS:TNG\" <http://bcscripterstng.forumsplace.com/>",
                "Version": "0.3.2",
                "License": "GPL",
                "Description": "Assimilation Beam",
                "needBridge": 0
            }


# Vars - We need to globalize sTargetName so you can't switch targets in
# mid-assimilation. And we need to globalize pTimerID for your usual global
# reasons.  As Sneaker says, "Those are the rules."
global sTargetName, pTimerID
sTargetName = None
pTimerID = None
LastShipType = "NonBorg"


## Section II: Initialization and Button Checks
def init():  # Check to see whether or not to add the buttton.
                pGame	        = App.Game_GetCurrentGame()
                pEpisode	= pGame.GetCurrentEpisode()
                pMission	= pEpisode.GetCurrentMission()

                # as we all agreed, disable these mods in MP to prevent cheating ;) -- USS Sovereign
                if App.g_kUtopiaModule.IsMultiplayer():
                       debug(__name__ + ", init")
                       return

                if not Libs.LibEngineering.CheckActiveMutator("BCS:TB: Assimilation Beam"):
                       return

                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SET_PLAYER, pMission, __name__ + ".NewPlayerButtonCheck")


# When we get a player change, we need to see if AB can become/remain visible.
def NewPlayerButtonCheck(pObject = None, pEvent = None):
                debug(__name__ + ", NewPlayerButtonCheck")
                global LastShipType
                pGame           = App.Game_GetCurrentGame()
                pEpisode        = pGame.GetCurrentEpisode()
                pMission        = pEpisode.GetCurrentMission()
                pPlayer	        = MissionLib.GetPlayer()

                DeleteMenuButton("Tactical", "Assimilation Beam")                

                # Check if we are the Borg.  If not, kill the button.
                if (GetRaceFromShip(pPlayer) == "Borg") or (GetShipType(pPlayer) == "C2cube") or (GetShipType(pPlayer) == "BOBWCube" or (GetShipType(pPlayer) == "BOBWCubeMT")):

                        if LastShipType == "NonBorg":           # LastShipType prevents aural overload when restarting missions.  You only get the speech when you first choose to play as The Borg.
                                pSound = App.TGSound_Create("sfx/Custom/AssimilationBeam/FirstContactBorgSpeech.wav", "FirstContactBorgSpeech", 0)
                                pSound.SetSFX(0)
                                pSound.SetInterface(1)
                                App.g_kSoundManager.PlaySound("FirstContactBorgSpeech")
                                
                        pButton = Libs.LibEngineering.CreateMenuButton("Assimilation Beam", "Tactical", __name__ + ".ResistanceIsFutile")
                        LastShipType = "Borg"
                    
                else:
                        LastShipType = "NonBorg"

                        

## Section III: Assimilation Functions
# Assimilate the enemy vessel.
def ResistanceIsFutile(pObject, pEvent):
                debug(__name__ + ", ResistanceIsFutile")
                global sTargetName, pTimerID
                pGame           = App.Game_GetCurrentGame()
                pEpisode        = pGame.GetCurrentEpisode()
                pMission        = pEpisode.GetCurrentMission()
                pPlayer	        = MissionLib.GetPlayer()
                pPlayerAttr     = App.ShipClass_Cast(pPlayer)
                pTarget         = pPlayer.GetTarget()
                pTargetAttr     = App.ShipClass_Cast(pTarget)
                sTargetName     = pTarget.GetName()
                pFriendlies     = pMission.GetFriendlyGroup()
                pEnemies        = pMission.GetEnemyGroup()

                # Um... we do have a target, right?
                if not pTarget:
                        print "The Collective must receive a target prior to assimilation."
                        return

                # Check whether the tractor beam is actually engaged.
                pConditionTractorFiring = App.ConditionScript_Create("Conditions.ConditionFiringTractorBeam", "ConditionFiringTractorBeam", pPlayer)
                pTractorState = pConditionTractorFiring.GetStatus()
                if pTractorState == 0:
                        print "The Collective must engage the tractor beam before the assimilation assault may begin."
                        return

                # Play sound A.
                pSound = App.TGSound_Create("sfx/Custom/AssimilationBeam/ResistanceIsFutile.wav", "ResistanceIsFutile", 0)
                pSound.SetSFX(0)
                pSound.SetInterface(1)
                App.g_kSoundManager.PlaySound("ResistanceIsFutile")

                MissionLib.CallFunctionWhenConditionChanges(pMission, __name__, "BeamInterrupted", pConditionTractorFiring)

                # Disable the button while the beam does its work.
                pMenu = Libs.LibEngineering.GetBridgeMenu("Tactical")
                pButton = Libs.LibEngineering.GetButton("Assimilation Beam", pMenu)
                pButton.SetDisabled()

                # Begin assimilation.
                iTargetTime = pTargetAttr.GetHull().GetMaxCondition()/1000
                pAssimilateTimer = MissionLib.CreateTimer(Libs.LibEngineering.GetEngineeringNextEventType(), __name__ + ".Switch", App.g_kUtopiaModule.GetGameTime() + iTargetTime, 0, 0)
                pTimerID = pAssimilateTimer.GetObjID()


# Modified from EnemyFriendlyCon.py, author unknown.
def Switch(pObject, pEvent):
                debug(__name__ + ", Switch")
                global sTargetName, pTimerID
                pGame = App.Game_GetCurrentGame()
                pEpisode = pGame.GetCurrentEpisode()
                pMission = pEpisode.GetCurrentMission()
                pFriendlies = pMission.GetFriendlyGroup()
                pEnemies = pMission.GetEnemyGroup()
                pPlayer	= MissionLib.GetPlayer()
                pTarget	= pPlayer.GetTarget()
                pTargetAttr = App.ShipClass_Cast(pTarget)

                if not pTarget:
                        print("No target")
                        return

                MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "BeamInterrupted")

                if pEnemies.IsNameInGroup(sTargetName):
                        pEnemies.RemoveName(sTargetName)

                pFriendlies.AddName(sTargetName)

                if not pEnemies.GetNameTuple():
                        pEnemies.AddName("nothing")

                # Play sound B.
                pSound = App.TGSound_Create("sfx/Custom/AssimilationBeam/TargetAquired.wav", "TargetAquired", 0)
                pSound.SetSFX(0)
                pSound.SetInterface(1)
                App.g_kSoundManager.PlaySound("TargetAquired")

                # "Slide down my rainbow, *clap-clap* into my cellar door, *clap-clap* and we'll be jolly friends
                # *clap-clap* forever more!  More!  Shut the door!  Turn out the light and say good night!  Good night!"
                SetAI(pTarget, "Friendly")

                # Kill assimilation timer.
                App.g_kTimerManager.DeleteTimer(pTimerID)
                App.g_kRealtimeTimerManager.DeleteTimer(pTimerID)

                # Button recharge time is equal to assimilation time.  Smaller ship = less energy expenditure =
                # shorter recharge time.
                # Also, I don't like globals, so I just recalculate iTargetTime here.
                iTargetTime = pTargetAttr.GetHull().GetMaxCondition()/1000
                MissionLib.CreateTimer(Libs.LibEngineering.GetEngineeringNextEventType(), __name__ + ".Recharge", App.g_kUtopiaModule.GetGameTime() + iTargetTime, 0, 0)
                                

def SetAI(pShip, Side = "Friendly"):
                debug(__name__ + ", SetAI")
                g_pAIShip = App.ShipClass_Cast(pShip)

                if (g_pAIShip.GetShipProperty().IsStationary() == 1):
                        g_pAIShip.SetAI(Libs.LibEngineering.CreateStarbaseFriendlyAI(g_pAIShip))
                else:
                        g_pAIShip.SetAI(Libs.LibEngineering.CreateFriendlyAI(g_pAIShip))


# In case some crazy dude deactivates the tractor beam mid-assimilation--or
# a clever ship captain disables the emitter.
def BeamInterrupted(bStatus = None):
                debug(__name__ + ", BeamInterrupted")
                global pTimerID
                pGame = App.Game_GetCurrentGame()
                pEpisode = pGame.GetCurrentEpisode()
                pMission = pEpisode.GetCurrentMission()
                pFriendlies = pMission.GetFriendlyGroup()
                pEnemies = pMission.GetEnemyGroup()
                pPlayer	= MissionLib.GetPlayer()
                pTarget	= pPlayer.GetTarget()
                pTargetAttr = App.ShipClass_Cast(pTarget)

                # Kill assimilation timer.
                App.g_kTimerManager.DeleteTimer(pTimerID)
                App.g_kRealtimeTimerManager.DeleteTimer(pTimerID)

                # Play sound.
                pSound = App.TGSound_Create("sfx/Custom/AssimilationBeam/FreedomIrrelevantLowQ.wav", "FreedomIrrelevantLowQ", 0)
                pSound.SetSFX(0)
                pSound.SetInterface(1)
                App.g_kSoundManager.PlaySound("FreedomIrrelevantLowQ")

                # Recharges.  Yep.
                iTargetTime = pTargetAttr.GetHull().GetMaxCondition()/1000
                MissionLib.CreateTimer(Libs.LibEngineering.GetEngineeringNextEventType(), __name__ + ".Recharge", App.g_kUtopiaModule.GetGameTime() + iTargetTime, 0, 0)
                
                MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "BeamInterrupted")


# Re-enable the button.
def Recharge(pObject, pEvent):
                debug(__name__ + ", Recharge")
                pMenu = Libs.LibEngineering.GetBridgeMenu("Tactical")
                pButton = Libs.LibEngineering.GetButton("Assimilation Beam", pMenu)
                pButton.SetEnabled()


## Section IV: Utility Functions
# Graciously sent by Defiant.
def GetRaceFromShip(pShip):
                debug(__name__ + ", GetRaceFromShip")
                ShipType = GetShipType(pShip)
                if Foundation.shipList.has_key(ShipType):
                        FdtnShip = Foundation.shipList[ShipType]
                
                        if FdtnShip.GetRace():
                                return FdtnShip.GetRace().name
                return None

    
# Returns the Shiptype (from ReturnShuttles)
def GetShipType(pShip):
                debug(__name__ + ", GetShipType")
                if pShip.GetScript():
                        return string.split(pShip.GetScript(), '.')[-1]
                return None


# A little bonus help for those of you who like switching ships as often as I do and get frustrated by the disabled MVAM Infinite menus.
# (Not enabled in this version.  We've had too many setbacks as it is with AB.)
def CheckMVAM(pShip):
                debug(__name__ + ", CheckMVAM")
                FdtnShips = Foundation.shipList
                ShipType = GetShipType(pShip)
                if FdtnShips:
                        if ShipType.MenuGroup():
                                if (ShipType.MenuGroup() == "Federation MVAM Ships") or (ShipType.MenuGroup() == "MVAM Ships") or (ShipType.MenuGroup() == "Federation MVAM Ships Ships"):
                                        return 1

                return 0


# Deletes a button.  From another mod, but it's BCS:TNG's mod and my code anyhow, so I suppose I could sue myself.  Hmm.
# Might get some punitive damages... and I can't afford the money, so maybe the government will pay.  Heh heh.  Money!
def DeleteMenuButton(sMenuName, sButtonName, sSubMenuName = None):
                debug(__name__ + ", DeleteMenuButton")
                pMenu   = GetBridgeMenu(sMenuName)
                pButton = pMenu.GetButton(sButtonName)
                if sSubMenuName != None:
                        pMenu = pMenu.GetSubmenu(sSubMenuName)
                        pButton = pMenu.GetButton(sButtonName)

                pMenu.DeleteChild(pButton)


# From ATP_GUIUtils:
def GetBridgeMenu(menuName):
                debug(__name__ + ", GetBridgeMenu")
                pTactCtrlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
                pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
                if(pDatabase is None):
                        return
                App.g_kLocalizationManager.Unload(pDatabase)
                return pTactCtrlWindow.FindMenu(pDatabase.GetString(menuName))

"""
by Mario aka USS Sovereign
All Rights Reserved
For permissions check the manual/readme/agreement
"""


# Imports
import App
import MissionLib
import loadspacehelper
import Actions.ShipScriptActions
import Bridge.BridgeMenus
import Bridge.BridgeUtils
import Foundation
import DS9FXLib.DS9FXMenuLib
from Custom.DS9FX.DS9FXLib import DS9FXShips, GalaxyCharts, DS9FXPrintTextLib, DS9FXLifeSupportLib
from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents, FixForCustomTravels
from Custom.DS9FX.DS9FXLifeSupport import LifeSupport_dict
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

# Events
ET_CAMPAIGN = App.UtopiaModule_GetNextEventType()
ET_CAMPAIGN_2 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION = App.UtopiaModule_GetNextEventType()
ET_HISTORIC_MISSION = App.UtopiaModule_GetNextEventType()
ET_CLOSE = App.UtopiaModule_GetNextEventType()
ET_BACK = App.UtopiaModule_GetNextEventType()
ET_UNAVAILABLE = App.UtopiaModule_GetNextEventType()
ET_WINDOW_CLOSE = App.UtopiaModule_GetNextEventType()
ET_WINDOW_CLOSE_2 = App.UtopiaModule_GetNextEventType()
ET_WINDOW_CLOSE_3 = App.UtopiaModule_GetNextEventType()
ET_WINDOW_CLOSE_4 = App.UtopiaModule_GetNextEventType()
ET_BORDER_SKIRMISH_1 = App.UtopiaModule_GetNextEventType()
ET_BORDER_SKIRMISH_2 = App.UtopiaModule_GetNextEventType()
ET_BORDER_SKIRMISH_3 = App.UtopiaModule_GetNextEventType()
ET_BORDER_SKIRMISH_4 = App.UtopiaModule_GetNextEventType()
ET_BORDER_SKIRMISH_5 = App.UtopiaModule_GetNextEventType()
ET_HISTORIC_MISSION_1 = App.UtopiaModule_GetNextEventType()
ET_HISTORIC_MISSION_2 = App.UtopiaModule_GetNextEventType()
ET_HISTORIC_MISSION_3 = App.UtopiaModule_GetNextEventType()
ET_HISTORIC_MISSION_4 = App.UtopiaModule_GetNextEventType()
ET_HISTORIC_MISSION_5 = App.UtopiaModule_GetNextEventType()
ET_HISTORIC_MISSION_6 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_1 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_2 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_3 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_4 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_5 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_6 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_7 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_8 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_9 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_10 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_11 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_12 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_13 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_14 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_15 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_16 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_17 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_18 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_19 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_20 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_21 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_22 = App.UtopiaModule_GetNextEventType()
ET_RANDOM_MISSION_1 = App.UtopiaModule_GetNextEventType()
ET_RANDOM_MISSION_2 = App.UtopiaModule_GetNextEventType()
ET_OLD_RIVALS_1 = App.UtopiaModule_GetNextEventType()
ET_OLD_RIVALS_2 = App.UtopiaModule_GetNextEventType()
ET_OLD_RIVALS_3 = App.UtopiaModule_GetNextEventType()
ET_OLD_RIVALS_4 = App.UtopiaModule_GetNextEventType()
ET_OLD_RIVALS_5 = App.UtopiaModule_GetNextEventType()
ET_OLD_RIVALS_6 = App.UtopiaModule_GetNextEventType()
ET_OLD_RIVALS_7 = App.UtopiaModule_GetNextEventType()
ET_OLD_RIVALS_8 = App.UtopiaModule_GetNextEventType()
ET_OLD_RIVALS_9 = App.UtopiaModule_GetNextEventType()
ET_OLD_RIVALS_10 = App.UtopiaModule_GetNextEventType()

# Variables
mHelm = None
mScanSubMenu = None
mDS9SubMenu = None
mWormholeSubMenu = None
mTransferSubMenu = None
mWarpTo = None
bEnter = None
bExitToGamma = None
bExitToDS9 = None
bDockToDS9 = None
bHail = None
bMissionStats = None
bCloseChannel = None
bScan = None
bScanPlayer = None
bScanPlanet = None
bScanRegion = None
bTransferCrew = None
bRecoverShip = None
bCaptureShip = None
bKaremma = None
bIdran = None
bDosi = None
bYadera = None
bNewBajor = None
bGaia = None
bKurrill = None
bTrialus = None
bTRogoran = None
bVandros = None
bFounders = None
Scale = 0
ExitingScale = 4
ScaleTimer = None
ExitingScaleTimer = None
ScaleDistanceTimer = None
DistanceCheckCondition = None
Firepoint = None
AttachTimer = None
InsideWormholeTimer = None
RandomAttackTimer = None
iHandlerOverflow = 0
iOverflow = 0
DS9Timer = 5
ScaleWormholePrevention = 0
MissionWindow = None
MissionWindow2 = None
MissionWindow3 = None
MissionWindow4 = None
pPaneID = App.NULL_ID
dBorderSkirmish = {}
dMiniMission = {}
dHistoric = {}
dOldRivals = {}

# List of asteroid scripts
sAsteroidList = ["ships.Asteroid", "ships.Asteroid1", "ships.Asteroid2", "ships.Asteroid3", "ships.Asteroidh1", "ships.Asteroidh2", "ships.Asteroidh3"]

# Functions
def init():
        global mHelm, mScanSubMenu, mDS9SubMenu, mWormholeSubMenu, mTransferSubMenu, mWarpTo, bEnter
        global bExitToGamma, bExitToDS9, bDockToDS9, bScan, bScanPlayer, bScanRegion, bScanPlanet, bTransferCrew
        global bRecoverShip, bCaptureShip, SecHandler, bHail, bCloseChannel, bKaremma, bFounders, bKurrill, bNewBajor
        global bIdran, bDosi, bVandros, bTRogoran, bTrialus, bGaia, bYadera, ET_WINDOW_CLOSE, ET_BORDER_SKIRMISH_1
        global ET_BORDER_SKIRMISH_2, ET_BORDER_SKIRMISH_3, ET_BORDER_SKIRMISH_4, ET_BORDER_SKIRMISH_5, ET_BACK, pPerson
        global ET_HISTORIC_MISSION_1, ET_MINI_MISSION_1, ET_MINI_MISSION_2, ET_MINI_MISSION_3, ET_MINI_MISSION_4, ET_MINI_MISSION_5
        global ET_MINI_MISSION_6, ET_WINDOW_CLOSE_2, ET_WINDOW_CLOSE_3, ET_UNAVAILABLE, ET_HISTORIC_MISSION_2, ET_HISTORIC_MISSION_3
        global ET_HISTORIC_MISSION_4, ET_HISTORIC_MISSION_5, ET_MINI_MISSION_7, ET_MINI_MISSION_8, ET_MINI_MISSION_9, ET_MINI_MISSION_10
        global ET_MINI_MISSION_11, ET_CAMPAIGN_2, ET_WINDOW_CLOSE_4, ET_OLD_RIVALS_1, ET_OLD_RIVALS_2, ET_OLD_RIVALS_3, ET_OLD_RIVALS_4
        global ET_OLD_RIVALS_5, ET_OLD_RIVALS_6, ET_OLD_RIVALS_7, ET_OLD_RIVALS_8, ET_OLD_RIVALS_9, ET_OLD_RIVALS_10, ET_MINI_MISSION_12
        global ET_HISTORIC_MISSION_6, ET_MINI_MISSION_13, ET_MINI_MISSION_14, ET_MINI_MISSION_15, ET_MINI_MISSION_16, ET_MINI_MISSION_17
        global ET_MINI_MISSION_18, ET_MINI_MISSION_19, ET_MINI_MISSION_20, ET_MINI_MISSION_21, bMissionStats, ET_MINI_MISSION_22
        global ET_RANDOM_MISSION_1, ET_RANDOM_MISSION_2

        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        pMissionDatabase = pMission.SetDatabase("data/TGL/DS9FXMissionMenu.tgl")

        pKiraSet = MissionLib.SetupBridgeSet("KiraSet", "data/Models/Sets/StarbaseControl/starbasecontrolRM.nif", -40, 65, -1.55)
        pKira = App.CharacterClass_GetObject(pKiraSet, "Kira")
        if not pKira:
                pKira = MissionLib.SetupCharacter("Bridge.Characters.DS9FXMajorKira", "KiraSet", 0, 0, 5)

        pKiraMenu = Bridge.BridgeMenus.CreateBlankCharacterMenu(pMissionDatabase.GetString("MainMenu"), 0.28, 0.4, 0.7, 0.1)
        pKira.SetMenu(pKiraMenu)

        pKira.AddPythonFuncHandlerForInstance(ET_CAMPAIGN, __name__ + ".ChooseCampaign")
        pKiraMenu.AddChild(CreateBridgeMenuButton(pMissionDatabase.GetString("BorderSkirmish"), ET_CAMPAIGN, 0, pKira))

        pKira.AddPythonFuncHandlerForInstance(ET_CAMPAIGN_2, __name__ + ".ChooseCampaign2")
        pKiraMenu.AddChild(CreateBridgeMenuButton(pMissionDatabase.GetString("OldRivals"), ET_CAMPAIGN_2, 0, pKira))

        pKira.AddPythonFuncHandlerForInstance(ET_MINI_MISSION, __name__ + ".ChooseMiniMission")
        pKiraMenu.AddChild(CreateBridgeMenuButton(pMissionDatabase.GetString("MiniMissions"), ET_MINI_MISSION, 0, pKira))

        pKira.AddPythonFuncHandlerForInstance(ET_HISTORIC_MISSION, __name__ + ".ChooseHistoric")
        pKiraMenu.AddChild(CreateBridgeMenuButton(pMissionDatabase.GetString("HistoricMissions"), ET_HISTORIC_MISSION, 0, pKira))

        pKira.AddPythonFuncHandlerForInstance(ET_CLOSE, __name__ + ".CloseChannel")
        pKiraMenu.AddChild(CreateBridgeMenuButton(pMissionDatabase.GetString("Close"), ET_CLOSE, 0, pKira))

        RemoveDS9FXMenu()

        mHelm = DS9FXLib.DS9FXMenuLib.CreateMenu("DS9FX", "Helm")

        mWarpTo = DS9FXLib.DS9FXMenuLib.CreateSubMenu(mHelm, "Warp To...")
        bYadera = DS9FXLib.DS9FXMenuLib.CreateBridgeMenuButton("Yadera System", "Helm", __name__ + ".WarpToYadera", mWarpTo)
        kYadera = DS9FXLib.DS9FXMenuLib.ColorizeButton(bYadera, 0.5, 0.5, 1.0, 1.0, 0.61, 0.61, 1.0, 1.0, 0.25, 0.25, 0.25, 1.0)
        bVandros = DS9FXLib.DS9FXMenuLib.CreateBridgeMenuButton("Vandros System", "Helm", __name__ + ".WarpToVandros", mWarpTo)
        kVandros = DS9FXLib.DS9FXMenuLib.ColorizeButton(bVandros, 0.5, 0.5, 1.0, 1.0, 0.61, 0.61, 1.0, 1.0, 0.25, 0.25, 0.25, 1.0)
        bTrialus = DS9FXLib.DS9FXMenuLib.CreateBridgeMenuButton("Trialus System", "Helm", __name__ + ".WarpToTrialus", mWarpTo)
        kTrialus = DS9FXLib.DS9FXMenuLib.ColorizeButton(bTrialus, 0.5, 0.5, 1.0, 1.0, 0.61, 0.61, 1.0, 1.0, 0.25, 0.25, 0.25, 1.0)
        bTRogoran = DS9FXLib.DS9FXMenuLib.CreateBridgeMenuButton("T-Rogoran System", "Helm", __name__ + ".WarpToTRogoran", mWarpTo)
        kTRogoran = DS9FXLib.DS9FXMenuLib.ColorizeButton(bTRogoran, 0.5, 0.5, 1.0, 1.0, 0.61, 0.61, 1.0, 1.0, 0.25, 0.25, 0.25, 1.0)
        bNewBajor = DS9FXLib.DS9FXMenuLib.CreateBridgeMenuButton("New Bajor System", "Helm", __name__ + ".WarpToNewBajor", mWarpTo)
        kNewBajor = DS9FXLib.DS9FXMenuLib.ColorizeButton(bNewBajor, 0.5, 0.5, 1.0, 1.0, 0.61, 0.61, 1.0, 1.0, 0.25, 0.25, 0.25, 1.0)
        bKurrill = DS9FXLib.DS9FXMenuLib.CreateBridgeMenuButton("Kurill System", "Helm", __name__ + ".WarpToKurrill", mWarpTo)
        kKurrill = DS9FXLib.DS9FXMenuLib.ColorizeButton(bKurrill, 0.5, 0.5, 1.0, 1.0, 0.61, 0.61, 1.0, 1.0, 0.25, 0.25, 0.25, 1.0)
        bKaremma = DS9FXLib.DS9FXMenuLib.CreateBridgeMenuButton("Karemma System", "Helm", __name__ + ".WarpToKaremma", mWarpTo)
        kKaremma = DS9FXLib.DS9FXMenuLib.ColorizeButton(bKaremma, 0.5, 0.5, 1.0, 1.0, 0.61, 0.61, 1.0, 1.0, 0.25, 0.25, 0.25, 1.0)
        bGaia = DS9FXLib.DS9FXMenuLib.CreateBridgeMenuButton("Gaia System", "Helm", __name__ + ".WarpToGaia", mWarpTo)
        kGaia = DS9FXLib.DS9FXMenuLib.ColorizeButton(bGaia, 0.5, 0.5, 1.0, 1.0, 0.61, 0.61, 1.0, 1.0, 0.25, 0.25, 0.25, 1.0)
        bFounders = DS9FXLib.DS9FXMenuLib.CreateBridgeMenuButton("Founders Homeworld", "Helm", __name__ + ".WarpToFounders", mWarpTo)
        kFounders = DS9FXLib.DS9FXMenuLib.ColorizeButton(bFounders, 0.5, 0.5, 1.0, 1.0, 0.61, 0.61, 1.0, 1.0, 0.25, 0.25, 0.25, 1.0)
        bDosi = DS9FXLib.DS9FXMenuLib.CreateBridgeMenuButton("Dosi System", "Helm", __name__ + ".WarpToDosi", mWarpTo)
        kDosi = DS9FXLib.DS9FXMenuLib.ColorizeButton(bDosi, 0.5, 0.5, 1.0, 1.0, 0.61, 0.61, 1.0, 1.0, 0.25, 0.25, 0.25, 1.0)
        bIdran = DS9FXLib.DS9FXMenuLib.CreateBridgeMenuButton("Idran System", "Helm", __name__ + ".WarpToIdran", mWarpTo)
        kIdran = DS9FXLib.DS9FXMenuLib.ColorizeButton(bIdran, 0.5, 0.5, 1.0, 1.0, 0.61, 0.61, 1.0, 1.0, 0.25, 0.25, 0.25, 1.0)

        mScanSubMenu = DS9FXLib.DS9FXMenuLib.CreateSubMenu(mHelm, "Scan Options...")
        bScan = DS9FXLib.DS9FXMenuLib.CreateBridgeMenuButton("Scan Target", "Helm", __name__ + ".ScanShip", mScanSubMenu)
        kScan = DS9FXLib.DS9FXMenuLib.ColorizeButton(bScan, 0.5, 0.5, 1.0, 1.0, 0.61, 0.61, 1.0, 1.0, 0.25, 0.25, 0.25, 1.0)
        bScanRegion = DS9FXLib.DS9FXMenuLib.CreateBridgeMenuButton("Scan System", "Helm", __name__ + ".ScanSystem", mScanSubMenu)
        kScanRegion = DS9FXLib.DS9FXMenuLib.ColorizeButton(bScanRegion, 0.5, 0.5, 1.0, 1.0, 0.61, 0.61, 1.0, 1.0, 0.25, 0.25, 0.25, 1.0)
        bScanPlanet = DS9FXLib.DS9FXMenuLib.CreateBridgeMenuButton("Scan Planet", "Helm", __name__ + ".ScanPlanet", mScanSubMenu)
        kScanPlanet = DS9FXLib.DS9FXMenuLib.ColorizeButton(bScanPlanet, 0.5, 0.5, 1.0, 1.0, 0.61, 0.61, 1.0, 1.0, 0.25, 0.25, 0.25, 1.0)
        bScanPlayer = DS9FXLib.DS9FXMenuLib.CreateBridgeMenuButton("Scan Myself", "Helm", __name__ + ".ScanPlayerShip", mScanSubMenu)
        kScanPlayer = DS9FXLib.DS9FXMenuLib.ColorizeButton(bScanPlayer, 0.5, 0.5, 1.0, 1.0, 0.61, 0.61, 1.0, 1.0, 0.25, 0.25, 0.25, 1.0)

        pIncompatible = GalaxyCharts.IsIncompatibleOn()

        reload (DS9FXSavedConfig)
        if DS9FXSavedConfig.LifeSupport == 1:
                mTransferSubMenu = DS9FXLib.DS9FXMenuLib.CreateSubMenu(mHelm, "Life Support Options...")
                bTransferCrew = DS9FXLib.DS9FXMenuLib.CreateBridgeMenuButton("Transfer Crew", "Helm", __name__ + ".TransferCrewGUI", mTransferSubMenu)
                kTransferCrew = DS9FXLib.DS9FXMenuLib.ColorizeButton(bTransferCrew, 0.5, 0.5, 1.0, 1.0, 0.61, 0.61, 1.0, 1.0, 0.25, 0.25, 0.25, 1.0)
                bRecoverShip = DS9FXLib.DS9FXMenuLib.CreateBridgeMenuButton("Recover Ship", "Helm", __name__ + ".ShipRecovery", mTransferSubMenu)
                kRecoverShip = DS9FXLib.DS9FXMenuLib.ColorizeButton(bRecoverShip, 0.5, 0.5, 1.0, 1.0, 0.61, 0.61, 1.0, 1.0, 0.25, 0.25, 0.25, 1.0)
                bCaptureShip = DS9FXLib.DS9FXMenuLib.CreateBridgeMenuButton("Capture Ship", "Helm", __name__ + ".CaptureShip", mTransferSubMenu)
                kCaptureShip = DS9FXLib.DS9FXMenuLib.ColorizeButton(bCaptureShip, 0.5, 0.5, 1.0, 1.0, 0.61, 0.61, 1.0, 1.0, 0.25, 0.25, 0.25, 1.0)

        reload(DS9FXSavedConfig)
        if DS9FXSavedConfig.FederationSide == 1:
                if DS9FXSavedConfig.DominionSide == 1:
                        if DS9FXSavedConfig.DS9Selection == 1:
                                mDS9SubMenu = DS9FXLib.DS9FXMenuLib.CreateSubMenu(mHelm, "DS9 Options...")
                                bDockToDS9 = DS9FXLib.DS9FXMenuLib.CreateBridgeMenuButton("Dock To DS9", "Helm", __name__ + ".DockToDS9", mDS9SubMenu)
                                kDockToDS9 = DS9FXLib.DS9FXMenuLib.ColorizeButton(bDockToDS9, 0.5, 0.5, 1.0, 1.0, 0.61, 0.61, 1.0, 1.0, 0.25, 0.25, 0.25, 1.0)
                        print "DS9FX: You have set Dominion to be friendly. For mission purposes they have to be set as enemy. Hailing function won't initialize!"
                else:
                        if DS9FXSavedConfig.DS9Selection == 1:
                                mDS9SubMenu = DS9FXLib.DS9FXMenuLib.CreateSubMenu(mHelm, "DS9 Options...")
                                bDockToDS9 = DS9FXLib.DS9FXMenuLib.CreateBridgeMenuButton("Dock To DS9", "Helm", __name__ + ".DockToDS9", mDS9SubMenu)
                                kDockToDS9 = DS9FXLib.DS9FXMenuLib.ColorizeButton(bDockToDS9, 0.5, 0.5, 1.0, 1.0, 0.61, 0.61, 1.0, 1.0, 0.25, 0.25, 0.25, 1.0)
                                if not pIncompatible:
                                        bCloseChannel = DS9FXLib.DS9FXMenuLib.CreateBridgeMenuButton("Close Channel", "Helm", __name__ + ".CloseChannelRedirect", mDS9SubMenu)
                                        kCloseChannel = DS9FXLib.DS9FXMenuLib.ColorizeButton(bCloseChannel, 0.5, 0.5, 1.0, 1.0, 0.61, 0.61, 1.0, 1.0, 0.25, 0.25, 0.25, 1.0)
                                        bHail = DS9FXLib.DS9FXMenuLib.CreateBridgeMenuButton("Hail DS9", "Helm", __name__ + ".HailDS9", mDS9SubMenu)
                                        kHail = DS9FXLib.DS9FXMenuLib.ColorizeButton(bHail, 0.5, 0.5, 1.0, 1.0, 0.61, 0.61, 1.0, 1.0, 0.25, 0.25, 0.25, 1.0)
                                        bMissionStats = DS9FXLib.DS9FXMenuLib.CreateBridgeMenuButton("Mission Log", "Helm", __name__ + ".MissionLog", mDS9SubMenu)
                                        kMissionStats = DS9FXLib.DS9FXMenuLib.ColorizeButton(bMissionStats, 0.5, 0.5, 1.0, 1.0, 0.61, 0.61, 1.0, 1.0, 0.25, 0.25, 0.25, 1.0)
                                else:
                                        print "DS9FX: DS9FX Missions have been disabled, turn off GC's RAF and RDF in order to play DS9FX Missions."
                        else:
                                print "DS9FX: DS9 has not been enabled, hailing and docking functions won't initialize"
        else:
                print "DS9FX: Federation is an enemy, Docking and Hailing functions won't initialize!"

        mWormholeSubMenu = DS9FXLib.DS9FXMenuLib.CreateSubMenu(mHelm, "Wormhole Options...")
        bEnter = DS9FXLib.DS9FXMenuLib.CreateBridgeMenuButton("Enter Wormhole", "Helm", __name__ + ".EnterSeq", mWormholeSubMenu)
        kEnter = DS9FXLib.DS9FXMenuLib.ColorizeButton(bEnter, 0.5, 0.5, 1.0, 1.0, 0.61, 0.61, 1.0, 1.0, 0.25, 0.25, 0.25, 1.0)
        bExitToGamma = DS9FXLib.DS9FXMenuLib.CreateBridgeMenuButton("Exit To Gamma", "Helm", __name__ + ".ExitToGammaSeq", mWormholeSubMenu)
        kExitToGamme = DS9FXLib.DS9FXMenuLib.ColorizeButton(bExitToGamma, 0.5, 0.5, 1.0, 1.0, 0.61, 0.61, 1.0, 1.0, 0.25, 0.25, 0.25, 1.0)
        bExitToDS9 = DS9FXLib.DS9FXMenuLib.CreateBridgeMenuButton("Exit To DS9", "Helm", __name__ + ".ExitToDS9Seq", mWormholeSubMenu)
        kExitToDS9 = DS9FXLib.DS9FXMenuLib.ColorizeButton(bExitToDS9, 0.5, 0.5, 1.0, 1.0, 0.61, 0.61, 1.0, 1.0, 0.25, 0.25, 0.25, 1.0)

        bExitToGamma.SetDisabled()
        bExitToDS9.SetDisabled()
        bEnter.SetDisabled()

        if bHail == None:
                pass
        else:
                bHail.SetDisabled()

        if bCloseChannel == None:
                pass
        else:
                bCloseChannel.SetDisabled()

        if bDockToDS9 == None:
                pass
        else:
                bDockToDS9.SetDisabled()
        bKaremma.SetDisabled()
        bIdran.SetDisabled()
        bDosi.SetDisabled()
        bYadera.SetDisabled()
        bNewBajor.SetDisabled()
        bGaia.SetDisabled()
        bKurrill.SetDisabled()
        bTrialus.SetDisabled()
        bTRogoran.SetDisabled()
        bVandros.SetDisabled()
        bFounders.SetDisabled()

        SecHandler = 5

        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".CreateWindow", App.g_kUtopiaModule.GetGameTime() + 2, 0, 0)
        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".CreateWindow2", App.g_kUtopiaModule.GetGameTime() + 2, 0, 0)
        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".CreateWindow3", App.g_kUtopiaModule.GetGameTime() + 2, 0, 0)
        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".CreateWindow4", App.g_kUtopiaModule.GetGameTime() + 2, 0, 0)

        pPersonSet = App.g_kSetManager.GetSet("KiraSet")
        pPerson = App.CharacterClass_GetObject(pPersonSet, "Kira")

        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_WINDOW_CLOSE, pMission, __name__ + ".Window")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_WINDOW_CLOSE_2, pMission, __name__ + ".Window2")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_WINDOW_CLOSE_3, pMission, __name__ + ".Window3")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_WINDOW_CLOSE_4, pMission, __name__ + ".Window4")
        pPerson.AddPythonFuncHandlerForInstance(ET_BORDER_SKIRMISH_1, __name__ + ".BorderSkirmishMission1")
        pPerson.AddPythonFuncHandlerForInstance(ET_BORDER_SKIRMISH_2, __name__ + ".BorderSkirmishMission2")
        pPerson.AddPythonFuncHandlerForInstance(ET_BORDER_SKIRMISH_3, __name__ + ".BorderSkirmishMission3")
        pPerson.AddPythonFuncHandlerForInstance(ET_BORDER_SKIRMISH_4, __name__ + ".BorderSkirmishMission4")
        pPerson.AddPythonFuncHandlerForInstance(ET_BORDER_SKIRMISH_5, __name__ + ".BorderSkirmishMission5")
        pPerson.AddPythonFuncHandlerForInstance(ET_HISTORIC_MISSION_1, __name__ + ".DS9FXHistoricMission1")
        pPerson.AddPythonFuncHandlerForInstance(ET_HISTORIC_MISSION_2, __name__ + ".DS9FXHistoricMission2")
        pPerson.AddPythonFuncHandlerForInstance(ET_HISTORIC_MISSION_3, __name__ + ".DS9FXHistoricMission3")
        pPerson.AddPythonFuncHandlerForInstance(ET_HISTORIC_MISSION_4, __name__ + ".DS9FXHistoricMission4")
        pPerson.AddPythonFuncHandlerForInstance(ET_HISTORIC_MISSION_5, __name__ + ".DS9FXHistoricMission5")
        pPerson.AddPythonFuncHandlerForInstance(ET_HISTORIC_MISSION_6, __name__ + ".DS9FXHistoricMission6")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_1, __name__ + ".DS9FXMiniMission1")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_2, __name__ + ".DS9FXMiniMission2")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_3, __name__ + ".DS9FXMiniMission3")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_4, __name__ + ".DS9FXMiniMission4")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_5, __name__ + ".DS9FXMiniMission5")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_6, __name__ + ".DS9FXMiniMission6")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_7, __name__ + ".DS9FXMiniMission7")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_8, __name__ + ".DS9FXMiniMission8")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_9, __name__ + ".DS9FXMiniMission9")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_10, __name__ + ".DS9FXMiniMission10")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_11, __name__ + ".DS9FXMiniMission11")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_12, __name__ + ".DS9FXMiniMission12")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_13, __name__ + ".DS9FXMiniMission13")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_14, __name__ + ".DS9FXMiniMission14")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_15, __name__ + ".DS9FXMiniMission15")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_16, __name__ + ".DS9FXMiniMission16")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_17, __name__ + ".DS9FXMiniMission17")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_18, __name__ + ".DS9FXMiniMission18")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_19, __name__ + ".DS9FXMiniMission19")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_20, __name__ + ".DS9FXMiniMission20")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_21, __name__ + ".DS9FXMiniMission21")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_22, __name__ + ".DS9FXMiniMission22")
        pPerson.AddPythonFuncHandlerForInstance(ET_RANDOM_MISSION_1, __name__ + ".DS9FXRandomMission1")
        pPerson.AddPythonFuncHandlerForInstance(ET_RANDOM_MISSION_2, __name__ + ".DS9FXRandomMission2")
        pPerson.AddPythonFuncHandlerForInstance(ET_OLD_RIVALS_1, __name__ + ".OldRivalsMission1")
        pPerson.AddPythonFuncHandlerForInstance(ET_OLD_RIVALS_2, __name__ + ".OldRivalsMission2")
        pPerson.AddPythonFuncHandlerForInstance(ET_OLD_RIVALS_3, __name__ + ".OldRivalsMission3")
        pPerson.AddPythonFuncHandlerForInstance(ET_OLD_RIVALS_4, __name__ + ".OldRivalsMission4")
        pPerson.AddPythonFuncHandlerForInstance(ET_OLD_RIVALS_5, __name__ + ".OldRivalsMission5")
        pPerson.AddPythonFuncHandlerForInstance(ET_OLD_RIVALS_6, __name__ + ".OldRivalsMission6")
        pPerson.AddPythonFuncHandlerForInstance(ET_OLD_RIVALS_7, __name__ + ".OldRivalsMission7")
        pPerson.AddPythonFuncHandlerForInstance(ET_OLD_RIVALS_8, __name__ + ".OldRivalsMission8")
        pPerson.AddPythonFuncHandlerForInstance(ET_OLD_RIVALS_9, __name__ + ".OldRivalsMission9")
        pPerson.AddPythonFuncHandlerForInstance(ET_OLD_RIVALS_10, __name__ + ".OldRivalsMission10")
        pPerson.AddPythonFuncHandlerForInstance(ET_BACK, __name__ + ".BackToHailMenu")
        pPerson.AddPythonFuncHandlerForInstance(App.ET_CHARACTER_MENU, __name__ + ".CloseWindow")
        pPerson.AddPythonFuncHandlerForInstance(App.ET_CHARACTER_MENU, __name__ + ".CloseWindow2")
        pPerson.AddPythonFuncHandlerForInstance(App.ET_CHARACTER_MENU, __name__ + ".CloseWindow3")
        pPerson.AddPythonFuncHandlerForInstance(App.ET_CHARACTER_MENU, __name__ + ".CloseWindow4")
        pPerson.AddPythonFuncHandlerForInstance(ET_UNAVAILABLE, __name__ + ".MissionUnavailable")

def RestartTrigger():
        global iHandlerOverflow
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        from Custom.DS9FX.DS9FXObjects import DS9FXPreLoadedShips
        DS9FXPreLoadedShips.PreLoadEverything(pMission)

        iHandlerOverflow = 1
        DeleteAllDS9FXTimers()
        DeleteScaleWormholeTimer()
        RestoreWarpButton()

        pSequence = App.TGSequence_Create()
        pAction = App.TGScriptAction_Create(__name__, "RestartTriggerActivated")
        pSequence.AddAction(pAction, None, 0.1)
        pSequence.Play()

def RestartTriggerActivated(pAction):
        CreateDS9FXShips()
        HandleRandomAttackTimer()

        print "DS9FX: Active and Operational..."

        pSequence = App.TGSequence_Create()
        pAction = App.TGScriptAction_Create(__name__, "RestoreHandlerOverflow")
        pSequence.AddAction(pAction, None, 2)
        pSequence.Play()

        return 0

def RestoreHandlerOverflow(pAction):
        global iHandlerOverflow
        iHandlerOverflow = 0

        return 0

def EnterSetTrigger():
        global iHandlerOverflow
        if iHandlerOverflow == 1:
                return

        DeleteAllDS9FXTimers()
        DeleteScaleWormholeTimer()

def EnterSeq(pObject, pEvent):
        global ScaleDistanceTimer

        iDialogOverflow = None
        iDialogOverflow = 0

        pPlayer = App.Game_GetCurrentPlayer()
        if not pPlayer:
                return 0

        pSet = pPlayer.GetContainingSet()

        PlayerName = pPlayer.GetName()

        lNoEnter = ["Bajoran Wormhole", "USS Excalibur", "Deep_Space_9", "USS Defiant",
                    "USS Oregon", "USS_Lakota", "Bugship 1", "Bugship 2", "Bugship 3",
                    "Comet Alpha", "Bajoran Wormhole Navpoint", "Bajoran Wormhole Dummy",
                    "Sensor Anomaly", "Unknown Nebula", "Unknown Anomaly", "MVAMTemp", "Verde", 
                    "Guadiana", "Lankin", "Maroni", "Kuban", "Paraguay", "Tigris"]

        if PlayerName in lNoEnter:
                ShowNoEnterMessage()
                print "DS9FX: System specific object, cannot enter wormhole. Game will crash!"
                return

        pImpulse = pPlayer.GetImpulseEngineSubsystem()

        if not pImpulse:
                return

        for iCounter in range(pImpulse.GetNumChildSubsystems()):
                pChild = pImpulse.GetChildSubsystem(iCounter)
                pImpulseStats = pChild.GetConditionPercentage()

                if pImpulseStats <= 0.65:
                        if iDialogOverflow == 0:
                                ImpulsePrompt()
                        iDialogOverflow = None
                        iDialogOverflow = 1
                        print "DS9FX: Repair impulse engines in order to enter the wormhole!"
                        return


        if (pSet.GetName() == "DeepSpace91"):
                DS9 = __import__("Systems.DeepSpace9.DeepSpace91")
                DS9Set = DS9.GetSet()

                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", DS9Set)
                if not pDS9FXWormhole:
                        return 0

                pDS9FXWormholeID = pDS9FXWormhole.GetObjID()

                if DistanceCheck(pDS9FXWormhole) > 300:
                        FelixWarnPrompt()
                        print "DS9FX: To far out to enter Wormhole!"
                        return

                elif DistanceCheck(pDS9FXWormhole) < 50:
                        FelixWarnPrompt()
                        print "DS9FX: To close to enter Wormhole!"
                        return

                Actions.ShipScriptActions.RepairShipFully(None, pDS9FXWormholeID)

                TranslatePlayer()

                DeleteRandomAttackTimer(None, None)

                DisableEngineerMenu()

                import Custom.DS9FX.DS9FXAILib.DS9FXEnterWormholeAI
                PlayerCast = App.ShipClass_Cast(pPlayer)
                PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXEnterWormholeAI.CreateAI(PlayerCast))

                pPlayer.SetAlertLevel(App.ShipClass.RED_ALERT)

                RemoveKeyboardControl()

                pPlayer = App.Game_GetCurrentPlayer()
                pSequence = App.TGSequence_Create ()
                pSequence.AppendAction (App.TGScriptAction_Create("MissionLib", "StartCutscene"))
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", pPlayer.GetContainingSet().GetName(), pPlayer.GetName ()))
                pSequence.Play()

                DS9FXGlobalEvents.Trigger_Stop_Manual_Entry_Trigger(MissionLib.GetPlayer())

                pDS9FXWormhole.SetScale(0.01)
                pDS9FXWormhole.SetHidden(1)

                ScaleDistanceTimer = DS9FXLib.DS9FXMenuLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".ScaleWormholeDistanceCheck", App.g_kUtopiaModule.GetGameTime() + 0.1)


        elif (pSet.GetName() == "GammaQuadrant1"):	
                Gamma = __import__("Systems.GammaQuadrant.GammaQuadrant1")
                GammaSet = Gamma.GetSet()

                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", GammaSet)
                if not pDS9FXWormhole:
                        return 0

                pDS9FXWormholeID = pDS9FXWormhole.GetObjID()

                if DistanceCheck(pDS9FXWormhole) > 300:
                        FelixWarnPrompt()
                        print "DS9FX: To far out to enter Wormhole!"
                        return

                elif DistanceCheck(pDS9FXWormhole) < 50:
                        FelixWarnPrompt()
                        print "DS9FX: To close to enter Wormhole!"
                        return

                Actions.ShipScriptActions.RepairShipFully(None, pDS9FXWormholeID)

                TranslatePlayer()

                DeleteRandomAttackTimer(None, None)

                DisableEngineerMenu()

                import Custom.DS9FX.DS9FXAILib.DS9FXEnterWormholeAI
                PlayerCast = App.ShipClass_Cast(pPlayer)
                PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXEnterWormholeAI.CreateAI(PlayerCast))

                pPlayer.SetAlertLevel(App.ShipClass.RED_ALERT)

                RemoveKeyboardControl()

                pPlayer = App.Game_GetCurrentPlayer()
                pSequence = App.TGSequence_Create ()
                pSequence.AppendAction (App.TGScriptAction_Create("MissionLib", "StartCutscene"))
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", pPlayer.GetContainingSet().GetName(), pPlayer.GetName ()))
                pSequence.Play()

                DS9FXGlobalEvents.Trigger_Stop_Manual_Entry_Trigger(MissionLib.GetPlayer())

                pDS9FXWormhole.SetScale(0.01)
                pDS9FXWormhole.SetHidden(1)

                ScaleDistanceTimer = DS9FXLib.DS9FXMenuLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".ScaleWormholeDistanceCheck", App.g_kUtopiaModule.GetGameTime() + 0.1)
        else:
                pass

def ShowNoEnterMessage():
        sText = "We can't enter the wormhole with this ship sir."
        iPos = 6
        iFont = 12
        iDur = 5
        iDelay = 1
        DS9FXPrintTextLib.PrintText(sText, iPos, iFont, iDur, iDelay)        
        
def ExitToDS9Seq(pObject, pEvent):
        pPlayer = App.Game_GetCurrentPlayer()
        if not pPlayer:
                return 0

        pSet = pPlayer.GetContainingSet()
        if (pSet.GetName() == "BajoranWormhole1"):

                import Custom.DS9FX.DS9FXAILib.DS9FXExitWormholeAI
                PlayerCast = App.ShipClass_Cast(pPlayer)
                PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXExitWormholeAI.CreateAI(PlayerCast))

                pPlayer.SetAlertLevel(App.ShipClass.RED_ALERT)

                pPlayer = App.Game_GetCurrentPlayer()
                pSequence = App.TGSequence_Create ()
                pSequence.AppendAction (App.TGScriptAction_Create("MissionLib", "StartCutscene"))
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChaseCam", pPlayer.GetContainingSet().GetName(), pPlayer.GetName ()))
                pSequence.Play()

                DisableEngineerMenu()

                MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".ExitToDS9Seq2", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)
        else:
                pass

def ExitToDS9Seq2(pObject, pEvent):
        pPlayer = App.Game_GetCurrentPlayer()
        if not pPlayer:
                return 0

        pSequence = App.TGSequence_Create ()

        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))
        pSequence.AppendAction(ExitBackToDS9(None, None), 1.0)
        pSequence.Play()

def ExitToDS9Seq3(pObject, pEvent):
        global ExitingScaleTimer, pPlayer

        pNewPlayer = App.Game_GetCurrentPlayer()
        if not pNewPlayer:
                return 0

        pSequence = App.TGSequence_Create ()
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pNewPlayer.GetContainingSet().GetName ()))
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", pNewPlayer.GetContainingSet().GetName(), "Bajoran Wormhole"))
        pSequence.Play()

        import Custom.DS9FX.DS9FXAILib.DS9FXWormholeExitingSeqAI
        PlayerCast = App.ShipClass_Cast(pPlayer)
        PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXWormholeExitingSeqAI.CreateAI(PlayerCast))

        StopScaleWormhole(None, None)

        ExitingScaleTimer = MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".ExitingWormholeScaling", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)

def ExitingWormholeScaling(pObject, pEvent):
        pPlayer = App.Game_GetCurrentPlayer()
        if not pPlayer:
                return 0

        pSet = pPlayer.GetContainingSet()

        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)

        StopScaleWormhole(None, None)

        if pDS9FXWormhole:

                App.g_kSoundManager.StopSound("DS9FXWormLoop")

                from Custom.DS9FX.DS9FXLib import DS9FXWormholeScalingHelperLib

                DS9FXWormholeScalingHelperLib.StartScaling()

        else:

                App.g_kSoundManager.StopSound("DS9FXWormLoop")

                App.g_kSoundManager.PlaySound("DS9FXWormClose")

                GlobalCutsceneEnding(None, None)

def ExitBackToDS9(pObject, pEvent):
        pPlayer = App.Game_GetCurrentPlayer()
        if not pPlayer:
                return 0

        pSet = pPlayer.GetContainingSet()
        if (pSet.GetName() == "BajoranWormhole1"):

                from Custom.DS9FX.DS9FXWormholeVid import DS9FXWormholeVideo

                DS9FXWormholeVideo.PlayMovieSeq()

                pSequence = App.TGSequence_Create ()
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "bridge"))
                pSequence.Play()

                MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".CheckVideoExitingDS9", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)

        else:
                pass

def ExitToGammaSeq(pObject, pEvent):
        pPlayer = App.Game_GetCurrentPlayer()
        if not pPlayer:
                return 0

        pSet = pPlayer.GetContainingSet()
        if (pSet.GetName() == "BajoranWormhole1"):

                import Custom.DS9FX.DS9FXAILib.DS9FXExitWormholeAI
                PlayerCast = App.ShipClass_Cast(pPlayer)
                PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXExitWormholeAI.CreateAI(PlayerCast))

                pPlayer.SetAlertLevel(App.ShipClass.RED_ALERT)

                pPlayer = App.Game_GetCurrentPlayer()
                pSequence = App.TGSequence_Create ()
                pSequence.AppendAction (App.TGScriptAction_Create("MissionLib", "StartCutscene"))
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChaseCam", pPlayer.GetContainingSet().GetName(), pPlayer.GetName ()))
                pSequence.Play()

                DisableEngineerMenu()

                MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".ExitToGammaSeq2", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)

        else:
                pass

def ExitToGammaSeq2(pObject, pEvent):
        pPlayer = App.Game_GetCurrentPlayer()
        if not pPlayer:
                return 0

        pSequence = App.TGSequence_Create ()

        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))
        pSequence.AppendAction(ExitBackToGamma(None, None), 1.0)
        pSequence.Play()

def ExitToGammaSeq3(pObject, pEvent):
        global ExitingScaleTimer, pPlayer

        pNewPlayer = App.Game_GetCurrentPlayer()
        if not pNewPlayer:
                return 0

        pSequence = App.TGSequence_Create ()
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pNewPlayer.GetContainingSet().GetName ()))
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", pNewPlayer.GetContainingSet().GetName(), "Bajoran Wormhole"))
        pSequence.Play()

        import Custom.DS9FX.DS9FXAILib.DS9FXWormholeExitingSeqAI
        PlayerCast = App.ShipClass_Cast(pPlayer)
        PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXWormholeExitingSeqAI.CreateAI(PlayerCast))

        StopScaleWormhole(None, None)

        ExitingScaleTimer = MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".ExitingWormholeScaling", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)

def GlobalCutsceneEnding(pObject, pEvent):
        global ScaleWormholePrevention

        pPlayer = App.Game_GetCurrentPlayer()
        if not pPlayer:
                return 0

        pSequence = App.TGSequence_Create ()
        pSet = pPlayer.GetContainingSet()

        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))

        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
        if not pDS9FXWormhole:
                return 0

        pDS9FXWormhole.SetScale(0.01)
        pDS9FXWormhole.SetHidden(1)

        import Custom.DS9FX.DS9FXAILib.DS9FXStayAI
        PlayerCast = App.ShipClass_Cast(pPlayer)
        PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXStayAI.CreateAI(PlayerCast))

        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pPlayer.GetContainingSet().GetName ()))

        if App.g_kSetManager.GetSet("bridge"):
                pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "bridge")
                pSequence.AppendAction(pAction)
        pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "EndCutscene"))

        pSequence.Play()

        EnableEngineerMenu()

        ScaleWormholePrevention = None
        ScaleWormholePrevention = 0

        DS9FXGlobalEvents.Trigger_Outside_Wormhole(MissionLib.GetPlayer())

def ExitBackToGamma(pObject, pEvent):
        pPlayer = App.Game_GetCurrentPlayer()
        if not pPlayer:
                return 0

        pSet = pPlayer.GetContainingSet()
        if (pSet.GetName() == "BajoranWormhole1"):

                from Custom.DS9FX.DS9FXWormholeVid import DS9FXWormholeVideo

                DS9FXWormholeVideo.PlayMovieSeq()

                pSequence = App.TGSequence_Create ()
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "bridge"))
                pSequence.Play()

                MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".CheckVideoExitingGamma", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)

        else:
                pass

def EnterCheckDummyCreation(pObject, pEvent):
        pPlayer = App.Game_GetCurrentPlayer()
        if not pPlayer:
                return 0

        pSet = pPlayer.GetContainingSet()

        loadspacehelper.CreateShip(DS9FXShips.Distortion, pSet, "Bajoran Wormhole Dummy", "Wormhole Location")

        pDS9FXWormholeDummy = MissionLib.GetShip("Bajoran Wormhole Dummy", pSet)

        pDS9FXWormholeDummy.SetInvincible(1)

        pDS9FXWormholeDummy.SetHurtable(0)

        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
        if not pDS9FXWormhole:
                return 0

        EnterCheck(None, None)

def EnterCheck(pObject, pEvent):
        global DistanceCheckCondition

        pPlayer = App.Game_GetCurrentPlayer()
        if not pPlayer:
                return 0

        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        pDS9FXWormhole = "Bajoran Wormhole Dummy"
        
        pRadius = pPlayer.GetRadius()
        if pRadius > 1.0:
                iDistance = 5
        elif pRadius > 0.5:
                iDistance = 10
        else:
                iDistance = 15

        DistanceCheckCondition = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", iDistance, pPlayer.GetName(), pDS9FXWormhole)
        MissionLib.CallFunctionWhenConditionChanges(pMission, __name__, "Redirect", DistanceCheckCondition)

def Redirect(bInRange):
        MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "Redirect")

        EnterSeq2(None, None)

def ScaleWormholeDistanceCheck(pObject, pEvent):
        global ScaleDistanceTimer

        pPlayer = App.Game_GetCurrentPlayer()
        if not pPlayer:
                return 0

        pSet = pPlayer.GetContainingSet()

        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
        if not pDS9FXWormhole:
                return 0

        if DistanceCheck(pDS9FXWormhole) <= 40:
                ScaleDistanceTimerDelete(None, None)

                EnterCheckDummyCreation(None, None)

                App.g_kSoundManager.PlaySound("DS9FXWormOpen")

                pSequence = App.TGSequence_Create ()
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "TargetWatch", pPlayer.GetContainingSet().GetName(), pPlayer.GetName (), "Bajoran Wormhole"))
                pSequence.Play()

                from Custom.DS9FX.DS9FXWormholeFlash.DS9FXEnterWormholeFlash import StartGFX, CreateGFX

                StartGFX()
                for i in range(1):
                        CreateGFX(pDS9FXWormhole)

                pDS9FXWormhole.SetHidden(0)

                MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".ScaleWormhole", App.g_kUtopiaModule.GetGameTime() + 2, 0, 0)

        else:
                pPlayerBackward = pPlayer.GetWorldBackwardTG()
                pPlayerDown = pPlayer.GetWorldDownTG()

                pDS9FXWormhole.AlignToVectors(pPlayerBackward, pPlayerDown)
                pDS9FXWormhole.UpdateNodeOnly()

                ScaleDistanceTimer = DS9FXLib.DS9FXMenuLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".ScaleWormholeDistanceCheck", App.g_kUtopiaModule.GetGameTime() + 0)

def ScaleDistanceTimerDelete(pObject, pEvent):
        global ScaleDistanceTimer

        try:
                App.g_kTimerManager.DeleteTimer(ScaleDistanceTimer.GetObjID())
                App.g_kRealtimeTimerManager.DeleteTimer(ScaleDistanceTimer.GetObjID())
                ScaleDistanceTimer = None
        except:
                pass

def EnterSeq2(pObject, pEvent):
        pPlayer = App.Game_GetCurrentPlayer()
        if not pPlayer:
                return 0

        pSequence = App.TGSequence_Create ()

        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))

        App.g_kSoundManager.PlaySound("DS9FXWormLoop")

        pSequence.AppendAction(Enter(None, None), 1.0)

        pSequence.Play()

def EnterSeq3(pObject, pEvent):
        global SecHandler

        if SecHandler > DS9Timer:
                ReturnKeyboardControl()
                return

        elif SecHandler < DS9Timer:
                ReturnKeyboardControl()
                return

        else:
                App.g_kSoundManager.StopSound("DS9FXWormLoop")

                App.g_kSoundManager.PlaySound("DS9FXWormClose")

                pPlayer = App.Game_GetCurrentPlayer()
                if not pPlayer:
                        return 0
                pSequence = App.TGSequence_Create ()
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pPlayer.GetContainingSet().GetName ()))

                if App.g_kSetManager.GetSet("bridge"):
                        pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "bridge")
                        pSequence.AppendAction(pAction)
                pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "EndCutscene"))


                pSequence.Play()

                EnableEngineerMenu()

                ReturnKeyboardControl()

                pPlayer.ClearAI()

                import AI.Player.Stay
                MissionLib.SetPlayerAI("Helm", AI.Player.Stay.CreateAI(pPlayer))

                import Custom.DS9FX.DS9FXAILib.DS9FXExitWormholeAI
                PlayerCast = App.ShipClass_Cast(pPlayer)
                PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXExitWormholeAI.CreateAI(PlayerCast))

                DS9FXGlobalEvents.Trigger_Inside_Wormhole(MissionLib.GetPlayer())

def Enter(pObject, pEvent):
        pPlayer = App.Game_GetCurrentPlayer()
        if not pPlayer:
                return 0

        pSet = pPlayer.GetContainingSet()
        if (pSet.GetName() == "DeepSpace91"):

                MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".TransferShips", App.g_kUtopiaModule.GetGameTime() + 0.1, 0, 0)

        elif (pSet.GetName() == "GammaQuadrant1"):

                MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".TransferShips", App.g_kUtopiaModule.GetGameTime() + 0.1, 0, 0)

        else:
                pass

def HandleRandomAttackTimer():
        global RandomEnemyFleet, RandomAttackTimer

        pPlayer = App.Game_GetCurrentPlayer()
        if not pPlayer:
                return

        pSet = pPlayer.GetContainingSet()

        if (pSet.GetName() == "DeepSpace91"):
                DeleteRandomAttackTimer(None, None)
                reload(DS9FXSavedConfig)
                if DS9FXSavedConfig.DominionTimeSpan == 1:
                        RandomEnemyFleet = App.g_kSystemWrapper.GetRandomNumber(120) + 240
                elif DS9FXSavedConfig.DominionTimeSpan == 2:
                        RandomEnemyFleet = App.g_kSystemWrapper.GetRandomNumber(120) + 360
                elif DS9FXSavedConfig.DominionTimeSpan == 3:
                        RandomEnemyFleet = App.g_kSystemWrapper.GetRandomNumber(479) + 1
                else:
                        RandomEnemyFleet = App.g_kSystemWrapper.GetRandomNumber(120) + 120
                reload(DS9FXSavedConfig)
                if DS9FXSavedConfig.RandomEnemyFleetAttacks == 1:
                        RandomAttackTimer = DS9FXLib.DS9FXMenuLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".EnemyFleetArrives", App.g_kUtopiaModule.GetGameTime() + RandomEnemyFleet)
        else:

                DeleteRandomAttackTimer(None, None)

def ActivateDS9FXButtons():
        global bEnter, bExitToGamma, bExitToDS9, bDockToDS9, bHail, bCloseChannel, bKaremma, bFounders, bKurrill, bIdran, bDosi, bVandros, bGaia, bYadera, bNewBajor, bTrialus, bTRogoran
        global iOverflow
        if iOverflow == 1:
                return

        pPlayer = App.Game_GetCurrentPlayer()
        if not pPlayer:
                return
        pSet = pPlayer.GetContainingSet()

        HandleRandomAttackTimer()

        if (pSet.GetName() == "DeepSpace91"):
                RestoreWarpButton()
                try:
                        bEnter.SetEnabled()
                except:
                        pass
                try:
                        bExitToGamma.SetDisabled()
                except:
                        pass
                try:
                        bExitToDS9.SetDisabled()
                except:
                        pass
                if bHail == None:
                        pass
                else:
                        bHail.SetEnabled()

                if bCloseChannel == None:
                        pass
                else:
                        bCloseChannel.SetEnabled()

                if bDockToDS9 == None:
                        pass
                else:
                        bDockToDS9.SetEnabled()
                bKaremma.SetDisabled()
                bIdran.SetDisabled()
                bDosi.SetDisabled()
                bYadera.SetDisabled()
                bNewBajor.SetDisabled()
                bGaia.SetDisabled()
                bKurrill.SetDisabled()
                bTrialus.SetDisabled()
                bTRogoran.SetDisabled()
                bVandros.SetDisabled()
                bFounders.SetDisabled()
                iOverflow = 1
                RestoreiOverflowAction()

        elif (pSet.GetName() == "BajoranWormhole1"):
                DisableWarpButton()
                bEnter.SetDisabled()
                bExitToGamma.SetEnabled()
                bExitToDS9.SetEnabled()
                if bHail == None:
                        pass
                else:
                        bHail.SetDisabled()
                if bCloseChannel == None:
                        pass
                else:
                        bCloseChannel.SetDisabled()
                if bDockToDS9 == None:
                        pass
                else:
                        bDockToDS9.SetDisabled()
                bKaremma.SetDisabled()
                bIdran.SetDisabled()
                bDosi.SetDisabled()
                bYadera.SetDisabled()
                bNewBajor.SetDisabled()
                bGaia.SetDisabled()
                bKurrill.SetDisabled()
                bTrialus.SetDisabled()
                bTRogoran.SetDisabled()
                bVandros.SetDisabled()
                bFounders.SetDisabled()
                iOverflow = 1
                RestoreiOverflowAction()

        elif (pSet.GetName() == "GammaQuadrant1"):
                DisableWarpButton()
                bEnter.SetEnabled()
                bExitToGamma.SetDisabled()
                bExitToDS9.SetDisabled()
                if bHail == None:
                        pass
                else:
                        bHail.SetDisabled()
                if bCloseChannel == None:
                        pass
                else:
                        bCloseChannel.SetDisabled()
                if bDockToDS9 == None:
                        pass
                else:
                        bDockToDS9.SetDisabled()
                bKaremma.SetEnabled()
                bIdran.SetDisabled()
                bDosi.SetEnabled()
                bYadera.SetEnabled()
                bNewBajor.SetEnabled()
                bGaia.SetEnabled()
                bKurrill.SetEnabled()
                bTrialus.SetEnabled()
                bTRogoran.SetEnabled()
                bVandros.SetEnabled()
                bFounders.SetEnabled()
                iOverflow = 1
                RestoreiOverflowAction()

        elif (pSet.GetName() == "DS9FXBadlands1"):
                DisableButtons()
                iOverflow = 1
                RestoreiOverflowAction()
                
        elif (pSet.GetName() == "DS9FXQonos1"):
                DisableButtons()
                iOverflow = 1
                RestoreiOverflowAction()    
                
        elif (pSet.GetName() == "DS9FXCardassia1"):
                DisableButtons()
                iOverflow = 1
                RestoreiOverflowAction()  
                
        elif (pSet.GetName() == "DS9FXTrivas1"):
                DisableButtons()
                iOverflow = 1
                RestoreiOverflowAction()                    
                
        elif (pSet.GetName() == "DS9FXChintoka1"):
                DisableButtons()
                iOverflow = 1
                RestoreiOverflowAction()  
                
        elif (pSet.GetName() == "DS9FXVela1"):
                DisableButtons()
                iOverflow = 1
                RestoreiOverflowAction()                  

        elif (pSet.GetName() == "DS9FXKaremma1"):
                bKaremma.SetDisabled()
                bIdran.SetEnabled()
                bDosi.SetEnabled()
                bYadera.SetEnabled()
                bNewBajor.SetEnabled()
                bGaia.SetEnabled()
                bKurrill.SetEnabled()
                bTrialus.SetEnabled()
                bTRogoran.SetEnabled()
                bVandros.SetEnabled()
                bFounders.SetEnabled()
                DisableButtons(0)
                iOverflow = 1
                RestoreiOverflowAction()

        elif (pSet.GetName() == "DS9FXDosi1"):
                bKaremma.SetEnabled()
                bIdran.SetEnabled()
                bDosi.SetDisabled()
                bYadera.SetEnabled()
                bNewBajor.SetEnabled()
                bGaia.SetEnabled()
                bKurrill.SetEnabled()
                bTrialus.SetEnabled()
                bTRogoran.SetEnabled()
                bVandros.SetEnabled()
                bFounders.SetEnabled()
                DisableButtons(0)
                iOverflow = 1
                RestoreiOverflowAction()

        elif (pSet.GetName() == "DS9FXYadera1"):
                bKaremma.SetEnabled()
                bIdran.SetEnabled()
                bDosi.SetEnabled()
                bYadera.SetDisabled()
                bNewBajor.SetEnabled()
                bGaia.SetEnabled()
                bKurrill.SetEnabled()
                bTrialus.SetEnabled()
                bTRogoran.SetEnabled()
                bVandros.SetEnabled()
                bFounders.SetEnabled()
                DisableButtons(0)
                iOverflow = 1
                RestoreiOverflowAction()

        elif (pSet.GetName() == "DS9FXNewBajor1"):
                bKaremma.SetEnabled()
                bIdran.SetEnabled()
                bDosi.SetEnabled()
                bYadera.SetEnabled()
                bNewBajor.SetDisabled()
                bGaia.SetEnabled()
                bKurrill.SetEnabled()
                bTrialus.SetEnabled()
                bTRogoran.SetEnabled()
                bVandros.SetEnabled()
                bFounders.SetEnabled()
                DisableButtons(0)
                iOverflow = 1
                RestoreiOverflowAction()

        elif (pSet.GetName() == "DS9FXGaia1"):
                bKaremma.SetEnabled()
                bIdran.SetEnabled()
                bDosi.SetEnabled()
                bYadera.SetEnabled()
                bNewBajor.SetEnabled()
                bGaia.SetDisabled()
                bKurrill.SetEnabled()
                bTrialus.SetEnabled()
                bTRogoran.SetEnabled()
                bVandros.SetEnabled()
                bFounders.SetEnabled()
                DisableButtons(0)
                iOverflow = 1
                RestoreiOverflowAction()

        elif (pSet.GetName() == "DS9FXKurill1"):
                bKaremma.SetEnabled()
                bIdran.SetEnabled()
                bDosi.SetEnabled()
                bYadera.SetEnabled()
                bNewBajor.SetEnabled()
                bGaia.SetEnabled()
                bKurrill.SetDisabled()
                bTrialus.SetEnabled()
                bTRogoran.SetEnabled()
                bVandros.SetEnabled()
                bFounders.SetEnabled()
                DisableButtons(0)
                iOverflow = 1
                RestoreiOverflowAction()

        elif (pSet.GetName() == "DS9FXTrialus1"):
                bKaremma.SetEnabled()
                bIdran.SetEnabled()
                bDosi.SetEnabled()
                bYadera.SetEnabled()
                bNewBajor.SetEnabled()
                bGaia.SetEnabled()
                bKurrill.SetEnabled()
                bTrialus.SetDisabled()
                bTRogoran.SetEnabled()
                bVandros.SetEnabled()
                bFounders.SetEnabled()
                DisableButtons(0)
                iOverflow = 1
                RestoreiOverflowAction()

        elif (pSet.GetName() == "DS9FXTRogoran1"):
                bKaremma.SetEnabled()
                bIdran.SetEnabled()
                bDosi.SetEnabled()
                bYadera.SetEnabled()
                bNewBajor.SetEnabled()
                bGaia.SetEnabled()
                bKurrill.SetEnabled()
                bTrialus.SetEnabled()
                bTRogoran.SetDisabled()
                bVandros.SetEnabled()
                bFounders.SetEnabled()
                DisableButtons(0)
                iOverflow = 1
                RestoreiOverflowAction()

        elif (pSet.GetName() == "DS9FXVandros1"):
                bKaremma.SetEnabled()
                bIdran.SetEnabled()
                bDosi.SetEnabled()
                bYadera.SetEnabled()
                bNewBajor.SetEnabled()
                bGaia.SetEnabled()
                bKurrill.SetEnabled()
                bTrialus.SetEnabled()
                bTRogoran.SetEnabled()
                bVandros.SetDisabled()
                bFounders.SetEnabled()
                DisableButtons(0)
                iOverflow = 1
                RestoreiOverflowAction()

        elif (pSet.GetName() == "DS9FXFoundersHomeworld1"):
                bKaremma.SetEnabled()
                bIdran.SetEnabled()
                bDosi.SetEnabled()
                bYadera.SetEnabled()
                bNewBajor.SetEnabled()
                bGaia.SetEnabled()
                bKurrill.SetEnabled()
                bTrialus.SetEnabled()
                bTRogoran.SetEnabled()
                bVandros.SetEnabled()
                bFounders.SetDisabled()
                DisableButtons(0)
                iOverflow = 1
                RestoreiOverflowAction()

        else:
                DisableButtons()

def RestoreiOverflowAction():
        pSequence = App.TGSequence_Create()
        pAction = App.TGScriptAction_Create(__name__, "RestoreiOverflow")
        pSequence.AddAction(pAction, None, 1)
        pSequence.Play()               

def RestoreiOverflow(pAction):
        global iOverflow
        iOverflow = 0

        return 0

def DisableButtons(bDisableAll = 1):
        try:
                bExitToGamma.SetDisabled()
                bExitToDS9.SetDisabled()
                bEnter.SetDisabled()
                bHail.SetDisabled()
                bCloseChannel.SetDisabled()
                bDockToDS9.SetDisabled()

                # Resolves a GC related bug when player drops out of warp and can't warp any longer to DS9FX Sets
                pDisallow = GalaxyCharts.IsIncompatibleOn()
                if pDisallow:
                        return 0
                
                if bDisableAll == 1:
                        bKaremma.SetDisabled()
                        bIdran.SetDisabled()
                        bDosi.SetDisabled()
                        bYadera.SetDisabled()
                        bNewBajor.SetDisabled()
                        bGaia.SetDisabled()
                        bKurrill.SetDisabled()
                        bTrialus.SetDisabled()
                        bTRogoran.SetDisabled()
                        bVandros.SetDisabled()
                        bFounders.SetDisabled()
        except:
                return 0

def CreateDS9FXShips():
        pPlayer = App.Game_GetCurrentPlayer()
        if not pPlayer:
                return

        pSet = pPlayer.GetContainingSet()

        if (pSet.GetName() == "DeepSpace91"):
                from Custom.DS9FX.DS9FXObjects import DS9Objects
                DS9Objects.DS9SetObjects()

                from Custom.DS9FX.DS9FXObjects import DS9Stations
                DS9Stations.DS9SetStations()

                from Custom.DS9FX.DS9FXObjects import DS9Ships
                DS9Ships.DS9SetShips()

        elif (pSet.GetName() == "GammaQuadrant1"):
                from Custom.DS9FX.DS9FXObjects import GammaObjects
                GammaObjects.GammsSetObjects()

                from Custom.DS9FX.DS9FXObjects import GammaShips
                GammaShips.GammaSetShips()

        elif (pSet.GetName() == "BajoranWormhole1"):
                from Custom.DS9FX.DS9FXObjects import WormholeObjects
                WormholeObjects.WormholeSetObjects()

        elif (pSet.GetName() == "DS9FXBadlands1"):
                from Custom.DS9FX.DS9FXObjects import BadlandsObjects
                BadlandsObjects.BadlandsSetObjects()
                
        elif (pSet.GetName() == "DS9FXKaremma1"):
                from Custom.DS9FX.DS9FXObjects import KaremmaShips
                KaremmaShips.KaremmaSetShips()

        elif (pSet.GetName() == "DS9FXNewBajor1"):
                from Custom.DS9FX.DS9FXObjects import NewBajorShips
                NewBajorShips.NewBajorSetShips()

        elif (pSet.GetName() == "DS9FXKurill1"):
                from Custom.DS9FX.DS9FXObjects import KurrillShips
                KurrillShips.KurrillSetShips()

        elif (pSet.GetName() == "DS9FXFoundersHomeworld1"):
                from Custom.DS9FX.DS9FXObjects import FoundersShips
                FoundersShips.FoundersSetShips()
                
        elif (pSet.GetName() == "DS9FXQonos1"):
                from Custom.DS9FX.DS9FXObjects import QonosShips
                QonosShips.QonosSetShips()      
                
        elif (pSet.GetName() == "DS9FXCardassia1"):
                from Custom.DS9FX.DS9FXObjects import CardassiaShips
                CardassiaShips.CardassiaSetShips()                 

        else:
                return

def DistanceCheck(pObject):
        pPlayer = App.Game_GetCurrentGame().GetPlayer()
        vDifference = pObject.GetWorldLocation()
        vDifference.Subtract(pPlayer.GetWorldLocation())

        return vDifference.Length()

def InsideWormholePlayerWormholeDistance(pObject):
        pPlayer = App.Game_GetCurrentGame().GetPlayer()
        try:
                vDifference = pObject.GetWorldLocation()

        except:
                return 10

        vDifference.Subtract(pPlayer.GetWorldLocation())

        return vDifference.Length()

def RemoveDS9FXMenu():
        pBridge = App.g_kSetManager.GetSet("bridge")
        g_pHelm	= App.CharacterClass_GetObject(pBridge, "Helm")
        pHelmMenu = g_pHelm.GetMenu()
        if (pHelmMenu != None):
                pButton = pHelmMenu.GetSubmenu("DS9FX")
                if (pButton != None):
                        pHelmMenu.DeleteChild(pButton)

def TransferShips(pObject, pEvent):
        global InsideWormholeTimer
        global Dummy, pPlayer

        Timer = DS9Timer

        DeleteAllDS9FXTimers()

        DeleteScaleWormholeTimer()

        if App.g_kSetManager.GetSet("BajoranWormhole1"):

                App.g_kSetManager.DeleteSet("BajoranWormhole1")

        Wormhole = __import__("Systems.BajoranWormhole.BajoranWormhole1")

        WormholeSetInitialize = Wormhole.Initialize()

        WormholeSet = Wormhole.GetSet()

        pPlayer = App.Game_GetCurrentPlayer()
        if not pPlayer:
                return 0

        pSet = pPlayer.GetContainingSet()

        pPlayerPosition = pPlayer.GetWorldLocation()

        Dummy = "Dummy"

        CreateDummy = loadspacehelper.CreateShip(DS9FXShips.Dummy, pSet, Dummy, None)
        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Dummy)
        pMission.GetFriendlyGroup().AddName(Dummy)

        GetDummy = MissionLib.GetShip(Dummy, pSet)
        GetDummy.SetInvincible(1)
        GetDummy.SetHurtable(0)
        GetDummy.SetHidden(1)
        GetDummy.SetCollisionsOn(0)

        GetDummy.SetTranslate(pPlayerPosition)
        GetDummy.UpdateNodeOnly()

        import Custom.DS9FX.DS9FXAILib.DS9FXStayAI
        PlayerCast = App.ShipClass_Cast(pPlayer)
        PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXStayAI.CreateAI(PlayerCast))

        lDelete = ["Bajoran Wormhole", "USS Excalibur", "Deep_Space_9", "USS Defiant",
                   "USS Oregon", "USS_Lakota", "Bugship 1", "Bugship 2", "Bugship 3",
                   "Comet Alpha", "Bajoran Wormhole Navpoint", "Bajoran Wormhole Dummy",
                   "Bajoran Wormhole Outer", "Bajoran Wormhole Inner", "Bajoran Wormhole Extra 1",
                   "Bajoran Wormhole Extra 2", "Bajoran Wormhole Extra 3", "Bajoran Wormhole Extra 4",
                   "Sensor Anomaly", "Unknown Nebula", "Unknown Anomaly", "MVAMTemp", "Verde", 
                   "Guadiana", "Lankin", "Maroni", "Kuban", "Paraguay", "Tigris"]

        for shipName in lDelete:
                try:
                        pSet.RemoveObjectFromSet(shipName)
                except:
                        pass

        for kShip in pSet.GetClassObjectList(App.CT_SHIP):
                fShip = App.ShipClass_GetObject(pSet, kShip.GetName())
                fScript = fShip.GetScript()
                if fScript in sAsteroidList:
                        continue
                if fShip.GetShipProperty().IsStationary() == 1:
                        continue
                pID = fShip.GetObjID()
                pType = DS9FXLifeSupportLib.GetShipType(fShip)
                if pID and pType:
                        if Foundation.shipList.has_key(pType):
                                fdtnShip = Foundation.shipList[pType]
                                if fdtnShip:
                                        if hasattr(fdtnShip, "fCrew"):
                                                if fdtnShip.fCrew == "Off":
                                                        pass
                                                else:
                                                        if LifeSupport_dict.dCrew.has_key(pID):
                                                                pCrew = LifeSupport_dict.dCrew[pID]
                                                                if pCrew <= 0:
                                                                        continue
                                        else:
                                                        if LifeSupport_dict.dCrew.has_key(pID):
                                                                pCrew = LifeSupport_dict.dCrew[pID]
                                                                if pCrew <= 0:
                                                                        continue
                bCloak = 0
                if fShip.IsCloaked():
                        bCloak = 1
                pSet.RemoveObjectFromSet(kShip.GetName())
                WormholeSet.AddObjectToSet(kShip, kShip.GetName())
                if bCloak:
                        fCloak = fShip.GetCloakingSubsystem()
                        if fCloak:
                                pSequence = App.TGSequence_Create()
                                pAction = App.TGScriptAction_Create(__name__, "RecloakShip", fCloak)
                                pSequence.AddAction(pAction, None, 6)
                                pSequence.Play()                 

                pLocation = pPlayer.GetWorldLocation()
                kShipX = pLocation.GetX()
                kShipY = pLocation.GetY()
                kShipZ = pLocation.GetZ()
                RateX = GetRandomRate(1)
                RateY = GetRandomRate(1)
                RateZ = GetRandomRate(1)
                pXCoord = kShipX + RateX
                pYCoord = kShipY + RateY
                pZCoord = kShipZ + RateZ
                kShip.SetTranslateXYZ(pXCoord, pYCoord, pZCoord)
                kShip.UpdateNodeOnly()

                ProximityManager = WormholeSet.GetProximityManager()
                if (ProximityManager):
                        ProximityManager.UpdateObject(kShip)


        from Custom.DS9FX.DS9FXObjects import WormholeObjects

        WormholeObjects.WormholeSetObjects()

        pGame = App.Game_GetCurrentGame()
        pGame.SetPlayer(GetDummy)

        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole Outer", WormholeSet)
        pDS9FXWormhole2 = MissionLib.GetShip("Bajoran Wormhole Inner", WormholeSet)

        pDS9FXWormhole3 = MissionLib.GetShip("Bajoran Wormhole Extra 1", WormholeSet)
        pDS9FXWormhole4 = MissionLib.GetShip("Bajoran Wormhole Extra 2", WormholeSet)
        pDS9FXWormhole5 = MissionLib.GetShip("Bajoran Wormhole Extra 3", WormholeSet)
        pDS9FXWormhole6 = MissionLib.GetShip("Bajoran Wormhole Extra 4", WormholeSet)
        bExtra1 = 0
        bExtra2 = 0
        bExtra3 = 0
        bExtra4 = 0

        if not pDS9FXWormhole or not pDS9FXWormhole2:
                return

        pPlayerBackward = pPlayer.GetWorldBackwardTG()
        pPlayerDown = pPlayer.GetWorldDownTG()
        pPlayerForward = pPlayer.GetWorldForwardTG()
        pPlayerUp = pPlayer.GetWorldUpTG()
        pPlayerPosition = pPlayer.GetWorldLocation()

        pDS9FXWormhole.AlignToVectors(pPlayerBackward, pPlayerDown)
        pDS9FXWormhole.SetTranslate(pPlayerPosition)
        pDS9FXWormhole.UpdateNodeOnly()

        pDS9FXWormhole2.AlignToVectors(pPlayerBackward, pPlayerDown)
        pDS9FXWormhole2.SetTranslate(pPlayerPosition)
        pDS9FXWormhole2.UpdateNodeOnly()

        if pDS9FXWormhole3:
                pDS9FXWormhole3.AlignToVectors(pPlayerBackward, pPlayerDown)
                TranslateWormholeExtras(pDS9FXWormhole3, x = 0, y = 400, z = 400)
                bExtra1 = 1

        if pDS9FXWormhole4:
                pDS9FXWormhole4.AlignToVectors(pPlayerBackward, pPlayerDown)
                TranslateWormholeExtras(pDS9FXWormhole4, x = 0, y = -400, z = -400)
                bExtra2 = 1

        if pDS9FXWormhole5:
                pDS9FXWormhole5.AlignToVectors(pPlayerForward, pPlayerUp)
                TranslateWormholeExtras(pDS9FXWormhole5, x = 0, y = 400, z = -400)
                bExtra3 = 1

        if pDS9FXWormhole6:
                pDS9FXWormhole6.AlignToVectors(pPlayerForward, pPlayerUp)
                TranslateWormholeExtras(pDS9FXWormhole6, x = 0, y = -400, z = 400)
                bExtra4 = 1

        pPlayer.ClearAI()

        import Custom.DS9FX.DS9FXAILib.DS9FXExitWormholeAI
        PlayerCast = App.ShipClass_Cast(pPlayer)
        PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXExitWormholeAI.CreateAI(PlayerCast))

        RemoveKeyboardControl()
        pSequence = App.TGSequence_Create ()
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pPlayer.GetContainingSet().GetName ()))
        pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "EndCutscene"))
        pSequence.AppendAction (App.TGScriptAction_Create("MissionLib", "StartCutscene"))
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChaseCam", pPlayer.GetContainingSet().GetName(), pPlayer.GetName ()))
        pSequence.Play()

        App.g_kLODModelManager.Purge()

        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".DeleteDummy", App.g_kUtopiaModule.GetGameTime() + 4, 0, 0)

        if Timer == 5:
                MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".EnterSeq3", App.g_kUtopiaModule.GetGameTime() + Timer, 0, 0)

        else:
                ReturnKeyboardControl()

        InsideWormholeTimer = DS9FXLib.DS9FXMenuLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".InsideWormholeDistanceCheck", App.g_kUtopiaModule.GetGameTime() + 10)

def TransferShips2(pObject, pEvent):
        global Dummy, pPlayer
        global ScaleWormholePrevention

        ScaleWormholePrevention = 1

        DeleteAllDS9FXTimers()

        DeleteScaleWormholeTimer()

        if App.g_kSetManager.GetSet("DeepSpace91"):

                DS9Set = App.g_kSetManager.GetSet("DeepSpace91")

        else:

                DS9 = __import__("Systems.DeepSpace9.DeepSpace91")

                DS9SetInitialize = DS9.Initialize()

                DS9Set = DS9.GetSet()

        pPlayer = App.Game_GetCurrentPlayer()
        if not pPlayer:
                return 0

        pSet = pPlayer.GetContainingSet()

        pPlayerPosition = pPlayer.GetWorldLocation()

        Dummy = "Dummy"

        CreateDummy = loadspacehelper.CreateShip(DS9FXShips.Dummy, pSet, Dummy, None)
        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Dummy)
        pMission.GetFriendlyGroup().AddName(Dummy)

        GetDummy = MissionLib.GetShip(Dummy, pSet)
        GetDummy.SetInvincible(1)
        GetDummy.SetHurtable(0)
        GetDummy.SetHidden(1)
        GetDummy.SetCollisionsOn(0)

        GetDummy.SetTranslate(pPlayerPosition)
        GetDummy.UpdateNodeOnly()

        lDelete = ["Bajoran Wormhole", "USS Excalibur", "Deep_Space_9", "USS Defiant",
                   "USS Oregon", "USS_Lakota", "Bugship 1", "Bugship 2", "Bugship 3",
                   "Comet Alpha", "Bajoran Wormhole Navpoint", "Bajoran Wormhole Dummy",
                   "Bajoran Wormhole Outer", "Bajoran Wormhole Inner", "Bajoran Wormhole Extra 1",
                   "Bajoran Wormhole Extra 2", "Bajoran Wormhole Extra 3", "Bajoran Wormhole Extra 4",
                   "Sensor Anomaly", "Unknown Nebula", "Unknown Anomaly", "MVAMTemp","Verde", 
                   "Guadiana", "Lankin", "Maroni", "Kuban", "Paraguay", "Tigris"]

        for shipName in lDelete:
                try:
                        pSet.RemoveObjectFromSet(shipName)
                except:
                        pass

        for kShip in pSet.GetClassObjectList(App.CT_SHIP):
                fShip = App.ShipClass_GetObject(pSet, kShip.GetName())
                fScript = fShip.GetScript()
                if fScript in sAsteroidList:
                        continue
                if fShip.GetShipProperty().IsStationary() == 1:
                        continue 
                pID = fShip.GetObjID()
                pType = DS9FXLifeSupportLib.GetShipType(fShip)
                if pID and pType:
                        if Foundation.shipList.has_key(pType):
                                fdtnShip = Foundation.shipList[pType]
                                if fdtnShip:
                                        if hasattr(fdtnShip, "fCrew"):
                                                if fdtnShip.fCrew == "Off":
                                                        pass
                                                else:
                                                        if LifeSupport_dict.dCrew.has_key(pID):
                                                                pCrew = LifeSupport_dict.dCrew[pID]
                                                                if pCrew <= 0:
                                                                        continue
                                        else:
                                                        if LifeSupport_dict.dCrew.has_key(pID):
                                                                pCrew = LifeSupport_dict.dCrew[pID]
                                                                if pCrew <= 0:
                                                                        continue                
                bCloak = 0
                if fShip.IsCloaked():
                        bCloak = 1             
                pSet.RemoveObjectFromSet(kShip.GetName())
                DS9Set.AddObjectToSet(kShip, kShip.GetName())
                if bCloak:
                        fCloak = fShip.GetCloakingSubsystem()
                        if fCloak:
                                pSequence = App.TGSequence_Create()
                                pAction = App.TGScriptAction_Create(__name__, "RecloakShip", fCloak)
                                pSequence.AddAction(pAction, None, 6)
                                pSequence.Play()               

                pLocation = pPlayer.GetWorldLocation()
                kShipX = pLocation.GetX()
                kShipY = pLocation.GetY()
                kShipZ = pLocation.GetZ()
                RateX = GetRandomRate(1)
                RateY = GetRandomRate(1)
                RateZ = GetRandomRate(1)
                pXCoord = kShipX + RateX
                pYCoord = kShipY + RateY
                pZCoord = kShipZ + RateZ
                kShip.SetTranslateXYZ(pXCoord, pYCoord, pZCoord)
                kShip.UpdateNodeOnly()

                ProximityManager = DS9Set.GetProximityManager()
                if (ProximityManager):
                        ProximityManager.UpdateObject(kShip)


        from Custom.DS9FX.DS9FXObjects import DS9Objects

        DS9Objects.DS9SetObjects()

        from Custom.DS9FX.DS9FXObjects import DS9Stations

        DS9Stations.DS9SetStations()

        from Custom.DS9FX.DS9FXObjects import DS9Ships

        DS9Ships.DS9SetShips()

        pGame = App.Game_GetCurrentGame()
        pGame.SetPlayer(GetDummy)

        import Custom.DS9FX.DS9FXAILib.DS9FXStayAI
        PlayerCast = App.ShipClass_Cast(pPlayer)
        PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXStayAI.CreateAI(PlayerCast))

        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", DS9Set)

        if not pDS9FXWormhole:
                return

        pWormholePlacement = App.PlacementObject_GetObject(DS9Set, "ExitPoint Location")
        pPlayer.SetTranslate(pWormholePlacement.GetWorldLocation())
        pPlayer.SetMatrixRotation(pWormholePlacement.GetWorldRotation())

        pPlayer.UpdateNodeOnly()

        App.g_kLODModelManager.Purge()

        pDS9FXWormhole.SetScale(ExitingScale)
        pDS9FXWormhole.SetHidden(0)

        StopScaleWormhole(None, None)

        ExitToDS9Seq3(None, None)

        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".DeleteDummy", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)

def TransferShips3(pObject, pEvent):
        global Dummy, pPlayer
        global ScaleWormholePrevention

        ScaleWormholePrevention = 1

        DeleteAllDS9FXTimers()

        DeleteScaleWormholeTimer()

        if App.g_kSetManager.GetSet("GammaQuadrant1"):

                GammaSet = App.g_kSetManager.GetSet("GammaQuadrant1")

        else:

                Gamma = __import__("Systems.GammaQuadrant.GammaQuadrant1")

                GammaSetInitialize = Gamma.Initialize()

                GammaSet = Gamma.GetSet()

        pPlayer = App.Game_GetCurrentPlayer()
        if not pPlayer:
                return 0

        pSet = pPlayer.GetContainingSet()

        pPlayerPosition = pPlayer.GetWorldLocation()

        Dummy = "Dummy"

        CreateDummy = loadspacehelper.CreateShip(DS9FXShips.Dummy, pSet, Dummy, None)
        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Dummy)
        pMission.GetFriendlyGroup().AddName(Dummy)

        GetDummy = MissionLib.GetShip(Dummy, pSet)
        GetDummy.SetInvincible(1)
        GetDummy.SetHurtable(0)
        GetDummy.SetHidden(1)
        GetDummy.SetCollisionsOn(0)

        GetDummy.SetTranslate(pPlayerPosition)
        GetDummy.UpdateNodeOnly()

        lDelete = ["Bajoran Wormhole", "USS Excalibur", "Deep_Space_9", "USS Defiant",
                   "USS Oregon", "USS_Lakota", "Bugship 1", "Bugship 2", "Bugship 3",
                   "Comet Alpha", "Bajoran Wormhole Navpoint", "Bajoran Wormhole Dummy",
                   "Bajoran Wormhole Outer", "Bajoran Wormhole Inner", "Bajoran Wormhole Extra 1",
                   "Bajoran Wormhole Extra 2", "Bajoran Wormhole Extra 3", "Bajoran Wormhole Extra 4",
                   "Sensor Anomaly", "Unknown Nebula", "Unknown Anomaly", "MVAMTemp", "Verde", 
                   "Guadiana", "Lankin", "Maroni", "Kuban", "Paraguay", "Tigris"]

        for shipName in lDelete:
                try:
                        pSet.RemoveObjectFromSet(shipName)
                except:
                        pass

        for kShip in pSet.GetClassObjectList(App.CT_SHIP):
                fShip = App.ShipClass_GetObject(pSet, kShip.GetName())
                fScript = fShip.GetScript()
                if fScript in sAsteroidList:
                        continue
                if fShip.GetShipProperty().IsStationary() == 1:
                        continue    
                pID = fShip.GetObjID()
                pType = DS9FXLifeSupportLib.GetShipType(fShip)
                if pID and pType:
                        if Foundation.shipList.has_key(pType):
                                fdtnShip = Foundation.shipList[pType]
                                if fdtnShip:
                                        if hasattr(fdtnShip, "fCrew"):
                                                if fdtnShip.fCrew == "Off":
                                                        pass
                                                else:
                                                        if LifeSupport_dict.dCrew.has_key(pID):
                                                                pCrew = LifeSupport_dict.dCrew[pID]
                                                                if pCrew <= 0:
                                                                        continue
                                        else:
                                                        if LifeSupport_dict.dCrew.has_key(pID):
                                                                pCrew = LifeSupport_dict.dCrew[pID]
                                                                if pCrew <= 0:
                                                                        continue                
                bCloak = 0
                if fShip.IsCloaked():
                        bCloak = 1               
                pSet.RemoveObjectFromSet(kShip.GetName())
                GammaSet.AddObjectToSet(kShip, kShip.GetName())
                if bCloak:
                        fCloak = fShip.GetCloakingSubsystem()
                        if fCloak:
                                pSequence = App.TGSequence_Create()
                                pAction = App.TGScriptAction_Create(__name__, "RecloakShip", fCloak)
                                pSequence.AddAction(pAction, None, 6)
                                pSequence.Play()               

                pLocation = pPlayer.GetWorldLocation()
                kShipX = pLocation.GetX()
                kShipY = pLocation.GetY()
                kShipZ = pLocation.GetZ()
                RateX = GetRandomRate(1)
                RateY = GetRandomRate(1)
                RateZ = GetRandomRate(1)
                pXCoord = kShipX + RateX
                pYCoord = kShipY + RateY
                pZCoord = kShipZ + RateZ
                kShip.SetTranslateXYZ(pXCoord, pYCoord, pZCoord)
                kShip.UpdateNodeOnly()

                ProximityManager = GammaSet.GetProximityManager()
                if (ProximityManager):
                        ProximityManager.UpdateObject(kShip)


        from Custom.DS9FX.DS9FXObjects import GammaObjects

        GammaObjects.GammsSetObjects()

        from Custom.DS9FX.DS9FXObjects import GammaShips

        GammaShips.GammaSetShips()

        pGame = App.Game_GetCurrentGame()
        pGame.SetPlayer(GetDummy)

        import Custom.DS9FX.DS9FXAILib.DS9FXStayAI
        PlayerCast = App.ShipClass_Cast(pPlayer)
        PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXStayAI.CreateAI(PlayerCast))

        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", GammaSet)

        if not pDS9FXWormhole:
                return

        pWormholePlacement = App.PlacementObject_GetObject(GammaSet, "ExitPoint Location")
        pPlayer.SetTranslate(pWormholePlacement.GetWorldLocation())
        pPlayer.SetMatrixRotation(pWormholePlacement.GetWorldRotation())

        pPlayer.UpdateNodeOnly()

        APShip = MissionLib.GetShip("Bugship 1", GammaSet)
        APShip2 = MissionLib.GetShip("Bugship 2", GammaSet)
        APShip3 = MissionLib.GetShip("Bugship 2", GammaSet)

        reload(DS9FXSavedConfig)
        if DS9FXSavedConfig.DomIS == 1:
                pCurrGame = App.Game_GetCurrentGame()
                pCurrEpisode = pCurrGame.GetCurrentEpisode()
                pCurrMission = pCurrEpisode.GetCurrentMission()
                pEnemies = pCurrMission.GetEnemyGroup()
                if pEnemies.IsNameInGroup("Bugship 1") or pEnemies.IsNameInGroup("Bugship 2") or pEnemies.IsNameInGroup("Bugship 3"):
                        if APShip:
                                MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".AntiprotonScan", App.g_kUtopiaModule.GetGameTime() + 60, 0, 0)

                        elif APShip2:
                                MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".AntiprotonScan", App.g_kUtopiaModule.GetGameTime() + 60, 0, 0)

                        elif APShip3:
                                MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".AntiprotonScan", App.g_kUtopiaModule.GetGameTime() + 60, 0, 0)

        App.g_kLODModelManager.Purge()

        pDS9FXWormhole.SetScale(ExitingScale)
        pDS9FXWormhole.SetHidden(0)

        StopScaleWormhole(None, None)

        ExitToGammaSeq3(None, None)

        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".DeleteDummy", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)

def InsideWormholeDistanceCheck(pObject, pEvent):
        global InsideWormholeTimer

        pPlayer = App.Game_GetCurrentPlayer()
        if not pPlayer:
                return 0

        pSet = pPlayer.GetContainingSet()

        Wormhole = __import__("Systems.BajoranWormhole.BajoranWormhole1")

        WormholeSet = Wormhole.GetSet()

        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole Outer", WormholeSet)
        pDS9FXWormhole2 = MissionLib.GetShip("Bajoran Wormhole Inner", WormholeSet)

        if not pDS9FXWormhole or not pDS9FXWormhole2:
                return 0

        pDS9FXWormhole3 = MissionLib.GetShip("Bajoran Wormhole Extra 1", WormholeSet)
        pDS9FXWormhole4 = MissionLib.GetShip("Bajoran Wormhole Extra 2", WormholeSet)
        pDS9FXWormhole5 = MissionLib.GetShip("Bajoran Wormhole Extra 3", WormholeSet)
        pDS9FXWormhole6 = MissionLib.GetShip("Bajoran Wormhole Extra 4", WormholeSet)

        if not (pSet.GetName() == "BajoranWormhole1"):
                KillInsideWormholeTimer(None, None)

        if InsideWormholePlayerWormholeDistance(pDS9FXWormhole) > 1500:
                TranslateWormholeCone(pDS9FXWormhole)
                TranslateWormholeCone(pDS9FXWormhole2)

                if pDS9FXWormhole3:
                        TranslateWormholeExtras(pDS9FXWormhole3, x = 0, y = 400, z = 400)

                if pDS9FXWormhole4:
                        TranslateWormholeExtras(pDS9FXWormhole4, x = 0, y = -400, z = -400)

                if pDS9FXWormhole5:
                        TranslateWormholeExtras(pDS9FXWormhole5, x = 0, y = 400, z = -400)

                if pDS9FXWormhole6:
                        TranslateWormholeExtras(pDS9FXWormhole6, x = 0, y = -400, z = 400)


        InsideWormholeTimer = DS9FXLib.DS9FXMenuLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".InsideWormholeDistanceCheck", App.g_kUtopiaModule.GetGameTime() + 10)

def RecloakShip(pAction, pCloak):
        pCloak.InstantCloak()

        return 0

def TranslateWormholeCone(pShip):
        pPlayer = App.Game_GetCurrentPlayer()
        if not pPlayer:
                return

        pPlayerPosition = pPlayer.GetWorldLocation()

        pShip.SetTranslate(pPlayerPosition)

        pShip.UpdateNodeOnly()

def TranslateWormholeExtras(pShip, x=0, y=0, z=0):
        Wormhole = __import__("Systems.BajoranWormhole.BajoranWormhole1")

        WormholeSet = Wormhole.GetSet()

        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole Outer", WormholeSet)
        if not pDS9FXWormhole:
                return 0

        pLocation = pDS9FXWormhole.GetWorldLocation()
        pX = pLocation.GetX() + x
        pY = pLocation.GetY() + y
        pZ = pLocation.GetZ() + z

        pShip.SetTranslateXYZ(pX, pY, pZ)

        pShip.UpdateNodeOnly()

def KillInsideWormholeTimer(pObject, pEvent):
        global InsideWormholeTimer

        try:
                App.g_kTimerManager.DeleteTimer(InsideWormholeTimer.GetObjID())
                App.g_kRealtimeTimerManager.DeleteTimer(InsideWormholeTimer.GetObjID())
                InsideWormholeTimer = None
        except:
                pass

def ScaleWormhole(pObject, pEvent):
        global Scale, ScaleTimer
        global ScaleWormholePrevention

        ScaleDistanceTimerDelete(None, None)

        if ScaleWormholePrevention == 1:
                StopScaleWormhole(None, None)
                return

        pPlayer = App.Game_GetCurrentPlayer()
        if not pPlayer:
                return 0

        pSet = pPlayer.GetContainingSet()

        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
        if not pDS9FXWormhole:
                return

        Scale = Scale + 0.015

        try:
                pDS9FXWormhole.SetScale(Scale)

        except AttributeError:
                StopScaleWormhole(None, None)

        if Scale >= 4:
                StopScaleWormhole(None, None)

        else:
                ScaleTimer = MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".ScaleWormhole", App.g_kUtopiaModule.GetGameTime() + 0.05, 0, 0)

def StopScaleWormhole(pObject, pEvent):
        global Scale, ScaleTimer

        DeleteScaleWormholeTimer()
        ScaleTimer = None
        Scale = 0

def AntiprotonScan(pObject, pEvent):
        Gamma = __import__("Systems.GammaQuadrant.GammaQuadrant1")
        GammaSet = Gamma.GetSet()

        APShip = MissionLib.GetShip("Bugship 1", GammaSet)
        APShip2 = MissionLib.GetShip("Bugship 2", GammaSet)
        APShip3 = MissionLib.GetShip("Bugship 2", GammaSet)

        pCurrGame = App.Game_GetCurrentGame()
        pCurrEpisode = pCurrGame.GetCurrentEpisode()
        pCurrMission = pCurrEpisode.GetCurrentMission()
        pEnemies = pCurrMission.GetEnemyGroup()
        if not pEnemies.IsNameInGroup("Bugship 1") or not pEnemies.IsNameInGroup("Bugship 2") or not pEnemies.IsNameInGroup("Bugship 3"):
                reload(DS9FXSavedConfig)
                if DS9FXSavedConfig.DomIS == 1:
                        if APShip:
                                MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".AntiprotonScan", App.g_kUtopiaModule.GetGameTime() + 60, 0, 0)

                        elif APShip2:
                                MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".AntiprotonScan", App.g_kUtopiaModule.GetGameTime() + 60, 0, 0)

                        elif APShip3:
                                MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".AntiprotonScan", App.g_kUtopiaModule.GetGameTime() + 60, 0, 0)
                return


        PlayerSelection = 5
        PredefinedValue = 1

        if GetRandomRateAPScan(PredefinedValue) > PlayerSelection:
                pGame = App.Game_GetCurrentGame()
                pEpisode = pGame.GetCurrentEpisode()
                pMission = pEpisode.GetCurrentMission()
                pPlayer = MissionLib.GetPlayer()
                pSet = GammaSet
                pFriendlies = pMission.GetFriendlyGroup()
                lpFriendlies = pFriendlies.GetActiveObjectTupleInSet(pSet)
                for pFriendlies in lpFriendlies:
                        APChance = App.g_kSystemWrapper.GetRandomNumber(99) + 1
                        pTargetattr	= App.ShipClass_Cast(pFriendlies)
                        if (pTargetattr.IsCloaked()):
                                if (APChance < 80):
                                        BuildFirepoint(pTargetattr)
                                else:
                                        pass

        else:
                pPlayer = MissionLib.GetPlayer()
                APChance = App.g_kSystemWrapper.GetRandomNumber(99) + 1
                if pPlayer.IsCloaked():
                        if (APChance < 80):
                                BuildFirepoint(pPlayer)
                                PlayerDetected()

                else:
                        pass

        reload(DS9FXSavedConfig)
        if DS9FXSavedConfig.DomIS == 1:
                if APShip:
                        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".AntiprotonScan", App.g_kUtopiaModule.GetGameTime() + 60, 0, 0)

                elif APShip2:
                        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".AntiprotonScan", App.g_kUtopiaModule.GetGameTime() + 60, 0, 0)

                elif APShip3:
                        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".AntiprotonScan", App.g_kUtopiaModule.GetGameTime() + 60, 0, 0)

def BuildFirepoint(pObject):
        global Firepoint, CloakedShipSet, CloakedShipName, FirepointValue, AttachTimer, GetFirepoint

        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        Firepoint = "Sensor Anomaly"

        CloakedShipSet = pObject.GetContainingSet()

        CreateFirepoint = loadspacehelper.CreateShip(DS9FXShips.Distortion, CloakedShipSet, Firepoint, None)
        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Firepoint)
        pMission.GetFriendlyGroup().AddName(Firepoint)

        GetFirepoint = MissionLib.GetShip(Firepoint, CloakedShipSet)
        GetFirepoint.SetTargetable(1)
        GetFirepoint.SetInvincible(1)
        GetFirepoint.SetHurtable(0)
        GetFirepoint.SetCollisionsOn(0)
        pObject.AttachObject(GetFirepoint)

        FirepointValue = pObject

        CloakedShip = App.ShipClass_Cast(pObject)

        CloakedShipName = None
        CloakedShipName = CloakedShip.GetName()

        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_DECLOAK_BEGINNING, pMission, __name__ + ".ObjectDecloaking")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")

        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".DeleteFirepoint", App.g_kUtopiaModule.GetGameTime() + 40, 0, 0)

        AttachTimer = MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".AttachFirepoint", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)

def DeleteFirepoint(pObject, pEvent):
        global Firepoint, CloakedShipSet

        try:
                CloakedShipSet.RemoveObjectFromSet(Firepoint)
        except:
                pass

def GetRandomRateAPScan(iNumber):
        return App.g_kSystemWrapper.GetRandomNumber(9) + iNumber

def ObjectDecloaking(pObject, pEvent):
        global CloakedShipName, FirepointValue

        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if (pShip == None):
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)
                return

        ShipName = pShip.GetName()

        if (ShipName == CloakedShipName):
                DeleteFirepoint(None, None)
                FirepointValue.SetTargetable(1)

                App.g_kEventManager.RemoveBroadcastHandler(App.ET_DECLOAK_BEGINNING, pMission, __name__ + ".ObjectDecloaking")

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def ObjectExploding(pObject, pEvent):
        global CloakedShipName, FirepointValue

        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if (pShip == None):
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)
                return

        ShipName = pShip.GetName()

        if (ShipName == CloakedShipName):
                DeleteFirepoint(None, None)
                FirepointValue.SetTargetable(1)

                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def AttachFirepoint(pObject, pEvent):
        global FirepointValue, AttachTimer, GetFirepoint

        try:
                FirepointValue.AttachObject(GetFirepoint)
        except:
                pass

        AttachTimer = MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".AttachFirepoint", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)

def FelixWarnPrompt(pObject = None, pEvent = None):
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        Database = pMission.SetDatabase("data/TGL/DS9FXDialogueDatabase.tgl")
        pSequence = App.TGSequence_Create()
        pSet = App.g_kSetManager.GetSet("bridge")
        pTactical = App.CharacterClass_GetObject(pSet, "Tactical")
        pSequence.AppendAction(App.CharacterAction_Create(pTactical, App.CharacterAction.AT_SAY_LINE, "WarnPrompt", None, 0, Database))
        pSequence.Play()

def ImpulsePrompt(pObject = None, pEvent = None):
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        Database = pMission.SetDatabase("data/TGL/DS9FXDialogueDatabase.tgl")
        pSequence = App.TGSequence_Create()
        pSet = App.g_kSetManager.GetSet("bridge")
        pEng = App.CharacterClass_GetObject(pSet, "Engineer")
        pSequence.AppendAction(App.CharacterAction_Create(pEng, App.CharacterAction.AT_SAY_LINE, "Impulse", None, 0, Database))
        pSequence.Play()

def DisableWarpButton():
        Bridge.BridgeUtils.DisableButton(None, "Helm", "Set Course")
        Bridge.BridgeUtils.DisableWarpButton()

def RestoreWarpButton():
        Bridge.BridgeUtils.EnableButton(None, "Helm", "Set Course")
        Bridge.BridgeUtils.RestoreWarpButton()

def GetRandomRate(iNumber):
        return App.g_kSystemWrapper.GetRandomNumber(150) + iNumber

def EnemyFleetArrives(pObject, pEvent):
        global RandomEnemyFleet, RandomAttackTimer

        reload(DS9FXSavedConfig)
        if DS9FXSavedConfig.DominionTimeSpan == 1:
                RandomEnemyFleet = App.g_kSystemWrapper.GetRandomNumber(120) + 240
        elif DS9FXSavedConfig.DominionTimeSpan == 2:
                RandomEnemyFleet = App.g_kSystemWrapper.GetRandomNumber(120) + 360
        elif DS9FXSavedConfig.DominionTimeSpan == 3:
                RandomEnemyFleet = App.g_kSystemWrapper.GetRandomNumber(479) + 1                
        else:
                RandomEnemyFleet = App.g_kSystemWrapper.GetRandomNumber(120) + 120

        pPlayer = App.Game_GetCurrentPlayer()
        if not pPlayer:
                return 0

        pSet = pPlayer.GetContainingSet()
        if (pSet.GetName() == "DeepSpace91"):
                pGame = App.Game_GetCurrentGame()
                pEpisode = pGame.GetCurrentEpisode()
                pMission = pEpisode.GetCurrentMission()
                Database = pMission.SetDatabase("data/TGL/DS9FXDialogueDatabase.tgl")
                pSequence = App.TGSequence_Create()
                pSet = App.g_kSetManager.GetSet("bridge")
                pTactical = App.CharacterClass_GetObject(pSet, "Tactical")
                pSequence.AppendAction(App.CharacterAction_Create(pTactical, App.CharacterAction.AT_SAY_LINE, "EnemiesEnteringTheSet", None, 0, Database))
                pSequence.Play()

                from Custom.DS9FX.DS9FXObjects import DS9RandomAttackFleet

                DS9RandomAttackFleet.DS9SetEnemyShips()

                RandomAttackTimer = DS9FXLib.DS9FXMenuLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".EnemyFleetArrives", App.g_kUtopiaModule.GetGameTime() + RandomEnemyFleet)

        else:
                RandomAttackTimer = DS9FXLib.DS9FXMenuLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".EnemyFleetArrives", App.g_kUtopiaModule.GetGameTime() + RandomEnemyFleet)

def DeleteRandomAttackTimer(pObject, pEvent):
        global RandomAttackTimer

        try:
                App.g_kTimerManager.DeleteTimer(RandomAttackTimer.GetObjID())
                App.g_kRealtimeTimerManager.DeleteTimer(RandomAttackTimer.GetObjID())
                RandomAttackTimer = None
        except:
                pass

def DockToDS9(pObject, pEvent):
        pPlayer = App.Game_GetCurrentPlayer()

        if (pPlayer is None):
                return 0

        pDS9 = GetDS9(pPlayer)

        if (pDS9 is None):
                return 0

        pDockingAction = None

        import Custom.DS9FX.DS9FXAILib.DS9FXDockToDS9
        MissionLib.SetPlayerAI("Helm", Custom.DS9FX.DS9FXAILib.DS9FXDockToDS9.CreateAI(pPlayer, pDS9, pDockingAction, bNoRepair = 0, bFadeEnd = 1))

def GetDS9(pShip):
        if pShip:
                pDS9Set = pShip.GetContainingSet()

                if(pDS9Set is None):
                        return None

                pDS9Base = MissionLib.GetShip("Deep_Space_9", pDS9Set)

                if(pDS9Base is None):
                        return None

                return pDS9Base

        else:
                return None

def DisableEngineerMenu():
        DetachMenus(None, None)

        pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
        pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
        pMenu = pTacticalControlWindow.FindMenu(pDatabase.GetString("Engineer"))
        App.g_kLocalizationManager.Unload(pDatabase)

        pMenu.SetDisabled()

def EnableEngineerMenu():
        ReatachMenus(None, None)

        pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
        pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
        pMenu = pTacticalControlWindow.FindMenu(pDatabase.GetString("Engineer"))
        App.g_kLocalizationManager.Unload(pDatabase)

        pMenu.SetEnabled()

def DeleteAllDS9FXTimers():
        DS9FXLib.DS9FXMenuLib.DeleteAllTimers()

def DeleteScaleWormholeTimer():
        global ScaleWormhole
        DS9FXLib.DS9FXMenuLib.DeleteTimer(ScaleTimer)

def PlayerDetected(pObject = None, pEvent = None):
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        Database = pMission.SetDatabase("data/TGL/DS9FXDialogueDatabase.tgl")
        pSequence = App.TGSequence_Create()
        pSet = App.g_kSetManager.GetSet("bridge")
        pXO = App.CharacterClass_GetObject(pSet, "XO")
        pSequence.AppendAction(App.CharacterAction_Create(pXO, App.CharacterAction.AT_SAY_LINE, "CloakDetect", None, 0, Database))
        pSequence.Play()

def DetachMenus(pObject, pEvent):
        pSet = App.g_kSetManager.GetSet("bridge")
        pEngineer = App.CharacterClass_Cast(pSet.GetObject("Engineer"))
        pScience = App.CharacterClass_Cast(pSet.GetObject("Science"))
        pXO = App.CharacterClass_Cast(pSet.GetObject("XO"))
        pTactical = App.CharacterClass_Cast(pSet.GetObject("Tactical"))
        pHelm = App.CharacterClass_Cast(pSet.GetObject("Helm"))

        if pEngineer:
                import Bridge.EngineerCharacterHandlers
                Bridge.EngineerCharacterHandlers.DetachMenuFromEngineer(pEngineer)

def ReatachMenus(pObject, pEvent):
        pSet = App.g_kSetManager.GetSet("bridge")
        pEngineer = App.CharacterClass_Cast(pSet.GetObject("Engineer"))
        pScience = App.CharacterClass_Cast(pSet.GetObject("Science"))
        pXO = App.CharacterClass_Cast(pSet.GetObject("XO"))
        pTactical = App.CharacterClass_Cast(pSet.GetObject("Tactical"))
        pHelm = App.CharacterClass_Cast(pSet.GetObject("Helm"))

        if pEngineer:
                import Bridge.EngineerCharacterHandlers
                Bridge.EngineerCharacterHandlers.AttachMenuToEngineer(pEngineer)

def DeleteDummy(pObject, pEvent):
        global Dummy, pPlayer

        NewPlayer = App.Game_GetCurrentPlayer()
        if not NewPlayer:
                return 0

        NewSet = NewPlayer.GetContainingSet()

        NewSet.RemoveObjectFromSet(Dummy)

        pGame = App.Game_GetCurrentGame()
        pGame.SetPlayer(pPlayer)

def RemoveKeyboardControl(pAction = None):
        pTopWindow = App.TopWindow_GetTopWindow()
        if (pTopWindow == None):
                return None

        pTopWindow.SetNotVisible()

        pTopWindow.DisableOptionsMenu(1)
        pTopWindow.AllowKeyboardInput(0)
        pTopWindow.AllowMouseInput(0)

        return 0

def ReturnKeyboardControl(pAction = None):
        pTopWindow = App.TopWindow_GetTopWindow()
        if (pTopWindow == None):
                return None

        pTopWindow.SetVisible()

        pTopWindow.DisableOptionsMenu(0)
        pTopWindow.AllowKeyboardInput(1)
        pTopWindow.AllowMouseInput(1)

        return 0

def HailDS9(pObject, pEvent):
        Player = App.Game_GetCurrentPlayer()
        if not Player:
                return 0

        Set = Player.GetContainingSet()

        pDS9 = MissionLib.GetShip("Deep_Space_9", Set)

        if not pDS9:
                return 0

        if DistanceCheck(pDS9) > 900:
                FelixWarnPrompt()
                print "DS9FX: To far out to Hail DS9!"
                return

        pSequence = MissionLib.NewDialogueSequence()
        pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOn", "KiraSet", "Kira", 200)
        pSequence.AppendAction(pAction)
        MissionLib.QueueActionToPlay(pSequence)

        ForceCamOn()

        pSequence2 = MissionLib.NewDialogueSequence()
        pSequence2.AppendAction(App.TGScriptAction_Create(__name__, "MenuUp"))
        pSequence2.Play()

        WelcomeToDS9Line()

def ForceCamOn():
        pBridge = App.BridgeSet_Cast(App.g_kSetManager.GetSet("bridge"))
        pLookAtSet = App.g_kSetManager.GetSet("KiraSet")
        pMainCamera = pLookAtSet.GetCamera("maincamera")
        if (pBridge):
                pViewScreen = pBridge.GetViewScreen()
                if (pViewScreen):
                        pViewScreen.SetRemoteCam(pMainCamera)
                        pViewScreen.SetIsOn(1)

def MenuUp(pAction):
        pKiraSet = App.g_kSetManager.GetSet("KiraSet")
        pKira = App.CharacterClass_GetObject (pKiraSet, "Kira")

        pAction = App.CharacterAction_Create(pKira, App.CharacterAction.AT_MENU_UP)
        pAction.Play()

        return 0

def MenuClose(pAction):
        pKiraSet = App.g_kSetManager.GetSet("KiraSet")
        pKira = App.CharacterClass_GetObject (pKiraSet, "Kira")

        pAction = App.CharacterAction_Create(pKira, App.CharacterAction.AT_MENU_DOWN)
        pAction.Play()

        return 0

def WelcomeToDS9Line(pObject = None, pEvent = None):
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        Database = pMission.SetDatabase("data/TGL/DS9FXDialogueDatabase.tgl")
        pSequence = App.TGSequence_Create()
        pKiraSet = App.g_kSetManager.GetSet("KiraSet")
        pKira = App.CharacterClass_GetObject (pKiraSet, "Kira")
        pKira.SetCharacterName("Kira")
        pSequence.AppendAction(App.CharacterAction_Create(pKira, App.CharacterAction.AT_SAY_LINE, "welcome", None, 0, Database))
        pSequence.Play()

def CreateBridgeMenuButton(pName, eType, iSubType, pCharacter):
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(eType)
        pEvent.SetDestination(pCharacter)
        pEvent.SetInt(iSubType)
        BridgeMenuButton = App.STButton_CreateW(pName, pEvent)
        return BridgeMenuButton

def ChooseCampaign(pObject, pEvent):
        RemoveWindowContents(None, None)
        CreateWindowPartII(None, None)
        Window(None, None)

def ChooseMiniMission(pObject, pEvent):
        RemoveWindow2Contents(None, None)
        CreateWindow2PartII(None, None)
        Window2(None, None)

def ChooseHistoric(pObject, pEvent):
        RemoveWindow3Contents(None, None)
        CreateWindow3PartII(None, None)
        Window3(None, None)

def ChooseCampaign2(pObject, pEvent):
        RemoveWindow4Contents(None, None)
        CreateWindow4PartII(None, None)
        Window4(None, None)

def RemoveWindowContents(pObject, pEvent):
        global MissionWindow, dBorderSkirmish

        if MissionWindow:
                for k in dBorderSkirmish.keys():
                        MissionWindow.DeleteChild(dBorderSkirmish[k])

        dBorderSkirmish = {}

def RemoveWindow2Contents(pObject, pEvent):
        global MissionWindow2, dMiniMission

        if MissionWindow2:
                for k in dMiniMission.keys():
                        MissionWindow2.DeleteChild(dMiniMission[k])

        dMiniMission = {}

def RemoveWindow3Contents(pObject, pEvent):
        global MissionWindow3, dHistoric

        if MissionWindow3:
                for k in dHistoric.keys():
                        MissionWindow3.DeleteChild(dHistoric[k])

        dHistoric = {}

def RemoveWindow4Contents(pObject, pEvent):
        global MissionWindow4, dOldRivals

        if MissionWindow4:
                for k in dOldRivals.keys():
                        MissionWindow4.DeleteChild(dOldRivals[k])

        dOldRivals = {}

def CloseChannelRedirect(pObject, pEvent):
        CloseChannel(None, None)

def CloseChannel(pObject, pEvent):
        CloseChannels(None, None)

        pSeq = MissionLib.NewDialogueSequence()
        pAction = App.TGScriptAction_Create(__name__, "MenuClose")
        pSeq.AppendAction(pAction)
        pSeq.Play()

        ChannelClosing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def ChannelClosing():
        pSeq = MissionLib.NewDialogueSequence()
        pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
        pSeq.AppendAction(pAction)
        MissionLib.QueueActionToPlay(pSeq)

        ForceCamOff()

def ForceCamOff():
        pGame = App.Game_GetCurrentGame()
        if not pGame:
                return 0
        pCamera = pGame.GetPlayerCamera()
        if not pCamera:
                return 0

        pBridge = App.BridgeSet_Cast(App.g_kSetManager.GetSet("bridge"))
        if (pBridge):
                pViewScreen = pBridge.GetViewScreen()
                if (pViewScreen):
                        pViewScreen.SetRemoteCam(pCamera)
                        pViewScreen.SetIsOn(1)

                        if (pViewScreen.IsStaticOn()):
                                pViewScreen.SetStaticIsOn(0)

def CreateWindow(pObject, pEvent):
        global MissionWindow

        kColor = App.TGColorA()
        kColor.SetRGBA(1, 0.81, 0.41, 1.0)

        MissionWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Campaign Mission Selection Menu"), 0.0, 0.0, None, 1, 0.50, 0.65, kColor)
        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
        pTCW.AddChild(MissionWindow, 0.25, 0.25)

        MissionWindow.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__ + ".MousePass")
        MissionWindow.SetNotVisible()

        CreateWindowPartII(None, None)

def CreateWindow2(pObject, pEvent):
        global MissionWindow2

        kColor = App.TGColorA()
        kColor.SetRGBA(1, 0.81, 0.41, 1.0)

        MissionWindow2 = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Mini Mission Selection Menu"), 0.0, 0.0, None, 1, 0.50, 0.65, kColor)
        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
        pTCW.AddChild(MissionWindow2, 0.25, 0.25)

        MissionWindow2.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__ + ".MousePass")
        MissionWindow2.SetNotVisible()

        CreateWindow2PartII(None, None)

def CreateWindow3(pObject, pEvent):
        global MissionWindow3

        kColor = App.TGColorA()
        kColor.SetRGBA(1, 0.81, 0.41, 1.0)

        MissionWindow3 = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Historic Mission Selection Menu"), 0.0, 0.0, None, 1, 0.50, 0.65, kColor)
        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
        pTCW.AddChild(MissionWindow3, 0.25, 0.25)

        MissionWindow3.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__ + ".MousePass")
        MissionWindow3.SetNotVisible()

        CreateWindow3PartII(None, None)

def CreateWindow4(pObject, pEvent):
        global MissionWindow4

        kColor = App.TGColorA()
        kColor.SetRGBA(1, 0.81, 0.41, 1.0)

        MissionWindow4 = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Campaign Mission Selection Menu"), 0.0, 0.0, None, 1, 0.50, 0.65, kColor)
        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
        pTCW.AddChild(MissionWindow4, 0.25, 0.25)

        MissionWindow4.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__ + ".MousePass")
        MissionWindow4.SetNotVisible()

        CreateWindow4PartII(None, None)

def MousePass(Window, pEvent):
        if Window and pEvent:
                Window.CallNextHandler(pEvent)

        if pEvent.EventHandled() == 0:
                pEvent.SetHandled()

def CreateWindowPartII(pObject, pEvent):
        global ET_WINDOW_CLOSE, ET_BORDER_SKIRMISH_1, ET_BORDER_SKIRMISH_2, ET_BORDER_SKIRMISH_3, ET_BORDER_SKIRMISH_4
        global ET_BORDER_SKIRMISH_5, ET_BACK, MissionWindow, pPerson, ET_UNAVAILABLE
        global dBorderSkirmish

        try:
                pConfig = __import__("DS9FXMissions.CampaignMode.BorderSkirmish.Save.defaultsavedconfig")
                Ship = pConfig.Ship
                if Ship == None:
                        pass
                else:
                        print "DS9FX: This isn't an authentic DS9FX Saved Config, destroying Campaign Selection Menu!"
                        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".CloseChannels", App.g_kUtopiaModule.GetGameTime() + 0.1, 0, 0)
                        return
                MissionProgress = 1
        except:
                pass
        try:
                pConfig2 = __import__("DS9FXMissions.CampaignMode.BorderSkirmish.Save.mission2")
                MissionProgress = 2
        except:
                pass
        try:
                pConfig3 = __import__("DS9FXMissions.CampaignMode.BorderSkirmish.Save.mission3")
                MissionProgress = 3
        except:
                pass
        try:
                pConfig4 = __import__("DS9FXMissions.CampaignMode.BorderSkirmish.Save.mission4")
                MissionProgress = 4
        except:
                pass
        try:
                pConfig5 = __import__("DS9FXMissions.CampaignMode.BorderSkirmish.Save.mission5")
                MissionProgress = 5
        except:
                pass

        x = 0
        y = 0.01
        dBorderSkirmish['6'] = App.TGParagraph_CreateW(App.TGString("Please Select a Mission. Remember that the Campaign Mode remembers your last used ship and you cannot switch ships later. Missions have to be unlocked one by one."), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow.AddChild(dBorderSkirmish['6'], x, y, 0)

        textx = 0
        texty = 0.10
        dBorderSkirmish['1'] = App.TGParagraph_CreateW(App.TGString("Mission 1: Patrol Duty"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow.AddChild(dBorderSkirmish['1'], textx, texty, 0)

        x = 0.35
        y = y + 0.08
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_BORDER_SKIRMISH_1)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dBorderSkirmish['7'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow.AddChild(dBorderSkirmish['7'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dBorderSkirmish['2'] = App.TGParagraph_CreateW(App.TGString("Mission 2: Investigations"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow.AddChild(dBorderSkirmish['2'], textx, texty, 0)
        if MissionProgress < 2:
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_UNAVAILABLE)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dBorderSkirmish['8'] = CreateWindowButton(pEvent, "Mission Locked", 1)
                MissionWindow.AddChild(dBorderSkirmish['8'], x, y, 0)
        else:
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_BORDER_SKIRMISH_2)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dBorderSkirmish['8'] = CreateWindowButton(pEvent, "Mission Briefing")
                MissionWindow.AddChild(dBorderSkirmish['8'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dBorderSkirmish['3'] = App.TGParagraph_CreateW(App.TGString("Mission 3: A Time To Fight"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow.AddChild(dBorderSkirmish['3'], textx, texty, 0)
        if MissionProgress < 3:
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_UNAVAILABLE)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dBorderSkirmish['9'] = CreateWindowButton(pEvent, "Mission Locked", 1)
                MissionWindow.AddChild(dBorderSkirmish['9'], x, y, 0)
        else:
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_BORDER_SKIRMISH_3)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dBorderSkirmish['9'] = CreateWindowButton(pEvent, "Mission Briefing")
                MissionWindow.AddChild(dBorderSkirmish['9'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dBorderSkirmish['4'] = App.TGParagraph_CreateW(App.TGString("Mission 4: Revenge Is A Dish Best Served Cold"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow.AddChild(dBorderSkirmish['4'], textx, texty, 0)
        if MissionProgress < 4:
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_UNAVAILABLE)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dBorderSkirmish['10'] = CreateWindowButton(pEvent, "Mission Locked", 1)
                MissionWindow.AddChild(dBorderSkirmish['10'], x, y, 0)
        else:
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_BORDER_SKIRMISH_4)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dBorderSkirmish['10'] = CreateWindowButton(pEvent, "Mission Briefing")
                MissionWindow.AddChild(dBorderSkirmish['10'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dBorderSkirmish['5'] = App.TGParagraph_CreateW(App.TGString("Mission 5: Once More Unto The Breach"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow.AddChild(dBorderSkirmish['5'], textx, texty, 0)
        if MissionProgress < 5:
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_UNAVAILABLE)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dBorderSkirmish['11'] = CreateWindowButton(pEvent, "Mission Locked", 1)
                MissionWindow.AddChild(dBorderSkirmish['11'], x, y, 0)
        else:
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_BORDER_SKIRMISH_5)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dBorderSkirmish['11'] = CreateWindowButton(pEvent, "Mission Briefing")
                MissionWindow.AddChild(dBorderSkirmish['11'], x, y, 0)

        x = 0
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_BACK)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dBorderSkirmish['12'] = CreateWindowButton(pEvent, "Back To Main Menu")
        MissionWindow.AddChild(dBorderSkirmish['12'], x, y, 0)

        x = 0
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_WINDOW_CLOSE)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dBorderSkirmish['13'] = CreateWindowButton(pEvent, "Close Channel")
        MissionWindow.AddChild(dBorderSkirmish['13'], x, y, 0)

        MissionWindow.InteriorChangedSize()
        MissionWindow.Layout()

def CreateWindow2PartII(pObject, pEvent):
        global ET_BACK, pPerson, ET_MINI_MISSION_1, ET_MINI_MISSION_2, MissionWindow2, ET_WINDOW_CLOSE_2, ET_MINI_MISSION_3
        global ET_MINI_MISSION_4, ET_MINI_MISSION_5, ET_MINI_MISSION_6, ET_MINI_MISSION_7, ET_MINI_MISSION_8, ET_MINI_MISSION_9
        global ET_MINI_MISSION_10, ET_MINI_MISSION_11, ET_MINI_MISSION_12, ET_MINI_MISSION_13, ET_MINI_MISSION_14, ET_MINI_MISSION_15
        global ET_MINI_MISSION_16, ET_MINI_MISSION_17, ET_MINI_MISSION_18, ET_MINI_MISSION_19, ET_MINI_MISSION_20, ET_MINI_MISSION_21
        global dMiniMission, ET_MINI_MISSION_22, ET_RANDOM_MISSION_1, ET_RANDOM_MISSION_2

        kNormalColor = App.TGColorA()
        kNormalColor.SetRGBA(0.8, 0.6, 0.8, 1.0)
        kHilightedColor = App.TGColorA()
        kHilightedColor.SetRGBA(0.92, 0.76, 0.92, 1.0)
        kDisabledColor = App.TGColorA()
        kDisabledColor.SetRGBA(0.25, 0.25, 0.25, 1.0)

        x = 0
        y = 0.01
        dMiniMission['1'] = App.TGParagraph_CreateW(App.TGString("Please Select a Mission. Unlike Campaign Mode you can freely pick any ship you wish! These are just small missions for fun."), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow2.AddChild(dMiniMission['1'], x, y, 0)

        textx = 0
        texty = 0.10
        dMiniMission['2'] = App.TGParagraph_CreateW(App.TGString("Mission: Procure Ketracel White"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow2.AddChild(dMiniMission['2'], textx, texty, 0)

        x = 0.35
        y = y + 0.08
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_MINI_MISSION_1)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dMiniMission['8'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow2.AddChild(dMiniMission['8'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dMiniMission['3'] = App.TGParagraph_CreateW(App.TGString("Mission: Anomalous Readings"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow2.AddChild(dMiniMission['3'], textx, texty, 0)

        x = 0.35
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_MINI_MISSION_2)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dMiniMission['12'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow2.AddChild(dMiniMission['12'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dMiniMission['4'] = App.TGParagraph_CreateW(App.TGString("Mission: The tides of Idran"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow2.AddChild(dMiniMission['4'], textx, texty, 0)

        x = 0.35
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_MINI_MISSION_3)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dMiniMission['11'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow2.AddChild(dMiniMission['11'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dMiniMission['5'] = App.TGParagraph_CreateW(App.TGString("Mission: The Dogs of War"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow2.AddChild(dMiniMission['5'], textx, texty, 0)

        x = 0.35
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_MINI_MISSION_4)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dMiniMission['13'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow2.AddChild(dMiniMission['13'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dMiniMission['6'] = App.TGParagraph_CreateW(App.TGString("Mission: Valiant"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow2.AddChild(dMiniMission['6'], textx, texty, 0)

        x = 0.35
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_MINI_MISSION_5)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dMiniMission['14'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow2.AddChild(dMiniMission['14'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dMiniMission['7'] = App.TGParagraph_CreateW(App.TGString("Mission: Section 31"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow2.AddChild(dMiniMission['7'], textx, texty, 0)

        x = 0.35
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_MINI_MISSION_6)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dMiniMission['15'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow2.AddChild(dMiniMission['15'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dMiniMission['16'] = App.TGParagraph_CreateW(App.TGString("Mission: Secret Weapon"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow2.AddChild(dMiniMission['16'], textx, texty, 0)

        x = 0.35
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_MINI_MISSION_7)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dMiniMission['17'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow2.AddChild(dMiniMission['17'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dMiniMission['18'] = App.TGParagraph_CreateW(App.TGString("Mission: Rebels"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow2.AddChild(dMiniMission['18'], textx, texty, 0)

        x = 0.35
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_MINI_MISSION_8)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dMiniMission['19'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow2.AddChild(dMiniMission['19'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dMiniMission['20'] = App.TGParagraph_CreateW(App.TGString("Mission: Supplies"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow2.AddChild(dMiniMission['20'], textx, texty, 0)

        x = 0.35
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_MINI_MISSION_9)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dMiniMission['21'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow2.AddChild(dMiniMission['21'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dMiniMission['22'] = App.TGParagraph_CreateW(App.TGString("Mission: Black OPS"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow2.AddChild(dMiniMission['22'], textx, texty, 0)

        x = 0.35
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_MINI_MISSION_10)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dMiniMission['23'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow2.AddChild(dMiniMission['23'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dMiniMission['24'] = App.TGParagraph_CreateW(App.TGString("Mission: Disturbing Times"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow2.AddChild(dMiniMission['24'], textx, texty, 0)

        x = 0.35
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_MINI_MISSION_11)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dMiniMission['25'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow2.AddChild(dMiniMission['25'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dMiniMission['26'] = App.TGParagraph_CreateW(App.TGString("Mission: Section 31 Surprise"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow2.AddChild(dMiniMission['26'], textx, texty, 0)

        x = 0.35
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_MINI_MISSION_12)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dMiniMission['27'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow2.AddChild(dMiniMission['27'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dMiniMission['28'] = App.TGParagraph_CreateW(App.TGString("Mission: Dominion Intelligence"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow2.AddChild(dMiniMission['28'], textx, texty, 0)

        x = 0.35
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_MINI_MISSION_13)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dMiniMission['29'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow2.AddChild(dMiniMission['29'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dMiniMission['30'] = App.TGParagraph_CreateW(App.TGString("Mission: Patrol"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow2.AddChild(dMiniMission['30'], textx, texty, 0)

        x = 0.35
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_MINI_MISSION_14)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dMiniMission['31'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow2.AddChild(dMiniMission['31'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dMiniMission['32'] = App.TGParagraph_CreateW(App.TGString("Mission: Distress Call"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow2.AddChild(dMiniMission['32'], textx, texty, 0)

        x = 0.35
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_MINI_MISSION_15)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dMiniMission['33'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow2.AddChild(dMiniMission['33'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dMiniMission['34'] = App.TGParagraph_CreateW(App.TGString("Mission: Dominion Bases"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow2.AddChild(dMiniMission['34'], textx, texty, 0)

        x = 0.35
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_MINI_MISSION_16)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dMiniMission['35'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow2.AddChild(dMiniMission['35'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dMiniMission['36'] = App.TGParagraph_CreateW(App.TGString("Mission: Recover Derelict"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow2.AddChild(dMiniMission['36'], textx, texty, 0)

        x = 0.35
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_MINI_MISSION_17)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dMiniMission['37'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow2.AddChild(dMiniMission['37'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dMiniMission['38'] = App.TGParagraph_CreateW(App.TGString("Mission: Stop the War"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow2.AddChild(dMiniMission['38'], textx, texty, 0)

        x = 0.35
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_MINI_MISSION_18)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dMiniMission['39'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow2.AddChild(dMiniMission['39'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dMiniMission['40'] = App.TGParagraph_CreateW(App.TGString("Mission: Assistance"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow2.AddChild(dMiniMission['40'], textx, texty, 0)

        x = 0.35
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_MINI_MISSION_19)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dMiniMission['41'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow2.AddChild(dMiniMission['41'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dMiniMission['42'] = App.TGParagraph_CreateW(App.TGString("Mission: Scan"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow2.AddChild(dMiniMission['42'], textx, texty, 0)

        x = 0.35
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_MINI_MISSION_20)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dMiniMission['43'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow2.AddChild(dMiniMission['43'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dMiniMission['44'] = App.TGParagraph_CreateW(App.TGString("Mission: Missing Ship"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow2.AddChild(dMiniMission['44'], textx, texty, 0)

        x = 0.35
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_MINI_MISSION_21)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dMiniMission['45'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow2.AddChild(dMiniMission['45'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dMiniMission['46'] = App.TGParagraph_CreateW(App.TGString("Mission: Escort Service"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow2.AddChild(dMiniMission['46'], textx, texty, 0)

        x = 0.35
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_MINI_MISSION_22)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dMiniMission['47'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow2.AddChild(dMiniMission['47'], x, y, 0)   

        reload(DS9FXSavedConfig)
        if DS9FXSavedConfig.EasterEggs == 1:                        
                textx = 0
                texty = texty + 0.06
                dMiniMission['48'] = App.TGParagraph_CreateW(App.TGString("Mission: Random Dominion Mission"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                MissionWindow2.AddChild(dMiniMission['48'], textx, texty, 0)
        
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_RANDOM_MISSION_1)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dMiniMission['49'] = CreateWindowButton(pEvent, "Mission Briefing")
                MissionWindow2.AddChild(dMiniMission['49'], x, y, 0)  
                
                textx = 0
                texty = texty + 0.06
                dMiniMission['50'] = App.TGParagraph_CreateW(App.TGString("Mission: Random Borg Mission"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                MissionWindow2.AddChild(dMiniMission['50'], textx, texty, 0)
        
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_RANDOM_MISSION_2)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dMiniMission['51'] = CreateWindowButton(pEvent, "Mission Briefing")
                MissionWindow2.AddChild(dMiniMission['51'], x, y, 0) 
        
        x = 0
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_BACK)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dMiniMission['9'] = CreateWindowButton(pEvent, "Back To Main Menu")
        MissionWindow2.AddChild(dMiniMission['9'], x, y, 0)

        x = 0
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_WINDOW_CLOSE_2)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dMiniMission['10'] = CreateWindowButton(pEvent, "Close Channel")
        MissionWindow2.AddChild(dMiniMission['10'], x, y, 0)

        MissionWindow2.InteriorChangedSize()
        MissionWindow2.Layout()

def CreateWindow3PartII(pObject, pEvent):
        global ET_BACK, pPerson, ET_HISTORIC_MISSION_1, MissionWindow3, ET_WINDOW_CLOSE_3, ET_HISTORIC_MISSION_2
        global ET_HISTORIC_MISSION_3, ET_HISTORIC_MISSION_4, ET_HISTORIC_MISSION_5, ET_HISTORIC_MISSION_6
        global dHistoric

        kNormalColor = App.TGColorA()
        kNormalColor.SetRGBA(0.8, 0.6, 0.8, 1.0)
        kHilightedColor = App.TGColorA()
        kHilightedColor.SetRGBA(0.92, 0.76, 0.92, 1.0)
        kDisabledColor = App.TGColorA()
        kDisabledColor.SetRGBA(0.25, 0.25, 0.25, 1.0)

        x = 0
        y = 0.01
        dHistoric['1'] = App.TGParagraph_CreateW(App.TGString("Please Select a Mission. Historic Mission Mode pays tribute to DS9. You can play a lot of historic missions seen in the show. All missions are available to you but your ship class varies from mission to mission."), MissionWindow3.GetMaximumInteriorWidth(), None, '', MissionWindow3.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow3.AddChild(dHistoric['1'], x, y, 0)

        textx = 0
        texty = 0.12
        dHistoric['2'] = App.TGParagraph_CreateW(App.TGString("Mission: Plant the minefield"), MissionWindow3.GetMaximumInteriorWidth(), None, '', MissionWindow3.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow3.AddChild(dHistoric['2'], textx, texty, 0)

        x = 0.35
        y = y + 0.10
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_HISTORIC_MISSION_1)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dHistoric['7'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow3.AddChild(dHistoric['7'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dHistoric['3'] = App.TGParagraph_CreateW(App.TGString("Mission: Retake DS9"), MissionWindow3.GetMaximumInteriorWidth(), None, '', MissionWindow3.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow3.AddChild(dHistoric['3'], textx, texty, 0)

        x = 0.35
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_HISTORIC_MISSION_2)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dHistoric['10'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow3.AddChild(dHistoric['10'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dHistoric['4'] = App.TGParagraph_CreateW(App.TGString("Mission: USS Odyssey"), MissionWindow3.GetMaximumInteriorWidth(), None, '', MissionWindow3.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow3.AddChild(dHistoric['4'], textx, texty, 0)

        x = 0.35
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_HISTORIC_MISSION_3)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dHistoric['11'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow3.AddChild(dHistoric['11'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dHistoric['5'] = App.TGParagraph_CreateW(App.TGString("Mission: Retake DS9 (Canon)"), MissionWindow3.GetMaximumInteriorWidth(), None, '', MissionWindow3.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow3.AddChild(dHistoric['5'], textx, texty, 0)

        x = 0.35
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_HISTORIC_MISSION_4)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dHistoric['12'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow3.AddChild(dHistoric['12'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dHistoric['6'] = App.TGParagraph_CreateW(App.TGString("Mission: The Way of the Warrior"), MissionWindow3.GetMaximumInteriorWidth(), None, '', MissionWindow3.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow3.AddChild(dHistoric['6'], textx, texty, 0)

        x = 0.35
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_HISTORIC_MISSION_5)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dHistoric['13'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow3.AddChild(dHistoric['13'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dHistoric['14'] = App.TGParagraph_CreateW(App.TGString("Mission: Save Odo"), MissionWindow3.GetMaximumInteriorWidth(), None, '', MissionWindow3.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow3.AddChild(dHistoric['14'], textx, texty, 0)

        x = 0.35
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_HISTORIC_MISSION_6)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dHistoric['15'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow3.AddChild(dHistoric['15'], x, y, 0)

        x = 0
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_BACK)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dHistoric['8'] = CreateWindowButton(pEvent, "Back To Main Menu")
        MissionWindow3.AddChild(dHistoric['8'], x, y, 0)

        x = 0
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_WINDOW_CLOSE_3)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dHistoric['9'] = CreateWindowButton(pEvent, "Close Channel")
        MissionWindow3.AddChild(dHistoric['9'], x, y, 0)

        MissionWindow3.InteriorChangedSize()
        MissionWindow3.Layout()

def CreateWindow4PartII(pObject, pEvent):
        global ET_WINDOW_CLOSE_4, ET_OLD_RIVALS_1, ET_BACK, MissionWindow4, pPerson, ET_UNAVAILABLE, ET_OLD_RIVALS_2, ET_OLD_RIVALS_3
        global ET_OLD_RIVALS_4, ET_OLD_RIVALS_5, ET_OLD_RIVALS_6, ET_OLD_RIVALS_7, ET_OLD_RIVALS_8, ET_OLD_RIVALS_9, ET_OLD_RIVALS_10
        global dOldRivals

        try:
                from Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals.Save import MissionState
                reload(MissionState)
                OnMission = MissionState.OnMission
                lProgress = []
                for i in range(1, 12):
                        lProgress.append(i)
                if not OnMission in lProgress:
                        print "DS9FX: This isn't an authentic DS9FX Saved Config, destroying Campaign Selection Menu!"
                        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".CloseChannels", App.g_kUtopiaModule.GetGameTime() + 0.1, 0, 0)
                        return
                iProgress = OnMission
        except:
                iProgress = 1

        x = 0
        y = 0.01
        dOldRivals['1'] = App.TGParagraph_CreateW(App.TGString("Please Select a Mission. Remember that the Campaign Mode remembers your last used ship and you cannot switch ships later. Missions have to be unlocked one by one."), MissionWindow4.GetMaximumInteriorWidth(), None, '', MissionWindow4.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow4.AddChild(dOldRivals['1'], x, y, 0)

        textx = 0
        texty = 0.10
        dOldRivals['2'] = App.TGParagraph_CreateW(App.TGString("Mission 1: Patrol"), MissionWindow4.GetMaximumInteriorWidth(), None, '', MissionWindow4.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow4.AddChild(dOldRivals['2'], textx, texty, 0)

        x = 0.35
        y = y + 0.08
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_OLD_RIVALS_1)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dOldRivals['3'] = CreateWindowButton(pEvent, "Mission Briefing")
        MissionWindow4.AddChild(dOldRivals['3'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dOldRivals['7'] = App.TGParagraph_CreateW(App.TGString("Mission 2: Elucidate"), MissionWindow4.GetMaximumInteriorWidth(), None, '', MissionWindow4.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow4.AddChild(dOldRivals['7'], textx, texty, 0)
        if iProgress < 2:
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_UNAVAILABLE)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dOldRivals['8'] = CreateWindowButton(pEvent, "Mission Locked", 1)
                MissionWindow4.AddChild(dOldRivals['8'], x, y, 0)
        else:
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_OLD_RIVALS_2)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dOldRivals['8'] = CreateWindowButton(pEvent, "Mission Briefing")
                MissionWindow4.AddChild(dOldRivals['8'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dOldRivals['9'] = App.TGParagraph_CreateW(App.TGString("Mission 3: Duplicity"), MissionWindow4.GetMaximumInteriorWidth(), None, '', MissionWindow4.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow4.AddChild(dOldRivals['9'], textx, texty, 0)
        if iProgress < 3:
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_UNAVAILABLE)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dOldRivals['10'] = CreateWindowButton(pEvent, "Mission Locked", 1)
                MissionWindow4.AddChild(dOldRivals['10'], x, y, 0)
        else:

                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_OLD_RIVALS_3)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dOldRivals['10'] = CreateWindowButton(pEvent, "Mission Briefing")
                MissionWindow4.AddChild(dOldRivals['10'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dOldRivals['11'] = App.TGParagraph_CreateW(App.TGString("Mission 4: The Price of Betrayal"), MissionWindow4.GetMaximumInteriorWidth(), None, '', MissionWindow4.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow4.AddChild(dOldRivals['11'], textx, texty, 0)
        if iProgress < 4:
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_UNAVAILABLE)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dOldRivals['12'] = CreateWindowButton(pEvent, "Mission Locked", 1)
                MissionWindow4.AddChild(dOldRivals['12'], x, y, 0)
        else:
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_OLD_RIVALS_4)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dOldRivals['12'] = CreateWindowButton(pEvent, "Mission Briefing")
                MissionWindow4.AddChild(dOldRivals['12'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dOldRivals['13'] = App.TGParagraph_CreateW(App.TGString("Mission 5: The Mission Continues"), MissionWindow4.GetMaximumInteriorWidth(), None, '', MissionWindow4.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow4.AddChild(dOldRivals['13'], textx, texty, 0)
        if iProgress < 5:
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_UNAVAILABLE)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dOldRivals['14'] = CreateWindowButton(pEvent, "Mission Locked", 1)
                MissionWindow4.AddChild(dOldRivals['14'], x, y, 0)
        else:
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_OLD_RIVALS_5)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dOldRivals['14'] = CreateWindowButton(pEvent, "Mission Briefing")
                MissionWindow4.AddChild(dOldRivals['14'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dOldRivals['15'] = App.TGParagraph_CreateW(App.TGString("Mission 6: Equivocation"), MissionWindow4.GetMaximumInteriorWidth(), None, '', MissionWindow4.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow4.AddChild(dOldRivals['15'], textx, texty, 0)
        if iProgress < 6:
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_UNAVAILABLE)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dOldRivals['16'] = CreateWindowButton(pEvent, "Mission Locked", 1)
                MissionWindow4.AddChild(dOldRivals['16'], x, y, 0)
        else:
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_OLD_RIVALS_6)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dOldRivals['16'] = CreateWindowButton(pEvent, "Mission Briefing")
                MissionWindow4.AddChild(dOldRivals['16'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dOldRivals['17'] = App.TGParagraph_CreateW(App.TGString("Mission 7: Humdrum"), MissionWindow4.GetMaximumInteriorWidth(), None, '', MissionWindow4.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow4.AddChild(dOldRivals['17'], textx, texty, 0)
        if iProgress < 7:
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_UNAVAILABLE)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dOldRivals['18'] = CreateWindowButton(pEvent, "Mission Locked", 1)
                MissionWindow4.AddChild(dOldRivals['18'], x, y, 0)
        else:
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_OLD_RIVALS_7)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dOldRivals['18'] = CreateWindowButton(pEvent, "Mission Briefing")
                MissionWindow4.AddChild(dOldRivals['18'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dOldRivals['19'] = App.TGParagraph_CreateW(App.TGString("Mission 8: Trepidation"), MissionWindow4.GetMaximumInteriorWidth(), None, '', MissionWindow4.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow4.AddChild(dOldRivals['19'], textx, texty, 0)
        if iProgress < 8:
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_UNAVAILABLE)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dOldRivals['20'] = CreateWindowButton(pEvent, "Mission Locked", 1)
                MissionWindow4.AddChild(dOldRivals['20'], x, y, 0)
        else:
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_OLD_RIVALS_8)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dOldRivals['20'] = CreateWindowButton(pEvent, "Mission Briefing")
                MissionWindow4.AddChild(dOldRivals['20'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dOldRivals['21'] = App.TGParagraph_CreateW(App.TGString("Mission 9: Elevation"), MissionWindow4.GetMaximumInteriorWidth(), None, '', MissionWindow4.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow4.AddChild(dOldRivals['21'], textx, texty, 0)
        if iProgress < 9:
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_UNAVAILABLE)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dOldRivals['22'] = CreateWindowButton(pEvent, "Mission Locked", 1)
                MissionWindow4.AddChild(dOldRivals['22'], x, y, 0)
        else:
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_OLD_RIVALS_9)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dOldRivals['22'] = CreateWindowButton(pEvent, "Mission Briefing")
                MissionWindow4.AddChild(dOldRivals['22'], x, y, 0)

        textx = 0
        texty = texty + 0.06
        dOldRivals['23'] = App.TGParagraph_CreateW(App.TGString("Mission 10: Anticipation"), MissionWindow4.GetMaximumInteriorWidth(), None, '', MissionWindow4.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        MissionWindow4.AddChild(dOldRivals['23'], textx, texty, 0)
        if iProgress < 10:
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_UNAVAILABLE)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dOldRivals['24'] = CreateWindowButton(pEvent, "Mission Locked", 1)
                MissionWindow4.AddChild(dOldRivals['24'], x, y, 0)
        else:
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_OLD_RIVALS_10)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                dOldRivals['24'] = CreateWindowButton(pEvent, "Mission Briefing")
                MissionWindow4.AddChild(dOldRivals['24'], x, y, 0)

        x = 0
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_BACK)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dOldRivals['4'] = CreateWindowButton(pEvent, "Back To Main Menu")
        MissionWindow4.AddChild(dOldRivals['4'], x, y, 0)

        x = 0
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_WINDOW_CLOSE_4)
        pEvent.SetDestination(pPerson)
        pEvent.SetInt(0)
        dOldRivals['5'] = CreateWindowButton(pEvent, "Close Channel")
        MissionWindow4.AddChild(dOldRivals['5'], x, y, 0)

        MissionWindow4.InteriorChangedSize()
        MissionWindow4.Layout()

def CreateWindowButton(pEvent, sText, bDisabled = 0):
        kNormalColor = App.TGColorA()
        kNormalColor.SetRGBA(0.8, 0.6, 0.8, 1.0)
        kHilightedColor = App.TGColorA()
        kHilightedColor.SetRGBA(0.92, 0.76, 0.92, 1.0)
        kDisabledColor = App.TGColorA()
        kDisabledColor.SetRGBA(0.25, 0.25, 0.25, 1.0)

        if bDisabled:
                pButton = App.STRoundedButton_CreateW(App.TGString(sText), pEvent, 0.13125, 0.034583)
                pButton.SetNormalColor(kDisabledColor)
                pButton.SetHighlightedColor(kDisabledColor)
                pButton.SetSelectedColor(kDisabledColor)
                pButton.SetDisabledColor(kDisabledColor)
                pButton.SetColorBasedOnFlags()
        else:
                pButton = App.STRoundedButton_CreateW(App.TGString(sText), pEvent, 0.13125, 0.034583)
                pButton.SetNormalColor(kNormalColor)
                pButton.SetHighlightedColor(kHilightedColor)
                pButton.SetSelectedColor(kNormalColor)
                pButton.SetDisabledColor(kDisabledColor)
                pButton.SetColorBasedOnFlags()

        return pButton

def Window(pObject, pEvent):
        global MissionWindow, MissionWindow2, MissionWindow3, MissionWindow4

        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()

        if not MissionWindow:
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)
                return

        if MissionWindow.IsVisible():
                if MissionWindow2.IsVisible():
                        pTCW.MoveToBack(MissionWindow2)
                        MissionWindow2.SetNotVisible()

                if MissionWindow3.IsVisible():
                        pTCW.MoveToBack(MissionWindow3)
                        MissionWindow3.SetNotVisible()

                if MissionWindow4.IsVisible():
                        pTCW.MoveToBack(MissionWindow4)
                        MissionWindow4.SetNotVisible()

                pTCW.MoveToBack(MissionWindow)
                MissionWindow.SetNotVisible()

                pSeq = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create(__name__, "MenuClose")
                pSeq.AppendAction(pAction)
                pSeq.Play()

                pSeq2 = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
                pSeq2.AppendAction(pAction)
                MissionLib.QueueActionToPlay(pSeq2)

                ForceCamOff()

        else:
                if MissionWindow2.IsVisible():
                        pTCW.MoveToBack(MissionWindow2)
                        MissionWindow2.SetNotVisible()

                if MissionWindow3.IsVisible():
                        pTCW.MoveToBack(MissionWindow3)
                        MissionWindow3.SetNotVisible()

                if MissionWindow4.IsVisible():
                        pTCW.MoveToBack(MissionWindow4)
                        MissionWindow4.SetNotVisible()

                MissionWindow.SetVisible()
                pTCW.MoveToFront(MissionWindow)
                pTCW.MoveTowardsBack(MissionWindow)

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def Window2(pObject, pEvent):
        global MissionWindow2, MissionWindow, MissionWindow3, MissionWindow4

        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()

        if not MissionWindow2:
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)
                return

        if MissionWindow2.IsVisible():
                if MissionWindow.IsVisible():
                        pTCW.MoveToBack(MissionWindow)
                        MissionWindow.SetNotVisible()

                if MissionWindow3.IsVisible():
                        pTCW.MoveToBack(MissionWindow3)
                        MissionWindow3.SetNotVisible()

                if MissionWindow4.IsVisible():
                        pTCW.MoveToBack(MissionWindow4)
                        MissionWindow4.SetNotVisible()

                pTCW.MoveToBack(MissionWindow2)
                MissionWindow2.SetNotVisible()

                pSeq = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create(__name__, "MenuClose")
                pSeq.AppendAction(pAction)
                pSeq.Play()

                pSeq2 = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
                pSeq2.AppendAction(pAction)
                MissionLib.QueueActionToPlay(pSeq2)

                ForceCamOff()


        else:
                if MissionWindow.IsVisible():
                        pTCW.MoveToBack(MissionWindow)
                        MissionWindow.SetNotVisible()

                if MissionWindow3.IsVisible():
                        pTCW.MoveToBack(MissionWindow3)
                        MissionWindow3.SetNotVisible()

                if MissionWindow4.IsVisible():
                        pTCW.MoveToBack(MissionWindow4)
                        MissionWindow4.SetNotVisible()

                MissionWindow2.SetVisible()
                pTCW.MoveToFront(MissionWindow2)
                pTCW.MoveTowardsBack(MissionWindow2)

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def Window3(pObject, pEvent):
        global MissionWindow3, MissionWindow, MissionWindow2, MissionWindow4

        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()

        if not MissionWindow3:
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)
                return

        if MissionWindow3.IsVisible():
                if MissionWindow.IsVisible():
                        pTCW.MoveToBack(MissionWindow)
                        MissionWindow.SetNotVisible()

                if MissionWindow2.IsVisible():
                        pTCW.MoveToBack(MissionWindow2)
                        MissionWindow2.SetNotVisible()

                if MissionWindow4.IsVisible():
                        pTCW.MoveToBack(MissionWindow4)
                        MissionWindow4.SetNotVisible()

                pTCW.MoveToBack(MissionWindow3)
                MissionWindow3.SetNotVisible()

                pSeq = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create(__name__, "MenuClose")
                pSeq.AppendAction(pAction)
                pSeq.Play()

                pSeq2 = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
                pSeq2.AppendAction(pAction)
                MissionLib.QueueActionToPlay(pSeq2)

                ForceCamOff()

        else:
                if MissionWindow.IsVisible():
                        pTCW.MoveToBack(MissionWindow)
                        MissionWindow.SetNotVisible()

                if MissionWindow2.IsVisible():
                        pTCW.MoveToBack(MissionWindow2)
                        MissionWindow2.SetNotVisible()

                if MissionWindow4.IsVisible():
                        pTCW.MoveToBack(MissionWindow4)
                        MissionWindow4.SetNotVisible()

                MissionWindow3.SetVisible()
                pTCW.MoveToFront(MissionWindow3)
                pTCW.MoveTowardsBack(MissionWindow3)

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def Window4(pObject, pEvent):
        global MissionWindow, MissionWindow2, MissionWindow3, MissionWindow4

        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()

        if not MissionWindow:
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)
                return

        if MissionWindow4.IsVisible():
                if MissionWindow2.IsVisible():
                        pTCW.MoveToBack(MissionWindow2)
                        MissionWindow2.SetNotVisible()

                if MissionWindow3.IsVisible():
                        pTCW.MoveToBack(MissionWindow3)
                        MissionWindow3.SetNotVisible()

                if MissionWindow.IsVisible():
                        pTCW.MoveToBack(MissionWindow)
                        MissionWindow.SetNotVisible()

                pTCW.MoveToBack(MissionWindow4)
                MissionWindow4.SetNotVisible()

                pSeq = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create(__name__, "MenuClose")
                pSeq.AppendAction(pAction)
                pSeq.Play()

                pSeq2 = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
                pSeq2.AppendAction(pAction)
                MissionLib.QueueActionToPlay(pSeq2)

                ForceCamOff()

        else:
                if MissionWindow2.IsVisible():
                        pTCW.MoveToBack(MissionWindow2)
                        MissionWindow2.SetNotVisible()

                if MissionWindow3.IsVisible():
                        pTCW.MoveToBack(MissionWindow3)
                        MissionWindow3.SetNotVisible()

                if MissionWindow.IsVisible():
                        pTCW.MoveToBack(MissionWindow)
                        MissionWindow.SetNotVisible()

                MissionWindow4.SetVisible()
                pTCW.MoveToFront(MissionWindow4)
                pTCW.MoveTowardsBack(MissionWindow4)

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def CloseWindow(pObject, pEvent):
        global MissionWindow

        if not MissionWindow:
                return

        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
        if MissionWindow.IsVisible():
                pTCW.MoveToBack(MissionWindow)
                MissionWindow.SetNotVisible()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def CloseWindow2(pObject, pEvent):
        global MissionWindow2

        if not MissionWindow2:
                return

        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
        if MissionWindow2.IsVisible():
                pTCW.MoveToBack(MissionWindow2)
                MissionWindow2.SetNotVisible()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def CloseWindow3(pObject, pEvent):
        global MissionWindow3

        if not MissionWindow3:
                return

        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
        if MissionWindow3.IsVisible():
                pTCW.MoveToBack(MissionWindow3)
                MissionWindow3.SetNotVisible()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def CloseWindow4(pObject, pEvent):
        global MissionWindow3

        if not MissionWindow4:
                return

        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
        if MissionWindow4.IsVisible():
                pTCW.MoveToBack(MissionWindow4)
                MissionWindow4.SetNotVisible()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def CloseChannels(pObject, pEvent):
        global MissionWindow, MissionWindow2, MissionWindow3, MissionWindow4

        if MissionWindow:
                pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
                if MissionWindow.IsVisible():
                        pTCW.MoveToBack(MissionWindow)
                        MissionWindow.SetNotVisible()

        if MissionWindow2:
                pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
                if MissionWindow2.IsVisible():
                        pTCW.MoveToBack(MissionWindow2)
                        MissionWindow2.SetNotVisible()

        if MissionWindow3:
                pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
                if MissionWindow3.IsVisible():
                        pTCW.MoveToBack(MissionWindow3)
                        MissionWindow3.SetNotVisible()

        if MissionWindow4:
                pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
                if MissionWindow4.IsVisible():
                        pTCW.MoveToBack(MissionWindow4)
                        MissionWindow4.SetNotVisible()

def RecallMissionMenu():
        pTop = App.TopWindow_GetTopWindow()
        pTop.ForceBridgeVisible()

        pSequence = MissionLib.NewDialogueSequence()
        pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOn", "KiraSet", "Kira", 200)
        pSequence.AppendAction(pAction)
        MissionLib.QueueActionToPlay(pSequence)

        ForceCamOn()

        pSequence2 = MissionLib.NewDialogueSequence()
        pSequence2.AppendAction(App.TGScriptAction_Create(__name__, "MenuUp"))
        pSequence2.Play()

def PreMissionActions():
        pSeq = MissionLib.NewDialogueSequence()
        pAction = App.TGScriptAction_Create(__name__, "MenuClose")
        pSeq.AppendAction(pAction)
        pSeq.Play()

        pSeq2 = MissionLib.NewDialogueSequence()
        pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
        pSeq2.AppendAction(pAction)
        MissionLib.QueueActionToPlay(pSeq2)

        ForceCamOff()

def BorderSkirmishMission1(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.CampaignMode.BorderSkirmish import Mission1
        Mission1.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def BorderSkirmishMission2(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.CampaignMode.BorderSkirmish import Mission2
        Mission2.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def BorderSkirmishMission3(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.CampaignMode.BorderSkirmish import Mission3
        Mission3.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def BorderSkirmishMission4(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.CampaignMode.BorderSkirmish import Mission4
        Mission4.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def BorderSkirmishMission5(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.CampaignMode.BorderSkirmish import Mission5
        Mission5.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXHistoricMission1(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.HistoricMode import HistoricMission1
        HistoricMission1.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXHistoricMission2(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.HistoricMode import HistoricMission2
        HistoricMission2.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXHistoricMission3(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.HistoricMode import HistoricMission3
        HistoricMission3.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXHistoricMission4(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.HistoricMode import HistoricMission4
        HistoricMission4.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXHistoricMission5(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.HistoricMode import HistoricMission5
        HistoricMission5.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXHistoricMission6(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.HistoricMode import HistoricMission6
        HistoricMission6.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXMiniMission1(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission1
        MiniMission1.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXMiniMission2(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission2
        MiniMission2.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXMiniMission3(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission3
        MiniMission3.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXMiniMission4(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission4
        MiniMission4.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXMiniMission5(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission5
        MiniMission5.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXMiniMission6(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission6
        MiniMission6.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXMiniMission7(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission7
        MiniMission7.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXMiniMission8(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission8
        MiniMission8.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXMiniMission9(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission9
        MiniMission9.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXMiniMission10(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission10
        MiniMission10.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXMiniMission11(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission11
        MiniMission11.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXMiniMission12(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission12
        MiniMission12.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXMiniMission13(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission13
        MiniMission13.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXMiniMission14(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission14
        MiniMission14.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXMiniMission15(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission15
        MiniMission15.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXMiniMission16(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission16
        MiniMission16.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXMiniMission17(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission17
        MiniMission17.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXMiniMission18(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission18
        MiniMission18.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXMiniMission19(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission19
        MiniMission19.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXMiniMission20(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission20
        MiniMission20.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXMiniMission21(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission21
        MiniMission21.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXMiniMission22(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission22
        MiniMission22.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)
                
def DS9FXRandomMission1(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import RandomMission1
        RandomMission1.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent) 
                
def DS9FXRandomMission2(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import RandomMission2
        RandomMission2.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)                    

def OldRivalsMission1(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals import Mission1
        Mission1.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def OldRivalsMission2(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals import Mission2
        Mission2.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def OldRivalsMission3(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals import Mission3
        Mission3.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def OldRivalsMission4(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals import Mission4
        Mission4.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def OldRivalsMission5(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals import Mission5
        Mission5.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def OldRivalsMission6(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals import Mission6
        Mission6.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def OldRivalsMission7(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals import Mission7
        Mission7.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def OldRivalsMission8(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals import Mission8
        Mission8.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def OldRivalsMission9(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals import Mission9
        Mission9.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def OldRivalsMission10(pObject, pEvent):
        PreMissionActions()

        from Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals import Mission10
        Mission10.Briefing()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def MissionUnavailable(pObject, pEvent):
        global pPaneID
        pPane = App.TGPane_Create(1.0, 1.0)
        App.g_kRootWindow.PrependChild(pPane)

        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)
        pSequence.AppendAction(TextSequence(pPane))
        pPaneID = pPane.GetObjID()
        pSequence.Play()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def TextSequence(pPane):
        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)

        pAction = LineAction("Mission Unavailable", pPane, 4, 1, 16)
        pSequence.AddAction(pAction, None, 0)
        pAction = App.TGScriptAction_Create(__name__, "KillPane")
        pSequence.AppendAction(pAction, 0.1)
        pSequence.Play()

def LineAction(sLine, pPane, fPos, duration, fontSize):
        fHeight = fPos * 0.0375
        App.TGCreditAction_SetDefaultColor(1.00, 1.00, 1.00, 1.00)
        pAction = App.TGCreditAction_CreateSTR(sLine, pPane, 0.0, fHeight, duration, 0.25, 0.5, fontSize)
        return pAction

def BackToHailMenu(pObject, pEvent):
        CloseChannels(None, None)
        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DS9FXExit():
        global MissionWindow, MissionWindow2, MissionWindow3, MissionWindow4

        if MissionWindow:
                MissionWindow.KillChildren()
                pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
                pTCW.DeleteChild(MissionWindow)
                MissionWindow = None

        if MissionWindow2:
                MissionWindow2.KillChildren()
                pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
                pTCW.DeleteChild(MissionWindow2)
                MissionWindow2 = None

        if MissionWindow3:
                MissionWindow3.KillChildren()
                pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
                pTCW.DeleteChild(MissionWindow3)
                MissionWindow3 = None

        if MissionWindow4:
                MissionWindow4.KillChildren()
                pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
                pTCW.DeleteChild(MissionWindow4)
                MissionWindow4 = None

        from Custom.DS9FX import DS9FXExitHelper
        DS9FXExitHelper.Exiting()

def CheckVideoExitingDS9(pObject, pEvent):
        from Custom.DS9FX.DS9FXWormholeVid import DS9FXWormholeVideo

        VideoMode = DS9FXWormholeVideo.CheckExitFromVideo()

        if VideoMode == 1:
                MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".TransferShips2", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)
        else:
                MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".CheckVideoExitingDS9", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)

def CheckVideoExitingGamma(pObject, pEvent):
        from Custom.DS9FX.DS9FXWormholeVid import DS9FXWormholeVideo

        VideoMode = DS9FXWormholeVideo.CheckExitFromVideo()

        if VideoMode == 1:
                MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".TransferShips3", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)
        else:
                MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".CheckVideoExitingGamma", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)

def TranslatePlayer():
        pPlayer = MissionLib.GetPlayer()
        if not pPlayer:
                return 0
        pSet = pPlayer.GetContainingSet()
        pPlacement = App.PlacementObject_GetObject(pSet, "Entry Location")
        if pPlacement:
                pPlayer.SetTranslate(pPlacement.GetWorldLocation())
                pPlayer.UpdateNodeOnly()

def KillPane(pAction):
        global pPaneID

        pPane = App.TGPane_Cast(App.TGObject_GetTGObjectPtr(pPaneID))
        App.g_kRootWindow.DeleteChild(pPane)

        pPaneID = App.NULL_ID

        return 0

def ScanShip(pObject, pEvent):
        from Custom.DS9FX.DS9FXScan import ProvideShipInfo
        ProvideShipInfo.ScanObject()

def ScanPlayerShip(pObject, pEvent):
        from Custom.DS9FX.DS9FXScan import ProvidePlayerInfo
        ProvidePlayerInfo.ScanPlayer()

def ScanPlanet(pObject, pEvent):
        from Custom.DS9FX.DS9FXScan import ProvidePlanetInfo
        ProvidePlanetInfo.Scan()

def ScanSystem(pObject, pEvent):
        from Custom.DS9FX.DS9FXScan import ProvideRegionInfo
        ProvideRegionInfo.Scan()

def TransferCrewGUI(pObject, pEvent):
        from Custom.DS9FX.DS9FXLifeSupport import HandleTransportCrew
        HandleTransportCrew.CreateGUI()

def ShipRecovery(pObject, pEvent):
        from Custom.DS9FX.DS9FXLifeSupport import ShipRecovery
        ShipRecovery.showGUI()

def CaptureShip(pObject, pEvent):
        from Custom.DS9FX.DS9FXLifeSupport import CaptureShip
        CaptureShip.TakeroverEnemy()

def WarpToKaremma(pObject, pEvent):
        pButton = Bridge.BridgeUtils.GetWarpButton()
        pButton.SetDestination("Systems.DS9FXKaremma.DS9FXKaremma1")
        FixForCustomTravels.SetCourseEvent()
        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def WarpToIdran(pObject, pEvent):
        pButton = Bridge.BridgeUtils.GetWarpButton()
        pButton.SetDestination("Systems.GammaQuadrant.GammaQuadrant1")
        FixForCustomTravels.SetCourseEvent()
        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def WarpToDosi(pObject, pEvent):
        pButton = Bridge.BridgeUtils.GetWarpButton()
        pButton.SetDestination("Systems.DS9FXDosi.DS9FXDosi1")
        FixForCustomTravels.SetCourseEvent()
        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def WarpToYadera(pObject, pEvent):
        pButton = Bridge.BridgeUtils.GetWarpButton()
        pButton.SetDestination("Systems.DS9FXYadera.DS9FXYadera1")
        FixForCustomTravels.SetCourseEvent()
        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def WarpToNewBajor(pObject, pEvent):
        pButton = Bridge.BridgeUtils.GetWarpButton()
        pButton.SetDestination("Systems.DS9FXNewBajor.DS9FXNewBajor1")
        FixForCustomTravels.SetCourseEvent()
        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def WarpToGaia(pObject, pEvent):
        pButton = Bridge.BridgeUtils.GetWarpButton()
        pButton.SetDestination("Systems.DS9FXGaia.DS9FXGaia1")
        FixForCustomTravels.SetCourseEvent()
        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def WarpToKurrill(pObject, pEvent):
        pButton = Bridge.BridgeUtils.GetWarpButton()
        pButton.SetDestination("Systems.DS9FXKurill.DS9FXKurill1")
        FixForCustomTravels.SetCourseEvent()
        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def WarpToTrialus(pObject, pEvent):
        pButton = Bridge.BridgeUtils.GetWarpButton()
        pButton.SetDestination("Systems.DS9FXTrialus.DS9FXTrialus1")
        FixForCustomTravels.SetCourseEvent()
        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def WarpToTRogoran(pObject, pEvent):
        pButton = Bridge.BridgeUtils.GetWarpButton()
        pButton.SetDestination("Systems.DS9FXTRogoran.DS9FXTRogoran1")
        FixForCustomTravels.SetCourseEvent()
        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def WarpToVandros(pObject, pEvent):
        pButton = Bridge.BridgeUtils.GetWarpButton()
        pButton.SetDestination("Systems.DS9FXVandros.DS9FXVandros1")
        FixForCustomTravels.SetCourseEvent()
        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def WarpToFounders(pObject, pEvent):
        pButton = Bridge.BridgeUtils.GetWarpButton()
        pButton.SetDestination("Systems.DS9FXFoundersHomeworld.DS9FXFoundersHomeworld1")
        FixForCustomTravels.SetCourseEvent()
        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def MissionLog(pObject, pEvent):
        from Custom.DS9FX.DS9FXMissions import MissionStatus
        MissionStatus.ViewMissionStatus()

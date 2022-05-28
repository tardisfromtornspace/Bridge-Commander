from bcdebug import debug
###############################################################################
#	Filename:	Mission10Menus.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script to build the UI for the Defend the starbase! mission
#	
#	Created:	Jun 12, '01 - Yossi Horowitz
###############################################################################


import App
import UIHelpers
import MissionLib
import Mission10
import Multiplayer.MissionShared
import Multiplayer.MissionMenusShared
import MainMenu.mainmenu
import Multiplayer.SpeciesToShip
import Multiplayer.SpeciesToSystem
import Bridge.BridgeUtils
import DynamicMusic
import string
import Tactical.Interface.ShipDisplay
import Multiplayer.Episode.Mission4.Mission4Menus
from Custom.QBautostart.Libs.Races import Races
from Custom.MultiplayerExtra.Mission10.Mission10Systems import lStartingSets, CreateSystemMenuEntrys, iDefaultStartingSet

FoundationMode = 1
useBridge = 0
StartMissionRunOnce = 0
dSets = {}
try:
	import Foundation
except:
	FoundationMode = 0
Mission10StartOnce = 0
QBGameModeActivated = 0
BridgeStartOnce = 0

# UI positioning info
MAIN_BUTTON_WIDTH			= 0.20156
MAIN_BUTTON_HEIGHT			= 0.034583

PLAYER_BUTTON_X_POS			= 0.75
PLAYER_BUTTON_Y_POS			= 0.010

SHIPS_BUTTON_X_POS			= 0.54
SHIPS_BUTTON_Y_POS			= 0.010

MISC_BUTTON_X_POS			= 0.33
MISC_BUTTON_Y_POS			= 0.010

SUB_PANE_X_POS				= 0.0
SUB_PANE_Y_POS				= 0.0916667
SUB_PANE_WIDTH				= 0.78125 + 0.08
SUB_PANE_HEIGHT				= 0.8458333 + 0.1

ADD_FRIEND_BUTTON_X_POS			= 0.2500257
ADD_FRIEND_BUTTON_Y_POS			= 0.560416537
ADD_FRIEND_BUTTON_WIDTH			= 0.2515625
ADD_FRIEND_BUTTON_HEIGHT		= 0.0354167

ADD_ENEMY_BUTTON_X_POS			= 0.250025
ADD_ENEMY_BUTTON_Y_POS			= 0.60416657
ADD_ENEMY_BUTTON_WIDTH			= 0.2515625
ADD_ENEMY_BUTTON_HEIGHT			= 0.0354167

FRIEND_LIST_X_POS			= 0.5390625 + 0.08
FRIEND_LIST_Y_POS			= 0.0083333 + 0.1
FRIEND_LIST_WIDTH			= 0.2421875
FRIEND_LIST_HEIGHT			= 0.3354167

ENEMY_LIST_X_POS			= 0.5390625 + 0.08
ENEMY_LIST_Y_POS			= 0.5020835 + 0.1
ENEMY_LIST_WIDTH			= 0.2421875
ENEMY_LIST_HEIGHT			= 0.3437498

SHIP_IMAGE_X_POS			= 0.250025
SHIP_IMAGE_Y_POS			= 0.04791657
SHIP_IMAGE_WIDTH			= 0.2515625
SHIP_IMAGE_HEIGHT			= 0.2458333

SHIPS_SUBPANE_WIDTH					= 0.22

DEL_BUTTON_X_POS			= 0.5390625 + 0.08
DEL_BUTTON_Y_POS			= 0.4120834 + 0.1
DEL_BUTTON_WIDTH			= 0.2421875
DEL_BUTTON_HEIGHT			= 0.0291667

SHIPS_TEXT_X_POS			= 0.250025
SHIPS_TEXT_Y_POS			= 0.304166537
SHIPS_TEXT_WIDTH			= 0.2515625
SHIPS_TEXT_HEIGHT			= 0.245833337

BAR_X_POS				= 0.240625
BAR_Y_POS				= 0.0083333
BAR_WIDTH				= 0.2609625
BAR_HEIGHT				= 0.0291666

SHIP_MENU_X_POS				= 0.0
SHIP_MENU_Y_POS				= 0.0083333
SHIP_MENU_WIDTH				= 0.240625
SHIP_MENU_HEIGHT			= 0.8375

BRIDGE_MENU_X_POS			= 0.1
BRIDGE_MENU_Y_POS			= 0.1
BRIDGE_MENU_WIDTH			= 0.2515625
BRIDGE_MENU_HEIGHT			= 0.3

SHIPS_WINDOW_X_POS					= 0.0925
SHIPS_WINDOW_Y_POS					= 0.1
SHIPS_WINDOW_WIDTH					= 0.504375
SHIPS_WINDOW_HEIGHT					= 0.4533333
SHIPS_WINDOW_BAR_THICKNESS			= 0.0291667

SHIPS_DESC_WINDOW_X_POS				= 0.0925
SHIPS_DESC_WINDOW_Y_POS				= 0.5675
SHIPS_DESC_WINDOW_WIDTH				= 0.504375
SHIPS_DESC_WINDOW_HEIGHT			= 0.2866667
SHIPS_DESC_WINDOW_BAR_THICKNESS		= 0.0291667

TEAM_PARA_X_POS				= 0.0925
TEAM_TOGGLE_Y_POS				= 0.8666666
TEAM_TOGGLE_WIDTH				= 0.140625
TEAM_TOGGLE_HEIGHT			= 0.0416667

NUMBER_190_X_POS					= 0.014375
NUMBER_190_Y_POS					= 0.7083333

NUMBER_945_X_POS					= 0.958125
NUMBER_945_Y_POS					= 0.05

NUMBER_04_X_POS						= 0.9625
NUMBER_04_Y_POS						= 0.7825

TOP_BAR_X_DISTANCE					= 0.009375
TOP_BAR_Y_POS						= 0.0141667
TOP_BAR_RIGHT_EDGE					= 0.990625
TOP_BAR_HEIGHT						= 0.025

TITLE_X_POS							= 0.089375
SUBTITLE_X_POS						= 0.089375
SUBTITLE_Y_POS						= 0.0541667

LEFT_BAR_1_X_POS					= 0.009375
LEFT_BAR_1_Y_POS					= 0.0141667
LEFT_BAR_1_WIDTH					= 0.06875
LEFT_BAR_1_HEIGHT					= 0.025

LEFT_BAR_2_X_POS					= 0.009375
LEFT_BAR_2_Y_POS					= 0.0516667
LEFT_BAR_2_WIDTH					= 0.06875
LEFT_BAR_2_HEIGHT					= 0.225

LEFT_BAR_3_X_POS					= 0.009375
LEFT_BAR_3_Y_POS					= 0.2891667
LEFT_BAR_3_WIDTH					= 0.06875
LEFT_BAR_3_HEIGHT					= 0.4108333

LOWER_LEFT_CURVE_X_POS				= 0.009375
LOWER_LEFT_CURVE_Y_POS				= 0.7125
LOWER_LEFT_CURVE_WIDTH				= 0.54
LOWER_LEFT_CURVE_HEIGHT				= 0.276667
LOWER_LEFT_CURVE_IN_WIDTH			= 0.06875
LOWER_LEFT_CURVE_IN_HEIGHT			= 0.264167
LOWER_LEFT_CURVE_OI_WIDTH			= 0.039375

RIGHT_BAR_1_X_POS					= 0.951875
RIGHT_BAR_1_Y_POS					= 0.0516667
RIGHT_BAR_1_WIDTH					= 0.03875
RIGHT_BAR_1_HEIGHT					= 0.4333333

RIGHT_BAR_2_X_POS					= 0.951875
RIGHT_BAR_2_Y_POS					= 0.4975
RIGHT_BAR_2_WIDTH					= 0.03875
RIGHT_BAR_2_HEIGHT					= 0.3083333

LOWER_RIGHT_CURVE_X_POS				= 0.864375
LOWER_RIGHT_CURVE_Y_POS				= 0.8183333
LOWER_RIGHT_CURVE_WIDTH				= 0.12625
LOWER_RIGHT_CURVE_HEIGHT			= 0.1708333
LOWER_RIGHT_CURVE_IN_WIDTH			= 0.03875
LOWER_RIGHT_CURVE_IN_HEIGHT			= 0.1583333
LOWER_RIGHT_CURVE_OI_WIDTH			= 0.039375

BOTTOM_BAR_1_X_POS					= 0.558125
BOTTOM_BAR_1_Y_POS					= 0.9766667
BOTTOM_BAR_1_WIDTH					= 0.07625
BOTTOM_BAR_1_HEIGHT					= 0.0125

BOTTOM_BAR_2_X_POS					= 0.640625
BOTTOM_BAR_2_Y_POS					= 0.9766667
BOTTOM_BAR_2_WIDTH					= 0.215625
BOTTOM_BAR_2_HEIGHT					= 0.0125

USE_BRIDGE_BUTTON_X_POS         = 0.1
USE_BRIDGE_BUTTON_Y_POS         = 0.45

# globals
NonSerializedObjects = (
"g_pTeamButton",
"g_pOptionsWindowBootButton",
"g_pOptionsWindowBanButton",
"g_pOptionsWindowPlayerMenu",
"g_pShipsButton",
"g_pPlayerButton",
"pPlayerPane",
"pShipsPane",
)

pPlayerPane = None
pShipsPane = None
pMiscPane = None
g_pPlayerButton = None
g_pShipsButton = None
g_pMiscButton = None
g_pMusicType = None
pOldMusic = None
# Save this one se we can make sure FoundationTech doesn't override it
SetShipID = None

g_fYPixelOffset = 0.0
g_fXPixelOffset = 0.0
g_iSpecies = 0
g_iTeam = 0
g_dAllTeams = {}
curMenuInMenu = 0
curShipInMenu = 0
SelectedSpecies = -1
g_iIdOfCurrentlySelectedPlayer = App.TGNetwork.TGNETWORK_INVALID_ID
groupTeam1 = {}
groupTeam2 = {}
pHelmCourseMenu = None
qbGameMode = None
myMultBridge = "GalaxyBridge"
g_pUseBridgeButton = None

# Global pointers to user interface items
g_pTeamButton = None
g_pOptionsWindowBootButton = None
g_pOptionsWindowBanButton  = None
g_pOptionsWindowPlayerMenu = None
	
# Mission specific events.  Start at 105
ET_BOOT_BUTTON_CLICKED			= App.g_kVarManager.MakeEpisodeEventType(105)
ET_PLAYER_BUTTON_CLICKED		= App.g_kVarManager.MakeEpisodeEventType(106)
ET_BAN_BUTTON_CLICKED			= App.g_kVarManager.MakeEpisodeEventType(107)
ET_SELECT_TEAM				= App.g_kVarManager.MakeEpisodeEventType(150)
ET_SELECT_SHIP_TYPE             	= App.g_kVarManager.MakeEpisodeEventType(100)
ET_SELECT_SHIP_IN_ENEMY_MENU            = App.g_kVarManager.MakeEpisodeEventType(200)
ET_SELECT_SHIP_IN_FRIENDLY_MENU         = App.g_kVarManager.MakeEpisodeEventType(201)
# more Event types
ET_DELETE				= App.g_kVarManager.MakeEpisodeEventType(202)
ET_OPEN_SHIPS_PANE			= App.g_kVarManager.MakeEpisodeEventType(203)
ET_OPEN_PLAYER_PANE			= App.g_kVarManager.MakeEpisodeEventType(204)
ET_OPEN_MISC_PANE			= App.g_kVarManager.MakeEpisodeEventType(205)
ET_ADD_AS_FRIEND			= App.g_kVarManager.MakeEpisodeEventType(206)
ET_ADD_AS_ENEMY				= App.g_kVarManager.MakeEpisodeEventType(207)
ET_SELECT_BRIDGE_TYPE                   = App.g_kVarManager.MakeEpisodeEventType(208)
ET_USE_BRIDGE                           = App.g_kVarManager.MakeEpisodeEventType(209)

# Dialog
iShipsUnlocked1 = App.g_kConfigMapping.GetIntValue("QuickBattle", "Ships Unlocked1")

iShipsUnlocked2 = App.g_kConfigMapping.GetIntValue("QuickBattle", "Ships Unlocked2")


# md5sums
ValidMd5sForEngineering = []
ValidMd5sForEngineering.append("6fd9fcafdb8b99a321abd38f8d1cf91b")
ValidMd5sForEngineering.append("1197008e9bc8461488766cddb9a51596")
ValidMd5sForEngineering.append("c1504b056d62e55b8672a90a7caeb8d8")


###############################################################################
#	BuildMission10Menu()
#	
#	Builds the Mission 5 options menu.
#	
#	Args:	none
#	
#	Return:	none
###############################################################################
def BuildMission10Menus(bRebuild = 0):
	debug(__name__ + ", BuildMission10Menus")
	global pPlayerPane, groupTeam1, groupTeam2, qbGameMode, FoundationMode, SetShipID

        if FoundationMode == 1:
                SetShipID = Tactical.Interface.ShipDisplay.SetShipID
                qbGameMode = Foundation.BuildGameMode()
        
        # reset dics
        groupTeam1 = {}
        groupTeam2 = {}

	# Find the Multiplayer window
	pTopWindow = App.TopWindow_GetTopWindow()
	pMultWindow = App.MultiplayerWindow_Cast (pTopWindow.FindMainWindow(App.MWT_MULTIPLAYER))

	# Hide all the children so that only we will be visible.
	pMultWindow.HideAllChildren()

	pDatabase = Multiplayer.MissionShared.g_pDatabase
	
	# Create the mission menu
	pPlayerPane = BuildMissionMenu(pMultWindow, pDatabase)
	pMultWindow.AddChild(pPlayerPane)
	
	#Build the mission-specific pane that will get put inside of the options menu
	BuildMissionSpecificOptionsMenuPane(pPlayerPane)

	# Build end game window.
	pMenu = Multiplayer.MissionMenusShared.BuildEndWindow(pMultWindow, pDatabase, 0)
	pMultWindow.AddChild(pMenu)
	pMenu.SetNotVisible();

	# Build the initial player list
	RebuildPlayerList()

	if (not bRebuild):
		# Make multiplayer window visible.
		pTopWindow.MoveToFront(pMultWindow)
		pMultWindow.SetVisible()

		# Hide the tactical menu
		pTactWindow = App.TacticalWindow_Cast(pTopWindow.FindMainWindow(App.MWT_TACTICAL))
		pTactWindow.SetNotVisible()

		pOptionsWindow = App.TopWindow_GetTopWindow().FindMainWindow(App.MWT_OPTIONS);
		if pOptionsWindow.IsVisible():
			App.TopWindow_GetTopWindow().ToggleOptionsMenu()


###############################################################################
#	BuildMissionMenu()
#	
#	Builds the Mission menu.
#	
#	Args:	none
#	
#	Return:	none
###############################################################################
def BuildMissionMenu(pMultWindow, pDatabase):
	debug(__name__ + ", BuildMissionMenu")
	global g_pShipsButton, g_pPlayerButton, pShipsPane, g_pTeamButton, g_pMiscButton, pMiscPane, g_dAllTeams
        global ET_OPEN_MISC_PANE, ET_OPEN_SHIPS_PANE, ET_SELECT_TEAM, ET_OPEN_PLAYER_PANE

	g_pMissionDatabase = App.g_kLocalizationManager.Load("data/TGL/QuickBattle/QuickBattle.tgl")
	
	pPlayerPane = Multiplayer.MissionMenusShared.BuildMissionMenu(pMultWindow, pDatabase,
		"The Border Skirmish Host", "The Border Skirmish Client", "The Border Skirmish Direct Host")

	# Create the Ships menu
	#pShipsPane = BuildShipsPane()
	#pMultWindow.AddChild(pShipsPane)
        
        # Misc Panel
        pMiscPane = BuildMiscPane()
        pMultWindow.AddChild(pMiscPane)
	
	# Set the font larger
	App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcSmallFont,
				MainMenu.mainmenu.g_kSmallFontSize[MainMenu.mainmenu.g_iRes] + 1)

	#########################################
	# Create team button

	# Get length of text for select team and time limit to determine which is longer.
	# we do this so we can position the buttons properly, with the proper alignment.

	pText = App.TGParagraph_CreateW(pDatabase.GetString("Select Team"))
	pText2 = App.TGParagraph_CreateW(pDatabase.GetString("Time Limit"))
	fWidth = pText.GetWidth()
	fWidth2 = pText2.GetWidth()
	if (fWidth2 > fWidth):
		fWidth = fWidth2

	pEvent = App.TGEvent_Create()
	pEvent.SetEventType(ET_SELECT_TEAM)
	pEvent.SetDestination(pPlayerPane)

	# The team caption
	pText.SetColor(App.g_kTitleColor)
	
	# get all teams
	for iTeam in range(len(Races.keys())):
		pcTeamName = Races.keys()[iTeam]
		g_dAllTeams[pcTeamName] = iTeam
	
	# Make sure we do not start with displaying god ships
	if Races.keys()[g_iTeam] == "GodShips":
		IncTeam()
	# Rebuild the ship select window based on team.
	RebuildShipSelectWindow()
	# The team button
	g_pTeamButton = App.STRoundedButton_CreateW(App.TGString(Races.keys()[g_iTeam]), pEvent, TEAM_TOGGLE_WIDTH, TEAM_TOGGLE_HEIGHT, 1)

	g_pTeamButton.SetColor(App.g_kTextEntryColor)
	g_pTeamButton.SetNormalColor(App.g_kMultiplayerButtonPurple)
	g_pTeamButton.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
	g_pTeamButton.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
	g_pTeamButton.SetTextColor(App.g_kSTMenuTextHighlightColor)
	g_pTeamButton.SetDisabledColor(App.g_kSTMenu1Disabled)
	g_pTeamButton.SetColorBasedOnFlags()
	pPlayerPane.AddChild(g_pTeamButton, TEAM_PARA_X_POS + fWidth + 0.005, TEAM_TOGGLE_Y_POS, 0)
	App.g_kFocusManager.AddObjectToTabOrder(g_pTeamButton)

	if (App.g_kUtopiaModule.IsHost() and not App.g_kUtopiaModule.IsClient()):
		# dedicated servers do not chose teams.
		g_pTeamButton.SetNotVisible()	

	fPosDelta = (pText.GetHeight() - g_pTeamButton.GetHeight()) / 2.0
	pPlayerPane.AddChild(pText, TEAM_PARA_X_POS + (fWidth - pText.GetWidth ()), TEAM_TOGGLE_Y_POS - fPosDelta, 0)

	#pEventShipsButton = App.TGEvent_Create()
	#pEventShipsButton.SetEventType(ET_OPEN_SHIPS_PANE)
	#pEventShipsButton.SetDestination(pShipsPane)

	pEventPlayerButton = App.TGEvent_Create()
	pEventPlayerButton.SetEventType(ET_OPEN_PLAYER_PANE)
	pEventPlayerButton.SetDestination(pPlayerPane)

	pEventMiscButton = App.TGEvent_Create()
	pEventMiscButton.SetEventType(ET_OPEN_MISC_PANE)
	pEventMiscButton.SetDestination(pMiscPane)

	# Create the buttons to switch between the Ships and Player subpanes
	#g_pShipsButton = App.STRoundedButton_CreateW(g_pMissionDatabase.GetString("Ships"), pEventShipsButton, MAIN_BUTTON_WIDTH, MAIN_BUTTON_HEIGHT, 1)
	#g_pShipsButton.SetNormalColor(App.g_kMainMenuButtonColor)
	#g_pShipsButton.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
	#g_pShipsButton.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
	#g_pShipsButton.SetColorBasedOnFlags()
        #g_pShipsButton.SetNotSelected()
	#pMultWindow.AddChild(g_pShipsButton, SHIPS_BUTTON_X_POS, SHIPS_BUTTON_Y_POS)
	#App.g_kFocusManager.AddObjectToTabOrder(g_pShipsButton)

	g_pPlayerButton = App.STRoundedButton_CreateW(g_pMissionDatabase.GetString("Player and Region"), pEventPlayerButton, MAIN_BUTTON_WIDTH, MAIN_BUTTON_HEIGHT, 1)
	g_pPlayerButton.SetNormalColor(App.g_kMainMenuButtonColor)
	g_pPlayerButton.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
	g_pPlayerButton.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
	g_pPlayerButton.SetColorBasedOnFlags()
        g_pPlayerButton.SetSelected()
	pMultWindow.AddChild(g_pPlayerButton, PLAYER_BUTTON_X_POS, PLAYER_BUTTON_Y_POS)
	App.g_kFocusManager.AddObjectToTabOrder(g_pPlayerButton)

	g_pMiscButton = App.STRoundedButton_CreateW(App.TGString("Misc"), pEventMiscButton, MAIN_BUTTON_WIDTH, MAIN_BUTTON_HEIGHT, 1)
	g_pMiscButton.SetNormalColor(App.g_kMainMenuButtonColor)
	g_pMiscButton.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
	g_pMiscButton.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
	g_pMiscButton.SetColorBasedOnFlags()
        g_pMiscButton.SetNotSelected()
        # Do not allow misc pane until we now why the Bridge doesn't work for clients
	pMultWindow.AddChild(g_pMiscButton, MISC_BUTTON_X_POS, MISC_BUTTON_Y_POS)
	App.g_kFocusManager.AddObjectToTabOrder(g_pMiscButton)

	#if not App.g_kUtopiaModule.IsHost():
            # clients do not chose Bots.
            #g_pShipsButton.SetNotVisible()

	# reposition the time limit button.
	pText = Multiplayer.MissionMenusShared.g_pTimeLimitText
	pButton = Multiplayer.MissionMenusShared.g_pTimeLimitButton

	#pText.SetPosition(Multiplayer.MissionMenusShared.TIME_LIMIT_PARA_X_POS + (fWidth - pText.GetWidth ()), pText.GetTop (), 0)
	#pButton.SetPosition(Multiplayer.MissionMenusShared.TIME_LIMIT_PARA_X_POS + fWidth + 0.005, pButton.GetTop (), 0)
	pText.SetNotVisible()
	pButton.SetNotVisible()

	pText = Multiplayer.MissionMenusShared.g_pFragLimitText
	pButton = Multiplayer.MissionMenusShared.g_pFragLimitButton
	pText.SetNotVisible()
	pButton.SetNotVisible()

	# Add some mission specific handlers for the mission pane
	pPlayerPane.AddPythonFuncHandlerForInstance(Multiplayer.MissionMenusShared.ET_FINISHED_SELECT, __name__ + ".FinishedSelectHandler")
	pPlayerPane.AddPythonFuncHandlerForInstance(Multiplayer.MissionMenusShared.ET_SELECT_SHIP_SPECIES, __name__ + ".SelectSpeciesHandler")
	#pPlayerPane.AddPythonFuncHandlerForInstance(Multiplayer.MissionMenusShared.ET_SELECT_SYSTEM, __name__ + ".SelectSystemHandler")
	pPlayerPane.AddPythonFuncHandlerForInstance(ET_SELECT_TEAM, __name__ + ".SelectTeamHandler")
	pPlayerPane.AddPythonFuncHandlerForInstance(ET_BOOT_BUTTON_CLICKED, __name__ + ".HandleBootButtonClicked")
	pPlayerPane.AddPythonFuncHandlerForInstance(ET_BAN_BUTTON_CLICKED, __name__ + ".HandleBanButtonClicked")
	pPlayerPane.AddPythonFuncHandlerForInstance(ET_PLAYER_BUTTON_CLICKED, __name__ + ".HandlePlayerButtonClicked")
	pPlayerPane.AddPythonFuncHandlerForInstance(ET_OPEN_PLAYER_PANE, __name__ + ".OpenPlayerPane")
        #pShipsPane.AddPythonFuncHandlerForInstance(ET_OPEN_SHIPS_PANE, __name__ + ".OpenShipsPane")
	#pShipsPane.AddPythonFuncHandlerForInstance(ET_SELECT_SHIP_TYPE, __name__ + ".SelectShipType")
	#pShipsPane.AddPythonFuncHandlerForInstance(ET_SELECT_SHIP_IN_ENEMY_MENU, __name__ + ".ShipInEnemyMenuSelect")
        #pShipsPane.AddPythonFuncHandlerForInstance(ET_SELECT_SHIP_IN_FRIENDLY_MENU, __name__ + ".ShipInFriendlyMenuSelect")
        #pShipsPane.AddPythonFuncHandlerForInstance(ET_ADD_AS_ENEMY, __name__ + ".AddShipAsEnemy")
        #pShipsPane.AddPythonFuncHandlerForInstance(ET_ADD_AS_FRIEND, __name__ + ".AddShipAsFriend")
        #pShipsPane.AddPythonFuncHandlerForInstance(ET_DELETE, __name__ + ".Delete")
        pMiscPane.AddPythonFuncHandlerForInstance(ET_OPEN_MISC_PANE, __name__ + ".OpenMiscPane")
        pMiscPane.AddPythonFuncHandlerForInstance(ET_SELECT_BRIDGE_TYPE, __name__ + ".SelectBridge")
        pMiscPane.AddPythonFuncHandlerForInstance(ET_USE_BRIDGE, __name__ + ".SetUseBridge")

	# Set the font back to normal small size
	App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcFlightSmallFont,
				MainMenu.mainmenu.g_kFlightSmallFontSize[MainMenu.mainmenu.g_iRes])

	if (App.g_kUtopiaModule.IsHost()):
		Multiplayer.MissionMenusShared.g_pSystemPane.SetNotVisible()
		Multiplayer.MissionMenusShared.g_pSystemIcon.SetNotVisible()
		Multiplayer.MissionMenusShared.g_pSystemDescPane.SetNotVisible()

	return pPlayerPane

###############################################################################
#	HandlePlayerButtonClicked()
#	
#	A button on the scoreboard has been clicked. We must activate the boot
#	button (if the player is the host).
#	
#	Args:	TGObject*	pObject	- the mission pane
#			TGEvent*	pEvent	- our ET_PLAYER_BUTTON_CLICKED event
#	
#	Return:	None
###############################################################################
def HandlePlayerButtonClicked(pObject, pEvent):
	debug(__name__ + ", HandlePlayerButtonClicked")
	if App.g_kUtopiaModule.IsHost():
		g_pOptionsWindowBootButton.SetEnabled()
		g_pOptionsWindowBanButton.SetEnabled()

	global g_iIdOfCurrentlySelectedPlayer
	g_iIdOfCurrentlySelectedPlayer = pEvent.GetPlayerID()

	pObject.CallNextHandler(pEvent)


###############################################################################
#	HandleBootButtonClicked()
#	
#	The boot button has been clicked. Let the multiplayer window know, and set
#	the UI back up the way it was
#	
#	Args:	TGObject*	pObject	- the mission pane
#			TGEvent*	pEvent	- our ET_BOOT_BUTTON_CLICKED event
#	
#	Return:	None
###############################################################################
def HandleBootButtonClicked(pObject, pEvent):
	debug(__name__ + ", HandleBootButtonClicked")
	g_pOptionsWindowBootButton.SetDisabled()
	g_pOptionsWindowBanButton.SetDisabled()

	global g_iIdOfCurrentlySelectedPlayer
	
	if g_iIdOfCurrentlySelectedPlayer != App.TGNetwork.TGNETWORK_INVALID_ID:
		pTopWindow = App.TopWindow_GetTopWindow()
		pMultWindow = App.MultiplayerWindow_Cast(pTopWindow.FindMainWindow(App.MWT_MULTIPLAYER))
		pEvent = App.TGPlayerEvent_Create()
		pEvent.SetEventType(App.ET_PLAYER_BOOT_EVENT)
		pEvent.SetDestination(pMultWindow)
		pEvent.SetPlayerID(g_iIdOfCurrentlySelectedPlayer)
		App.g_kEventManager.AddEvent(pEvent)
	
	g_iIdOfCurrentlySelectedPlayer = App.TGNetwork.TGNETWORK_INVALID_ID

	pObject.CallNextHandler(pEvent)

###############################################################################
#	HandleBanButtonClicked(pObject, pEvent)
#	
#	The ban button has been clicked. Do a normal boot, but also add the
#	player's IP to the ban list.
#	
#	Args:	pObject	- the mission pane
#			pEvent	- the ET_BAN_BUTTON_CLICKED event
#	
#	Return:	none
###############################################################################
def HandleBanButtonClicked(pObject, pEvent):
	debug(__name__ + ", HandleBanButtonClicked")
	g_pOptionsWindowBootButton.SetDisabled()
	g_pOptionsWindowBanButton.SetDisabled()

	global g_iIdOfCurrentlySelectedPlayer
	pNetwork = App.g_kUtopiaModule.GetNetwork()

	# Make sure we're valid, and that the selection is not the host/local player.
	if ((pNetwork == None) or 
		(g_iIdOfCurrentlySelectedPlayer == pNetwork.GetHostID()) or
	    (g_iIdOfCurrentlySelectedPlayer == pNetwork.GetLocalID())):
		g_iIdOfCurrentlySelectedPlayer = App.TGNetwork.TGNETWORK_INVALID_ID
		pObject.CallNextHandler(pEvent)
		return

	if g_iIdOfCurrentlySelectedPlayer != App.TGNetwork.TGNETWORK_INVALID_ID:
		pPlayerList = pNetwork.GetPlayerList()
		pPlayer = pPlayerList.GetPlayer(g_iIdOfCurrentlySelectedPlayer)

		if pPlayer:
			# Add them to the ban list.
			App.TGWinsockNetwork_BanPlayerByIP(pPlayer.GetNetAddress())

		# Now do a normal boot.
		pTopWindow = App.TopWindow_GetTopWindow()
		pMultWindow = App.MultiplayerWindow_Cast(pTopWindow.FindMainWindow(App.MWT_MULTIPLAYER))
		pEvent = App.TGPlayerEvent_Create()
		pEvent.SetEventType(App.ET_PLAYER_BOOT_EVENT)
		pEvent.SetDestination(pMultWindow)
		pEvent.SetPlayerID(g_iIdOfCurrentlySelectedPlayer)
		App.g_kEventManager.AddEvent(pEvent)

	g_iIdOfCurrentlySelectedPlayer = App.TGNetwork.TGNETWORK_INVALID_ID

	pObject.CallNextHandler(pEvent)
		
###############################################################################
#	RebuildPlayerList()
#	
#	Update the scoreboard with the latest data
#	
#	Args:	None
#	
#	Return:	None
###############################################################################
def RebuildPlayerList():
	debug(__name__ + ", RebuildPlayerList")
	RebuildShipSelectWindow()
	
	# We don't want to refresh the player list when the Game Over screen is up
	# 'cuz that can sometimes break the game over screen
	if Multiplayer.MissionShared.g_bGameOver:
		return

	pNetwork = App.g_kUtopiaModule.GetNetwork()
	if (not pNetwork):
		# Don't rebuild the list since you can't
		return

	pGame = App.Game_GetCurrentGame()
	if (not pGame):
		# Game over.  Can't rebuild list.
		return

	pDatabase = Multiplayer.MissionShared.g_pDatabase

	pMultGame = App.MultiplayerGame_Cast(pGame)

	# Find the Multiplayer window
	pTopWindow = App.TopWindow_GetTopWindow()
	pMultWindow = App.MultiplayerWindow_Cast(pTopWindow.FindMainWindow(App.MWT_MULTIPLAYER))
	
	pEndPane = App.TGPane_Cast (pMultWindow.GetEndWindow())
	pSortList = []
	pTeamScoresList = []

	pTeamScoresDict = Mission10.g_kTeamScoreDictionary
	pTeamKillsDict = Mission10.g_kTeamKillsDictionary


	if (pEndPane):
		# Get the menu
		pPane = Multiplayer.MissionMenusShared.g_pEndPlayerListPane
		pStyleWindow = Multiplayer.MissionMenusShared.g_pEndPlayerListWindow
		pMenu = Multiplayer.MissionMenusShared.g_pEndPlayerListMenu

#		print ("Rebuilding player list.got menu")

		# Kill all the children.		
		pMenu.KillChildren()

		# Reconstruct the menu, first storing it in a python list.
		pDict = Mission10.g_kKillsDictionary

		pPlayerList = pNetwork.GetPlayerList()
		iNumPlayers = pPlayerList.GetNumPlayers()
		i = 0
		while (i < iNumPlayers):
			pPlayer = pPlayerList.GetPlayerAtIndex(i)
			
			if (pMultGame):
				if (pDict.has_key (pPlayer.GetNetID()) and pPlayer.IsDisconnected() == 0):
					# This is an actual player in the game.  Add him to the sort list for
					# later sorting/
					pSortList.append(pPlayer)

			# Increment the index to look at the next player.				
			i = i + 1

		# Okay, now we have a list of all the players in the game.  Sort it
		# using the ComparePlayer function to do comparisons.
		pSortList.sort(ComparePlayer)

		# Sort the team scores
		for iTeam in pTeamScoresDict.keys():
			pTeamScoresList.append(iTeam)
		pTeamScoresList.sort(CompareTeams)

		pTeamDict = Mission10.g_kTeamDictionary 

		# Find out how many players are on each team
		pNumPlayersOnTeam = {}
		for iTeam in pTeamScoresList:
			pNumPlayersOnTeam[iTeam] = 0
			for pPlayer in pSortList:
				if pTeamDict.has_key(pPlayer.GetNetID()):
					iPlayerTeam = pTeamDict[pPlayer.GetNetID()]
					if (iPlayerTeam == iTeam):
						pNumPlayersOnTeam[iTeam] = pNumPlayersOnTeam[iTeam] + 1
						
		# Okay, now build the team scores
		for iTeam in pTeamScoresList:
			if pNumPlayersOnTeam[iTeam] < 1:
				continue
			
			pcTeamName = Races.keys()[g_iTeam]

			pPane = CreateTeamScoreEntry(pcTeamName)
			pMenu.AddChild(pPane, 0, 0, 0)

			# Add the top 3 performers for that team.
			iCount = 0
			for pPlayer in pSortList:
				iPlayerTeam = Mission10.INVALID_TEAM
				if (pTeamDict.has_key(pPlayer.GetNetID())):
					iPlayerTeam = pTeamDict[pPlayer.GetNetID()]

				if (iPlayerTeam == iTeam):
					# This is a top performer on this team.
					pTeamAcePane = App.TGPane_Create (0.4, 0.1)

					pPane = CreateTeamAceEntry (pPlayer)
					pTeamAcePane.AddChild (pPane, 0.02, 0, 0)
					pTeamAcePane.Resize (pTeamAcePane.GetWidth(), pPane.GetHeight(), 0)

					pMenu.AddChild (pTeamAcePane, 0, 0, 0)

					iCount = iCount + 1

					if (iCount == 3):
						# Only show the top two performers
						break;

		# Now add in your own performance.
		pPlayer = pPlayerList.GetPlayer(pNetwork.GetLocalID())
		if (pPlayer):
			pPane = CreatePlayerScoreEntry(pPlayer)
			pMenu.AddChild (pPane, 0.0, 0.0)

		# Now call layout on the entire menu.
		pMenu.Layout()
		pStyleWindow.InteriorChangedSize()

	# Also rebuild the scoreboard in the Options Window

	if g_pOptionsWindowPlayerMenu:

		# Set the font larger
		App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcSmallFont,
					MainMenu.mainmenu.g_kSmallFontSize[MainMenu.mainmenu.g_iRes])

		g_pOptionsWindowPlayerMenu.KillChildren()
		
		# First add an empty pane the height of an entry to push the other entries
		# down so that the top of the list is not covered by the headers
		g_pOptionsWindowPlayerMenu.AddChild(App.TGPane_Create(0.4, 0.04), 0.0, 0.0, 0)
		
		# Build the scoreboard that goes in the options window
		for iTeam in pTeamScoresList:
			if pNumPlayersOnTeam[iTeam] < 1:
				continue
#			print "Rebuilding the scoreboard in the Options Window. Creating team score entry."

			pPane = CreateScoreboardTeamScoreEntry(pcTeamName)
			g_pOptionsWindowPlayerMenu.AddChild(pPane, 0, 0, 0)
			
			for pPlayer in pSortList:
				if pTeamDict.has_key(pPlayer.GetNetID()):
					iPlayerTeam = pTeamDict[pPlayer.GetNetID()]
					if (iPlayerTeam == iTeam):
						#print "Rebuilding the scoreboard in the Options Window. Creating player score entry."
						pPane = CreateScoreboardPlayerScoreEntry(pPlayer)
						g_pOptionsWindowPlayerMenu.AddChild(pPane, 0.0, 0.0, 0)

		# Now layout the menu. No need to call InteriorChangedSize on its parent because
		# it's an STSubPane and knows to handle that on its own.
		g_pOptionsWindowPlayerMenu.Resize(g_pOptionsWindowPlayerMenu.GetWidth(), g_pOptionsWindowPlayerMenu.GetTotalHeightOfChildren())
		g_pOptionsWindowPlayerMenuWindow.Layout()
		g_pOptionsWindowPlayerMenuWindow.InteriorChangedSize()
		#g_pOptionsWindowPlayerMenu.Layout()

		# Set the font back to the flight size
		App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcFlightSmallFont,
				MainMenu.mainmenu.g_kFlightSmallFontSize[MainMenu.mainmenu.g_iRes])

	# Disable the boot button, since the player it's set to boot may no longer be
	# around
	if g_pOptionsWindowBootButton:
		g_pOptionsWindowBootButton.SetDisabled()
	if g_pOptionsWindowBanButton:
		g_pOptionsWindowBanButton.SetDisabled()

	# Now rebuild the info pane
	RebuildInfoPane()

	# Close and open the score window so it'll properly re-lay itself out
	DoScoreWindow()
	DoScoreWindow()

###############################################################################
#	CreateScoreboardPlayerScoreEntry()
#	
#	Create a player info entry for the scoreboard that's in the options window
#	
#	Args:	pPlayer		- the player
#	
#	Return:	A TGPane* containing a player info entry
###############################################################################
def CreateScoreboardPlayerScoreEntry(pPlayer):
	# Set the font larger
	debug(__name__ + ", CreateScoreboardPlayerScoreEntry")
	App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcSmallFont,
				MainMenu.mainmenu.g_kSmallFontSize[MainMenu.mainmenu.g_iRes])

	# Initialize some globals
	# create a pane to hold everything.
	pPlayerEntryPane = App.TGPane_Create(0.5, 0.04)

	# Create the event that gets sent that can be used for booting a player
	pTopWindow = App.TopWindow_GetTopWindow()
	pMultWindow = App.MultiplayerWindow_Cast (pTopWindow.FindMainWindow(App.MWT_MULTIPLAYER))
	pEvent = App.TGPlayerEvent_Create()
	pEvent.SetEventType(ET_PLAYER_BUTTON_CLICKED)
	pEvent.SetDestination(pMultWindow.GetMissionPane())
	iPlayerID = pPlayer.GetNetID()
	pEvent.SetPlayerID(iPlayerID)

	# Create the player name text
	pButton = App.STButton_CreateW(pPlayer.GetName(), pEvent, 0, 0.04, 0.04)
	pButton.SetNormalColor(App.g_kSTMenu4NormalBase)
	pButton.SetHighlightedColor(App.g_kSTMenu4HighlightedBase)
	pButton.SetSelectedColor(App.g_kSTMenu4Selected)
	pButton.SetColorBasedOnFlags()
	pPlayerEntryPane.PrependChild(pButton, 0.03, 0.0, 0)
	
	pName = App.TGTextButton_Create(pPlayer.GetName().GetCString())
	pName.AlignTextHorizontal(App.TGTextButton.ALIGN_CENTER, 0)
	pName.AlignTextVertical(App.TGTextButton.ALIGN_MIDDLE, 0)
	pPlayerEntryPane.PrependChild(pName, 0.07, 0.0, 0)
	
	# create kills
	# Get the kill total from the score dictionaries
	pDict = Mission10.g_kKillsDictionary

	iKills = 0
	if (pDict.has_key(iPlayerID)):
		iKills = pDict[iPlayerID]

	pText = App.TGTextButton_Create(str(iKills))
	pText.AlignTextHorizontal(App.TGTextButton.ALIGN_CENTER, 0)
	pText.AlignTextVertical(App.TGTextButton.ALIGN_MIDDLE, 0)
	pText.Resize(0.065, 0.04, 0)
	pPlayerEntryPane.PrependChild(pText, 0.25, 0.0, 0)

	# Create death total
	# Get the death total from the score dictionaries
	pDict = Mission10.g_kDeathsDictionary

	iDeaths = 0
	if (pDict.has_key(iPlayerID)):
		iDeaths = pDict[iPlayerID]

	pText = App.TGTextButton_Create(str(iDeaths))
	pText.AlignTextHorizontal(App.TGTextButton.ALIGN_CENTER, 0)
	pText.AlignTextVertical(App.TGTextButton.ALIGN_MIDDLE, 0)
	pText.Resize(0.065, 0.04, 0)
	pPlayerEntryPane.PrependChild(pText, 0.325, 0.0, 0)

	return pPlayerEntryPane

def CreateScoreboardTeamScoreEntry(pcString):
	debug(__name__ + ", CreateScoreboardTeamScoreEntry")
	pDatabase = Multiplayer.MissionShared.g_pDatabase

	# create a pane to hold everything.
	pTeamEntryPane = App.TGPane_Create(0.4, 0.1)

	pText = App.TGParagraph_Create(pcString)
	pText.SetColor(App.g_kTitleColor)
	pTeamEntryPane.AddChild(pText, 0, 0, 0)

	# Resize the team entry pane
	fHeight = pText.GetHeight()
	pTeamEntryPane.Resize(0.4, fHeight, 0)

	return pTeamEntryPane

def CreateTeamScoreEntry(pcString):
	debug(__name__ + ", CreateTeamScoreEntry")
	pDatabase = Multiplayer.MissionShared.g_pDatabase

	# create a pane to hold everything.
	pTeamEntryPane = App.TGPane_Create(0.4, 0.1)

	pText = App.TGParagraph_Create(pcString)
	pTeamEntryPane.AddChild(pText, 0, 0, 0)

	# Resize the team entry pane
	fHeight = pText.GetHeight()
	pTeamEntryPane.Resize(0.4, fHeight * 2.0, 0)

	# Create the top performer entry
	pText = App.TGParagraph_CreateW(pDatabase.GetString ("Team Ace"))
	pTeamEntryPane.AddChild(pText, 0.01, fHeight, 0)

	return pTeamEntryPane

def CreateTeamAceEntry(pPlayer):
	debug(__name__ + ", CreateTeamAceEntry")
	pDatabase = Multiplayer.MissionShared.g_pDatabase

	# Create the player name text
	pPane = App.TGPane_Create(0.38, 0.1)

	pString = pDatabase.GetString("Starbase Team Player")
	pcString = pString.GetCString()

	pName = pPlayer.GetName()
	pcName = pName.GetCString()

	iPlayerID = pPlayer.GetNetID()

	# Get the kill total from the score dictionaries
	pDict = Mission10.g_kKillsDictionary

	iKills = 0
	if (pDict.has_key(iPlayerID)):
		iKills = pDict[iPlayerID]

	pcKills = str(iKills)

	# Create the death count
	# Get the death total from the score dictionaries
	pDict = Mission10.g_kDeathsDictionary

	iDeaths = 0
	if (pDict.has_key(iPlayerID)):
		iDeaths = pDict[iPlayerID]

	pcDeaths = str (iDeaths)

	pcSubString = pcString % (pcName, pcKills, pcDeaths)

	pText = App.TGParagraph_Create (pcSubString)

	pPane.AddChild(pText, 0, 0, 0)
	fHeight = pText.GetHeight ()
	pPane.Resize(0.38, fHeight, 0)

	return pPane
					
def CreatePlayerScoreEntry(pPlayer):
	debug(__name__ + ", CreatePlayerScoreEntry")
	pDatabase = Multiplayer.MissionShared.g_pDatabase

	# Create the player name text
	pPane = App.TGPane_Create (0.40, 0.1)

	pString = pDatabase.GetString ("Starbase Your Stats")
	pcString = pString.GetCString()

	iPlayerID = pPlayer.GetNetID()

	# Get the kill total from the score dictionaries
	pDict = Mission10.g_kKillsDictionary

	iKills = 0
	if (pDict.has_key(iPlayerID)):
		iKills = pDict [iPlayerID]

	pcKills = str(iKills)

	# Create the death count
	# Get the death total from the score dictionaries
	pDict = Mission10.g_kDeathsDictionary

	iDeaths = 0
	if (pDict.has_key(iPlayerID)):
		iDeaths = pDict[iPlayerID]

	pcDeaths = str(iDeaths)

	pcSubString = pcString % (pcKills, pcDeaths)

	pText = App.TGParagraph_Create(pcSubString)

	pPane.AddChild(pText, 0, 0, 0)
	fHeight = pText.GetHeight()
	pPane.Resize(0.4, fHeight, 0)

	return pPane
					


def ComparePlayer(pThisPlayer, pOtherPlayer):
	# Get the kills of this player and the other player.
	debug(__name__ + ", ComparePlayer")
	iThisID = pThisPlayer.GetNetID()
	iOtherID = pOtherPlayer.GetNetID()

	# Get the kill total from the score dictionaries
	pDict = Mission10.g_kScoresDictionary

	iThisScore = 0
	iOtherScore = 0

	if (pDict.has_key(iThisID)):
		iThisScore = pDict[iThisID]

	if (pDict.has_key(iOtherID)):
		iOtherScore = pDict[iOtherID]
	
	# reverse sort.  Higher kills get sorted higher.
	if (iThisScore < iOtherScore):
		return 1
	elif (iThisScore == iOtherScore):
		pKillsDict = Mission10.g_kKillsDictionary

		iThisKills = 0
		iOtherKills = 0
		if (pKillsDict.has_key(iThisID)):
			iThisKills = pKillsDict[iThisID]

		if (pKillsDict.has_key(iOtherID)):
			iOtherKills = pKillsDict[iOtherID]
		
		# We want lower deaths to get sorted higher
		if (iThisKills < iOtherKills):
			return -1
		elif (iThisKills > iOtherKills):
			return 1
		else:
			return 0
	else:
		return -1


def CompareTeams(iThisTeam, iOtherTeam):
	# Get the score total from the teamscore dictionaries
	debug(__name__ + ", CompareTeams")
	pDict = Mission10.g_kTeamScoreDictionary

	iThisScore = 0
	iOtherScore = 0

	if (pDict.has_key(iThisTeam)):
		iThisScore = pDict[iThisTeam]

	if (pDict.has_key(iOtherTeam)):
		iOtherScore = pDict[iOtherTeam]
	
	# reverse sort.  Higher kills get sorted higher.
	if (iThisScore < iOtherScore):
		return 1
	elif (iThisScore == iOtherScore):
		if iThisTeam < iOtherTeam:
			return -1
		else:
			return 1
	else:
		return -1

# These must be here cause they are called by other scripts and by code.
def DoScoreWindow():
	debug(__name__ + ", DoScoreWindow")
	Multiplayer.MissionMenusShared.DoScoreWindow()
	return 0

def DoEndGameDialog(bRestartable = 0):
	debug(__name__ + ", DoEndGameDialog")
	Multiplayer.MissionMenusShared.DoEndGameDialog(bRestartable)
	return 1

###############################################################################
#	SelectSpeciesHandler()
#	
#	Handle events for selection of a new system
#	
#	Args:	TGObject	pObject - destination object for the event
#			TGIntEvent	pEvent  - The Int in this event is the index of our new
#									species
#	
#	Return:	None
###############################################################################
def SelectSpeciesHandler(TGObject, pEvent):
	# Set the global species selected number.
	debug(__name__ + ", SelectSpeciesHandler")
	Multiplayer.MissionMenusShared.SelectSpecies(pEvent.GetInt())

	# make the previously select button not chosen
	if (Multiplayer.MissionMenusShared.g_pChosenSpecies):
		Multiplayer.MissionMenusShared.g_pChosenSpecies.SetChosen(0)

	# Set the button that was clicked chosen, so it will have a different color.
	pButton = App.STButton_Cast(pEvent.GetSource())
	pButton.SetChosen(1)
	Multiplayer.MissionMenusShared.g_pChosenSpecies = pButton

	# Make the start button visible if system and ship selected
	UpdateStartButton()

	TGObject.CallNextHandler(pEvent)


def FinishedSelectHandler (TGObject, pEvent):
	# Allow the Options Window to come up
#	App.TopWindow_GetTopWindow().AllowShowOptionsWindow(1)

	# Find the Multiplayer window
	debug(__name__ + ", FinishedSelectHandler")
	pTopWindow = App.TopWindow_GetTopWindow()
	pMultWindow = App.MultiplayerWindow_Cast (pTopWindow.FindMainWindow(App.MWT_MULTIPLAYER))

	# Get the mission pane and hide it.
	pPlayerPane = pMultWindow.GetMissionPane()
	pPlayerPane.SetNotVisible()

	# Send event to host telling him what team we've selected
	if (App.g_kUtopiaModule.IsClient()):
		pNetwork = App.g_kUtopiaModule.GetNetwork()
		if (pNetwork):
			pMessage = App.TGMessage_Create()
			pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet
			
			# Setup the stream.
			kStream = App.TGBufferStream()		# Allocate a local buffer stream.
			kStream.OpenBuffer (256)				# Open the buffer stream with a 256 byte buffer.
			
			# Write relevant data to the stream.
			# First write message type.
			kStream.WriteChar(chr(Mission10.TEAM_MESSAGE))

			# Write this player's id
			kStream.WriteLong(pNetwork.GetLocalID())

			# Write the team selected
			kStream.WriteChar(chr(g_iTeam))

			# Okay, now set the data from the buffer stream to the message
			pMessage.SetDataFromStream(kStream)

			# Send the message.
			pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)

			# We're done.  Close the buffer.
			kStream.CloseBuffer()

	# Start the mission
	StartMission(Multiplayer.MissionMenusShared.g_iSpecies)

	# If we're dedicated server, bring up the options window
	if (App.g_kUtopiaModule.IsHost() and (not App.g_kUtopiaModule.IsClient())):
		# Bring up options again.
		# Find the multiplayer window
		pTopWindow = App.TopWindow_GetTopWindow()
		pMultWindow = App.MultiplayerWindow_Cast(pTopWindow.FindMainWindow(App.MWT_MULTIPLAYER))

		# Hide all panes, make MultiplayerPane visible.
		pMultWindow.HideAllChildren()

		# Hide the entire window and make options window visible.
		pMain = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
		pMain.SetVisible()
		pTopWindow.MoveToFront (pMain)
	else:		
		# Assign myself to this team
		Mission10.g_kTeamDictionary[pNetwork.GetLocalID()] = g_iTeam

	TGObject.CallNextHandler(pEvent)


###############################################################################
#	ResetLimitInfo()	
#	
#	Updates the user interface's limit buttons (time, frag, num players) to
#	reflect the accurate values of this information
#	
#	Args:	None
#	
#	Return:	None
###############################################################################
def ResetLimitInfo():
        # player limit
	debug(__name__ + ", ResetLimitInfo")
	pcString = Multiplayer.MissionShared.g_pDatabase.GetString("Num Players").GetCString()
	pcString = pcString % str(Multiplayer.MissionMenusShared.g_iPlayerLimit)
	pString = App.TGString(pcString)
	Multiplayer.MissionMenusShared.g_pPlayerLimitButton.SetName(pString)

	# time limit
	if (Multiplayer.MissionMenusShared.g_iTimeLimit == -1):
		Multiplayer.MissionMenusShared.g_pTimeLimitButton.SetName(Multiplayer.MissionShared.g_pDatabase.GetString("None"))
	else:
		pString = Multiplayer.MissionShared.g_pDatabase.GetString("Num Minutes")
		pcString = pString.GetCString()

		pcSubString = pcString % str(Multiplayer.MissionMenusShared.g_iTimeLimit)

		pNewString = App.TGString()
		pNewString.SetString(pcSubString)

		Multiplayer.MissionMenusShared.g_pTimeLimitButton.SetName(pNewString)

	# Frag limit
	if (Multiplayer.MissionMenusShared.g_iFragLimit == -1):
		Multiplayer.MissionMenusShared.g_pFragLimitButton.SetName(Multiplayer.MissionShared.g_pDatabase.GetString("None"))
	else:
		pString = None
		pcSubString = None
		if (Multiplayer.MissionMenusShared.g_iUseScoreLimit):
			pString = Multiplayer.MissionShared.g_pDatabase.GetString("Num Points")
			pcString = pString.GetCString()
			pcSubString = pcString % str (Multiplayer.MissionMenusShared.g_iFragLimit * 10000)
		else:
			pString = Multiplayer.MissionShared.g_pDatabase.GetString("Num Frags")
			pcString = pString.GetCString()
			pcSubString = pcString % str (Multiplayer.MissionMenusShared.g_iFragLimit)

		pNewString = App.TGString()
		pNewString.SetString(pcSubString)

		Multiplayer.MissionMenusShared.g_pFragLimitButton.SetName(pNewString)


def UpdateStartButton():
	debug(__name__ + ", UpdateStartButton")
	if App.g_kUtopiaModule.IsHost() and (not App.g_kUtopiaModule.IsClient()):
		Multiplayer.MissionMenusShared.g_pStartButton.SetEnabled ()
		return
	elif Multiplayer.MissionMenusShared.g_iSpecies != 0:
		Multiplayer.MissionMenusShared.g_pStartButton.SetEnabled()
		return

	# if we get here, the start button should be disabled since something wasn't
	# selected yet.
	Multiplayer.MissionMenusShared.g_pStartButton.SetDisabled()


# Looks like this is disabled in Multiplayer by default...
def TacticalToggleHandler(pObject, pEvent):
        debug(__name__ + ", TacticalToggleHandler")
        pTop = App.TopWindow_GetTopWindow()
        pTop.ToggleBridgeAndTactical()


def LoadBridge():
        debug(__name__ + ", LoadBridge")
        global myMultBridge, useBridge, BridgeStartOnce
	import LoadBridge
	
        if useBridge == 0:
	#	if not BridgeStartOnce:
	#		LoadBridge.CreateCharacterMenus()
	#	BridgeStartOnce = 1
		return

        # We have to manually import the bridge Fixes, if present.
        try:
                import Fixes20030217
                Bridge.Characters.CommonAnimations.SetPosition = Fixes20030217.SetPosition
                LoadBridge.Load = Fixes20030217.LoadBridge_Load
        except:
                pass

	LoadBridge.Load(myMultBridge)

        pTopWindow = App.TopWindow_GetTopWindow()
        pTopWindow.AddPythonFuncHandlerForInstance(App.ET_INPUT_TOGGLE_BRIDGE_AND_TACTICAL, __name__ + ".TacticalToggleHandler")
        # finally enable ViewScreen
        pViewscreen = MissionLib.GetViewScreen()
        pViewscreen.LookTowardsSpace()


def CheckActiveMutator(MutatorName):
	debug(__name__ + ", CheckActiveMutator")
	global FoundationMode
	if FoundationMode == 0:
		return 0
        Foundation.LoadConfig()
	for i in Foundation.mutatorList._arrayList:
		fdtnMode = Foundation.mutatorList._keyList[i]
		if fdtnMode.IsEnabled() and (fdtnMode.name == MutatorName):
			return 1
	return 0


# only Load if present:
def LoadATP():
        debug(__name__ + ", LoadATP")
        global useBridge
	ATP = 0
        # Load valid config first
	if CheckActiveMutator("ATP 3"):
		ATP = 1
	if ATP == 0:# or useBridge == 0:
		return
        import Custom.AdvancedTechnologies.Data.QuickBattleAddon
        Custom.AdvancedTechnologies.Data.QuickBattleAddon.SetupEventHandlersForMP()


# only Load if present:
def LoadTech(mode=0):
        debug(__name__ + ", LoadTech")
        global useBridge
	Tech = 0
        myVersion = 0
        # Load valid config first
	if CheckActiveMutator("New Technology System"):
		Tech = 1
                # Get the Version:
                pModule = __import__("ftb.FTB_MissionLib")
                if hasattr(pModule, "MODINFO"):
                        MODINFO = pModule.MODINFO
                        if MODINFO.has_key("Version"):
                                myVersion = int(MODINFO["Version"])
                                
	if Tech == 0 or myVersion < 20041201:
		return
        if mode == 0:
                import techfunc
                techfunc.ImportTechs()
        elif mode == 2:
                import ftb.LaunchShipHandlers
                ftb.LaunchShipHandlers.MissionRestart(None, None)


# only Load if present:
def LoadQBautostart(Load=1):
        debug(__name__ + ", LoadQBautostart")
        global useBridge
	QBautostart = 0
        # Load valid config first
	if CheckActiveMutator("QBautostart Extension V0.8"):
                if useBridge == 0:
                        return
		QBautostart = 1
        elif CheckActiveMutator("QBautostart Extension V0.9") or CheckActiveMutator("QBautostart Extension V1.0"):
                QBautostart = 1
	if QBautostart == 0:
		return
	
	#if (TestsItsMd5("scripts\\Custom\\Autoload\\LoadEngineeringExtension.py") == 0):
	#	print("Failed checking MD5 of QBautostart LoadQBautostart.py")
	#	return
	#if (TestsItsMd5("scripts\\Custom\\QBautostart\\Libs\\LibEngineering.py") == 0):
	#	print("Failed checking MD5 of QBautostart LibEngineering.py")
	#	return
	from Custom.Autoload.LoadEngineeringExtension import LoadQBautostart
	if Load == 1:
		LoadQBautostart.MultImportQBautostart(QBrestart=0)
	elif Load == 2:
		LoadQBautostart.MultImportQBautostart(QBrestart=1)
	else:
		LoadQBautostart.EngineeringInit = 0


def LoadTechExpansion():
        debug(__name__ + ", LoadTechExpansion")
        global useBridge
        TechExpansion = 0
        #if CheckActiveMutator("Cloaked Firing"):
        #        TechExpansion = 1
        
        #if TechExpansion == 0 or useBridge == 0:
	#	return
                
        #import Custom.TechnologyExpansion.Scripts.CloakedFiring.LoadMenu
        #Custom.TechnologyExpansion.Scripts.CloakedFiring.LoadMenu.LoadMenu()
        if CheckActiveMutator("Blind Firing"):
                import Custom.TechnologyExpansion.Scripts.BlindFiring.LoadMenu
		Custom.TechnologyExpansion.Scripts.BlindFiring.LoadMenu.LoadMenu()
        if CheckActiveMutator("Thrusters"):
                import Custom.Autoload.Thrusters
                Custom.Autoload.Thrusters.PrepareThrusters()


def GetFoundationShip(ShipType):
        debug(__name__ + ", GetFoundationShip")
        i = 0
        for k in Foundation.shipList:
                if Foundation.shipList[i].shipFile == ShipType:
                        return Foundation.shipList[i]
                i = i + 1
        return None


def CreateSystemFromSpecies(mySystem):
	debug(__name__ + ", CreateSystemFromSpecies")
	return Multiplayer.Episode.Mission4.Mission4Menus.CreateSystemFromSpecies(mySystem)


def TargetChanged(pObject, pEvent):
        debug(__name__ + ", TargetChanged")

	pPlayer = MissionLib.GetPlayer()
	Mission10.SendTargetChanged(pPlayer)

	if (pObject and pEvent):
		pObject.CallNextHandler(pEvent)


def StartMission(iSpecies):
        debug(__name__ + ", StartMission")
        global g_pPlayerButton, g_pShipsButton, qbGameMode, g_pMiscButton, FoundationMode, dSets
        global g_pUseBridgeButton, StartMissionRunOnce, g_pMusicType, pOldMusic, SetShipID, QBGameModeActivated

	# Specify (and load if necessary) our bridge
	
	# Load the Bridge
	LoadBridge()
	
	global Mission10StartOnce
	if not Mission10StartOnce and not useBridge:
		Mission10StartOnce = 1
		pMission = MissionLib.GetMission()		
		Multiplayer.MissionShared.SetupEventHandlers(pMission)
		
	# Get the current game.  We use this in various places below.
	pGame = App.Game_GetCurrentGame()
	pMultGame = App.MultiplayerGame_Cast(pGame)	# Cast the game to a multiplayer game

	# Starting sets
	sSelectedTeam = Races.keys()[g_iTeam]
	if App.g_kUtopiaModule.IsHost() and not Multiplayer.MissionMenusShared.g_bGameStarted:
		for mySystem in lStartingSets:
			pSet = Multiplayer.Episode.Mission4.Mission4Menus.CreateSystemFromSpecies(mySystem)
			dSets[mySystem] = pSet 

			if not hasattr(Races[sSelectedTeam], "iStartingSet") and iDefaultStartingSet == mySystem:
				Multiplayer.MissionShared.g_pStartingSet = pSet
			if hasattr(Races[sSelectedTeam], "iStartingSet") and Races[sSelectedTeam].iStartingSet == mySystem:
				Multiplayer.MissionShared.g_pStartingSet = pSet
	else:
		for mySystem in lStartingSets:
			if not hasattr(Races[sSelectedTeam], "iStartingSet") and iDefaultStartingSet == mySystem:
				Multiplayer.MissionShared.g_pStartingSet = dSets[mySystem]
			if hasattr(Races[sSelectedTeam], "iStartingSet") and Races[sSelectedTeam].iStartingSet == mySystem:
				Multiplayer.MissionShared.g_pStartingSet = dSets[mySystem]
		
	CreateSystemMenuEntrys()

	pSet = Multiplayer.MissionShared.g_pStartingSet
        if not pSet:
		print "Set is NULL!"
		return
        
	###################################################
	#This next section will create the ships and set their stats

	#Determine if we need to create the player's ship.
	if (iSpecies != Multiplayer.SpeciesToShip.UNKNOWN):
		# We've got a valid species.  Create the player's ship.
		
		pPlayer = None
		bUsingExisting = 0
		sShipScript = Multiplayer.SpeciesToShip.GetScriptFromSpecies(iSpecies)
		for pSet in App.g_kSetManager.GetAllSets():
			lObjects = pSet.GetClassObjectList(App.CT_SHIP)
			for pObject in lObjects:
				pShip = App.ShipClass_Cast(pObject)
				if not pShip:
					continue
				
				if pShip.GetScript() == 'ships.' + sShipScript:
					bUsingExisting = 1
                        		kLocation = pShip.GetWorldLocation()
					kForward = pShip.GetWorldForwardTG()
					kUp = pShip.GetWorldUpTG()
					iShipOldID = pShip.GetObjID()
					break
		
		
		pPlayer = Multiplayer.MissionMenusShared.CreateShip(iSpecies)
		if (pPlayer != None):
			if not bUsingExisting:
				pPlayer.RandomOrientation()
				pPlayer.UpdateNodeOnly()

			pNetwork = App.g_kUtopiaModule.GetNetwork()
			if (pNetwork):
				pPlayer.SetNetPlayerID(pNetwork.GetLocalID())

			# Get the player's name from the network.
			pNetwork = App.g_kUtopiaModule.GetNetwork()
			if (not App.IsNull(pNetwork)):
				pcName = pNetwork.GetCName()
			else:
				pcName = "N/A"

			# Determine if there is already a ship with the same name.
			pcOrigName = pcName
			i = 0
			iCount = 1
			while (i == 0):
				pObj = App.BaseObjectClass_GetObject(None, pcName)
				if (pObj):
					# Yes, an object already exists.  We need to create
					# a new name
					pcName = pcOrigName
					pcName = pcName + str (iCount)
					iCount = iCount + 1
				else:
					i = 1

			# randomly locate the player's ship.
			fRadius = pPlayer.GetRadius() * 1.25

			if not bUsingExisting:
				kPos = Multiplayer.MissionMenusShared.FindGoodLocation(pSet, fRadius)
				pPlayer.SetTranslate(kPos)
			else:
				Mission10.MPGetShipAttributes(pShip)
				Mission10.DeleteObjectFromSet(pSet, pShip)
				Mission10.MPSetShipAttributes(pPlayer, iShipOldID)
				pPlayer.SetTranslate(kLocation)
				pPlayer.AlignToVectors(kForward, kUp)
			
			# Add the ship to the set.
			pSet.AddObjectToSet(pPlayer, pcName)

			pMultGame.SetPlayer(pPlayer)

			# Add event handler for when this ship is destroyed.
			# Find the Multiplayer window
			pTopWindow = App.TopWindow_GetTopWindow()
			pMultWindow = App.MultiplayerWindow_Cast(pTopWindow.FindMainWindow(App.MWT_MULTIPLAYER))

			# Add broadcast handler for when an object is destroyed.  This handler will bring up the mission pane
			# again if the player's ship is destroyed.
			pPlayerPane = pMultWindow.GetMissionPane()
			App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_DELETE_OBJECT_PUBLIC, pPlayerPane, __name__ + ".myObjectDestroyedHandler")
			pPlayer.AddPythonFuncHandlerForInstance(App.ET_TARGET_WAS_CHANGED,	__name__ + ".TargetChanged")
			pPlayer.AddPythonFuncHandlerForInstance(App.ET_SET_TARGET,			__name__ + ".TargetChanged")

			# Player got a new ship...
			Mission10.InformAboutShipBuild(g_iTeam, iSpecies)
			
	# Hide select region menu and move ship selection menu into it's proper place
	pTopWindow = App.TopWindow_GetTopWindow()
	if (App.g_kUtopiaModule.IsHost()):
		Multiplayer.MissionMenusShared.g_pSystemPane.SetNotVisible()
		Multiplayer.MissionMenusShared.g_pSystemIcon.SetNotVisible()
		Multiplayer.MissionMenusShared.g_pSystemDescPane.SetNotVisible()

		Multiplayer.MissionMenusShared.g_pInfoPane.SetVisible()

		if (not App.g_kUtopiaModule.IsClient()):
			# Dedicated server.  Disable options toggling.
			pTopWindow.DisableOptionsMenu(1)	
			pResumeButton = App.STRoundedButton_Cast(App.TGObject_GetTGObjectPtr(MainMenu.mainmenu.g_idResumeButton))
			if (pResumeButton):
				pResumeButton.SetDisabled()

	# Force tactical view
	if (App.g_kUtopiaModule.IsClient()):
		# Now force tactical view.
		pTopWindow.ForceTacticalVisible()

	# Ready for new players to join.  Notify the game of this.
	if (App.g_kUtopiaModule.IsHost()):
		if (not pMultGame.IsReadyForNewPlayers()):
			pMultGame.SetReadyForNewPlayers(1)				# Set flag to ready

		if (not Multiplayer.MissionMenusShared.g_bGameStarted):
			# Set time left for this mission if there's a time limit.
			if (Multiplayer.MissionMenusShared.g_iTimeLimit != -1):
				Multiplayer.MissionShared.CreateTimeLeftTimer (Multiplayer.MissionMenusShared.g_iTimeLimit * 60)
			Multiplayer.MissionMenusShared.g_bGameStarted = 1

	# rebuild the scoreboard to accurately display things
	RebuildPlayerList()
        
        # Hide Select Buttons
        #g_pUseBridgeButton.SetDisabled()
        g_pPlayerButton.SetNotVisible()
        #g_pShipsButton.SetNotVisible()
        g_pMiscButton.SetNotVisible()

	# reset warp speed to default
	try:
		from Custom.QBautostart.Libs.LibWarp import SetCurWarpSpeed, iDefaultSpeed
		pPlayer = MissionLib.GetPlayer()
		SetCurWarpSpeed(pPlayer, iDefaultSpeed)
	except ImportError:
		pass

        # Load Foundation
	if FoundationMode == 1:
                # play Music
                pPlayer = MissionLib.GetPlayer()
                if pPlayer:
                        ShipType = string.split(pPlayer.GetScript(), '.')[-1]
                        g_sPlayerType = GetFoundationShip(ShipType)
                        if g_sPlayerType and hasattr(g_sPlayerType, "GetMusic"):
                                g_pMusicType = g_sPlayerType.GetMusic()
                                if g_pMusicType != pOldMusic:
                                        DynamicMusic.StopMusic()
                                        g_pMusicType.ChangeMusic(DynamicMusic.StandardCombatMusic)
                                        pOldMusic = g_pMusicType
                
                if StartMissionRunOnce == 0:
                        print ("Mission10 starting")
		        qbGameMode.Activate()
			QBGameModeActivated = 1
                        # start QBautostart
                        LoadQBautostart()
                        # Shuttle Launching framework
                        LoadTech()
                        # ATP 3
                        LoadATP()
                        # Technology Expansion
                        LoadTechExpansion()
			# cwp 2.0
			try:
				import Custom.Autoload.SovNFX2Fix
				import Custom.NanoFXv2.WarpFX.WarpFX_GUI
				Custom.NanoFXv2.WarpFX.WarpFX_GUI.SetupButtons()
			except ImportError:
				pass
				
                        StartMissionRunOnce = 1
			
			Multiplayer.Episode.Mission4.Mission4Menus.HandleGalaxyCharts()
                else:
                        print ("Mission10 restarting")
                        # Restart Engineering
                        LoadQBautostart(2)
                        # Tech
                        LoadTech(2)
                        
                # restore the real SetShipID if needed.
                if CheckActiveMutator("Foundation Technologies"):
                        Tactical.Interface.ShipDisplay.SetShipID = SetShipID


def IncTeam():
	debug(__name__ + ", IncTeam")
	global g_iTeam
	g_iTeam = g_iTeam + 1
	
	if g_iTeam >= len(Races.keys()):
		g_iTeam = 0
	if Races.keys()[g_iTeam] == "GodShips":
		g_iTeam = g_iTeam + 1
	if g_iTeam >= len(Races.keys()):
		g_iTeam = 0


def SelectTeamHandler(pSelf, pEvent):
	debug(__name__ + ", SelectTeamHandler")
	IncTeam()

	# Update interface.
	g_pTeamButton.SetName(App.TGString(Races.keys()[g_iTeam]))
	RebuildShipSelectWindow()

	pSelf.CallNextHandler(pEvent)


# New version		
def RebuildInfoPane():        
#	print ("Rebuilding info pane")

	debug(__name__ + ", RebuildInfoPane")
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	if (not pNetwork):
		# Don't rebuild the list since you can't
		return

	pDatabase = Multiplayer.MissionShared.g_pDatabase

	pOrigFontGroup = App.g_kFontManager.GetDefaultFont()

	# Set the font small
	App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcSmallFont,
				MainMenu.mainmenu.g_kSmallFontSize[MainMenu.mainmenu.g_iRes])

	# Kill all the children in the info pane, since we will be rebuilding it from scratch.
	Multiplayer.MissionMenusShared.g_pInfoPane.KillChildren()
	
	pText = App.TGParagraph_CreateW(Multiplayer.MissionShared.g_pDatabase.GetString("Mission System"))
	pText.SetColor(App.g_kTitleColor)
	Multiplayer.MissionMenusShared.g_pInfoPane.AddChild(pText, Multiplayer.MissionMenusShared.SYSTEM_WINDOW_X_POS, Multiplayer.MissionMenusShared.SYSTEM_WINDOW_Y_POS - pText.GetHeight () - 0.005, 0)
	fWidth = pText.GetWidth()

	pText = App.TGParagraph_CreateW(pDatabase.GetString("Unknown"))

	pText.SetColor(App.g_kSTMenuTextHighlightColor)
	Multiplayer.MissionMenusShared.g_pInfoPane.AddChild(pText, Multiplayer.MissionMenusShared.SYSTEM_WINDOW_X_POS + fWidth + 0.005, Multiplayer.MissionMenusShared.SYSTEM_WINDOW_Y_POS - pText.GetHeight () - 0.005, 0)

	# Build the stylized window.
	fHeight = Multiplayer.MissionMenusShared.SYSTEM_DESC_WINDOW_Y_POS + Multiplayer.MissionMenusShared.SYSTEM_DESC_WINDOW_HEIGHT - Multiplayer.MissionMenusShared.SYSTEM_WINDOW_Y_POS
	pWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", pDatabase.GetString("Players In Game"), 
						0.0, 0.0, None, 1, Multiplayer.MissionMenusShared.SYSTEM_WINDOW_WIDTH, fHeight)
	pWindow.SetTitleBarThickness(Multiplayer.MissionMenusShared.SYSTEM_WINDOW_BAR_THICKNESS)
	Multiplayer.MissionMenusShared.g_pInfoPane.AddChild(pWindow, Multiplayer.MissionMenusShared.SYSTEM_WINDOW_X_POS, Multiplayer.MissionMenusShared.SYSTEM_WINDOW_Y_POS, 0)
  
	# Build player list pane.
	pListPane = App.STSubPane_Create(Multiplayer.MissionMenusShared.SYSTEM_WINDOW_WIDTH, 500.0)
	
	pMultGame = App.MultiplayerGame_Cast(App.Game_GetCurrentGame())

	# Display the team
	iTeam = 0

	pTeamScoresDict = Mission10.g_kTeamScoreDictionary
	pTeamKillsDict = Mission10.g_kTeamKillsDictionary
	pTeamDict = Mission10.g_kTeamDictionary 

	for iTeam in range(len(Races.keys())):
		pcTeamName = Races.keys()[iTeam]
		if pcTeamName == "GodShips":
			continue

		pText = App.TGParagraph_Create(pcTeamName)
		pListPane.AddChild(pText, 0, 0, 0)

		# Display the players on this team.
		pPlayerList = pNetwork.GetPlayerList()
		iNumPlayers = pPlayerList.GetNumPlayers()
		i = 0
		while (i < iNumPlayers):
			pPlayer = pPlayerList.GetPlayerAtIndex(i)
			
			if (pTeamDict.has_key(pPlayer.GetNetID()) and pPlayer.IsDisconnected() == 0):
				 # This player is on a team.  See if he's on my team.
				 if (pTeamDict [pPlayer.GetNetID()] == iTeam):
					pPane = CreatePlayerInfoEntry(pPlayer, pMultGame)

					pListPane.AddChild(pPane, 0.05, 0, 0)

			# Increment the index to look at the next player.				
			i = i + 1

	pListPane.Resize(pListPane.GetWidth(), pListPane.GetTotalHeightOfChildren(), 0)

	pWindow.AddChild(pListPane, 0, 0, 0)	
	pWindow.Layout()
	pWindow.InteriorChangedSize()
	
	# Restore default font
	App.g_kFontManager.SetDefaultFont(pOrigFontGroup.GetFontName(), pOrigFontGroup.GetFontSize())

	Multiplayer.MissionMenusShared.g_pInfoPane.Layout()


def CreatePlayerInfoEntry (pPlayer, pMultGame):
	# create a pane to hold everything.
	debug(__name__ + ", CreatePlayerInfoEntry")
	pPlayerEntryPane = App.TGPane_Create (Multiplayer.MissionMenusShared.SYSTEM_WINDOW_WIDTH, 0.1)

	pDatabase = Multiplayer.MissionShared.g_pDatabase

	# Create the player name text
#	pPane = App.TGPane_Create (Multiplayer.MissionMenusShared.SYSTEM_WINDOW_WIDTH - 0.1, 0.1)
	pPane = App.TGPane_Create (Multiplayer.MissionMenusShared.SYSTEM_WINDOW_WIDTH, 0.1)
	pText = App.TGParagraph_CreateW(pPlayer.GetName())
	pPane.AddChild(pText, 0.01, 0, 0)
	pPlayerEntryPane.PrependChild(pPane, 0, 0, 0)

	fHeight = pText.GetHeight()
	fWidth = pText.GetWidth()

	# Resize the player entry pane
	pPlayerEntryPane.Resize(Multiplayer.MissionMenusShared.SYSTEM_WINDOW_WIDTH, fHeight, 0)

	# Create ship text
	iPlayerID = pPlayer.GetNetID()
	pShip = pMultGame.GetShipFromPlayerID(iPlayerID)
	pcText = ""
	if (pShip):
		# Get the type from the ship.
		iType = pShip.GetNetType()
		if (pShip.IsDying() or pShip.IsDead()):
			pString = pDatabase.GetString("Dead")
		else:
			if (iType == 0):
				# Don't know what ship.  Display unknown
#				print ("Got ship but don't know what type")
				pString = pDatabase.GetString("Unknown")
			else:
				pString = Multiplayer.MissionShared.g_pShipDatabase.GetString (Multiplayer.SpeciesToShip.GetScriptFromSpecies (iType))
	else:
		# Don't know what ship.  Display unknown
#		print ("Didn't get ship")
		pString = pDatabase.GetString ("Unknown")

	pcString = pString.GetCString ()
	pcText = " - " + pcString

	pText = App.TGParagraph_Create (pcText)

	pPane.AddChild (pText, 0.01 + fWidth, 0, 0)

	# Create the score
	# Get the death total from the score dictionaries
#	pDict = Mission10.g_kScoresDictionary

#	iScore = 0
#	if (pDict.has_key (iPlayerID)):
#		iScore = pDict [iPlayerID]
#
#	pText = App.TGParagraph_Create (str (iScore) + "pts")
#	pPlayerEntryPane.AddChild (pText, Multiplayer.MissionMenusShared.SYSTEM_WINDOW_WIDTH - 0.1, 0, 0)

	return pPlayerEntryPane


###############################################################################
#	BuildMissionSpecificOptionsMenuPane()
#	
#	Builds the scoreboard along with the boot button that you see when you
#	press ESCAPE while playing in deathmatch mode
#	
#	Args:	TGPane*	pEventPane	- the pane that handles our events
#	
#	Return:	None
###############################################################################
def BuildMissionSpecificOptionsMenuPane(pEventPane):	
	debug(__name__ + ", BuildMissionSpecificOptionsMenuPane")
	if App.g_kUtopiaModule.IsHost() and App.g_kUtopiaModule.IsClient():
		pSubtitle = Multiplayer.MissionShared.g_pDatabase.GetString("The Border Skirmish Host")
	elif App.g_kUtopiaModule.IsClient():
		pSubtitle = Multiplayer.MissionShared.g_pDatabase.GetString("The Border Skirmish Client")
	else:
		pSubtitle = Multiplayer.MissionShared.g_pDatabase.GetString("The Border Skirmish Direct Host")
	pPane = Multiplayer.MultiplayerMenus.GetMissionPane(pSubtitle)

	# We want our stylized window to take up 3/4 of the available height in
	# the pane, and to be centered
	fScoreWindowWidth = 0.5125
	fScoreWindowHeight = pPane.GetHeight() * 0.75
	fScoreXPos = (pPane.GetWidth() - fScoreWindowWidth) / 2.0 
	fScoreYPos = (pPane.GetHeight() - fScoreWindowHeight) / 2.0

	# Set the font larger
	App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcSmallFont,
				MainMenu.mainmenu.g_kSmallFontSize[MainMenu.mainmenu.g_iRes])

	# Create Player, Kills, Deaths, and Score text
	pTextPane = App.TGPane_Create(0.175, 0.04)
	pText = App.TGParagraph_CreateW(Multiplayer.MissionShared.g_pDatabase.GetString("Player"))
	pText.SetColor(App.g_kMultiplayerBorderBlue)
	pTextPane.AddChild(pText, 0.0, 0.0, 0)
	pTextPane.Resize(0.175, pText.GetHeight(), 0)
	pPane.AddChild(pTextPane, 0.10 + fScoreXPos + 0.0105, fScoreYPos + 0.03, 0)

	pTextPane = App.TGPane_Create(0.065, 0.1)
	pText = App.TGParagraph_CreateW(Multiplayer.MissionShared.g_pDatabase.GetString("Kills"))
	pText.SetColor(App.g_kMultiplayerBorderBlue)
	pTextPane.AddChild(pText, 0.0, 0.0, 0)
	pTextPane.Resize(0.08, pText.GetHeight(), 0)
	pPane.AddChild(pTextPane, 0.27 + fScoreXPos + 0.0105, fScoreYPos + 0.03, 0)
	
	pTextPane = App.TGPane_Create(0.065, 0.1)
	pText = App.TGParagraph_CreateW(Multiplayer.MissionShared.g_pDatabase.GetString("Deaths"))
	pText.SetColor(App.g_kMultiplayerBorderBlue)
	pTextPane.AddChild(pText, 0.0, 0.0, 0)
	pTextPane.Resize(0.08, pText.GetHeight(), 0)
	pPane.AddChild(pTextPane, 0.335 + fScoreXPos + 0.0105, fScoreYPos + 0.03, 0)

	# Build the black header the goes behind the captions.
	# Its purpose is to cover up menu items that scroll up behind it.
	# It handles events so that they won't reach any buttons that it's
	# covering up.
	pHeader = App.TGIcon_Create(App.GraphicsModeInfo_GetCurrentMode().GetLcarsString(), 200)
	pHeader.SetColor(App.NiColorA_BLACK)
	pHeader.Resize(0.502, 0.04, 0)
	pHeader.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__ + ".HandleMouseEventsForGlass")
	pPane.AddChild(pHeader,	fScoreXPos + 0.0105, fScoreYPos + 0.03, 0)

	# Create the stylized window in which our player list will go
	pWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", 
		Multiplayer.MissionShared.g_pDatabase.GetString("Score Board"), 0.0,
		0.0, None, 1, fScoreWindowWidth, fScoreWindowHeight)
	pWindow.SetTitleBarThickness(0.03, 0)
	pPane.AddChild(pWindow, fScoreXPos, fScoreYPos, 0)

	# Create a subpane inside of which will go the player list. It will be the nice,
	# unassuming, docile sort of subpane which obediently resizes itself to fit snugly
	# within its parent StylizedWindow
	global g_pOptionsWindowPlayerMenu, g_pOptionsWindowPlayerMenuWindow
	g_pOptionsWindowPlayerMenu = App.STSubPane_Create(0.0, 0.0, 1)
	g_pOptionsWindowPlayerMenuWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("test"))
	g_pOptionsWindowPlayerMenuWindow.SetUseScrolling(0)
	g_pOptionsWindowPlayerMenuWindow.SetFixedSize(0.5, 1.0)
	g_pOptionsWindowPlayerMenuWindow.AddChild(g_pOptionsWindowPlayerMenu)
	pWindow.AddChild(g_pOptionsWindowPlayerMenuWindow, 0.0, 0.0)
	pWindow.InteriorChangedSize(1)
	
	# We want the boot button to take up about 1/3 of the space under the
	# stylized window, horizontally, 2/5 of the space under it vertically,
	# and to be centered under it along both axes. It should be disabled if we're
	# not the host
	fBootButtonWidth = fScoreWindowWidth * (1.0/3.0)
	fBootButtonHeight = (pPane.GetHeight() - (fScoreWindowHeight + fScoreYPos)) * 0.4
	fBootButtonXPos = (pPane.GetWidth() - fBootButtonWidth) / 2.0
	fBootButtonYPos = (((pPane.GetHeight() - (fScoreWindowHeight + fScoreYPos)) - fBootButtonHeight) / 2.0) + fScoreWindowHeight + fScoreYPos

	pEvent = App.TGEvent_Create()
	pEvent.SetEventType(ET_BOOT_BUTTON_CLICKED)
	pEvent.SetDestination(pEventPane)

	pBanEvent = App.TGEvent_Create()
	pBanEvent.SetEventType(ET_BAN_BUTTON_CLICKED)
	pBanEvent.SetDestination(pEventPane)

	global g_pOptionsWindowBootButton
	global g_pOptionsWindowBanButton

	g_pOptionsWindowBootButton = App.STButton_CreateW(
		Multiplayer.MissionShared.g_pDatabase.GetString("Boot"),
		pEvent, 0, fBootButtonWidth, fBootButtonHeight)
	g_pOptionsWindowBootButton.SetJustification(App.STButton.CENTER)
	g_pOptionsWindowBootButton.SetNormalColor(App.g_kMainMenuButtonColor)
	g_pOptionsWindowBootButton.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
	g_pOptionsWindowBootButton.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
	g_pOptionsWindowBootButton.SetColorBasedOnFlags()
	g_pOptionsWindowBootButton.SetDisabled(0)

	g_pOptionsWindowBanButton = App.STButton_CreateW(Multiplayer.MissionShared.g_pDatabase.GetString("Ban"),
		pBanEvent, 0, fBootButtonWidth, fBootButtonHeight)
	g_pOptionsWindowBanButton.SetJustification(App.STButton.CENTER)
	g_pOptionsWindowBanButton.SetNormalColor(App.g_kMainMenuButtonColor)
	g_pOptionsWindowBanButton.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
	g_pOptionsWindowBanButton.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
	g_pOptionsWindowBanButton.SetColorBasedOnFlags()
	g_pOptionsWindowBanButton.SetDisabled(0)

	pPane.AddChild(g_pOptionsWindowBootButton, fBootButtonXPos, fBootButtonYPos, 0)
	pPane.AddChild(g_pOptionsWindowBanButton, 
				   fBootButtonXPos + g_pOptionsWindowBootButton.GetWidth() + (App.globals.DEFAULT_ST_INDENT_HORIZ * 2.0),
				   fBootButtonYPos, 0)

	pPane.Layout()

	# Go back to the flight font
	App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcFlightSmallFont,
				MainMenu.mainmenu.g_kFlightSmallFontSize[MainMenu.mainmenu.g_iRes])

###############################################################################
#	HandleMouseEventsForGlass()
#	
#	There are times that we want to cover up some UI elements with glass.
#	We have to make sure the user can't click on them, so we make the glass
#	handle mouse events before letting them pass underneath
#	
#	Args:	TGObject*	pObject	- the glass
#			TGEvent*	pEvent	- the ET_MOUSE_EVENT
#	
#	Return:	
###############################################################################
def HandleMouseEventsForGlass(pObject, pEvent):
	debug(__name__ + ", HandleMouseEventsForGlass")
	pEvent.SetHandled()
	pObject.CallNextHandler(pEvent)


###############################################################################
#	OpenShipsPane()
#
#	Show the ships subpane and hide the player subpane
#
#	Args:	TGObject	pObject	- NULL  Don't use this
#			TGIntEvent	pEvent	- ET_OPEN_DIALOG event
#
#	Return:	none
###############################################################################
def OpenShipsPane(pObject, pEvent):
	debug(__name__ + ", OpenShipsPane")
	global pPlayerPane, pShipsPane, pMiscPane, g_pShipsButton, g_pPlayerButton, g_pMiscButton
	
	pPlayerPane.SetNotVisible()
        pMiscPane.SetNotVisible()
	pShipsPane.SetVisible()
	g_pShipsButton.SetSelected()
	g_pPlayerButton.SetNotSelected()
        #g_pMiscButton.SetNotSelected()
        pMultWindow = g_pShipsButton.GetParent()
        pMultWindow.MoveToFront(g_pShipsButton) # They lost focus, move them to front
        pMultWindow.MoveToFront(g_pPlayerButton)
        #pMultWindow.MoveToFront(g_pMiscButton)


###############################################################################
#	OpenPlayerPane()
#
#	Show the player subpane and hide the ships subpane
#
#	Args:	TGObject	pObject	- NULL  Don't use this
#			TGIntEvent	pEvent	- ET_OPEN_DIALOG event
#
#	Return:	none
###############################################################################
def OpenPlayerPane(pObject, pEvent):
	debug(__name__ + ", OpenPlayerPane")
	global pPlayerPane, pShipsPane, pMiscPane, g_pShipsButton, g_pPlayerButton, g_pMiscButton
	
	#pShipsPane.SetNotVisible()
        pMiscPane.SetNotVisible()
	pPlayerPane.SetVisible()
        g_pPlayerButton.SetSelected()
	#g_pShipsButton.SetNotSelected()
        g_pMiscButton.SetNotSelected()


def OpenMiscPane(pObject, pEvent):
	debug(__name__ + ", OpenMiscPane")
	global pPlayerPane, pShipsPane, pMiscPane, g_pShipsButton, g_pPlayerButton, g_pMiscButton
	pPlayerPane.SetNotVisible()
        pMiscPane.SetVisible()
	#pShipsPane.SetNotVisible()
	#g_pShipsButton.SetNotSelected()
	g_pPlayerButton.SetNotSelected()
        g_pMiscButton.SetSelected()
        pMultWindow = g_pPlayerButton.GetParent()
        #pMultWindow.MoveToFront(g_pShipsButton) # They lost focus, move them to front
        pMultWindow.MoveToFront(g_pPlayerButton)
        pMultWindow.MoveToFront(g_pMiscButton)


def BuildMiscPane():
        debug(__name__ + ", BuildMiscPane")
        global FoundationMode, qbGameMode, useBridge, g_pUseBridgeButton
        pMiscPane = App.TGPane_Create(SUB_PANE_WIDTH, SUB_PANE_HEIGHT)
	
	pEyeCandyPane = App.TGPane_Create (1.0, 1.0)
	#########################################
	# Create eye candy
	pGraphicsMode = App.GraphicsModeInfo_GetCurrentMode()
	pcLCARS = pGraphicsMode.GetLcarsString()
        pDatabase = Multiplayer.MissionShared.g_pDatabase

	# Set the font small
	App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcFlightSmallFont,
				MainMenu.mainmenu.g_kFlightSmallFontSize[MainMenu.mainmenu.g_iRes])

	# Create the little "190" that's in the lower-left curve
	p190 = App.TGParagraph_Create("190", 1.0, App.g_kSTMenuTextColor)
	pEyeCandyPane.AddChild(p190, NUMBER_190_X_POS, NUMBER_190_Y_POS, 0)
	
	# Create the little "945" that's in RightBar1
	p945 = App.TGParagraph_Create("945", 1.0, App.g_kSTMenuTextColor)
	pEyeCandyPane.AddChild(p945, NUMBER_945_X_POS, NUMBER_945_Y_POS, 0)

	# Create the little "04" that's in RightBar2
	p04 = App.TGParagraph_Create("04", 1.0, App.g_kSTMenuTextColor)
	pEyeCandyPane.AddChild(p04, NUMBER_04_X_POS, NUMBER_04_Y_POS, 0)

	# Set the font larger
	App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcSmallFont,
				MainMenu.mainmenu.g_kSmallFontSize[MainMenu.mainmenu.g_iRes] + 1)

	# Create the title
	pTitle = App.TGParagraph_CreateW(pDatabase.GetString("Multiplayer"), 1.0, App.globals.g_kTitleColor)
	fPosDelta = (pTitle.GetHeight() - TOP_BAR_HEIGHT) / 2.0
	pEyeCandyPane.AddChild(pTitle, TITLE_X_POS, TOP_BAR_Y_POS - fPosDelta, 0)
	
	# Create the subtitle
        pSubtitle = App.TGParagraph_CreateW(App.TGString("Misc"), 1.0, App.globals.g_kTitleColor)
	pEyeCandyPane.AddChild(pSubtitle, SUBTITLE_X_POS, SUBTITLE_Y_POS, 0)

	# Set the font smaller but still large
	App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcSmallFont,
				MainMenu.mainmenu.g_kSmallFontSize[MainMenu.mainmenu.g_iRes])

	# Create the top bar
	fTopXPos = TITLE_X_POS + pTitle.GetWidth() + TOP_BAR_X_DISTANCE
	fTopWidth = TOP_BAR_RIGHT_EDGE - fTopXPos
	pTopBar = App.TGIcon_Create("NormalStyleFrame", 5, App.globals.g_kInterfaceBorderColor)
	pTopBar.Resize(fTopWidth, TOP_BAR_HEIGHT, 0)
	pEyeCandyPane.AddChild(pTopBar, fTopXPos, TOP_BAR_Y_POS, 0)  

	# Create the first left bar
	pLeftBar1 = App.TGIcon_Create("NormalStyleFrame", 5, App.globals.g_kInterfaceBorderColor)
	pLeftBar1.Resize(LEFT_BAR_1_WIDTH, LEFT_BAR_1_HEIGHT, 0)
	pEyeCandyPane.AddChild(pLeftBar1, LEFT_BAR_1_X_POS, LEFT_BAR_1_Y_POS, 0)  

	# Create the second left bar
	pLeftBar2 = App.TGIcon_Create("NormalStyleFrame", 5, App.globals.g_kMultiplayerBorderBlue)
	pLeftBar2.Resize(LEFT_BAR_2_WIDTH, LEFT_BAR_2_HEIGHT, 0)
	pEyeCandyPane.AddChild(pLeftBar2, LEFT_BAR_2_X_POS, LEFT_BAR_2_Y_POS, 0)  

	# Create the third left bar
	pLeftBar3 = App.TGIcon_Create("NormalStyleFrame", 5, App.globals.g_kMultiplayerBorderPurple)
	pLeftBar3.Resize(LEFT_BAR_3_WIDTH, LEFT_BAR_3_HEIGHT, 0)
	pEyeCandyPane.AddChild(pLeftBar3, LEFT_BAR_3_X_POS, LEFT_BAR_3_Y_POS, 0)  

	# Create the lower-left curve
	pLLCurve = UIHelpers.CreateCurve(UIHelpers.LOWER_LEFT_CURVE, LOWER_LEFT_CURVE_IN_WIDTH,
							 LOWER_LEFT_CURVE_WIDTH, LOWER_LEFT_CURVE_IN_HEIGHT,
							 LOWER_LEFT_CURVE_HEIGHT, App.globals.g_kMultiplayerBorderBlue,
							 LOWER_LEFT_CURVE_OI_WIDTH)
	pEyeCandyPane.AddChild(pLLCurve, LOWER_LEFT_CURVE_X_POS, LOWER_LEFT_CURVE_Y_POS, 0)

	# Create the first right bar
	pRightBar1 = App.TGIcon_Create("NormalStyleFrame", 5, App.globals.g_kMultiplayerBorderBlue)
	pRightBar1.Resize(RIGHT_BAR_1_WIDTH, RIGHT_BAR_1_HEIGHT, 0)
	pEyeCandyPane.AddChild(pRightBar1, RIGHT_BAR_1_X_POS, RIGHT_BAR_1_Y_POS, 0)  
	
	# Create the second right bar
	pRightBar2 = App.TGIcon_Create("NormalStyleFrame", 5, App.globals.g_kMultiplayerBorderPurple)
	pRightBar2.Resize(RIGHT_BAR_2_WIDTH, RIGHT_BAR_2_HEIGHT, 0)
	pEyeCandyPane.AddChild(pRightBar2, RIGHT_BAR_2_X_POS, RIGHT_BAR_2_Y_POS, 0)  
	 
	# Create the lower-right curve
	pLRCurve = UIHelpers.CreateCurve(UIHelpers.LOWER_RIGHT_CURVE, LOWER_RIGHT_CURVE_IN_WIDTH,
							 LOWER_RIGHT_CURVE_WIDTH, LOWER_RIGHT_CURVE_IN_HEIGHT,
							 LOWER_RIGHT_CURVE_HEIGHT, App.globals.g_kMultiplayerBorderBlue,
							 LOWER_RIGHT_CURVE_OI_WIDTH)
	pEyeCandyPane.AddChild(pLRCurve, LOWER_RIGHT_CURVE_X_POS, LOWER_RIGHT_CURVE_Y_POS, 0)

	# Create the first bottom bar
	pBottomBar1 = App.TGIcon_Create("NormalStyleFrame", 5, App.globals.g_kMultiplayerBorderPurple)
	pBottomBar1.Resize(BOTTOM_BAR_1_WIDTH, BOTTOM_BAR_1_HEIGHT, 0)
	pEyeCandyPane.AddChild(pBottomBar1, BOTTOM_BAR_1_X_POS, BOTTOM_BAR_1_Y_POS, 0)  

	# Create the second bottom bar
	pBottomBar2 = App.TGIcon_Create("NormalStyleFrame", 5, App.globals.g_kMultiplayerBorderPurple)
	pBottomBar2.Resize(BOTTOM_BAR_2_WIDTH, BOTTOM_BAR_2_HEIGHT, 0)
	pEyeCandyPane.AddChild(pBottomBar2, BOTTOM_BAR_2_X_POS, BOTTOM_BAR_2_Y_POS, 0)

	# Add eye candy pane
	pMiscPane.AddChild(pEyeCandyPane, 0, 0, 0)

        # here the important Stuff:
        if FoundationMode == 1:        
                import FoundationMenu
                bridgeMenuBuilder = FoundationMenu.BridgeMenuBuilderDef(pDatabase)
                pBridgeMenu = GeneratePlayerBridgeMenu(bridgeMenuBuilder, qbGameMode.bridgeList, pMiscPane)

	pEvent = App.TGEvent_Create()
	pEvent.SetEventType(ET_USE_BRIDGE)
	pEvent.SetDestination(pMiscPane)
        if useBridge == 1:
                ButtonText = "Use Bridge: Yes"
        else:
                ButtonText = "Use Bridge: No"
        g_pUseBridgeButton = App.STRoundedButton_CreateW(App.TGString(ButtonText), pEvent, ADD_FRIEND_BUTTON_WIDTH, ADD_FRIEND_BUTTON_HEIGHT, 1)
	g_pUseBridgeButton.SetNormalColor(App.g_kMainMenuButtonColor)
	g_pUseBridgeButton.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
	g_pUseBridgeButton.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
	g_pUseBridgeButton.SetColorBasedOnFlags()
	pMiscPane.AddChild(g_pUseBridgeButton, USE_BRIDGE_BUTTON_X_POS, USE_BRIDGE_BUTTON_Y_POS)

        
	# We want our stylized window to take up 3/4 of the available height in
	# the pane, and to be centered
	fScoreWindowWidth = 0.5125
	fScoreWindowHeight = pMiscPane.GetHeight() * 0.75
	fScoreXPos = (pMiscPane.GetWidth() - fScoreWindowWidth) / 2.0 
	fScoreYPos = (pMiscPane.GetHeight() - fScoreWindowHeight) / 2.0
        
    	pHeader = App.TGIcon_Create(App.GraphicsModeInfo_GetCurrentMode().GetLcarsString(), 200)
	pHeader.SetColor(App.NiColorA_BLACK)
	pHeader.Resize(0.502, 0.04, 0)
	pHeader.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__ + ".HandleMouseEventsForGlass")
	pMiscPane.AddChild(pHeader, fScoreXPos + 0.0105, fScoreYPos + 0.03, 0)

	# Create a black background so that the main menu won't be visible behind us
	# Set it to handle mouse events so that the now-hidden buttons behind it
	# won't get clicked
        pcLCARS = App.GraphicsModeInfo_GetCurrentMode().GetLcarsString()
	pBGIcon = App.TGIcon_Create(pcLCARS, 200)
	pBGIcon.SetColor(App.NiColorA_BLACK)
	pBGIcon.Resize(pMiscPane.GetWidth(), pMiscPane.GetHeight())
	pBGIcon.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__ + ".HandleMouseEventsForGlass")
	pMiscPane.AddChild(pBGIcon)
        
        pMiscPane.SetNotVisible()
	return pMiscPane


def GeneratePlayerBridgeMenu(bridgeMenuBuilder, bridgeList, pMiscPane):
        # Create menus for the player's ship
        debug(__name__ + ", GeneratePlayerBridgeMenu")
        pShipMenu = App.STSubPane_Create(BRIDGE_MENU_WIDTH, BRIDGE_MENU_HEIGHT, 1)
        pStylizedWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Select Bridge"))
        pStylizedWindow.SetUseScrolling(1)
        pStylizedWindow.SetFixedSize(BRIDGE_MENU_WIDTH, BRIDGE_MENU_HEIGHT)
        pStylizedWindow.SetTitleBarThickness(BAR_HEIGHT)
        pStylizedWindow.AddChild(pShipMenu)
        pMiscPane.AddChild(pStylizedWindow, BRIDGE_MENU_X_POS, BRIDGE_MENU_Y_POS)
        
        bridgeMenuBuilder(bridgeList, pShipMenu, ET_SELECT_BRIDGE_TYPE, pMiscPane)
        
        pShipMenu.Resize(pShipMenu.GetWidth(), pShipMenu.GetTotalHeightOfChildren())
        pStylizedWindow.Layout()
        pStylizedWindow.InteriorChangedSize()
        return pStylizedWindow


###############################################################################
#	BuildShipsPane()
#	
#	Builds the Ships menu.
#	
#	Args:	none
#	
#	Return:	none
###############################################################################
def BuildShipsPane():
	debug(__name__ + ", BuildShipsPane")
	global pShipsPane, g_pAddFriendButton, g_pAddEnemyButton, g_fXPixelOffset, g_fYPixelOffset
	
        pDatabase = Multiplayer.MissionShared.g_pDatabase
        g_pMissionDatabase = App.g_kLocalizationManager.Load("data/TGL/QuickBattle/QuickBattle.tgl")
        
	pShipsPane = App.TGPane_Create(SUB_PANE_WIDTH, SUB_PANE_HEIGHT)

	pEyeCandyPane = App.TGPane_Create (1.0, 1.0)
	#########################################
	# Create eye candy
	pGraphicsMode = App.GraphicsModeInfo_GetCurrentMode()
	pcLCARS = pGraphicsMode.GetLcarsString()

	# Set the font small
	App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcFlightSmallFont,
				MainMenu.mainmenu.g_kFlightSmallFontSize[MainMenu.mainmenu.g_iRes])

	# Create the little "190" that's in the lower-left curve
	p190 = App.TGParagraph_Create("190", 1.0, App.g_kSTMenuTextColor)
	pEyeCandyPane.AddChild(p190, NUMBER_190_X_POS, NUMBER_190_Y_POS, 0)
	
	# Create the little "945" that's in RightBar1
	p945 = App.TGParagraph_Create("945", 1.0, App.g_kSTMenuTextColor)
	pEyeCandyPane.AddChild(p945, NUMBER_945_X_POS, NUMBER_945_Y_POS, 0)

	# Create the little "04" that's in RightBar2
	p04 = App.TGParagraph_Create("04", 1.0, App.g_kSTMenuTextColor)
	pEyeCandyPane.AddChild(p04, NUMBER_04_X_POS, NUMBER_04_Y_POS, 0)

	# Set the font larger
	App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcSmallFont,
				MainMenu.mainmenu.g_kSmallFontSize[MainMenu.mainmenu.g_iRes] + 1)

	# Create the title
	pTitle = App.TGParagraph_CreateW(pDatabase.GetString("Multiplayer"), 1.0, App.globals.g_kTitleColor)
	fPosDelta = (pTitle.GetHeight() - TOP_BAR_HEIGHT) / 2.0
	pEyeCandyPane.AddChild(pTitle, TITLE_X_POS, TOP_BAR_Y_POS - fPosDelta, 0)
	
	# Create the subtitle
        pSubtitle = App.TGParagraph_CreateW(App.TGString("Select Ships"), 1.0, App.globals.g_kTitleColor)
	pEyeCandyPane.AddChild(pSubtitle, SUBTITLE_X_POS, SUBTITLE_Y_POS, 0)

	# Set the font smaller but still large
	App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcSmallFont,
				MainMenu.mainmenu.g_kSmallFontSize[MainMenu.mainmenu.g_iRes])

	# Create the top bar
	fTopXPos = TITLE_X_POS + pTitle.GetWidth() + TOP_BAR_X_DISTANCE
	fTopWidth = TOP_BAR_RIGHT_EDGE - fTopXPos
	pTopBar = App.TGIcon_Create("NormalStyleFrame", 5, App.globals.g_kInterfaceBorderColor)
	pTopBar.Resize(fTopWidth, TOP_BAR_HEIGHT, 0)
	pEyeCandyPane.AddChild(pTopBar, fTopXPos, TOP_BAR_Y_POS, 0)  

	# Create the first left bar
	pLeftBar1 = App.TGIcon_Create("NormalStyleFrame", 5, App.globals.g_kInterfaceBorderColor)
	pLeftBar1.Resize(LEFT_BAR_1_WIDTH, LEFT_BAR_1_HEIGHT, 0)
	pEyeCandyPane.AddChild(pLeftBar1, LEFT_BAR_1_X_POS, LEFT_BAR_1_Y_POS, 0)  

	# Create the second left bar
	pLeftBar2 = App.TGIcon_Create("NormalStyleFrame", 5, App.globals.g_kMultiplayerBorderBlue)
	pLeftBar2.Resize(LEFT_BAR_2_WIDTH, LEFT_BAR_2_HEIGHT, 0)
	pEyeCandyPane.AddChild(pLeftBar2, LEFT_BAR_2_X_POS, LEFT_BAR_2_Y_POS, 0)  

	# Create the third left bar
	pLeftBar3 = App.TGIcon_Create("NormalStyleFrame", 5, App.globals.g_kMultiplayerBorderPurple)
	pLeftBar3.Resize(LEFT_BAR_3_WIDTH, LEFT_BAR_3_HEIGHT, 0)
	pEyeCandyPane.AddChild(pLeftBar3, LEFT_BAR_3_X_POS, LEFT_BAR_3_Y_POS, 0)  

	# Create the lower-left curve
	pLLCurve = UIHelpers.CreateCurve(UIHelpers.LOWER_LEFT_CURVE, LOWER_LEFT_CURVE_IN_WIDTH,
							 LOWER_LEFT_CURVE_WIDTH, LOWER_LEFT_CURVE_IN_HEIGHT,
							 LOWER_LEFT_CURVE_HEIGHT, App.globals.g_kMultiplayerBorderBlue,
							 LOWER_LEFT_CURVE_OI_WIDTH)
	pEyeCandyPane.AddChild(pLLCurve, LOWER_LEFT_CURVE_X_POS, LOWER_LEFT_CURVE_Y_POS, 0)

	# Create the first right bar
	pRightBar1 = App.TGIcon_Create("NormalStyleFrame", 5, App.globals.g_kMultiplayerBorderBlue)
	pRightBar1.Resize(RIGHT_BAR_1_WIDTH, RIGHT_BAR_1_HEIGHT, 0)
	pEyeCandyPane.AddChild(pRightBar1, RIGHT_BAR_1_X_POS, RIGHT_BAR_1_Y_POS, 0)  
	
	# Create the second right bar
	pRightBar2 = App.TGIcon_Create("NormalStyleFrame", 5, App.globals.g_kMultiplayerBorderPurple)
	pRightBar2.Resize(RIGHT_BAR_2_WIDTH, RIGHT_BAR_2_HEIGHT, 0)
	pEyeCandyPane.AddChild(pRightBar2, RIGHT_BAR_2_X_POS, RIGHT_BAR_2_Y_POS, 0)  
	 
	# Create the lower-right curve
	pLRCurve = UIHelpers.CreateCurve(UIHelpers.LOWER_RIGHT_CURVE, LOWER_RIGHT_CURVE_IN_WIDTH,
							 LOWER_RIGHT_CURVE_WIDTH, LOWER_RIGHT_CURVE_IN_HEIGHT,
							 LOWER_RIGHT_CURVE_HEIGHT, App.globals.g_kMultiplayerBorderBlue,
							 LOWER_RIGHT_CURVE_OI_WIDTH)
	pEyeCandyPane.AddChild(pLRCurve, LOWER_RIGHT_CURVE_X_POS, LOWER_RIGHT_CURVE_Y_POS, 0)

	# Create the first bottom bar
	pBottomBar1 = App.TGIcon_Create("NormalStyleFrame", 5, App.globals.g_kMultiplayerBorderPurple)
	pBottomBar1.Resize(BOTTOM_BAR_1_WIDTH, BOTTOM_BAR_1_HEIGHT, 0)
	pEyeCandyPane.AddChild(pBottomBar1, BOTTOM_BAR_1_X_POS, BOTTOM_BAR_1_Y_POS, 0)  

	# Create the second bottom bar
	pBottomBar2 = App.TGIcon_Create("NormalStyleFrame", 5, App.globals.g_kMultiplayerBorderPurple)
	pBottomBar2.Resize(BOTTOM_BAR_2_WIDTH, BOTTOM_BAR_2_HEIGHT, 0)
	pEyeCandyPane.AddChild(pBottomBar2, BOTTOM_BAR_2_X_POS, BOTTOM_BAR_2_Y_POS, 0)

	# Add eye candy pane
	pShipsPane.AddChild(pEyeCandyPane, 0, 0, 0)

	pEventAddAsFriendButton = App.TGEvent_Create()
	pEventAddAsFriendButton.SetEventType(ET_ADD_AS_FRIEND)
	pEventAddAsFriendButton.SetDestination(pShipsPane)
	
	pEventAddAsEnemyButton = App.TGEvent_Create()
	pEventAddAsEnemyButton.SetEventType(ET_ADD_AS_ENEMY)
	pEventAddAsEnemyButton.SetDestination(pShipsPane)
	
	pEventDelete = App.TGEvent_Create()
	pEventDelete.SetEventType(ET_DELETE)
	pEventDelete.SetDestination(pShipsPane)
	
	# Create a button to add the currently selected ship to the list of friendlies
	g_pAddFriendButton = App.STRoundedButton_CreateW(App.TGString("Add to Team 1"), pEventAddAsFriendButton, ADD_FRIEND_BUTTON_WIDTH, ADD_FRIEND_BUTTON_HEIGHT, 1)
	g_pAddFriendButton.SetDisabled() # So that you can't add a ship 'til one has been selected
	g_pAddFriendButton.SetNormalColor(App.g_kMainMenuButtonColor)
	g_pAddFriendButton.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
	g_pAddFriendButton.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
	g_pAddFriendButton.SetColorBasedOnFlags()
	pShipsPane.AddChild(g_pAddFriendButton, ADD_FRIEND_BUTTON_X_POS, ADD_FRIEND_BUTTON_Y_POS)


	# Create a button to add the currently selected ship to the list of enemies
	g_pAddEnemyButton = App.STRoundedButton_CreateW(App.TGString("Add to Team 2"), pEventAddAsEnemyButton, ADD_ENEMY_BUTTON_WIDTH, ADD_ENEMY_BUTTON_HEIGHT, 1)
	g_pAddEnemyButton.SetDisabled() # So that you can't add a ship 'til one has been selected
	g_pAddEnemyButton.SetNormalColor(App.g_kMainMenuButtonColor)
	g_pAddEnemyButton.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
	g_pAddEnemyButton.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
	g_pAddEnemyButton.SetColorBasedOnFlags()
	pShipsPane.AddChild(g_pAddEnemyButton, ADD_ENEMY_BUTTON_X_POS, ADD_ENEMY_BUTTON_Y_POS)

	GenerateFriendMenu()
	GenerateEnemyMenu()

	# Go to the small font
	App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcFlightSmallFont, MainMenu.mainmenu.g_kFlightSmallFontSize[MainMenu.mainmenu.g_iRes])

	global g_pDeleteButton
	g_pDeleteButton = App.STRoundedButton_CreateW(g_pMissionDatabase.GetString("Delete"), pEventDelete, DEL_BUTTON_WIDTH, DEL_BUTTON_HEIGHT, 1)
	g_pDeleteButton.SetNormalColor(App.g_kQuickBattleBrightRed)
	pShipsPane.AddChild(g_pDeleteButton, DEL_BUTTON_X_POS, DEL_BUTTON_Y_POS)

	# Go back to the large font
	App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcSmallFont, MainMenu.mainmenu.g_kSmallFontSize[MainMenu.mainmenu.g_iRes])

	# Generete the textbox for ship descriptions
	pStylizedWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", g_pMissionDatabase.GetString("Ship Description"))
	pStylizedWindow.SetFixedSize(SHIPS_TEXT_WIDTH, SHIPS_TEXT_HEIGHT)
	pStylizedWindow.SetTitleBarThickness(BAR_HEIGHT)

	# Go back to the large font
	App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcSmallFont, MainMenu.mainmenu.g_kSmallFontSize[MainMenu.mainmenu.g_iRes])

        pPane = BuildShipSelectWindow(pShipsPane, pDatabase)
        
        pShipsPane.AddChild(pPane, SHIPS_WINDOW_X_POS, SHIPS_WINDOW_Y_POS, 0)

	# We want our stylized window to take up 3/4 of the available height in
	# the pane, and to be centered
	fScoreWindowWidth = 0.5125
	fScoreWindowHeight = pShipsPane.GetHeight() * 0.75
	fScoreXPos = (pShipsPane.GetWidth() - fScoreWindowWidth) / 2.0 
	fScoreYPos = (pShipsPane.GetHeight() - fScoreWindowHeight) / 2.0

	# Generate the bar that extends out of the STStylizedWindow that surrounds
	# the ShipMenu
	pShipsBar = App.TGIcon_Create("NormalStyleFrame", 5, App.globals.g_kInterfaceBorderColor)
	pShipsBar.SizeToArtwork(0)
	pShipsBar.Resize(BAR_WIDTH, BAR_HEIGHT)
    
    	pHeader = App.TGIcon_Create(App.GraphicsModeInfo_GetCurrentMode().GetLcarsString(), 200)
	pHeader.SetColor(App.NiColorA_BLACK)
	pHeader.Resize(0.502, 0.04, 0)
	pHeader.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__ + ".HandleMouseEventsForGlass")
	pShipsPane.AddChild(pHeader, fScoreXPos + 0.0105, fScoreYPos + 0.03, 0)

	# Create a black background so that the main menu won't be visible behind us
	# Set it to handle mouse events so that the now-hidden buttons behind it
	# won't get clicked
        pcLCARS = App.GraphicsModeInfo_GetCurrentMode().GetLcarsString()
	pBGIcon = App.TGIcon_Create(pcLCARS, 200)
	pBGIcon.SetColor(App.NiColorA_BLACK)
	pBGIcon.Resize(pShipsPane.GetWidth(), pShipsPane.GetHeight())
	pBGIcon.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__ + ".HandleMouseEventsForGlass")
	pShipsPane.AddChild(pBGIcon)

        pShipsPane.SetNotVisible()
        
	return pShipsPane


###############################################################################
#	GenerateFriendMenu()
#
#	Generate the menu in which selected friendly ships will be listed
#
#	Args:	none
#
#	Return:	none
###############################################################################
def GenerateFriendMenu():
	debug(__name__ + ", GenerateFriendMenu")
	global g_pFriendWindow, g_pFriendMenu
	
	g_pMissionDatabase = Multiplayer.MissionShared.g_pDatabase
	
	g_pFriendMenu = App.STSubPane_Create(FRIEND_LIST_WIDTH, FRIEND_LIST_HEIGHT, 1)
	g_pFriendWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", g_pMissionDatabase.GetString("Team1 Name"))
	g_pFriendMenu.Resize(FRIEND_LIST_WIDTH - g_pFriendWindow.GetBorderWidth(), FRIEND_LIST_HEIGHT - g_pFriendWindow.GetBorderHeight())
	g_pFriendWindow.SetFixedSize(FRIEND_LIST_WIDTH, FRIEND_LIST_HEIGHT)
	g_pFriendWindow.AddChild(g_pFriendMenu)
	pShipsPane.AddChild(g_pFriendWindow, FRIEND_LIST_X_POS, FRIEND_LIST_Y_POS)
	g_pFriendMenu.ResizeToContents()


###############################################################################
#	GenerateEnemyMenu()
#
#	Generate the menu in which selected enemy ships will be listed
#
#	Args:	none
#
#	Return:	none
###############################################################################
def GenerateEnemyMenu():
	debug(__name__ + ", GenerateEnemyMenu")
	global g_pEnemyWindow, g_pEnemyMenu
	
	g_pMissionDatabase = Multiplayer.MissionShared.g_pDatabase
	
	g_pEnemyMenu = App.STSubPane_Create(ENEMY_LIST_WIDTH, ENEMY_LIST_HEIGHT, 1)
	g_pEnemyWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", g_pMissionDatabase.GetString("Team2 Name"))
	g_pEnemyMenu.Resize(ENEMY_LIST_WIDTH - g_pEnemyWindow.GetBorderWidth(), ENEMY_LIST_HEIGHT - g_pEnemyWindow.GetBorderHeight())
	g_pEnemyWindow.SetFixedSize(ENEMY_LIST_WIDTH, ENEMY_LIST_HEIGHT)
	g_pEnemyWindow.AddChild(g_pEnemyMenu)
	pShipsPane.AddChild(g_pEnemyWindow, ENEMY_LIST_X_POS, ENEMY_LIST_Y_POS)
	g_pEnemyMenu.ResizeToContents()


def BuildShipSelectWindow(pMissionPane, pDatabase):
	# Create the window
	debug(__name__ + ", BuildShipSelectWindow")
	pWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", pDatabase.GetString("Select Your Ship"), 
						0.0, 0.0, None, 1, SHIPS_WINDOW_WIDTH, SHIPS_WINDOW_HEIGHT)
	pWindow.SetTitleBarThickness(SHIPS_WINDOW_BAR_THICKNESS)
	App.g_kFocusManager.AddObjectToTabOrder(pWindow)

	pSubPane = App.STSubPane_Create (SHIPS_SUBPANE_WIDTH, 500.0, 0)
	pWindow.AddChild (pSubPane, 0, 0, 0)

	
	#########################################
	# Create the buttons
        dict_sides = {}
	for iIndex in range(1, Multiplayer.SpeciesToShip.MAX_SHIPS):
                # Setup the event for when this button is clicked
		pEvent = App.TGIntEvent_Create()
		pEvent.SetEventType(ET_SELECT_SHIP_TYPE)
		pEvent.SetInt(iIndex)		# store the index so we know which button was clicked.
		pEvent.SetDestination(pMissionPane)
                # Create the button.
		pButton = App.STButton_CreateW(Multiplayer.MissionShared.g_pShipDatabase.GetString(Multiplayer.SpeciesToShip.GetScriptFromSpecies(iIndex)), pEvent)
		if (iIndex == g_iSpecies):
			pButton.SetChosen(1)
			global g_pChosenSpecies
			g_pChosenSpecies = pButton
		pEvent.SetSource(pButton)
                if Multiplayer.SpeciesToShip.GetScriptFromSpecies(iIndex):
                        if Multiplayer.MissionShared.g_pShipDatabase.HasString(Multiplayer.SpeciesToShip.GetScriptFromSpecies(iIndex)):
                                mvSpecies = Multiplayer.SpeciesToShip.GetSideFromSpecies(iIndex)
                                if not dict_sides.has_key(mvSpecies):
                                        try:
                                                dict_sides[mvSpecies] = App.STCharacterMenu_Create(mvSpecies)
                                        except:
                                                continue
                                        pSubPane.AddChild(dict_sides[mvSpecies], 0, 0, 0)
                                # test if a TGL String is available. if not, don't add it.
                                dict_sides[mvSpecies].AddChild(pButton, 0, 0, 0)
                        else:
                                print "No entry in Ships.tgl for \"%s\"" % Multiplayer.SpeciesToShip.GetScriptFromSpecies(iIndex)

	pSubPane.ResizeToContents()

	return pWindow



def SelectShipType(pObject, pEvent):
        debug(__name__ + ", SelectShipType")
        global g_pAddFriendButton, g_pAddEnemyButton, SelectedSpecies
        
        # Now we have a ship so we can enable these Buttons:
        g_pAddFriendButton.SetEnabled()
        g_pAddEnemyButton.SetEnabled()
        
	SelectedSpecies = pEvent.GetInt()

	pObject.CallNextHandler(pEvent)


def SetUseBridge(pObject, pEvent):
        debug(__name__ + ", SetUseBridge")
        global useBridge, FoundationMode, g_pUseBridgeButton
        if FoundationMode == 0:
                return
        
        # host cannot activate bridge use for now - too unstable:
        #if App.g_kUtopiaModule.IsHost():
        #        useBridge = 0
        #        return
        
        if useBridge == 1:
                useBridge = 0
                ButtonText = "Use Bridge: No"
        else:
                useBridge = 1
                ButtonText = "Use Bridge: Yes"
        g_pUseBridgeButton.SetName(App.TGString(ButtonText))


def SelectBridge(pObject, pEvent):
        debug(__name__ + ", SelectBridge")
        global myMultBridge
        if hasattr(pEvent, "GetInt"):
                myMultBridge = Foundation.bridgeList[pEvent.GetInt()].bridgeString
	pObject.CallNextHandler(pEvent)


def AddShipAsEnemy(pObject, pEvent):
    debug(__name__ + ", AddShipAsEnemy")
    global SelectedSpecies, groupTeam2

    groupTeam2[len(groupTeam2.keys())] = SelectedSpecies
    RebuildEnemyMenu()


def AddShipAsFriend(pObject, pEvent):
    debug(__name__ + ", AddShipAsFriend")
    global SelectedSpecies, groupTeam1

    groupTeam1[len(groupTeam1.keys())] = SelectedSpecies
    RebuildFriendlyMenu()
    

def RebuildEnemyMenu():
    debug(__name__ + ", RebuildEnemyMenu")
    global g_pEnemyMenu, g_pEnemyWindow, groupTeam2, ET_SELECT_SHIP_IN_ENEMY_MENU

    g_pEnemyMenu.KillChildren()
    i = -1
    check_i = 0
    while check_i < len(groupTeam2.keys()):
        i = i + 1
        if not groupTeam2.has_key(i):
            continue
        check_i = check_i + 1
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_SELECT_SHIP_IN_ENEMY_MENU)
        pEvent.SetInt(groupTeam2[i])
        pEvent.SetDestination(pShipsPane)
                
        Ship = Multiplayer.SpeciesToShip.GetScriptFromSpecies(groupTeam2[i])
        pButton = App.STButton_CreateW(Multiplayer.MissionShared.g_pShipDatabase.GetString(Ship), pEvent)
        g_pEnemyMenu.AddChild(pButton)

    # resize Window
    g_pEnemyMenu.ResizeToContents()
    g_pEnemyWindow.ScrollToBottom()
    g_pEnemyWindow.Layout()


def RebuildFriendlyMenu():
    debug(__name__ + ", RebuildFriendlyMenu")
    global g_pFriendWindow, g_pFriendMenu, groupTeam1, ET_SELECT_SHIP_IN_FRIENDLY_MENU

    g_pFriendMenu.KillChildren()
    i = -1
    check_i = 0
    while check_i < len(groupTeam1.keys()):
        i = i + 1
        if not groupTeam1.has_key(i):
            continue
        check_i = check_i + 1
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_SELECT_SHIP_IN_FRIENDLY_MENU)
        pEvent.SetInt(groupTeam1[i])
        pEvent.SetDestination(pShipsPane)
                
        Ship = Multiplayer.SpeciesToShip.GetScriptFromSpecies(groupTeam1[i])
        pButton = App.STButton_CreateW(Multiplayer.MissionShared.g_pShipDatabase.GetString(Ship), pEvent)
        g_pFriendMenu.AddChild(pButton)

    # resize Window
    g_pFriendMenu.ResizeToContents()
    g_pFriendWindow.ScrollToBottom()
    g_pFriendWindow.Layout()


def ShipInEnemyMenuSelect(pObject, pEvent):
    debug(__name__ + ", ShipInEnemyMenuSelect")
    global curMenuInMenu, curShipInMenu
    curMenuInMenu = "Group2"
    curShipInMenu = pEvent.GetInt()
    

def ShipInFriendlyMenuSelect(pObject, pEvent):
    debug(__name__ + ", ShipInFriendlyMenuSelect")
    global curMenuInMenu, curShipInMenu
    curMenuInMenu = "Group1"
    curShipInMenu = pEvent.GetInt()


def Delete(pObject, pEvent):
    debug(__name__ + ", Delete")
    global curMenuInMenu, curShipInMenu, g_pEnemyMenu, g_pEnemyWindow, groupTeam1, groupTeam2
    if (curMenuInMenu == "Group2"):
        i = -1
        check_i = 0
        while check_i < len(groupTeam2.keys()):
            i = i + 1
            if not groupTeam2.has_key(i):
                continue
            check_i = check_i + 1
            if (groupTeam2[i] == curShipInMenu):
                del groupTeam2[i]
                RebuildEnemyMenu()
                break
    elif (curMenuInMenu == "Group1"):
        i = -1
        check_i = 0
        while check_i < len(groupTeam1.keys()):
            i = i + 1
            if not groupTeam1.has_key(i):
                continue
            check_i = check_i + 1
            if (groupTeam1[i] == curShipInMenu):
                del groupTeam1[i]
                RebuildFriendlyMenu()
                break


def myObjectDestroyedHandler(pObject, pEvent):
        debug(__name__ + ", myObjectDestroyedHandler")
        global g_pShipsButton, g_pPlayerButton, g_pMiscButton

        pPlayer = MissionLib.GetPlayer()
        pKilledObject = pEvent.GetDestination()
        if (pKilledObject.IsTypeOf(App.CT_SHIP)):
                pShip = App.ShipClass_Cast(pKilledObject)
                
                if pPlayer and pShip and pPlayer.GetObjID() == pShip.GetObjID():
                        Multiplayer.MissionMenusShared.ObjectDestroyedHandler(pObject, pEvent)
                        #if App.g_kUtopiaModule.IsHost():
                                #g_pShipsButton.SetVisible()
                        g_pPlayerButton.SetVisible()
                        g_pMiscButton.SetVisible()
                        #g_pTeamButton.SetDisabled()


def IsValidMd5(mymd5sum):
	debug(__name__ + ", IsValidMd5")
	global ValidMd5sForEngineering
	i = ValidMd5sForEngineering.count(mymd5sum)
	if i == 0:
		return 0
	return 1


def TestsItsMd5(filename):
        debug(__name__ + ", TestsItsMd5")
        import nt
        file = nt.open(filename, nt.O_CREAT)
        mdsum = MD5new()
        readBytes = 1024
        while(readBytes):
                readString = nt.read(file, 1024)
                mdsum.update(readString)
                readBytes = len(readString)
        nt.close(file)
        #file = nt.open("scripts\Custom\QBautostart\md5.txt", nt.O_CREAT | nt.O_RDWR)
        #nt.write(file, "md5 = " + mdsum.hexdigest() + "\n")
        #nt.close(file)
        return IsValidMd5(mdsum.hexdigest())


"""A sample implementation of MD5 in pure Python.

This is an implementation of the MD5 hash function, as specified by
RFC 1321, in pure Python. It was implemented using Bruce Schneier's
excellent book "Applied Cryptography", 2nd ed., 1996.

Surely this is not meant to compete with the existing implementation
of the Python standard library (written in C). Rather, it should be
seen as a Python complement that is more readable than C and can be
used more conveniently for learning and experimenting purposes in
the field of cryptography.

This module tries very hard to follow the API of the existing Python
standard library's "md5" module, but although it seems to work fine,
it has not been extensively tested! (But note that there is a test
module, test_md5py.py, that compares this Python implementation with
the C one of the Python standard library.

BEWARE: this comes with no guarantee whatsoever about fitness and/or
other properties! Specifically, do not use this in any production
code! License is Python License!

Special thanks to Aurelian Coman who fixed some nasty bugs!

Dinu C. Gherman
"""


__date__    = '2001-10-1'
__version__ = 0.9


#import struct, string, copy
import struct, string

# ======================================================================
# Bit-Manipulation helpers
#
#   _long2bytes() was contributed by Barry Warsaw
#   and is reused here with tiny modifications.
# ======================================================================

def _long2bytes(n, blocksize=0):
    debug(__name__ + ", _long2bytes")
    """Convert a long integer to a byte string.

    If optional blocksize is given and greater than zero, pad the front
    of the byte string with binary zeros so that the length is a multiple
    of blocksize.
    """

    # After much testing, this algorithm was deemed to be the fastest.
    s = ''
    pack = struct.pack
    while n > 0:
        ### CHANGED FROM '>I' TO '<I'. (DCG)
        s = pack('<I', n & 0xffffffffL) + s
        ### --------------------------
        n = n >> 32

    # Strip off leading zeros.
    for i in range(len(s)):
        if s[i] <> '\000':
            break
    else:
        # Only happens when n == 0.
        s = '\000'
        i = 0

    s = s[i:]

    # Add back some pad bytes. This could be done more efficiently
    # w.r.t. the de-padding being done above, but sigh...
    if blocksize > 0 and len(s) % blocksize:
        s = (blocksize - len(s) % blocksize) * '\000' + s

    return s


def _bytelist2long(list):
    debug(__name__ + ", _bytelist2long")
    "Transform a list of characters into a list of longs."

    imax = len(list)/4
    hl = [0L] * imax

    j = 0
    i = 0
    while i < imax:
        b0 = long(ord(list[j]))
        b1 = (long(ord(list[j+1]))) << 8
        b2 = (long(ord(list[j+2]))) << 16
        b3 = (long(ord(list[j+3]))) << 24
        hl[i] = b0 | b1 |b2 | b3
        i = i+1
        j = j+4

    return hl


def _rotateLeft(x, n):
    debug(__name__ + ", _rotateLeft")
    "Rotate x (32 bit) left n bits circularly."

    return (x << n) | (x >> (32-n))


# ======================================================================
# The real MD5 meat...
#
#   Implemented after "Applied Cryptography", 2nd ed., 1996,
#   pp. 436-441 by Bruce Schneier.
# ======================================================================

# F, G, H and I are basic MD5 functions.

def F(x, y, z):
    debug(__name__ + ", F")
    return (x & y) | ((~x) & z)

def G(x, y, z):
    debug(__name__ + ", G")
    return (x & z) | (y & (~z))

def H(x, y, z):
    debug(__name__ + ", H")
    return x ^ y ^ z

def I(x, y, z):
    debug(__name__ + ", I")
    return y ^ (x | (~z))


def XX(func, a, b, c, d, x, s, ac):
    debug(__name__ + ", XX")
    """Wrapper for call distribution to functions F, G, H and I.

    This replaces functions FF, GG, HH and II from "Appl. Crypto.
    Rotation is separate from addition to prevent recomputation
    (now summed-up in one function).
    """

    res = 0L
    res = res + a + func(b, c, d)
    res = res + x 
    res = res + ac
    res = res & 0xffffffffL
    res = _rotateLeft(res, s)
    res = res & 0xffffffffL
    res = res + b

    return res & 0xffffffffL


class MD5:
    "An implementation of the MD5 hash function in pure Python."

    def __init__(self):
        debug(__name__ + ", __init__")
        "Initialisation."
        
        # Initial 128 bit message digest (4 times 32 bit).
        self.A = 0L
        self.B = 0L
        self.C = 0L
        self.D = 0L
        
        # Initial message length in bits(!).
        self.length = 0L
        self.count = [0, 0]

        # Initial empty message as a sequence of bytes (8 bit characters).
        self.input = []

        # Length of the final hash (in bytes).
        self.HASH_LENGTH = 16
         
        # Length of a block (the number of bytes hashed in every transform).
        self.DATA_LENGTH = 64

        # Call a separate init function, that can be used repeatedly
        # to start from scratch on the same object.
        self.init()


    def init(self):
        debug(__name__ + ", init")
        "Initialize the message-digest and set all fields to zero."

        self.length = 0L
        self.input = []

        # Load magic initialization constants.
        self.A = 0x67452301L
        self.B = 0xefcdab89L
        self.C = 0x98badcfeL
        self.D = 0x10325476L


    def _transform(self, inp):
        debug(__name__ + ", _transform")
        """Basic MD5 step transforming the digest based on the input.

        Note that if the Mysterious Constants are arranged backwards
        in little-endian order and decrypted with the DES they produce
        OCCULT MESSAGES!
        """

        a, b, c, d = A, B, C, D = self.A, self.B, self.C, self.D

        # Round 1.

        S11, S12, S13, S14 = 7, 12, 17, 22

        a = XX(F, a, b, c, d, inp[ 0], S11, 0xD76AA478L) # 1 
        d = XX(F, d, a, b, c, inp[ 1], S12, 0xE8C7B756L) # 2 
        c = XX(F, c, d, a, b, inp[ 2], S13, 0x242070DBL) # 3 
        b = XX(F, b, c, d, a, inp[ 3], S14, 0xC1BDCEEEL) # 4 
        a = XX(F, a, b, c, d, inp[ 4], S11, 0xF57C0FAFL) # 5 
        d = XX(F, d, a, b, c, inp[ 5], S12, 0x4787C62AL) # 6 
        c = XX(F, c, d, a, b, inp[ 6], S13, 0xA8304613L) # 7 
        b = XX(F, b, c, d, a, inp[ 7], S14, 0xFD469501L) # 8 
        a = XX(F, a, b, c, d, inp[ 8], S11, 0x698098D8L) # 9 
        d = XX(F, d, a, b, c, inp[ 9], S12, 0x8B44F7AFL) # 10 
        c = XX(F, c, d, a, b, inp[10], S13, 0xFFFF5BB1L) # 11 
        b = XX(F, b, c, d, a, inp[11], S14, 0x895CD7BEL) # 12 
        a = XX(F, a, b, c, d, inp[12], S11, 0x6B901122L) # 13 
        d = XX(F, d, a, b, c, inp[13], S12, 0xFD987193L) # 14 
        c = XX(F, c, d, a, b, inp[14], S13, 0xA679438EL) # 15 
        b = XX(F, b, c, d, a, inp[15], S14, 0x49B40821L) # 16 

        # Round 2.

        S21, S22, S23, S24 = 5, 9, 14, 20

        a = XX(G, a, b, c, d, inp[ 1], S21, 0xF61E2562L) # 17 
        d = XX(G, d, a, b, c, inp[ 6], S22, 0xC040B340L) # 18 
        c = XX(G, c, d, a, b, inp[11], S23, 0x265E5A51L) # 19 
        b = XX(G, b, c, d, a, inp[ 0], S24, 0xE9B6C7AAL) # 20 
        a = XX(G, a, b, c, d, inp[ 5], S21, 0xD62F105DL) # 21 
        d = XX(G, d, a, b, c, inp[10], S22, 0x02441453L) # 22 
        c = XX(G, c, d, a, b, inp[15], S23, 0xD8A1E681L) # 23 
        b = XX(G, b, c, d, a, inp[ 4], S24, 0xE7D3FBC8L) # 24 
        a = XX(G, a, b, c, d, inp[ 9], S21, 0x21E1CDE6L) # 25 
        d = XX(G, d, a, b, c, inp[14], S22, 0xC33707D6L) # 26 
        c = XX(G, c, d, a, b, inp[ 3], S23, 0xF4D50D87L) # 27 
        b = XX(G, b, c, d, a, inp[ 8], S24, 0x455A14EDL) # 28 
        a = XX(G, a, b, c, d, inp[13], S21, 0xA9E3E905L) # 29 
        d = XX(G, d, a, b, c, inp[ 2], S22, 0xFCEFA3F8L) # 30 
        c = XX(G, c, d, a, b, inp[ 7], S23, 0x676F02D9L) # 31 
        b = XX(G, b, c, d, a, inp[12], S24, 0x8D2A4C8AL) # 32 

        # Round 3.

        S31, S32, S33, S34 = 4, 11, 16, 23

        a = XX(H, a, b, c, d, inp[ 5], S31, 0xFFFA3942L) # 33 
        d = XX(H, d, a, b, c, inp[ 8], S32, 0x8771F681L) # 34 
        c = XX(H, c, d, a, b, inp[11], S33, 0x6D9D6122L) # 35 
        b = XX(H, b, c, d, a, inp[14], S34, 0xFDE5380CL) # 36 
        a = XX(H, a, b, c, d, inp[ 1], S31, 0xA4BEEA44L) # 37 
        d = XX(H, d, a, b, c, inp[ 4], S32, 0x4BDECFA9L) # 38 
        c = XX(H, c, d, a, b, inp[ 7], S33, 0xF6BB4B60L) # 39 
        b = XX(H, b, c, d, a, inp[10], S34, 0xBEBFBC70L) # 40 
        a = XX(H, a, b, c, d, inp[13], S31, 0x289B7EC6L) # 41 
        d = XX(H, d, a, b, c, inp[ 0], S32, 0xEAA127FAL) # 42 
        c = XX(H, c, d, a, b, inp[ 3], S33, 0xD4EF3085L) # 43 
        b = XX(H, b, c, d, a, inp[ 6], S34, 0x04881D05L) # 44 
        a = XX(H, a, b, c, d, inp[ 9], S31, 0xD9D4D039L) # 45 
        d = XX(H, d, a, b, c, inp[12], S32, 0xE6DB99E5L) # 46 
        c = XX(H, c, d, a, b, inp[15], S33, 0x1FA27CF8L) # 47 
        b = XX(H, b, c, d, a, inp[ 2], S34, 0xC4AC5665L) # 48 

        # Round 4.

        S41, S42, S43, S44 = 6, 10, 15, 21

        a = XX(I, a, b, c, d, inp[ 0], S41, 0xF4292244L) # 49 
        d = XX(I, d, a, b, c, inp[ 7], S42, 0x432AFF97L) # 50 
        c = XX(I, c, d, a, b, inp[14], S43, 0xAB9423A7L) # 51 
        b = XX(I, b, c, d, a, inp[ 5], S44, 0xFC93A039L) # 52 
        a = XX(I, a, b, c, d, inp[12], S41, 0x655B59C3L) # 53 
        d = XX(I, d, a, b, c, inp[ 3], S42, 0x8F0CCC92L) # 54 
        c = XX(I, c, d, a, b, inp[10], S43, 0xFFEFF47DL) # 55 
        b = XX(I, b, c, d, a, inp[ 1], S44, 0x85845DD1L) # 56 
        a = XX(I, a, b, c, d, inp[ 8], S41, 0x6FA87E4FL) # 57 
        d = XX(I, d, a, b, c, inp[15], S42, 0xFE2CE6E0L) # 58 
        c = XX(I, c, d, a, b, inp[ 6], S43, 0xA3014314L) # 59 
        b = XX(I, b, c, d, a, inp[13], S44, 0x4E0811A1L) # 60 
        a = XX(I, a, b, c, d, inp[ 4], S41, 0xF7537E82L) # 61 
        d = XX(I, d, a, b, c, inp[11], S42, 0xBD3AF235L) # 62 
        c = XX(I, c, d, a, b, inp[ 2], S43, 0x2AD7D2BBL) # 63 
        b = XX(I, b, c, d, a, inp[ 9], S44, 0xEB86D391L) # 64 

        A = (A + a) & 0xffffffffL
        B = (B + b) & 0xffffffffL
        C = (C + c) & 0xffffffffL
        D = (D + d) & 0xffffffffL

        self.A, self.B, self.C, self.D = A, B, C, D


    # Down from here all methods follow the Python Standard Library
    # API of the md5 module.

    def update(self, inBuf):
        debug(__name__ + ", update")
        """Add to the current message.

        Update the md5 object with the string arg. Repeated calls
        are equivalent to a single call with the concatenation of all
        the arguments, i.e. m.update(a); m.update(b) is equivalent
        to m.update(a+b).
        """

        leninBuf = long(len(inBuf))

        # Compute number of bytes mod 64.
        index = (self.count[0] >> 3) & 0x3FL

        # Update number of bits.
        self.count[0] = self.count[0] + (leninBuf << 3)
        if self.count[0] < (leninBuf << 3):
            self.count[1] = self.count[1] + 1
        self.count[1] = self.count[1] + (leninBuf >> 29)

        partLen = 64 - index

        if leninBuf >= partLen:
            index = int(index)
            partLen = int(partLen)
            self.input[index:] = map(None, inBuf[:partLen])
            self._transform(_bytelist2long(self.input))
            i = partLen
            while i + 63 < leninBuf:
                self._transform(_bytelist2long(map(None, inBuf[i:i+64])))
                i = i + 64
            else:
                leninBuf = int(leninBuf)
                self.input = map(None, inBuf[i:leninBuf])
        else:
            i = 0
            self.input = self.input + map(None, inBuf)


    def digest(self):
        debug(__name__ + ", digest")
        """Terminate the message-digest computation and return digest.

        Return the digest of the strings passed to the update()
        method so far. This is a 16-byte string which may contain
        non-ASCII characters, including null bytes.
        """

        A = self.A
        B = self.B
        C = self.C
        D = self.D
        input = [] + self.input
        count = [] + self.count

        index = (self.count[0] >> 3) & 0x3fL

        if index < 56:
                padLen = 56 - index
        else:
                padLen = 120 - index

        padding = ['\200'] + ['\000'] * 63
        self.update(padding[:int(padLen)])

        # Append length (before padding).
        bits = _bytelist2long(self.input[:56]) + count

        self._transform(bits)

        # Store state in digest.
        digest = _long2bytes(self.A << 96, 16)[:4] + \
                 _long2bytes(self.B << 64, 16)[4:8] + \
                 _long2bytes(self.C << 32, 16)[8:12] + \
                 _long2bytes(self.D, 16)[12:]

        self.A = A 
        self.B = B
        self.C = C
        self.D = D
        self.input = input 
        self.count = count 

        return digest


    def hexdigest(self):
        debug(__name__ + ", hexdigest")
        """Terminate and return digest in HEX form.

        Like digest() except the digest is returned as a string of
        length 32, containing only hexadecimal digits. This may be
        used to exchange the value safely in email or other non-
        binary environments.
        """

        d = map(None, self.digest())
        d = map(ord, d)
        d = map(lambda x:"%02x" % x, d)
        d = string.join(d, '')

        return d


#    def copy(self):
        """Return a clone object.

        Return a copy ('clone') of the md5 object. This can be used
        to efficiently compute the digests of strings that share
        a common initial substring.
        """

#        return copy.deepcopy(self)


# ======================================================================
# Mimick Python top-level functions from standard library API
# for consistency with the md5 module of the standard library.
# ======================================================================

def MD5new(arg=None):
    debug(__name__ + ", MD5new")
    """Return a new md5 object.

    If arg is present, the method call update(arg) is made.
    """

    md5 = MD5()
    if arg:
        md5.update(arg)

    return md5


###############################################################################
#	BuildShipSelectWindow()	
#	
#	Build the stylized window from which the system can be selected
#	
#	Args:	TGPane					pMissionPane	- The pane to which our
#													events should be sent
#			TGLocalizationDatabase	pDatabase		- the database with our
#													text in it		
#	
#	Return:	A TGStylized window with a SubPane inside of it serving as a menu
###############################################################################
def RebuildShipSelectWindow():
	debug(__name__ + ", RebuildShipSelectWindow")
	Multiplayer.MissionMenusShared.g_iSpecies = 0
	UpdateStartButton()
	
	# Set the font larger
	App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcSmallFont, MainMenu.mainmenu.g_kSmallFontSize[MainMenu.mainmenu.g_iRes] + 1)

	# Find the Multiplayer window
	pTopWindow = App.TopWindow_GetTopWindow()
	pMultWindow = App.MultiplayerWindow_Cast(pTopWindow.FindMainWindow(App.MWT_MULTIPLAYER))
	# Get the mission pane
	pMissionPane = pMultWindow.GetMissionPane()

	pDatabase = Multiplayer.MissionShared.g_pDatabase
	pWindow = Multiplayer.MissionMenusShared.g_pShipSelectWindow
	pSubPane = App.STSubPane_Cast(pWindow.GetNthChild(0))

	# Delete everything so we can readd the buttons.
	pSubPane.KillChildren()

	#########################################
	# Create the buttons
	for iIndex in range(1, Multiplayer.SpeciesToShip.MAX_FLYABLE_SHIPS):
		# Create the button.	
		sSelectedTeam = Races.keys()[g_iTeam]
		sShipScript = Multiplayer.SpeciesToShip.GetScriptFromSpecies(iIndex)

		if Races[sSelectedTeam].NumFreeShips(sShipScript) > 0:
			# Setup the event for when this button is clicked
			pEvent = App.TGIntEvent_Create()
			pEvent.SetEventType(Multiplayer.MissionMenusShared.ET_SELECT_SHIP_SPECIES)
			pEvent.SetInt(iIndex)		# store the index so we know which button was clicked.
			pEvent.SetDestination(pMissionPane)
		
			pButton = App.STButton_CreateW (Multiplayer.MissionShared.g_pShipDatabase.GetString(sShipScript), pEvent)
			pSubPane.AddChild(pButton, 0, 0, 0)		
			pEvent.SetSource(pButton)

	pSubPane.Resize(pSubPane.GetWidth(), pSubPane.GetTotalHeightOfChildren(), 0)
	pWindow.Layout()
	pWindow.InteriorChangedSize()

	# Set the font back to normal
	App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcFlightSmallFont, MainMenu.mainmenu.g_kFlightSmallFontSize[MainMenu.mainmenu.g_iRes] + 1)

	# clear the previously selected button
	Multiplayer.MissionMenusShared.g_pChosenSpecies = None

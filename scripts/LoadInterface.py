###############################################################################
#	Filename:	LoadInterface.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games
#	
#	Functions for loading things dealing with the general game interface.
#	
#	Created:	5/24/2001 -	KDeus
###############################################################################

import App

#
# List linking interface sound names to sound files.  Used by
# LoadSounds and UnloadSounds.
g_lInterfaceSounds = (
	( "UIBeep",				"sfx/Interface/mouseover.wav" ),
	( "UIButtonClicked",	"sfx/Interface/mouseclick.wav" ),
	( "UIMenuOpened",		"sfx/Interface/menu3_open.wav" ),
	( "UIMenuClosed",		"sfx/Interface/menu3_close.wav" ),
	( "UITextEntryClick",	"sfx/Interface/typing.wav" ),
	( "UIMinimize",			"sfx/Interface/minimize_window.wav" ),
	( "UIUnminimize",		"sfx/Interface/maximize_window.wav" ),
	( "UIQuit",				"sfx/Interface/exit.wav" ),
	( "UIStart",			("sfx/Interface/new_game.wav", "sfx/Interface/new_game2.wav", "sfx/Interface/new_game3.wav")[App.g_kSystemWrapper.GetRandomNumber(3)] ),
	( "UIScrolling",		"sfx/Interface/scroll_loop_1.wav" ),
	( "UINumericBarClick",	"sfx/Interface/slider_tick.wav" ),
	( "UIScanObject",		"sfx/Interface/scanning3.wav" ),
	( "UIScanArea",			"sfx/Interface/scanning.wav" ),
	( "UITorpsNotLoaded",	"sfx/Interface/fire_torp_none_ready.wav" ),
	( "UITorpsNoAmmo",		"sfx/Interface/fire_torp_no_ammo.wav" ),
	( "UICrosshair",		"sfx/Interface/crosshair.wav" ),
	)

###############################################################################
#	LoadSounds
#	
#	Load interface sounds.
#	
#	Args:	None
#	
#	Return:	None
###############################################################################
def LoadSounds():
	for sName, sFile in g_lInterfaceSounds:
		pSound = App.TGSound_Create(sFile, sName, 0)
		# All interface sounds count as sfx.
		pSound.SetSFX(0)
		pSound.SetInterface(1)

###############################################################################
#	UnloadSounds
#	
#	Unload sounds loaded by LoadSounds.
#	
#	Args:	None
#	
#	Return:	None
###############################################################################
def UnloadSounds():
	for sName, sFile in g_lInterfaceSounds:
		App.g_kSoundManager.DeleteSound(sName)

###############################################################################
#	SetupColors()
#	
#	Called to set up some standard colors for the interface.
#	
#	Args:	none
#	
#	Return:	none
###############################################################################
def SetupColors():
	# STButton marker colors.
	SetupColor(App.g_kSTButtonMarkerDefault, 250.0 / 255.0, 181.0 / 255.0, 80.0 / 255.0, 1.0)
	SetupColor(App.g_kSTButtonMarkerHighlighted, 245.0 / 255.0, 242.0 / 255.0, 82.0 / 255.0, 1.0)
	SetupColor(App.g_kSTButtonMarkerSelected, 203.0 / 255.0, 153.0 / 255.0, 204.0 / 255.0, 1.0)
	#SetupColor(App.g_kSTButtonMarkerGray, 69.0 / 255.0, 66.0 / 255.0, 0.0 / 255.0, 1.0)
	SetupColor(App.g_kSTButtonMarkerGray, 104.0 / 255.0, 101.0 / 255.0, 27.0 / 255.0, 1.0)

	SetupColor(App.g_kSTButtonCheckmarkOn, 251.0 / 255.0, 255.0 / 255.0, 112.0 / 255.0, 1.0)
	SetupColor(App.g_kSTButtonCheckmarkOff, 0.0, 0.0, 0.0, 1.0)

	# Menu colors
	SetupColor(App.g_kSTMenuArrowColor, 215.0 / 255.0, 215.0 / 255.0, 215.0 / 255.0, 1.0)

	SetupColor(App.g_kSTMenu1NormalBase, 103.0 / 255.0, 149.0 / 255.0, 251.0 / 255.0, 1.0)
	SetupColor(App.g_kSTMenu1HighlightedBase, 141.0 / 255.0, 190.0 / 255.0, 236.0 / 255.0, 1.0)
	SetupColor(App.g_kSTMenu1Disabled, 0.25, 0.25, 0.25, 1.0)
	SetupColor(App.g_kSTMenu1OpenedHighlightedBase, 141.0 / 255.0, 190.0 / 255.0, 236.0 / 255.0, 1.0)
	SetupColor(App.g_kSTMenu1Selected, 252.0 / 255.0, 254.0 / 255.0, 206.0 / 255.0, 1.0)

	SetupColor(App.g_kSTMenu2NormalBase, 255.0 / 255.0, 204.0 / 255.0, 102.0 / 255.0, 1.0)
	SetupColor(App.g_kSTMenu2HighlightedBase, 252.0 / 255.0, 204.0 / 255.0, 0.0 / 255.0, 1.0)
	SetupColor(App.g_kSTMenu2Disabled, 0.25, 0.25, 0.25, 1.0)
	SetupColor(App.g_kSTMenu2OpenedHighlightedBase, 252.0 / 255.0, 204.0 / 255.0, 0.0 / 255.0, 1.0)
	SetupColor(App.g_kSTMenu2Selected, 245.0 / 255.0, 242.0 / 255.0, 82.5 / 255.0, 1.0)

	SetupColor(App.g_kSTMenu3NormalBase, 100.0 / 255.0, 109.0 / 255.0, 204.0 / 255.0, 1.0)
	SetupColor(App.g_kSTMenu3HighlightedBase, 203.0 / 255.0, 153.0 / 255.0, 204.0 / 255.0, 1.0)
	SetupColor(App.g_kSTMenu3Disabled, 0.25, 0.25, 0.25, 1.0)
	SetupColor(App.g_kSTMenu3OpenedHighlightedBase, 156.0 / 255.0, 156.0 / 255.0, 255.0 / 255.0, 1.0)
	SetupColor(App.g_kSTMenu3Selected, 198.5 / 255.0, 181.0 / 255.0, 239.5 / 104.0, 1.0)

	SetupColor(App.g_kSTMenu4NormalBase, 100.0 / 255.0, 109.0 / 255.0, 204.0 / 255.0, 1.0)
	SetupColor(App.g_kSTMenu4HighlightedBase, 156.0 / 255.0, 156.0 / 255.0, 255.0 / 255.0, 1.0)
	SetupColor(App.g_kSTMenu4Disabled, 0.25, 0.25, 0.25, 1.0)
	SetupColor(App.g_kSTMenu4OpenedHighlightedBase, 156.0 / 255.0, 156.0 / 255.0, 255.0 / 255.0, 1.0)
	SetupColor(App.g_kSTMenu4Selected, 198.0 / 255.0, 181.5 / 255.0, 239.0 / 255.0, 1.0)

	SetupColor(App.g_kSTMenuTextColor, 0.0, 0.0, 0.0, 1.0)
	SetupColor(App.g_kSTMenuTextSelectedColor, 1.0, 1.0, 1.0, 1.0)
	SetupColor(App.g_kSTMenuTextHighlightColor, 1.0, 1.0, 1.0, 1.0)

	SetupColor(App.g_kTextEntryColor, 0.5, 0.5, 0.8, 1.0)
	SetupColor(App.g_kTextHighlightColor, 0.2196, 0.4196, 0.3843, 1.0)

	SetupColor(App.g_kTextEntryBackgroundColor, 225.0 / 255.0, 183.0 / 255.0, 82.0 / 255.0, 1.0)
	SetupColor(App.g_kTextEntryBackgroundHighlightColor, 249.0 / 255.0, 232.0 / 255.0, 167.0 / 255.0, 1.0)

	# Tactical Interface Colors
	SetupColor(App.g_kTIPhotonReadyColor, 0.0, 1.0, 0.0, 1.0)
	SetupColor(App.g_kTIPhotonNotReadyColor, 1.0, 0.0, 0.0, 1.0)

	# Radar border highlight color
	SetupColor(App.g_kSTRadarBorderHighlighted, 173.0 / 255.0, 144.0 / 255.0, 99.0 / 255.0, 1.0)

	# General Interface Colors
	SetupColor(App.g_kTitleColor, 100.0 / 255.0, 109.0 / 255.0, 204.0 / 255.0, 1.0)
	SetupColor(App.g_kInterfaceBorderColor, 173.0 / 255.0, 144.0 / 255.0, 99.0 / 255.0, 1.0)
	SetupColor(App.g_kLeftSeparatorColor, 253.0 / 255.0, 255.0 / 255.0, 207.0 / 255.0, 1.0)


	# Radar colors
	SetupColor(App.g_kRadarBorder, 173.0 / 255.0, 144.0 / 255.0, 99.0 / 255.0, 0.5)
	SetupColor(App.g_kSTRadarIncomingTorpColor, 1.00, 1.00, 0.0, 1.0)
	SetupColor(App.g_kRadarFriendlyColor, 100.0 / 255.0, 109.0 / 255.0, 204.0 / 255.0, 1.0)
	SetupColor(App.g_kRadarEnemyColor, 174.0 / 255.0, 0.0 / 255.0, 1.0 / 255.0, 1.0)
	SetupColor(App.g_kRadarNeutralColor, 1.0, 1.0, 0.68627, 1.0)
	SetupColor(App.g_kRadarUnknownColor, 127.5 / 255.0, 127.5 / 255.0, 127.5 / 255.0, 1.0)

	# Subsystem colors, used in subsystem menus for fill gauge.
	SetupColor(App.g_kSubsystemFillColor, 202.6 / 255.0, 171.0 / 255.0, 116 / 255.0, 1.0)
	SetupColor(App.g_kSubsystemEmptyColor, 170.6 / 255.0, 25.0 / 255.0, 25.0 / 255.0, 1.0)
	SetupColor(App.g_kSubsystemDisabledColor, 0.6, 0.6, 0.6, 1.0)

	# Color used for header text in the tactical weapons control.
	SetupColor(App.g_kTacWeaponsCtrlHeaderTextColor, 190.0 / 255.0, 188.0 / 255.0, 191.0 / 204.0, 1.0)

	# Damage display colors.
	SetupColor(App.g_kDamageDisplayDestroyedColor, 174.0 / 255.0, 0.0 / 255.0, 1.0 / 255.0, 1.0)
	SetupColor(App.g_kDamageDisplayDamagedColor, 100.0 / 255.0, 109.0 / 255.0, 204.0 / 255.0, 1.0)
	SetupColor(App.g_kDamageDisplayDisabledColor, 100.0 / 255.0, 109.0 / 255.0, 204.0 / 255.0, 1.0)

	# Main menu colors, which are used elsewhere.
	SetupColor(App.g_kMainMenuButtonColor,  203.0 / 255.0, 153.0 / 255.0, 204.0 / 255.0, 1.0)
	SetupColor(App.g_kMainMenuButtonHighlightedColor, 255.0 / 255.0, 204.0 / 255.0, 102.0 / 255.0, 1.0)
	SetupColor(App.g_kMainMenuButtonSelectedColor, 245.0 / 255.0, 162.0 / 255.0, 16.0 / 255.0, 1.0)

	SetupColor(App.g_kMainMenuButton1Color, 203.0 / 255.0, 153.0 / 255.0, 204.0 / 255.0, 1.0)
	SetupColor(App.g_kMainMenuButton1HighlightedColor, 217.0 / 255.0, 170.0 / 255.0, 197.0 / 255.0, 1.0)
	SetupColor(App.g_kMainMenuButton1SelectedColor, 245.0 / 255.0, 162.0 / 255.0, 16.0 / 255.0, 1.0)

	SetupColor(App.g_kMainMenuButton2Color, 252.0 / 255.0, 183.0 / 255.0, 82.0 / 255.0, 1.0)
	SetupColor(App.g_kMainMenuButton2HighlightedColor, 245.0 / 255.0, 172.0 / 255.0, 199.0 / 255.0, 1.0)
	SetupColor(App.g_kMainMenuButton2SelectedColor, 121.0 / 255.0, 55.0 / 255.0, 79.0 / 255.0, 1.0)

	SetupColor(App.g_kMainMenuButton3Color, 201.0 / 255.0, 96.0 / 255.0, 97.0 / 255.0, 1.0)
	SetupColor(App.g_kMainMenuButton3HighlightedColor, 202.0 / 255.0, 103 / 255.0, 204 / 255.0, 1.0)
	SetupColor(App.g_kMainMenuButton3SelectedColor, 20.0 / 255.0, 1.0 / 255.0, 1.0 / 255.0, 1.0)

	SetupColor(App.g_kMainMenuBorderMainColor, 255.0 / 255.0, 204.0 / 255.0, 102.0 / 255.0, 1.0)
	SetupColor(App.g_kMainMenuBorderOffColor, 203.0 / 255.0, 153.0 / 255.0, 204.0 / 255.0, 1.0)
	SetupColor(App.g_kMainMenuBorderBlock1Color, 255.0 / 255.0, 204.0 / 255.0, 102.0 / 255.0, 1.0)
	SetupColor(App.g_kMainMenuBorderTopColor, 203.0 / 255.0, 153.0 / 255.0, 204.0 / 255.0, 1.0)

	# Engineering display colors.
	SetupColor(App.g_kEngineeringShieldsColor, 198.0 / 255.0, 181.0 / 255.0, 239.0 / 255.0, 1.0)
	SetupColor(App.g_kEngineeringEnginesColor, 100.0 / 255.0, 109.0 / 255.0, 204.0 / 255.0, 1.0)
	SetupColor(App.g_kEngineeringWeaponsColor, 70.0 / 255.0, 76.0 / 255.0, 139.0 / 255.0, 1.0)
	SetupColor(App.g_kEngineeringSensorsColor, 156.0 / 255.0, 156.0 / 255.0, 255.0 / 255.0, 1.0)
	SetupColor(App.g_kEngineeringCloakColor, 198.0 / 255.0, 181.0 / 255.0, 239.0 / 255.0, 1.0)
	SetupColor(App.g_kEngineeringTractorColor, 75.0 / 255.0, 176.0 / 255.0, 255.0 / 255.0, 1.0)

	SetupColor(App.g_kEngineeringWarpCoreColor, 255.0 / 255.0, 156.0 / 255.0, 0.0 / 255.0, 1.0)
	SetupColor(App.g_kEngineeringMainPowerColor, 247.0 / 255.0, 189.0 / 255.0, 90.0 / 255.0, 1.0)
	SetupColor(App.g_kEngineeringBackupPowerColor, 253.0 / 255.0, 253.0 / 255.0, 154.0 / 255.0, 1.0)

	SetupColor(App.g_kEngineeringCtrlBkgndLineColor, 198.0 / 255.0, 181.0 / 255.0, 239.0 / 255.0, 1.0)

	# QuickBattle and Multiplayer Colors
	SetupColor(App.g_kQuickBattleBrightRed, 174.0 / 255.0, 0.0 / 255.0, 1.0 / 255.0, 1.0)
	SetupColor(App.g_kMultiplayerBorderBlue, 255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.0)
	SetupColor(App.g_kMultiplayerBorderPurple, 247.0 / 255.0, 189.0 / 255.0, 90.0 / 255.0, 1.0)
	SetupColor(App.g_kMultiplayerStylizedPurple, 178.0 / 255.0, 132.0 / 255.0, 82.0 / 255.0, 1.0)
	SetupColor(App.g_kMultiplayerButtonPurple, 216.0 / 255.0, 191.0 / 255.0, 170.0 / 255.0, 1.0)
	SetupColor(App.g_kMultiplayerButtonOrange, 255.0 / 255.0, 183.0 / 255.0, 0.0 / 255.0, 1.0)
	#SetupColor(App.g_kMultiplayerRadioPink, 194.0 / 255.0, 152.0 / 255.0, 176.0 / 255.0, 1.0)
	SetupColor(App.g_kMultiplayerDividerPurple, 174.0 / 255.0, 105.0 / 255.0, 125.0 / 255.0, 1.0)


###############################################################################
#	SetupColor(kColor, fRed, fGreen, fBlue, fAlpha)
#	
#	Sets up a single color.
#	
#	Args:	kColor						- the color
#			fRed, fGreen, fBlue, fAlpha	- the color values, [0..1]
#	
#	Return:	none
###############################################################################
def SetupColor(kColor, fRed, fGreen, fBlue, fAlpha):
	kColor.r = fRed
	kColor.g = fGreen
	kColor.b = fBlue
	kColor.a = fAlpha

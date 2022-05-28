###############################################################################
#	Filename:	RHCD.py
#	
#	Confidential and Proprietary, Copyright 2002 by Totally Games
#	
#	The game object for my custom missions.
#	
#	Created:	4/10/2002 -	Brian Moler (RedHotChiliDog)
###############################################################################
import App
import MissionLib

# Globals
g_idPlayer = App.NULL_ID

###############################################################################
#	Initialize(pGame)
#	
#	Initializes the game.
#	
#	Args:	pGame	- the game object
#	
#	Return:	none
###############################################################################
def Initialize(pGame):
	"Called Initialize and activate our Game"
	#
	# This is where you might set up your Game level module globals
	# don't forget to declare them global so they aren't treated as
	# Initialize() locals.
	#

	# Set our Game level TGL
	pGame.SetDatabase("data/TGL/RHCD/RHCD.tgl")

	# Set the game name, for use with data files and such
	App.g_kUtopiaModule.SetGameName("RHCD")

	#
	# This is where you might setup handlers to listen for Episode
	# completion events, to trigger Game events that are handled by
	# loading up the next Episode and playing mid-game cutscenes
	#
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_DESTROYED, 
											pGame, __name__ + ".ObjectDestroyed")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SET_PLAYER,
											pGame, __name__ + ".HandlePlayerChanged")
	
	#
	# Load the Game persistent stuff.
	#

	#
	# Start up the music system.
	#
	SetupMusic(pGame)

	# Load the Sounds for Tactical Station
	import LoadTacticalSounds
	LoadTacticalSounds.LoadSounds()

	#
	# Clear our SetManager and start loading the initial Episode
	#
	App.g_kSetManager.ClearRenderedSet()

	# Check if there is an episode override, and if so, then
	# use it.
	pcOverride = App.g_kVarManager.GetStringVariable("Options", "EpisodeOverride")

	if (pcOverride != ""):
		pGame.LoadEpisode("Custom.RHCD." + pcOverride + "." + pcOverride)
		App.g_kVarManager.SetStringVariable("Options", "EpisodeOverride", "")
	else:
		pGame.LoadEpisode("Custom.RHCD.Episode.Episode")



###############################################################################
#	SetupMusic(pGame)
#	
#	Sets up the dynamic music system.
#	
#	Args:	pGame	- the game object
#	
#	Return:	none
###############################################################################
def SetupMusic(pGame):
	# Start up dynamic music.
	import DynamicMusic
	DynamicMusic.Initialize(pGame,
		# Base songs/fanfares to use as music...
		(("sfx/Music/Episode 7.mp3", "Starting Ambient"),
		("sfx/Music/Starbase12.mp3", "Starbase12 Ambient"),
		("sfx/Music/Nebula 1.mp3", "Nebula Ambient"),
		("sfx/Music/Panic-9a.mp3", "Cbt Panic 1"),
		("sfx/Music/Panic-9b.mp3", "Cbt Panic 2"),
		("sfx/Music/Panic-9c.mp3", "Cbt Panic 3"),
		("sfx/Music/Panic-9d.mp3", "Cbt Panic 4"),
		("sfx/Music/Panic-9e.mp3", "Cbt Panic 5"),
		("sfx/Music/Panic-9f.mp3", "Cbt Panic 6"),
		("sfx/Music/Panic-9g.mp3", "Cbt Panic 7"),
		("sfx/Music/Neutral-10i.mp3", "Cbt Neutral 1"),
		("sfx/Music/Neutral-10b.mp3", "Cbt Neutral 2"),
		("sfx/Music/Neutral-10c.mp3", "Cbt Neutral 3"),
		("sfx/Music/Neutral-10d.mp3", "Cbt Neutral 4"),
		("sfx/Music/Neutral-10e.mp3", "Cbt Neutral 5"),
		("sfx/Music/Neutral-10f.mp3", "Cbt Neutral 6"),
		("sfx/Music/Neutral-10g.mp3", "Cbt Neutral 7"),
		("sfx/Music/Neutral-10h.mp3", "Cbt Neutral 8"),
		("sfx/Music/Neutral-10a.mp3", "Cbt Neutral 9"),
		("sfx/Music/Confident-11a.mp3", "Cbt Confident 1"),
		("sfx/Music/Confident-11b.mp3", "Cbt Confident 2"),
		("sfx/Music/Confident-11c.mp3", "Cbt Confident 3"),
		("sfx/Music/Confident-11d.mp3", "Cbt Confident 4"),
		("sfx/Music/Confident-11e.mp3", "Cbt Confident 5"),
		("sfx/Music/Confident-11f.mp3", "Cbt Confident 6"),
		("sfx/Music/Confident-11g.mp3", "Cbt Confident 7")),
		# Which music to use as a transition between 2
		# other pieces.
		(),
		# Special music states which are collections of
		# pieces of music, played in random order.
		(("Nebula Ambient", ("Nebula1",
				"Nebula2")),
		("Combat Panic", ("Cbt Panic 1",
				"Cbt Panic 2",
				"Cbt Panic 3",
				"Cbt Panic 4",
				"Cbt Panic 5",
				"Cbt Panic 6",
				"Cbt Panic 7")),
		("Combat Neutral", ("Cbt Neutral 1",
				"Cbt Neutral 2",
				"Cbt Neutral 3",
				"Cbt Neutral 4",
				"Cbt Neutral 5",
				"Cbt Neutral 6",
				"Cbt Neutral 7",
				"Cbt Neutral 8",
				"Cbt Neutral 9")),
		("Combat Confident", ("Cbt Confident 1",
				"Cbt Confident 2",
				"Cbt Confident 3",
				"Cbt Confident 4",
				"Cbt Confident 5",
				"Cbt Confident 6",
				"Cbt Confident 7"))),
		# Which state machine to use
		DynamicMusic.StandardCombatMusic
		)

################################################################################
#	ObjectDestroyed(pObject, pEvent)
#
#	Called when an object is destroyed. If it's the player's ship,
#	return the player to the main menu.
#
#	Args:	pObject	- The TGObject object.
#		pEvent	- The event that was sent.
#
#	Return:	None
################################################################################
def ObjectDestroyed(pObject, pEvent):
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	if pShip and (pShip.GetObjID() == g_idPlayer):
		pSequence = App.TGSequence_Create()
		pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "FadeOut"))
		pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "ExitGame"))
		pSequence.Play()

###############################################################################
#	HandlePlayerChanged(pGame, pEvent)
#	
#	Called when the player is changed. Sets up handlers for the player's
#	warp engines.
#	
#	Args:	pGame	- the game
#		pEvent	- the event
#	
#	Return:	none
###############################################################################
def HandlePlayerChanged(pGame, pEvent):
	global g_idPlayer

	pPlayer = App.Game_GetCurrentPlayer()
	if (pPlayer == None):
		g_idPlayer = App.NULL_ID
		return

	g_idPlayer = pPlayer.GetObjID()

###############################################################################
#	MakeMissionButton(sName)
#	
#	Makes a mission button for this campaign.
#	
#	Args:	sName	- the name for the button
#	
#	Return:	the button
###############################################################################
def MakeMissionButton(sName):
	import MainMenu.mainmenu

	pButton = App.STButton_Create(sName)
	pEvent = App.TGEvent_Create()
	pEvent.SetEventType(MainMenu.mainmenu.ET_CUSTOM_MISSION)
	pEvent.SetDestination(pButton)
	pButton.SetActivationEvent(pEvent)
	pButton.AddPythonFuncHandlerForInstance(MainMenu.mainmenu.ET_CUSTOM_MISSION, __name__ + ".MissionHandler")

	return pButton

###############################################################################
#	CreateMenu()
#	
#	Creates a menu for the custom mission menu. Allows the player to select
#	any mission in this campaign.
#	
#	Args:	none
#	
#	Return:	none
###############################################################################
def CreateMenu():
	pMenu = App.STMenu_Create("RHCD Missions")

	pMenu.AddChild(MakeMissionButton("TNG Klingon Kobayashi Maru"))
	pMenu.AddChild(MakeMissionButton("TNG Romulan Kobayashi Maru"))
        # Defiant: disabled because we don't have these ships in FBCMP
	#pMenu.AddChild(MakeMissionButton("TOS Classic Kobayashi Maru"))
	pMenu.AddChild(MakeMissionButton("TNG Cardassian Kobayashi Maru"))
	pMenu.AddChild(MakeMissionButton("Klingon Overrun Defense"))
	pMenu.AddChild(MakeMissionButton("Romulan Overrun Defense"))
	pMenu.AddChild(MakeMissionButton("Cardassian Overrun Defense"))
	pMenu.AddChild(MakeMissionButton("Klingon Target of Opportunity"))
	pMenu.AddChild(MakeMissionButton("Romulan Target of Opportunity"))
	pMenu.AddChild(MakeMissionButton("Cardassian Target of Opportunity"))
	pMenu.AddChild(MakeMissionButton("Random Skirmish"))

	return pMenu

###############################################################################
#	MissionHandler(pButton, pEvent)
#	
#	Handler for button presses, for the mission selection menu.
#	
#	Args:	pButton	- the button that triggered us. Used to determine the
#					  correct override mission.
#			pEvent	- the event
#	
#	Return:	none
###############################################################################
def MissionHandler(pButton, pEvent):
	pButton = App.STButton_Cast(pButton)
	if not pButton:
		App.Breakpoint()
	import MainMenu.mainmenu

	dButtonToOverride = {
		"TNG Klingon Kobayashi Maru":		["Episode", "M1"],
		"TNG Romulan Kobayashi Maru":		["Episode", "M2"],
		"TOS Classic Kobayashi Maru":		["Episode", "M3"],
		"TNG Cardassian Kobayashi Maru":	["Episode", "M4"],
		"Klingon Overrun Defense":		["Episode", "M5"],
		"Romulan Overrun Defense":		["Episode", "M6"],
		"Cardassian Overrun Defense":		["Episode", "M7"],
		"Klingon Target of Opportunity":	["Episode", "M8"],
		"Romulan Target of Opportunity":	["Episode", "M9"],
		"Cardassian Target of Opportunity":	["Episode", "M10"],
		"Random Skirmish":		        ["Episode", "M11"]
	}

	kString = App.TGString()
	pButton.GetName(kString)

	sName = kString.GetCString()

	if dButtonToOverride.has_key(sName):
		App.g_kVarManager.SetStringVariable("Options", "EpisodeOverride", dButtonToOverride[sName][0])
		App.g_kVarManager.SetStringVariable("Options", "MissionOverride", dButtonToOverride[sName][1])
	else:
		App.g_kVarManager.SetStringVariable("Options", "EpisodeOverride", "")
		App.g_kVarManager.SetStringVariable("Options", "MissionOverride", "")

	# Send the override mission event.
	pTop = App.TopWindow_GetTopWindow()
	pOptions = pTop.FindMainWindow(App.MWT_OPTIONS)
	pEvent = App.TGStringEvent_Create()
	pEvent.SetEventType(MainMenu.mainmenu.ET_CUSTOM_MISSION)
	pEvent.SetDestination(pOptions)
	pEvent.SetString("RHCD")
	App.g_kEventManager.AddEvent(pEvent)
	return
	
###############################################################################
#	Terminate(pGame)
#	
#	Cleans up the game.
#	
#	Args:	pGame	- the game object
#	
#	Return:	none
###############################################################################
def Terminate(pGame):
	#
	# Unload our bridge set, which is specifically ignored from 
	# mission to mission, and generally ignored by the Episodes
	#
	App.g_kSetManager.DeleteAllSets()

	import DynamicMusic
	DynamicMusic.Terminate(pGame)

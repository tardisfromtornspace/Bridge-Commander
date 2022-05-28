from bcdebug import debug
###############################################################################
#	Filename:	Brex.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Brex, the Engineer, and configures animations.
#	
#	Created:	3/28/00 -	Erik Novales
###############################################################################

import App
import Bridge.BridgeUtils
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create Brex by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating Brex")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("Engineer") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Engineer")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadBrex/brex_head_no_mouth.nif", None)
	pIntBrex = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", CharacterPaths.g_pcHeadNIFPath + "HeadBrex/brex_head_no_mouth.nif")
	pIntBrex.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Brex/brex_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/brex_head.tga")

	pIntBrex.SetCharacterName("Brex")

	# Add the character to the set
	pSet.AddObjectToSet(pIntBrex, "Engineer")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pIntBrex)

	# Setup the character configuration
	pIntBrex.SetSize(App.CharacterClass.SMALL)
	pIntBrex.SetGender(App.CharacterClass.MALE)
	pIntBrex.SetRandomAnimationChance(.75)
	pIntBrex.SetBlinkChance(0.1)

	pIntBrex.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Engineering officer generic sounds
	LoadSounds()

	pIntBrex.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_blink1.tga")
	pIntBrex.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_blink2.tga")
	pIntBrex.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_eyes_close.tga")
	pIntBrex.SetBlinkStages(3)

	pIntBrex.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_head_a.tga")
	pIntBrex.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_head_e.tga")
	pIntBrex.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_head_u.tga")
	pIntBrex.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pIntBrex.GetDatabase(), "BrexNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pIntBrex.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Engineering")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	pIntBrex.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pIntBrex.SetLocation("")

#	kDebugObj.Print("Finished creating Brex")
	return pIntBrex


###############################################################################
#	ConfigureForShip()
#
#	Configure ourselves for the particular ship object.  This involves setting
#	up range watchers that tell us how to report.
#
#	Args:	pSet	- the Set object
#			pShip	- the player's ship (ShipClass object)
#
#	Return:	none
###############################################################################
def ConfigureForShip(pSet, pShip):
	debug(__name__ + ", ConfigureForShip")
	pIntBrex = App.CharacterClass_Cast(pSet.GetObject("Engineer"))
	if (pIntBrex == None):
#		kDebugObj.Print("******* Engineering officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Engineer..")
	import Bridge.EngineerCharacterHandlers
	Bridge.EngineerCharacterHandlers.AttachMenuToEngineer(pIntBrex)

	# Set up the status events that we need - Shield and Hull
	# Other events (repairs, subsystem reports) are generated elsewhere
	pShieldWatcher = pShip.GetShields().GetShieldWatcher(6)
	pHullWatcher = pShip.GetHull().GetCombinedPercentageWatcher()

	lWatchers = (
		( pShieldWatcher,	App.ET_TACTICAL_SHIELD_LEVEL_CHANGE ),
		( pHullWatcher,		App.ET_TACTICAL_HULL_LEVEL_CHANGE ) )

	lRanges = ( 0.05, 0.1, 0.15, 0.2, 0.25, 0.5, 0.75 )

	for pWatcher, eEventType in lWatchers:
		for fRange in lRanges:
			# Need an event for this range check..
			pEvent = App.TGFloatEvent_Create()
			pEvent.SetEventType(eEventType)
			pEvent.SetDestination(pShip)

			pWatcher.AddRangeCheck(fRange, App.FloatRangeWatcher.FRW_BELOW, pEvent)

	lWatchers = (
		( pShip.GetShields().GetShieldWatcher(0), App.ET_TACTICAL_SHIELD_0_LEVEL_CHANGE ),
		( pShip.GetShields().GetShieldWatcher(1), App.ET_TACTICAL_SHIELD_1_LEVEL_CHANGE ),
		( pShip.GetShields().GetShieldWatcher(2), App.ET_TACTICAL_SHIELD_2_LEVEL_CHANGE ),
		( pShip.GetShields().GetShieldWatcher(3), App.ET_TACTICAL_SHIELD_3_LEVEL_CHANGE ),
		( pShip.GetShields().GetShieldWatcher(4), App.ET_TACTICAL_SHIELD_4_LEVEL_CHANGE ),
		( pShip.GetShields().GetShieldWatcher(5), App.ET_TACTICAL_SHIELD_5_LEVEL_CHANGE ) )

	lRanges = ( 0.05, 0.5)

	for pWatcher, eEventType in lWatchers:
		for fRange in lRanges:
			# Need an event for this range check..
			pEvent = App.TGFloatEvent_Create()
			pEvent.SetEventType(eEventType)
			pEvent.SetDestination(pShip)

			pWatcher.AddRangeCheck(fRange, App.FloatRangeWatcher.FRW_BELOW, pEvent)


###############################################################################
#	ConfigureForIntrepid()
#
#	Configure ourselves for the Intrepid bridge
#
#	Args:	pIntBrex	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForIntrepid(pIntBrex):
#	kDebugObj.Print("Configuring Brex for the Intrepid bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForIntrepid")
	pIntBrex.ClearAnimations()

	# Register animation mappings
	pIntBrex.AddAnimation("SeatedIntEngineer", "Bridge.Characters.CommonAnimations.StandingConsole")
	pIntBrex.AddAnimation("EBL1SToE", "Bridge.Characters.Brex.EBMoveFromL1ToE")
	pIntBrex.AddAnimation("SovereignEngSeatedToE", "Bridge.Characters.Brex.EBMoveFromL1ToE")
	pIntBrex.AddAnimation("EBEngineerToL1", "Bridge.Characters.Brex.EBMoveFromEToL1")
	pIntBrex.AddAnimation("IntEngineerTurnCaptain", "Bridge.Characters.IntSmallAnimations.IntTurnAtETowardsCaptain")
	pIntBrex.AddAnimation("IntEngineerBackCaptain", "Bridge.Characters.IntSmallAnimations.IntTurnBackAtEFromCaptain")
	pIntBrex.AddAnimation("EBEngineer1ToE", "Bridge.Characters.IntSmallAnimations.EBMoveFromE1ToE")
	pIntBrex.AddAnimation("EBEngineerToE1", "Bridge.Characters.IntSmallAnimations.EBMoveFromEToE1")
	pIntBrex.AddAnimation("EBEngineer2ToE", "Bridge.Characters.IntSmallAnimations.EBMoveFromE2ToE")
	pIntBrex.AddAnimation("EBEngineerToE2", "Bridge.Characters.IntSmallAnimations.EBMoveFromEToE2")
	pIntBrex.AddAnimation("EBEngineer1ToE2", "Bridge.Characters.IntSmallAnimations.EBMoveFromE1ToE2")
	pIntBrex.AddAnimation("EBEngineer2ToE1", "Bridge.Characters.IntSmallAnimations.EBMoveFromE2ToE1")

	pIntBrex.AddAnimation("IntEngineerGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pIntBrex.AddAnimation("IntEngineerGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.StandingConsole")

	pIntBrex.AddAnimation("EBEngineerTurnC", "Bridge.Characters.IntSmallAnimations.EBETalkC")
	pIntBrex.AddAnimation("EBEngineerBackC", "Bridge.Characters.CommonAnimations.StandingConsole")
	pIntBrex.AddAnimation("EBEngineerTurnH", "Bridge.Characters.IntSmallAnimations.EBETalkH")
	pIntBrex.AddAnimation("EBEngineerBackH", "Bridge.Characters.CommonAnimations.StandingConsole")
	pIntBrex.AddAnimation("EBEngineerTurnS", "Bridge.Characters.IntSmallAnimations.EBETalkS")
	pIntBrex.AddAnimation("EBEngineerBackS", "Bridge.Characters.CommonAnimations.StandingConsole")
	pIntBrex.AddAnimation("EBEngineerTurnT", "Bridge.Characters.IntSmallAnimations.EBETalkT")
	pIntBrex.AddAnimation("EBEngineerBackT", "Bridge.Characters.CommonAnimations.StandingConsole")

	pIntBrex.AddAnimation("IntEngineerTurnX", "Bridge.Characters.IntSmallAnimations.IntTurnAtETowardsCaptain")
	pIntBrex.AddAnimation("IntEngineerBackX", "Bridge.Characters.IntSmallAnimations.IntTurnBackAtEFromCaptain")

	# Breathing
	pIntBrex.AddAnimation("EBEngineerBreathe", "Bridge.Characters.CommonAnimations.StandingConsole")
	pIntBrex.AddAnimation("EBEngineerBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pIntBrex.AddRandomAnimation("Bridge.Characters.IntSmallAnimations.IntEConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pIntBrex.AddAnimation("PushingButtons", "Bridge.Characters.IntSmallAnimations.IntEConsoleInteraction")

	# Hit animations
	pIntBrex.AddAnimation("IntEngineerHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pIntBrex.AddAnimation("IntEngineerHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pIntBrex.AddAnimation("IntEngineerReactLeftStanding", "Bridge.Characters.CommonAnimations.ReactLeft");
	pIntBrex.AddAnimation("IntEngineerReactRightStanding", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	AddCommonAnimations(pIntBrex)

	# Brex sits on the Int bridge
	pIntBrex.SetStanding(0)
	pIntBrex.SetLocation("IntEngineer")
	pIntBrex.AddPositionZoom("IntEngineer", 0.55)
	pIntBrex.AddPositionZoom("IntEngineer1", 0.55)
	pIntBrex.AddPositionZoom("IntEngineer2", 0.55)
#	kDebugObj.Print("Finished configuring Brex")
	pIntBrex.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pIntBrex	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pIntBrex):
	debug(__name__ + ", AddCommonAnimations")
	pIntBrex.AddRandomAnimation("Bridge.Characters.IntSmallAnimations.ELookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	#pIntBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pIntBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	pIntBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pIntBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	#pIntBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	#pIntBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	#pIntBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.AtEase", App.CharacterClass.STANDING_ONLY)


###############################################################################
#	LoadSounds()
#
#	Load generic bridge sounds for this character
#
#	Args:	none
#
#	Return:	none
###############################################################################
def LoadSounds():
	debug(__name__ + ", LoadSounds")
	pGame = App.Game_GetCurrentGame()
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Crew General.tgl")

	#
	# Build a list of sound to load
	#
	kSoundList =	[	"BrexSir1",		# Click Response
						"BrexSir2",
						"BrexSir3",
						"BrexSir4",
						"BrexSir5",

						"BrexYes1",		# Order Confirmation
						"BrexYes2",
						"BrexYes3",
						"BrexYes4",

						"BrexTransfer",	# Transferring Power
						"MainPowerDraining",

						"FrontShieldDraining",
						"FrontShieldFailed",
						"RearShieldDraining",
						"RearShieldFailed",
						"TopShieldDraining",
						"TopShieldFailed",
						"BottomShieldDraining",
						"BottomShieldFailed",
						"LeftShieldDraining",
						"LeftShieldFailed",
						"RightShieldDraining",
						"RightShieldFailed",
						"PhasersDisabled",
						"PhasersDestroyed",
						"ShieldsDisabled",
						"ShieldsDestroyed",
						"SensorsDisabled",
						"SensorsDestroyed",
						"TorpedoesDisabled",
						"TorpedoesDestroyed",
						"TractorDisabled",
						"TractorDestroyed",
						"ImpulseDisabled",
						"ImpulseDestroyed",
						"WarpDisabled",
						"WarpDestroyed",
						"PowerDisabled",
						"OutOfTorpedoes",
						"Hull05",
						"Hull10",
						"Hull15",
						"Hull20",
						"Hull25",
						"Hull50",
						"Hull75",
						"MultipleShieldsOffline",
						"Shields05",
						"Shields10",
						"Shields15",
						"Shields20",
						"Shields25",
						"Shields50",
						"Shields75",
						"ShieldsFailed"
					]
	#
	# Loop through that list, loading each sound in the "BridgeGeneric" group
	#
	for i in range(len(kSoundList)):
		pGame.LoadDatabaseSoundInGroup(pDatabase, kSoundList[i], "BridgeGeneric")

	App.g_kLocalizationManager.Unload(pDatabase)

###############################################################################
#	MoveFromEToL1 & MoveFromL1ToE
#	
#	Functions that turn the "Contact Engineering" button on and off
#	
#	Args:	self		- the character that called these
#	
#	Return:	pSequence	- returned by the real functions
###############################################################################
def MoveFromEToL1(self):
	debug(__name__ + ", MoveFromEToL1")
	import Bridge.Characters.IntSmallAnimations
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Galaxy")

	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(Bridge.Characters.IntSmallAnimations.MoveFromEToL1(self))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "EnableContactEngineeringButton"), 15.0)
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEngineeringSet"), 0.1)
	pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "GalaxyEngSeated"))
	return pSequence

def MoveToEngineeringSet(pAction):
#	kDebugObj.Print("Moving Brex to the Engineering set")

	debug(__name__ + ", MoveToEngineeringSet")
	pBridge = App.g_kSetManager.GetSet("bridge")
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet()
	pIntBrex = pBridge.RemoveObjectFromSet("Engineer")
	assert pIntBrex
	bSuccess = pEngineering.AddObjectToSet(pIntBrex, "Engineer")
	assert bSuccess

#	kDebugObj.Print("Done in MoveToEngineeringSet()")

	return 0

def EnableContactEngineeringButton(pAction):
	debug(__name__ + ", EnableContactEngineeringButton")
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringEnabled(1)

	return 0
	
def MoveFromL1ToE(self):
	debug(__name__ + ", MoveFromL1ToE")
	import Bridge.Characters.IntSmallAnimations
	pSequence = App.TGSequence_Create()
	#pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "DBL1S"))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToDBridgeSet"))
	pSequence.AppendAction(Bridge.Characters.IntSmallAnimations.MoveFromL1ToE(self))
	return pSequence

def MoveToDBridgeSet(pAction):
	debug(__name__ + ", MoveToDBridgeSet")
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringEnabled(0)
	import Bridge.Characters.IntSmallAnimations

	pBridge = Bridge.BridgeUtils.GetBridge()
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Galaxy")
	pIntBrex = pEngineering.RemoveObjectFromSet("Engineer")
	assert pIntBrex
	bSuccess = pBridge.AddObjectToSet(pIntBrex, "Engineer")
	assert bSuccess

	return 0

def EBMoveFromEToL1(self):
	debug(__name__ + ", EBMoveFromEToL1")
	import Bridge.Characters.IntSmallAnimations
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Sovereign")
	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(Bridge.Characters.IntSmallAnimations.EBMoveFromEToL1(self))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "EnableContactEngineeringButton"), 5.0)
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEngineeringSet"), 0.1)
	pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "SovereignEngSeated"))
	return pSequence

def EBMoveFromL1ToE(self):
	debug(__name__ + ", EBMoveFromL1ToE")
	import Bridge.Characters.IntSmallAnimations
	pSequence = App.TGSequence_Create()
	#pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "EBL1S"))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEBridgeSet"))
	pSequence.AppendAction(Bridge.Characters.IntSmallAnimations.EBMoveFromL1ToE(self))
	return pSequence

def MoveToEBridgeSet(pAction):
	debug(__name__ + ", MoveToEBridgeSet")
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringEnabled(0)
	import Bridge.Characters.IntSmallAnimations

	pBridge = Bridge.BridgeUtils.GetBridge()
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Sovereign")
	pIntBrex = pEngineering.RemoveObjectFromSet("Engineer")
	assert pIntBrex
	bSuccess = pBridge.AddObjectToSet(pIntBrex, "Engineer")
	assert bSuccess

	return 0

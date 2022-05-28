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
	pDFBrex = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", CharacterPaths.g_pcHeadNIFPath + "HeadBrex/brex_head_no_mouth.nif")
	pDFBrex.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Brex/brex_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/brex_head.tga")

	pDFBrex.SetCharacterName("Brex")

	# Add the character to the set
	pSet.AddObjectToSet(pDFBrex, "Engineer")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pDFBrex)

	# Setup the character configuration
	pDFBrex.SetSize(App.CharacterClass.SMALL)
	pDFBrex.SetGender(App.CharacterClass.MALE)
	pDFBrex.SetRandomAnimationChance(.75)
	pDFBrex.SetBlinkChance(0.1)

	pDFBrex.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Engineering officer generic sounds
	LoadSounds()

	pDFBrex.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_blink1.tga")
	pDFBrex.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_blink2.tga")
	pDFBrex.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_eyes_close.tga")
	pDFBrex.SetBlinkStages(3)

	pDFBrex.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_head_a.tga")
	pDFBrex.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_head_e.tga")
	pDFBrex.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_head_u.tga")
	pDFBrex.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pDFBrex.GetDatabase(), "BrexNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pDFBrex.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Engineering")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	pDFBrex.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pDFBrex.SetLocation("")

#	kDebugObj.Print("Finished creating Brex")
	return pDFBrex


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
	pDFBrex = App.CharacterClass_Cast(pSet.GetObject("Engineer"))
	if (pDFBrex == None):
#		kDebugObj.Print("******* Engineering officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Engineer..")
	import Bridge.EngineerCharacterHandlers
	Bridge.EngineerCharacterHandlers.AttachMenuToEngineer(pDFBrex)

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
#	ConfigureForDefiant()
#
#	Configure ourselves for the Defiant bridge
#
#	Args:	pDFBrex	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForDefiant(pDFBrex):
#	kDebugObj.Print("Configuring Brex for the Defiant bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForDefiant")
	pDFBrex.ClearAnimations()

	# Register animation mappings
	pDFBrex.AddAnimation("SeatedDFEngineer", "Bridge.Characters.CommonAnimations.StandingConsole")
	pDFBrex.AddAnimation("EBL1SToE", "Bridge.Characters.Brex.EBMoveFromL1ToE")
	pDFBrex.AddAnimation("SovereignEngSeatedToE", "Bridge.Characters.Brex.EBMoveFromL1ToE")
	pDFBrex.AddAnimation("EBEngineerToL1", "Bridge.Characters.Brex.EBMoveFromEToL1")
	pDFBrex.AddAnimation("DFEngineerTurnCaptain", "Bridge.Characters.DFSmallAnimations.DFTurnAtETowardsCaptain")
	pDFBrex.AddAnimation("DFEngineerBackCaptain", "Bridge.Characters.DFSmallAnimations.DFTurnBackAtEFromCaptain")
	pDFBrex.AddAnimation("EBEngineer1ToE", "Bridge.Characters.DFSmallAnimations.EBMoveFromE1ToE")
	pDFBrex.AddAnimation("EBEngineerToE1", "Bridge.Characters.DFSmallAnimations.EBMoveFromEToE1")
	pDFBrex.AddAnimation("EBEngineer2ToE", "Bridge.Characters.DFSmallAnimations.EBMoveFromE2ToE")
	pDFBrex.AddAnimation("EBEngineerToE2", "Bridge.Characters.DFSmallAnimations.EBMoveFromEToE2")
	pDFBrex.AddAnimation("EBEngineer1ToE2", "Bridge.Characters.DFSmallAnimations.EBMoveFromE1ToE2")
	pDFBrex.AddAnimation("EBEngineer2ToE1", "Bridge.Characters.DFSmallAnimations.EBMoveFromE2ToE1")

	pDFBrex.AddAnimation("DFEngineerGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pDFBrex.AddAnimation("DFEngineerGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.StandingConsole")

	pDFBrex.AddAnimation("EBEngineerTurnC", "Bridge.Characters.DFSmallAnimations.EBETalkC")
	pDFBrex.AddAnimation("EBEngineerBackC", "Bridge.Characters.CommonAnimations.StandingConsole")
	pDFBrex.AddAnimation("EBEngineerTurnH", "Bridge.Characters.DFSmallAnimations.EBETalkH")
	pDFBrex.AddAnimation("EBEngineerBackH", "Bridge.Characters.CommonAnimations.StandingConsole")
	pDFBrex.AddAnimation("EBEngineerTurnS", "Bridge.Characters.DFSmallAnimations.EBETalkS")
	pDFBrex.AddAnimation("EBEngineerBackS", "Bridge.Characters.CommonAnimations.StandingConsole")
	pDFBrex.AddAnimation("EBEngineerTurnT", "Bridge.Characters.DFSmallAnimations.EBETalkT")
	pDFBrex.AddAnimation("EBEngineerBackT", "Bridge.Characters.CommonAnimations.StandingConsole")

	pDFBrex.AddAnimation("DFEngineerTurnX", "Bridge.Characters.DFSmallAnimations.DFTurnAtETowardsCaptain")
	pDFBrex.AddAnimation("DFEngineerBackX", "Bridge.Characters.DFSmallAnimations.DFTurnBackAtEFromCaptain")

	# Breathing
	pDFBrex.AddAnimation("EBEngineerBreathe", "Bridge.Characters.CommonAnimations.StandingConsole")
	pDFBrex.AddAnimation("EBEngineerBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pDFBrex.AddRandomAnimation("Bridge.Characters.DFSmallAnimations.DFEConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pDFBrex.AddAnimation("PushingButtons", "Bridge.Characters.DFSmallAnimations.DFEConsoleInteraction")

	# Hit animations
	pDFBrex.AddAnimation("DFEngineerHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pDFBrex.AddAnimation("DFEngineerHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pDFBrex.AddAnimation("DFEngineerReactLeftStanding", "Bridge.Characters.CommonAnimations.ReactLeft");
	pDFBrex.AddAnimation("DFEngineerReactRightStanding", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	AddCommonAnimations(pDFBrex)

	# Brex sits on the DF bridge
	pDFBrex.SetStanding(0)
	pDFBrex.SetLocation("DFEngineer")
	pDFBrex.AddPositionZoom("DFEngineer", 0.55)
	pDFBrex.AddPositionZoom("DFEngineer1", 0.55)
	pDFBrex.AddPositionZoom("DFEngineer2", 0.55)
#	kDebugObj.Print("Finished configuring Brex")
	pDFBrex.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pDFBrex	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pDFBrex):
	debug(__name__ + ", AddCommonAnimations")
	pDFBrex.AddRandomAnimation("Bridge.Characters.DFSmallAnimations.ELookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	#pDFBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pDFBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	pDFBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pDFBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pDFBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pDFBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	#pDFBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.AtEase", App.CharacterClass.STANDING_ONLY)


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
	import Bridge.Characters.DFSmallAnimations
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Galaxy")

	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(Bridge.Characters.DFSmallAnimations.MoveFromEToL1(self))
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
	pDFBrex = pBridge.RemoveObjectFromSet("Engineer")
	assert pDFBrex
	bSuccess = pEngineering.AddObjectToSet(pDFBrex, "Engineer")
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
	import Bridge.Characters.DFSmallAnimations
	pSequence = App.TGSequence_Create()
	#pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "DBL1S"))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToDBridgeSet"))
	pSequence.AppendAction(Bridge.Characters.DFSmallAnimations.MoveFromL1ToE(self))
	return pSequence

def MoveToDBridgeSet(pAction):
	debug(__name__ + ", MoveToDBridgeSet")
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringEnabled(0)
	import Bridge.Characters.DFSmallAnimations

	pBridge = Bridge.BridgeUtils.GetBridge()
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Galaxy")
	pDFBrex = pEngineering.RemoveObjectFromSet("Engineer")
	assert pDFBrex
	bSuccess = pBridge.AddObjectToSet(pDFBrex, "Engineer")
	assert bSuccess

	return 0

def EBMoveFromEToL1(self):
	debug(__name__ + ", EBMoveFromEToL1")
	import Bridge.Characters.DFSmallAnimations
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Sovereign")
	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(Bridge.Characters.DFSmallAnimations.EBMoveFromEToL1(self))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "EnableContactEngineeringButton"), 5.0)
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEngineeringSet"), 0.1)
	pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "SovereignEngSeated"))
	return pSequence

def EBMoveFromL1ToE(self):
	debug(__name__ + ", EBMoveFromL1ToE")
	import Bridge.Characters.DFSmallAnimations
	pSequence = App.TGSequence_Create()
	#pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "EBL1S"))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEBridgeSet"))
	pSequence.AppendAction(Bridge.Characters.DFSmallAnimations.EBMoveFromL1ToE(self))
	return pSequence

def MoveToEBridgeSet(pAction):
	debug(__name__ + ", MoveToEBridgeSet")
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringEnabled(0)
	import Bridge.Characters.DFSmallAnimations

	pBridge = Bridge.BridgeUtils.GetBridge()
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Sovereign")
	pDFBrex = pEngineering.RemoveObjectFromSet("Engineer")
	assert pDFBrex
	bSuccess = pBridge.AddObjectToSet(pDFBrex, "Engineer")
	assert bSuccess

	return 0

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
#	ConfigureForAmbassador()
#
#	Configure ourselves for the Ambassador bridge
#
#	Args:	pDFBrex	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForAmbassador(pAmbBrex):
#	kDebugObj.Print("Configuring Brex for the Ambassador bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForAmbassador")
	pAmbBrex.ClearAnimations()

	# Register animation mappings
	pAmbBrex.AddAnimation("SeatedAmbEngineer", "Bridge.Characters.AmbSmallAnimations.Amb_stand_e")
	pAmbBrex.AddAnimation("EBL1SToE", "Bridge.Characters.Brex.EBMoveFromL1ToE")
	pAmbBrex.AddAnimation("SovereignEngSeatedToE", "Bridge.Characters.Brex.EBMoveFromL1ToE")
	pAmbBrex.AddAnimation("EBEngineerToL1", "Bridge.Characters.Brex.EBMoveFromEToL1")
	pAmbBrex.AddAnimation("AmbEngineerTurnCaptain", "Bridge.Characters.AmbSmallAnimations.AmbTurnAtETowardsCaptain")
	pAmbBrex.AddAnimation("AmbEngineerBackCaptain", "Bridge.Characters.AmbSmallAnimations.AmbTurnBackAtEFromCaptain")
	pAmbBrex.AddAnimation("EBEngineer1ToE", "Bridge.Characters.AmbSmallAnimations.EBMoveFromE1ToE")
	pAmbBrex.AddAnimation("EBEngineerToE1", "Bridge.Characters.AmbSmallAnimations.EBMoveFromEToE1")
	pAmbBrex.AddAnimation("EBEngineer2ToE", "Bridge.Characters.AmbSmallAnimations.EBMoveFromE2ToE")
	pAmbBrex.AddAnimation("EBEngineerToE2", "Bridge.Characters.AmbSmallAnimations.EBMoveFromEToE2")
	pAmbBrex.AddAnimation("EBEngineer1ToE2", "Bridge.Characters.AmbSmallAnimations.EBMoveFromE1ToE2")
	pAmbBrex.AddAnimation("EBEngineer2ToE1", "Bridge.Characters.AmbSmallAnimations.EBMoveFromE2ToE1")

	pAmbBrex.AddAnimation("AmbEngineerGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pAmbBrex.AddAnimation("AmbEngineerGlanceAwayCaptain", "Bridge.Characters.AmbSmallAnimations.AmbEConsoleInteraction")

	pAmbBrex.AddAnimation("EBEngineerTurnC", "Bridge.Characters.AmbSmallAnimations.EBETalkC")
	pAmbBrex.AddAnimation("EBEngineerBackC", "Bridge.Characters.AmbSmallAnimations.Amb_stand_e")
	pAmbBrex.AddAnimation("EBEngineerTurnH", "Bridge.Characters.AmbSmallAnimations.EBETalkH")
	pAmbBrex.AddAnimation("EBEngineerBackH", "Bridge.Characters.AmbSmallAnimations.Amb_stand_e")
	pAmbBrex.AddAnimation("EBEngineerTurnS", "Bridge.Characters.AmbSmallAnimations.EBETalkS")
	pAmbBrex.AddAnimation("EBEngineerBackS", "Bridge.Characters.AmbSmallAnimations.Amb_stand_e")
	pAmbBrex.AddAnimation("EBEngineerTurnT", "Bridge.Characters.AmbSmallAnimations.EBETalkT")
	pAmbBrex.AddAnimation("EBEngineerBackT", "Bridge.Characters.AmbSmallAnimations.Amb_stand_e")

	pAmbBrex.AddAnimation("AmbEngineerTurnX", "Bridge.Characters.AmbSmallAnimations.AmbTurnAtETowardsCaptain")
	pAmbBrex.AddAnimation("AmbEngineerBackX", "Bridge.Characters.AmbSmallAnimations.AmbTurnBackAtEFromCaptain")

	# Breathing
	pAmbBrex.AddAnimation("EBEngineerBreathe", "Bridge.Characters.AmbSmallAnimations.Amb_stand_e")
	pAmbBrex.AddAnimation("EBEngineerBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pAmbBrex.AddRandomAnimation("Bridge.Characters.AmbSmallAnimations.AmbEConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pAmbBrex.AddAnimation("PushingButtons", "Bridge.Characters.AmbSmallAnimations.AmbEConsoleInteraction")

	# Hit animations
	pAmbBrex.AddAnimation("AmbEngineerHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pAmbBrex.AddAnimation("AmbEngineerHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pAmbBrex.AddAnimation("AmbEngineerReactLeftStanding", "Bridge.Characters.CommonAnimations.ReactLeft");
	pAmbBrex.AddAnimation("AmbEngineerReactRightStanding", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	AddCommonAnimations(pAmbBrex)

	# Brex stands on the Amb bridge
	pAmbBrex.SetStanding(1)
	pAmbBrex.SetLocation("AmbEngineer")
	pAmbBrex.AddPositionZoom("AmbEngineer", 0.9)
	pAmbBrex.AddPositionZoom("AmbEngineer1", 0.9)
	pAmbBrex.AddPositionZoom("AmbEngineer2", 0.9)
#	kDebugObj.Print("Finished configuring Brex")
	pAmbBrex.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pAmbBrex	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pAmbBrex):
	debug(__name__ + ", AddCommonAnimations")
	pAmbBrex.AddRandomAnimation("Bridge.Characters.AmbSmallAnimations.ELookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	#pAmbBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pAmbBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	pAmbBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pAmbBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pAmbBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pAmbBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	#pAmbBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.AtEase", App.CharacterClass.STANDING_ONLY)


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
	import Bridge.Characters.AmbSmallAnimations
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Galaxy")

	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(Bridge.Characters.AmbSmallAnimations.MoveFromEToL1(self))
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
	pAmbBrex = pBridge.RemoveObjectFromSet("Engineer")
	assert pAmbBrex
	bSuccess = pEngineering.AddObjectToSet(pAmbBrex, "Engineer")
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
	import Bridge.Characters.AmbSmallAnimations
	pSequence = App.TGSequence_Create()
	#pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "DBL1S"))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToDBridgeSet"))
	pSequence.AppendAction(Bridge.Characters.AmbSmallAnimations.MoveFromL1ToE(self))
	return pSequence

def MoveToDBridgeSet(pAction):
	debug(__name__ + ", MoveToDBridgeSet")
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringEnabled(0)
	import Bridge.Characters.AmbSmallAnimations

	pBridge = Bridge.BridgeUtils.GetBridge()
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Galaxy")
	pAmbBrex = pEngineering.RemoveObjectFromSet("Engineer")
	assert pAmbBrex
	bSuccess = pBridge.AddObjectToSet(pAmbBrex, "Engineer")
	assert bSuccess

	return 0

def EBMoveFromEToL1(self):
	debug(__name__ + ", EBMoveFromEToL1")
	import Bridge.Characters.AmbSmallAnimations
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Sovereign")
	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(Bridge.Characters.AmbSmallAnimations.EBMoveFromEToL1(self))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "EnableContactEngineeringButton"), 5.0)
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEngineeringSet"), 0.1)
	pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "SovereignEngSeated"))
	return pSequence

def EBMoveFromL1ToE(self):
	debug(__name__ + ", EBMoveFromL1ToE")
	import Bridge.Characters.AmbSmallAnimations
	pSequence = App.TGSequence_Create()
	#pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "EBL1S"))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEBridgeSet"))
	pSequence.AppendAction(Bridge.Characters.AmbSmallAnimations.EBMoveFromL1ToE(self))
	return pSequence

def MoveToEBridgeSet(pAction):
	debug(__name__ + ", MoveToEBridgeSet")
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringEnabled(0)
	import Bridge.Characters.AmbSmallAnimations

	pBridge = Bridge.BridgeUtils.GetBridge()
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Sovereign")
	pAmbBrex = pEngineering.RemoveObjectFromSet("Engineer")
	assert pAmbBrex
	bSuccess = pBridge.AddObjectToSet(pAmbBrex, "Engineer")
	assert bSuccess

	return 0

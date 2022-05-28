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
	pNebBrex = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", CharacterPaths.g_pcHeadNIFPath + "HeadBrex/brex_head_no_mouth.nif")
	pNebBrex.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadBrex/brex_head.tga")

	pNebBrex.SetCharacterName("NebBrex")

	# Add the character to the set
	pSet.AddObjectToSet(pNebBrex, "Engineer")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pNebBrex)

	# Setup the character configuration
	pNebBrex.SetSize(App.CharacterClass.SMALL)
	pNebBrex.SetGender(App.CharacterClass.MALE)
	pNebBrex.SetRandomAnimationChance(.75)
	pNebBrex.SetBlinkChance(0.1)

	pNebBrex.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Engineering officer generic sounds
	LoadSounds()

	pNebBrex.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "HeadBrex/Brex_blink1.tga")
	pNebBrex.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "HeadBrex/Brex_blink2.tga")
	pNebBrex.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "HeadBrex/Brex_eyes_close.tga")
	pNebBrex.SetBlinkStages(3)

	pNebBrex.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "HeadBrex/Brex_head_a.tga")
	pNebBrex.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "HeadBrex/Brex_head_e.tga")
	pNebBrex.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "HeadBrex/Brex_head_u.tga")
	pNebBrex.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pNebBrex.GetDatabase(), "BrexNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pNebBrex.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Engineering")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	pNebBrex.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pNebBrex.SetLocation("")

#	kDebugObj.Print("Finished creating Brex")
	return pNebBrex


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
	pNebBrex = App.CharacterClass_Cast(pSet.GetObject("Engineer"))
	if (pNebBrex == None):
#		kDebugObj.Print("******* Engineering officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Engineer..")
	import Bridge.EngineerCharacterHandlers
	Bridge.EngineerCharacterHandlers.AttachMenuToEngineer(pNebBrex)

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
#	ConfigureForNebula()
#
#	Configure ourselves for the Nebula bridge
#
#	Args:	pNebBrex	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForNebula(pNebBrex):
#	kDebugObj.Print("Configuring Brex for the Sovereign bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForNebula")
	pNebBrex.ClearAnimations()

	# Register animation mappings
	pNebBrex.AddAnimation("SeatedNebEngineer", "Bridge.Characters.CommonAnimations.SeatedS")
	pNebBrex.AddAnimation("EBL1SToE", "Bridge.Characters.Brex.EBMoveFromL1ToE")
	pNebBrex.AddAnimation("SovereignEngSeatedToE", "Bridge.Characters.Brex.EBMoveFromL1ToE")
	pNebBrex.AddAnimation("EBEngineerToL1", "Bridge.Characters.Brex.EBMoveFromEToL1")
	pNebBrex.AddAnimation("NebEngineerTurnCaptain", "Bridge.Characters.NebSmallAnimations.NebTurnAtETowardsCaptain")
	pNebBrex.AddAnimation("NebEngineerBackCaptain", "Bridge.Characters.NebSmallAnimations.NebTurnBackAtEFromCaptain")
	pNebBrex.AddAnimation("NEbEngineer1ToE", "Bridge.Characters.NebSmallAnimations.EBMoveFromE1ToE")
	pNebBrex.AddAnimation("NEbEngineerToE1", "Bridge.Characters.NebSmallAnimations.EBMoveFromEToE1")
	pNebBrex.AddAnimation("NebEngineer2ToE", "Bridge.Characters.NebSmallAnimations.EBMoveFromE2ToE")
	pNebBrex.AddAnimation("NebEngineerToE2", "Bridge.Characters.NebSmallAnimations.EBMoveFromEToE2")
	pNebBrex.AddAnimation("NEbEngineer1ToE2", "Bridge.Characters.NebSmallAnimations.EBMoveFromE1ToE2")
	pNebBrex.AddAnimation("NebEngineer2ToE1", "Bridge.Characters.NebSmallAnimations.EBMoveFromE2ToE1")

	pNebBrex.AddAnimation("NebEngineerGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pNebBrex.AddAnimation("NebEngineerGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedS")

	pNebBrex.AddAnimation("NebEngineerTurnC", "Bridge.Characters.NebSmallAnimations.EBETalkC")
	pNebBrex.AddAnimation("NebEngineerBackC", "Bridge.Characters.CommonAnimations.SeatedS")
	pNebBrex.AddAnimation("EBEngineerTurnH", "Bridge.Characters.NebSmallAnimations.EBETalkH")
	pNebBrex.AddAnimation("EBEngineerBackH", "Bridge.Characters.CommonAnimations.SeatedS")
	pNebBrex.AddAnimation("EBEngineerTurnS", "Bridge.Characters.NebSmallAnimations.EBETalkS")
	pNebBrex.AddAnimation("EBEngineerBackS", "Bridge.Characters.CommonAnimations.SeatedS")
	pNebBrex.AddAnimation("EBEngineerTurnT", "Bridge.Characters.NebSmallAnimations.EBETalkT")
	pNebBrex.AddAnimation("EBEngineerBackT", "Bridge.Characters.CommonAnimations.SeatedS")

	pNebBrex.AddAnimation("NebEngineerTurnX", "Bridge.Characters.NebSmallAnimations.NebTurnAtETowardsCaptain")
	pNebBrex.AddAnimation("NebEngineerBackX", "Bridge.Characters.NebSmallAnimations.NebTurnBackAtEFromCaptain")

	# Breathing
	pNebBrex.AddAnimation("NebEngineerBreathe", "Bridge.Characters.CommonAnimations.SeatedS")
	pNebBrex.AddAnimation("NebEngineerBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pNebBrex.AddRandomAnimation("Bridge.Characters.NebSmallAnimations.NebEConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pNebBrex.AddAnimation("PushingButtons", "Bridge.Characters.NebSmallAnimations.NebEConsoleInteraction")

	# Hit animations
	pNebBrex.AddAnimation("NebEngineerHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pNebBrex.AddAnimation("NebEngineerHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pNebBrex.AddAnimation("NebEngineerReactLeftStanding", "Bridge.Characters.CommonAnimations.ReactLeft");
	pNebBrex.AddAnimation("NebEngineerReactRightStanding", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	AddCommonAnimations(pNebBrex)

	# Brex sits on the Nebula bridge
	pNebBrex.SetStanding(0)
	pNebBrex.SetLocation("NebEngineer")
	pNebBrex.AddPositionZoom("NebEngineer", 0.7)
	pNebBrex.AddPositionZoom("NebEngineer1", 0.7)
	pNebBrex.AddPositionZoom("NebEngineer2", 0.8)
#	kDebugObj.Print("Finished configuring Brex")
	pNebBrex.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pNebBrex	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pNebBrex):
	debug(__name__ + ", AddCommonAnimations")
	pNebBrex.AddRandomAnimation("Bridge.Characters.NebSmallAnimations.ELookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	#pNebBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pNebBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	pNebBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pNebBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pNebBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pNebBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	#pNebBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.AtEase", App.CharacterClass.STANDING_ONLY)


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
	import Bridge.Characters.NebSmallAnimations
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Galaxy")

	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(Bridge.Characters.NebSmallAnimations.MoveFromEToL1(self))
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
	pNebBrex = pBridge.RemoveObjectFromSet("Engineer")
	assert pNebBrex
	bSuccess = pEngineering.AddObjectToSet(pNebBrex, "Engineer")
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
	import Bridge.Characters.NebSmallAnimations
	pSequence = App.TGSequence_Create()
	#pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "DBL1S"))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToDBridgeSet"))
	pSequence.AppendAction(Bridge.Characters.NebSmallAnimations.MoveFromL1ToE(self))
	return pSequence

def MoveToDBridgeSet(pAction):
	debug(__name__ + ", MoveToDBridgeSet")
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringEnabled(0)
	import Bridge.Characters.NebSmallAnimations

	pBridge = Bridge.BridgeUtils.GetBridge()
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Galaxy")
	pNebBrex = pEngineering.RemoveObjectFromSet("Engineer")
	assert pNebBrex
	bSuccess = pBridge.AddObjectToSet(pNebBrex, "Engineer")
	assert bSuccess

	return 0

def EBMoveFromEToL1(self):
	debug(__name__ + ", EBMoveFromEToL1")
	import Bridge.Characters.NebSmallAnimations
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Sovereign")
	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(Bridge.Characters.NebSmallAnimations.EBMoveFromEToL1(self))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "EnableContactEngineeringButton"), 5.0)
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEngineeringSet"), 0.1)
	pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "SovereignEngSeated"))
	return pSequence

def EBMoveFromL1ToE(self):
	debug(__name__ + ", EBMoveFromL1ToE")
	import Bridge.Characters.NebSmallAnimations
	pSequence = App.TGSequence_Create()
	#pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "EBL1S"))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEBridgeSet"))
	pSequence.AppendAction(Bridge.Characters.NebSmallAnimations.EBMoveFromL1ToE(self))
	return pSequence

def MoveToEBridgeSet(pAction):
	debug(__name__ + ", MoveToEBridgeSet")
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringEnabled(0)
	import Bridge.Characters.NebSmallAnimations

	pBridge = Bridge.BridgeUtils.GetBridge()
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Sovereign")
	pNebBrex = pEngineering.RemoveObjectFromSet("Engineer")
	assert pNebBrex
	bSuccess = pBridge.AddObjectToSet(pNebBrex, "Engineer")
	assert bSuccess

	return 0

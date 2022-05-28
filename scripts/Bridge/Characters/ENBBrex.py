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
	pENBBrex = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", CharacterPaths.g_pcHeadNIFPath + "HeadBrex/brex_head_no_mouth.nif")
	pENBBrex.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Brex/brex_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/brex_head.tga")

	pENBBrex.SetCharacterName("Brex")

	# Add the character to the set
	pSet.AddObjectToSet(pENBBrex, "Engineer")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pENBBrex)

	# Setup the character configuration
	pENBBrex.SetSize(App.CharacterClass.SMALL)
	pENBBrex.SetGender(App.CharacterClass.MALE)
	pENBBrex.SetRandomAnimationChance(.75)
	pENBBrex.SetBlinkChance(0.1)

	pENBBrex.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Engineering officer generic sounds
	LoadSounds()

	pENBBrex.AddfacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_blink1.tga")
	pENBBrex.AddfacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_blink2.tga")
	pENBBrex.AddfacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_eyes_close.tga")
	pENBBrex.SetBlinkStages(3)

	pENBBrex.AddfacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_head_a.tga")
	pENBBrex.AddfacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_head_e.tga")
	pENBBrex.AddfacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_head_u.tga")
	pENBBrex.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pENBBrex.GetDatabase(), "BrexNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pENBBrex.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Engineering")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	pENBBrex.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pENBBrex.SetLocation("")

#	kDebugObj.Print("Finished creating Brex")
	return pENBBrex


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
	pENBBrex = App.CharacterClass_Cast(pSet.GetObject("Engineer"))
	if (pENBBrex == None):
#		kDebugObj.Print("******* Engineering officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Engineer..")
	import Bridge.EngineerCharacterHandlers
	Bridge.EngineerCharacterHandlers.AttachMenuToEngineer(pENBBrex)

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
#	ConfigureForEnterpriseB()
#
#	Configure ourselves for the EnterpriseB bridge
#
#	Args:	pENBBrex	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForEnterpriseB(pENBBrex):
#	kDebugObj.Print("Configuring Brex for the EnterpriseB bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForEnterpriseB")
	pENBBrex.ClearAnimations()

	# Register animation mappings
	pENBBrex.AddAnimation("SeatedENBEngineer", "Bridge.Characters.CommonAnimations.StandingConsole")
	pENBBrex.AddAnimation("EBL1SToE", "Bridge.Characters.Brex.EBMoveFromL1ToE")
	pENBBrex.AddAnimation("SovereignEngSeatedToE", "Bridge.Characters.Brex.EBMoveFromL1ToE")
	pENBBrex.AddAnimation("EBEngineerToL1", "Bridge.Characters.Brex.EBMoveFromEToL1")
	pENBBrex.AddAnimation("ENBEngineerTurnCaptain", "Bridge.Characters.ENBSmallAnimations.ENBTurnAtETowardsCaptain")
	pENBBrex.AddAnimation("ENBEngineerBackCaptain", "Bridge.Characters.ENBSmallAnimations.ENBTurnBackAtEFromCaptain")
	pENBBrex.AddAnimation("EBEngineer1ToE", "Bridge.Characters.ENBSmallAnimations.EBMoveFromE1ToE")
	pENBBrex.AddAnimation("EBEngineerToE1", "Bridge.Characters.ENBSmallAnimations.EBMoveFromEToE1")
	pENBBrex.AddAnimation("EBEngineer2ToE", "Bridge.Characters.ENBSmallAnimations.EBMoveFromE2ToE")
	pENBBrex.AddAnimation("EBEngineerToE2", "Bridge.Characters.ENBSmallAnimations.EBMoveFromEToE2")
	pENBBrex.AddAnimation("EBEngineer1ToE2", "Bridge.Characters.ENBSmallAnimations.EBMoveFromE1ToE2")
	pENBBrex.AddAnimation("EBEngineer2ToE1", "Bridge.Characters.ENBSmallAnimations.EBMoveFromE2ToE1")

	pENBBrex.AddAnimation("ENBEngineerGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pENBBrex.AddAnimation("ENBEngineerGlanceAwayCaptain", "Bridge.Characters.ENBSmallAnimations.ENBEConsoleInteraction")

	pENBBrex.AddAnimation("EBEngineerTurnC", "Bridge.Characters.ENBSmallAnimations.EBETalkC")
	pENBBrex.AddAnimation("EBEngineerBackC", "Bridge.Characters.CommonAnimations.StandingConsole")
	pENBBrex.AddAnimation("EBEngineerTurnH", "Bridge.Characters.ENBSmallAnimations.EBETalkH")
	pENBBrex.AddAnimation("EBEngineerBackH", "Bridge.Characters.CommonAnimations.StandingConsole")
	pENBBrex.AddAnimation("EBEngineerTurnS", "Bridge.Characters.ENBSmallAnimations.EBETalkS")
	pENBBrex.AddAnimation("EBEngineerBackS", "Bridge.Characters.CommonAnimations.StandingConsole")
	pENBBrex.AddAnimation("EBEngineerTurnT", "Bridge.Characters.ENBSmallAnimations.EBETalkT")
	pENBBrex.AddAnimation("EBEngineerBackT", "Bridge.Characters.CommonAnimations.StandingConsole")

	pENBBrex.AddAnimation("ENBEngineerTurnX", "Bridge.Characters.ENBSmallAnimations.ENBTurnAtETowardsCaptain")
	pENBBrex.AddAnimation("ENBEngineerBackX", "Bridge.Characters.ENBSmallAnimations.ENBTurnBackAtEFromCaptain")

	# Breathing
	pENBBrex.AddAnimation("EBEngineerBreathe", "Bridge.Characters.CommonAnimations.StandingConsole")
	pENBBrex.AddAnimation("EBEngineerBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pENBBrex.AddRandomAnimation("Bridge.Characters.ENBSmallAnimations.ENBEConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pENBBrex.AddAnimation("PushingButtons", "Bridge.Characters.ENBSmallAnimations.ENBEConsoleInteraction")

	# Hit animations
	pENBBrex.AddAnimation("ENBEngineerHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pENBBrex.AddAnimation("ENBEngineerHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pENBBrex.AddAnimation("ENBEngineerReactLeftStanding", "Bridge.Characters.CommonAnimations.ReactLeft");
	pENBBrex.AddAnimation("ENBEngineerReactRightStanding", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	AddCommonAnimations(pENBBrex)

	# Brex sits on the ENB bridge
	pENBBrex.SetStanding(0)
	pENBBrex.SetLocation("ENBEngineer")
	pENBBrex.AddPositionZoom("ENBEngineer", 0.4)
	pENBBrex.AddPositionZoom("ENBEngineer1", 0.4)
	pENBBrex.AddPositionZoom("ENBEngineer2", 0.4)
#	kDebugObj.Print("Finished configuring Brex")
	pENBBrex.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pENBBrex	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pENBBrex):
	debug(__name__ + ", AddCommonAnimations")
	pENBBrex.AddRandomAnimation("Bridge.Characters.ENBSmallAnimations.ELookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	#pENBBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pENBBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	pENBBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pENBBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pENBBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pENBBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	#pENBBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.AtEase", App.CharacterClass.STANDING_ONLY)


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
						"FrontShieldfailed",
						"RearShieldDraining",
						"RearShieldfailed",
						"TopShieldDraining",
						"TopShieldfailed",
						"BottomShieldDraining",
						"BottomShieldfailed",
						"LeftShieldDraining",
						"LeftShieldfailed",
						"RightShieldDraining",
						"RightShieldfailed",
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
	import Bridge.Characters.ENBSmallAnimations
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Galaxy")

	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(Bridge.Characters.ENBSmallAnimations.MoveFromEToL1(self))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "enableContactEngineeringButton"), 15.0)
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEngineeringSet"), 0.1)
	pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "GalaxyEngSeated"))
	return pSequence

def MoveToEngineeringSet(pAction):
#	kDebugObj.Print("Moving Brex to the Engineering set")

	debug(__name__ + ", MoveToEngineeringSet")
	pBridge = App.g_kSetManager.GetSet("bridge")
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet()
	pENBBrex = pBridge.RemoveObjectFromSet("Engineer")
	assert pENBBrex
	bSuccess = pEngineering.AddObjectToSet(pENBBrex, "Engineer")
	assert bSuccess

#	kDebugObj.Print("Done in MoveToEngineeringSet()")

	return 0

def enableContactEngineeringButton(pAction):
	debug(__name__ + ", enableContactEngineeringButton")
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringenabled(1)

	return 0
	
def MoveFromL1ToE(self):
	debug(__name__ + ", MoveFromL1ToE")
	import Bridge.Characters.ENBSmallAnimations
	pSequence = App.TGSequence_Create()
	#pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "DBL1S"))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToDBridgeSet"))
	pSequence.AppendAction(Bridge.Characters.ENBSmallAnimations.MoveFromL1ToE(self))
	return pSequence

def MoveToDBridgeSet(pAction):
	debug(__name__ + ", MoveToDBridgeSet")
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringenabled(0)
	import Bridge.Characters.ENBSmallAnimations

	pBridge = Bridge.BridgeUtils.GetBridge()
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Galaxy")
	pENBBrex = pEngineering.RemoveObjectFromSet("Engineer")
	assert pENBBrex
	bSuccess = pBridge.AddObjectToSet(pENBBrex, "Engineer")
	assert bSuccess

	return 0

def EBMoveFromEToL1(self):
	debug(__name__ + ", EBMoveFromEToL1")
	import Bridge.Characters.ENBSmallAnimations
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Sovereign")
	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(Bridge.Characters.ENBSmallAnimations.EBMoveFromEToL1(self))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "enableContactEngineeringButton"), 5.0)
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEngineeringSet"), 0.1)
	pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "SovereignEngSeated"))
	return pSequence

def EBMoveFromL1ToE(self):
	debug(__name__ + ", EBMoveFromL1ToE")
	import Bridge.Characters.ENBSmallAnimations
	pSequence = App.TGSequence_Create()
	#pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "EBL1S"))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEBridgeSet"))
	pSequence.AppendAction(Bridge.Characters.ENBSmallAnimations.EBMoveFromL1ToE(self))
	return pSequence

def MoveToEBridgeSet(pAction):
	debug(__name__ + ", MoveToEBridgeSet")
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringenabled(0)
	import Bridge.Characters.ENBSmallAnimations

	pBridge = Bridge.BridgeUtils.GetBridge()
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Sovereign")
	pENBBrex = pEngineering.RemoveObjectFromSet("Engineer")
	assert pENBBrex
	bSuccess = pBridge.AddObjectToSet(pENBBrex, "Engineer")
	assert bSuccess

	return 0

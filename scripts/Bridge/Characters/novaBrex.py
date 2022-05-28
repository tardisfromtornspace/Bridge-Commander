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

	if (pSet.GetObject("Engineer") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Engineer")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadBrex/brex_head_no_mouth.nif", None)
	pnovaBrex = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", CharacterPaths.g_pcHeadNIFPath + "HeadBrex/brex_head_no_mouth.nif")
	pnovaBrex.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Brex/brex_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/brex_head.tga")

	pnovaBrex.SetCharacterName("Brex")

	# Add the character to the set
	pSet.AddObjectToSet(pnovaBrex, "Engineer")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pnovaBrex)

	# Setup the character configuration
	pnovaBrex.SetSize(App.CharacterClass.SMALL)
	pnovaBrex.SetGender(App.CharacterClass.MALE)
	pnovaBrex.SetRandomAnimationChance(.75)
	pnovaBrex.SetBlinkChance(0.1)

	pnovaBrex.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Engineering officer generic sounds
	LoadSounds()

	pnovaBrex.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_blink1.tga")
	pnovaBrex.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_blink2.tga")
	pnovaBrex.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_eyes_close.tga")
	pnovaBrex.SetBlinkStages(3)

	pnovaBrex.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_head_a.tga")
	pnovaBrex.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_head_e.tga")
	pnovaBrex.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_head_u.tga")
	pnovaBrex.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pnovaBrex.GetDatabase(), "BrexNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pnovaBrex.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Engineering")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	pnovaBrex.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pnovaBrex.SetLocation("")

#	kDebugObj.Print("Finished creating Brex")
	return pnovaBrex


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
	pnovaBrex = App.CharacterClass_Cast(pSet.GetObject("Engineer"))
	if (pnovaBrex == None):
#		kDebugObj.Print("******* Engineering officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Engineer..")
	import Bridge.EngineerCharacterHandlers
	Bridge.EngineerCharacterHandlers.AttachMenuToEngineer(pnovaBrex)

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
#	ConfigureForPrometheus()
#
#	Configure ourselves for the novaetheus bridge
#
#	Args:	pnovaBrex	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForPrometheus(pnovaBrex):
#	kDebugObj.Print("Configuring Brex for the novaetheus bridge")

	# Clear out any old animations from another configuration
	pnovaBrex.ClearAnimations()

	# Register animation mappings
	pnovaBrex.AddAnimation("SeatednovaEngineer", "Bridge.Characters.CommonAnimations.StandingConsole")
	pnovaBrex.AddAnimation("EBL1SToE", "Bridge.Characters.Brex.EBMoveFromL1ToE")
	pnovaBrex.AddAnimation("SovereignEngSeatedToE", "Bridge.Characters.Brex.EBMoveFromL1ToE")
	pnovaBrex.AddAnimation("EBEngineerToL1", "Bridge.Characters.Brex.EBMoveFromEToL1")
	pnovaBrex.AddAnimation("novaEngineerTurnCaptain", "Bridge.Characters.novaSmallAnimations.novaTurnAtETowardsCaptain")
	pnovaBrex.AddAnimation("novaEngineerBackCaptain", "Bridge.Characters.novaSmallAnimations.novaTurnBackAtEFromCaptain")
	pnovaBrex.AddAnimation("EBEngineer1ToE", "Bridge.Characters.novaSmallAnimations.EBMoveFromE1ToE")
	pnovaBrex.AddAnimation("EBEngineerToE1", "Bridge.Characters.novaSmallAnimations.EBMoveFromEToE1")
	pnovaBrex.AddAnimation("EBEngineer2ToE", "Bridge.Characters.novaSmallAnimations.EBMoveFromE2ToE")
	pnovaBrex.AddAnimation("EBEngineerToE2", "Bridge.Characters.novaSmallAnimations.EBMoveFromEToE2")
	pnovaBrex.AddAnimation("EBEngineer1ToE2", "Bridge.Characters.novaSmallAnimations.EBMoveFromE1ToE2")
	pnovaBrex.AddAnimation("EBEngineer2ToE1", "Bridge.Characters.novaSmallAnimations.EBMoveFromE2ToE1")

	pnovaBrex.AddAnimation("novaEngineerGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pnovaBrex.AddAnimation("novaEngineerGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.StandingConsole")

	pnovaBrex.AddAnimation("EBEngineerTurnC", "Bridge.Characters.novaSmallAnimations.EBETalkC")
	pnovaBrex.AddAnimation("EBEngineerBackC", "Bridge.Characters.CommonAnimations.StandingConsole")
	pnovaBrex.AddAnimation("EBEngineerTurnH", "Bridge.Characters.novaSmallAnimations.EBETalkH")
	pnovaBrex.AddAnimation("EBEngineerBackH", "Bridge.Characters.CommonAnimations.StandingConsole")
	pnovaBrex.AddAnimation("EBEngineerTurnS", "Bridge.Characters.novaSmallAnimations.EBETalkS")
	pnovaBrex.AddAnimation("EBEngineerBackS", "Bridge.Characters.CommonAnimations.StandingConsole")
	pnovaBrex.AddAnimation("EBEngineerTurnT", "Bridge.Characters.novaSmallAnimations.EBETalkT")
	pnovaBrex.AddAnimation("EBEngineerBackT", "Bridge.Characters.CommonAnimations.StandingConsole")

	pnovaBrex.AddAnimation("novaEngineerTurnX", "Bridge.Characters.novaSmallAnimations.novaTurnAtETowardsCaptain")
	pnovaBrex.AddAnimation("novaEngineerBackX", "Bridge.Characters.novaSmallAnimations.novaTurnBackAtEFromCaptain")

	# Breathing
	pnovaBrex.AddAnimation("EBEngineerBreathe", "Bridge.Characters.CommonAnimations.StandingConsole")
	pnovaBrex.AddAnimation("EBEngineerBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pnovaBrex.AddRandomAnimation("Bridge.Characters.novaSmallAnimations.novaEConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pnovaBrex.AddAnimation("PushingButtons", "Bridge.Characters.novaSmallAnimations.novaEConsoleInteraction")

	# Hit animations
	pnovaBrex.AddAnimation("novaEngineerHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pnovaBrex.AddAnimation("novaEngineerHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pnovaBrex.AddAnimation("novaEngineerReactLeftStanding", "Bridge.Characters.CommonAnimations.ReactLeft");
	pnovaBrex.AddAnimation("novaEngineerReactRightStanding", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	AddCommonAnimations(pnovaBrex)

	# Brex sits on the nova bridge
	pnovaBrex.SetStanding(0)
	pnovaBrex.SetLocation("novaEngineer")
	pnovaBrex.AddPositionZoom("novaEngineer", 0.55)
	pnovaBrex.AddPositionZoom("novaEngineer1", 0.55)
	pnovaBrex.AddPositionZoom("novaEngineer2", 0.55)
#	kDebugObj.Print("Finished configuring Brex")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pnovaBrex	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pnovaBrex):
	pnovaBrex.AddRandomAnimation("Bridge.Characters.novaSmallAnimations.ELookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	#pnovaBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pnovaBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	pnovaBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pnovaBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	#pnovaBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	#pnovaBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	#pnovaBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.AtEase", App.CharacterClass.STANDING_ONLY)


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
						"LoweringShields",

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
	import Bridge.Characters.novaSmallAnimations
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Galaxy")

	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(Bridge.Characters.novaSmallAnimations.MoveFromEToL1(self))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "EnableContactEngineeringButton"), 15.0)
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEngineeringSet"), 0.1)
	pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "GalaxyEngSeated"))
	return pSequence

def MoveToEngineeringSet(pAction):
#	kDebugObj.Print("Moving Brex to the Engineering set")

	pBridge = App.g_kSetManager.GetSet("bridge")
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet()
	pnovaBrex = pBridge.RemoveObjectFromSet("Engineer")
	assert pnovaBrex
	bSuccess = pEngineering.AddObjectToSet(pnovaBrex, "Engineer")
	assert bSuccess

#	kDebugObj.Print("Done in MoveToEngineeringSet()")

	return 0

def EnableContactEngineeringButton(pAction):
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringEnabled(1)

	return 0
	
def MoveFromL1ToE(self):
	import Bridge.Characters.novaSmallAnimations
	pSequence = App.TGSequence_Create()
	#pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "DBL1S"))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToDBridgeSet"))
	pSequence.AppendAction(Bridge.Characters.novaSmallAnimations.MoveFromL1ToE(self))
	return pSequence

def MoveToDBridgeSet(pAction):
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringEnabled(0)
	import Bridge.Characters.novaSmallAnimations

	pBridge = Bridge.BridgeUtils.GetBridge()
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Galaxy")
	pnovaBrex = pEngineering.RemoveObjectFromSet("Engineer")
	assert pnovaBrex
	bSuccess = pBridge.AddObjectToSet(pnovaBrex, "Engineer")
	assert bSuccess

	return 0

def EBMoveFromEToL1(self):
	import Bridge.Characters.novaSmallAnimations
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Sovereign")
	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(Bridge.Characters.novaSmallAnimations.EBMoveFromEToL1(self))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "EnableContactEngineeringButton"), 5.0)
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEngineeringSet"), 0.1)
	pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "SovereignEngSeated"))
	return pSequence

def EBMoveFromL1ToE(self):
	import Bridge.Characters.novaSmallAnimations
	pSequence = App.TGSequence_Create()
	#pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "EBL1S"))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEBridgeSet"))
	pSequence.AppendAction(Bridge.Characters.novaSmallAnimations.EBMoveFromL1ToE(self))
	return pSequence

def MoveToEBridgeSet(pAction):
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringEnabled(0)
	import Bridge.Characters.novaSmallAnimations

	pBridge = Bridge.BridgeUtils.GetBridge()
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Sovereign")
	pnovaBrex = pEngineering.RemoveObjectFromSet("Engineer")
	assert pnovaBrex
	bSuccess = pBridge.AddObjectToSet(pnovaBrex, "Engineer")
	assert bSuccess

	return 0

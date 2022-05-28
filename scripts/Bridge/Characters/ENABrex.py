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
	pENABrex = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", CharacterPaths.g_pcHeadNIFPath + "HeadBrex/brex_head_no_mouth.nif")
	pENABrex.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Brex/brex_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/brex_head.tga")

	pENABrex.SetCharacterName("Brex")

	# Add the character to the set
	pSet.AddObjectToSet(pENABrex, "Engineer")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pENABrex)

	# Setup the character configuration
	pENABrex.SetSize(App.CharacterClass.SMALL)
	pENABrex.SetGender(App.CharacterClass.MALE)
	pENABrex.SetRandomAnimationChance(.75)
	pENABrex.SetBlinkChance(0.1)

	pENABrex.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Engineering officer generic sounds
	LoadSounds()

	pENABrex.AdENAacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_blink1.tga")
	pENABrex.AdENAacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_blink2.tga")
	pENABrex.AdENAacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_eyes_close.tga")
	pENABrex.SetBlinkStages(3)

	pENABrex.AdENAacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_head_a.tga")
	pENABrex.AdENAacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_head_e.tga")
	pENABrex.AdENAacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_head_u.tga")
	pENABrex.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pENABrex.GetDatabase(), "BrexNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pENABrex.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Engineering")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	pENABrex.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pENABrex.SetLocation("")

#	kDebugObj.Print("Finished creating Brex")
	return pENABrex


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
	pENABrex = App.CharacterClass_Cast(pSet.GetObject("Engineer"))
	if (pENABrex == None):
#		kDebugObj.Print("******* Engineering officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Engineer..")
	import Bridge.EngineerCharacterHandlers
	Bridge.EngineerCharacterHandlers.AttachMenuToEngineer(pENABrex)

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
#	ConfigureForEnterpriseA()
#
#	Configure ourselves for the EnterpriseA bridge
#
#	Args:	pENABrex	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForEnterpriseA(pENABrex):
#	kDebugObj.Print("Configuring Brex for the EnterpriseA bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForEnterpriseA")
	pENABrex.ClearAnimations()

	# Register animation mappings
	pENABrex.AddAnimation("SeatedENAEngineer", "Bridge.Characters.CommonAnimations.StandingConsole")
	pENABrex.AddAnimation("EBL1SToE", "Bridge.Characters.Brex.EBMoveFromL1ToE")
	pENABrex.AddAnimation("SovereignEngSeatedToE", "Bridge.Characters.Brex.EBMoveFromL1ToE")
	pENABrex.AddAnimation("EBEngineerToL1", "Bridge.Characters.Brex.EBMoveFromEToL1")
	pENABrex.AddAnimation("ENAEngineerTurnCaptain", "Bridge.Characters.ENASmallAnimations.ENATurnAtETowardsCaptain")
	pENABrex.AddAnimation("ENAEngineerBackCaptain", "Bridge.Characters.ENASmallAnimations.ENATurnBackAtEFromCaptain")
	pENABrex.AddAnimation("EBEngineer1ToE", "Bridge.Characters.ENASmallAnimations.EBMoveFromE1ToE")
	pENABrex.AddAnimation("EBEngineerToE1", "Bridge.Characters.ENASmallAnimations.EBMoveFromEToE1")
	pENABrex.AddAnimation("EBEngineer2ToE", "Bridge.Characters.ENASmallAnimations.EBMoveFromE2ToE")
	pENABrex.AddAnimation("EBEngineerToE2", "Bridge.Characters.ENASmallAnimations.EBMoveFromEToE2")
	pENABrex.AddAnimation("EBEngineer1ToE2", "Bridge.Characters.ENASmallAnimations.EBMoveFromE1ToE2")
	pENABrex.AddAnimation("EBEngineer2ToE1", "Bridge.Characters.ENASmallAnimations.EBMoveFromE2ToE1")

	pENABrex.AddAnimation("ENAEngineerGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pENABrex.AddAnimation("ENAEngineerGlanceAwayCaptain", "Bridge.Characters.ENASmallAnimations.ENAEConsoleInteraction")

	pENABrex.AddAnimation("EBEngineerTurnC", "Bridge.Characters.ENASmallAnimations.EBETalkC")
	pENABrex.AddAnimation("EBEngineerBackC", "Bridge.Characters.CommonAnimations.StandingConsole")
	pENABrex.AddAnimation("EBEngineerTurnH", "Bridge.Characters.ENASmallAnimations.EBETalkH")
	pENABrex.AddAnimation("EBEngineerBackH", "Bridge.Characters.CommonAnimations.StandingConsole")
	pENABrex.AddAnimation("EBEngineerTurnS", "Bridge.Characters.ENASmallAnimations.EBETalkS")
	pENABrex.AddAnimation("EBEngineerBackS", "Bridge.Characters.CommonAnimations.StandingConsole")
	pENABrex.AddAnimation("EBEngineerTurnT", "Bridge.Characters.ENASmallAnimations.EBETalkT")
	pENABrex.AddAnimation("EBEngineerBackT", "Bridge.Characters.CommonAnimations.StandingConsole")

	pENABrex.AddAnimation("ENAEngineerTurnX", "Bridge.Characters.ENASmallAnimations.ENATurnAtETowardsCaptain")
	pENABrex.AddAnimation("ENAEngineerBackX", "Bridge.Characters.ENASmallAnimations.ENATurnBackAtEFromCaptain")

	# Breathing
	pENABrex.AddAnimation("EBEngineerBreathe", "Bridge.Characters.CommonAnimations.StandingConsole")
	pENABrex.AddAnimation("EBEngineerBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pENABrex.AddRandomAnimation("Bridge.Characters.ENASmallAnimations.ENAEConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pENABrex.AddAnimation("PushingButtons", "Bridge.Characters.ENASmallAnimations.ENAEConsoleInteraction")

	# Hit animations
	pENABrex.AddAnimation("ENAEngineerHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pENABrex.AddAnimation("ENAEngineerHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pENABrex.AddAnimation("ENAEngineerReactLeftStanding", "Bridge.Characters.CommonAnimations.ReactLeft");
	pENABrex.AddAnimation("ENAEngineerReactRightStanding", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	AddCommonAnimations(pENABrex)

	# Brex sits on the ENA bridge
	pENABrex.SetStanding(0)
	pENABrex.SetLocation("ENAEngineer")
	pENABrex.AddPositionZoom("ENAEngineer", 0.4)
	pENABrex.AddPositionZoom("ENAEngineer1", 0.4)
	pENABrex.AddPositionZoom("ENAEngineer2", 0.4)
#	kDebugObj.Print("Finished configuring Brex")
	pENABrex.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pENABrex	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pENABrex):
	debug(__name__ + ", AddCommonAnimations")
	pENABrex.AddRandomAnimation("Bridge.Characters.ENASmallAnimations.ELookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	#pENABrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pENABrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	pENABrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pENABrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pENABrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pENABrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	#pENABrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.AtEase", App.CharacterClass.STANDING_ONLY)


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
						"FrontShielENAailed",
						"RearShieldDraining",
						"RearShielENAailed",
						"TopShieldDraining",
						"TopShielENAailed",
						"BottomShieldDraining",
						"BottomShielENAailed",
						"LeftShieldDraining",
						"LeftShielENAailed",
						"RightShieldDraining",
						"RightShielENAailed",
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
	import Bridge.Characters.ENASmallAnimations
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Galaxy")

	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(Bridge.Characters.ENASmallAnimations.MoveFromEToL1(self))
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
	pENABrex = pBridge.RemoveObjectFromSet("Engineer")
	assert pENABrex
	bSuccess = pEngineering.AddObjectToSet(pENABrex, "Engineer")
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
	import Bridge.Characters.ENASmallAnimations
	pSequence = App.TGSequence_Create()
	#pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "DBL1S"))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToDBridgeSet"))
	pSequence.AppendAction(Bridge.Characters.ENASmallAnimations.MoveFromL1ToE(self))
	return pSequence

def MoveToDBridgeSet(pAction):
	debug(__name__ + ", MoveToDBridgeSet")
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringEnabled(0)
	import Bridge.Characters.ENASmallAnimations

	pBridge = Bridge.BridgeUtils.GetBridge()
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Galaxy")
	pENABrex = pEngineering.RemoveObjectFromSet("Engineer")
	assert pENABrex
	bSuccess = pBridge.AddObjectToSet(pENABrex, "Engineer")
	assert bSuccess

	return 0

def EBMoveFromEToL1(self):
	debug(__name__ + ", EBMoveFromEToL1")
	import Bridge.Characters.ENASmallAnimations
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Sovereign")
	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(Bridge.Characters.ENASmallAnimations.EBMoveFromEToL1(self))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "EnableContactEngineeringButton"), 5.0)
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEngineeringSet"), 0.1)
	pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "SovereignEngSeated"))
	return pSequence

def EBMoveFromL1ToE(self):
	debug(__name__ + ", EBMoveFromL1ToE")
	import Bridge.Characters.ENASmallAnimations
	pSequence = App.TGSequence_Create()
	#pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "EBL1S"))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEBridgeSet"))
	pSequence.AppendAction(Bridge.Characters.ENASmallAnimations.EBMoveFromL1ToE(self))
	return pSequence

def MoveToEBridgeSet(pAction):
	debug(__name__ + ", MoveToEBridgeSet")
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringEnabled(0)
	import Bridge.Characters.ENASmallAnimations

	pBridge = Bridge.BridgeUtils.GetBridge()
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Sovereign")
	pENABrex = pEngineering.RemoveObjectFromSet("Engineer")
	assert pENABrex
	bSuccess = pBridge.AddObjectToSet(pENABrex, "Engineer")
	assert bSuccess

	return 0

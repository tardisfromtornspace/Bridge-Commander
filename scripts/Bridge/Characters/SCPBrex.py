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
	pSCPBrex = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", CharacterPaths.g_pcHeadNIFPath + "HeadBrex/brex_head_no_mouth.nif")
	pSCPBrex.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Brex/brex_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/brex_head.tga")

	pSCPBrex.SetCharacterName("Brex")

	# Add the character to the set
	pSet.AddObjectToSet(pSCPBrex, "Engineer")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pSCPBrex)

	# Setup the character configuration
	pSCPBrex.SetSize(App.CharacterClass.SMALL)
	pSCPBrex.SetGender(App.CharacterClass.MALE)
	pSCPBrex.SetRandomAnimationChance(.75)
	pSCPBrex.SetBlinkChance(0.1)

	pSCPBrex.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Engineering officer generic sounds
	LoadSounds()

	pSCPBrex.AdSCPacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_blink1.tga")
	pSCPBrex.AdSCPacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_blink2.tga")
	pSCPBrex.AdSCPacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_eyes_close.tga")
	pSCPBrex.SetBlinkStages(3)

	pSCPBrex.AdSCPacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_head_a.tga")
	pSCPBrex.AdSCPacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_head_e.tga")
	pSCPBrex.AdSCPacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_head_u.tga")
	pSCPBrex.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pSCPBrex.GetDatabase(), "BrexNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pSCPBrex.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Engineering")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	pSCPBrex.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pSCPBrex.SetLocation("")

#	kDebugObj.Print("Finished creating Brex")
	return pSCPBrex


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
	pSCPBrex = App.CharacterClass_Cast(pSet.GetObject("Engineer"))
	if (pSCPBrex == None):
#		kDebugObj.Print("******* Engineering officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Engineer..")
	import Bridge.EngineerCharacterHandlers
	Bridge.EngineerCharacterHandlers.AttachMenuToEngineer(pSCPBrex)

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
#	ConfigureForGalor()
#
#	Configure ourselves for the Galor bridge
#
#	Args:	pSCPBrex	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalor(pSCPBrex):
#	kDebugObj.Print("Configuring Brex for the Galor bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalor")
	pSCPBrex.ClearAnimations()

	# Register animation mappings
	pSCPBrex.AddAnimation("SeatedSCPEngineer", "Bridge.Characters.CommonAnimations.StandingConsole")
	pSCPBrex.AddAnimation("EBL1SToE", "Bridge.Characters.Brex.EBMoveFromL1ToE")
	pSCPBrex.AddAnimation("SovereignEngSeatedToE", "Bridge.Characters.Brex.EBMoveFromL1ToE")
	pSCPBrex.AddAnimation("EBEngineerToL1", "Bridge.Characters.Brex.EBMoveFromEToL1")
	pSCPBrex.AddAnimation("SCPEngineerTurnCaptain", "Bridge.Characters.SCPSmallAnimations.SCPTurnAtETowardsCaptain")
	pSCPBrex.AddAnimation("SCPEngineerBackCaptain", "Bridge.Characters.SCPSmallAnimations.SCPTurnBackAtEFromCaptain")
	pSCPBrex.AddAnimation("EBEngineer1ToE", "Bridge.Characters.SCPSmallAnimations.EBMoveFromE1ToE")
	pSCPBrex.AddAnimation("EBEngineerToE1", "Bridge.Characters.SCPSmallAnimations.EBMoveFromEToE1")
	pSCPBrex.AddAnimation("EBEngineer2ToE", "Bridge.Characters.SCPSmallAnimations.EBMoveFromE2ToE")
	pSCPBrex.AddAnimation("EBEngineerToE2", "Bridge.Characters.SCPSmallAnimations.EBMoveFromEToE2")
	pSCPBrex.AddAnimation("EBEngineer1ToE2", "Bridge.Characters.SCPSmallAnimations.EBMoveFromE1ToE2")
	pSCPBrex.AddAnimation("EBEngineer2ToE1", "Bridge.Characters.SCPSmallAnimations.EBMoveFromE2ToE1")

	pSCPBrex.AddAnimation("SCPEngineerGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pSCPBrex.AddAnimation("SCPEngineerGlanceAwayCaptain", "Bridge.Characters.SCPSmallAnimations.SCPEConsoleInteraction")

	pSCPBrex.AddAnimation("EBEngineerTurnC", "Bridge.Characters.SCPSmallAnimations.EBETalkC")
	pSCPBrex.AddAnimation("EBEngineerBackC", "Bridge.Characters.SCPSmallAnimations.SCPEConsoleInteraction")
	pSCPBrex.AddAnimation("EBEngineerTurnH", "Bridge.Characters.SCPSmallAnimations.EBETalkH")
	pSCPBrex.AddAnimation("EBEngineerBackH", "Bridge.Characters.SCPSmallAnimations.SCPEConsoleInteraction")
	pSCPBrex.AddAnimation("EBEngineerTurnS", "Bridge.Characters.SCPSmallAnimations.EBETalkS")
	pSCPBrex.AddAnimation("EBEngineerBackS", "Bridge.Characters.SCPSmallAnimations.SCPEConsoleInteraction")
	pSCPBrex.AddAnimation("EBEngineerTurnT", "Bridge.Characters.SCPSmallAnimations.EBETalkT")
	pSCPBrex.AddAnimation("EBEngineerBackT", "Bridge.Characters.SCPSmallAnimations.SCPEConsoleInteraction")

	pSCPBrex.AddAnimation("SCPEngineerTurnX", "Bridge.Characters.SCPSmallAnimations.SCPTurnAtETowardsCaptain")
	pSCPBrex.AddAnimation("SCPEngineerBackX", "Bridge.Characters.SCPSmallAnimations.SCPTurnBackAtEFromCaptain")

	# Breathing
	pSCPBrex.AddAnimation("EBEngineerBreathe", "Bridge.Characters.SCPSmallAnimations.SCPEConsoleInteraction")
	pSCPBrex.AddAnimation("EBEngineerBreatheTurned", "Bridge.Characters.SCPSmallAnimations.SCPEConsoleInteraction")

	# Interaction
	pSCPBrex.AddRandomAnimation("Bridge.Characters.SCPSmallAnimations.SCPEConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pSCPBrex.AddAnimation("PushingButtons", "Bridge.Characters.SCPSmallAnimations.SCPEConsoleInteraction")

	# Hit animations
	pSCPBrex.AddAnimation("SCPEngineerHit", "Bridge.Characters.SCPMediumAnimations.SCPeHit")
	pSCPBrex.AddAnimation("SCPEngineerHitHard", "Bridge.Characters.SCPMediumAnimations.SCPeHitHard")
	pSCPBrex.AddAnimation("SCPEngineerReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft");
	pSCPBrex.AddAnimation("SCPEngineerReactRight", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	AddCommonAnimations(pSCPBrex)

	# Brex sits on the SCP bridge
	pSCPBrex.SetStanding(0)
	pSCPBrex.SetLocation("SCPEngineer")
	pSCPBrex.AddPositionZoom("SCPEngineer", 0.4)
	pSCPBrex.AddPositionZoom("SCPEngineer1", 0.4)
	pSCPBrex.AddPositionZoom("SCPEngineer2", 0.4)
#	kDebugObj.Print("Finished configuring Brex")
	pSCPBrex.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pSCPBrex	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pSCPBrex):
	debug(__name__ + ", AddCommonAnimations")
	pSCPBrex.AddRandomAnimation("Bridge.Characters.SCPSmallAnimations.ELookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	#pSCPBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pSCPBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	pSCPBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pSCPBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pSCPBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pSCPBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	#pSCPBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.AtEase", App.CharacterClass.STANDING_ONLY)


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
						"FrontShielSCPailed",
						"RearShieldDraining",
						"RearShielSCPailed",
						"TopShieldDraining",
						"TopShielSCPailed",
						"BottomShieldDraining",
						"BottomShielSCPailed",
						"LeftShieldDraining",
						"LeftShielSCPailed",
						"RightShieldDraining",
						"RightShielSCPailed",
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
	import Bridge.Characters.SCPSmallAnimations
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Galaxy")

	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(Bridge.Characters.SCPSmallAnimations.MoveFromEToL1(self))
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
	pSCPBrex = pBridge.RemoveObjectFromSet("Engineer")
	assert pSCPBrex
	bSuccess = pEngineering.AddObjectToSet(pSCPBrex, "Engineer")
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
	import Bridge.Characters.SCPSmallAnimations
	pSequence = App.TGSequence_Create()
	#pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "DBL1S"))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToDBridgeSet"))
	pSequence.AppendAction(Bridge.Characters.SCPSmallAnimations.MoveFromL1ToE(self))
	return pSequence

def MoveToDBridgeSet(pAction):
	debug(__name__ + ", MoveToDBridgeSet")
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringEnabled(0)
	import Bridge.Characters.SCPSmallAnimations

	pBridge = Bridge.BridgeUtils.GetBridge()
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Galaxy")
	pSCPBrex = pEngineering.RemoveObjectFromSet("Engineer")
	assert pSCPBrex
	bSuccess = pBridge.AddObjectToSet(pSCPBrex, "Engineer")
	assert bSuccess

	return 0

def EBMoveFromEToL1(self):
	debug(__name__ + ", EBMoveFromEToL1")
	import Bridge.Characters.SCPSmallAnimations
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Sovereign")
	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(Bridge.Characters.SCPSmallAnimations.EBMoveFromEToL1(self))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "EnableContactEngineeringButton"), 5.0)
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEngineeringSet"), 0.1)
	pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "SovereignEngSeated"))
	return pSequence

def EBMoveFromL1ToE(self):
	debug(__name__ + ", EBMoveFromL1ToE")
	import Bridge.Characters.SCPSmallAnimations
	pSequence = App.TGSequence_Create()
	#pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "EBL1S"))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEBridgeSet"))
	pSequence.AppendAction(Bridge.Characters.SCPSmallAnimations.EBMoveFromL1ToE(self))
	return pSequence

def MoveToEBridgeSet(pAction):
	debug(__name__ + ", MoveToEBridgeSet")
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringEnabled(0)
	import Bridge.Characters.SCPSmallAnimations

	pBridge = Bridge.BridgeUtils.GetBridge()
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Sovereign")
	pSCPBrex = pEngineering.RemoveObjectFromSet("Engineer")
	assert pSCPBrex
	bSuccess = pBridge.AddObjectToSet(pSCPBrex, "Engineer")
	assert bSuccess

	return 0

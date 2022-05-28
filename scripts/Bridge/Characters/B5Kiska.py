###############################################################################
#	Filename:	RomKiska.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads RomKiska Lomar, Helm, and configures animations
#	
#	Created:	3/28/00 -	Erik Novales
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create RomKiska by building her character and placing her on the passed in set.
#	Create her menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating RomKiska")

	if (pSet.GetObject("Helm") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Helm")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "B5/BodyFemM/BodyFemM.NIF", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "B5/HeadKiska/kiska_head.NIF", None)
	pRomKiska = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "B5/BodyFemM/BodyFemM.NIF", CharacterPaths.g_pcHeadNIFPath + "B5/HeadKiska/kiska_head.NIF", 1)
	pRomKiska.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "B5/BodyFemS/FedFemGold_body.tga", CharacterPaths.g_pcHeadTexPath + "B5/HeadKiska/kiska_head.tga")

	pRomKiska.SetCharacterName("Kiska")

	# Add the character to the set
	pSet.AddObjectToSet(pRomKiska, "Helm")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pRomKiska)

	# Setup the character configuration
	pRomKiska.SetSize(App.CharacterClass.MEDIUM)
	pRomKiska.SetGender(App.CharacterClass.FEMALE)
	pRomKiska.SetStanding(0)
	pRomKiska.SetRandomAnimationChance(0.75)
	pRomKiska.SetBlinkChance(0.1)
	pRomKiska.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Helm officer generic sounds
	LoadSounds()

	pRomKiska.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "B5/HeadKiska/Kiska_head_blink1.tga")
	pRomKiska.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "B5/HeadKiska/Kiska_head_blink2.tga")
	pRomKiska.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "B5/HeadKiska/Kiska_head_eyesclosed.tga")
	pRomKiska.SetBlinkStages(3)

	pRomKiska.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "B5/HeadKiska/Kiska_head_a.tga")
	pRomKiska.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "B5/HeadKiska/Kiska_head_e.tga")
	pRomKiska.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "B5/HeadKiska/Kiska_head_u.tga")
	pRomKiska.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pRomKiska.GetDatabase(), "KiskaNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pRomKiska.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Helm")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating RomKiska")
	return pRomKiska


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
	# Get our character object
	pRomKiska = App.CharacterClass_Cast(pSet.GetObject("Helm"))
	if (pRomKiska == None):
#		kDebugObj.Print("******* Helm officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Helm..")
	import Bridge.HelmCharacterHandlers
	Bridge.HelmCharacterHandlers.AttachMenuToHelm(pRomKiska)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Orbiting planet"
	#



###############################################################################
#	ConfigureForWarbird()
#
#	Configure ourselves for the Warbird bridge
#
#	Args:	pRomKiska	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForWarbird(pRomKiska):
#	kDebugObj.Print("Configuring RomKiska for the Galaxy bridge")

	# Clear out any old animations from another configuration
	pRomKiska.ClearAnimations()

	# Register animation mappings
	pRomKiska.AddAnimation("DBL1MToH", "Bridge.Characters.MediumAnimations.MoveFromL1ToH")
	pRomKiska.AddAnimation("DBHelmToL1", "Bridge.Characters.MediumAnimations.MoveFromHToL1")

	pRomKiska.AddAnimation("RomHelmTurnCaptain", "Bridge.Characters.MediumAnimations.TurnAtHTowardsCaptain")
	pRomKiska.AddAnimation("RomHelmBackCaptain", "Bridge.Characters.MediumAnimations.TurnBackAtHFromCaptain")

	pRomKiska.AddAnimation("DBHelmTurnC", "Bridge.Characters.MediumAnimations.DBHTalkC")
	pRomKiska.AddAnimation("DBHelmBackC", "Bridge.Characters.MediumAnimations.DBHTalkFinC")
	pRomKiska.AddAnimation("DBHelmTurnE", "Bridge.Characters.MediumAnimations.DBHTalkE")
	pRomKiska.AddAnimation("DBHelmBackE", "Bridge.Characters.MediumAnimations.DBHTalkFinE")
	pRomKiska.AddAnimation("DBHelmTurnS", "Bridge.Characters.MediumAnimations.DBHTalkS")
	pRomKiska.AddAnimation("DBHelmBackS", "Bridge.Characters.MediumAnimations.DBHTalkFinS")
	pRomKiska.AddAnimation("DBHelmTurnT", "Bridge.Characters.MediumAnimations.DBHTalkT")
	pRomKiska.AddAnimation("DBHelmBackT", "Bridge.Characters.MediumAnimations.DBHTalkFinT")

	pRomKiska.AddAnimation("DBHelmTurnX", "Bridge.Characters.MediumAnimations.DBHTalkX")
	pRomKiska.AddAnimation("DBHelmBackX", "Bridge.Characters.MediumAnimations.DBHTalkFinX")

	pRomKiska.AddAnimation("RomHelmGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pRomKiska.AddAnimation("RomHelmGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedM")

	# Breathing
	pRomKiska.AddAnimation("DBHelmBreathe", "Bridge.Characters.CommonAnimations.SeatedM")

	# Interaction
	pRomKiska.AddRandomAnimation("Bridge.Characters.MediumAnimations.DBHConsoleInteraction", App.CharacterClass.SITTING_ONLY, 1, 1)

	# So the mission builders can force the call
	pRomKiska.AddAnimation("PushingButtons", "Bridge.Characters.MediumAnimations.DBHConsoleInteraction")

	# Hit animations
	pRomKiska.AddAnimation("DBHelmHit", "Bridge.Characters.MediumAnimations.HHit")
	pRomKiska.AddAnimation("DBHelmHitHard", "Bridge.Characters.MediumAnimations.HHitHard")
	pRomKiska.AddAnimation("DBHelmReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pRomKiska.AddAnimation("DBHelmReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pRomKiska)

	pRomKiska.SetLocation("RomHelm")
	pRomKiska.AddPositionZoom("RomHelm", 0.45, "Helm")
	pRomKiska.SetLookAtAdj(20, -220, 53)
#	kDebugObj.Print("Finished configuring RomKiska")
	


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pRomKiska	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pRomKiska):
	# Interaction with their environment
	pRomKiska.AddRandomAnimation("Bridge.Characters.MediumAnimations.HLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	# Just random stuff
	pRomKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pRomKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pRomKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pRomKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	# These look bad
	#pRomKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pRomKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")

	# These force the arms up
	#pRomKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pRomKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")

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
	lSoundList =	[	"KiskaSir1",	# Click Response
						"KiskaSir2",
						"KiskaSir3",
						"KiskaSir4",
						"KiskaSir5",
						
						"KiskaYes1",	# Order Confirmation
						"KiskaYes2",
						"KiskaYes3",
						"KiskaYes4",

						"gh075",	# Course laid in
						"gh081",	# Intercept course plotted

						"HailOpen1",
						"HailOpen2",
						"NotResponding1",
						"NotResponding2",
						"OnScreen",

						"CollisionAlert1",
						"CollisionAlert2",
						"CollisionAlert3",
						"CollisionAlert4",
						"CollisionAlert5",
						"CollisionAlert6",
						"CollisionAlert7",
						"CollisionAlert10",

						"IncomingMsg1",
						"IncomingMsg2",
						"IncomingMsg3",
						"IncomingMsg4",
						"IncomingMsg5",
						"IncomingMsg6",
					]
	#
	# Loop through that list, loading each sound in the "BridgeGeneric" group
	#
	for sLine in lSoundList:
		pGame.LoadDatabaseSoundInGroup(pDatabase, sLine, "BridgeGeneric")

	App.g_kLocalizationManager.Unload(pDatabase)

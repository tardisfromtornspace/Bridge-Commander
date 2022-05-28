###############################################################################
#	Filename:	novaFemaleExtra2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador novaFemaleExtra2, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDnovaugObj = App.CPyDnovaug()

###############################################################################
#	CreateCharacter()
#
#	Create novaFemaleExtra2 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDnovaugObj.Print("Creating novaFemaleExtra2")

	if (pSet.GetObject("novaFemaleExtra2") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra2")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadLiu/liu_head.nif", None)
	pnovaFemaleExtra2 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadLiu/liu_head.nif")

	pnovaFemaleExtra2.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemTeal_body1.tga", CharacterPaths.g_pcHeadTexPath + "HeadLiu/novaFemale_ensignA_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pnovaFemaleExtra2, "FemaleExtra2")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pnovaFemaleExtra2)

	# Setup the character configuration
	pnovaFemaleExtra2.SetSize(App.CharacterClass.MEDIUM)
	pnovaFemaleExtra2.SetGender(App.CharacterClass.FEMALE)
	pnovaFemaleExtra2.SetRandomAnimationChance(.75)
	pnovaFemaleExtra2.SetBlinkChance(0.1)
	pnovaFemaleExtra2.SetCharacterName("FemaleExtra2")

	pnovaFemaleExtra2.SetHidden(0)

	# Load novaFemaleExtra2's generic sounds
	LoadSounds()

	# Create novaFemaleExtra2's menus
	#import novaFemaleExtra2MenuHandlers
	#novaFemaleExtra2MenuHandlers.CreateMenus(pnovaFemaleExtra2)

	pnovaFemaleExtra2.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pnovaFemaleExtra2.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pnovaFemaleExtra2.SetLocation("")

#	kDnovaugObj.Print("Finished creating novaFemaleExtra2")
	return pnovaFemaleExtra2

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pnovaFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pnovaFemaleExtra2):
#	kDnovaugObj.Print("Configuring novaFemaleExtra2 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	pnovaFemaleExtra2.ClearAnimations()

	#
	# *** CURRENTLY novaFemaleExtra2 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pnovaFemaleExtra2)

	pnovaFemaleExtra2.SetAsExtra(1)
	pnovaFemaleExtra2.SetHidden(0)
	pnovaFemaleExtra2.SetStanding(0)

	pnovaFemaleExtra2.SetLocation("DBL2M")
#	kDnovaugObj.Print("Finished configuring novaFemaleExtra2")


###############################################################################
#	ConfigureForPrometheus()
#
#	Configure ourselves for the novaetheus bridge
#
#	Args:	pnovaFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForPrometheus(pnovaFemaleExtra2):
#	kDnovaugObj.Print("Configuring novaFemaleExtra2 for the novaetheus bridge")

	# Clear out any old animations from another configuration
	pnovaFemaleExtra2.ClearAnimations()

	# Register animation mappings
	#pnovaFemaleExtra2.AddAnimation("novaL2MToG", "Bridge.Characters.novaMediumAnimations.novaL2ToG2")
	#pnovaFemaleExtra2.AddAnimation("novaG2MToL", "Bridge.Characters.novaMediumAnimations.novaG2ToL2")
	#pnovaFemaleExtra2.AddAnimation("StandingnovaG2M", "Bridge.Characters.CommonAnimations.Standing")
	#pnovaFemaleExtra2.SetStanding(1)

	# Hit animations
	#pnovaFemaleExtra2.AddAnimation("novaG2MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#pnovaFemaleExtra2.AddAnimation("novaG2MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	#pnovaFemaleExtra2.AddAnimation("novaG2MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	#pnovaFemaleExtra2.AddAnimation("novaG2MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	#pnovaFemaleExtra2.AddAnimation("novaG2MFly", "Bridge.Characters.CommonAnimations.Blast")

	pnovaFemaleExtra2.SetAsExtra(1)
	pnovaFemaleExtra2.SetHidden(0)

	# Add common animations.
	AddCommonAnimations(pnovaFemaleExtra2)

	pnovaFemaleExtra2.SetLocation("novaL3M")
#	kDnovaugObj.Print("Finished configuring novaFemaleExtra2")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pnovaFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pnovaFemaleExtra2):
	pnovaFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pnovaFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
#	pnovaFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
#	pnovaFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
#	pnovaFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
#	pnovaFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
#	pnovaFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
#	pnovaFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
#	pnovaFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pnovaFemaleExtra2.AddRandomAnimation("Bridge.Characters.novaMediumAnimations.nova_seated_interaction")
#	pnovaFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pnovaFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
#	pnovaFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	#
	# novaFemaleExtra2 has no generic bridge sounds at this time
	#
	pass

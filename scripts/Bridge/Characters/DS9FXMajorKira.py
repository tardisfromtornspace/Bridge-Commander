# by USS Sovereign register and make a new character in game :P
# MajorKira v2.1, thanks to BlackRook of course :)

# Imports
import App

# Fix for low/med detail game settings
g_pBodyPath = 'data/Models/Characters/Bodies/'
g_pHeadPath = 'data/Models/Characters/Heads/'


# Create character
def CreateCharacter(pSet):

        # Register Kira
	if (pSet.GetObject("Kira") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Kira")))

	# Create the character
	App.g_kModelManager.LoadModel(g_pBodyPath + "BodyFemS/BodyFemS.nif", "Bip01")
	App.g_kModelManager.LoadModel(g_pHeadPath + "DS9FXMajorKira/kira_head.nif", None)
	pKira = App.CharacterClass_Create(g_pBodyPath + "BodyFemS/BodyFemS.nif", g_pHeadPath + "DS9FXMajorKira/kira_head.nif")
	pKira.ReplaceBodyAndHead(g_pBodyPath + "BodyFemS/BajoranRed_body.tga", g_pHeadPath + "DS9FXMajorKira/kira_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pKira, "Kira")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pKira)
	
	# Setup the character configuration
	pKira.SetSize(App.CharacterClass.MEDIUM)
	pKira.SetGender(App.CharacterClass.FEMALE)
	pKira.SetStanding(1)
	pKira.SetRandomAnimationChance(.01)
	pKira.SetBlinkChance(0.1)

	pKira.SetCharacterName("Kira")
	pKira.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Configure for the Generic bridge
	import Guest
	Guest.ConfigureForGeneric(pKira)

	pKira.AddFacialImage("Blink0", g_pHeadPath + "DS9FXMajorKira/kira_head_blink1.tga")
	pKira.AddFacialImage("Blink1", g_pHeadPath + "DS9FXMajorKira/kira_head_blink2.tga")
	pKira.AddFacialImage("Blink2", g_pHeadPath + "DS9FXMajorKira/kira_head_eyesclosed.tga")
	pKira.SetBlinkStages(3)

	pKira.AddFacialImage("SpeakA", g_pHeadPath + "DS9FXMajorKira/kira_head_a.tga")
	pKira.AddFacialImage("SpeakE", g_pHeadPath + "DS9FXMajorKira/kira_head_e.tga")
	pKira.AddFacialImage("SpeakU", g_pHeadPath + "DS9FXMajorKira/kira_head_u.tga")
	pKira.SetAnimatedSpeaking(1)

	pKira.AddAnimation("StarbaseSeatedGlanceLeft", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pKira.AddAnimation("StarbaseSeatedGlanceAwayLeft", __name__ + ".Breathing")

	pKira.SetLocation("StarbaseSeated")

	return pKira




def Breathing(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/StarbaseSeated01breathing.nif", "StarbaseSeated01breathing")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimAction_Create(pAnimNode, "StarbaseSeated01breathing", 0, 0)
	pSequence.AddAction(pAction)
	return pSequence

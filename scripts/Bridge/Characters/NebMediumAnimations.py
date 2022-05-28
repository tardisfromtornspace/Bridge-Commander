from bcdebug import debug
# MediumAnimations.py
# This file includes all animations shared by medium characters

import App
import Bridge.Characters.CommonAnimations

########################################################################################################################
####################################################
# D-Bridge Animations
####################################################
def PlaceAtH(pCharacter):
	debug(__name__ + ", PlaceAtH")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_stand_h_m.nif", "db_stand_h_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "db_stand_h_m")
	pSequence.AddAction(pAction)
	return pSequence

def PlaceAtL1(pCharacter):
	debug(__name__ + ", PlaceAtL1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_L1toG1_S.nif", "db_L1toG1_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "db_L1toG1_S")
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def PlaceAtL2(pCharacter):
	debug(__name__ + ", PlaceAtL2")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_L2toG2_S.nif", "db_L2toG2_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "db_L2toG2_S")
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def PlaceAtL3(pCharacter):
	debug(__name__ + ", PlaceAtL3")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_L3toG3_S.nif", "db_L3toG3_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "db_L3toG3_S")
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def PlaceAtC(pCharacter):
	debug(__name__ + ", PlaceAtC")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_stand_c_m.nif", "db_stand_c_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "db_stand_c_m")
	pSequence.AddAction(pAction)
	return pSequence

def PlaceAtC1(pCharacter):
	debug(__name__ + ", PlaceAtC1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_face_capt_c1.nif", "db_face_capt_c1")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "db_face_capt_c1")
	pSequence.AddAction(pAction)
	return pSequence

def SeatedH(pCharacter):
	debug(__name__ + ", SeatedH")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_seated_h_m.nif", "db_seated_h_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimAction_Create(pAnimNode, "db_seated_h_m", 0, 0)
	pSequence.AddAction(pAction)
	return pSequence

def SeatedC(pCharacter):
	debug(__name__ + ", SeatedC")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_seated_c_m.nif", "db_seated_c_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimAction_Create(pAnimNode, "db_seated_c_m", 0, 0)
	pSequence.AddAction(pAction)
	return pSequence

def TurnAtC1TowardsCaptain(pCharacter):
	debug(__name__ + ", TurnAtC1TowardsCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_face_capt_c1.nif", "db_face_capt_c1")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_face_capt_c1", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def TurnAtCTowardsCaptain(pCharacter):
	debug(__name__ + ", TurnAtCTowardsCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_face_capt_c.nif", "db_face_capt_c")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_face_capt_c", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def TurnAtXTowardsCaptain(pCharacter):
	debug(__name__ + ", TurnAtXTowardsCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_face_capt_x.nif", "db_face_capt_x")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_face_capt_x", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

	# Turn towards captain medium
def TurnAtHTowardsCaptain(pCharacter):
	debug(__name__ + ", TurnAtHTowardsCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_face_capt_h.nif", "db_face_capt_h")
	kAM.LoadAnimation ("data/animations/db_chair_H_face_capt.nif", "db_chair_H_face_capt")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_face_capt_h", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	pAction = App.TGAnimAction_Create(pBridgeNode, "db_chair_H_face_capt", 0, 0)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def TurnBackAtCFromCaptain(pCharacter):
	debug(__name__ + ", TurnBackAtCFromCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_seated_c_m.NIF", "db_seated_c_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_seated_c_m", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def TurnBackAtC1FromCaptain(pCharacter):
	debug(__name__ + ", TurnBackAtC1FromCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_face_capt_c1_reverse.NIF", "db_face_capt_c1_reverse")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_face_capt_c1_reverse", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

	# Turn back from looking at captain medium
def TurnBackAtHFromCaptain(pCharacter):
	debug(__name__ + ", TurnBackAtHFromCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_face_capt_h_reverse.nif", "db_face_capt_h_reverse")
	kAM.LoadAnimation ("data/animations/db_chair_H_face_capt_reverse.nif", "db_chair_H_face_capt_reverse")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_face_capt_h_reverse", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	pAction = App.TGAnimAction_Create(pBridgeNode, "db_chair_H_face_capt_reverse", 0, 0)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

	# L1 to C medium
def MoveFromL1ToC(pCharacter):
	debug(__name__ + ", MoveFromL1ToC")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_L1toC_m.nif", "db_L1toC_m")
	kAM.LoadAnimation ("data/animations/db_sit_C_m.nif", "db_sit_C_m")
	kAM.LoadAnimation ("data/animations/db_door_l1.nif", "db_Door_L1")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_WalkFromLift = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_L1toC_m", 0, 0)
	pSequence.AddAction(pAnimAction_WalkFromLift, pOpenEyes)
	pDoorAction = App.TGAnimAction_Create(pBridgeNode, "db_Door_L1", 0, 0)
	pSequence.AddAction(pDoorAction, pOpenEyes, 0.125)
	pAnimAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_sit_C_m", 0, 0)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "DBCommander"))
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_SEATED)
	pAnimAction.AddCompletedEvent(pEvent)
	pSequence.AddAction(pAnimAction, pAnimAction_WalkFromLift, 0.0)
	return pSequence	

	# L1 to H medium
def MoveFromL1ToH(pCharacter):
	debug(__name__ + ", MoveFromL1ToH")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_L1toH_m.nif", "db_L1toH_m")
	kAM.LoadAnimation ("data/animations/DB_sit_H_m.nif", "db_sit_h_m")
	kAM.LoadAnimation ("data/animations/db_chair_H_in.nif", "db_chair_H_in")
	kAM.LoadAnimation ("data/animations/db_door_l1.nif", "db_Door_L1")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	fTime = 0.0
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_WalkFromLift = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_L1toH_m", 0, 0)
	pSequence.AddAction(pAnimAction_WalkFromLift, pOpenEyes)
	fTime = kAM.GetAnimationLength("db_L1toH_m")
	pSequence.AddAction(App.TGAnimAction_Create(pBridgeNode, "db_Door_L1", 0, 0), pOpenEyes, 0.125)
	pAnimAction_Sit = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_sit_h_m", 0, 0)
	pSequence.AddAction(pAnimAction_Sit, pAnimAction_WalkFromLift)
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "db_chair_H_in", 0, 0)
	pSequence.AddAction(pAnimAction, pAnimAction_WalkFromLift)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "DBHelm"))
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination (pCharacter)
	pEvent.SetInt (App.CharacterClass.CS_SEATED)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence

def MoveFromCToL1(pCharacter):
	debug(__name__ + ", MoveFromCToL1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_stand_c_m.nif", "db_stand_c_m")
	kAM.LoadAnimation ("data/animations/db_CtoL1_m.nif", "db_CtoL1_m")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Stand = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_stand_c_m", 0, 0);
	pSequence.AddAction(pAnimAction_Stand, pOpenEyes)
	pAnimAction_WalkToLift = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_CtoL1_m", 0, 0)
	pSequence.AddAction(pAnimAction_WalkToLift, pAnimAction_Stand)
	fTime = kAM.GetAnimationLength("db_CtoL1_m");
#	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_Door_L1", 0, 0)
#	pSequence.AddAction(pAnimAction, pAnimAction_Stand, fTime - 1.5)

	pDoorAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "LiftDoorAction", pBridge, "EB_Door_L1", "LiftDoor")
	pSequence.AddAction(pDoorAction, pAnimAction_Stand, fTime - 1.5)

	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "DBL1M"))
	pEvent = App.TGIntEvent_Create()		# Add event to hide character after it gets into the turbolift
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_HIDDEN)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence

	# From chair to L1 medium
def MoveFromHToL1(pCharacter):
	debug(__name__ + ", MoveFromHToL1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_stand_h_m.nif", "db_stand_h_m")
	kAM.LoadAnimation ("data/animations/db_chair_H_out.nif", "db_chair_H_out")
	kAM.LoadAnimation ("data/animations/db_HtoL1_m.nif", "db_HtoL1_m")
	kAM.LoadAnimation ("data/animations/db_door_l1.nif", "DB_Door_L1")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Stand = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_stand_h_m", 0, 0)
	pSequence.AddAction(pAnimAction_Stand, pOpenEyes)
	pSequence.AddAction(Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter), pAnimAction_Stand, 0.0)
	pSequence.AddAction(App.TGAnimAction_Create(pBridgeNode, "db_chair_H_out", 0, 0), pOpenEyes)
	pAnimAction_WalkToLift = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_HtoL1_m", 0, 0)
	pSequence.AddAction(pAnimAction_WalkToLift, pAnimAction_Stand, 0.0)
	fTime = kAM.GetAnimationLength("db_HtoL1_m")
#	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "DB_Door_L1", 0, 0)
#	pSequence.AddAction(pAnimAction, pAnimAction_Stand, fTime - 1.7)	

	pDoorAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "LiftDoorAction", pBridge, "DB_Door_L1", "LiftDoor")
	pSequence.AddAction(pDoorAction, pAnimAction_Stand, fTime - 1.7)

	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "DBL1M"))
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_HIDDEN)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence

def MoveFromCToC1(pCharacter):
	debug(__name__ + ", MoveFromCToC1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_stand_c_m.NIF", "db_stand_c_m")
	kAM.LoadAnimation ("data/animations/DB_CtoC1_M.NIF", "DB_CtoC1_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Stand = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_stand_c_m", 0, 0)
	pSequence.AddAction(pAnimAction_Stand, pOpenEyes)
	pAnimAction_Walk = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_CtoC1_M", 0, 0)
	pSequence.AddAction(pAnimAction_Walk, pAnimAction_Stand, 0.0)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "DBCommander1"))
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_STANDING)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence

def MoveFromC1ToC(pCharacter):
	debug(__name__ + ", MoveFromC1ToC")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_sit_c_m.NIF", "db_sit_c_m")
	kAM.LoadAnimation ("data/animations/DB_C1toC_M.NIF", "DB_C1toC_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Walk = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_C1toC_M", 0, 0)
	pSequence.AddAction(pAnimAction_Walk, pOpenEyes)
	pAnimAction_Sit = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_sit_c_m", 0, 0)
	pSequence.AddAction(pAnimAction_Sit, pAnimAction_Walk)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "DBCommander"))
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_SEATED)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence

def PlaceAtL1Saffi(pCharacter):
	debug(__name__ + ", PlaceAtL1Saffi")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_L1toC_m.nif", "db_L1toC_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "db_L1toC_m")
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def MoveFromC1ToC2(pCharacter):
	debug(__name__ + ", MoveFromC1ToC2")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_C1toC_M.NIF", "DB_C1toC_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Walk = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_C1toC_M", 0, 0)
	pSequence.AddAction(pAnimAction_Walk, pOpenEyes)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "DBCommander2"))
	return pSequence

def MoveFromL1ToC2(pCharacter):
	debug(__name__ + ", MoveFromL1ToC2")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_L1toC_m.nif", "db_L1toC_m")
	kAM.LoadAnimation ("data/animations/db_door_l1.nif", "db_Door_L1")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_WalkFromLift = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_L1toC_m", 0, 0)
	pSequence.AddAction(pAnimAction_WalkFromLift, pOpenEyes)
	pDoorAction = App.TGAnimAction_Create(pBridgeNode, "db_Door_L1", 0, 0)
	pSequence.AddAction(pDoorAction, pOpenEyes, 0.125)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "DBCommander2"))
	return pSequence	

def MoveFromC2ToC(pCharacter):
	debug(__name__ + ", MoveFromC2ToC")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_sit_c_m.NIF", "db_sit_c_m")

	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Sit = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_sit_c_m", 0, 0)
	pSequence.AddAction(pAnimAction_Sit, pOpenEyes)
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_SEATED)
	pSequence.AddCompletedEvent(pEvent)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "DBCommander"))
	return pSequence

####################################################
# E-Bridge Animations
####################################################

def EBPlaceAtH(pCharacter):
	debug(__name__ + ", EBPlaceAtH")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_stand_h_m.nif", "EB_stand_h_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "EB_stand_h_m")
	pSequence.AddAction(pAction)
	return pSequence

def EBPlaceAtL1(pCharacter):
	debug(__name__ + ", EBPlaceAtL1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_L1toX_M.nif", "EB_L1toX_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "EB_L1toX_M")
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def EBPlaceAtL2(pCharacter):
	debug(__name__ + ", EBPlaceAtL2")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_L2toG1_S.nif", "EB_L2toG1_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "EB_L2toG1_S")
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def EBPlaceAtL3(pCharacter):
	debug(__name__ + ", EBPlaceAtL3")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_L3toG3_S.nif", "EB_L3toG3_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "EB_L3toG3_S")
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def EBPlaceAtG1(pCharacter):
	debug(__name__ + ", EBPlaceAtG1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_G1toL2_S.nif", "EB_G1toL2_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "EB_G1toL2_S")
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def EBPlaceAtG2(pCharacter):
	debug(__name__ + ", EBPlaceAtG2")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_G2toL2_S.nif", "EB_G2toL2_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "EB_G2toL2_S")
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def EBPlaceAtG3(pCharacter):
	debug(__name__ + ", EBPlaceAtG3")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_G3toL1_S.nif", "EB_G3toL1_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "EB_G3toL1_S")
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def EBPlaceAtC(pCharacter):
	debug(__name__ + ", EBPlaceAtC")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_stand_c_m.nif", "EB_stand_c_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "EB_stand_c_m")
	pSequence.AddAction(pAction)
	return pSequence

def EBPlaceAtX(pCharacter):
	debug(__name__ + ", EBPlaceAtX")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_stand_X_m.nif", "EB_stand_X_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "EB_stand_X_m")
	pSequence.AddAction(pAction)
	return pSequence

def EBSeatedH(pCharacter):
	debug(__name__ + ", EBSeatedH")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_seated_h_m.nif", "EB_seated_h_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimAction_Create(pAnimNode, "EB_seated_h_m", 0, 0)
	pSequence.AddAction(pAction)
	return pSequence

def EBSeatedC(pCharacter):
	debug(__name__ + ", EBSeatedC")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_seated_c_m.nif", "EB_seated_c_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimAction_Create(pAnimNode, "EB_seated_c_m", 0, 0)
	pSequence.AddAction(pAction)
	return pSequence

def EBSeatedX(pCharacter):
	debug(__name__ + ", EBSeatedX")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_seated_X_m.nif", "EB_seated_X_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimAction_Create(pAnimNode, "EB_seated_X_m", 0, 0)
	pSequence.AddAction(pAction)
	return pSequence

def EBTurnAtC1TowardsCaptain(pCharacter):
	debug(__name__ + ", EBTurnAtC1TowardsCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_face_capt_c1.nif", "EB_face_capt_c1")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_face_capt_c1", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def EBTurnAtCTowardsCaptain(pCharacter):
	debug(__name__ + ", EBTurnAtCTowardsCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_face_capt_c.nif", "EB_face_capt_c")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_face_capt_c", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

	# Turn towards captain medium
def EBTurnAtHTowardsCaptain(pCharacter):
	debug(__name__ + ", EBTurnAtHTowardsCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_face_capt_h.nif", "EB_face_capt_h")
	kAM.LoadAnimation ("data/animations/EB_chair_H_face_capt.nif", "EB_chair_H_face_capt")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_face_capt_h", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	pAction = App.TGAnimAction_Create(pBridgeNode, "EB_chair_H_face_capt", 0, 0)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def EBTurnAtXTowardsCaptain(pCharacter):
	debug(__name__ + ", EBTurnAtXTowardsCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_face_capt_X.nif", "EB_face_capt_X")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_face_capt_X", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def EBTurnBackAtCFromCaptain(pCharacter):
	debug(__name__ + ", EBTurnBackAtCFromCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_face_capt_C_reverse.NIF", "EB_face_capt_C_reverse")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_face_capt_C_reverse", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def EBTurnBackAtC1FromCaptain(pCharacter):
	debug(__name__ + ", EBTurnBackAtC1FromCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_face_capt_c1_reverse.NIF", "EB_face_capt_c1_reverse")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_face_capt_c1_reverse", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

	# Turn back from looking at captain medium
def EBTurnBackAtHFromCaptain(pCharacter):
	debug(__name__ + ", EBTurnBackAtHFromCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_face_capt_h_reverse.nif", "EB_face_capt_h_reverse")
	kAM.LoadAnimation ("data/animations/EB_chair_H_face_capt_reverse.nif", "EB_chair_H_face_capt_reverse")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_face_capt_h_reverse", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	pAction = App.TGAnimAction_Create(pBridgeNode, "EB_chair_H_face_capt_reverse", 0, 0)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def EBTurnBackAtXFromCaptain(pCharacter):
	debug(__name__ + ", EBTurnBackAtXFromCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_face_capt_X_reverse.NIF", "EB_face_capt_X_reverse")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_face_capt_X_reverse", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

	# L1 to C medium
def EBMoveFromL1ToC(pCharacter):
	debug(__name__ + ", EBMoveFromL1ToC")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_L1toC_m.nif", "EB_L1toC_m")
	kAM.LoadAnimation ("data/animations/EB_chair_C_in.nif", "EB_chair_C_in")
	kAM.LoadAnimation ("data/animations/EB_sit_C_m.nif", "EB_sit_C_m")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_WalkFromLift = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_L1toC_m", 0, 0, 1)
	pSequence.AddAction(pAnimAction_WalkFromLift, pOpenEyes)
	pDoorAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "LiftDoorAction", pBridge, "EB_Door_L1", "LiftDoor")

	pSequence.AddAction(pDoorAction, pOpenEyes, 0.125)
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_chair_C_in", 0, 0)
	pSequence.AddAction(pAnimAction, pAnimAction_WalkFromLift)
	pSitAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_sit_C_m", 0, 0)
	pSequence.AddAction(pSitAction, pAnimAction_WalkFromLift)
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_SEATED)
	pSequence.AddCompletedEvent(pEvent)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBCommander"))
	return pSequence	

	# L1 to H medium
def EBMoveFromL1ToH(pCharacter):
	debug(__name__ + ", EBMoveFromL1ToH")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_L1toH_m.nif", "EB_L1toH_m")
	kAM.LoadAnimation ("data/animations/EB_sit_H_m.nif", "EB_sit_h_m")
	kAM.LoadAnimation ("data/animations/EB_chair_H_in.nif", "EB_chair_H_in")
	kAM.LoadAnimation ("data/animations/EB_door_l1.nif", "EB_Door_L1")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	fTime = 0.0
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_WalkFromLift = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_L1toH_m", 0, 0, 1)
	pSequence.AddAction(pAnimAction_WalkFromLift, pOpenEyes)
	fTime = kAM.GetAnimationLength("EB_L1toH_m")
	pDoorAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "LiftDoorAction", pBridge, "EB_Door_L1", "LiftDoor")

	pSequence.AddAction(pDoorAction, pOpenEyes, 0.125)
	pAnimAction_Sit = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_sit_h_m", 0, 0)
	pSequence.AddAction(pAnimAction_Sit, pAnimAction_WalkFromLift)
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_chair_H_in", 0, 0)
	pSequence.AddAction(pAnimAction, pAnimAction_WalkFromLift)
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination (pCharacter)
	pEvent.SetInt (App.CharacterClass.CS_SEATED)
	pSequence.AddCompletedEvent(pEvent)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBHelm"))
	return pSequence

def EBMoveFromL1ToX(pCharacter):
	debug(__name__ + ", EBMoveFromL1ToX")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_L1toX_m.nif", "EB_L1toX_m")
	kAM.LoadAnimation ("data/animations/EB_sit_X_m.nif", "EB_sit_X_m")
	kAM.LoadAnimation ("data/animations/EB_chair_X_in.nif", "EB_chair_X_in")
	kAM.LoadAnimation ("data/animations/EB_door_l1.nif", "EB_Door_L1")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	fTime = 0.0
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_WalkFromLift = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_L1toX_m", 0, 0, 1)
	pSequence.AddAction(pAnimAction_WalkFromLift, pOpenEyes)
	fTime = kAM.GetAnimationLength("EB_L1toX_m")
	pDoorAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "LiftDoorAction", pBridge, "EB_Door_L1", "LiftDoor")
	pSequence.AddAction(pDoorAction, pOpenEyes, 0.125)
	pAnimAction_Sit = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_sit_X_m", 0, 0)
	pSequence.AddAction(pAnimAction_Sit, pAnimAction_WalkFromLift)
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_chair_X_in", 0, 0)
	pSequence.AddAction(pAnimAction, pAnimAction_WalkFromLift)
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination (pCharacter)
	pEvent.SetInt (App.CharacterClass.CS_SEATED)
	pSequence.AddCompletedEvent(pEvent)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBGuest"))
	return pSequence

def EBMoveFromL1ToX2(pCharacter):
	debug(__name__ + ", EBMoveFromL1ToX2")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_L1toX2_m.nif", "EB_L1toX2_m")
	kAM.LoadAnimation ("data/animations/EB_door_l1.nif", "EB_Door_L1")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	fTime = 0.0
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_WalkFromLift = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_L1toX2_m", 0, 0, 1)
	pSequence.AddAction(pAnimAction_WalkFromLift, pOpenEyes)
	fTime = kAM.GetAnimationLength("EB_L1toX2_m")
	pDoorAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "LiftDoorAction", pBridge, "EB_Door_L1", "LiftDoor")
	pSequence.AddAction(pDoorAction, pOpenEyes, 0.125)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBGuest2"))
	return pSequence

def EBMoveFromX2ToX(pCharacter):
	debug(__name__ + ", EBMoveFromX2ToX")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_X2toX_m.nif", "EB_X2toX_m")
	kAM.LoadAnimation ("data/animations/EB_chair_X_in.nif", "EB_chair_X_in")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_WalkFromLift = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_X2toX_m", 0, 0, 1)
	pSequence.AddAction(pAnimAction_WalkFromLift, pOpenEyes)
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_chair_X_in", 0, 0)
	fTime = kAM.GetAnimationLength("EB_X2toX_m") - kAM.GetAnimationLength("ET_chair_X_in") - 1.75
	pSequence.AddAction(pAnimAction, pOpenEyes, fTime)
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination (pCharacter)
	pEvent.SetInt (App.CharacterClass.CS_SEATED)
	pSequence.AddCompletedEvent(pEvent)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBGuest"))
	return pSequence

def EBMoveFromCToL1(pCharacter):
	debug(__name__ + ", EBMoveFromCToL1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_stand_c_m.nif", "EB_stand_c_m")
	kAM.LoadAnimation ("data/animations/EB_CtoL1_m.nif", "EB_CtoL1_m")
	kAM.LoadAnimation ("data/animations/EB_chair_C_out.nif", "EB_chair_C_out")
	kAM.LoadAnimation ("data/animations/EB_door_l1.nif", "EB_Door_L1")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Stand = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_stand_c_m", 0, 0, 1)
	pSequence.AddAction(pAnimAction_Stand, pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pBridgeNode, "EB_chair_C_out", 0, 0), pOpenEyes)
	pAnimAction_WalkToLift = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_CtoL1_m", 0, 0)
	pSequence.AddAction(pAnimAction_WalkToLift, pAnimAction_Stand)
	fTime = kAM.GetAnimationLength("EB_CtoL1_m")
#	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_Door_L1", 0, 0)
#	pSequence.AddAction(pAnimAction, pAnimAction_Stand, fTime - 1.5)

	pDoorAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "LiftDoorAction", pBridge, "EB_Door_L1", "LiftDoor")
	pSequence.AddAction(pDoorAction, pAnimAction_Stand, fTime - 1.5)

	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBL1M"))
	pEvent = App.TGIntEvent_Create()		# Add event to hide character after it gets into the turbolift
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_HIDDEN)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence

	# From chair to L1 medium
def EBMoveFromHToL1(pCharacter):
	debug(__name__ + ", EBMoveFromHToL1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_stand_h_m.nif", "EB_stand_h_m")
	kAM.LoadAnimation ("data/animations/EB_chair_H_out.nif", "EB_chair_H_out")
	kAM.LoadAnimation ("data/animations/EB_HtoL1_m.nif", "EB_HtoL1_m")
	kAM.LoadAnimation ("data/animations/EB_door_l1.nif", "EB_Door_L1")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Stand = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_stand_h_m", 0, 0, 1)
	pSequence.AddAction(pAnimAction_Stand, pOpenEyes)
	pSequence.AddAction(Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter), pAnimAction_Stand, 0.0)
	pSequence.AddAction(App.TGAnimAction_Create(pBridgeNode, "EB_chair_H_out", 0, 0), pOpenEyes)
	pAnimAction_WalkToLift = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_HtoL1_m", 0, 0)
	pSequence.AddAction(pAnimAction_WalkToLift, pAnimAction_Stand, 0.0)
	fTime = kAM.GetAnimationLength("EB_HtoL1_m")
#	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_Door_L1", 0, 0)
#	pSequence.AddAction(pAnimAction, pAnimAction_Stand, fTime - 1.7)	

	pDoorAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "LiftDoorAction", pBridge, "EB_Door_L1", "LiftDoor")
	pSequence.AddAction(pDoorAction, pAnimAction_Stand, fTime - 1.7)

	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBL1M"))
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_HIDDEN)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence

def EBMoveFromXToL1(pCharacter):
	debug(__name__ + ", EBMoveFromXToL1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_stand_X_m.nif", "EB_stand_X_m")
	kAM.LoadAnimation ("data/animations/EB_chair_X_out.nif", "EB_chair_X_out")
	kAM.LoadAnimation ("data/animations/EB_XtoL1_m.nif", "EB_XtoL1_m")
	kAM.LoadAnimation ("data/animations/EB_door_l1.nif", "EB_Door_L1")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Stand = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_stand_X_m", 0, 0, 1)
	pSequence.AddAction(pAnimAction_Stand, pOpenEyes)
	pSequence.AddAction(Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter), pAnimAction_Stand, 0.0)
	pSequence.AddAction(App.TGAnimAction_Create(pBridgeNode, "EB_chair_X_out", 0, 0), pOpenEyes)
	pAnimAction_WalkToLift = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_XtoL1_m", 0, 0)
	pSequence.AddAction(pAnimAction_WalkToLift, pAnimAction_Stand, 0.0)
	fTime = kAM.GetAnimationLength("EB_XtoL1_m")
#	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_Door_L1", 0, 0)
#	pSequence.AddAction(pAnimAction, pAnimAction_Stand, fTime - 1.7)	

	pDoorAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "LiftDoorAction", pBridge, "EB_Door_L1", "LiftDoor")
	pSequence.AddAction(pDoorAction, pAnimAction_Stand, fTime - 1.7)

	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBL1M"))
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_HIDDEN)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence

def EBMoveFromCToC1(pCharacter):
	debug(__name__ + ", EBMoveFromCToC1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_stand_c_m.NIF", "EB_stand_c_m")
	kAM.LoadAnimation ("data/animations/EB_CtoC1_M.NIF", "EB_CtoC1_M")
	kAM.LoadAnimation ("data/animations/EB_chair_C_out.nif", "EB_chair_C_out")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Stand = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_stand_c_m", 0, 0, 1)
	pSequence.AddAction(pAnimAction_Stand, pOpenEyes)
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_chair_C_out", 0, 0)
	pSequence.AddAction(pAnimAction, pOpenEyes)
	pAnimAction_Walk = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_CtoC1_M", 0, 0)
	pSequence.AddAction(pAnimAction_Walk, pAnimAction_Stand, 0.0)
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_STANDING)
	pSequence.AddCompletedEvent(pEvent)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBCommander1"))
	return pSequence

def EBMoveFromC1ToC(pCharacter):
	debug(__name__ + ", EBMoveFromC1ToC")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_sit_c_m.NIF", "EB_sit_c_m")
	kAM.LoadAnimation ("data/animations/EB_C1toC_M.NIF", "EB_C1toC_M")
	kAM.LoadAnimation ("data/animations/EB_chair_C_in.nif", "EB_chair_C_in")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Walk = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_C1toC_M", 0, 0, 1)
	pSequence.AddAction(pAnimAction_Walk, pOpenEyes)
	pAnimAction_Sit = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_sit_c_m", 0, 0)
	pSequence.AddAction(pAnimAction_Sit, pAnimAction_Walk)
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_chair_C_in", 0, 0)
	pSequence.AddAction(pAnimAction, pAnimAction_Walk)
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_SEATED)
	pSequence.AddCompletedEvent(pEvent)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBCommander"))
	return pSequence


def EBMoveFromXToX1(pCharacter):
	debug(__name__ + ", EBMoveFromXToX1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_stand_x_m.NIF", "EB_stand_x_m")
	kAM.LoadAnimation ("data/animations/EB_XtoX1_M.NIF", "EB_XtoX1_M")
	kAM.LoadAnimation ("data/animations/EB_chair_X_out.nif", "EB_chair_X_out")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Stand = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_stand_x_m", 0, 0, 1)
	pSequence.AddAction(pAnimAction_Stand, pOpenEyes)
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_chair_X_out", 0, 0)
	pSequence.AddAction(pAnimAction, pOpenEyes)
	pAnimAction_Walk = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_XtoX1_M", 0, 0)
	pSequence.AddAction(pAnimAction_Walk, pAnimAction_Stand, 0.0)
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_STANDING)
	pSequence.AddCompletedEvent(pEvent)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBGuest1"))
	return pSequence

def EBMoveFromX1ToX(pCharacter):
	debug(__name__ + ", EBMoveFromX1ToX")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_sit_x_m.NIF", "EB_sit_x_m")
	kAM.LoadAnimation ("data/animations/EB_X1toX_M.NIF", "EB_X1toX_M")
	kAM.LoadAnimation ("data/animations/EB_chair_X_in.nif", "EB_chair_X_in")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Walk = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_X1toX_M", 0, 0, 1)
	pSequence.AddAction(pAnimAction_Walk, pOpenEyes)
	pAnimAction_Sit = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_sit_x_m", 0, 0)
	pSequence.AddAction(pAnimAction_Sit, pAnimAction_Walk)
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_chair_X_in", 0, 0)
	pSequence.AddAction(pAnimAction, pAnimAction_Walk)
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_SEATED)
	pSequence.AddCompletedEvent(pEvent)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBGuest"))
	return pSequence

def EBL2ToG1(pCharacter):
	debug(__name__ + ", EBL2ToG1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_L2toG1_M.nif", "EB_L2toG1_M")
	kAM.LoadAnimation ("data/animations/EB_Door_L2.nif", "EB_Door_L2")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pCharacter.SetHidden(0)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_L2toG1_M", 0, 0, 1)
	pSequence.AddAction(pAnimAction1)#, pOpenEyes)
	pDoorAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "LiftDoorAction", pBridge, "EB_Door_L2", "LiftDoor")
	pSequence.AddAction(pDoorAction, pOpenEyes, 0.125)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBG1M"))
	return pSequence

def EBG1ToL2(pCharacter):
	debug(__name__ + ", EBG1ToL2")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_G1toL2_M.nif", "EB_G1toL2_M")
	kAM.LoadAnimation ("data/animations/EB_Door_L2.nif", "EB_Door_L2")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_G1toL2_M", 0, 0, 1)
	pSequence.AddAction(pAnimAction, pOpenEyes)
	fTime = kAM.GetAnimationLength("EB_G1toL2_M")
	pDoorAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "LiftDoorAction", pBridge, "EB_Door_L2", "LiftDoor")
	pSequence.AddAction(pDoorAction, pOpenEyes, fTime - 2.5)
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_HIDDEN)
	pSequence.AddCompletedEvent(pEvent)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBL2M"))
	return pSequence

def EBL2ToG2(pCharacter):
	debug(__name__ + ", EBL2ToG2")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_L2toG2_M.nif", "EB_L2toG2_M")
	kAM.LoadAnimation ("data/animations/EB_Door_L2.nif", "EB_Door_L2")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pCharacter.SetHidden(0)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_L2toG2_M", 0, 0, 1)
	pSequence.AddAction(pAnimAction1, pOpenEyes)
	pDoorAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "LiftDoorAction", pBridge, "EB_Door_L2", "LiftDoor")
	pSequence.AddAction(pDoorAction, pOpenEyes, 0.125)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBG2M"))
	return pSequence

def EBG2ToL2(pCharacter):
	debug(__name__ + ", EBG2ToL2")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_G2toL2_M.nif", "EB_G2toL2_M")
	kAM.LoadAnimation ("data/animations/EB_Door_L2.nif", "EB_Door_L2")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_G2toL2_M", 0, 0, 1)
	pSequence.AddAction(pAnimAction, pOpenEyes)
	fTime = kAM.GetAnimationLength("EB_G2toL2_M")
	pDoorAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "LiftDoorAction", pBridge, "EB_Door_L2", "LiftDoor")
	pSequence.AddAction(pDoorAction, pOpenEyes, fTime - 2.5)
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_HIDDEN)
	pSequence.AddCompletedEvent(pEvent)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBL2M"))
	return pSequence


def EBL1ToG3(pCharacter):
	debug(__name__ + ", EBL1ToG3")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_L1toG3_M.nif", "EB_L1toG3_M")
	kAM.LoadAnimation ("data/animations/EB_Door_L1.nif", "EB_Door_L1")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pCharacter.SetHidden(0)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_L1toG3_M", 0, 0, 1)
	pSequence.AddAction(pAnimAction1, pOpenEyes)
	pDoorAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "LiftDoorAction", pBridge, "EB_Door_L1", "LiftDoor")
	pSequence.AddAction(pDoorAction, pOpenEyes, 0.125)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBG3M"))
	return pSequence

def EBG3ToL1(pCharacter):
	debug(__name__ + ", EBG3ToL1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_G3toL1_M.nif", "EB_G3toL1_M")
	kAM.LoadAnimation ("data/animations/EB_Door_L1.nif", "EB_Door_L1")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_G3toL1_M", 0, 0, 1)
	pSequence.AddAction(pAnimAction, pOpenEyes)
	fTime = kAM.GetAnimationLength("EB_G3toL1_M")
	pDoorAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "LiftDoorAction", pBridge, "EB_Door_L1", "LiftDoor")
	pSequence.AddAction(pDoorAction, pOpenEyes, fTime - 2.5)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBL1M"))
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_HIDDEN)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence

def EBHHit(pCharacter):
	debug(__name__ + ", EBHHit")
	return None
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_hit_h.NIF", "EB_hit_h")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()

	# Lean
	pAction = App.TGAnimAction_Create(pAnimNode, "EB_hit_h", 0, 0, 1)
	pSequence.AddAction(pAction)

	# open eyes and close mouth
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes, pAction)

#	if (App.g_kSystemWrapper.GetRandomNumber(5) == 3):
#		if (pCharacter.GetGender() == 0):
#			pSequence.AddAction(App.TGSoundAction_Create("MaleEek"+ str(App.g_kSystemWrapper.GetRandomNumber(7)+1)))
#		else:
#			pSequence.AddAction(App.TGSoundAction_Create("FemaleEek"+ str(App.g_kSystemWrapper.GetRandomNumber(7)+1)))

	return pSequence

	# lean hard left animation
def EBHHitHard(pCharacter):
	debug(__name__ + ", EBHHitHard")
	return NebHHit (pCharacter)
########################################################################################################################


	# lean left animation
def EBCHit (pCharacter):
	debug(__name__ + ", EBCHit")
	return None
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_hit_c.NIF", "EB_hit_c")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()

	# Lean
	pLeanAction = App.TGAnimAction_Create(pAnimNode, "EB_hit_c", 0, 0, 1)
	pSequence.AddAction(pLeanAction)

	# open eyes and close mouth
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)

	# Return to default.
	pAction = App.CharacterAction_Create (pCharacter, App.CharacterAction.AT_DEFAULT);
	pSequence.AddAction (pAction, pLeanAction)

#	if (App.g_kSystemWrapper.GetRandomNumber(5) == 3):
#		if (pCharacter.GetGender() == 0):
#			pSequence.AddAction(App.TGSoundAction_Create("MaleEek"+ str(App.g_kSystemWrapper.GetRandomNumber(7)+1)))
#		else:
#			pSequence.AddAction(App.TGSoundAction_Create("FemaleEek"+ str(App.g_kSystemWrapper.GetRandomNumber(7)+1)))

	return pSequence

	# lean hard left animation
def EBCHitHard(pCharacter):
	debug(__name__ + ", EBCHitHard")
	return NebCHit (pCharacter)

def EBXHit (pCharacter):
	debug(__name__ + ", EBXHit")
	return None
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_hit_x.NIF", "EB_hit_x")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()

	# Lean
	pLeanAction = App.TGAnimAction_Create(pAnimNode, "EB_hit_x", 0, 0, 1)
	pSequence.AddAction(pLeanAction)

	# open eyes and close mouth
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)

	# Return to default.
	pAction = App.CharacterAction_Create (pCharacter, App.CharacterAction.AT_DEFAULT);
	pSequence.AddAction (pAction, pLeanAction)

	return pSequence

	# lean hard left animation
def EBXHitHard(pCharacter):
	debug(__name__ + ", EBXHitHard")
	return NebXHit (pCharacter)
####################################################
# Neb-Bridge Animations
####################################################

def NebPlaceAtH(pCharacter):
	debug(__name__ + ", NebPlaceAtH")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/Neb_stand_h_m.nif", "Neb_stand_h_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "Neb_stand_h_m")
	pSequence.AddAction(pAction)
	return pSequence


def NebPlaceAtC(pCharacter):
	debug(__name__ + ", NebPlaceAtC")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/Neb_stand_c_m.nif", "Neb_stand_c_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "Neb_stand_c_m")
	pSequence.AddAction(pAction)
	return pSequence

def NebPlaceAtX(pCharacter):
	debug(__name__ + ", NebPlaceAtX")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/Neb_stand_X_m.nif", "Neb_stand_X_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "EB_stand_X_m")
	pSequence.AddAction(pAction)
	return pSequence

def NebSeatedH(pCharacter):
	debug(__name__ + ", NebSeatedH")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/Neb_seated_h_m.nif", "Neb_seated_h_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimAction_Create(pAnimNode, "Neb_seated_h_m", 0, 0)
	pSequence.AddAction(pAction)
	return pSequence

def NebSeatedC(pCharacter):
	debug(__name__ + ", NebSeatedC")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/Neb_seated_c_m.nif", "Neb_seated_c_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimAction_Create(pAnimNode, "Neb_seated_c_m", 0, 0)
	pSequence.AddAction(pAction)
	return pSequence

def NebSeatedX(pCharacter):
	debug(__name__ + ", NebSeatedX")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/Neb_seated_X_m.nif", "Neb_seated_X_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimAction_Create(pAnimNode, "Neb_seated_X_m", 0, 0)
	pSequence.AddAction(pAction)
	return pSequence

def NEbTurnAtC1TowardsCaptain(pCharacter):
	debug(__name__ + ", NEbTurnAtC1TowardsCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/Neb_face_capt_c1.nif", "Neb_face_capt_c1")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "Neb_face_capt_c1", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def NebTurnAtCTowardsCaptain(pCharacter):
	debug(__name__ + ", NebTurnAtCTowardsCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/Neb_face_capt_c.nif", "Neb_face_capt_c")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "Neb_face_capt_c", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def NebTurnAtHTowardsCaptain(pCharacter):
	debug(__name__ + ", NebTurnAtHTowardsCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/Neb_face_capt_h.nif", "Neb_face_capt_h")
	kAM.LoadAnimation ("data/animations/Neb_chair_H_face_capt.nif", "Neb_chair_H_face_capt")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "Neb_face_capt_h", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	pAction = App.TGAnimAction_Create(pBridgeNode, "Neb_chair_H_face_capt", 0, 0)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def NebTurnAtXTowardsCaptain(pCharacter):
	debug(__name__ + ", NebTurnAtXTowardsCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/Neb_face_capt_X.nif", "Neb_face_capt_X")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "Neb_face_capt_X", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def NebTurnBackAtCFromCaptain(pCharacter):
	debug(__name__ + ", NebTurnBackAtCFromCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/Neb_face_capt_C_reverse.NIF", "Neb_face_capt_C_reverse")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "Neb_face_capt_C_reverse", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def NebTurnBackAtC1FromCaptain(pCharacter):
	debug(__name__ + ", NebTurnBackAtC1FromCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/Neb_face_capt_c1_reverse.NIF", "Neb_face_capt_c1_reverse")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "Neb_face_capt_c1_reverse", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

	# Turn back from looking at captain medium
def NebTurnBackAtHFromCaptain(pCharacter):
	debug(__name__ + ", NebTurnBackAtHFromCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/Neb_face_capt_h_reverse.nif", "Neb_face_capt_h_reverse")
	kAM.LoadAnimation ("data/animations/Neb_chair_H_face_capt_reverse.nif", "Neb_chair_H_face_capt_reverse")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "Neb_face_capt_h_reverse", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	pAction = App.TGAnimAction_Create(pBridgeNode, "Neb_chair_H_face_capt_reverse", 0, 0)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def NebTurnBackAtXFromCaptain(pCharacter):
	debug(__name__ + ", NebTurnBackAtXFromCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/Neb_face_capt_X_reverse.NIF", "Neb_face_capt_X_reverse")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "Neb_face_capt_X_reverse", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

#def EBMoveFromCToC1(pCharacter):
#	kAM = App.g_kAnimationManager
#	kAM.LoadAnimation ("data/animations/EB_stand_c_m.NIF", "EB_stand_c_m")
#	kAM.LoadAnimation ("data/animations/EB_CtoC1_M.NIF", "EB_CtoC1_M")
#	kAM.LoadAnimation ("data/animations/EB_chair_C_out.nif", "EB_chair_C_out")
#	pSet = App.g_kSetManager.GetSet("bridge")
#	pBridge = pSet.GetObject("bridge")
#	pBridgeNode = pBridge.GetAnimNode()
#	pCharacter = App.CharacterClass_Cast(pCharacter)
#	pSequence = App.TGSequence_Create()
#	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
#	pSequence.AddAction(pOpenEyes)
#	pAnimAction_Stand = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_stand_c_m", 0, 0, 1)
#	pSequence.AddAction(pAnimAction_Stand, pOpenEyes)
#	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_chair_C_out", 0, 0)
#	pSequence.AddAction(pAnimAction, pOpenEyes)
#	pAnimAction_Walk = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_CtoC1_M", 0, 0)
#	pSequence.AddAction(pAnimAction_Walk, pAnimAction_Stand, 0.0)
#	pEvent = App.TGIntEvent_Create()
#	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
#	pEvent.SetDestination(pCharacter)
#	pEvent.SetInt(App.CharacterClass.CS_STANDING)
#	pSequence.AddCompletedEvent(pEvent)
#	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBCommander1"))
#	return pSequence

#def EBMoveFromXToX1(pCharacter):
#	kAM = App.g_kAnimationManager
#	kAM.LoadAnimation ("data/animations/EB_stand_x_m.NIF", "EB_stand_x_m")
#	kAM.LoadAnimation ("data/animations/EB_XtoX1_M.NIF", "EB_XtoX1_M")
#	kAM.LoadAnimation ("data/animations/EB_chair_X_out.nif", "EB_chair_X_out")
#	pSet = App.g_kSetManager.GetSet("bridge")
#	pBridge = pSet.GetObject("bridge")
#	pBridgeNode = pBridge.GetAnimNode()
#	pCharacter = App.CharacterClass_Cast(pCharacter)
#	pSequence = App.TGSequence_Create()
#	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
#	pSequence.AddAction(pOpenEyes)
#	pAnimAction_Stand = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_stand_x_m", 0, 0, 1)
#	pSequence.AddAction(pAnimAction_Stand, pOpenEyes)
#	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_chair_X_out", 0, 0)
#	pSequence.AddAction(pAnimAction, pOpenEyes)
#	pAnimAction_Walk = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_XtoX1_M", 0, 0)
#	pSequence.AddAction(pAnimAction_Walk, pAnimAction_Stand, 0.0)
#	pEvent = App.TGIntEvent_Create()
#	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
#	pEvent.SetDestination(pCharacter)
#	pEvent.SetInt(App.CharacterClass.CS_STANDING)
#	pSequence.AddCompletedEvent(pEvent)
#	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBGuest1"))
#	return pSequence

def NebL2ToG1(pCharacter):
	debug(__name__ + ", NebL2ToG1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/Neb_L2toG1_M.nif", "Neb_L2toG1_M")
	kAM.LoadAnimation ("data/animations/Neb_Door_L2.nif", "Neb_Door_L2")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pCharacter.SetHidden(0)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "Neb_L2toG1_M", 0, 0, 1)
	pSequence.AddAction(pAnimAction1)#, pOpenEyes)
	pDoorAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "LiftDoorAction", pBridge, "Neb_Door_L2", "LiftDoor")
	pSequence.AddAction(pDoorAction, pOpenEyes, 0.125)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "NebG1M"))
	return pSequence

def NebG1ToL2(pCharacter):
	debug(__name__ + ", NebG1ToL2")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/Neb_G1toL2_M.nif", "Neb_G1toL2_M")
	kAM.LoadAnimation ("data/animations/Neb_Door_L2.nif", "Neb_Door_L2")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "Neb_G1toL2_M", 0, 0, 1)
	pSequence.AddAction(pAnimAction, pOpenEyes)
	fTime = kAM.GetAnimationLength("Neb_G1toL2_M")
	pDoorAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "LiftDoorAction", pBridge, "Neb_Door_L2", "LiftDoor")
	pSequence.AddAction(pDoorAction, pOpenEyes, fTime - 2.5)
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_HIDDEN)
	pSequence.AddCompletedEvent(pEvent)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "NebL2M"))
	return pSequence

def NebL2ToG2(pCharacter):
	debug(__name__ + ", NebL2ToG2")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/Neb_L2toG2_M.nif", "Neb_L2toG2_M")
	kAM.LoadAnimation ("data/animations/Neb_Door_L2.nif", "Neb_Door_L2")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pCharacter.SetHidden(0)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "Neb_L2toG2_M", 0, 0, 1)
	pSequence.AddAction(pAnimAction1, pOpenEyes)
	pDoorAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "LiftDoorAction", pBridge, "Neb_Door_L2", "LiftDoor")
	pSequence.AddAction(pDoorAction, pOpenEyes, 0.125)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "NebG2M"))
	return pSequence

def NebG2ToL2(pCharacter):
	debug(__name__ + ", NebG2ToL2")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/Neb_G2toL2_M.nif", "Neb_G2toL2_M")
	kAM.LoadAnimation ("data/animations/Neb_Door_L2.nif", "Neb_Door_L2")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "Neb_G2toL2_M", 0, 0, 1)
	pSequence.AddAction(pAnimAction, pOpenEyes)
	fTime = kAM.GetAnimationLength("Neb_G2toL2_M")
	pDoorAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "LiftDoorAction", pBridge, "Neb_Door_L2", "LiftDoor")
	pSequence.AddAction(pDoorAction, pOpenEyes, fTime - 2.5)
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_HIDDEN)
	pSequence.AddCompletedEvent(pEvent)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "NebL2M"))
	return pSequence


def NebL1ToG3(pCharacter):
	debug(__name__ + ", NebL1ToG3")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/Neb_L1toG3_M.nif", "Neb_L1toG3_M")
	kAM.LoadAnimation ("data/animations/Neb_Door_L1.nif", "Neb_Door_L1")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pCharacter.SetHidden(0)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "Neb_L1toG3_M", 0, 0, 1)
	pSequence.AddAction(pAnimAction1, pOpenEyes)
	pDoorAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "LiftDoorAction", pBridge, "Neb_Door_L1", "LiftDoor")
	pSequence.AddAction(pDoorAction, pOpenEyes, 0.125)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "NebG3M"))
	return pSequence

def NebG3ToL1(pCharacter):
	debug(__name__ + ", NebG3ToL1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/Neb_G3toL1_M.nif", "Neb_G3toL1_M")
	kAM.LoadAnimation ("data/animations/Neb_Door_L1.nif", "Neb_Door_L1")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "Neb_G3toL1_M", 0, 0, 1)
	pSequence.AddAction(pAnimAction, pOpenEyes)
	fTime = kAM.GetAnimationLength("Neb_G3toL1_M")
	pDoorAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "LiftDoorAction", pBridge, "Neb_Door_L1", "LiftDoor")
	pSequence.AddAction(pDoorAction, pOpenEyes, fTime - 2.5)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "NebL1M"))
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_HIDDEN)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence

######################################################
def NebHHit(pCharacter):
	debug(__name__ + ", NebHHit")
	return None
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_hit_h.NIF", "Neb_hit_h")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()

	# Lean
	pAction = App.TGAnimAction_Create(pAnimNode, "Neb_hit_h", 0, 0, 1)
	pSequence.AddAction(pAction)

	# open eyes and close mouth
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes, pAction)

#	if (App.g_kSystemWrapper.GetRandomNumber(5) == 3):
#		if (pCharacter.GetGender() == 0):
#			pSequence.AddAction(App.TGSoundAction_Create("MaleEek"+ str(App.g_kSystemWrapper.GetRandomNumber(7)+1)))
#		else:
#			pSequence.AddAction(App.TGSoundAction_Create("FemaleEek"+ str(App.g_kSystemWrapper.GetRandomNumber(7)+1)))

	return pSequence
	# lean hard left animation
def NebHHitHard(pCharacter):
	debug(__name__ + ", NebHHitHard")
	return NebHHit (pCharacter)

	# lean left animation
def NebCHit (pCharacter):
	debug(__name__ + ", NebCHit")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_hit_c.NIF", "Neb_hit_c")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()

	# Lean
	pLeanAction = App.TGAnimAction_Create(pAnimNode, "Neb_hit_c", 0, 0)
	pSequence.AddAction(pLeanAction)

	# open eyes and close mouth
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)

	# Return to default.
	pAction = App.CharacterAction_Create (pCharacter, App.CharacterAction.AT_DEFAULT);
	pSequence.AddAction (pAction, pLeanAction)

#	if (App.g_kSystemWrapper.GetRandomNumber(5) == 3):
#		if (pCharacter.GetGender() == 0):
#			pSequence.AddAction(App.TGSoundAction_Create("MaleEek"+ str(App.g_kSystemWrapper.GetRandomNumber(7)+1)))
#		else:
#			pSequence.AddAction(App.TGSoundAction_Create("FemaleEek"+ str(App.g_kSystemWrapper.GetRandomNumber(7)+1)))

	return pSequence

	# lean hard left animation
def NebCHitHard(pCharacter):
	debug(__name__ + ", NebCHitHard")
	return NebCHit (pCharacter)


def NebXHit (pCharacter):
	debug(__name__ + ", NebXHit")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_hit_x.NIF", "Neb_hit_x")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()

	# Lean
	pLeanAction = App.TGAnimAction_Create(pAnimNode, "Neb_hit_x", 0, 0)
	pSequence.AddAction(pLeanAction)

	# open eyes and close mouth
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)

	# Return to default.
	pAction = App.CharacterAction_Create (pCharacter, App.CharacterAction.AT_DEFAULT);
	pSequence.AddAction (pAction, pLeanAction)

	return pSequence

	# lean hard left animation
def NebXHitHard(pCharacter):
	debug(__name__ + ", NebXHitHard")
	return NebXHit (pCharacter)
#########################################################################################################################

###############################################################################
#	HLookAroundConsoleDown, HConsoleInteraction
#	
#	Helm-specific definitions for these functions
#	
#	Args:	pCharacter		- the character to call on
#	
#	Return:	pSequence	- the created sequence
###############################################################################
def HLookAroundConsoleDown(pCharacter):
	debug(__name__ + ", HLookAroundConsoleDown")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	if not (pCharacter):
		return None

	# Look forward, fore right, and right
	iNumLooks = App.g_kSystemWrapper.GetRandomNumber(4)+2
	pSequence = App.TGSequence_Create()
	pLastAction = App.TGAction_CreateNull()

	for i in range (iNumLooks):
		iRandAction = App.g_kSystemWrapper.GetRandomNumber(4)

		if (iRandAction == 0):
			pNextAction = Bridge.Characters.CommonAnimations.ConsoleLookDown(pCharacter)
		elif (iRandAction == 1):
			pNextAction = Bridge.Characters.CommonAnimations.ConsoleLookDownForeLeft(pCharacter)
		elif (iRandAction == 2):
			pNextAction = Bridge.Characters.CommonAnimations.ConsoleLookDownForeRight(pCharacter)
		elif (iRandAction == 3):
			pNextAction = Bridge.Characters.CommonAnimations.ConsoleLookDownRight(pCharacter)

		pSequence.AddAction(pNextAction, pLastAction)
		pLastAction = pNextAction

	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_BREATHE))

	return pSequence


def DBHConsoleInteraction(pCharacter):
	debug(__name__ + ", DBHConsoleInteraction")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	if not (pCharacter):
		return None

	iNumPresses = App.g_kSystemWrapper.GetRandomNumber(6)+3
	pSequence = App.TGSequence_Create()
	pLastAction = App.TGAction_CreateNull()

	for i in range (iNumPresses):
		iRandAction = App.g_kSystemWrapper.GetRandomNumber(10)

		if (iRandAction == 0):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "DB_H", "A")
		elif (iRandAction == 1):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "DB_H", "B")
		elif (iRandAction == 2):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "DB_H", "C")
		elif (iRandAction == 3):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "DB_H", "D")
		elif (iRandAction == 4):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "DB_H", "E")
		elif (iRandAction == 5):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "DB_H", "F")
		elif (iRandAction == 6):
			pNextAction = Bridge.Characters.CommonAnimations.ConsoleSlide(pCharacter, "DB_H", "A")
		elif (iRandAction == 7):
			pNextAction = Bridge.Characters.CommonAnimations.ConsoleSlide(pCharacter, "DB_H", "B")
		elif (iRandAction == 8):
			pNextAction = Bridge.Characters.CommonAnimations.ConsoleSlide(pCharacter, "DB_H", "C")
		elif (iRandAction == 9):
			pNextAction = Bridge.Characters.CommonAnimations.ConsoleSlide(pCharacter, "DB_H", "D")

		pSequence.AddAction(pNextAction, pLastAction)
		pLastAction = pNextAction

	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_BREATHE))

	return pSequence


def NebHConsoleInteraction(pCharacter):
	debug(__name__ + ", NebHConsoleInteraction")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	if not (pCharacter):
		return None

	iNumPresses = App.g_kSystemWrapper.GetRandomNumber(6)+3
	pSequence = App.TGSequence_Create()
	pLastAction = App.TGAction_CreateNull()

	for i in range (iNumPresses):
		iRandAction = App.g_kSystemWrapper.GetRandomNumber(10)

		if (iRandAction == 0):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_H", "A")
		elif (iRandAction == 1):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_H", "B")
		elif (iRandAction == 2):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_H", "C")
		elif (iRandAction == 3):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_H", "D")
		elif (iRandAction == 4):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_H", "E")
		elif (iRandAction == 5):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_H", "F")
		elif (iRandAction == 6):
			pNextAction = Bridge.Characters.CommonAnimations.ConsoleSlide(pCharacter, "EB_H", "A")
		elif (iRandAction == 7):
			pNextAction = Bridge.Characters.CommonAnimations.ConsoleSlide(pCharacter, "EB_H", "B")
		elif (iRandAction == 8):
			pNextAction = Bridge.Characters.CommonAnimations.ConsoleSlide(pCharacter, "EB_H", "C")
		elif (iRandAction == 9):
			pNextAction = Bridge.Characters.CommonAnimations.ConsoleSlide(pCharacter, "EB_H", "D")

		pSequence.AddAction(pNextAction, pLastAction)
		pLastAction = pNextAction

	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_BREATHE))

	return pSequence


###############################################################################
#	CLookAroundConsoleDown, CConsoleInteraction
#	
#	XO-specific definitions for these functions
#	
#	Args:	pCharacter		- the character to call on
#	
#	Return:	pSequence	- the created sequence
###############################################################################
def CLookAroundConsoleDown(pCharacter):
	debug(__name__ + ", CLookAroundConsoleDown")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	if not (pCharacter):
		return None

	# Look forward, fore right, and right
	iNumLooks = App.g_kSystemWrapper.GetRandomNumber(4)+2
	pSequence = App.TGSequence_Create()
	pLastAction = App.TGAction_CreateNull()

	for i in range (iNumLooks):
		iRandAction = App.g_kSystemWrapper.GetRandomNumber(3)

		if (iRandAction == 0):
			pNextAction = Bridge.Characters.CommonAnimations.ConsoleLookDown(pCharacter)
		elif (iRandAction == 1):
			pNextAction = Bridge.Characters.CommonAnimations.ConsoleLookDownForeRight(pCharacter)
		elif (iRandAction == 2):
			pNextAction = Bridge.Characters.CommonAnimations.ConsoleLookDownRight(pCharacter)

		pSequence.AddAction(pNextAction, pLastAction)
		pLastAction = pNextAction

	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_BREATHE))

	return pSequence


def DBCConsoleInteraction(pCharacter):
	debug(__name__ + ", DBCConsoleInteraction")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	if not (pCharacter):
		return None

	pSequence = App.TGSequence_Create()

	pSequence.AppendAction(App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_C_pushingbuttons_A", 0, 0))
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_BREATHE))

	return pSequence

def NebCConsoleInteraction(pCharacter):
	debug(__name__ + ", NebCConsoleInteraction")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	if not (pCharacter):
		return None

	iNumPresses = App.g_kSystemWrapper.GetRandomNumber(6)+3
	pSequence = App.TGSequence_Create()
	pLastAction = App.TGAction_CreateNull()

	for i in range (iNumPresses):
		iRandAction = App.g_kSystemWrapper.GetRandomNumber(7)

		if (iRandAction == 0):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_C", "A")
		elif (iRandAction == 1):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_C", "B")
		elif (iRandAction == 2):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_C", "C")
		elif (iRandAction == 3):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_C", "D")
		elif (iRandAction == 4):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_C", "E")
		elif (iRandAction == 5):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_C", "F")
		elif (iRandAction == 6):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_C", "G")

		pSequence.AddAction(pNextAction, pLastAction)
		pLastAction = pNextAction

	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_BREATHE))

	return pSequence


def DBXConsoleInteraction(pCharacter):
	debug(__name__ + ", DBXConsoleInteraction")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	if not (pCharacter):
		return None

	iNumPresses = App.g_kSystemWrapper.GetRandomNumber(6)+3
	pSequence = App.TGSequence_Create()
	pLastAction = App.TGAction_CreateNull()

	for i in range (iNumPresses):
		iRandAction = App.g_kSystemWrapper.GetRandomNumber(7)

		if (iRandAction == 0):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_X", "A")
		elif (iRandAction == 1):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_X", "B")
		elif (iRandAction == 2):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_X", "C")
		elif (iRandAction == 3):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_X", "D")
		elif (iRandAction == 4):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_X", "E")
		elif (iRandAction == 5):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_X", "F")
		elif (iRandAction == 6):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_X", "G")

		pSequence.AddAction(pNextAction, pLastAction)
		pLastAction = pNextAction

	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_BREATHE))

	return pSequence

def NebXConsoleInteraction(pCharacter):
	debug(__name__ + ", NebXConsoleInteraction")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	if not (pCharacter):
		return None

	iNumPresses = App.g_kSystemWrapper.GetRandomNumber(6)+3
	pSequence = App.TGSequence_Create()
	pLastAction = App.TGAction_CreateNull()

	for i in range (iNumPresses):
		iRandAction = App.g_kSystemWrapper.GetRandomNumber(7)

		if (iRandAction == 0):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_X", "A")
		elif (iRandAction == 1):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_X", "B")
		elif (iRandAction == 2):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_X", "C")
		elif (iRandAction == 3):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_X", "D")
		elif (iRandAction == 4):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_X", "E")
		elif (iRandAction == 5):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_X", "F")
		elif (iRandAction == 6):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_X", "G")

		pSequence.AddAction(pNextAction, pLastAction)
		pLastAction = pNextAction

	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_BREATHE))

	return pSequence

# nebula standing animation
def NebStanding(pCharacter):
	debug(__name__ + ", NebStanding")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/Neb_stand_C_M.NIF", "NebStanding")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimAction_Create(pAnimNode, "NebStanding", 0, 0)
	pSequence.AddAction(pAction)
	return pSequence

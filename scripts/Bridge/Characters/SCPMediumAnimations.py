# MediumAnimations.py
# This file includes all animations shared by medium characters

import App
import Bridge.Characters.CommonAnimations

########################################################################################################################
####################################################
# D-Bridge Animations
####################################################
def PlaceAtH(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_stand_h_m.nif", "db_stand_h_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "db_stand_h_m")
	pSequence.AddAction(pAction)
	return pSequence

def PlaceAtL1(pCharacter):
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
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_stand_c_m.nif", "db_stand_c_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "db_stand_c_m")
	pSequence.AddAction(pAction)
	return pSequence

def PlaceAtC1(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_face_capt_c1.nif", "db_face_capt_c1")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "db_face_capt_c1")
	pSequence.AddAction(pAction)
	return pSequence

def SeatedH(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_seated_h_m.nif", "db_seated_h_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimAction_Create(pAnimNode, "db_seated_h_m", 0, 0)
	pSequence.AddAction(pAction)
	return pSequence

def SeatedC(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_seated_c_m.nif", "db_seated_c_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimAction_Create(pAnimNode, "db_seated_c_m", 0, 0)
	pSequence.AddAction(pAction)
	return pSequence

def TurnAtC1TowardsCaptain(pCharacter):
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
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_stand_h_m.nif", "EB_stand_h_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "EB_stand_h_m")
	pSequence.AddAction(pAction)
	return pSequence

def EBPlaceAtL1(pCharacter):
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
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_stand_c_m.nif", "EB_stand_c_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "EB_stand_c_m")
	pSequence.AddAction(pAction)
	return pSequence

def EBPlaceAtX(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_stand_X_m.nif", "EB_stand_X_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "EB_stand_X_m")
	pSequence.AddAction(pAction)
	return pSequence

def EBSeatedH(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_seated_h_m.nif", "EB_seated_h_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimAction_Create(pAnimNode, "EB_seated_h_m", 0, 0)
	pSequence.AddAction(pAction)
	return pSequence

def EBSeatedC(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_seated_c_m.nif", "EB_seated_c_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimAction_Create(pAnimNode, "EB_seated_c_m", 0, 0)
	pSequence.AddAction(pAction)
	return pSequence

def EBSeatedX(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_seated_X_m.nif", "EB_seated_X_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimAction_Create(pAnimNode, "EB_seated_X_m", 0, 0)
	pSequence.AddAction(pAction)
	return pSequence

def EBTurnAtC1TowardsCaptain(pCharacter):
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
	return HHit (pCharacter)
########################################################################################################################


	# lean left animation
def EBCHit (pCharacter):
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
	return CHit (pCharacter)

def EBXHit (pCharacter):
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
	return XHit (pCharacter)
####################################################
# Galor-Bridge Animations
####################################################
def SCPPlaceAtH(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_stand_h_m.NIF", "SCP_stand_h_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "SCP_stand_h_m")
	pSequence.AddAction(pAction)
	return pSequence


def SCPPlaceAtC(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_stand_c_m.nif", "SCP_stand_c_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "SCP_stand_c_m")
	pSequence.AddAction(pAction)
	return pSequence

def SCPseatedm(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_standm_c_m.nif", "SCP_standm_c_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "SCP_standm_c_m")
	pSequence.AddAction(pAction)
	return pSequence

def SCPPlaceAtX(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_stand_X_m.nif", "SCP_stand_X_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "SCP_stand_X_m")
	pSequence.AddAction(pAction)
	return pSequence

def SCPSeatedH(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_seated_h_m.nif", "SCP_seated_h_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimAction_Create(pAnimNode, "SCP_seated_h_m", 0, 0)
	pSequence.AddAction(pAction)
	return pSequence

def SCPSeatedC(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_seated_c_m.nif", "SCP_seated_c_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimAction_Create(pAnimNode, "SCP_seated_c_m", 0, 0)
	pSequence.AddAction(pAction)
	return pSequence

def SCPSeatedX(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_seated_X_m.nif", "SCP_seated_X_m")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimAction_Create(pAnimNode, "Neb_seated_X_m", 0, 0)
	pSequence.AddAction(pAction)
	return pSequence

def SCPTurnAtC1TowardsCaptain(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_face_capt_c.nif", "SCP_face_capt_c1")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "SCP_face_capt_c1", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def SCPTurnAtCTowardsCaptain(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_face_capt_C.nif", "SCP_face_capt_C")
	kAM.LoadAnimation ("data/animations/SCP_chair_C_face_capt.nif", "SCP_chair_C_face_capt")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "SCP_face_capt_C", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	pAction = App.TGAnimAction_Create(pBridgeNode, "SCP_chair_C_face_capt", 0, 0)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence


	# Turn towards captain medium
def SCPTurnAtHTowardsCaptain(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_face_capt_h.nif", "SCP_face_capt_h")
	kAM.LoadAnimation ("data/animations/SCP_chair_H_face_capt.nif", "SCP_chair_H_face_capt")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "SCP_face_capt_h", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	pAction = App.TGAnimAction_Create(pBridgeNode, "SCP_chair_H_face_capt", 0, 0)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def SCPTurnAtXTowardsCaptain(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_face_capt_X.nif", "SCP_face_capt_X")
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

	# Turn back from looking at captain medium
def SCPTurnBackAtCFromCaptain(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_face_capt_C_reverse.nif", "SCP_face_capt_C_reverse")
	kAM.LoadAnimation ("data/animations/SCP_chair_C_face_capt_reverse.nif", "SCP_chair_C_face_capt_reverse")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "SCP_face_capt_C_reverse", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	pAction = App.TGAnimAction_Create(pBridgeNode, "SCP_chair_C_face_capt_reverse", 0, 0)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def SCPTurnBackAtC1FromCaptain(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_face_capt_c_reverse.NIF", "SCP_face_capt_c1_reverse")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "SCP_face_capt_c1_reverse", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

	# Turn back from looking at captain medium
def SCPTurnBackAtHFromCaptain(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_face_capt_h_reverse.nif", "SCP_face_capt_h_reverse")
	kAM.LoadAnimation ("data/animations/SCP_chair_H_face_capt_reverse.nif", "SCP_chair_H_face_capt_reverse")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "SCP_face_capt_h_reverse", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	pAction = App.TGAnimAction_Create(pBridgeNode, "SCP_chair_H_face_capt_reverse", 0, 0)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def SCPTurnBackAtXFromCaptain(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_face_capt_X_reverse.NIF", "SCP_face_capt_X_reverse")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "SCP_face_capt_X_reverse", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence




def HHit(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_hit_h.NIF", "db_hit_h")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()

	# Lean
	pAction = App.TGAnimAction_Create(pAnimNode, "db_hit_h", 0, 0)
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
def HHitHard(pCharacter):
	return HHit (pCharacter)

	# lean left animation
def CHit (pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_hit_c.NIF", "db_hit_c")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()

	# Lean
	pLeanAction = App.TGAnimAction_Create(pAnimNode, "db_hit_c", 0, 0)
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
def CHitHard(pCharacter):
	return CHit (pCharacter)


def XHit (pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_hit_x.NIF", "db_hit_x")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()

	# Lean
	pLeanAction = App.TGAnimAction_Create(pAnimNode, "db_hit_x", 0, 0)
	pSequence.AddAction(pLeanAction)

	# open eyes and close mouth
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)

	# Return to default.
	pAction = App.CharacterAction_Create (pCharacter, App.CharacterAction.AT_DEFAULT);
	pSequence.AddAction (pAction, pLeanAction)

	return pSequence

	# lean hard left animation
def XHitHard(pCharacter):
	return XHit (pCharacter)
##########################

def SCPHHit(pCharacter):
	return None
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_hit_c.NIF", "SCP_hit_h")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	# Lean
	pAction = App.TGAnimAction_Create(pAnimNode, "SCP_hit_h", 0, 0, 1)
	pSequence.AddAction(pAction)

	# open eyes and close mouth
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes, pAction)
	if (App.g_kSystemWrapper.GetRandomNumber(5) == 3):
		if (pCharacter.GetGender() == 0):
			pSequence.AddAction(App.TGSoundAction_Create("MaleEek"+ str(App.g_kSystemWrapper.GetRandomNumber(7)+1)))
		else:
			pSequence.AddAction(App.TGSoundAction_Create("FemaleEek"+ str(App.g_kSystemWrapper.GetRandomNumber(7)+1)))
	return pSequence

	# lean hard left animation
def SCPHHitHard(pCharacter):
	return SCPHHit (pCharacter)


	# lean left animation
def SCPCHit (pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_hit_c.NIF", "SCP_hit_c")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()

	# Lean
	pLeanAction = App.TGAnimAction_Create(pAnimNode, "SCP_hit_c", 0, 0)
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
def SCPCHitHard(pCharacter):
	return SCPCHit (pCharacter)

def SCPXHit (pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_hit_x.NIF", "SCP_hit_x")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()

	# Lean
	pLeanAction = App.TGAnimAction_Create(pAnimNode, "SCP_hit_x", 0, 0)
	pSequence.AddAction(pLeanAction)

	# open eyes and close mouth
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)

	# Return to default.
	pAction = App.CharacterAction_Create (pCharacter, App.CharacterAction.AT_DEFAULT);
	pSequence.AddAction (pAction, pLeanAction)

	return pSequence

	# lean hard left animation
def SCPXHitHard(pCharacter):
	return SCPXHit (pCharacter)


def SCPPlaceAtL1(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_L1toG3_S.nif", "SCP_L1toG3_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "SCP_L1toG3_S")
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def SCPPlaceAtL2(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_L2toG1_s.nif", "SCP_L2toG1_s")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "SCP_L2toG1_s")
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def SCPPlaceAtG1(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_G1toL2_S.nif", "SCP_G1toL2_s")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "SCP_G1toL2_s")
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def SCPPlaceAtG2(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_G2toL2_S.nif", "SCP_G2toL2_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "SCP_G2toL2_S")
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def SCPPlaceAtG3(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_G3toL1_S.nif", "SCP_G3toL1_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "SCP_G3toL1_S")
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def SCPL2ToG1(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_L2toG1_M.nif", "SCP_L2toG1_M")
	kAM.LoadAnimation ("data/animations/SCP_Door_L1.nif", "SCP_Door_L1")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pCharacter.SetHidden(0)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "SCP_L2toG1_M", 0, 0, 1)
	pSequence.AddAction(pAnimAction1)#, pOpenEyes)
	pDoorAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "LiftDoorAction", pBridge, "SCP_Door_L1", "LiftDoor")
	pSequence.AddAction(pDoorAction, pOpenEyes, 0.125)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "SCPG1M"))
	return pSequence

def SCPG1ToL2(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_G1toL2_M.nif", "SCP_G1toL2_M")
	kAM.LoadAnimation ("data/animations/SCP_Door_L1b.nif", "SCP_Door_L1B")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "SCP_G1toL2_M", 0, 0, 1)
	pSequence.AddAction(pAnimAction, pOpenEyes)
	fTime = kAM.GetAnimationLength("SCP_G1toL2_M")
	pDoorAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "LiftDoorAction", pBridge, "SCP_Door_L1B", "LiftDoor")
	pSequence.AddAction(pDoorAction, pOpenEyes, fTime - 2.5)
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_HIDDEN)
	pSequence.AddCompletedEvent(pEvent)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "SCPL2M"))
	return pSequence

def SCPL2ToG2(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_L2toG2_M.nif", "SCP_L2toG2_M")
	kAM.LoadAnimation ("data/animations/SCP_Door_L1.nif", "SCP_Door_L1")
	kAM.LoadAnimation ("data/animations/SCP_chair_e1.nif", "SCP_chair_e1")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pCharacter.SetHidden(0)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "SCP_L2toG2_M", 0, 0, 1)
	pSequence.AddAction(pAnimAction1, pOpenEyes)
	pDoorAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "LiftDoorAction", pBridge, "SCP_Door_L1", "LiftDoor")
	pSequence.AddAction(pDoorAction, pOpenEyes, 0.125)
	pAction = App.TGAnimAction_Create(pBridgeNode, "SCP_chair_e1", 0, 0)
	pSequence.AddAction(pAction, pOpenEyes)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "SCPG2M"))
	return pSequence

	# LC: My chair reference
#def SCPTurnBackAtCFromCaptain(pCharacter):
#	kAM = App.g_kAnimationManager
#	kAM.LoadAnimation ("data/animations/SCP_face_capt_C_reverse.nif", "SCP_face_capt_C_reverse")
#	kAM.LoadAnimation ("data/animations/SCP_chair_C_face_capt_reverse.nif", "SCP_chair_C_face_capt_reverse")
#	pSet = App.g_kSetManager.GetSet("bridge")
#	pBridge = pSet.GetObject("bridge")
#	pBridgeNode = pBridge.GetAnimNode()
#	pCharacter = App.CharacterClass_Cast(pCharacter)
#	pCharacter = App.CharacterClass_Cast(pCharacter)
#	pSequence = App.TGSequence_Create()
#	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
#	pSequence.AddAction(pOpenEyes)
#	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "SCP_face_capt_C_reverse", 0, 0, 1)
#	pSequence.AddAction(pAction, pOpenEyes)
#	pAction = App.TGAnimAction_Create(pBridgeNode, "SCP_chair_C_face_capt_reverse", 0, 0)
#	pSequence.AddAction(pAction, pOpenEyes)
#	return pSequence

def SCPG2ToL2(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_G2toL2_M.nif", "SCP_G2toL2_M")
	kAM.LoadAnimation ("data/animations/SCP_Door_L1c.nif", "SCP_Door_L1C")
	kAM.LoadAnimation ("data/animations/SCP_chair_e2.nif", "SCP_chair_e2")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "SCP_G2toL2_M", 0, 0, 1)
	pSequence.AddAction(pAnimAction, pOpenEyes)
	fTime = kAM.GetAnimationLength("SCP_G2toL2_M")
	pDoorAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "LiftDoorAction", pBridge, "SCP_Door_L1C", "LiftDoor")
	pSequence.AddAction(pDoorAction, pOpenEyes, fTime - 2.5)
	pAction = App.TGAnimAction_Create(pBridgeNode, "SCP_chair_e2", 0, 0)
	pSequence.AddAction(pAction, pOpenEyes)
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_HIDDEN)
	pSequence.AddCompletedEvent(pEvent)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "SCPL2M"))
	return pSequence


def SCPL1ToG3(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_L1toG3_M.nif", "SCP_L1toG3_M")
	kAM.LoadAnimation ("data/animations/SCP_Door_L2b.nif", "SCP_Door_L2b")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pCharacter.SetHidden(0)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "SCP_L1toG3_M", 0, 0, 1)
	pSequence.AddAction(pAnimAction1, pOpenEyes)
	pDoorAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "LiftDoorAction", pBridge, "SCP_Door_L2b", "LiftDoor")
	pSequence.AddAction(pDoorAction, pOpenEyes, 0.125)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "SCPG3M"))
	return pSequence

def SCPG3ToL1(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_G3toL1_M.nif", "SCP_G3toL1_M")
	kAM.LoadAnimation ("data/animations/SCP_Door_L2b.nif", "SCP_Door_L2B")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "SCP_G3toL1_M", 0, 0, 1)
	pSequence.AddAction(pAnimAction, pOpenEyes)
	fTime = kAM.GetAnimationLength("SCP_G3toL1_M")
	pDoorAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "LiftDoorAction", pBridge, "SCP_Door_L2B", "LiftDoor")
	pSequence.AddAction(pDoorAction, pOpenEyes, fTime - 2.5)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "SCPL1M"))
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_HIDDEN)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence


def SCP_extra3_M_interaction(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_extra3_m_interaction.NIF", "SCP_extra3_M_interaction")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "SCP_extra3_M_interaction", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def SCP_extra2_M_interaction(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_extra2_m_interaction.NIF", "SCP_extra2_M_interaction")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "SCP_extra2_M_interaction", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def SCP_extra1_M_interaction_1(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_extra1_m_interaction_1.NIF", "SCP_extra1_M_interaction_1")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "SCP_extra1_M_interaction_1", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

def SCP_extra1_M_interaction_2(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/SCP_extra1_m_interaction_2.NIF", "SCP_extra1_M_interaction_2")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAction = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "SCP_extra1_M_interaction_2", 0, 0, 1)
	pSequence.AddAction(pAction, pOpenEyes)
	return pSequence

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


def EBHConsoleInteraction(pCharacter):
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
	pCharacter = App.CharacterClass_Cast(pCharacter)
	if not (pCharacter):
		return None

	pSequence = App.TGSequence_Create()

	pSequence.AppendAction(App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_C_pushingbuttons_A", 0, 0))
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_BREATHE))

	return pSequence

def SCPCConsoleInteraction(pCharacter):
	pCharacter = App.CharacterClass_Cast(pCharacter)
	if not (pCharacter):
		return None

	iNumPresses = App.g_kSystemWrapper.GetRandomNumber(3)+1
	pSequence = App.TGSequence_Create()
	pLastAction = App.TGAction_CreateNull()

	for i in range (iNumPresses):
		iRandAction = App.g_kSystemWrapper.GetRandomNumber(7)

		if (iRandAction == 0):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_C", "seated_A")
		elif (iRandAction == 1):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_C", "seated_B")
		elif (iRandAction == 2):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_C", "seated_C")
		elif (iRandAction == 3):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_C", "seated_D")
		elif (iRandAction == 4):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_C", "seated_E")
		elif (iRandAction == 5):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_C", "seated_F")
		elif (iRandAction == 6):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_C", "seated_G")

		pSequence.AddAction(pNextAction, pLastAction)
		pLastAction = pNextAction

	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_BREATHE))

	return pSequence

def DBXConsoleInteraction(pCharacter):
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

def EBXConsoleInteraction(pCharacter):
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

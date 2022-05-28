from bcdebug import debug
# MediumAnimations.py
# This file includes all animations shared by medium characters

import App
import Bridge.Characters.CommonAnimations

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

def HHit(pCharacter):
	debug(__name__ + ", HHit")
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
	debug(__name__ + ", HHitHard")
	return HHit (pCharacter)

	# lean left animation
def CHit (pCharacter):
	debug(__name__ + ", CHit")
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
	debug(__name__ + ", CHitHard")
	return CHit (pCharacter)


def XHit (pCharacter):
	debug(__name__ + ", XHit")
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
	debug(__name__ + ", XHitHard")
	return XHit (pCharacter)

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
	return HHit (pCharacter)

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
	return CHit (pCharacter)

def EBXHit (pCharacter):
	debug(__name__ + ", EBXHit")
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
	return XHit (pCharacter)

def ConsoleSlides(pCharacter):
	debug(__name__ + ", ConsoleSlides")
	iNumLooks = App.g_kSystemWrapper.GetRandomNumber(3)+1
	pSequence = App.TGSequence_Create()
	pLastAction = App.TGAction_CreateNull()

	for i in range (iNumLooks):
		iRandAction = App.g_kSystemWrapper.GetRandomNumber(4)

		if (iRandAction == 0):
			pNextAction = ConsoleSlideForeLeft(pCharacter)
		elif (iRandAction == 1):
			pNextAction = ConsoleSlideForeRight(pCharacter)
		elif (iRandAction == 2):
#			pNextAction = ConsoleSlideLeft(pCharacter)
			pNextAction = ConsoleSlideRight(pCharacter)
		elif (iRandAction == 3):
			pNextAction = ConsoleSlideRight(pCharacter)

		pSequence.AddAction(pNextAction, pLastAction, 0.25)
		pLastAction = pNextAction

	return pSequence

def ConsoleSlideForeLeft(pCharacter):
	debug(__name__ + ", ConsoleSlideForeLeft")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_Console_Slide_Fore_Left_H.NIF", "EB_console_slide_fore_left_H")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_console_slide_fore_left_H", 0, 0)
	return pAnimAction1

def ConsoleSlideForeRight(pCharacter):
	debug(__name__ + ", ConsoleSlideForeRight")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_Console_Slide_Fore_Right_H.NIF", "EB_console_slide_fore_right_H")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_console_slide_fore_right_H", 0, 0)
	return pAnimAction1

def ConsoleSlideLeft(pCharacter):
	debug(__name__ + ", ConsoleSlideLeft")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_Console_Slide_Left_H.NIF", "EB_console_slide_left_H")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_console_slide_left_H", 0, 0)
	return pAnimAction1

def ConsoleSlideRight(pCharacter):
	debug(__name__ + ", ConsoleSlideRight")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_Console_Slide_Right_H.NIF", "EB_console_slide_right_H")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_console_slide_right_H", 0, 0)
	return pAnimAction1

# Looks
def DBCTalkE(pCharacter):
	debug(__name__ + ", DBCTalkE")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_C_Talk_ES_M.NIF", "DB_C_Talk_ES_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_C_Talk_ES_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def DBCTalkH(pCharacter):
	debug(__name__ + ", DBCTalkH")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_C_Talk_TH_M.NIF", "DB_C_Talk_TH_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_C_Talk_TH_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def DBCTalkT(pCharacter):
	debug(__name__ + ", DBCTalkT")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_C_Talk_TH_M.NIF", "DB_C_Talk_TH_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_C_Talk_TH_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def DBCTalkS(pCharacter):
	debug(__name__ + ", DBCTalkS")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_C_Talk_ES_M.NIF", "DB_C_Talk_ES_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_C_Talk_ES_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def DBCTalkX(pCharacter):
	debug(__name__ + ", DBCTalkX")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_C_Talk_X_M.NIF", "DB_C_Talk_X_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_C_Talk_X_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def DBC2TalkP1(pCharacter):
	debug(__name__ + ", DBC2TalkP1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_C2_Talk_P1_M.NIF", "DB_C2_Talk_P1_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_C2_Talk_P1_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def DBC2TalkFinP1(pCharacter):
	debug(__name__ + ", DBC2TalkFinP1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_C2_Talk_P1_M_reverse.NIF", "DB_C2_Talk_P1_M_reverse")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_C2_Talk_P1_M_reverse", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def DBXTalkE(pCharacter):
	debug(__name__ + ", DBXTalkE")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_X_Talk_E_M.NIF", "DB_X_Talk_E_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_X_Talk_E_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def DBXTalkH(pCharacter):
	debug(__name__ + ", DBXTalkH")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_X_Talk_TH_M.NIF", "DB_X_Talk_TH_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_X_Talk_TH_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def DBXTalkT(pCharacter):
	debug(__name__ + ", DBXTalkT")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_X_Talk_TH_M.NIF", "DB_X_Talk_TH_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_X_Talk_TH_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def DBXTalkS(pCharacter):
	debug(__name__ + ", DBXTalkS")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_X_Talk_S_M.NIF", "DB_X_Talk_S_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_X_Talk_S_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def DBP1TalkC2(pCharacter):
	debug(__name__ + ", DBP1TalkC2")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_P1_Talk_C2_M.NIF", "DB_P1_Talk_C2_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_P1_Talk_C2_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def DBP1TalkFinC2(pCharacter):
	debug(__name__ + ", DBP1TalkFinC2")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_P1_Talk_C2_M_reverse.NIF", "DB_P1_Talk_C2_M_reverse")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_P1_Talk_C2_M_reverse", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def DBHTalkC(pCharacter):
	debug(__name__ + ", DBHTalkC")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_H_Talk_to_C_M.NIF", "DB_H_Talk_to_C_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_H_Talk_to_C_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def DBHTalkE(pCharacter):
	debug(__name__ + ", DBHTalkE")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_H_Talk_to_E_M.NIF", "DB_H_Talk_to_E_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_H_Talk_to_E_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def DBHTalkS(pCharacter):
	debug(__name__ + ", DBHTalkS")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_H_Talk_to_S_M.NIF", "DB_H_Talk_to_S_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_H_Talk_to_S_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def DBHTalkX(pCharacter):
	debug(__name__ + ", DBHTalkX")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_H_Talk_to_T_M.NIF", "DB_H_Talk_to_T_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_H_Talk_to_T_M", 0, 0, 1)
	return pAnimAction1

def DBHTalkT(pCharacter):
	debug(__name__ + ", DBHTalkT")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_H_Talk_X_M.NIF", "DB_H_Talk_X_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_H_Talk_X_M", 0, 0, 1)
	return pAnimAction1

def DBHTalkFinC(pCharacter):
	debug(__name__ + ", DBHTalkFinC")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_H_Talk_fin_C_M.NIF", "DB_H_Talk_fin_C_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_H_Talk_fin_C_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def DBHTalkFinE(pCharacter):
	debug(__name__ + ", DBHTalkFinE")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_H_Talk_fin_E_M.NIF", "DB_H_Talk_fin_E_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_H_Talk_fin_E_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def DBHTalkFinS(pCharacter):
	debug(__name__ + ", DBHTalkFinS")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_H_Talk_fin_S_M.NIF", "DB_H_Talk_fin_S_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_H_Talk_fin_S_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def DBHTalkFinT(pCharacter):
	debug(__name__ + ", DBHTalkFinT")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_H_Talk_fin_T_M.NIF", "DB_H_Talk_fin_T_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_H_Talk_fin_T_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def DBHTalkFinX(pCharacter):
	debug(__name__ + ", DBHTalkFinX")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_H_Talk_X_M_reverse.NIF", "DB_H_Talk_X_M_reverse")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_H_Talk_X_M_reverse", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBCTalkE(pCharacter):
	debug(__name__ + ", EBCTalkE")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_C_Talk_G3_M.NIF", "EB_C_Talk_G3_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_C_Talk_G3_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBCTalkS(pCharacter):
	debug(__name__ + ", EBCTalkS")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_C_Talk_S_M.NIF", "EB_C_Talk_S_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_C_Talk_S_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBCTalkH(pCharacter):
	debug(__name__ + ", EBCTalkH")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_C_Talk_TH_M.NIF", "EB_C_Talk_TH_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_C_Talk_TH_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBCTalkT(pCharacter):
	debug(__name__ + ", EBCTalkT")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_C_Talk_TH_M.NIF", "EB_C_Talk_TH_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_C_Talk_TH_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBXTalkE(pCharacter):
	debug(__name__ + ", EBXTalkE")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_X_Talk_E_M.NIF", "EB_X_Talk_E_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_X_Talk_E_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBXTalkC(pCharacter):
	debug(__name__ + ", EBXTalkC")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_X_Talk_C_M.NIF", "EB_X_Talk_C_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_X_Talk_C_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBHTalkC(pCharacter):
	debug(__name__ + ", EBHTalkC")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_H_Talk_to_G2_M.NIF", "EB_H_Talk_to_G2_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_H_Talk_to_G2_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBHTalkE(pCharacter):
	debug(__name__ + ", EBHTalkE")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_H_Talk_to_G3_M.NIF", "EB_H_Talk_to_G3_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_H_Talk_to_G3_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBHTalkS(pCharacter):
	debug(__name__ + ", EBHTalkS")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_H_Talk_to_G2_M.NIF", "EB_H_Talk_to_G2_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_H_Talk_to_G2_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBHTalkT(pCharacter):
	debug(__name__ + ", EBHTalkT")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_H_Talk_to_T_M.NIF", "EB_H_Talk_to_T_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_H_Talk_to_T_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBHTalkFinC(pCharacter):
	debug(__name__ + ", EBHTalkFinC")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_H_Talk_fin_G2_M.NIF", "EB_H_Talk_fin_G2_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_H_Talk_fin_G2_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBHTalkFinE(pCharacter):
	debug(__name__ + ", EBHTalkFinE")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_H_Talk_fin_G3_M.NIF", "EB_H_Talk_fin_G3_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_H_Talk_fin_G3_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBHTalkFinS(pCharacter):
	debug(__name__ + ", EBHTalkFinS")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_H_Talk_fin_G2_M.NIF", "EB_H_Talk_fin_G2_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_H_Talk_fin_G2_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBHTalkFinT(pCharacter):
	debug(__name__ + ", EBHTalkFinT")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_H_Talk_fin_T_M.NIF", "EB_H_Talk_fin_T_M")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_H_Talk_fin_T_M", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

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
	pSequence = App.TGSequence_Create()
	if not (pCharacter):
		return pSequence

	# Look forward, fore right, and right
	iNumLooks = App.g_kSystemWrapper.GetRandomNumber(4)+2
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
	pSequence = App.TGSequence_Create()
	if not (pCharacter):
		return pSequence

	iNumPresses = App.g_kSystemWrapper.GetRandomNumber(6)+3
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
	debug(__name__ + ", EBHConsoleInteraction")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	if not (pCharacter):
		return pSequence

	iNumPresses = App.g_kSystemWrapper.GetRandomNumber(6)+3
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
	pSequence = App.TGSequence_Create()
	if not (pCharacter):
		return pSequence

	# Look forward, fore right, and right
	iNumLooks = App.g_kSystemWrapper.GetRandomNumber(4)+2
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
	pSequence = App.TGSequence_Create()
	if not (pCharacter):
		return pSequence

	pSequence.AppendAction(App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_C_pushingbuttons_A", 0, 0))
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_BREATHE))

	return pSequence

def EBCConsoleInteraction(pCharacter):
	debug(__name__ + ", EBCConsoleInteraction")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	if not (pCharacter):
		return pSequence

	iNumPresses = App.g_kSystemWrapper.GetRandomNumber(6)+3
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
	pSequence = App.TGSequence_Create()
	if not (pCharacter):
		return pSequence

	iNumPresses = App.g_kSystemWrapper.GetRandomNumber(6)+3
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
	debug(__name__ + ", EBXConsoleInteraction")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	if not (pCharacter):
		return pSequence

	iNumPresses = App.g_kSystemWrapper.GetRandomNumber(6)+3
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

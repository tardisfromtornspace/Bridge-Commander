from bcdebug import debug
# SmallAnimations.py
# This file includes all animations shared by small characters

import App
import Bridge.Characters.CommonAnimations

def PlaceAtE(pCharacter):
	debug(__name__ + ", PlaceAtE")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_EtoL1_s.nif", "db_EtoL1_s")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "db_EtoL1_s")
	pSequence.AddAction(pAction)
	return pSequence

def PlaceAtS(pCharacter):
	debug(__name__ + ", PlaceAtS")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_StoL1_S.nif", "db_StoL1_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "db_StoL1_S")
	pSequence.AddAction(pAction)
	return pSequence

def PlaceAtL1(pCharacter):
	debug(__name__ + ", PlaceAtL1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_L1toE_S.nif", "db_L1toE_S")
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_L1toE_S", 0, 0), pOpenEyes)
	return pSequence

def TurnAtETowardsCaptain(pCharacter):
	debug(__name__ + ", TurnAtETowardsCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_face_capt_e.nif", "db_face_capt_e")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_face_capt_e", 0, 0, 1), pOpenEyes)
	return pSequence

	# Turn towards captain from Science
def TurnAtSTowardsCaptain(pCharacter):
	debug(__name__ + ", TurnAtSTowardsCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_face_capt_s.nif", "db_face_capt_s")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_face_capt_s", 0, 0, 1), pOpenEyes)
	return pSequence

	# L1 to E
def MoveFromL1ToE(pCharacter):
	debug(__name__ + ", MoveFromL1ToE")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_L1toE_S.nif", "db_L1toE_S")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_WalkFromLift = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_L1toE_S", 0, 0, 1)
	pSequence.AddAction(pAnimAction_WalkFromLift, pOpenEyes)
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "doorl1", 0, 0)
	pSequence.AddAction(pAnimAction, pOpenEyes, 0.125)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "DBEngineer"))
	pEvent = App.TGIntEvent_Create ()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination (pCharacter)
	pEvent.SetInt (App.CharacterClass.CS_STANDING)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence	

	# L1 to S
def MoveFromL1ToS(pCharacter):
	debug(__name__ + ", MoveFromL1ToS")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_L1toS_S.nif", "db_L1toS_S")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_WalkFromLift = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_L1toS_S", 0, 0, 1)
	pSequence.AddAction(pAnimAction_WalkFromLift, pOpenEyes)
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "doorl1", 0, 0)
	pSequence.AddAction(pAnimAction, pOpenEyes, 0.125)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "DBScience"))
	pEvent = App.TGIntEvent_Create ()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination (pCharacter)
	pEvent.SetInt (App.CharacterClass.CS_STANDING)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence	

	# From E to L1
def MoveFromEToL1(pCharacter):
	debug(__name__ + ", MoveFromEToL1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_EtoL1_s.nif", "db_EtoL1_s")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_WalkToLift = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_EtoL1_s", 0, 0, 1)
	pSequence.AddAction(pAnimAction_WalkToLift, pOpenEyes)
	fTime = kAM.GetAnimationLength("db_EtoL1_s")
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "doorl1", 0, 0)
	pSequence.AddAction(pAnimAction, pOpenEyes, fTime - 2.1)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "DBL1S"))
	#pEvent = App.TGIntEvent_Create ()		# Add event to hide character after it gets into the turbolift
	#pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	#pEvent.SetDestination (pCharacter)
	#pEvent.SetInt (App.CharacterClass.CS_HIDDEN)
	#pSequence.AddCompletedEvent(pEvent)
	return pSequence

	# From S to L1
def MoveFromSToL1(pCharacter):
	debug(__name__ + ", MoveFromSToL1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_StoL1_s.nif", "db_StoL1_s")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_WalkToLift = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_StoL1_s", 0, 0, 1)
	pSequence.AddAction(pAnimAction_WalkToLift, pOpenEyes)
	fTime = kAM.GetAnimationLength("db_StoL1_s")
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "doorl1", 0, 0)
	pSequence.AddAction(pAnimAction, pOpenEyes, fTime - 2.1)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "DBL1S"))
	pEvent = App.TGIntEvent_Create ()		# Add event to hide character after it gets into the turbolift
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination (pCharacter)
	pEvent.SetInt (App.CharacterClass.CS_HIDDEN)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence

####################################################
# E-Bridge Animations
####################################################

def EBPlaceAtE(pCharacter):
	debug(__name__ + ", EBPlaceAtE")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_stand_e_s.nif", "EB_stand_e_s")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "EB_stand_e_s")
	pSequence.AddAction(pAction)
	return pSequence

	# Seat at E
def EBSeatedE(pCharacter):
	debug(__name__ + ", EBSeatedE")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_seated_e_s.nif", "EB_seated_e_s")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimAction_Create(pAnimNode, "EB_seated_e_s", 0, 0)
	pSequence.AddAction(pAction)
	return pSequence

def EBPlaceAtS(pCharacter):
	debug(__name__ + ", EBPlaceAtS")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_stand_s_s.nif", "EB_stand_s_s")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "EB_stand_s_s")
	pSequence.AddAction(pAction)
	return pSequence

	# Seat at S
def EBSeatedS(pCharacter):
	debug(__name__ + ", EBSeatedS")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_seated_s_s.nif", "EB_seated_s_s")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimAction_Create(pAnimNode, "EB_seated_s_s", 0, 0)
	pSequence.AddAction(pAction)
	return pSequence

def EBPlaceAtL1(pCharacter):
	debug(__name__ + ", EBPlaceAtL1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_L1toE_S.nif", "EB_L1toE_S")
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_L1toE_S", 0, 0), pOpenEyes)
	return pSequence

def EBTurnAtETowardsCaptain(pCharacter):
	debug(__name__ + ", EBTurnAtETowardsCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_face_capt_e.nif", "EB_face_capt_e")
	kAM.LoadAnimation ("data/animations/EB_chair_e_face_capt.nif", "EB_chair_e_face_capt")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_face_capt_e", 0, 0, 1), pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pBridgeNode, "EB_chair_e_face_capt", 0, 0), pOpenEyes)
	return pSequence

	# Turn towards captain from Science
def EBTurnAtSTowardsCaptain(pCharacter):
	debug(__name__ + ", EBTurnAtSTowardsCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_face_capt_s.nif", "EB_face_capt_s")
	kAM.LoadAnimation ("data/animations/EB_chair_s_face_capt.nif", "EB_chair_s_face_capt")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_face_capt_s", 0, 0, 1), pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pBridgeNode, "EB_chair_s_face_capt", 0, 0), pOpenEyes)
	return pSequence

def EBTurnBackAtEFromCaptain(pCharacter):
	debug(__name__ + ", EBTurnBackAtEFromCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_face_capt_e_reverse.nif", "EB_face_capt_e_reverse")
	kAM.LoadAnimation ("data/animations/EB_chair_e_face_capt_reverse.nif", "EB_chair_e_face_capt_reverse")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_face_capt_e_reverse", 0, 0, 1), pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pBridgeNode, "EB_chair_e_face_capt_reverse", 0, 0), pOpenEyes)
	return pSequence

def EBTurnBackAtSFromCaptain(pCharacter):
	debug(__name__ + ", EBTurnBackAtSFromCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_face_capt_s_reverse.nif", "EB_face_capt_s_reverse")
	kAM.LoadAnimation ("data/animations/EB_chair_s_face_capt_reverse.nif", "EB_chair_s_face_capt_reverse")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_face_capt_s_reverse", 0, 0, 1), pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pBridgeNode, "EB_chair_s_face_capt_reverse", 0, 0), pOpenEyes)
	return pSequence

	# L1 to E
def EBMoveFromL1ToE(pCharacter):
	debug(__name__ + ", EBMoveFromL1ToE")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_L1toE_S.nif", "EB_L1toE_S")
	kAM.LoadAnimation ("data/animations/EB_sit_E_s.nif", "EB_sit_E_s")
	kAM.LoadAnimation ("data/animations/EB_chair_E_in.nif", "EB_chair_E_in")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_WalkFromLift = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_L1toE_S", 0, 0, 1)
	pSequence.AddAction(pAnimAction_WalkFromLift, pOpenEyes)
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_Door_L1", 0, 0)
	pSequence.AddAction(pAnimAction, pOpenEyes, 0.125)
	pAnimAction_Sit = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_sit_E_s", 0, 0)
	pSequence.AddAction(pAnimAction_Sit, pAnimAction_WalkFromLift, 0.0)
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_chair_E_in", 0, 0)
	pSequence.AddAction(pAnimAction, pAnimAction_WalkFromLift, 0.0)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBEngineer"))
	pEvent = App.TGIntEvent_Create ()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination (pCharacter)
	pEvent.SetInt (App.CharacterClass.CS_STANDING)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence	

	# L1 to S
def EBMoveFromL1ToS(pCharacter):
	debug(__name__ + ", EBMoveFromL1ToS")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_L1toS_S.nif", "EB_L1toS_S")
	kAM.LoadAnimation ("data/animations/EB_sit_S_s.nif", "EB_sit_S_s")
	kAM.LoadAnimation ("data/animations/EB_chair_S_in.nif", "EB_chair_S_in")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_WalkFromLift = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_L1toS_S", 0, 0, 1)
	pSequence.AddAction(pAnimAction_WalkFromLift, pOpenEyes)
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_Door_L1", 0, 0)
	pSequence.AddAction(pAnimAction, pOpenEyes, 0.125)
	pAnimAction_Sit = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_sit_S_s", 0, 0)
	pSequence.AddAction(pAnimAction_Sit, pAnimAction_WalkFromLift, 0.0)
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_chair_S_in", 0, 0)
	pSequence.AddAction(pAnimAction, pAnimAction_WalkFromLift, 0.0)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBScience"))
	pEvent = App.TGIntEvent_Create ()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination (pCharacter)
	pEvent.SetInt (App.CharacterClass.CS_STANDING)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence	

	# From E to L1
def EBMoveFromEToL1(pCharacter):
	debug(__name__ + ", EBMoveFromEToL1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_stand_E_s.nif", "EB_stand_E_s")
	kAM.LoadAnimation ("data/animations/EB_chair_E_out.nif", "EB_chair_E_out")
	kAM.LoadAnimation ("data/animations/EB_EtoL1_s.nif", "EB_EtoL1_s")
	kAM.LoadAnimation ("data/animations/EB_door_l1.nif", "EB_Door_L1")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Stand = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_stand_E_s", 0, 0, 1)
	pSequence.AddAction(pAnimAction_Stand, pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pBridgeNode, "EB_chair_E_out", 0, 0), pOpenEyes)
	pAnimAction_WalkToLift = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_EtoL1_s", 0, 0)
	pSequence.AddAction(pAnimAction_WalkToLift, pAnimAction_Stand)
	fTime = kAM.GetAnimationLength("EB_EtoL1_s")
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_Door_L1", 0, 0)
	pSequence.AddAction(pAnimAction, pAnimAction_Stand, fTime - 2.1)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBL1S"))
	#pEvent = App.TGIntEvent_Create ()		# Add event to hide character after it gets into the turbolift
	#pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	#pEvent.SetDestination (pCharacter)
	#pEvent.SetInt (App.CharacterClass.CS_HIDDEN)
	#pSequence.AddCompletedEvent(pEvent)
	return pSequence

	# From S to L1
def EBMoveFromSToL1(pCharacter):
	debug(__name__ + ", EBMoveFromSToL1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_stand_S_s.nif", "EB_stand_S_s")
	kAM.LoadAnimation ("data/animations/EB_chair_S_out.nif", "EB_chair_S_out")
	kAM.LoadAnimation ("data/animations/EB_StoL1_s.nif", "EB_StoL1_s")
	kAM.LoadAnimation ("data/animations/EB_door_l1.nif", "EB_Door_L1")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Stand = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_stand_S_s", 0, 0, 1)
	pSequence.AddAction(pAnimAction_Stand, pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pBridgeNode, "EB_chair_S_out", 0, 0), pOpenEyes)
	pAnimAction_WalkToLift = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_StoL1_s", 0, 0)
	pSequence.AddAction(pAnimAction_WalkToLift, pAnimAction_Stand)
	fTime = kAM.GetAnimationLength("EB_StoL1_s")
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_Door_L1", 0, 0)
	pSequence.AddAction(pAnimAction, pAnimAction_Stand, fTime - 2.1)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBL1S"))
	pEvent = App.TGIntEvent_Create ()		# Add event to hide character after it gets into the turbolift
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination (pCharacter)
	pEvent.SetInt (App.CharacterClass.CS_HIDDEN)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence

def EBMoveFromSToS1(pCharacter):
	debug(__name__ + ", EBMoveFromSToS1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_stand_s_s.NIF", "EB_stand_s_s")
	kAM.LoadAnimation ("data/animations/EB_StoS1_S.NIF", "EB_StoS1_S")
	kAM.LoadAnimation ("data/animations/EB_chair_S_out.nif", "EB_chair_S_out")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Stand = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_stand_s_s", 0, 0, 1)
	pSequence.AddAction(pAnimAction_Stand, pOpenEyes)
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_chair_S_out", 0, 0)
	pSequence.AddAction(pAnimAction, pOpenEyes)
	pAnimAction_Walk = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_StoS1_S", 0, 0)
	pSequence.AddAction(pAnimAction_Walk, pAnimAction_Stand, 0.0)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBScience1"))
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_STANDING)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence

def EBMoveFromS1ToS(pCharacter):
	debug(__name__ + ", EBMoveFromS1ToS")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_sit_s_s.NIF", "EB_sit_s_s")
	kAM.LoadAnimation ("data/animations/EB_S1toS_S.NIF", "EB_S1toS_S")
	kAM.LoadAnimation ("data/animations/EB_chair_S_in.nif", "EB_chair_S_in")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Walk = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_S1toS_S", 0, 0, 1)
	pSequence.AddAction(pAnimAction_Walk, pOpenEyes)
	pAnimAction_Sit = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_sit_s_s", 0, 0)
	pSequence.AddAction(pAnimAction_Sit, pAnimAction_Walk)
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_chair_S_in", 0, 0)
	pSequence.AddAction(pAnimAction, pAnimAction_Walk)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBScience"))
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_SEATED)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence

def EBMoveFromSToS2(pCharacter):
	debug(__name__ + ", EBMoveFromSToS2")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_stand_s_s.NIF", "EB_stand_s_s")
	kAM.LoadAnimation ("data/animations/EB_StoS2_S.NIF", "EB_StoS2_S")
	kAM.LoadAnimation ("data/animations/EB_chair_S_out.nif", "EB_chair_S_out")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Stand = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_stand_s_s", 0, 0, 1)
	pSequence.AddAction(pAnimAction_Stand, pOpenEyes)
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_chair_S_out", 0, 0)
	pSequence.AddAction(pAnimAction, pOpenEyes)
	pAnimAction_Walk = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_StoS2_S", 0, 0)
	pSequence.AddAction(pAnimAction_Walk, pAnimAction_Stand, 0.0)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBScience2"))
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_STANDING)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence

def EBMoveFromS2ToS(pCharacter):
	debug(__name__ + ", EBMoveFromS2ToS")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_sit_s_s.NIF", "EB_sit_s_s")
	kAM.LoadAnimation ("data/animations/EB_S2toS_S.NIF", "EB_S2toS_S")
	kAM.LoadAnimation ("data/animations/EB_chair_S_in.nif", "EB_chair_S_in")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Walk = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_S2toS_S", 0, 0, 1)
	pSequence.AddAction(pAnimAction_Walk, pOpenEyes)
	pAnimAction_Sit = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_sit_s_s", 0, 0)
	pSequence.AddAction(pAnimAction_Sit, pAnimAction_Walk)
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_chair_S_in", 0, 0)
	pSequence.AddAction(pAnimAction, pAnimAction_Walk)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBScience"))
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_SEATED)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence

def EBMoveFromS2ToS1(pCharacter):
	debug(__name__ + ", EBMoveFromS2ToS1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_S2toS1_S.NIF", "EB_S2toS1_S")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Walk = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_S2toS1_S", 0, 0, 1)
	pSequence.AddAction(pAnimAction_Walk, pOpenEyes, 0.0)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBScience1"))
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_STANDING)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence

def EBMoveFromS1ToS2(pCharacter):
	debug(__name__ + ", EBMoveFromS1ToS2")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_S1toS2_S.NIF", "EB_S1toS2_S")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Walk = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_S1toS2_S", 0, 0, 1)
	pSequence.AddAction(pAnimAction_Walk, pOpenEyes, 0.0)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBScience2"))
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_STANDING)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence

def EBMoveFromEToE1(pCharacter):
	debug(__name__ + ", EBMoveFromEToE1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_stand_e_s.NIF", "EB_stand_e_s")
	kAM.LoadAnimation ("data/animations/EB_StoS1_E.NIF", "EB_EtoE1_S")
	kAM.LoadAnimation ("data/animations/EB_chair_E_out.nif", "EB_chair_E_out")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Stand = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_stand_e_s", 0, 0, 1)
	pSequence.AddAction(pAnimAction_Stand, pOpenEyes)
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_chair_E_out", 0, 0)
	pSequence.AddAction(pAnimAction, pOpenEyes)
	pAnimAction_Walk = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_EtoE1_S", 0, 0)
	pSequence.AddAction(pAnimAction_Walk, pAnimAction_Stand, 0.0)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBEngineer1"))
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_STANDING)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence

def EBMoveFromE1ToE(pCharacter):
	debug(__name__ + ", EBMoveFromE1ToE")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_sit_e_s.NIF", "EB_sit_e_s")
	kAM.LoadAnimation ("data/animations/EB_E1toE_S.NIF", "EB_E1toE_S")
	kAM.LoadAnimation ("data/animations/EB_chair_E_in.nif", "EB_chair_E_in")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Walk = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_E1toE_S", 0, 0, 1)
	pSequence.AddAction(pAnimAction_Walk, pOpenEyes)
	pAnimAction_Sit = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_sit_e_s", 0, 0)
	pSequence.AddAction(pAnimAction_Sit, pAnimAction_Walk)
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_chair_E_in", 0, 0)
	pSequence.AddAction(pAnimAction, pAnimAction_Walk)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBEngineer"))
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_SEATED)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence

def EBMoveFromEToE2(pCharacter):
	debug(__name__ + ", EBMoveFromEToE2")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_stand_e_s.NIF", "EB_stand_e_s")
	kAM.LoadAnimation ("data/animations/EB_EtoE2_S.NIF", "EB_EtoE2_S")
	kAM.LoadAnimation ("data/animations/EB_chair_E_out.nif", "EB_chair_E_out")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Stand = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_stand_e_s", 0, 0, 1)
	pSequence.AddAction(pAnimAction_Stand, pOpenEyes)
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_chair_E_out", 0, 0)
	pSequence.AddAction(pAnimAction, pOpenEyes)
	pAnimAction_Walk = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_EtoE2_S", 0, 0)
	pSequence.AddAction(pAnimAction_Walk, pAnimAction_Stand, 0.0)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBEngineer2"))
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_STANDING)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence

def EBMoveFromE2ToE(pCharacter):
	debug(__name__ + ", EBMoveFromE2ToE")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_sit_e_s.NIF", "EB_sit_e_s")
	kAM.LoadAnimation ("data/animations/EB_E2toE_S.NIF", "EB_E2toE_S")
	kAM.LoadAnimation ("data/animations/EB_chair_E_in.nif", "EB_chair_E_in")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Walk = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_E2toE_S", 0, 0, 1)
	pSequence.AddAction(pAnimAction_Walk, pOpenEyes)
	pAnimAction_Sit = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_sit_e_s", 0, 0)
	pSequence.AddAction(pAnimAction_Sit, pAnimAction_Walk)
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_chair_E_in", 0, 0)
	pSequence.AddAction(pAnimAction, pAnimAction_Walk)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBEngineer"))
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_SEATED)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence

def EBMoveFromE2ToE1(pCharacter):
	debug(__name__ + ", EBMoveFromE2ToE1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_E2toE1_S.NIF", "EB_E2toE1_S")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Walk = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_E2toE1_S", 0, 0, 1)
	pSequence.AddAction(pAnimAction_Walk, pOpenEyes, 0.0)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBEngineer1"))
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_STANDING)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence

def EBMoveFromE1ToE2(pCharacter):
	debug(__name__ + ", EBMoveFromE1ToE2")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_E1toE2_S.NIF", "EB_E1toE2_S")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Walk = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_E1toE2_S", 0, 0, 1)
	pSequence.AddAction(pAnimAction_Walk, pOpenEyes, 0.0)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBEngineer2"))
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(App.CharacterClass.CS_STANDING)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence

# Looking at other characters
def DBETalkC(pCharacter):
	debug(__name__ + ", DBETalkC")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_E_Talk_C_S.NIF", "DB_E_Talk_C_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_E_Talk_C_S", 0, 0, 1)
	return pAnimAction1

def DBETalkH(pCharacter):
	debug(__name__ + ", DBETalkH")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_E_Talk_H_S.NIF", "DB_E_Talk_H_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_E_Talk_H_S", 0, 0, 1)
	return pAnimAction1

def DBETalkS(pCharacter):
	debug(__name__ + ", DBETalkS")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_E_Talk_S_S.NIF", "DB_E_Talk_S_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_E_Talk_S_S", 0, 0, 1)
	return pAnimAction1

def DBETalkT(pCharacter):
	debug(__name__ + ", DBETalkT")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_E_Talk_T_S.NIF", "DB_E_Talk_T_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_E_Talk_T_S", 0, 0, 1)
	return pAnimAction1

def DBETalkX(pCharacter):
	debug(__name__ + ", DBETalkX")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_E_Talk_X_S.NIF", "DB_E_Talk_X_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_E_Talk_X_S", 0, 0, 1)
	return pAnimAction1

def DBSTalkC(pCharacter):
	debug(__name__ + ", DBSTalkC")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_S_Talk_C_S.NIF", "DB_S_Talk_C_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_S_Talk_C_S", 0, 0, 1)
	return pAnimAction1

def DBSTalkH(pCharacter):
	debug(__name__ + ", DBSTalkH")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_S_Talk_H_S.NIF", "DB_S_Talk_H_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_S_Talk_H_S", 0, 0, 1)
	return pAnimAction1

def DBSTalkE(pCharacter):
	debug(__name__ + ", DBSTalkE")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_S_Talk_E_S.NIF", "DB_S_Talk_E_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_S_Talk_E_S", 0, 0, 1)
	return pAnimAction1

def DBSTalkT(pCharacter):
	debug(__name__ + ", DBSTalkT")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_S_Talk_T_S.NIF", "DB_S_Talk_T_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_S_Talk_T_S", 0, 0, 1)
	return pAnimAction1

def DBSTalkX(pCharacter):
	debug(__name__ + ", DBSTalkX")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_S_Talk_X_S.NIF", "DB_S_Talk_X_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_S_Talk_X_S", 0, 0, 1)
	return pAnimAction1

# E-Bridge looks
def EBETalkC(pCharacter):
	debug(__name__ + ", EBETalkC")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_E_Talk_G2_S.NIF", "EB_E_Talk_G2_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_E_Talk_G2_S", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBETalkH(pCharacter):
	debug(__name__ + ", EBETalkH")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_E_Talk_TH_S.NIF", "EB_E_Talk_TH_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_E_Talk_TH_S", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBETalkS(pCharacter):
	debug(__name__ + ", EBETalkS")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_E_Talk_G2_S.NIF", "EB_E_Talk_G2_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_E_Talk_G2_S", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBETalkT(pCharacter):
	debug(__name__ + ", EBETalkT")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_E_Talk_TH_S.NIF", "EB_E_Talk_TH_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_E_Talk_TH_S", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBETalkFinC(pCharacter):
	debug(__name__ + ", EBETalkFinC")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_E_Talk_fin_C_S.NIF", "EB_E_Talk_fin_C_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_E_Talk_fin_C_S", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBETalkFinH(pCharacter):
	debug(__name__ + ", EBETalkFinH")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_E_Talk_fin_H_S.NIF", "EB_E_Talk_fin_H_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_E_Talk_fin_H_S", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBETalkFinS(pCharacter):
	debug(__name__ + ", EBETalkFinS")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_E_Talk_fin_S_S.NIF", "EB_E_Talk_fin_S_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_E_Talk_fin_S_S", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBETalkFinT(pCharacter):
	debug(__name__ + ", EBETalkFinT")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_E_Talk_fin_T_S.NIF", "EB_E_Talk_fin_T_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_E_Talk_fin_T_S", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBSTalkC(pCharacter):
	debug(__name__ + ", EBSTalkC")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_S_Talk_C_S.NIF", "EB_S_Talk_C_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_S_Talk_C_S", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBSTalkH(pCharacter):
	debug(__name__ + ", EBSTalkH")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_S_Talk_TH_S.NIF", "EB_S_Talk_TH_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_S_Talk_TH_S", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBSTalkE(pCharacter):
	debug(__name__ + ", EBSTalkE")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_S_Talk_G3_S.NIF", "EB_S_Talk_G3_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_S_Talk_G3_S", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBSTalkT(pCharacter):
	debug(__name__ + ", EBSTalkT")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_S_Talk_TH_S.NIF", "EB_S_Talk_TH_S")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_S_Talk_TH_S", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1


###############################################################################
#	SLookAroundConsoleDown, SConsoleInteraction
#	
#	Science-specific definitions for these functions
#	
#	Args:	pCharacter		- the character to call on
#	
#	Return:	pSequence	- the created sequence
###############################################################################
def SLookAroundConsoleDown(pCharacter):
	debug(__name__ + ", SLookAroundConsoleDown")
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


def DBSConsoleInteraction(pCharacter):
	debug(__name__ + ", DBSConsoleInteraction")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	if not (pCharacter):
		return pSequence

	iNumPresses = App.g_kSystemWrapper.GetRandomNumber(6)+3
	pLastAction = App.TGAction_CreateNull()

	for i in range (iNumPresses):
		iRandAction = App.g_kSystemWrapper.GetRandomNumber(4)

		if (iRandAction == 0):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "DB_S", "A")
		elif (iRandAction == 1):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "DB_S", "B")
		elif (iRandAction == 2):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "DB_S", "C")
		elif (iRandAction == 3):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "DB_S", "D")

		pSequence.AddAction(pNextAction, pLastAction)
		pLastAction = pNextAction

	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_BREATHE))

	return pSequence


def EBSConsoleInteraction(pCharacter):
	debug(__name__ + ", EBSConsoleInteraction")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()

	if not (pCharacter):
		return pSequence

	iNumPresses = App.g_kSystemWrapper.GetRandomNumber(6)+3
	pLastAction = App.TGAction_CreateNull()

	for i in range (iNumPresses):
		iRandAction = App.g_kSystemWrapper.GetRandomNumber(3)

		if (iRandAction == 0):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_S", "seated_A")
		elif (iRandAction == 1):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_S", "seated_B")
		elif (iRandAction == 2):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_S", "seated_C")

		pSequence.AddAction(pNextAction, pLastAction)
		pLastAction = pNextAction

	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_BREATHE))

	return pSequence


###############################################################################
#	ELookAroundConsoleDown, EConsoleInteraction
#	
#	Engineering-specific definitions for these functions
#	
#	Args:	pCharacter		- the character to call on
#	
#	Return:	pSequence	- the created sequence
###############################################################################
def ELookAroundConsoleDown(pCharacter):
	debug(__name__ + ", ELookAroundConsoleDown")
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


def DBEConsoleInteraction(pCharacter):
	debug(__name__ + ", DBEConsoleInteraction")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()

	if not (pCharacter):
		return pSequence

	iNumPresses = App.g_kSystemWrapper.GetRandomNumber(6)+3
	pLastAction = App.TGAction_CreateNull()

	for i in range (iNumPresses):
		iRandAction = App.g_kSystemWrapper.GetRandomNumber(4)

		if (iRandAction == 0):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "DB_E", "A")
		elif (iRandAction == 1):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "DB_E", "B")
		elif (iRandAction == 2):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "DB_E", "C")
		elif (iRandAction == 3):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "DB_E", "D")

		pSequence.AddAction(pNextAction, pLastAction)
		pLastAction = pNextAction

	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_BREATHE))

	return pSequence


def EBEConsoleInteraction(pCharacter):
	debug(__name__ + ", EBEConsoleInteraction")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	if not (pCharacter):
		return pSequence

	iNumPresses = App.g_kSystemWrapper.GetRandomNumber(6)+3
	pLastAction = App.TGAction_CreateNull()

	for i in range (iNumPresses):
		iRandAction = App.g_kSystemWrapper.GetRandomNumber(3)

		if (iRandAction == 0):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_E", "seated_A")
		elif (iRandAction == 1):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_E", "seated_B")
		elif (iRandAction == 2):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_E", "seated_C")

		pSequence.AddAction(pNextAction, pLastAction)
		pLastAction = pNextAction

	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_BREATHE))

	return pSequence


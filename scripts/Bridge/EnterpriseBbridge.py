##############################################################################
#	Filename:	EnterpriseBbridge.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	This contains the code to create and configure the EnterpriseB class bridge.
#	It is only called by LoadBridge.Initialize("EnterpriseBbridge"), so don't
#	call these functions directly
#
#	Created:	9/12/00 -	DLitwin
###############################################################################
import App

#NonSerializedObjects = ( "debug", )

#debug = App.CPyDebug(__name__).Print
#debug("Loading " + __name__ + " module...")

###############################################################################
#	CreateBridgeModel()
#
#	Create the EnterpriseB bridge model, viewscreen and main camera, attaching them
#	to the Set passed in.
#
#	Args:	pBridgeSet	- The Bridge set
#
#	Return:	none
###############################################################################
def CreateBridgeModel(pBridgeSet):
	iDetail = App.g_kImageManager.GetImageDetail()
	pcDetail = [ "High/", "High/", "High/" ]
	pcEnvPath = "data/Models/Sets/EnterpriseBBridge/" + pcDetail[iDetail]

	# Pre-load the Bridge model and viewscreen
	App.g_kModelManager.LoadModel("data/Models/Sets/EnterpriseBbridge/EnterpriseBbridge.nif", None, pcEnvPath)
	App.g_kModelManager.LoadModel("data/Models/Sets/EnterpriseBbridge/EnterpriseBViewScreen.NIF", None, pcEnvPath)

	# Load the viewscreen and set it up specially with SetViewScreen()
	pViewScreen = App.ViewScreenObject_Create("data/Models/Sets/EnterpriseBbridge/EnterpriseBViewScreen.NIF")
	pBridgeSet.SetViewScreen(pViewScreen, "viewscreen")

	# Setup bridge object
	pBridgeObject = App.BridgeObjectClass_Create("data/Models/Sets/EnterpriseBbridge/EnterpriseBbridge.nif")
	pBridgeSet.AddObjectToSet(pBridgeObject, "bridge")
	pBridgeObject.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	pBridgeObject.SetAngleAxisRotation(0.000000, 1.000000, 0.000000, 0.000000)

	# setup hardpoints for dbridge.
	pPropertySet = pBridgeObject.GetPropertySet()
	import Bridge.EnterpriseBBridgeProperties
	App.g_kModelPropertyManager.ClearLocalTemplates()
	reload(Bridge.EnterpriseBBridgeProperties)
	Bridge.EnterpriseBBridgeProperties.LoadPropertySet(pPropertySet)


	# Create camera
	lPos = GetBaseCameraPosition()
	pCamera = App.ZoomCameraObjectClass_Create(lPos[0], lPos[1], lPos[2], 1.570796, -0.000665, -0.087559, 0.996159, "maincamera")
	pCamera.SetMinZoom(0.8)
	pCamera.SetMaxZoom(1.0)
	pCamera.SetZoomTime(0.375)
	pBridgeSet.AddCameraToSet(pCamera, "maincamera")
	pCamera.Update( App.g_kUtopiaModule.GetGameTime() )
	App.g_kVarManager.SetFloatVariable("global", "fZoomTuneState", 0)

	# Load EnterpriseB bridge specific sounds
	LoadSounds()

	App.g_kModelPropertyManager.ClearLocalTemplates()

###############################################################################
#	GetBaseCameraPosition
#	
#	Get the normal camera position for this bridge.
#	
#	Args:	None
#	
#	Return:	A tuple with the (x,y,z) location for the base camera position.
###############################################################################
def GetBaseCameraPosition():
	return (5, 90, 70)

###############################################################################
#	AdjustCameraPositionForBridge
#	
#	Adjust the position of the camera, based on the horizontal
#	angle it's facing, based on the bridge that it's on.
#	
#	Args:	fHorizAngle
#	
#	Return:	The adjusted camera position.
###############################################################################
def AdjustCameraPositionForBridge(pCamera, fHorizAngle):
	vLocation = App.TGPoint3()
	apply(vLocation.SetXYZ, GetBaseCameraPosition())
	return vLocation

###############################################################################
#	ConfigureCharacters()
#
#	Configure the bridge crew to the set, which adds bridge specific animations
#	to them.
#
#	Args:	pBridgeSet	- The Bridge set
#
#	Return:	none
###############################################################################
def ConfigureCharacters(pBridgeSet):
	# Configure bridge characters to our bridge
	import Bridge.Characters.ENBFelix
	import Bridge.Characters.ENBKiska
	import Bridge.Characters.ENBSaffi
	import Bridge.Characters.ENBBrex
	import Bridge.Characters.ENBMiguel

	import Bridge.Characters.ENBFemaleExtra1
	import Bridge.Characters.ENBFemaleExtra2
	import Bridge.Characters.ENBFemaleExtra3
	import Bridge.Characters.ENBMaleExtra1
	import Bridge.Characters.ENBMaleExtra2
	import Bridge.Characters.ENBMaleExtra3

	pENBFelix = App.CharacterClass_Cast(pBridgeSet.GetObject("Tactical"))
	pENBKiska = App.CharacterClass_Cast(pBridgeSet.GetObject("Helm"))
	pENBSaffi = App.CharacterClass_Cast(pBridgeSet.GetObject("XO"))
	pENBMiguel = App.CharacterClass_Cast(pBridgeSet.GetObject("Science"))
	pENBBrex = App.CharacterClass_Cast(pBridgeSet.GetObject("Engineer"))

	pENBFemaleExtra1 = App.CharacterClass_Cast(pBridgeSet.GetObject("FemaleExtra1"))
	pENBFemaleExtra2 = App.CharacterClass_Cast(pBridgeSet.GetObject("FemaleExtra2"))
	pENBFemaleExtra3 = App.CharacterClass_Cast(pBridgeSet.GetObject("FemaleExtra3"))

	pENBMaleExtra1 = App.CharacterClass_Cast(pBridgeSet.GetObject("MaleExtra1"))
	pENBMaleExtra2 = App.CharacterClass_Cast(pBridgeSet.GetObject("MaleExtra2"))
	pENBMaleExtra3 = App.CharacterClass_Cast(pBridgeSet.GetObject("MaleExtra3"))

	Bridge.Characters.ENBFelix.ConfigureForEnterpriseB(pENBFelix)
	Bridge.Characters.ENBKiska.ConfigureForEnterpriseB(pENBKiska)
	Bridge.Characters.ENBSaffi.ConfigureForEnterpriseB(pENBSaffi)
	Bridge.Characters.ENBMiguel.ConfigureForEnterpriseB(pENBMiguel)
	Bridge.Characters.ENBBrex.ConfigureForEnterpriseB(pENBBrex)

	if (pENBFemaleExtra1):
		Bridge.Characters.ENBFemaleExtra1.ConfigureForEnterpriseB(pENBFemaleExtra1)
	if (pENBFemaleExtra2):
		Bridge.Characters.ENBFemaleExtra2.ConfigureForEnterpriseB(pENBFemaleExtra2)
	if (pENBFemaleExtra3):
		Bridge.Characters.ENBFemaleExtra3.ConfigureForEnterpriseB(pENBFemaleExtra3)
	if (pENBMaleExtra1):
		Bridge.Characters.ENBMaleExtra1.ConfigureForEnterpriseB(pENBMaleExtra1)
	if (pENBMaleExtra2):
		Bridge.Characters.ENBMaleExtra2.ConfigureForEnterpriseB(pENBMaleExtra2)
	if (pENBMaleExtra3):
		Bridge.Characters.ENBMaleExtra3.ConfigureForEnterpriseB(pENBMaleExtra3)

	pCamera = App.ZoomCameraObjectClass_GetObject(pBridgeSet, "maincamera")
	pCamera.SetTranslateXYZ(5, 90, 70)


###############################################################################
#	LoadSounds()
#
#	Load any EnterpriseB bridge specific sounds
#
#	Args:	none
#
#	Return:	none
###############################################################################
def LoadSounds():

#	debug("Loading EnterpriseB door sound")

	pGame = App.Game_GetCurrentGame()
	pGame.LoadSoundInGroup("sfx/TMP-door.wav",  "LiftDoor", "BridgeGeneric")

#	debug("Loading EnterpriseB hail sound")

	pGame = App.Game_GetCurrentGame()
	pGame.LoadSoundInGroup("sfx/TMP-hail.wav",  "Hail", "BridgeGeneric")

#	debug("Loading EnterpriseB Ambient sound")

	pGame = App.Game_GetCurrentGame()
	pGame.LoadSoundInGroup("sfx/TMP-bridge2.loop.wav",  "AmbBridge", "BridgeGeneric")


###############################################################################
#	UnloadSounds()
#
#	Unload any EnterpriseB bridge specific sounds
#
#	Args:	none
#
#	Return:	none
###############################################################################
def UnloadSounds():
	App.g_kSoundManager.DeleteSound("LiftDoor")
	App.g_kSoundManager.DeleteSound("Hail")
	App.g_kSoundManager.DeleteSound("AmbBridge")


###############################################################################
#	PreloadAnimations()
#
#	Load any EnterpriseB bridge specific animations that are common
#
#	Args:	none
#
#	Return:	none
###############################################################################
def PreloadAnimations ():
	kAM = App.g_kAnimationManager

	kAM.LoadAnimation ("data/animations/ENB_door_L1.nif", "ENB_Door_L1")
	kAM.LoadAnimation ("data/animations/ENB_door_L2.nif", "ENB_Door_L2")

	# Small animations
	# Science Movement
	kAM.LoadAnimation ("data/animations/ENB_stand_s_s.nif", "ENB_stand_s_s")
	kAM.LoadAnimation ("data/animations/ENB_seated_s_s.nif", "ENB_seated_s_s")
	kAM.LoadAnimation ("data/animations/ENB_face_capt_s.nif", "ENB_face_capt_s")
	kAM.LoadAnimation ("data/animations/ENB_chair_s_face_capt.nif", "ENB_chair_s_face_capt")
	kAM.LoadAnimation ("data/animations/ENB_face_capt_s_reverse.nif", "ENB_face_capt_s_reverse")
	kAM.LoadAnimation ("data/animations/ENB_chair_s_face_capt_reverse.nif", "ENB_chair_s_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/EB_chair_S_in.nif", "EB_chair_S_in")

	# Science Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/ENB_S_pushing_buttons_A.NIF", "ENB_S_pushing_buttons_A")
	kAM.LoadAnimation ("data/animations/ENB_S_pushing_buttons_B.NIF", "ENB_S_pushing_buttons_B")
	kAM.LoadAnimation ("data/animations/ENB_S_pushing_buttons_C.NIF", "ENB_S_pushing_buttons_C")
	kAM.LoadAnimation ("data/animations/ENB_S_pushing_buttons_D.NIF", "ENB_S_pushing_buttons_D")

	# Science Talking to other stations

	# Engineer Movement
	kAM.LoadAnimation ("data/animations/ENB_stand_e_s.nif", "ENB_stand_e_s")
	kAM.LoadAnimation ("data/animations/ENB_seated_e_s.nif", "ENB_seated_e_s")
	kAM.LoadAnimation ("data/animations/ENB_face_capt_e.nif", "ENB_face_capt_e")
	kAM.LoadAnimation ("data/animations/ENB_chair_e_face_capt.nif", "ENB_chair_e_face_capt")
	kAM.LoadAnimation ("data/animations/ENB_face_capt_e_reverse.nif", "ENB_face_capt_e_reverse")
	kAM.LoadAnimation ("data/animations/ENB_chair_e_face_capt_reverse.nif", "ENB_chair_e_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/EB_chair_E_in.nif", "EB_chair_E_in")

	# Engineer Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/ENB_E_pushing_buttons_A.NIF", "ENB_E_pushing_buttons_A")
	kAM.LoadAnimation ("data/animations/ENB_E_pushing_buttons_B.NIF", "ENB_E_pushing_buttons_B")
	kAM.LoadAnimation ("data/animations/ENB_E_pushing_buttons_C.NIF", "ENB_E_pushing_buttons_C")
	kAM.LoadAnimation ("data/animations/ENB_E_pushing_buttons_D.NIF", "ENB_E_pushing_buttons_D")

	# Engineer Talking to other stations

	# 
	# medium animations
	# Helm Movement
	kAM.LoadAnimation ("data/animations/ENB_stand_h_m.nif", "ENB_stand_h_m")
	kAM.LoadAnimation ("data/animations/ENB_seated_h_m.nif", "ENB_seated_h_m")
	kAM.LoadAnimation ("data/animations/ENB_face_capt_h.nif", "ENB_face_capt_h")
	kAM.LoadAnimation ("data/animations/ENB_chair_H_face_capt.nif", "ENB_chair_H_face_capt")
	kAM.LoadAnimation ("data/animations/ENB_face_capt_h_reverse.nif", "ENB_face_capt_h_reverse")
	kAM.LoadAnimation ("data/animations/ENB_chair_H_face_capt_reverse.nif", "ENB_chair_H_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/EB_glance_h_m.nif", "ENB_glance_h_m")
	kAM.LoadAnimation ("data/animations/EB_glance_h_m_reverse.nif", "ENB_glance_h_m_reverse")

	kAM.LoadAnimation ("data/animations/EB_hit_h.NIF", "ENB_hit_h")


	# Helm Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/ENB_H_pushing_buttons_A.NIF", "ENB_H_pushing_buttons_A")
	kAM.LoadAnimation ("data/animations/ENB_H_pushing_buttons_B.NIF", "ENB_H_pushing_buttons_B")
	kAM.LoadAnimation ("data/animations/ENB_H_pushing_buttons_C.NIF", "ENB_H_pushing_buttons_C")
	kAM.LoadAnimation ("data/animations/ENB_H_pushing_buttons_D.NIF", "ENB_H_pushing_buttons_D")

	# Helm Talking to other stations
	kAM.LoadAnimation ("data/animations/EB_H_Talk_to_C_M.NIF", "EB_H_Talk_to_C_M")
	kAM.LoadAnimation ("data/animations/EB_H_Talk_to_E_M.NIF", "EB_H_Talk_to_E_M")
	kAM.LoadAnimation ("data/animations/EB_H_Talk_to_S_M.NIF", "EB_H_Talk_to_S_M")
	kAM.LoadAnimation ("data/animations/EB_H_Talk_to_T_M.NIF", "EB_H_Talk_to_T_M")
	kAM.LoadAnimation ("data/animations/EB_H_Talk_fin_C_M.NIF", "EB_H_Talk_fin_C_M")
	kAM.LoadAnimation ("data/animations/EB_H_Talk_fin_E_M.NIF", "EB_H_Talk_fin_E_M")
	kAM.LoadAnimation ("data/animations/EB_H_Talk_fin_S_M.NIF", "EB_H_Talk_fin_S_M")
	kAM.LoadAnimation ("data/animations/EB_H_Talk_fin_T_M.NIF", "EB_H_Talk_fin_T_M")

	# XO Movement
	kAM.LoadAnimation ("data/animations/ENB_seated_C_M.nif", "ENB_seated_c_m")
	kAM.LoadAnimation ("data/animations/ENB_seatedm_C_M.nif", "ENB_seatedm_c_m")
	kAM.LoadAnimation ("data/animations/ENB_stand_V_M.nif", "ENB_stand_c_m")
	kAM.LoadAnimation ("data/animations/ENB_face_capt_c1.nif", "ENB_face_capt_c1")
	kAM.LoadAnimation ("data/animations/ENB_face_capt_c.nif", "ENB_face_capt_c")
	kAM.LoadAnimation ("data/animations/ENB_face_capt_C_reverse.NIF", "ENB_face_capt_C_reverse")
	kAM.LoadAnimation ("data/animations/ENB_face_capt_c1_reverse.NIF", "ENB_face_capt_c1_reverse")
	kAM.LoadAnimation ("data/animations/EB_hit_c.NIF", "Int_hit_c")

	#Commander interaction
	kAM.LoadAnimation ("data/animations/ENB_C_pushing_buttons_A.NIF", "ENB_C_pushing_buttons_A")
	kAM.LoadAnimation ("data/animations/ENB_C_pushing_buttons_B.NIF", "ENB_C_pushing_buttons_B")
	kAM.LoadAnimation ("data/animations/ENB_C_pushing_buttons_C.NIF", "ENB_C_pushing_buttons_C")
	kAM.LoadAnimation ("data/animations/ENB_C_pushing_buttons_D.NIF", "ENB_C_pushing_buttons_D")

	kAM.LoadAnimation ("data/animations/EB_X_pushing_buttons_A.NIF", "EB_X_pushing_buttons_A")
	kAM.LoadAnimation ("data/animations/EB_X_pushing_buttons_B.NIF", "EB_X_pushing_buttons_B")
	kAM.LoadAnimation ("data/animations/EB_X_pushing_buttons_C.NIF", "EB_X_pushing_buttons_C")
	kAM.LoadAnimation ("data/animations/EB_X_pushing_buttons_D.NIF", "EB_X_pushing_buttons_D")
	kAM.LoadAnimation ("data/animations/EB_X_pushing_buttons_E.NIF", "EB_X_pushing_buttons_E")
	kAM.LoadAnimation ("data/animations/EB_X_pushing_buttons_F.NIF", "EB_X_pushing_buttons_F")
	kAM.LoadAnimation ("data/animations/EB_X_pushing_buttons_G.NIF", "EB_X_pushing_buttons_G")

	# XO Talking to other stations
	kAM.LoadAnimation ("data/animations/EB_C_Talk_E_M.NIF", "EB_C_Talk_E_M")
	kAM.LoadAnimation ("data/animations/EB_C_Talk_G2_M.NIF", "EB_C_Talk_G2_M")
	kAM.LoadAnimation ("data/animations/EB_C_Talk_G3_M.NIF", "EB_C_Talk_G3_M")
	kAM.LoadAnimation ("data/animations/EB_C_Talk_TH_M.NIF", "EB_C_Talk_TH_M")
	kAM.LoadAnimation ("data/animations/EB_C_Talk_S_M.NIF", "EB_C_Talk_S_M")

	# Guest Animations
	kAM.LoadAnimation ("data/animations/EB_L1toX_M.nif", "EB_L1toX_M")
	kAM.LoadAnimation ("data/animations/EB_seated_X_m.nif", "EB_seated_X_m")
	kAM.LoadAnimation ("data/animations/EB_face_capt_X.nif", "EB_face_capt_X")
	kAM.LoadAnimation ("data/animations/EB_face_capt_X_reverse.NIF", "EB_face_capt_X_reverse")
	kAM.LoadAnimation ("data/animations/EB_hit_x.NIF", "ENB_hit_x")

	# Extras
	kAM.LoadAnimation ("data/animations/ENB_L1toG3_S.nif", "ENB_L1toG3_S")
	kAM.LoadAnimation ("data/animations/ENB_L1toG3_M.nif", "ENB_L1toG3_M")
	kAM.LoadAnimation ("data/animations/ENB_L1toG3_L.nif", "ENB_L1toG3_L")

	kAM.LoadAnimation ("data/animations/ENB_L2toG1_S.nif", "ENB_L2toG1_S")
	kAM.LoadAnimation ("data/animations/ENB_L2toG1_M.nif", "ENB_L2toG1_M")
	kAM.LoadAnimation ("data/animations/ENB_L2toG1_L.nif", "ENB_L2toG1_L")

	kAM.LoadAnimation ("data/animations/ENB_L2toG2_S.nif", "ENB_L2toG2_S")
	kAM.LoadAnimation ("data/animations/ENB_L2toG2_M.nif", "ENB_L2toG2_M")
	kAM.LoadAnimation ("data/animations/ENB_L2toG2_L.nif", "ENB_L2toG2_L")

	kAM.LoadAnimation ("data/animations/ENB_G1toL2_S.nif", "ENB_G1toL2_S")
	kAM.LoadAnimation ("data/animations/ENB_G1toL2_M.nif", "ENB_G1toL2_M")
	kAM.LoadAnimation ("data/animations/ENB_G1toL2_L.nif", "ENB_G1toL2_L")
	
	kAM.LoadAnimation ("data/animations/ENB_G2toL2_S.nif", "ENB_G2toL2_S")
	kAM.LoadAnimation ("data/animations/ENB_G2toL2_M.nif", "ENB_G2toL2_M")
	kAM.LoadAnimation ("data/animations/ENB_G2toL2_L.nif", "ENB_G2toL2_L")
	
	kAM.LoadAnimation ("data/animations/ENB_G3toL1_S.nif", "ENB_G3toL1_S")
	kAM.LoadAnimation ("data/animations/ENB_G3toL1_M.nif", "ENB_G3toL1_M")
	kAM.LoadAnimation ("data/animations/ENB_G3toL1_L.nif", "ENB_G3toL1_L")


	# Large animations
	# Tactical Movement
	kAM.LoadAnimation ("data/animations/ENB_stand_t_l.nif", "ENB_stand_t_l")
	kAM.LoadAnimation ("data/animations/ENB_seated_t_l.nif", "ENB_seated_t_l")
	kAM.LoadAnimation ("data/animations/ENB_seatedm_t_l.nif", "ENB_seatedm_t_l")
	kAM.LoadAnimation ("data/animations/ENB_face_capt_t.nif", "ENB_face_capt_t")
	kAM.LoadAnimation ("data/animations/ENB_chair_T_face_capt.nif", "ENB_chair_T_face_capt")
	kAM.LoadAnimation ("data/animations/ENB_face_capt_t_reverse.nif", "ENB_face_capt_t_reverse")
	kAM.LoadAnimation ("data/animations/ENB_chair_T_face_capt_reverse.nif", "ENB_chair_T_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/EB_hit_t.NIF", "EB_hit_t")

	# Tactical Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/ENB_T_pushing_buttons_A.NIF", "ENB_T_pushing_buttons_A")
	kAM.LoadAnimation ("data/animations/ENB_T_pushing_buttons_B.NIF", "ENB_T_pushing_buttons_B")
	kAM.LoadAnimation ("data/animations/ENB_T_pushing_buttons_C.NIF", "ENB_T_pushing_buttons_C")
	kAM.LoadAnimation ("data/animations/ENB_T_pushing_buttons_D.NIF", "ENB_T_pushing_buttons_D")

	# Tactical Talking to other stations
	kAM.LoadAnimation ("data/animations/EB_T_Talk_to_H_L.NIF", "EB_T_Talk_to_H_L")
	kAM.LoadAnimation ("data/animations/EB_T_Talk_to_G2_L.NIF", "EB_T_Talk_to_G2_L")
	kAM.LoadAnimation ("data/animations/EB_T_Talk_to_G3_L.NIF", "EB_T_Talk_to_G3_L")

	kAM.LoadAnimation ("data/animations/EB_T_Talk_fin_H_L.NIF", "EB_T_Talk_fin_H_L")
	kAM.LoadAnimation ("data/animations/EB_T_Talk_fin_G2_L.NIF", "EB_T_Talk_fin_G2_L")
	kAM.LoadAnimation ("data/animations/EB_T_Talk_fin_G3_L.NIF", "EB_T_Talk_fin_G3_L")

	return

###############################################################################
#	UnloadAnimations()
#
#	Unload any EnterpriseB bridge specific animations that are common
#
#	Args:	none
#
#	Return:	none
###############################################################################
def UnloadAnimations ():
	kAM = App.g_kAnimationManager

	kAM.FreeAnimation("ENB_Door_L1")
	kAM.FreeAnimation("ENB_Door_L2")

	# Small animations
	# Science Movement
	kAM.FreeAnimation("ENB_stand_s_s")
	kAM.FreeAnimation("ENB_seated_s_s")
	kAM.FreeAnimation("ENB_face_capt_s")
	kAM.FreeAnimation("ENB_chair_s_face_capt")
	kAM.FreeAnimation("ENB_face_capt_s_reverse")
	kAM.FreeAnimation("ENB_chair_s_face_capt_reverse")
	kAM.FreeAnimation("EB_chair_S_in")

	# Science Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/ENB_S_pushing_buttons_A.NIF", "ENB_S_pushing_buttons_A")
	kAM.LoadAnimation ("data/animations/ENB_S_pushing_buttons_B.NIF", "ENB_S_pushing_buttons_B")
	kAM.LoadAnimation ("data/animations/ENB_S_pushing_buttons_C.NIF", "ENB_S_pushing_buttons_C")
	kAM.LoadAnimation ("data/animations/ENB_S_pushing_buttons_D.NIF", "ENB_S_pushing_buttons_D")

	# Science Talking to other stations

	# Engineer Movement
	kAM.FreeAnimation("ENB_stand_e_s")
	kAM.FreeAnimation("ENB_seated_e_s")
	kAM.FreeAnimation("ENB_face_capt_e")
	kAM.FreeAnimation("ENB_chair_e_face_capt")
	kAM.FreeAnimation("ENB_face_capt_e_reverse")
	kAM.FreeAnimation("ENB_chair_e_face_capt_reverse")
	kAM.FreeAnimation("EB_chair_E_in")

	# Engineer Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/ENB_E_pushing_buttons_A.NIF", "ENB_E_pushing_buttons_A")
	kAM.LoadAnimation ("data/animations/ENB_E_pushing_buttons_B.NIF", "ENB_E_pushing_buttons_B")
	kAM.LoadAnimation ("data/animations/ENB_E_pushing_buttons_C.NIF", "ENB_E_pushing_buttons_C")
	kAM.LoadAnimation ("data/animations/ENB_E_pushing_buttons_D.NIF", "ENB_E_pushing_buttons_D")

	# Engineer Talking to other stations

	# medium animations
	# Helm Movement
	kAM.FreeAnimation("ENB_stand_h_m")
	kAM.FreeAnimation("ENB_seated_h_m")
	kAM.FreeAnimation("ENB_face_capt_h")
	kAM.FreeAnimation("ENB_face_capt_h_reverse")
	kAM.FreeAnimation("EB_hit_h")


	# Helm Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/ENB_H_pushing_buttons_A.NIF", "ENB_H_pushing_buttons_A")
	kAM.LoadAnimation ("data/animations/ENB_H_pushing_buttons_B.NIF", "ENB_H_pushing_buttons_B")
	kAM.LoadAnimation ("data/animations/ENB_H_pushing_buttons_C.NIF", "ENB_H_pushing_buttons_C")
	kAM.LoadAnimation ("data/animations/ENB_H_pushing_buttons_D.NIF", "ENB_H_pushing_buttons_D")

	# Helm Talking to other stations
	kAM.FreeAnimation("EB_H_Talk_to_C_M")
	kAM.FreeAnimation("EB_H_Talk_to_E_M")
	kAM.FreeAnimation("EB_H_Talk_to_S_M")
	kAM.FreeAnimation("EB_H_Talk_to_T_M")
	kAM.FreeAnimation("EB_H_Talk_fin_C_M")
	kAM.FreeAnimation("EB_H_Talk_fin_E_M")
	kAM.FreeAnimation("EB_H_Talk_fin_S_M")
	kAM.FreeAnimation("EB_H_Talk_fin_T_M")

	# XO Movement
	kAM.FreeAnimation("ENB_seated_c_m")
	kAM.FreeAnimation("ENB_seatedm_c_m")
	kAM.FreeAnimation("ENB_stand_c_m")
	kAM.FreeAnimation("ENB_face_capt_c1")
	kAM.FreeAnimation("ENB_face_capt_c")
	kAM.FreeAnimation("ENB_face_capt_C_reverse")
	kAM.FreeAnimation("ENB_face_capt_c1_reverse")
	kAM.FreeAnimation("ENB_hit_c")
	kAM.FreeAnimation("ENB_stand_D_M")
	kAM.FreeAnimation("ENB_seated_D_M")


	# XO Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/ENB_C_pushing_buttons_A.NIF", "ENB_C_pushing_buttons_A")
	kAM.LoadAnimation ("data/animations/ENB_C_pushing_buttons_B.NIF", "ENB_C_pushing_buttons_B")
	kAM.LoadAnimation ("data/animations/ENB_C_pushing_buttons_C.NIF", "ENB_C_pushing_buttons_C")
	kAM.LoadAnimation ("data/animations/ENB_C_pushing_buttons_D.NIF", "ENB_C_pushing_buttons_D")

	# XO Talking to other stations
	kAM.FreeAnimation("EB_C_Talk_E_M")
	kAM.FreeAnimation("EB_C_Talk_H_M")
	kAM.FreeAnimation("EB_C_Talk_T_M")
	kAM.FreeAnimation("EB_C_Talk_S_M")

	# Guest Animations
	kAM.FreeAnimation("EB_L1toX_M")
	kAM.FreeAnimation("EB_seated_X_m")
	kAM.FreeAnimation("EB_face_capt_X")
	kAM.FreeAnimation("EB_face_capt_X_reverse")
	kAM.FreeAnimation("ENB_hit_x")

	kAM.FreeAnimation("EB_X_pushing_buttons_A")
	kAM.FreeAnimation("EB_X_pushing_buttons_B")
	kAM.FreeAnimation("EB_X_pushing_buttons_C")
	kAM.FreeAnimation("EB_X_pushing_buttons_D")
	kAM.FreeAnimation("EB_X_pushing_buttons_E")
	kAM.FreeAnimation("EB_X_pushing_buttons_F")
	kAM.FreeAnimation("EB_X_pushing_buttons_G")

	#Extra
	kAM.FreeAnimation("ENB_L1toG3_S")
	kAM.FreeAnimation("ENB_L1toG3_M")
	kAM.FreeAnimation("ENB_L1toG3_L")

	kAM.FreeAnimation("ENB_L2toG1_S")
	kAM.FreeAnimation("ENB_L2toG1_M")
	kAM.FreeAnimation("ENB_L2toG1_L")

	kAM.FreeAnimation("ENB_L2toG2_S")
	kAM.FreeAnimation("ENB_L2toG2_M")
	kAM.FreeAnimation("ENB_L2toG2_L")

	kAM.FreeAnimation("ENB_G1toL2_S")
	kAM.FreeAnimation("ENB_G1toL2_M")
	kAM.FreeAnimation("ENB_G1toL2_L")
	
	kAM.FreeAnimation("ENB_G2toL2_S")
	kAM.FreeAnimation("ENB_G2toL2_M")
	kAM.FreeAnimation("ENB_G2toL2_L")
	
	kAM.FreeAnimation("ENB_G3toL1_S")
	kAM.FreeAnimation("ENB_G3toL1_M")
	kAM.FreeAnimation("ENB_G3toL1_L")
	
	# Large animations
	# Tactical Movement
	kAM.FreeAnimation("ENB_stand_t_l")
	kAM.FreeAnimation("ENB_seated_t_l")
	kAM.FreeAnimation("ENB_seatedm_t_l")
	kAM.FreeAnimation("ENB_face_capt_t")
	kAM.FreeAnimation("ENB_chair_T_face_capt")
	kAM.FreeAnimation("ENB_face_capt_t_reverse")
	kAM.FreeAnimation("ENB_chair_T_face_capt_reverse")
	kAM.FreeAnimation("ENB_hit_t")

	# Tactical Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/ENB_T_pushing_buttons_A.NIF", "ENB_T_pushing_buttons_A")
	kAM.LoadAnimation ("data/animations/ENB_T_pushing_buttons_B.NIF", "ENB_T_pushing_buttons_B")
	kAM.LoadAnimation ("data/animations/ENB_T_pushing_buttons_C.NIF", "ENB_T_pushing_buttons_C")
	kAM.LoadAnimation ("data/animations/ENB_T_pushing_buttons_D.NIF", "ENB_T_pushing_buttons_D")

	# Tactical Talking to other stations
	kAM.FreeAnimation("EB_T_Talk_to_H_L")
	kAM.FreeAnimation("EB_T_Talk_to_G2_L")
	kAM.FreeAnimation("EB_T_Talk_to_G3_L")

	kAM.FreeAnimation("EB_T_Talk_fin_H_L")
	kAM.FreeAnimation("EB_T_Talk_fin_G2_L")
	kAM.FreeAnimation("EB_T_Talk_fin_G3_L")


	return

##############################################################################
#	Filename:	EnterpriseCbridge.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	This contains the code to create and configure the Yamaguchi class bridge.
#	It is only called by LoadBridge.Initialize("EnterpriseCbridge"), so don't
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
#	Create the Enteprise C bridge model, viewscreen and main camera, attaching them
#	to the Set passed in.
#
#	Args:	pBridgeSet	- The Bridge set
#
#	Return:	none
###############################################################################
def CreateBridgeModel(pBridgeSet):
	iDetail = App.g_kImageManager.GetImageDetail()
	pcDetail = [ "Low/", "Medium/", "High/" ]
	pcEnvPath = "data/Models/Sets/AmbassadorBridge/" + pcDetail[iDetail]

	# Pre-load the Bridge model and viewscreen
	App.g_kModelManager.LoadModel("data/Models/Sets/AmbassadorBridge/Yamaguchi.NIF", None, pcEnvPath)
	App.g_kModelManager.LoadModel("data/Models/Sets/AmbassadorBridge/YamaguchiViewScreen.NIF", None, pcEnvPath)

	# Load the viewscreen and set it up specially with SetViewScreen()
	pViewScreen = App.ViewScreenObject_Create("data/Models/Sets/AmbassadorBridge/YamaguchiViewScreen.NIF")
	pBridgeSet.SetViewScreen(pViewScreen, "viewscreen")

	# Setup bridge object
	pBridgeObject = App.BridgeObjectClass_Create("data/Models/Sets/AmbassadorBridge/Yamaguchi.NIF")
	pBridgeSet.AddObjectToSet(pBridgeObject, "bridge")
	pBridgeObject.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	pBridgeObject.SetAngleAxisRotation(0.000000, 1.000000, 0.000000, 0.000000)

	# setup hardpoints for dbridge.
	pPropertySet = pBridgeObject.GetPropertySet()
	import Bridge.AmbassadorBridgeProperties
	App.g_kModelPropertyManager.ClearLocalTemplates()
	reload(Bridge.AmbassadorBridgeProperties)
	Bridge.AmbassadorBridgeProperties.LoadPropertySet(pPropertySet)


	# Create camera
	lPos = GetBaseCameraPosition()
	pCamera = App.ZoomCameraObjectClass_Create(lPos[0], lPos[1], lPos[2], 1.570796, -0.000665, -0.087559, 0.996159, "maincamera")
	pCamera.SetMinZoom(0.8)
	pCamera.SetMaxZoom(1.0)
	pCamera.SetZoomTime(0.375)
	pBridgeSet.AddCameraToSet(pCamera, "maincamera")
	pCamera.Update( App.g_kUtopiaModule.GetGameTime() )
	App.g_kVarManager.SetFloatVariable("global", "fZoomTuneState", 0)

	# Load Yamaguchi bridge specific sounds
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
	return (-28.75, -28.1501, 10)

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
	import Bridge.Characters.AmbFelix
	import Bridge.Characters.AmbKiska
	import Bridge.Characters.AmbTNGSaffi
	import Bridge.Characters.AmbBrex
	import Bridge.Characters.AmbMiguel

	import Bridge.Characters.AmbFemaleExtra1
	import Bridge.Characters.AmbFemaleExtra2
	import Bridge.Characters.AmbFemaleExtra3
	import Bridge.Characters.AmbMaleExtra1
	import Bridge.Characters.AmbMaleExtra2
	import Bridge.Characters.AmbMaleExtra3

	pAmbFelix = App.CharacterClass_Cast(pBridgeSet.GetObject("Tactical"))
	pAmbKiska = App.CharacterClass_Cast(pBridgeSet.GetObject("Helm"))
	pAmbTNGSaffi = App.CharacterClass_Cast(pBridgeSet.GetObject("XO"))
	pAmbMiguel = App.CharacterClass_Cast(pBridgeSet.GetObject("Science"))
	pAmbBrex = App.CharacterClass_Cast(pBridgeSet.GetObject("Engineer"))

	pAmbFemaleExtra1 = App.CharacterClass_Cast(pBridgeSet.GetObject("FemaleExtra1"))
	pAmbFemaleExtra2 = App.CharacterClass_Cast(pBridgeSet.GetObject("FemaleExtra2"))
	pAmbFemaleExtra3 = App.CharacterClass_Cast(pBridgeSet.GetObject("FemaleExtra3"))

	pAmbMaleExtra1 = App.CharacterClass_Cast(pBridgeSet.GetObject("MaleExtra1"))
	pAmbMaleExtra2 = App.CharacterClass_Cast(pBridgeSet.GetObject("MaleExtra2"))
	pAmbMaleExtra3 = App.CharacterClass_Cast(pBridgeSet.GetObject("MaleExtra3"))

	Bridge.Characters.AmbFelix.ConfigureForAmbassador(pAmbFelix)
	Bridge.Characters.AmbKiska.ConfigureForAmbassador(pAmbKiska)
	Bridge.Characters.AmbTNGSaffi.ConfigureForAmbassador(pAmbTNGSaffi)
	Bridge.Characters.AmbMiguel.ConfigureForAmbassador(pAmbMiguel)
	Bridge.Characters.AmbBrex.ConfigureForAmbassador(pAmbBrex)

	if (pAmbFemaleExtra1):
		Bridge.Characters.AmbFemaleExtra1.ConfigureForAmbassador(pAmbFemaleExtra1)
	if (pAmbFemaleExtra2):
		Bridge.Characters.AmbFemaleExtra2.ConfigureForAmbassador(pAmbFemaleExtra2)
	if (pAmbFemaleExtra3):
		Bridge.Characters.AmbFemaleExtra3.ConfigureForAmbassador(pAmbFemaleExtra3)
	if (pAmbMaleExtra1):
		Bridge.Characters.AmbMaleExtra1.ConfigureForAmbassador(pAmbMaleExtra1)
	if (pAmbMaleExtra2):
		Bridge.Characters.AmbMaleExtra2.ConfigureForAmbassador(pAmbMaleExtra2)
	if (pAmbMaleExtra3):
		Bridge.Characters.AmbMaleExtra3.ConfigureForAmbassador(pAmbMaleExtra3)

	pCamera = App.ZoomCameraObjectClass_GetObject(pBridgeSet, "maincamera")
	pCamera.SetTranslateXYZ(-28.75, -28.1501, 10)



###############################################################################
#	LoadSounds()
#
#	Load any Ambassador bridge specific sounds
#
#	Args:	none
#
#	Return:	none
###############################################################################
def LoadSounds():

#	debug("Loading Ambassador door sound")

	pGame = App.Game_GetCurrentGame()
	pGame.LoadSoundInGroup("sfx/door.wav",  "LiftDoor", "BridgeGeneric")


###############################################################################
#	UnloadSounds()
#
#	Unload any Ambassador bridge specific sounds
#
#	Args:	none
#
#	Return:	none
###############################################################################
def UnloadSounds():
	App.g_kSoundManager.DeleteSound("LiftDoor")


###############################################################################
#	PreloadAnimations()
#
#	Load any Ambassador bridge specific animations that are common
#
#	Args:	none
#
#	Return:	none
###############################################################################
def PreloadAnimations ():
	kAM = App.g_kAnimationManager

	kAM.LoadAnimation ("data/animations/AmbTNG_door_L1.NIF", "Amb_Door_L1")
	kAM.LoadAnimation ("data/animations/AmbTNG_door_L2.nif", "Amb_Door_L2")

	# Small animations
	# Science Movement
	kAM.LoadAnimation ("data/animations/Amb_stand_s_s.nif", "Amb_stand_s_s")
	kAM.LoadAnimation ("data/animations/Amb_seated_s_s.nif", "Amb_seated_s_s")
	kAM.LoadAnimation ("data/animations/Amb_face_capt_s.nif", "Amb_face_capt_s")
	kAM.LoadAnimation ("data/animations/Amb_chair_s_face_capt.nif", "Amb_chair_s_face_capt")
	kAM.LoadAnimation ("data/animations/Amb_face_capt_s_reverse.nif", "Amb_face_capt_s_reverse")
	kAM.LoadAnimation ("data/animations/Amb_chair_s_face_capt_reverse.nif", "Amb_chair_s_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/EB_chair_S_in.nif", "EB_chair_S_in")

	# Science Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/Amb_s_pushing_buttons_A.NIF", "EB_S_pushing_buttons_seated_A")
	kAM.LoadAnimation ("data/animations/Amb_C_pushing_buttons_A.NIF", "EB_S_pushing_buttons_seated_B")
	kAM.LoadAnimation ("data/animations/Amb_e_pushing_buttons_A.NIF", "EB_S_pushing_buttons_seated_C")

	# Science Talking to other stations

	# Engineer Movement
	kAM.LoadAnimation ("data/animations/Amb_stand_e_s.nif", "Amb_stand_e_s")
	kAM.LoadAnimation ("data/animations/Amb_seated_e_s.nif", "Amb_seated_e_s")
	kAM.LoadAnimation ("data/animations/Amb_face_capt_e.nif", "Amb_face_capt_e")
	kAM.LoadAnimation ("data/animations/Amb_chair_e_face_capt.nif", "Amb_chair_e_face_capt")
	kAM.LoadAnimation ("data/animations/Amb_face_capt_e_reverse.nif", "Amb_face_capt_e_reverse")
	kAM.LoadAnimation ("data/animations/Amb_chair_e_face_capt_reverse.nif", "Amb_chair_e_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/EB_chair_E_in.nif", "EB_chair_E_in")

	# Engineer Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/Amb_e_pushing_buttons_A.NIF", "EB_E_pushing_buttons_seated_A")
	kAM.LoadAnimation ("data/animations/Amb_s_pushing_buttons_A.NIF", "EB_E_pushing_buttons_seated_B")
	kAM.LoadAnimation ("data/animations/Amb_C_pushing_buttons_A.NIF", "EB_E_pushing_buttons_seated_C")

	# Engineer Talking to other stations

	# 
	# medium animations
	# Helm Movement
	kAM.LoadAnimation ("data/animations/Amb_stand_h_m.nif", "Amb_stand_h_m")
	kAM.LoadAnimation ("data/animations/Amb_seated_h_m.nif", "Amb_seated_h_m")
	kAM.LoadAnimation ("data/animations/Amb_face_capt_h.nif", "Amb_face_capt_h")
	kAM.LoadAnimation ("data/animations/Amb_chair_H_face_capt.nif", "Amb_chair_H_face_capt")
	kAM.LoadAnimation ("data/animations/Amb_face_capt_h_reverse.nif", "Amb_face_capt_h_reverse")
	kAM.LoadAnimation ("data/animations/Amb_chair_H_face_capt_reverse.nif", "Amb_chair_H_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/EB_glance_h_m.nif", "Amb_glance_h_m")
	kAM.LoadAnimation ("data/animations/EB_glance_h_m_reverse.nif", "Amb_glance_h_m_reverse")
	kAM.LoadAnimation ("data/animations/Amb_seated_H.nif", "Amb_seated_h")
	#kAM.LoadAnimation ("data/animations/Amb_interaction_H.nif", "Amb_interaction_h")

	kAM.LoadAnimation ("data/animations/EB_hit_h.NIF", "Amb_hit_h")


	# Helm Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/Amb_H_pushing_buttons_A.NIF", "EB_H_console_slide_A")
	kAM.LoadAnimation ("data/animations/Amb_H_pushing_buttons_A.NIF", "EB_H_console_slide_B")
	kAM.LoadAnimation ("data/animations/Amb_T_pushing_buttons_A.NIF", "EB_H_console_slide_C")
	kAM.LoadAnimation ("data/animations/Amb_T_pushing_buttons_A.NIF", "EB_H_console_slide_D")

	kAM.LoadAnimation ("data/animations/Amb_H_pushing_buttons_A.NIF", "EB_H_pushing_buttons_A")
	kAM.LoadAnimation ("data/animations/Amb_H_pushing_buttons_A.NIF", "EB_H_pushing_buttons_B")
	kAM.LoadAnimation ("data/animations/Amb_H_pushing_buttons_A.NIF", "EB_H_pushing_buttons_C")
	kAM.LoadAnimation ("data/animations/Amb_T_pushing_buttons_A.NIF", "EB_H_pushing_buttons_D")
	kAM.LoadAnimation ("data/animations/Amb_T_pushing_buttons_A.NIF", "EB_H_pushing_buttons_E")
	kAM.LoadAnimation ("data/animations/Amb_T_pushing_buttons_A.NIF", "EB_H_pushing_buttons_F")

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
	kAM.LoadAnimation ("data/animations/AmbTNG_seated_C_M.nif", "AmbTNG_seated_c_m")
	kAM.LoadAnimation ("data/animations/Amb_stand_C_M.nif", "Amb_stand_c_m")
	#kAM.LoadAnimation ("data/animations/EB_face_capt_c1.nif", "Amb_face_capt_c1")
	kAM.LoadAnimation ("data/animations/AmbTNG_face_capt_c.nif", "AmbTNG_face_capt_c")
	kAM.LoadAnimation ("data/animations/AmbTNG_face_capt_C_reverse.NIF", "AmbTNG_face_capt_C_reverse")
	#kAM.LoadAnimation ("data/animations/EB_face_capt_c1_reverse.NIF", "Amb_face_capt_c1_reverse")
	kAM.LoadAnimation ("data/animations/EB_hit_c.NIF", "EB_hit_c")

	#Commander interaction
	#kAM.LoadAnimation ("data/animations/Amb_C_pushing_buttons_A.NIF", "EB_C_pushing_buttons_seated_A")
	#kAM.LoadAnimation ("data/animations/Amb_C_pushing_buttons_A.NIF", "EB_C_pushing_buttons_seated_B")
	#kAM.LoadAnimation ("data/animations/Amb_s_pushing_buttons_A.NIF", "EB_C_pushing_buttons_seated_C")
	#kAM.LoadAnimation ("data/animations/Amb_e_pushing_buttons_A.NIF", "EB_C_pushing_buttons_seated_D")
	#kAM.LoadAnimation ("data/animations/Amb_s_pushing_buttons_A.NIF", "EB_C_pushing_buttons_seated_E")
	#kAM.LoadAnimation ("data/animations/Amb_e_pushing_buttons_A.NIF", "EB_C_pushing_buttons_seated_F")
	#kAM.LoadAnimation ("data/animations/Amb_e_pushing_buttons_A.NIF", "EB_C_pushing_buttons_seated_G")

	#kAM.LoadAnimation ("data/animations/EB_X_pushing_buttons_A.NIF", "EB_X_pushing_buttons_A")
	#kAM.LoadAnimation ("data/animations/EB_X_pushing_buttons_B.NIF", "EB_X_pushing_buttons_B")
	#kAM.LoadAnimation ("data/animations/EB_X_pushing_buttons_C.NIF", "EB_X_pushing_buttons_C")
	#kAM.LoadAnimation ("data/animations/EB_X_pushing_buttons_D.NIF", "EB_X_pushing_buttons_D")
	#kAM.LoadAnimation ("data/animations/EB_X_pushing_buttons_E.NIF", "EB_X_pushing_buttons_E")
	#kAM.LoadAnimation ("data/animations/EB_X_pushing_buttons_F.NIF", "EB_X_pushing_buttons_F")
	#kAM.LoadAnimation ("data/animations/EB_X_pushing_buttons_G.NIF", "EB_X_pushing_buttons_G")

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
	kAM.LoadAnimation ("data/animations/EB_hit_x.NIF", "Amb_hit_x")

	# Extras
	kAM.LoadAnimation ("data/animations/Amb_L1toG3_S.nif", "Amb_L1toG3_S")
	kAM.LoadAnimation ("data/animations/Amb_L1toG3_M.nif", "Amb_L1toG3_M")
	kAM.LoadAnimation ("data/animations/Amb_L1toG3_L.nif", "Amb_L1toG3_L")

	# kAM.LoadAnimation ("data/animations/Amb_L2toG1_S.nif", "Amb_L2toG1_S")
	# kAM.LoadAnimation ("data/animations/Amb_L2toG1_M.nif", "Amb_L2toG1_M")
	# kAM.LoadAnimation ("data/animations/Amb_L2toG1_L.nif", "Amb_L2toG1_L")

	kAM.LoadAnimation ("data/animations/Amb_L2toG2_S.nif", "Amb_L2toG2_S")
	kAM.LoadAnimation ("data/animations/Amb_L2toG2_M.nif", "Amb_L2toG2_M")
	kAM.LoadAnimation ("data/animations/Amb_L2toG2_L.nif", "Amb_L2toG2_L")

	# kAM.LoadAnimation ("data/animations/Amb_G1toL2_S.nif", "Amb_G1toL2_S")
	# kAM.LoadAnimation ("data/animations/Amb_G1toL2_M.nif", "Amb_G1toL2_M")
	# kAM.LoadAnimation ("data/animations/Amb_G1toL2_L.nif", "Amb_G1toL2_L")
	
	kAM.LoadAnimation ("data/animations/Amb_G2toL2_S.nif", "Amb_G2toL2_S")
	kAM.LoadAnimation ("data/animations/Amb_G2toL2_M.nif", "Amb_G2toL2_M")
	kAM.LoadAnimation ("data/animations/Amb_G2toL2_L.nif", "Amb_G2toL2_L")
	
	kAM.LoadAnimation ("data/animations/Amb_G3toL1_S.nif", "Amb_G3toL1_S")
	kAM.LoadAnimation ("data/animations/Amb_G3toL1_M.nif", "Amb_G3toL1_M")
	kAM.LoadAnimation ("data/animations/Amb_G3toL1_L.nif", "Amb_G3toL1_L")


	# Large animations
	# Tactical Movement
	kAM.LoadAnimation ("data/animations/Amb_stand_t_l.nif", "Amb_stand_t_l")
	kAM.LoadAnimation ("data/animations/Amb_seated_t_l.nif", "Amb_seated_t_l")
	kAM.LoadAnimation ("data/animations/Amb_face_capt_t.nif", "Amb_face_capt_t")
	kAM.LoadAnimation ("data/animations/Amb_chair_T_face_capt.nif", "Amb_chair_T_face_capt")
	kAM.LoadAnimation ("data/animations/Amb_face_capt_t_reverse.nif", "Amb_face_capt_t_reverse")
	kAM.LoadAnimation ("data/animations/Amb_chair_T_face_capt_reverse.nif", "Amb_chair_T_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/Amb_seated_T.nif", "Amb_seated_t")
	kAM.LoadAnimation ("data/animations/EB_hit_t.NIF", "Amb_hit_t")

	# Tactical Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/Amb_T_pushing_buttons_A.NIF", "EB_T_console_slide_A")
	kAM.LoadAnimation ("data/animations/Amb_T_pushing_buttons_A.NIF", "EB_T_console_slide_B")
	kAM.LoadAnimation ("data/animations/Amb_H_pushing_buttons_A.NIF", "EB_T_console_slide_C")
	kAM.LoadAnimation ("data/animations/Amb_H_pushing_buttons_A.NIF", "EB_T_console_slide_D")

	kAM.LoadAnimation ("data/animations/Amb_T_pushing_buttons_A.NIF", "EB_T_pushing_buttons_A")
	kAM.LoadAnimation ("data/animations/Amb_T_pushing_buttons_A.NIF", "EB_T_pushing_buttons_B")
	kAM.LoadAnimation ("data/animations/Amb_T_pushing_buttons_A.NIF", "EB_T_pushing_buttons_C")
	kAM.LoadAnimation ("data/animations/Amb_H_pushing_buttons_A.NIF", "EB_T_pushing_buttons_D")
	kAM.LoadAnimation ("data/animations/Amb_H_pushing_buttons_A.NIF", "EB_T_pushing_buttons_E")
	kAM.LoadAnimation ("data/animations/Amb_H_pushing_buttons_A.NIF", "EB_T_pushing_buttons_F")

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
#	Unload any Ambassador bridge specific animations that are common
#
#	Args:	none
#
#	Return:	none
###############################################################################
def UnloadAnimations ():
	kAM = App.g_kAnimationManager

	kAM.FreeAnimation("Amb_Door_L1")
	kAM.FreeAnimation("Amb_Door_L2")

	# Small animations
	# Science Movement
	kAM.FreeAnimation("Amb_stand_s_s")
	kAM.FreeAnimation("Amb_seated_s_s")
	kAM.FreeAnimation("Amb_face_capt_s")
	kAM.FreeAnimation("Amb_chair_s_face_capt")
	kAM.FreeAnimation("Amb_face_capt_s_reverse")
	kAM.FreeAnimation("Amb_chair_s_face_capt_reverse")
	kAM.FreeAnimation("EB_chair_S_in")

	# Science Console Slides and Button Pushes
	kAM.FreeAnimation("EB_S_pushing_buttons_seated_A")
	kAM.FreeAnimation("EB_S_pushing_buttons_seated_B")
	kAM.FreeAnimation("EB_S_pushing_buttons_seated_C")

	# Science Talking to other stations

	# Engineer Movement
	kAM.FreeAnimation("Amb_stand_e_s")
	kAM.FreeAnimation("Amb_seated_e_s")
	kAM.FreeAnimation("Amb_face_capt_e")
	kAM.FreeAnimation("Amb_chair_e_face_capt")
	kAM.FreeAnimation("Amb_face_capt_e_reverse")
	kAM.FreeAnimation("Amb_chair_e_face_capt_reverse")
	kAM.FreeAnimation("EB_chair_E_in")

	# Engineer Console Slides and Button Pushes
	kAM.FreeAnimation("EB_E_pushing_buttons_seated_A")
	kAM.FreeAnimation("EB_E_pushing_buttons_seated_B")
	kAM.FreeAnimation("EB_E_pushing_buttons_seated_C")

	# Engineer Talking to other stations

	# medium animations
	# Helm Movement
	kAM.FreeAnimation("Amb_stand_h_m")
	kAM.FreeAnimation("Amb_seated_h_m")
	kAM.FreeAnimation("Amb_face_capt_h")
	kAM.FreeAnimation("Amb_chair_h_face_capt")
	kAM.FreeAnimation("Amb_face_capt_h_reverse")
	kAM.FreeAnimation("Amb_chair_h_face_capt_reverse")
	kAM.FreeAnimation("Amb_seated_h")
	#kAM.FreeAnimation("Amb_interaction_h")
	kAM.FreeAnimation("Amb_hit_h")


	# Helm Console Slides and Button Pushes
	kAM.FreeAnimation("EB_H_console_slide_A")
	kAM.FreeAnimation("EB_H_console_slide_B")
	kAM.FreeAnimation("EB_H_console_slide_C")
	kAM.FreeAnimation("EB_H_console_slide_D")

	kAM.FreeAnimation("EB_H_pushing_buttons_A")
	kAM.FreeAnimation("EB_H_pushing_buttons_B")
	kAM.FreeAnimation("EB_H_pushing_buttons_C")
	kAM.FreeAnimation("EB_H_pushing_buttons_D")
	kAM.FreeAnimation("EB_H_pushing_buttons_E")
	kAM.FreeAnimation("EB_H_pushing_buttons_F")

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
	kAM.FreeAnimation("AmbTNG_seated_c_m")
	kAM.FreeAnimation("Amb_stand_c_m")
	kAM.FreeAnimation("AmbTNG_face_capt_c1")
	kAM.FreeAnimation("AmbTNG_face_capt_c")
	kAM.FreeAnimation("AmbTNG_face_capt_C_reverse")
	kAM.FreeAnimation("AmbTNG_face_capt_c1_reverse")
	kAM.FreeAnimation("Amb_hit_c")

	# XO Console Slides and Button Pushes
	kAM.FreeAnimation("EB_C_pushing_buttons_seated_A")
	kAM.FreeAnimation("EB_C_pushing_buttons_seated_B")
	kAM.FreeAnimation("EB_C_pushing_buttons_seated_C")
	kAM.FreeAnimation("EB_C_pushing_buttons_seated_D")
	kAM.FreeAnimation("EB_C_pushing_buttons_seated_E")
	kAM.FreeAnimation("EB_C_pushing_buttons_seated_F")
	kAM.FreeAnimation("EB_C_pushing_buttons_seated_G")

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
	kAM.FreeAnimation("Amb_hit_x")

	kAM.FreeAnimation("EB_X_pushing_buttons_A")
	kAM.FreeAnimation("EB_X_pushing_buttons_B")
	kAM.FreeAnimation("EB_X_pushing_buttons_C")
	kAM.FreeAnimation("EB_X_pushing_buttons_D")
	kAM.FreeAnimation("EB_X_pushing_buttons_E")
	kAM.FreeAnimation("EB_X_pushing_buttons_F")
	kAM.FreeAnimation("EB_X_pushing_buttons_G")

	#Extra
	kAM.FreeAnimation("Amb_L1toG3_S")
	kAM.FreeAnimation("Amb_L1toG3_M")
	kAM.FreeAnimation("Amb_L1toG3_L")

	# kAM.FreeAnimation("Amb_L2toG1_S")
	# kAM.FreeAnimation("Amb_L2toG1_M")
	# kAM.FreeAnimation("Amb_L2toG1_L")

	kAM.FreeAnimation("Amb_L2toG2_S")
	kAM.FreeAnimation("Amb_L2toG2_M")
	kAM.FreeAnimation("Amb_L2toG2_L")

	# kAM.FreeAnimation("Amb_G1toL2_S")
	# kAM.FreeAnimation("Amb_G1toL2_M")
	# kAM.FreeAnimation("Amb_G1toL2_L")
	
	kAM.FreeAnimation("Amb_G2toL2_S")
	kAM.FreeAnimation("Amb_G2toL2_M")
	kAM.FreeAnimation("Amb_G2toL2_L")
	
	kAM.FreeAnimation("Amb_G3toL1_S")
	kAM.FreeAnimation("Amb_G3toL1_M")
	kAM.FreeAnimation("Amb_G3toL1_L")
	
	# Large animations
	# Tactical Movement
	kAM.FreeAnimation("Amb_stand_t_l")
	kAM.FreeAnimation("Amb_seated_t_l")
	kAM.FreeAnimation("Amb_face_capt_t")
	kAM.FreeAnimation("Amb_chair_T_face_capt")
	kAM.FreeAnimation("Amb_face_capt_t_reverse")
	kAM.FreeAnimation("Amb_chair_T_face_capt_reverse")
	kAM.FreeAnimation("Amb_seated_t")
	kAM.FreeAnimation("Amb_hit_t")

	# Tactical Console Slides and Button Pushes
	kAM.FreeAnimation("EB_T_console_slide_A")
	kAM.FreeAnimation("EB_T_console_slide_B")
	kAM.FreeAnimation("EB_T_console_slide_C")
	kAM.FreeAnimation("EB_T_console_slide_D")

	kAM.FreeAnimation("EB_T_pushing_buttons_A")
	kAM.FreeAnimation("EB_T_pushing_buttons_B")
	kAM.FreeAnimation("EB_T_pushing_buttons_C")
	kAM.FreeAnimation("EB_T_pushing_buttons_D")
	kAM.FreeAnimation("EB_T_pushing_buttons_E")
	kAM.FreeAnimation("EB_T_pushing_buttons_F")

	# Tactical Talking to other stations
	kAM.FreeAnimation("EB_T_Talk_to_H_L")
	kAM.FreeAnimation("EB_T_Talk_to_G2_L")
	kAM.FreeAnimation("EB_T_Talk_to_G3_L")

	kAM.FreeAnimation("EB_T_Talk_fin_H_L")
	kAM.FreeAnimation("EB_T_Talk_fin_G2_L")
	kAM.FreeAnimation("EB_T_Talk_fin_G3_L")


	return

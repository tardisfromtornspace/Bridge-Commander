##############################################################################
#	Filename:	nebulaBridge.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	This contains the code to create and configure the nebula class bridge.
#	It is only called by LoadBridge.Initialize("nebulaBridge"), so don't
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
#	Create the nebula bridge model, viewscreen and main camera, attaching them
#	to the Set passed in.
#
#	Args:	pBridgeSet	- The Bridge set
#
#	Return:	none
###############################################################################
def CreateBridgeModel(pBridgeSet):
	iDetail = App.g_kImageManager.GetImageDetail()
	pcDetail = [ "High/", "High/", "High/" ]
	pcEnvPath = "data/Models/Sets/nebulabridgev3/" + pcDetail[iDetail]

	# Pre-load the Bridge model and viewscreen
	App.g_kModelManager.LoadModel("data/Models/Sets/nebulabridgev3/nebulabridge.nif", None, pcEnvPath)
	App.g_kModelManager.LoadModel("data/Models/Sets/nebulabridgev3/nebulaViewScreen.nif", None, pcEnvPath)

	# Load the viewscreen and set it up specially with SetViewScreen()
	pViewScreen = App.ViewScreenObject_Create("data/Models/Sets/nebulabridgev3/nebulaViewScreen.nif")
	pBridgeSet.SetViewScreen(pViewScreen, "viewscreen")

	# Setup bridge object
	pBridgeObject = App.BridgeObjectClass_Create("data/Models/Sets/nebulabridgev3/nebulabridge.nif")
	pBridgeSet.AddObjectToSet(pBridgeObject, "bridge")
	pBridgeObject.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	pBridgeObject.SetAngleAxisRotation(0.000000, 1.000000, 0.000000, 0.000000)

	# setup hardpoints for dbridge.
	pPropertySet = pBridgeObject.GetPropertySet()
	import Bridge.nebulabridgeProperties
	App.g_kModelPropertyManager.ClearLocalTemplates()
	reload(Bridge.nebulabridgeProperties)
	Bridge.nebulabridgeProperties.LoadPropertySet(pPropertySet)


	# Create camera
	lPos = GetBaseCameraPosition()
	pCamera = App.ZoomCameraObjectClass_Create(lPos[0], lPos[1], lPos[2], 1.570796, -0.000665, -0.087559, 0.996159, "maincamera")
	pCamera.SetMinZoom(0.66)
	pCamera.SetMaxZoom(1.2)
	pCamera.SetZoomTime(0.375)
	pBridgeSet.AddCameraToSet(pCamera, "maincamera")
	pCamera.Update( App.g_kUtopiaModule.GetGameTime() )
	App.g_kVarManager.SetFloatVariable("global", "fZoomTuneState", 0)

	# Load nebula bridge specific sounds
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
	return (0.683736, 20.585, 77.678)

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
	import Bridge.Characters.NebFelix
	import Bridge.Characters.NebKiska
	import Bridge.Characters.NebSaffi
	import Bridge.Characters.NebBrex
	import Bridge.Characters.NebMiguel

	import Bridge.Characters.NebFemaleExtra1
	import Bridge.Characters.NebFemaleExtra2
	import Bridge.Characters.NebFemaleExtra3
	import Bridge.Characters.NebMaleExtra1
	import Bridge.Characters.NebMaleExtra2
	import Bridge.Characters.NebMaleExtra3

	pNebFelix = App.CharacterClass_Cast(pBridgeSet.GetObject("Tactical"))
	pNebKiska = App.CharacterClass_Cast(pBridgeSet.GetObject("Helm"))
	pNebSaffi = App.CharacterClass_Cast(pBridgeSet.GetObject("XO"))
	pNebMiguel = App.CharacterClass_Cast(pBridgeSet.GetObject("Science"))
	pNebBrex = App.CharacterClass_Cast(pBridgeSet.GetObject("Engineer"))

	pNebFemaleExtra1 = App.CharacterClass_Cast(pBridgeSet.GetObject("FemaleExtra1"))
	pNebFemaleExtra2 = App.CharacterClass_Cast(pBridgeSet.GetObject("FemaleExtra2"))
	pNebFemaleExtra3 = App.CharacterClass_Cast(pBridgeSet.GetObject("FemaleExtra3"))

	pNebMaleExtra1 = App.CharacterClass_Cast(pBridgeSet.GetObject("MaleExtra1"))
	pNebMaleExtra2 = App.CharacterClass_Cast(pBridgeSet.GetObject("MaleExtra2"))
	pNebMaleExtra3 = App.CharacterClass_Cast(pBridgeSet.GetObject("MaleExtra3"))

	Bridge.Characters.NebFelix.ConfigureForNebula(pNebFelix)
	Bridge.Characters.NebKiska.ConfigureForNebula(pNebKiska)
	Bridge.Characters.NebSaffi.ConfigureForNebula(pNebSaffi)
	Bridge.Characters.NebMiguel.ConfigureForNebula(pNebMiguel)
	Bridge.Characters.NebBrex.ConfigureForNebula(pNebBrex)


	if (pNebFemaleExtra1):
		Bridge.Characters.NebFemaleExtra1.ConfigureForNebula(pNebFemaleExtra1)
	if (pNebFemaleExtra2):
		Bridge.Characters.NebFemaleExtra2.ConfigureForNebula(pNebFemaleExtra2)
	if (pNebFemaleExtra3):
		Bridge.Characters.NebFemaleExtra3.ConfigureForNebula(pNebFemaleExtra3)
	if (pNebMaleExtra1):
		Bridge.Characters.NebMaleExtra1.ConfigureForNebula(pNebMaleExtra1)
	if (pNebMaleExtra2):
		Bridge.Characters.NebMaleExtra2.ConfigureForNebula(pNebMaleExtra2)
	if (pNebMaleExtra3):
		Bridge.Characters.NebMaleExtra3.ConfigureForNebula(pNebMaleExtra3)

	pCamera = App.ZoomCameraObjectClass_GetObject(pBridgeSet, "maincamera")
	pCamera.SetTranslateXYZ(0.683736, 20.585, 77.678)


###############################################################################
#	LoadSounds()
#
#	Load any nebula bridge specific sounds
#
#	Args:	none
#
#	Return:	none
###############################################################################
def LoadSounds():

#	debug("Loading nebula door sound")

	pGame = App.Game_GetCurrentGame()
	pGame.LoadSoundInGroup("sfx/door.wav",  "LiftDoor", "BridgeGeneric")


###############################################################################
#	UnloadSounds()
#
#	Unload any nebula bridge specific sounds
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
#	Load any nebula bridge specific animations that are common
#
#	Args:	none
#
#	Return:	none
###############################################################################
def PreloadAnimations ():
	kAM = App.g_kAnimationManager

	kAM.LoadAnimation ("data/animations/Neb_door_L1.nif", "Neb_Door_L1")
	kAM.LoadAnimation ("data/animations/Neb_door_L2.nif", "Neb_Door_L2")

	# Small animations
	# Science Movement
	kAM.LoadAnimation ("data/animations/Neb_stand_s_s.nif", "Neb_stand_s_s")
	kAM.LoadAnimation ("data/animations/Neb_seated_s_s.nif", "Neb_seated_s_s")
	kAM.LoadAnimation ("data/animations/Neb_face_capt_s.nif", "Neb_face_capt_s")
	kAM.LoadAnimation ("data/animations/Neb_chair_s_face_capt.nif", "Neb_chair_s_face_capt")
	kAM.LoadAnimation ("data/animations/Neb_face_capt_s_reverse.nif", "Neb_face_capt_s_reverse")
	kAM.LoadAnimation ("data/animations/Neb_chair_s_face_capt_reverse.nif", "Neb_chair_s_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/EB_chair_S_in.nif", "EB_chair_S_in")

	# Science Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/EB_S_pushing_buttons_seated_A.NIF", "EB_S_pushing_buttons_seated_A")
	kAM.LoadAnimation ("data/animations/EB_S_pushing_buttons_seated_B.NIF", "EB_S_pushing_buttons_seated_B")
	kAM.LoadAnimation ("data/animations/EB_S_pushing_buttons_seated_C.NIF", "EB_S_pushing_buttons_seated_C")

	# Science Talking to other stations

	# Engineer Movement
	kAM.LoadAnimation ("data/animations/Neb_stand_e_s.nif", "Neb_stand_e_s")
	kAM.LoadAnimation ("data/animations/Neb_seated_e_s.nif", "Neb_seated_e_s")
	kAM.LoadAnimation ("data/animations/Neb_face_capt_e.nif", "Neb_face_capt_e")
	kAM.LoadAnimation ("data/animations/Neb_chair_e_face_capt.nif", "Neb_chair_e_face_capt")
	kAM.LoadAnimation ("data/animations/Neb_face_capt_e_reverse.nif", "Neb_face_capt_e_reverse")
	kAM.LoadAnimation ("data/animations/Neb_chair_e_face_capt_reverse.nif", "Neb_chair_e_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/EB_chair_E_in.nif", "EB_chair_E_in")

	# Engineer Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/EB_E_pushing_buttons_seated_A.NIF", "EB_E_pushing_buttons_seated_A")
	kAM.LoadAnimation ("data/animations/EB_E_pushing_buttons_seated_B.NIF", "EB_E_pushing_buttons_seated_B")
	kAM.LoadAnimation ("data/animations/EB_E_pushing_buttons_seated_C.NIF", "EB_E_pushing_buttons_seated_C")

	# Engineer Talking to other stations

	# 
	# medium animations
	# Helm Movement
	kAM.LoadAnimation ("data/animations/Neb_stand_h_m.nif", "Neb_stand_h_m")
	kAM.LoadAnimation ("data/animations/Neb_seated_h_m.nif", "Neb_seated_h_m")
	kAM.LoadAnimation ("data/animations/Neb_chair_H_face_capt.nif", "Neb_chair_H_face_capt")
	kAM.LoadAnimation ("data/animations/Neb_face_capt_h_reverse.nif", "Neb_face_capt_h_reverse")
	kAM.LoadAnimation ("data/animations/Neb_face_capt_h.nif", "Neb_face_capt_h")
	kAM.LoadAnimation ("data/animations/Neb_face_capt_h_reverse.nif", "Neb_face_capt_h_reverse")
	kAM.LoadAnimation ("data/animations/EB_hit_h.NIF", "Neb_hit_h")

	# Helm Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/EB_H_Console_Slide_A.NIF", "EB_H_console_slide_A")
	kAM.LoadAnimation ("data/animations/EB_H_Console_Slide_B.NIF", "EB_H_console_slide_B")
	kAM.LoadAnimation ("data/animations/EB_H_Console_Slide_C.NIF", "EB_H_console_slide_C")
	kAM.LoadAnimation ("data/animations/EB_H_Console_Slide_D.NIF", "EB_H_console_slide_D")

	kAM.LoadAnimation ("data/animations/EB_H_pushing_buttons_A.NIF", "EB_H_pushing_buttons_A")
	kAM.LoadAnimation ("data/animations/EB_H_pushing_buttons_B.NIF", "EB_H_pushing_buttons_B")
	kAM.LoadAnimation ("data/animations/EB_H_pushing_buttons_C.NIF", "EB_H_pushing_buttons_C")
	kAM.LoadAnimation ("data/animations/EB_H_pushing_buttons_D.NIF", "EB_H_pushing_buttons_D")
	kAM.LoadAnimation ("data/animations/EB_H_pushing_buttons_E.NIF", "EB_H_pushing_buttons_E")
	kAM.LoadAnimation ("data/animations/EB_H_pushing_buttons_F.NIF", "EB_H_pushing_buttons_F")

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
	kAM.LoadAnimation ("data/animations/Neb_seated_C_M.nif", "Neb_seated_c_m")
	kAM.LoadAnimation ("data/animations/Neb_stand_V_M.nif", "Neb_stand_c_m")
	kAM.LoadAnimation ("data/animations/Neb_face_capt_c1.nif", "Neb_face_capt_c1")
	kAM.LoadAnimation ("data/animations/Neb_face_capt_c.nif", "Neb_face_capt_c")
	kAM.LoadAnimation ("data/animations/Neb_face_capt_C_reverse.NIF", "Neb_face_capt_C_reverse")
	kAM.LoadAnimation ("data/animations/Neb_face_capt_c1_reverse.NIF", "Neb_face_capt_c1_reverse")
	kAM.LoadAnimation ("data/animations/EB_hit_c.NIF", "Neb_hit_c")
	kAM.LoadAnimation ("data/animations/Neb_stand_C_M.NIF", "NebStanding")


	# XO Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/EB_C_pushing_buttons_A.NIF", "EB_C_pushing_buttons_A")
	kAM.LoadAnimation ("data/animations/EB_C_pushing_buttons_B.NIF", "EB_C_pushing_buttons_B")
	kAM.LoadAnimation ("data/animations/EB_C_pushing_buttons_C.NIF", "EB_C_pushing_buttons_C")
	kAM.LoadAnimation ("data/animations/EB_C_pushing_buttons_D.NIF", "EB_C_pushing_buttons_D")
	kAM.LoadAnimation ("data/animations/EB_C_pushing_buttons_E.NIF", "EB_C_pushing_buttons_E")
	kAM.LoadAnimation ("data/animations/EB_C_pushing_buttons_F.NIF", "EB_C_pushing_buttons_F")
	kAM.LoadAnimation ("data/animations/EB_C_pushing_buttons_G.NIF", "EB_C_pushing_buttons_G")

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
	kAM.LoadAnimation ("data/animations/EB_hit_x.NIF", "Neb_hit_x")

	# Extras
	kAM.LoadAnimation ("data/animations/Neb_L1toG3_S.nif", "Neb_L1toG3_S")
	kAM.LoadAnimation ("data/animations/Neb_L1toG3_M.nif", "Neb_L1toG3_M")
	kAM.LoadAnimation ("data/animations/Neb_L1toG3_L.nif", "Neb_L1toG3_L")

	kAM.LoadAnimation ("data/animations/Neb_L2toG1_S.nif", "Neb_L2toG1_S")
	kAM.LoadAnimation ("data/animations/Neb_L2toG1_M.nif", "Neb_L2toG1_M")
	kAM.LoadAnimation ("data/animations/Neb_L2toG1_L.nif", "Neb_L2toG1_L")

	kAM.LoadAnimation ("data/animations/Neb_L2toG2_S.nif", "Neb_L2toG2_S")
	kAM.LoadAnimation ("data/animations/Neb_L2toG2_M.nif", "Neb_L2toG2_M")
	kAM.LoadAnimation ("data/animations/Neb_L2toG2_L.nif", "Neb_L2toG2_L")

	kAM.LoadAnimation ("data/animations/Neb_G1toL2_S.nif", "Neb_G1toL2_S")
	kAM.LoadAnimation ("data/animations/Neb_G1toL2_M.nif", "Neb_G1toL2_M")
	kAM.LoadAnimation ("data/animations/Neb_G1toL2_L.nif", "Neb_G1toL2_L")
	
	kAM.LoadAnimation ("data/animations/Neb_G2toL2_S.nif", "Neb_G2toL2_S")
	kAM.LoadAnimation ("data/animations/Neb_G2toL2_M.nif", "Neb_G2toL2_M")
	kAM.LoadAnimation ("data/animations/Neb_G2toL2_L.nif", "Neb_G2toL2_L")
	
	kAM.LoadAnimation ("data/animations/Neb_G3toL1_S.nif", "Neb_G3toL1_S")
	kAM.LoadAnimation ("data/animations/Neb_G3toL1_M.nif", "Neb_G3toL1_M")
	kAM.LoadAnimation ("data/animations/Neb_G3toL1_L.nif", "Neb_G3toL1_L")

	# Large animations
	# Tactical Movement
	kAM.LoadAnimation ("data/animations/Neb_stand_t_l.nif", "Neb_stand_t_l")
	kAM.LoadAnimation ("data/animations/Neb_seated_t_l.nif", "Neb_seated_t_l")
	kAM.LoadAnimation ("data/animations/Neb_face_capt_t.nif", "Neb_face_capt_t")
	kAM.LoadAnimation ("data/animations/Neb_chair_T_face_capt.nif", "Neb_chair_T_face_capt")
	kAM.LoadAnimation ("data/animations/Neb_face_capt_t_reverse.nif", "Neb_face_capt_t_reverse")
	kAM.LoadAnimation ("data/animations/Neb_chair_T_face_capt_reverse.nif", "Neb_chair_T_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/EB_hit_t.NIF", "Neb_hit_t")

	# Tactical Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/EB_T_Console_Slide_A.NIF", "EB_T_console_slide_A")
	kAM.LoadAnimation ("data/animations/EB_T_Console_Slide_B.NIF", "EB_T_console_slide_B")
	kAM.LoadAnimation ("data/animations/EB_T_Console_Slide_C.NIF", "EB_T_console_slide_C")
	kAM.LoadAnimation ("data/animations/EB_T_Console_Slide_D.NIF", "EB_T_console_slide_D")

	kAM.LoadAnimation ("data/animations/EB_T_pushing_buttons_A.NIF", "EB_T_pushing_buttons_A")
	kAM.LoadAnimation ("data/animations/EB_T_pushing_buttons_B.NIF", "EB_T_pushing_buttons_B")
	kAM.LoadAnimation ("data/animations/EB_T_pushing_buttons_C.NIF", "EB_T_pushing_buttons_C")
	kAM.LoadAnimation ("data/animations/EB_T_pushing_buttons_D.NIF", "EB_T_pushing_buttons_D")
	kAM.LoadAnimation ("data/animations/EB_T_pushing_buttons_E.NIF", "EB_T_pushing_buttons_E")
	kAM.LoadAnimation ("data/animations/EB_T_pushing_buttons_F.NIF", "EB_T_pushing_buttons_F")

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
#	Unload any nebula bridge specific animations that are common
#
#	Args:	none
#
#	Return:	none
###############################################################################
def UnloadAnimations ():
	kAM = App.g_kAnimationManager

	kAM.FreeAnimation("Neb_Door_L1")
	kAM.FreeAnimation("Neb_Door_L2")

	# Small animations
	# Science Movement
	kAM.FreeAnimation("Neb_stand_s_s")
	kAM.FreeAnimation("Neb_seated_s_s")
	kAM.FreeAnimation("Neb_face_capt_s")
	kAM.FreeAnimation("Neb_chair_s_face_capt")
	kAM.FreeAnimation("Neb_face_capt_s_reverse")
	kAM.FreeAnimation("Neb_chair_s_face_capt_reverse")
	kAM.FreeAnimation("EB_chair_S_in")

	# Science Console Slides and Button Pushes
	kAM.FreeAnimation("EB_S_pushing_buttons_seated_A")
	kAM.FreeAnimation("EB_S_pushing_buttons_seated_B")
	kAM.FreeAnimation("EB_S_pushing_buttons_seated_C")

	# Science Talking to other stations

	# Engineer Movement
	kAM.FreeAnimation("Neb_stand_e_s")
	kAM.FreeAnimation("Neb_seated_e_s")
	kAM.FreeAnimation("Neb_face_capt_e")
	kAM.FreeAnimation("Neb_chair_e_face_capt")
	kAM.FreeAnimation("Neb_face_capt_e_reverse")
	kAM.FreeAnimation("Neb_chair_e_face_capt_reverse")
	kAM.FreeAnimation("EB_chair_E_in")

	# Engineer Console Slides and Button Pushes
	kAM.FreeAnimation("EB_E_pushing_buttons_seated_A")
	kAM.FreeAnimation("EB_E_pushing_buttons_seated_B")
	kAM.FreeAnimation("EB_E_pushing_buttons_seated_C")

	# Engineer Talking to other stations

	# medium animations
	# Helm Movement
	kAM.FreeAnimation("Neb_stand_h_m")
	kAM.FreeAnimation("Neb_seated_h_m")
	kAM.FreeAnimation("Exc_chair_H_face_capt")
	kAM.FreeAnimation("Exc_face_capt_h_reverse")
	kAM.FreeAnimation("Neb_face_capt_h")
	kAM.FreeAnimation("Neb_face_capt_h_reverse")
	kAM.FreeAnimation("Neb_hit_h")


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
	kAM.FreeAnimation("Neb_seated_c_m")
	kAM.FreeAnimation("Neb_stand_c_m")
	kAM.FreeAnimation("Neb_face_capt_c1")
	kAM.FreeAnimation("Neb_face_capt_c")
	kAM.FreeAnimation("Neb_face_capt_C_reverse")
	kAM.FreeAnimation("Neb_face_capt_c1_reverse")
	kAM.FreeAnimation("Neb_hit_c")
	kAM.FreeAnimation("NebStanding")

	# XO Console Slides and Button Pushes
	kAM.FreeAnimation("EB_C_pushing_buttons_A")
	kAM.FreeAnimation("EB_C_pushing_buttons_B")
	kAM.FreeAnimation("EB_C_pushing_buttons_C")
	kAM.FreeAnimation("EB_C_pushing_buttons_D")
	kAM.FreeAnimation("EB_C_pushing_buttons_E")
	kAM.FreeAnimation("EB_C_pushing_buttons_F")
	kAM.FreeAnimation("EB_C_pushing_buttons_G")

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
	kAM.FreeAnimation("Neb_hit_x")

	kAM.FreeAnimation("EB_X_pushing_buttons_A")
	kAM.FreeAnimation("EB_X_pushing_buttons_B")
	kAM.FreeAnimation("EB_X_pushing_buttons_C")
	kAM.FreeAnimation("EB_X_pushing_buttons_D")
	kAM.FreeAnimation("EB_X_pushing_buttons_E")
	kAM.FreeAnimation("EB_X_pushing_buttons_F")
	kAM.FreeAnimation("EB_X_pushing_buttons_G")

	#Extra
	kAM.FreeAnimation("Neb_L1toG3_S")
	kAM.FreeAnimation("Neb_L1toG3_M")
	kAM.FreeAnimation("Neb_L1toG3_L")

	kAM.FreeAnimation("Neb_L2toG1_S")
	kAM.FreeAnimation("Neb_L2toG1_M")
	kAM.FreeAnimation("Neb_L2toG1_L")

	kAM.FreeAnimation("Neb_L2toG2_S")
	kAM.FreeAnimation("Neb_L2toG2_M")
	kAM.FreeAnimation("Neb_L2toG2_L")

	kAM.FreeAnimation("Neb_G1toL2_S")
	kAM.FreeAnimation("Neb_G1toL2_M")
	kAM.FreeAnimation("Neb_G1toL2_L")
	
	kAM.FreeAnimation("Neb_G2toL2_S")
	kAM.FreeAnimation("Neb_G2toL2_M")
	kAM.FreeAnimation("Neb_G2toL2_L")
	
	kAM.FreeAnimation("Neb_G3toL1_S")
	kAM.FreeAnimation("Neb_G3toL1_M")
	kAM.FreeAnimation("Neb_G3toL1_L")
	
	# Large animations
	# Tactical Movement
	kAM.FreeAnimation("Neb_stand_t_l")
	kAM.FreeAnimation("Neb_seated_t_l")
	kAM.FreeAnimation("Neb_face_capt_t")
	kAM.FreeAnimation("Neb_chair_T_face_capt")
	kAM.FreeAnimation("Neb_face_capt_t_reverse")
	kAM.FreeAnimation("Neb_chair_T_face_capt_reverse")
	kAM.FreeAnimation("Neb_hit_t")

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

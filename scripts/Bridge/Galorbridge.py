##############################################################################
#	Filename:	Galorbridge.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	This contains the code to create and configure the Galor class bridge.
#	It is only called by LoadBridge.Initialize("Galorbridge"), so don't
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
#	Create the Galor bridge model, viewscreen and main camera, attaching them
#	to the Set passed in.
#
#	Args:	pBridgeSet	- The Bridge set
#
#	Return:	none
###############################################################################
def CreateBridgeModel(pBridgeSet):
	iDetail = App.g_kImageManager.GetImageDetail()
	pcDetail = [ "High/", "High/", "High/" ]
	pcEnvPath = "data/Models/Sets/Galorbridge/" + pcDetail[iDetail]

	# Pre-load the Bridge model and viewscreen
	App.g_kModelManager.LoadModel("data/Models/Sets/Galorbridge/Galorbridge.nif", None, pcEnvPath)
	App.g_kModelManager.LoadModel("data/Models/Sets/Galorbridge/GalorViewScreen.NIF", None, pcEnvPath)

	# Load the viewscreen and set it up specially with SetViewScreen()
	pViewScreen = App.ViewScreenObject_Create("data/Models/Sets/Galorbridge/GalorViewScreen.NIF")
	pBridgeSet.SetViewScreen(pViewScreen, "viewscreen")

	# Setup bridge object
	pBridgeObject = App.BridgeObjectClass_Create("data/Models/Sets/Galorbridge/Galorbridge.nif")
	pBridgeSet.AddObjectToSet(pBridgeObject, "bridge")
	pBridgeObject.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	pBridgeObject.SetAngleAxisRotation(0.000000, 1.000000, 0.000000, 0.000000)

	# setup hardpoints for dbridge.
	pPropertySet = pBridgeObject.GetPropertySet()
	import Bridge.GalorbridgeProperties
	App.g_kModelPropertyManager.ClearLocalTemplates()
	reload(Bridge.GalorbridgeProperties)
	Bridge.GalorbridgeProperties.LoadPropertySet(pPropertySet)


	# Create camera
	lPos = GetBaseCameraPosition()
	pCamera = App.ZoomCameraObjectClass_Create(lPos[0], lPos[1], lPos[2], 1.570796, -0.000665, -0.087559, 0.996159, "maincamera")
	pCamera.SetMinZoom(0.8)
	pCamera.SetMaxZoom(1.0)
	pCamera.SetZoomTime(0.375)
	pBridgeSet.AddCameraToSet(pCamera, "maincamera")
	pCamera.Update( App.g_kUtopiaModule.GetGameTime() )
	App.g_kVarManager.SetFloatVariable("global", "fZoomTuneState", 0)

	# Load Galor bridge specific sounds
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
	import Bridge.Characters.SCPFelix
	import Bridge.Characters.SCPKiska
	import Bridge.Characters.SCPSaffi
	import Bridge.Characters.SCPBrex
	import Bridge.Characters.SCPMiguel

	import Bridge.Characters.SCPFemaleExtra1
	import Bridge.Characters.SCPFemaleExtra2
	import Bridge.Characters.SCPFemaleExtra3
	import Bridge.Characters.SCPMaleExtra1
	import Bridge.Characters.SCPMaleExtra2
	import Bridge.Characters.SCPMaleExtra3

	pSCPFelix = App.CharacterClass_Cast(pBridgeSet.GetObject("Tactical"))
	pSCPKiska = App.CharacterClass_Cast(pBridgeSet.GetObject("Helm"))
	pSCPSaffi = App.CharacterClass_Cast(pBridgeSet.GetObject("XO"))
	pSCPMiguel = App.CharacterClass_Cast(pBridgeSet.GetObject("Science"))
	pSCPBrex = App.CharacterClass_Cast(pBridgeSet.GetObject("Engineer"))

	pSCPFemaleExtra1 = App.CharacterClass_Cast(pBridgeSet.GetObject("FemaleExtra1"))
	pSCPFemaleExtra2 = App.CharacterClass_Cast(pBridgeSet.GetObject("FemaleExtra2"))
	pSCPFemaleExtra3 = App.CharacterClass_Cast(pBridgeSet.GetObject("FemaleExtra3"))

	pSCPMaleExtra1 = App.CharacterClass_Cast(pBridgeSet.GetObject("MaleExtra1"))
	pSCPMaleExtra2 = App.CharacterClass_Cast(pBridgeSet.GetObject("MaleExtra2"))
	pSCPMaleExtra3 = App.CharacterClass_Cast(pBridgeSet.GetObject("MaleExtra3"))

	Bridge.Characters.SCPFelix.ConfigureForGalor(pSCPFelix)
	Bridge.Characters.SCPKiska.ConfigureForGalor(pSCPKiska)
	Bridge.Characters.SCPSaffi.ConfigureForGalor(pSCPSaffi)
	Bridge.Characters.SCPMiguel.ConfigureForGalor(pSCPMiguel)
	Bridge.Characters.SCPBrex.ConfigureForGalor(pSCPBrex)

	if (pSCPFemaleExtra1):
		Bridge.Characters.SCPFemaleExtra1.ConfigureForGalor(pSCPFemaleExtra1)
	if (pSCPFemaleExtra2):
		Bridge.Characters.SCPFemaleExtra2.ConfigureForGalor(pSCPFemaleExtra2)
	if (pSCPFemaleExtra3):
		Bridge.Characters.SCPFemaleExtra3.ConfigureForGalor(pSCPFemaleExtra3)
	if (pSCPMaleExtra1):
		Bridge.Characters.SCPMaleExtra1.ConfigureForGalor(pSCPMaleExtra1)
	if (pSCPMaleExtra2):
		Bridge.Characters.SCPMaleExtra2.ConfigureForGalor(pSCPMaleExtra2)
	if (pSCPMaleExtra3):
		Bridge.Characters.SCPMaleExtra3.ConfigureForGalor(pSCPMaleExtra3)

	pCamera = App.ZoomCameraObjectClass_GetObject(pBridgeSet, "maincamera")
	pCamera.SetTranslateXYZ(5, 90, 70)


###############################################################################
#	LoadSounds()
#
#	Load any Galor bridge specific sounds
#
#	Args:	none
#
#	Return:	none
###############################################################################
def LoadSounds():

#	debug("Loading Galor door sound")

	pGame = App.Game_GetCurrentGame()
	pGame.LoadSoundInGroup("sfx/door.wav",  "LiftDoor", "BridgeGeneric")


###############################################################################
#	UnloadSounds()
#
#	Unload any Galor bridge specific sounds
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
#	Load any Galor bridge specific animations that are common
#
#	Args:	none
#
#	Return:	none
###############################################################################
def PreloadAnimations ():
	kAM = App.g_kAnimationManager

	kAM.LoadAnimation ("data/animations/SCP_door_L1.nif", "SCP_Door_L1")
	kAM.LoadAnimation ("data/animations/SCP_door_L1b.nif", "SCP_Door_L1B")
	kAM.LoadAnimation ("data/animations/SCP_door_L1c.nif", "SCP_Door_L1c")
	kAM.LoadAnimation ("data/animations/SCP_door_L2.nif", "SCP_Door_L2")
	kAM.LoadAnimation ("data/animations/SCP_door_L2b.nif", "SCP_Door_L2B")

	# Small animations
	# Science Movement
	kAM.LoadAnimation ("data/animations/SCP_stand_s_s.nif", "SCP_stand_s_s")
	kAM.LoadAnimation ("data/animations/SCP_seated_s_s.nif", "SCP_seated_s_s")
	kAM.LoadAnimation ("data/animations/SCP_face_capt_s.nif", "SCP_face_capt_s")
	kAM.LoadAnimation ("data/animations/SCP_chair_s_face_capt.nif", "SCP_chair_s_face_capt")
	kAM.LoadAnimation ("data/animations/SCP_face_capt_s_reverse.nif", "SCP_face_capt_s_reverse")
	kAM.LoadAnimation ("data/animations/SCP_chair_s_face_capt_reverse.nif", "SCP_chair_s_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/EB_chair_S_in.nif", "EB_chair_S_in")

	# Science Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/SCP_s_pushing_buttons_A.NIF", "EB_S_pushing_buttons_seated_A")
	kAM.LoadAnimation ("data/animations/SCP_s_pushing_buttons_A.NIF", "EB_S_pushing_buttons_seated_B")
	kAM.LoadAnimation ("data/animations/SCP_s_pushing_buttons_A.NIF", "EB_S_pushing_buttons_seated_C")

	# Science Talking to other stations

	# Engineer Movement
	kAM.LoadAnimation ("data/animations/SCP_stand_e_s.nif", "SCP_stand_e_s")
	kAM.LoadAnimation ("data/animations/SCP_seated_e_s.nif", "SCP_seated_e_s")
	kAM.LoadAnimation ("data/animations/SCP_face_capt_e.nif", "SCP_face_capt_e")
	kAM.LoadAnimation ("data/animations/SCP_chair_e_face_capt.nif", "SCP_chair_e_face_capt")
	kAM.LoadAnimation ("data/animations/SCP_face_capt_e_reverse.nif", "SCP_face_capt_e_reverse")
	kAM.LoadAnimation ("data/animations/SCP_chair_e_face_capt_reverse.nif", "SCP_chair_e_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/EB_chair_E_in.nif", "EB_chair_E_in")

	# Engineer Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/SCP_e_pushing_buttons_A.NIF", "EB_E_pushing_buttons_seated_A")
	kAM.LoadAnimation ("data/animations/SCP_e_pushing_buttons_A.NIF", "EB_E_pushing_buttons_seated_B")
	kAM.LoadAnimation ("data/animations/SCP_e_pushing_buttons_A.NIF", "EB_E_pushing_buttons_seated_C")

	# Engineer Talking to other stations


	kAM.LoadAnimation ("data/animations/_hit_hard_A.NIF", "SCP_hit_s")
	kAM.LoadAnimation ("data/animations/_hit_hard_A.NIF", "SCP_hit_e")

	# 
	# medium animations
	# Helm Movement
	kAM.LoadAnimation ("data/animations/SCP_stand_h_m.nif", "SCP_stand_h_m")
	kAM.LoadAnimation ("data/animations/SCP_seated_h_m.nif", "SCP_seated_h_m")
	kAM.LoadAnimation ("data/animations/SCP_face_capt_h.nif", "SCP_face_capt_h")
	kAM.LoadAnimation ("data/animations/SCP_chair_H_face_capt.nif", "SCP_chair_H_face_capt")
	kAM.LoadAnimation ("data/animations/SCP_face_capt_h_reverse.nif", "SCP_face_capt_h_reverse")
	kAM.LoadAnimation ("data/animations/SCP_chair_H_face_capt_reverse.nif", "SCP_chair_H_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/EB_glance_h_m.nif", "SCP_glance_h_m")
	kAM.LoadAnimation ("data/animations/EB_glance_h_m_reverse.nif", "SCP_glance_h_m_reverse")

	kAM.LoadAnimation ("data/animations/DB_hit_h.NIF", "SCP_hit_h")


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
	kAM.LoadAnimation ("data/animations/SCP_seated_C_M.nif", "SCP_seated_c_m")
	kAM.LoadAnimation ("data/animations/SCP_seatedm_C_M.nif", "SCP_seatedm_c_m")
	kAM.LoadAnimation ("data/animations/SCP_stand_V_M.nif", "SCP_stand_c_m")
	kAM.LoadAnimation ("data/animations/SCP_face_capt_c1.nif", "SCP_face_capt_c1")
	kAM.LoadAnimation ("data/animations/SCP_face_capt_c.nif", "SCP_face_capt_c")
	kAM.LoadAnimation ("data/animations/SCP_face_capt_C_reverse.NIF", "SCP_face_capt_C_reverse")
	kAM.LoadAnimation ("data/animations/SCP_face_capt_c1_reverse.NIF", "SCP_face_capt_c1_reverse")
	kAM.LoadAnimation ("data/animations/DB_hit_c.NIF", "SCP_hit_c")

	#Commander interaction
	kAM.LoadAnimation ("data/animations/EB_C_pushing_buttons_A.NIF", "EB_C_pushing_buttons_seated_A")
	kAM.LoadAnimation ("data/animations/EB_C_pushing_buttons_B.NIF", "EB_C_pushing_buttons_seated_B")
	kAM.LoadAnimation ("data/animations/EB_C_pushing_buttons_C.NIF", "EB_C_pushing_buttons_seated_C")
	kAM.LoadAnimation ("data/animations/EB_C_pushing_buttons_D.NIF", "EB_C_pushing_buttons_seated_D")
	kAM.LoadAnimation ("data/animations/EB_C_pushing_buttons_E.NIF", "EB_C_pushing_buttons_seated_E")
	kAM.LoadAnimation ("data/animations/EB_C_pushing_buttons_F.NIF", "EB_C_pushing_buttons_seated_F")
	kAM.LoadAnimation ("data/animations/EB_C_pushing_buttons_G.NIF", "EB_C_pushing_buttons_seated_G")

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
	kAM.LoadAnimation ("data/animations/EB_hit_x.NIF", "SCP_hit_x")

	# Extras
	kAM.LoadAnimation ("data/animations/SCP_L1toG3_S.nif", "SCP_L1toG3_S")
	kAM.LoadAnimation ("data/animations/SCP_L1toG3_M.nif", "SCP_L1toG3_M")
	kAM.LoadAnimation ("data/animations/SCP_L1toG3_L.nif", "SCP_L1toG3_L")

	kAM.LoadAnimation ("data/animations/SCP_L2toG1_S.nif", "SCP_L2toG1_S")
	kAM.LoadAnimation ("data/animations/SCP_L2toG1_M.nif", "SCP_L2toG1_M")
	kAM.LoadAnimation ("data/animations/SCP_L2toG1_L.nif", "SCP_L2toG1_L")

	kAM.LoadAnimation ("data/animations/SCP_L2toG2_S.nif", "SCP_L2toG2_S")
	kAM.LoadAnimation ("data/animations/SCP_L2toG2_M.nif", "SCP_L2toG2_M")
	kAM.LoadAnimation ("data/animations/SCP_L2toG2_L.nif", "SCP_L2toG2_L")
	kAM.LoadAnimation ("data/animations/SCP_chair_e1.nif", "SCP_chair_e1")

	kAM.LoadAnimation ("data/animations/SCP_G1toL2_S.nif", "SCP_G1toL2_S")
	kAM.LoadAnimation ("data/animations/SCP_G1toL2_M.nif", "SCP_G1toL2_M")
	kAM.LoadAnimation ("data/animations/SCP_G1toL2_L.nif", "SCP_G1toL2_L")
	
	kAM.LoadAnimation ("data/animations/SCP_G2toL2_S.nif", "SCP_G2toL2_S")
	kAM.LoadAnimation ("data/animations/SCP_G2toL2_M.nif", "SCP_G2toL2_M")
	kAM.LoadAnimation ("data/animations/SCP_G2toL2_L.nif", "SCP_G2toL2_L")
	
	kAM.LoadAnimation ("data/animations/SCP_G3toL1_S.nif", "SCP_G3toL1_S")
	kAM.LoadAnimation ("data/animations/SCP_G3toL1_M.nif", "SCP_G3toL1_M")
	kAM.LoadAnimation ("data/animations/SCP_G3toL1_L.nif", "SCP_G3toL1_L")

	kAM.LoadAnimation ("data/animations/SCP_extra3_M_interaction.nif", "SCP_extra3_M_interaction")
	kAM.LoadAnimation ("data/animations/SCP_extra2_M_interaction.nif", "SCP_extra2_M_interaction")
	kAM.LoadAnimation ("data/animations/SCP_extra1_M_interaction_1.nif", "SCP_extra1_M_interaction_1")
	kAM.LoadAnimation ("data/animations/SCP_extra1_M_interaction_2.nif", "SCP_extra1_M_interaction_1")

	kAM.LoadAnimation ("data/animations/SCP_chair_e1.nif", "SCP_chair_e1")
	kAM.LoadAnimation ("data/animations/SCP_chair_e2.nif", "SCP_chair_e2")

	# Large animations
	# Tactical Movement
	kAM.LoadAnimation ("data/animations/SCP_stand_t_l.nif", "SCP_stand_t_l")
	kAM.LoadAnimation ("data/animations/SCP_seated_t_l.nif", "SCP_seated_t_l")
	kAM.LoadAnimation ("data/animations/SCP_seatedm_t_l.nif", "SCP_seatedm_t_l")
	kAM.LoadAnimation ("data/animations/SCP_face_capt_t.nif", "SCP_face_capt_t")
	kAM.LoadAnimation ("data/animations/SCP_chair_T_face_capt.nif", "SCP_chair_T_face_capt")
	kAM.LoadAnimation ("data/animations/SCP_face_capt_t_reverse.nif", "SCP_face_capt_t_reverse")
	kAM.LoadAnimation ("data/animations/SCP_chair_T_face_capt_reverse.nif", "SCP_chair_T_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/DB_hit_t.NIF", "SCP_hit_t")

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
#	Unload any Galor bridge specific animations that are common
#
#	Args:	none
#
#	Return:	none
###############################################################################
def UnloadAnimations ():
	kAM = App.g_kAnimationManager

	kAM.FreeAnimation("SCP_Door_L1")
	kAM.FreeAnimation("SCP_Door_L1B")
	kAM.FreeAnimation("SCP_Door_L2")
	kAM.FreeAnimation("SCP_Door_L2B")

	# Small animations
	# Science Movement
	kAM.FreeAnimation("SCP_stand_s_s")
	kAM.FreeAnimation("SCP_seated_s_s")
	kAM.FreeAnimation("SCP_face_capt_s")
	kAM.FreeAnimation("SCP_chair_s_face_capt")
	kAM.FreeAnimation("SCP_face_capt_s_reverse")
	kAM.FreeAnimation("SCP_chair_s_face_capt_reverse")
	kAM.FreeAnimation("EB_chair_S_in")

	# Science Console Slides and Button Pushes
	kAM.FreeAnimation("EB_S_pushing_buttons_seated_A")
	kAM.FreeAnimation("EB_S_pushing_buttons_seated_B")
	kAM.FreeAnimation("EB_S_pushing_buttons_seated_C")

	# Science Talking to other stations

	# Engineer Movement
	kAM.FreeAnimation("SCP_stand_e_s")
	kAM.FreeAnimation("SCP_seated_e_s")
	kAM.FreeAnimation("SCP_face_capt_e")
	kAM.FreeAnimation("SCP_chair_e_face_capt")
	kAM.FreeAnimation("SCP_face_capt_e_reverse")
	kAM.FreeAnimation("SCP_chair_e_face_capt_reverse")
	kAM.FreeAnimation("EB_chair_E_in")

	# Engineer Console Slides and Button Pushes
	kAM.FreeAnimation("EB_E_pushing_buttons_seated_A")
	kAM.FreeAnimation("EB_E_pushing_buttons_seated_B")
	kAM.FreeAnimation("EB_E_pushing_buttons_seated_C")

	# Engineer Talking to other stations

	kAM.FreeAnimation("SCP_hit_s")
	kAM.FreeAnimation("SCP_hit_e")

	# medium animations
	# Helm Movement
	kAM.FreeAnimation("SCP_stand_h_m")
	kAM.FreeAnimation("SCP_seated_h_m")
	kAM.FreeAnimation("SCP_face_capt_h")
	kAM.FreeAnimation("SCP_face_capt_h_reverse")
	kAM.FreeAnimation("SCP_hit_h")


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
	kAM.FreeAnimation("SCP_seated_c_m")
	kAM.FreeAnimation("SCP_seatedm_c_m")
	kAM.FreeAnimation("SCP_stand_c_m")
	kAM.FreeAnimation("SCP_face_capt_c1")
	kAM.FreeAnimation("SCP_face_capt_c")
	kAM.FreeAnimation("SCP_face_capt_C_reverse")
	kAM.FreeAnimation("SCP_face_capt_c1_reverse")
	kAM.FreeAnimation("SCP_hit_c")
	kAM.FreeAnimation("SCP_stand_D_M")
	kAM.FreeAnimation("SCP_seated_D_M")


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
	kAM.FreeAnimation("SCP_hit_x")

	kAM.FreeAnimation("EB_X_pushing_buttons_A")
	kAM.FreeAnimation("EB_X_pushing_buttons_B")
	kAM.FreeAnimation("EB_X_pushing_buttons_C")
	kAM.FreeAnimation("EB_X_pushing_buttons_D")
	kAM.FreeAnimation("EB_X_pushing_buttons_E")
	kAM.FreeAnimation("EB_X_pushing_buttons_F")
	kAM.FreeAnimation("EB_X_pushing_buttons_G")

	#Extra
	kAM.FreeAnimation("SCP_L1toG3_S")
	kAM.FreeAnimation("SCP_L1toG3_M")
	kAM.FreeAnimation("SCP_L1toG3_L")

	kAM.FreeAnimation("SCP_L2toG1_S")
	kAM.FreeAnimation("SCP_L2toG1_M")
	kAM.FreeAnimation("SCP_L2toG1_L")

	kAM.FreeAnimation("SCP_L2toG2_S")
	kAM.FreeAnimation("SCP_L2toG2_M")
	kAM.FreeAnimation("SCP_L2toG2_L")
	kAM.FreeAnimation("SCP_chair_e1")

	kAM.FreeAnimation("SCP_G1toL2_S")
	kAM.FreeAnimation("SCP_G1toL2_M")
	kAM.FreeAnimation("SCP_G1toL2_L")
	
	kAM.FreeAnimation("SCP_G2toL2_S")
	kAM.FreeAnimation("SCP_G2toL2_M")
	kAM.FreeAnimation("SCP_G2toL2_L")
	
	kAM.FreeAnimation("SCP_G3toL1_S")
	kAM.FreeAnimation("SCP_G3toL1_M")
	kAM.FreeAnimation("SCP_G3toL1_L")

	kAM.FreeAnimation("SCP_extra3_M_interaction")
	kAM.FreeAnimation("SCP_extra2_M_interaction")
	kAM.FreeAnimation("SCP_extra1_M_interaction_1")
	kAM.FreeAnimation("SCP_extra1_M_interaction_2")

	kAM.FreeAnimation("SCP_chair_e1")
	kAM.FreeAnimation("SCP_chair_e2")
	
	# Large animations
	# Tactical Movement
	kAM.FreeAnimation("SCP_stand_t_l")
	kAM.FreeAnimation("SCP_seated_t_l")
	kAM.FreeAnimation("SCP_seatedm_t_l")
	kAM.FreeAnimation("SCP_face_capt_t")
	kAM.FreeAnimation("SCP_chair_T_face_capt")
	kAM.FreeAnimation("SCP_face_capt_t_reverse")
	kAM.FreeAnimation("SCP_chair_T_face_capt_reverse")
	kAM.FreeAnimation("SCP_hit_t")

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

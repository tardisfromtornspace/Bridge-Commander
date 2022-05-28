##############################################################################
#	Filename:	ExcaliburBridge.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	This contains the code to create and configure the Excalibur class bridge.
#	It is only called by LoadBridge.Initialize("ExcaliburBridge"), so don't
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
#	Create the Excalibur bridge model, viewscreen and main camera, attaching them
#	to the Set passed in.
#
#	Args:	pBridgeSet	- The Bridge set
#
#	Return:	none
###############################################################################
def CreateBridgeModel(pBridgeSet):
	iDetail = App.g_kImageManager.GetImageDetail()
	pcDetail = [ "High/", "High/", "High/" ]
	pcEnvPath = "data/Models/Sets/ExcaliburBridge/" + pcDetail[iDetail]

	# Pre-load the Bridge model and viewscreen
	App.g_kModelManager.LoadModel("data/Models/Sets/ExcaliburBridge/ExcaliburBridge.nif", None, pcEnvPath)
	App.g_kModelManager.LoadModel("data/Models/Sets/ExcaliburBridge/ExcaliburViewScreen.nif", None, pcEnvPath)

	# Load the viewscreen and set it up specially with SetViewScreen()
	pViewScreen = App.ViewScreenObject_Create("data/Models/Sets/ExcaliburBridge/ExcaliburViewScreen.nif")
	pBridgeSet.SetViewScreen(pViewScreen, "viewscreen")

	# Setup bridge object
	pBridgeObject = App.BridgeObjectClass_Create("data/Models/Sets/ExcaliburBridge/ExcaliburBridge.nif")
	pBridgeSet.AddObjectToSet(pBridgeObject, "bridge")
	pBridgeObject.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	pBridgeObject.SetAngleAxisRotation(0.000000, 1.000000, 0.000000, 0.000000)

	# setup hardpoints for dbridge.
	pPropertySet = pBridgeObject.GetPropertySet()
	import Bridge.ExcaliburBridgeProperties
	App.g_kModelPropertyManager.ClearLocalTemplates()
	reload(Bridge.ExcaliburBridgeProperties)
	Bridge.ExcaliburBridgeProperties.LoadPropertySet(pPropertySet)


	# Create camera
	lPos = GetBaseCameraPosition()
	pCamera = App.ZoomCameraObjectClass_Create(lPos[0], lPos[1], lPos[2], 1.570796, -0.000665, -0.087559, 0.996159, "maincamera")
	pCamera.SetMinZoom(0.8)
	pCamera.SetMaxZoom(1.0)
	pCamera.SetZoomTime(0.375)
	pBridgeSet.AddCameraToSet(pCamera, "maincamera")
	pCamera.Update( App.g_kUtopiaModule.GetGameTime() )
	App.g_kVarManager.SetFloatVariable("global", "fZoomTuneState", 0)

	# Load Excalibur bridge specific sounds
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
	return (0,0,0)

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
	import Bridge.Characters.ExcFelix
	import Bridge.Characters.ExcKiska
	import Bridge.Characters.ExcSaffi
	import Bridge.Characters.ExcBrex
	import Bridge.Characters.ExcMiguel

	import Bridge.Characters.ExcFemaleExtra1
	import Bridge.Characters.ExcFemaleExtra2
	import Bridge.Characters.ExcFemaleExtra3
	import Bridge.Characters.ExcMaleExtra1
	import Bridge.Characters.ExcMaleExtra2
	import Bridge.Characters.ExcMaleExtra3

	pExcFelix = App.CharacterClass_Cast(pBridgeSet.GetObject("Tactical"))
	pExcKiska = App.CharacterClass_Cast(pBridgeSet.GetObject("Helm"))
	pExcSaffi = App.CharacterClass_Cast(pBridgeSet.GetObject("XO"))
	pExcMiguel = App.CharacterClass_Cast(pBridgeSet.GetObject("Science"))
	pExcBrex = App.CharacterClass_Cast(pBridgeSet.GetObject("Engineer"))

	pExcFemaleExtra1 = App.CharacterClass_Cast(pBridgeSet.GetObject("FemaleExtra1"))
	pExcFemaleExtra2 = App.CharacterClass_Cast(pBridgeSet.GetObject("FemaleExtra2"))
	pExcFemaleExtra3 = App.CharacterClass_Cast(pBridgeSet.GetObject("FemaleExtra3"))

	pExcMaleExtra1 = App.CharacterClass_Cast(pBridgeSet.GetObject("MaleExtra1"))
	pExcMaleExtra2 = App.CharacterClass_Cast(pBridgeSet.GetObject("MaleExtra2"))
	pExcMaleExtra3 = App.CharacterClass_Cast(pBridgeSet.GetObject("MaleExtra3"))

	Bridge.Characters.ExcFelix.ConfigureForExcalibur(pExcFelix)
	Bridge.Characters.ExcKiska.ConfigureForExcalibur(pExcKiska)
	Bridge.Characters.ExcSaffi.ConfigureForExcalibur(pExcSaffi)
	Bridge.Characters.ExcMiguel.ConfigureForExcalibur(pExcMiguel)
	Bridge.Characters.ExcBrex.ConfigureForExcalibur(pExcBrex)

	if (pExcFemaleExtra1):
		Bridge.Characters.ExcFemaleExtra1.ConfigureForExcalibur(pExcFemaleExtra1)
	if (pExcFemaleExtra2):
		Bridge.Characters.ExcFemaleExtra2.ConfigureForExcalibur(pExcFemaleExtra2)
	if (pExcFemaleExtra3):
		Bridge.Characters.ExcFemaleExtra3.ConfigureForExcalibur(pExcFemaleExtra3)
	if (pExcMaleExtra1):
		Bridge.Characters.ExcMaleExtra1.ConfigureForExcalibur(pExcMaleExtra1)
	if (pExcMaleExtra2):
		Bridge.Characters.ExcMaleExtra2.ConfigureForExcalibur(pExcMaleExtra2)
	if (pExcMaleExtra3):
		Bridge.Characters.ExcMaleExtra3.ConfigureForExcalibur(pExcMaleExtra3)

	pCamera = App.ZoomCameraObjectClass_GetObject(pBridgeSet, "maincamera")
	pCamera.SetTranslateXYZ(-24.683736, 65.585, 55.678)


###############################################################################
#	LoadSounds()
#
#	Load any Excalibur bridge specific sounds
#
#	Args:	none
#
#	Return:	none
###############################################################################
def LoadSounds():

#	debug("Loading Excalibur door sound")

	pGame = App.Game_GetCurrentGame()
	pGame.LoadSoundInGroup("sfx/door.wav",  "LiftDoor", "BridgeGeneric")


###############################################################################
#	UnloadSounds()
#
#	Unload any Excalibur bridge specific sounds
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
#	Load any Excalibur bridge specific animations that are common
#
#	Args:	none
#
#	Return:	none
###############################################################################
def PreloadAnimations ():
	kAM = App.g_kAnimationManager

	kAM.LoadAnimation ("data/animations/Exc_door_L1.nif", "Exc_Door_L1")
	kAM.LoadAnimation ("data/animations/Exc_door_L2.nif", "Exc_Door_L2")

	# Small animations
	# Science Movement
	kAM.LoadAnimation ("data/animations/Exc_stand_s_s.nif", "Exc_stand_s_s")
	kAM.LoadAnimation ("data/animations/Exc_seated_s_s.nif", "Exc_seated_s_s")
	kAM.LoadAnimation ("data/animations/Exc_face_capt_s.nif", "Exc_face_capt_s")
	kAM.LoadAnimation ("data/animations/Exc_chair_s_face_capt.nif", "Exc_chair_s_face_capt")
	kAM.LoadAnimation ("data/animations/Exc_face_capt_s_reverse.nif", "Exc_face_capt_s_reverse")
	kAM.LoadAnimation ("data/animations/Exc_chair_s_face_capt_reverse.nif", "Exc_chair_s_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/EB_chair_S_in.nif", "EB_chair_S_in")

	# Science Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/EB_S_pushing_buttons_seated_A.NIF", "EB_S_pushing_buttons_seated_A")
	kAM.LoadAnimation ("data/animations/EB_S_pushing_buttons_seated_B.NIF", "EB_S_pushing_buttons_seated_B")
	kAM.LoadAnimation ("data/animations/EB_S_pushing_buttons_seated_C.NIF", "EB_S_pushing_buttons_seated_C")

	# Science Talking to other stations

	# Engineer Movement
	kAM.LoadAnimation ("data/animations/Exc_stand_e_s.nif", "Exc_stand_e_s")
	kAM.LoadAnimation ("data/animations/Exc_seated_e_s.nif", "Exc_seated_e_s")
	kAM.LoadAnimation ("data/animations/Exc_face_capt_e.nif", "Exc_face_capt_e")
	kAM.LoadAnimation ("data/animations/Exc_chair_e_face_capt.nif", "Exc_chair_e_face_capt")
	kAM.LoadAnimation ("data/animations/Exc_face_capt_e_reverse.nif", "Exc_face_capt_e_reverse")
	kAM.LoadAnimation ("data/animations/Exc_chair_e_face_capt_reverse.nif", "Exc_chair_e_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/EB_chair_E_in.nif", "EB_chair_E_in")

	# Engineer Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/EB_S_pushing_buttons_seated_A.NIF", "Int_E_pushing_buttons_seated_A")
	kAM.LoadAnimation ("data/animations/EB_S_pushing_buttons_seated_B.NIF", "Int_E_pushing_buttons_seated_B")
	kAM.LoadAnimation ("data/animations/EB_S_pushing_buttons_seated_C.NIF", "Int_E_pushing_buttons_seated_C")
	kAM.LoadAnimation ("data/animations/EB_S_pushing_buttons_seated_A.NIF", "Int_E_pushing_buttons_seated_D")
	kAM.LoadAnimation ("data/animations/EB_S_pushing_buttons_seated_B.NIF", "Int_E_pushing_buttons_seated_E")
	kAM.LoadAnimation ("data/animations/EB_S_pushing_buttons_seated_C.NIF", "Int_E_pushing_buttons_seated_F")
	kAM.LoadAnimation ("data/animations/EB_S_pushing_buttons_seated_A.NIF", "Int_E_pushing_buttons_seated_G")
	kAM.LoadAnimation ("data/animations/EB_S_pushing_buttons_seated_B.NIF", "Int_E_pushing_buttons_seated_H")

	# Engineer Talking to other stations

	# 
	# medium animations
	# Helm Movement
	kAM.LoadAnimation ("data/animations/Exc_stand_h_m.nif", "Exc_stand_h_m")
	kAM.LoadAnimation ("data/animations/Exc_seated_h_m.nif", "Exc_seated_h_m")
	kAM.LoadAnimation ("data/animations/Exc_face_capt_h.nif", "Exc_face_capt_h")
	kAM.LoadAnimation ("data/animations/Exc_chair_H_face_capt.nif", "Exc_chair_H_face_capt")
	kAM.LoadAnimation ("data/animations/Exc_face_capt_h_reverse.nif", "Exc_face_capt_h_reverse")
	kAM.LoadAnimation ("data/animations/Exc_chair_H_face_capt_reverse.nif", "Exc_chair_H_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/Int_glance_h_m.nif", "Exc_glance_h_m")
	kAM.LoadAnimation ("data/animations/Int_glance_h_m_reverse.nif", "Exc_glance_h_m_reverse")

	kAM.LoadAnimation ("data/animations/EB_hit_h.NIF", "Exc_hit_h")


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
	kAM.LoadAnimation ("data/animations/Exc_seated_C_M.nif", "Exc_seated_c_m")
	kAM.LoadAnimation ("data/animations/Exc_stand_V_M.nif", "Exc_stand_c_m")
	kAM.LoadAnimation ("data/animations/Exc_face_capt_c1.nif", "Exc_face_capt_c1")
	kAM.LoadAnimation ("data/animations/Exc_face_capt_c.nif", "Exc_face_capt_c")
	kAM.LoadAnimation ("data/animations/Exc_face_capt_C_reverse.NIF", "Exc_face_capt_C_reverse")
	kAM.LoadAnimation ("data/animations/Exc_face_capt_c1_reverse.NIF", "Exc_face_capt_c1_reverse")
	kAM.LoadAnimation ("data/animations/EB_hit_c.NIF", "Int_hit_c")

	#Commander interaction
	kAM.LoadAnimation ("data/animations/Exc_c_interaction.NIF", "Exc_C_pushing_buttons_seated_A")
	kAM.LoadAnimation ("data/animations/Exc_c_interaction.NIF", "Exc_C_pushing_buttons_seated_B")
	kAM.LoadAnimation ("data/animations/Exc_c_interaction.NIF", "Exc_C_pushing_buttons_seated_C")
	kAM.LoadAnimation ("data/animations/Exc_c_interaction.NIF", "Exc_C_pushing_buttons_seated_D")
	kAM.LoadAnimation ("data/animations/Exc_c_interaction.NIF", "Exc_C_pushing_buttons_seated_E")
	kAM.LoadAnimation ("data/animations/Exc_c_interaction.NIF", "Exc_C_pushing_buttons_seated_F")
	kAM.LoadAnimation ("data/animations/Exc_c_interaction.NIF", "Exc_C_pushing_buttons_seated_G")
	kAM.LoadAnimation ("data/animations/Exc_c_interaction.NIF", "Exc_C_pushing_buttons_seated_H")

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
	kAM.LoadAnimation ("data/animations/EB_hit_x.NIF", "Exc_hit_x")

	# Extras
	kAM.LoadAnimation ("data/animations/Exc_L1toG3_S.nif", "Exc_L1toG3_S")
	kAM.LoadAnimation ("data/animations/Exc_L1toG3_M.nif", "Exc_L1toG3_M")
	kAM.LoadAnimation ("data/animations/Exc_L1toG3_L.nif", "Exc_L1toG3_L")

	kAM.LoadAnimation ("data/animations/Exc_L2toG1_S.nif", "Exc_L2toG1_S")
	kAM.LoadAnimation ("data/animations/Exc_L2toG1_M.nif", "Exc_L2toG1_M")
	kAM.LoadAnimation ("data/animations/Exc_L2toG1_L.nif", "Exc_L2toG1_L")

	kAM.LoadAnimation ("data/animations/Exc_L2toG2_S.nif", "Exc_L2toG2_S")
	kAM.LoadAnimation ("data/animations/Exc_L2toG2_M.nif", "Exc_L2toG2_M")
	kAM.LoadAnimation ("data/animations/Exc_L2toG2_L.nif", "Exc_L2toG2_L")

	kAM.LoadAnimation ("data/animations/Exc_G1toL2_S.nif", "Exc_G1toL2_S")
	kAM.LoadAnimation ("data/animations/Exc_G1toL2_M.nif", "Exc_G1toL2_M")
	kAM.LoadAnimation ("data/animations/Exc_G1toL2_L.nif", "Exc_G1toL2_L")
	
	kAM.LoadAnimation ("data/animations/Exc_G2toL2_S.nif", "Exc_G2toL2_S")
	kAM.LoadAnimation ("data/animations/Exc_G2toL2_M.nif", "Exc_G2toL2_M")
	kAM.LoadAnimation ("data/animations/Exc_G2toL2_L.nif", "Exc_G2toL2_L")
	
	kAM.LoadAnimation ("data/animations/Exc_G3toL1_S.nif", "Exc_G3toL1_S")
	kAM.LoadAnimation ("data/animations/Exc_G3toL1_M.nif", "Exc_G3toL1_M")
	kAM.LoadAnimation ("data/animations/Exc_G3toL1_L.nif", "Exc_G3toL1_L")


	# Large animations
	# Tactical Movement
	kAM.LoadAnimation ("data/animations/Exc_stand_t_l.nif", "Exc_stand_t_l")
	kAM.LoadAnimation ("data/animations/Exc_seated_t_l.nif", "Exc_seated_t_l")
	kAM.LoadAnimation ("data/animations/Exc_face_capt_t.nif", "Exc_face_capt_t")
	kAM.LoadAnimation ("data/animations/Exc_chair_T_face_capt.nif", "Exc_chair_T_face_capt")
	kAM.LoadAnimation ("data/animations/Exc_face_capt_t_reverse.nif", "Exc_face_capt_t_reverse")
	kAM.LoadAnimation ("data/animations/Exc_chair_T_face_capt_reverse.nif", "Exc_chair_T_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/EB_hit_t.NIF", "Exc_hit_t")

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
#	Unload any Excalibur bridge specific animations that are common
#
#	Args:	none
#
#	Return:	none
###############################################################################
def UnloadAnimations ():
	kAM = App.g_kAnimationManager

	kAM.FreeAnimation("Exc_Door_L1")
	kAM.FreeAnimation("Exc_Door_L2")

	# Small animations
	# Science Movement
	kAM.FreeAnimation("Exc_stand_s_s")
	kAM.FreeAnimation("Exc_seated_s_s")
	kAM.FreeAnimation("Exc_face_capt_s")
	kAM.FreeAnimation("Exc_chair_s_face_capt")
	kAM.FreeAnimation("Exc_face_capt_s_reverse")
	kAM.FreeAnimation("Exc_chair_s_face_capt_reverse")
	kAM.FreeAnimation("EB_chair_S_in")

	# Science Console Slides and Button Pushes
	kAM.FreeAnimation("EB_S_pushing_buttons_seated_A")
	kAM.FreeAnimation("EB_S_pushing_buttons_seated_B")
	kAM.FreeAnimation("EB_S_pushing_buttons_seated_C")

	# Science Talking to other stations

	# Engineer Movement
	kAM.FreeAnimation("Exc_stand_e_s")
	kAM.FreeAnimation("Exc_seated_e_s")
	kAM.FreeAnimation("Exc_face_capt_e")
	kAM.FreeAnimation("Exc_chair_e_face_capt")
	kAM.FreeAnimation("Exc_face_capt_e_reverse")
	kAM.FreeAnimation("Exc_chair_e_face_capt_reverse")
	kAM.FreeAnimation("EB_chair_E_in")

	# Engineer Console Slides and Button Pushes
	kAM.FreeAnimation("Int_E_pushing_buttons_seated_A")
	kAM.FreeAnimation("Int_E_pushing_buttons_seated_B")
	kAM.FreeAnimation("Int_E_pushing_buttons_seated_C")
	kAM.FreeAnimation("Int_E_pushing_buttons_seated_D")
	kAM.FreeAnimation("Int_E_pushing_buttons_seated_E")
	kAM.FreeAnimation("Int_E_pushing_buttons_seated_F")
	kAM.FreeAnimation("Int_E_pushing_buttons_seated_G")

	# Engineer Talking to other stations

	# medium animations
	# Helm Movement
	kAM.FreeAnimation("Exc_stand_h_m")
	kAM.FreeAnimation("Exc_seated_h_m")
	kAM.FreeAnimation("Exc_face_capt_h")
	kAM.FreeAnimation("Exc_face_capt_h_reverse")
	kAM.FreeAnimation("Exc_hit_h")


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
	kAM.FreeAnimation("Exc_seated_c_m")
	kAM.FreeAnimation("Exc_stand_c_m")
	kAM.FreeAnimation("Exc_face_capt_c1")
	kAM.FreeAnimation("Exc_face_capt_c")
	kAM.FreeAnimation("Exc_face_capt_C_reverse")
	kAM.FreeAnimation("Exc_face_capt_c1_reverse")
	kAM.FreeAnimation("Exc_hit_c")
	kAM.FreeAnimation("Exc_stand_D_M")
	kAM.FreeAnimation("Exc_seated_D_M")

	kAM.FreeAnimation("Exc_C_pushing_buttons_seated_A")
	kAM.FreeAnimation("Exc_C_pushing_buttons_seated_B")
	kAM.FreeAnimation("Exc_C_pushing_buttons_seated_C")
	kAM.FreeAnimation("Exc_C_pushing_buttons_seated_D")
	kAM.FreeAnimation("Exc_C_pushing_buttons_seated_E")
	kAM.FreeAnimation("Exc_C_pushing_buttons_seated_F")
	kAM.FreeAnimation("Exc_C_pushing_buttons_seated_G")

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
	kAM.FreeAnimation("Exc_hit_x")

	kAM.FreeAnimation("EB_X_pushing_buttons_A")
	kAM.FreeAnimation("EB_X_pushing_buttons_B")
	kAM.FreeAnimation("EB_X_pushing_buttons_C")
	kAM.FreeAnimation("EB_X_pushing_buttons_D")
	kAM.FreeAnimation("EB_X_pushing_buttons_E")
	kAM.FreeAnimation("EB_X_pushing_buttons_F")
	kAM.FreeAnimation("EB_X_pushing_buttons_G")

	#Extra
	kAM.FreeAnimation("Exc_L1toG3_S")
	kAM.FreeAnimation("Exc_L1toG3_M")
	kAM.FreeAnimation("Exc_L1toG3_L")

	kAM.FreeAnimation("Exc_L2toG1_S")
	kAM.FreeAnimation("Exc_L2toG1_M")
	kAM.FreeAnimation("Exc_L2toG1_L")

	kAM.FreeAnimation("Exc_L2toG2_S")
	kAM.FreeAnimation("Exc_L2toG2_M")
	kAM.FreeAnimation("Exc_L2toG2_L")

	kAM.FreeAnimation("Exc_G1toL2_S")
	kAM.FreeAnimation("Exc_G1toL2_M")
	kAM.FreeAnimation("Exc_G1toL2_L")
	
	kAM.FreeAnimation("Exc_G2toL2_S")
	kAM.FreeAnimation("Exc_G2toL2_M")
	kAM.FreeAnimation("Exc_G2toL2_L")
	
	kAM.FreeAnimation("Exc_G3toL1_S")
	kAM.FreeAnimation("Exc_G3toL1_M")
	kAM.FreeAnimation("Exc_G3toL1_L")
	
	# Large animations
	# Tactical Movement
	kAM.FreeAnimation("Exc_stand_t_l")
	kAM.FreeAnimation("Exc_seated_t_l")
	kAM.FreeAnimation("Exc_face_capt_t")
	kAM.FreeAnimation("Exc_chair_T_face_capt")
	kAM.FreeAnimation("Exc_face_capt_t_reverse")
	kAM.FreeAnimation("Exc_chair_T_face_capt_reverse")
	kAM.FreeAnimation("Exc_hit_t")

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

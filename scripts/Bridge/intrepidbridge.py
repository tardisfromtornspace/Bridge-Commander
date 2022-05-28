##############################################################################
#	Filename:	IntrepidBridge.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	This contains the code to create and configure the Intrepid class bridge.
#	It is only called by LoadBridge.Initialize("IntrepidBridge"), so don't
#	call these functions directly
#
#	Created:	9/12/00 -	DLitwin
###############################################################################
import App
import MissionLib

#NonSerializedObjects = ( "debug", )

#debug = App.CPyDebug(__name__).Print
#debug("Loading " + __name__ + " module...")

BridgeName = "Int"

###############################################################################
#	CreateBridgeModel()
#
#	Create the Intrepid bridge model, viewscreen and main camera, attaching them
#	to the Set passed in.
#
#	Args:	pBridgeSet	- The Bridge set
#
#	Return:	none
###############################################################################
def CreateBridgeModel(pBridgeSet):
	iDetail = App.g_kImageManager.GetImageDetail()
	pcDetail = [ "High/", "High/", "High/" ]
	pcEnvPath = "data/Models/Sets/intrepidbridgev3/" + pcDetail[iDetail]

	# Pre-load the Bridge model and viewscreen
	App.g_kModelManager.LoadModel("data/Models/Sets/intrepidbridgev3/intrepidbridge.nif", None, pcEnvPath)
	App.g_kModelManager.LoadModel("data/Models/Sets/intrepidbridgev3/intrepidViewScreen.nif", None, pcEnvPath)

	# Load the viewscreen and set it up specially with SetViewScreen()
	pViewScreen = App.ViewScreenObject_Create("data/Models/Sets/intrepidbridgev3/intrepidViewScreen.nif")
	pBridgeSet.SetViewScreen(pViewScreen, "viewscreen")

	# Setup bridge object
	pBridgeObject = App.BridgeObjectClass_Create("data/Models/Sets/intrepidbridgev3/intrepidbridge.nif")
	pBridgeSet.AddObjectToSet(pBridgeObject, "bridge")
	pBridgeObject.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	pBridgeObject.SetAngleAxisRotation(0.000000, 1.000000, 0.000000, 0.000000)

	# setup hardpoints for dbridge.
	pPropertySet = pBridgeObject.GetPropertySet()
	import Bridge.IntrepidBridgeProperties
	App.g_kModelPropertyManager.ClearLocalTemplates()
	reload(Bridge.IntrepidBridgeProperties)
	Bridge.IntrepidBridgeProperties.LoadPropertySet(pPropertySet)


	# Create camera
	lPos = GetBaseCameraPosition()
	pCamera = App.ZoomCameraObjectClass_Create(lPos[0], lPos[1], lPos[2], 1.570796, -0.000665, -0.087559, 0.996159, "maincamera")
	pCamera.SetMinZoom(0.8)
	pCamera.SetMaxZoom(1.0)
	pCamera.SetZoomTime(0.375)
	pBridgeSet.AddCameraToSet(pCamera, "maincamera")
	pCamera.Update( App.g_kUtopiaModule.GetGameTime() )
	App.g_kVarManager.SetFloatVariable("global", "fZoomTuneState", 0)

	# Load Intrepid bridge specific sounds
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
	return (-32.683736, 60.585, 55.678)

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
	import Bridge.Characters.IntFelix
	import Bridge.Characters.IntKiska
	import Bridge.Characters.IntSaffi
	import Bridge.Characters.IntBrex
	import Bridge.Characters.IntMiguel

	import Bridge.Characters.IntFemaleExtra1
	import Bridge.Characters.IntFemaleExtra2
	import Bridge.Characters.IntFemaleExtra3
	import Bridge.Characters.IntMaleExtra1
	import Bridge.Characters.IntMaleExtra2
	import Bridge.Characters.IntMaleExtra3

	pIntFelix = App.CharacterClass_Cast(pBridgeSet.GetObject("Tactical"))
	pIntKiska = App.CharacterClass_Cast(pBridgeSet.GetObject("Helm"))
	pIntSaffi = App.CharacterClass_Cast(pBridgeSet.GetObject("XO"))
	pIntMiguel = App.CharacterClass_Cast(pBridgeSet.GetObject("Science"))
	pIntBrex = App.CharacterClass_Cast(pBridgeSet.GetObject("Engineer"))

	pIntFemaleExtra1 = App.CharacterClass_Cast(pBridgeSet.GetObject("FemaleExtra1"))
	pIntFemaleExtra2 = App.CharacterClass_Cast(pBridgeSet.GetObject("FemaleExtra2"))
	pIntFemaleExtra3 = App.CharacterClass_Cast(pBridgeSet.GetObject("FemaleExtra3"))

	pIntMaleExtra1 = App.CharacterClass_Cast(pBridgeSet.GetObject("MaleExtra1"))
	pIntMaleExtra2 = App.CharacterClass_Cast(pBridgeSet.GetObject("MaleExtra2"))
	pIntMaleExtra3 = App.CharacterClass_Cast(pBridgeSet.GetObject("MaleExtra3"))

	Bridge.Characters.IntFelix.ConfigureForIntrepid(pIntFelix)
	Bridge.Characters.IntKiska.ConfigureForIntrepid(pIntKiska)
	Bridge.Characters.IntSaffi.ConfigureForIntrepid(pIntSaffi)
	Bridge.Characters.IntMiguel.ConfigureForIntrepid(pIntMiguel)
	Bridge.Characters.IntBrex.ConfigureForIntrepid(pIntBrex)

	if (pIntFemaleExtra1):
		Bridge.Characters.IntFemaleExtra1.ConfigureForIntrepid(pIntFemaleExtra1)
	if (pIntFemaleExtra2):
		Bridge.Characters.IntFemaleExtra2.ConfigureForIntrepid(pIntFemaleExtra2)
	if (pIntFemaleExtra3):
		Bridge.Characters.IntFemaleExtra3.ConfigureForIntrepid(pIntFemaleExtra3)
	if (pIntMaleExtra1):
		Bridge.Characters.IntMaleExtra1.ConfigureForIntrepid(pIntMaleExtra1)
	if (pIntMaleExtra2):
		Bridge.Characters.IntMaleExtra2.ConfigureForIntrepid(pIntMaleExtra2)
	if (pIntMaleExtra3):
		Bridge.Characters.IntMaleExtra3.ConfigureForIntrepid(pIntMaleExtra3)

	pCamera = App.ZoomCameraObjectClass_GetObject(pBridgeSet, "maincamera")
	pCamera.SetTranslateXYZ(-32.683736, 60.585, 55.678)

###############################################################################
#	LoadSounds()
#
#	Load any Intrepid bridge specific sounds
#
#	Args:	none
#
#	Return:	none
###############################################################################
def LoadSounds():

#	debug("Loading Intrepid door sound")

	pGame = App.Game_GetCurrentGame()
	pGame.LoadSoundInGroup("sfx/door.wav",  "LiftDoor", "BridgeGeneric")


###############################################################################
#	UnloadSounds()
#
#	Unload any Intrepid bridge specific sounds
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
#	Load any Intrepid bridge specific animations that are common
#
#	Args:	none
#
#	Return:	none
###############################################################################
def PreloadAnimations ():
	kAM = App.g_kAnimationManager

	kAM.LoadAnimation ("data/animations/Int_door_L1.nif", "Int_Door_L1")
	kAM.LoadAnimation ("data/animations/Int_door_L2.nif", "Int_Door_L2")

	# Small animations
	# Science Movement
	kAM.LoadAnimation ("data/animations/Int_stand_s_s.nif", "Int_stand_s_s")
	kAM.LoadAnimation ("data/animations/Int_seated_s_s.nif", "Int_seated_s_s")
	kAM.LoadAnimation ("data/animations/Int_face_capt_s.nif", "Int_face_capt_s")
	kAM.LoadAnimation ("data/animations/Int_chair_s_face_capt.nif", "Int_chair_s_face_capt")
	kAM.LoadAnimation ("data/animations/Int_face_capt_s_reverse.nif", "Int_face_capt_s_reverse")
	kAM.LoadAnimation ("data/animations/Int_chair_s_face_capt_reverse.nif", "Int_chair_s_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/EB_chair_S_in.nif", "EB_chair_S_in")

	# Science Console Slides and Button Pushes
	kAM.LoadAnimation("data/animations/DB_S_pushing_buttons_A.NIF", "DB_S_pushing_buttons_A")
	kAM.LoadAnimation("data/animations/DB_S_pushing_buttons_B.NIF", "DB_S_pushing_buttons_B")
	kAM.LoadAnimation("data/animations/DB_S_pushing_buttons_C.NIF", "DB_S_pushing_buttons_C")
	kAM.LoadAnimation("data/animations/DB_S_pushing_buttons_D.NIF", "DB_S_pushing_buttons_D")

	# Science Talking to other stations

	# Engineer Movement
	kAM.LoadAnimation ("data/animations/Int_stand_e_s.nif", "Int_stand_e_s")
	kAM.LoadAnimation ("data/animations/Int_seated_e_s.nif", "Int_seated_e_s")
	kAM.LoadAnimation ("data/animations/Int_face_capt_e.nif", "Int_face_capt_e")
	kAM.LoadAnimation ("data/animations/Int_chair_e_face_capt.nif", "Int_chair_e_face_capt")
	kAM.LoadAnimation ("data/animations/Int_face_capt_e_reverse.nif", "Int_face_capt_e_reverse")
	kAM.LoadAnimation ("data/animations/Int_chair_e_face_capt_reverse.nif", "Int_chair_e_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/EB_chair_E_in.nif", "EB_chair_E_in")

	# Engineer Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/Int_e_console_l_high.NIF", "Int_E_pushing_buttons_seated_A")
	kAM.LoadAnimation ("data/animations/Int_e_console_r_high.NIF", "Int_E_pushing_buttons_seated_B")
	kAM.LoadAnimation ("data/animations/Int_e_console_l_medium.NIF", "Int_E_pushing_buttons_seated_C")
	kAM.LoadAnimation ("data/animations/Int_e_console_r_medium.NIF", "Int_E_pushing_buttons_seated_D")
	kAM.LoadAnimation ("data/animations/Int_e_console_l_low.NIF", "Int_E_pushing_buttons_seated_E")
	kAM.LoadAnimation ("data/animations/Int_e_console_r_low.NIF", "Int_E_pushing_buttons_seated_F")
	kAM.LoadAnimation ("data/animations/Int_e_console_l_lowered.NIF", "Int_E_pushing_buttons_seated_G")
	kAM.LoadAnimation ("data/animations/Int_e_console_r_standing.NIF", "Int_E_pushing_buttons_seated_H")

	# Engineer Talking to other stations

	# 
	# medium animations
	# Helm Movement
	kAM.LoadAnimation ("data/animations/Int_stand_h_m.nif", "Int_stand_h_m")
	kAM.LoadAnimation ("data/animations/Int_seated_h_m.nif", "Int_seated_h_m")
	kAM.LoadAnimation ("data/animations/Int_face_capt_h.nif", "Int_face_capt_h")
	kAM.LoadAnimation ("data/animations/Int_conn_chair.NIF", "Int_chair_H_face_capt")
	kAM.LoadAnimation ("data/animations/Int_face_capt_h_reverse.nif", "Int_face_capt_h_reverse")
	kAM.LoadAnimation ("data/animations/Int_conn_chair_reverse.nif", "Int_chair_H_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/Int_glance_h_m.nif", "Int_glance_h_m")
	kAM.LoadAnimation ("data/animations/Int_glance_h_m_reverse.nif", "Int_glance_h_m_reverse")

	kAM.LoadAnimation ("data/animations/EB_hit_h.NIF", "Int_hit_h")


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
	kAM.LoadAnimation ("data/animations/Int_seated_C_M.nif", "Int_seated_c_m")
	kAM.LoadAnimation ("data/animations/Int_stand_V_M.nif", "Int_stand_c_m")
	kAM.LoadAnimation ("data/animations/Int_face_capt_c1.nif", "Int_face_capt_c1")
	kAM.LoadAnimation ("data/animations/Int_face_capt_c.nif", "Int_face_capt_c")
	kAM.LoadAnimation ("data/animations/Int_face_capt_C_reverse.NIF", "Int_face_capt_C_reverse")
	kAM.LoadAnimation ("data/animations/Int_face_capt_c1_reverse.NIF", "Int_face_capt_c1_reverse")
	kAM.LoadAnimation ("data/animations/EB_hit_c.NIF", "Int_hit_c")


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
	kAM.LoadAnimation ("data/animations/EB_hit_x.NIF", "Int_hit_x")

	# Extras
	kAM.LoadAnimation ("data/animations/Int_L1toG3_S.nif", "Int_L1toG3_S")
	kAM.LoadAnimation ("data/animations/Int_L1toG3_M.nif", "Int_L1toG3_M")
	kAM.LoadAnimation ("data/animations/Int_L1toG3_L.nif", "Int_L1toG3_L")

	kAM.LoadAnimation ("data/animations/Int_L2toG1_S.nif", "Int_L2toG1_S")
	kAM.LoadAnimation ("data/animations/Int_L2toG1_M.nif", "Int_L2toG1_M")
	kAM.LoadAnimation ("data/animations/Int_L2toG1_L.nif", "Int_L2toG1_L")

	kAM.LoadAnimation ("data/animations/Int_L2toG2_S.nif", "Int_L2toG2_S")
	kAM.LoadAnimation ("data/animations/Int_L2toG2_M.nif", "Int_L2toG2_M")
	kAM.LoadAnimation ("data/animations/Int_L2toG2_L.nif", "Int_L2toG2_L")

	kAM.LoadAnimation ("data/animations/Int_G1toL2_S.nif", "Int_G1toL2_S")
	kAM.LoadAnimation ("data/animations/Int_G1toL2_M.nif", "Int_G1toL2_M")
	kAM.LoadAnimation ("data/animations/Int_G1toL2_L.nif", "Int_G1toL2_L")
	
	kAM.LoadAnimation ("data/animations/Int_G2toL2_S.nif", "Int_G2toL2_S")
	kAM.LoadAnimation ("data/animations/Int_G2toL2_M.nif", "Int_G2toL2_M")
	kAM.LoadAnimation ("data/animations/Int_G2toL2_L.nif", "Int_G2toL2_L")
	
	kAM.LoadAnimation ("data/animations/Int_G3toL1_S.nif", "Int_G3toL1_S")
	kAM.LoadAnimation ("data/animations/Int_G3toL1_M.nif", "Int_G3toL1_M")
	kAM.LoadAnimation ("data/animations/Int_G3toL1_L.nif", "Int_G3toL1_L")


	# Large animations
	# Tactical Movement
	kAM.LoadAnimation ("data/animations/Int_stand_t_l.nif", "Int_stand_t_l")
	kAM.LoadAnimation ("data/animations/Int_seated_t_l.nif", "Int_seated_t_l")
	kAM.LoadAnimation ("data/animations/Int_face_capt_t.nif", "Int_face_capt_t")
	kAM.LoadAnimation ("data/animations/Int_chair_T_face_capt.nif", "Int_chair_T_face_capt")
	kAM.LoadAnimation ("data/animations/Int_face_capt_t_reverse.nif", "Int_face_capt_t_reverse")
	kAM.LoadAnimation ("data/animations/Int_chair_T_face_capt_reverse.nif", "Int_chair_T_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/EB_hit_t.NIF", "Int_hit_t")

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
#	Unload any Intrepid bridge specific animations that are common
#
#	Args:	none
#
#	Return:	none
###############################################################################
def UnloadAnimations ():
	kAM = App.g_kAnimationManager

	kAM.FreeAnimation("Int_Door_L1")
	kAM.FreeAnimation("Int_Door_L2")

	# Small animations
	# Science Movement
	kAM.FreeAnimation("Int_stand_s_s")
	kAM.FreeAnimation("Int_seated_s_s")
	kAM.FreeAnimation("Int_face_capt_s")
	kAM.FreeAnimation("Int_chair_s_face_capt")
	kAM.FreeAnimation("Int_face_capt_s_reverse")
	kAM.FreeAnimation("Int_chair_s_face_capt_reverse")
	kAM.FreeAnimation("EB_chair_S_in")

	# Science Console Slides and Button Pushes
	kAM.FreeAnimation("DB_S_pushing_buttons_A")
	kAM.FreeAnimation("DB_S_pushing_buttons_B")
	kAM.FreeAnimation("DB_S_pushing_buttons_C")
	kAM.FreeAnimation("DB_S_pushing_buttons_D")

	# Science Talking to other stations

	# Engineer Movement
	kAM.FreeAnimation("Int_stand_e_s")
	kAM.FreeAnimation("Int_seated_e_s")
	kAM.FreeAnimation("Int_face_capt_e")
	kAM.FreeAnimation("Int_chair_e_face_capt")
	kAM.FreeAnimation("Int_face_capt_e_reverse")
	kAM.FreeAnimation("Int_chair_e_face_capt_reverse")
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
	kAM.FreeAnimation("Int_stand_h_m")
	kAM.FreeAnimation("Int_seated_h_m")
	kAM.FreeAnimation("Int_face_capt_h")
	kAM.FreeAnimation("Int_face_capt_h_reverse")
	kAM.FreeAnimation("Int_hit_h")


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
	kAM.FreeAnimation("Int_seated_c_m")
	kAM.FreeAnimation("Int_stand_c_m")
	kAM.FreeAnimation("Int_face_capt_c1")
	kAM.FreeAnimation("Int_face_capt_c")
	kAM.FreeAnimation("Int_face_capt_C_reverse")
	kAM.FreeAnimation("Int_face_capt_c1_reverse")
	kAM.FreeAnimation("Int_hit_c")
	kAM.FreeAnimation("Int_stand_D_M")
	kAM.FreeAnimation("Int_seated_D_M")

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
	kAM.FreeAnimation("Int_hit_x")

	kAM.FreeAnimation("EB_X_pushing_buttons_A")
	kAM.FreeAnimation("EB_X_pushing_buttons_B")
	kAM.FreeAnimation("EB_X_pushing_buttons_C")
	kAM.FreeAnimation("EB_X_pushing_buttons_D")
	kAM.FreeAnimation("EB_X_pushing_buttons_E")
	kAM.FreeAnimation("EB_X_pushing_buttons_F")
	kAM.FreeAnimation("EB_X_pushing_buttons_G")

	#Extra
	kAM.FreeAnimation("Int_L1toG3_S")
	kAM.FreeAnimation("Int_L1toG3_M")
	kAM.FreeAnimation("Int_L1toG3_L")

	kAM.FreeAnimation("Int_L2toG1_S")
	kAM.FreeAnimation("Int_L2toG1_M")
	kAM.FreeAnimation("Int_L2toG1_L")

	kAM.FreeAnimation("Int_L2toG2_S")
	kAM.FreeAnimation("Int_L2toG2_M")
	kAM.FreeAnimation("Int_L2toG2_L")

	kAM.FreeAnimation("Int_G1toL2_S")
	kAM.FreeAnimation("Int_G1toL2_M")
	kAM.FreeAnimation("Int_G1toL2_L")
	
	kAM.FreeAnimation("Int_G2toL2_S")
	kAM.FreeAnimation("Int_G2toL2_M")
	kAM.FreeAnimation("Int_G2toL2_L")
	
	kAM.FreeAnimation("Int_G3toL1_S")
	kAM.FreeAnimation("Int_G3toL1_M")
	kAM.FreeAnimation("Int_G3toL1_L")
	
	# Large animations
	# Tactical Movement
	kAM.FreeAnimation("Int_stand_t_l")
	kAM.FreeAnimation("Int_seated_t_l")
	kAM.FreeAnimation("Int_face_capt_t")
	kAM.FreeAnimation("Int_chair_T_face_capt")
	kAM.FreeAnimation("Int_face_capt_t_reverse")
	kAM.FreeAnimation("Int_chair_T_face_capt_reverse")
	kAM.FreeAnimation("Int_hit_t")

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

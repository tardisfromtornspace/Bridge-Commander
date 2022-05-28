##############################################################################
#	Filename:	RunaboutLate.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	This contains the code to create and configure the Defiant class bridge.
#	It is only called by LoadBridge.Initialize("RunaboutLate"), so don't
#	call these functions directly
#
#	    Created:	9/12/00 -	DLitwin
#           Modified: Defiant Bridge.py  L.C. Amaral 
#           Modified: 02/06/05             Blackrook32
###############################################################################
import App

#NonSerializedObjects = ( "debug", )

#debug = App.CPyDebug(__name__).Print
#debug("Loading " + __name__ + " module...")

###############################################################################
#	CreateBridgeModel()
#
#	Create the Defiant bridge model, viewscreen and main camera, attaching them
#	to the Set passed in.
#
#	Args:	pBridgeSet	- The Bridge set
#
#	Return:	none
###############################################################################
def CreateBridgeModel(pBridgeSet):
	iDetail = App.g_kImageManager.GetImageDetail()
	pcDetail = [ "Low/", "Medium/", "High/" ]
	pcEnvPath = "data/Models/Sets/RunaboutLate/" + pcDetail[iDetail]

	# Pre-load the Bridge model and viewscreen
	App.g_kModelManager.LoadModel("data/Models/Sets/RunaboutLate/RunaboutLate.nif", None, pcEnvPath)
	App.g_kModelManager.LoadModel("data/Models/Sets/RunaboutLate/RunaboutLate.nif", None, pcEnvPath)

	# Load the viewscreen and set it up specially with SetViewScreen()
	pViewScreen = App.ViewScreenObject_Create("data/Models/Sets/RunaboutLate/RunaboutViewScreen.nif")
	pBridgeSet.SetViewScreen(pViewScreen, "viewscreen")
	pViewScreen.SetScale(1.0)

	# Setup bridge object
	pBridgeObject = App.BridgeObjectClass_Create("data/Models/Sets/RunaboutLate/RunaboutLate.nif")
	pBridgeSet.AddObjectToSet(pBridgeObject, "bridge")
	pBridgeObject.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	pBridgeObject.SetAngleAxisRotation(0.000000, 1.000000, 0.000000, 0.000000)
	pBridgeObject.SetScale(1.0)

	# setup hardpoints for dbridge.
	pPropertySet = pBridgeObject.GetPropertySet()
	import Bridge.EBridgeProperties
	App.g_kModelPropertyManager.ClearLocalTemplates()
	reload(Bridge.EBridgeProperties)
	Bridge.EBridgeProperties.LoadPropertySet(pPropertySet)

	# Create camera
	lPos = GetBaseCameraPosition()
	pCamera = App.ZoomCameraObjectClass_Create(lPos[0], lPos[1], lPos[2], 3.1, 0.0, 0.0, 0.8, "maincamera")
	pCamera.SetMinZoom(0.8)
	pCamera.SetMaxZoom(1.0)
	pCamera.SetZoomTime(0.375)
	pBridgeSet.AddCameraToSet(pCamera, "maincamera")
	pCamera.Update( App.g_kUtopiaModule.GetGameTime() )
	App.g_kVarManager.SetFloatVariable("global", "fZoomTuneState", 0)

	# Load Defiant bridge specific sounds
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
	return (30, 150, 100)

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
	import Bridge.Characters.RunFelix
	import Bridge.Characters.RunKiska
	import Bridge.Characters.RunMiguel
	import Bridge.Characters.RunBrex
	import Bridge.Characters.RunSaffi

	pFelix  = App.CharacterClass_Cast(pBridgeSet.GetObject("Tactical"))
	pKiska  = App.CharacterClass_Cast(pBridgeSet.GetObject("Helm"))
	pSaffi  = App.CharacterClass_Cast(pBridgeSet.GetObject("XO"))
	pMiguel = App.CharacterClass_Cast(pBridgeSet.GetObject("Science"))
	pBrex   = App.CharacterClass_Cast(pBridgeSet.GetObject("Engineer"))
	
	Bridge.Characters.RunFelix.ConfigureForType11(pFelix)
	Bridge.Characters.RunKiska.ConfigureForType11(pKiska)
	Bridge.Characters.RunMiguel.ConfigureForType11(pMiguel)
	Bridge.Characters.RunBrex.ConfigureForType11(pBrex)
	Bridge.Characters.RunSaffi.ConfigureForType11(pSaffi)

	pCamera = App.ZoomCameraObjectClass_GetObject(pBridgeSet, "maincamera")
	pCamera.SetTranslateXYZ(30, 150, 100)


###############################################################################
#	LoadSounds()
#
#	Load any Type 11 bridge specific sounds
#
#	Args:	none
#
#	Return:	none
###############################################################################
def LoadSounds():

	pGame = App.Game_GetCurrentGame()
	pGame.LoadSoundInGroup("sfx/door.wav",  "LiftDoor", "BridgeGeneric")
                          
###############################################################################
#	UnloadSounds()
#
#	Unload any Type 11Cockpit  specific sounds
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
#	Load any Type11 Cockpit  specific animations that are common
#
#	Args:	none
#
#	Return:	none
###############################################################################
def PreloadAnimations ():
	kAM = App.g_kAnimationManager

	# Small animations
	# Science Movement
	kAM.LoadAnimation ("data/animations/Run_stand_s_s.nif", "Run_stand_s_s")
	kAM.LoadAnimation ("data/animations/Run_seated_s_s.nif", "Run_seated_s_s")
	kAM.LoadAnimation ("data/animations/EB_face_capt_s.nif", "EB_face_capt_s")
	kAM.LoadAnimation ("data/animations/EB_chair_s_face_capt.nif", "EB_chair_s_face_capt")
	kAM.LoadAnimation ("data/animations/EB_face_capt_s_reverse.nif", "EB_face_capt_s_reverse")
	kAM.LoadAnimation ("data/animations/EB_chair_s_face_capt_reverse.nif", "EB_chair_s_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/EB_chair_S_in.nif", "EB_chair_S_in")

	# Science Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/Run_S_pushing_buttons_A.NIF", "Run_S_pushing_buttons_A")
	kAM.LoadAnimation ("data/animations/Run_S_pushing_buttons_B.NIF", "Run_S_pushing_buttons_B")
	kAM.LoadAnimation ("data/animations/Run_S_pushing_buttons_C.NIF", "Run_S_pushing_buttons_C")
	kAM.LoadAnimation ("data/animations/Run_S_pushing_buttons_D.NIF", "Run_S_pushing_buttons_D")


	# Science Talking to other stations

	# Engineer Movement
	kAM.LoadAnimation ("data/animations/Run_stand_e_s.nif", "Run_stand_e_s")
	kAM.LoadAnimation ("data/animations/Run_seated_e_s.nif", "Run_seated_e_s")
	kAM.LoadAnimation ("data/animations/EB_face_capt_e.nif", "EB_face_capt_e")
	kAM.LoadAnimation ("data/animations/EB_chair_e_face_capt.nif", "EB_chair_e_face_capt")
	kAM.LoadAnimation ("data/animations/EB_face_capt_e_reverse.nif", "EB_face_capt_e_reverse")
	kAM.LoadAnimation ("data/animations/EB_chair_e_face_capt_reverse.nif", "EB_chair_e_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/EB_chair_E_in.nif", "EB_chair_E_in")

	# Engineer Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/Run_S_pushing_buttons_A.NIF", "Run_S_pushing_buttons_A")
	kAM.LoadAnimation ("data/animations/Run_S_pushing_buttons_B.NIF", "Run_S_pushing_buttons_B")
	kAM.LoadAnimation ("data/animations/Run_S_pushing_buttons_C.NIF", "Run_S_pushing_buttons_C")
	kAM.LoadAnimation ("data/animations/Run_S_pushing_buttons_D.NIF", "Run_S_pushing_buttons_D")


	# Engineer Talking to other stations

	# 
	# medium animations
	# Helm Movement
	kAM.LoadAnimation ("data/animations/Run_stand_h_m.nif", "Run_stand_h_m")
	kAM.LoadAnimation ("data/animations/Run_seated_h_m.nif", "Run_seated_h_m")
	kAM.LoadAnimation ("data/animations/EB_face_capt_h.nif", "EB_face_capt_h")
	kAM.LoadAnimation ("data/animations/EB_chair_H_face_capt.nif", "EB_chair_H_face_capt")
	kAM.LoadAnimation ("data/animations/EB_face_capt_h_reverse.nif", "EB_face_capt_h_reverse")
	kAM.LoadAnimation ("data/animations/EB_chair_H_face_capt_reverse.nif", "EB_chair_H_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/EB_hit_h.NIF", "EB_hit_h")


	# Helm Console Slides and Button Pushes
	kAM.LoadAnimation("data/animations/DB_H_Console_Slide_A.NIF", "DB_H_console_slide_A")
	kAM.LoadAnimation("data/animations/DB_H_Console_Slide_B.NIF", "DB_H_console_slide_B")
	kAM.LoadAnimation("data/animations/DB_H_Console_Slide_C.NIF", "DB_H_console_slide_C")
	kAM.LoadAnimation("data/animations/DB_H_Console_Slide_D.NIF", "DB_H_console_slide_D")

	kAM.LoadAnimation("data/animations/DB_H_pushing_buttons_A.NIF", "DB_H_pushing_buttons_A")
	kAM.LoadAnimation("data/animations/DB_H_pushing_buttons_B.NIF", "DB_H_pushing_buttons_B")
	kAM.LoadAnimation("data/animations/DB_H_pushing_buttons_C.NIF", "DB_H_pushing_buttons_C")
	kAM.LoadAnimation("data/animations/DB_H_pushing_buttons_D.NIF", "DB_H_pushing_buttons_D")
	kAM.LoadAnimation("data/animations/DB_H_pushing_buttons_E.NIF", "DB_H_pushing_buttons_E")
	kAM.LoadAnimation("data/animations/DB_H_pushing_buttons_F.NIF", "DB_H_pushing_buttons_F")

	# Helm Talking to other stations
	kAM.LoadAnimation ("data/animations/EB_H_Talk_to_C_M.NIF", "EB_H_Talk_to_C_M")
	kAM.LoadAnimation ("data/animations/EB_H_Talk_to_E_M.NIF", "EB_H_Talk_to_E_M")
	kAM.LoadAnimation ("data/animations/EB_H_Talk_to_S_M.NIF", "EB_H_Talk_to_S_M")
	kAM.LoadAnimation ("data/animations/EB_H_Talk_to_T_M.NIF", "EB_H_Talk_to_T_M")
	kAM.LoadAnimation ("data/animations/EB_H_Talk_fin_C_M.NIF", "EB_H_Talk_fin_C_M")
	kAM.LoadAnimation ("data/animations/EB_H_Talk_fin_E_M.NIF", "EB_H_Talk_fin_E_M")
	kAM.LoadAnimation ("data/animations/EB_H_Talk_fin_S_M.NIF", "EB_H_Talk_fin_S_M")
	kAM.LoadAnimation ("data/animations/EB_H_Talk_fin_T_M.NIF", "EB_H_Talk_fin_T_M")

	# Large animations
	# Tactical Movement
	kAM.LoadAnimation ("data/animations/Run_stand_t_l.nif", "Run_stand_t_l")
	kAM.LoadAnimation ("data/animations/Run_seated_t_l.nif", "Run_seated_t_l")
	kAM.LoadAnimation ("data/animations/Run_seatedm_t_l.nif", "Run_seatedm_t_l")
	kAM.LoadAnimation ("data/animations/EB_face_capt_t.nif", "EB_face_capt_t")
	kAM.LoadAnimation ("data/animations/EB_chair_T_face_capt.nif", "EB_chair_T_face_capt")
	kAM.LoadAnimation ("data/animations/EB_face_capt_t_reverse.nif", "EB_face_capt_t_reverse")
	kAM.LoadAnimation ("data/animations/EB_chair_T_face_capt_reverse.nif", "EB_chair_T_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/EB_hit_t.NIF", "EB_hit_t")

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
#	Unload any Defiant bridge specific animations that are common
#
#	Args:	none
#
#	Return:	none
###############################################################################
def UnloadAnimations ():
	kAM = App.g_kAnimationManager

	# Small animations
	# Science Movement
	kAM.FreeAnimation("Run_stand_s_s")
	kAM.FreeAnimation("Run_seated_s_s")
	kAM.FreeAnimation("EB_face_capt_s")
	kAM.FreeAnimation("EB_chair_s_face_capt")
	kAM.FreeAnimation("EB_face_capt_s_reverse")
	kAM.FreeAnimation("EB_chair_s_face_capt_reverse")
	kAM.FreeAnimation("EB_chair_S_in")

	# Science Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/Run_S_pushing_buttons_A.NIF", "Run_S_pushing_buttons_A")
	kAM.LoadAnimation ("data/animations/Run_S_pushing_buttons_B.NIF", "Run_S_pushing_buttons_B")
	kAM.LoadAnimation ("data/animations/Run_S_pushing_buttons_C.NIF", "Run_S_pushing_buttons_C")
	kAM.LoadAnimation ("data/animations/Run_S_pushing_buttons_D.NIF", "Run_S_pushing_buttons_D")

	# Science Talking to other stations

	# Engineer Movement
	kAM.FreeAnimation("Run_stand_e_s")
	kAM.FreeAnimation("Run_seated_e_s")
	kAM.FreeAnimation("EB_face_capt_e")
	kAM.FreeAnimation("EB_chair_e_face_capt")
	kAM.FreeAnimation("EB_face_capt_e_reverse")
	kAM.FreeAnimation("EB_chair_e_face_capt_reverse")
	kAM.FreeAnimation("EB_chair_E_in")

	# Engineer Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/Run_S_pushing_buttons_A.NIF", "Run_S_pushing_buttons_A")
	kAM.LoadAnimation ("data/animations/Run_S_pushing_buttons_B.NIF", "Run_S_pushing_buttons_B")
	kAM.LoadAnimation ("data/animations/Run_S_pushing_buttons_C.NIF", "Run_S_pushing_buttons_C")
	kAM.LoadAnimation ("data/animations/Run_S_pushing_buttons_D.NIF", "Run_S_pushing_buttons_D")
	
	# Engineer Talking to other stations
	
	# medium animations
	# Helm Movement
	kAM.FreeAnimation("Run_stand_h_m")
	kAM.FreeAnimation("Run_seated_h_m")
	kAM.FreeAnimation("EB_face_capt_h")
	kAM.FreeAnimation("EB_chair_H_face_capt")
	kAM.FreeAnimation("EB_face_capt_h_reverse")
	kAM.FreeAnimation("EB_chair_H_face_capt_reverse")
	kAM.FreeAnimation("EB_hit_h")


	# Helm Console Slides and Button Pushes
	kAM.FreeAnimation("DB_H_console_slide_A")
	kAM.FreeAnimation("DB_H_console_slide_B")
	kAM.FreeAnimation("DB_H_console_slide_C")
	kAM.FreeAnimation("DB_H_console_slide_D")

	kAM.FreeAnimation("DB_H_pushing_buttons_A")
	kAM.FreeAnimation("DB_H_pushing_buttons_B")
	kAM.FreeAnimation("DB_H_pushing_buttons_C")
	kAM.FreeAnimation("DB_H_pushing_buttons_D")
	kAM.FreeAnimation("DB_H_pushing_buttons_E")
	kAM.FreeAnimation("DB_H_pushing_buttons_F")


	# Helm Talking to other stations
	kAM.FreeAnimation("EB_H_Talk_to_C_M")
	kAM.FreeAnimation("EB_H_Talk_to_E_M")
	kAM.FreeAnimation("EB_H_Talk_to_S_M")
	kAM.FreeAnimation("EB_H_Talk_to_T_M")
	kAM.FreeAnimation("EB_H_Talk_fin_C_M")
	kAM.FreeAnimation("EB_H_Talk_fin_E_M")
	kAM.FreeAnimation("EB_H_Talk_fin_S_M")
	kAM.FreeAnimation("EB_H_Talk_fin_T_M")

	
	# Large animations
	# Tactical Movement
	kAM.FreeAnimation("Run_stand_t_l")
	kAM.FreeAnimation("Run_seated_t_l")
	kAM.FreeAnimation("Run_seatedm_t_l")
	kAM.FreeAnimation("EB_face_capt_t")
	kAM.FreeAnimation("EB_chair_T_face_capt")
	kAM.FreeAnimation("EB_face_capt_t_reverse")
	kAM.FreeAnimation("EB_chair_T_face_capt_reverse")
	kAM.FreeAnimation("EB_hit_t")

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

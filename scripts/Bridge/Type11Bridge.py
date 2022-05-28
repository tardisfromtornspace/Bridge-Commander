##############################################################################
#	Filename:	Type11Bridge.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	This contains the code to create and configure the Defiant class bridge.
#	It is only called by LoadBridge.Initialize("type11bridge"), so don't
#	call these functions directly
#
#	Created:	9/12/00 -	DLitwin
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
	pcEnvPath = "data/Models/Sets/Type11/" + pcDetail[iDetail]

	# Pre-load the Bridge model and viewscreen
	App.g_kModelManager.LoadModel("data/Models/Sets/Type11/Type11Bridge_withseats.nif", None, pcEnvPath)
	App.g_kModelManager.LoadModel("data/Models/Sets/Type11/Type11bridgeviewscreen.nif", None, pcEnvPath)

	# Load the viewscreen and set it up specially with SetViewScreen()
	pViewScreen = App.ViewScreenObject_Create("data/Models/Sets/Type11/Type11bridgeviewscreen.nif")
	pBridgeSet.SetViewScreen(pViewScreen, "viewscreen")
	pViewScreen.SetScale(1.0)

	# Setup bridge object
	pBridgeObject = App.BridgeObjectClass_Create("data/Models/Sets/Type11/Type11Bridge_withseats.nif")
	pBridgeSet.AddObjectToSet(pBridgeObject, "bridge")
	pBridgeObject.SetTranslateXYZ(0.000000, -50.000000, -90.000000)
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
	return (2, 16, 8)

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
	import Bridge.Characters.T11Felix
	import Bridge.Characters.T11Kiska
	import Bridge.Characters.T11Miguel
	import Bridge.Characters.T11Brex
	import Bridge.Characters.T11Saffi

	pFelix  = App.CharacterClass_Cast(pBridgeSet.GetObject("Tactical"))
	pKiska  = App.CharacterClass_Cast(pBridgeSet.GetObject("Helm"))
	pSaffi  = App.CharacterClass_Cast(pBridgeSet.GetObject("XO"))
	pMiguel = App.CharacterClass_Cast(pBridgeSet.GetObject("Science"))
	pBrex   = App.CharacterClass_Cast(pBridgeSet.GetObject("Engineer"))
	
	Bridge.Characters.T11Felix.ConfigureForType11(pFelix)
	Bridge.Characters.T11Kiska.ConfigureForType11(pKiska)
	Bridge.Characters.T11Miguel.ConfigureForType11(pMiguel)
	Bridge.Characters.T11Brex.ConfigureForType11(pBrex)
	Bridge.Characters.T11Saffi.ConfigureForType11(pSaffi)

	pCamera = App.ZoomCameraObjectClass_GetObject(pBridgeSet, "maincamera")
	pCamera.SetTranslateXYZ(2, 16, 8)


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
	kAM.LoadAnimation ("data/animations/T11_stand_s_s.nif", "T11_stand_s_s")
	kAM.LoadAnimation ("data/animations/T11_seated_s_s.nif", "T11_seated_s_s")
	kAM.LoadAnimation ("data/animations/T11_face_capt_s.nif", "T11_face_capt_s")
	kAM.LoadAnimation ("data/animations/T11_chair_s_face_capt.nif", "T11_chair_s_face_capt")
	kAM.LoadAnimation ("data/animations/T11_face_capt_s_reverse.nif", "T11_face_capt_s_reverse")
	kAM.LoadAnimation ("data/animations/T11_chair_s_face_capt_reverse.nif", "T11_chair_s_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/T11B_chair_S_in.nif", "T11B_chair_S_in")

	# Science Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/T11B_S_pushing_buttons_seated_A.NIF", "T11B_S_pushing_buttons_seated_A")
	kAM.LoadAnimation ("data/animations/T11B_S_pushing_buttons_seated_B.NIF", "T11B_S_pushing_buttons_seated_B")
	kAM.LoadAnimation ("data/animations/T11B_S_pushing_buttons_seated_C.NIF", "T11B_S_pushing_buttons_seated_C")

	# Science Talking to other stations

	# 
	# medium animations
	# Helm Movement
	kAM.LoadAnimation ("data/animations/T11_stand_h_m.nif", "T11_stand_h_m")
	kAM.LoadAnimation ("data/animations/T11_seated_h_m.nif", "T11_seated_h_m")
	kAM.LoadAnimation ("data/animations/T11_face_capt_h.nif", "T11_face_capt_h")
	kAM.LoadAnimation ("data/animations/T11_chair_H_face_capt.nif", "T11_chair_H_face_capt")
	kAM.LoadAnimation ("data/animations/T11_face_capt_h_reverse.nif", "T11_face_capt_h_reverse")
	kAM.LoadAnimation ("data/animations/T11_chair_H_face_capt_reverse.nif", "T11_chair_H_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/T11B_glance_h_m.nif", "T11_glance_h_m")
	kAM.LoadAnimation ("data/animations/T11BB_glance_h_m_reverse.nif", "T11_glance_h_m_reverse")

	kAM.LoadAnimation ("data/animations/T11B_hit_h.NIF", "T11_hit_h")


	# Helm Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/T11B_H_Console_Slide_A.NIF", "T11B_H_console_slide_A")
	kAM.LoadAnimation ("data/animations/T11B_H_Console_Slide_B.NIF", "T11B_H_console_slide_B")
	kAM.LoadAnimation ("data/animations/T11B_H_Console_Slide_C.NIF", "T11B_H_console_slide_C")
	kAM.LoadAnimation ("data/animations/T11B_H_Console_Slide_D.NIF", "T11B_H_console_slide_D")

	kAM.LoadAnimation ("data/animations/T11B_H_pushing_buttons_A.NIF", "T11B_H_pushing_buttons_A")
	kAM.LoadAnimation ("data/animations/T11B_H_pushing_buttons_B.NIF", "T11B_H_pushing_buttons_B")
	kAM.LoadAnimation ("data/animations/T11B_H_pushing_buttons_C.NIF", "T11B_H_pushing_buttons_C")
	kAM.LoadAnimation ("data/animations/T11B_H_pushing_buttons_D.NIF", "T11B_H_pushing_buttons_D")
	kAM.LoadAnimation ("data/animations/T11B_H_pushing_buttons_E.NIF", "T11B_H_pushing_buttons_E")
	kAM.LoadAnimation ("data/animations/T11B_H_pushing_buttons_F.NIF", "T11B_H_pushing_buttons_F")

	# Helm Talking to other stations
	kAM.LoadAnimation ("data/animations/T11B_H_Talk_to_C_M.NIF", "T11B_H_Talk_to_C_M")
	kAM.LoadAnimation ("data/animations/T11B_H_Talk_to_E_M.NIF", "T11B_H_Talk_to_E_M")
	kAM.LoadAnimation ("data/animations/T11B_H_Talk_to_S_M.NIF", "T11B_H_Talk_to_S_M")
	kAM.LoadAnimation ("data/animations/T11B_H_Talk_to_T_M.NIF", "T11B_H_Talk_to_T_M")
	kAM.LoadAnimation ("data/animations/T11B_H_Talk_fin_C_M.NIF", "T11B_H_Talk_fin_C_M")
	kAM.LoadAnimation ("data/animations/T11B_H_Talk_fin_E_M.NIF", "T11B_H_Talk_fin_E_M")
	kAM.LoadAnimation ("data/animations/T11B_H_Talk_fin_S_M.NIF", "T11B_H_Talk_fin_S_M")
	kAM.LoadAnimation ("data/animations/T11B_H_Talk_fin_T_M.NIF", "T11B_H_Talk_fin_T_M")

	# Large animations
	# Tactical Movement
	kAM.LoadAnimation ("data/animations/T11_stand_t_l.nif", "T11_stand_t_l")
	kAM.LoadAnimation ("data/animations/T11_seated_t_l.nif", "T11_seated_t_l")
	kAM.LoadAnimation ("data/animations/T11_seatedm_t_l.nif", "T11_seatedm_t_l")
	kAM.LoadAnimation ("data/animations/T11_face_capt_t.nif", "T11_face_capt_t")
	kAM.LoadAnimation ("data/animations/T11_chair_T_face_capt.nif", "T11_chair_T_face_capt")
	kAM.LoadAnimation ("data/animations/T11_face_capt_t_reverse.nif", "T11_face_capt_t_reverse")
	kAM.LoadAnimation ("data/animations/T11_chair_T_face_capt_reverse.nif", "T11_chair_T_face_capt_reverse")
	kAM.LoadAnimation ("data/animations/T11_hit_t.NIF", "T11_hit_t")

	# Tactical Console Slides and Button Pushes
	kAM.LoadAnimation ("data/animations/T11B_T_Console_Slide_A.NIF", "T11B_T_console_slide_A")
	kAM.LoadAnimation ("data/animations/T11B_T_Console_Slide_B.NIF", "T11B_T_console_slide_B")
	kAM.LoadAnimation ("data/animations/T11B_T_Console_Slide_C.NIF", "T11B_T_console_slide_C")
	kAM.LoadAnimation ("data/animations/T11B_T_Console_Slide_D.NIF", "T11B_T_console_slide_D")

	kAM.LoadAnimation ("data/animations/T11B_T_pushing_buttons_A.NIF", "T11B_T_pushing_buttons_A")
	kAM.LoadAnimation ("data/animations/T11B_T_pushing_buttons_B.NIF", "T11B_T_pushing_buttons_B")
	kAM.LoadAnimation ("data/animations/T11B_T_pushing_buttons_C.NIF", "T11B_T_pushing_buttons_C")
	kAM.LoadAnimation ("data/animations/T11B_T_pushing_buttons_D.NIF", "T11B_T_pushing_buttons_D")
	kAM.LoadAnimation ("data/animations/T11B_T_pushing_buttons_E.NIF", "T11B_T_pushing_buttons_E")
	kAM.LoadAnimation ("data/animations/T11B_T_pushing_buttons_F.NIF", "T11B_T_pushing_buttons_F")

	# Tactical Talking to other stations
	kAM.LoadAnimation ("data/animations/T11B_T_Talk_to_H_L.NIF", "T11B_T_Talk_to_H_L")
	kAM.LoadAnimation ("data/animations/T11B_T_Talk_to_G2_L.NIF", "T11B_T_Talk_to_G2_L")
	kAM.LoadAnimation ("data/animations/T11B_T_Talk_to_G3_L.NIF", "T11B_T_Talk_to_G3_L")

	kAM.LoadAnimation ("data/animations/T11B_T_Talk_fin_H_L.NIF", "T11B_T_Talk_fin_H_L")
	kAM.LoadAnimation ("data/animations/T11B_T_Talk_fin_G2_L.NIF", "T11B_T_Talk_fin_G2_L")
	kAM.LoadAnimation ("data/animations/T11B_T_Talk_fin_G3_L.NIF", "T11B_T_Talk_fin_G3_L")

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
	kAM.FreeAnimation("T11_stand_s_s")
	kAM.FreeAnimation("T11_seated_s_s")
	kAM.FreeAnimation("T11_face_capt_s")
	kAM.FreeAnimation("T11_chair_s_face_capt")
	kAM.FreeAnimation("T11_face_capt_s_reverse")
	kAM.FreeAnimation("T11_chair_s_face_capt_reverse")
	kAM.FreeAnimation("T11B_chair_S_in")

	# Science Console Slides and Button Pushes
	kAM.FreeAnimation("T11B_S_pushing_buttons_seated_A")
	kAM.FreeAnimation("T11B_S_pushing_buttons_seated_B")
	kAM.FreeAnimation("T11B_S_pushing_buttons_seated_C")

	# Science Talking to other stations

	# medium animations
	# Helm Movement
	kAM.FreeAnimation("T11_stand_h_m")
	kAM.FreeAnimation("T11_seated_h_m")
	kAM.FreeAnimation("T11_face_capt_h")
	kAM.FreeAnimation("T11_face_capt_h_reverse")
	kAM.FreeAnimation("T11_hit_h")


	# Helm Console Slides and Button Pushes
	kAM.FreeAnimation("T11B_H_console_slide_A")
	kAM.FreeAnimation("T11B_H_console_slide_B")
	kAM.FreeAnimation("T11B_H_console_slide_C")
	kAM.FreeAnimation("T11B_H_console_slide_D")

	kAM.FreeAnimation("T11B_H_pushing_buttons_A")
	kAM.FreeAnimation("T11B_H_pushing_buttons_B")
	kAM.FreeAnimation("T11B_H_pushing_buttons_C")
	kAM.FreeAnimation("T11B_H_pushing_buttons_D")
	kAM.FreeAnimation("T11B_H_pushing_buttons_E")
	kAM.FreeAnimation("T11B_H_pushing_buttons_F")

	# Helm Talking to other stations
	kAM.FreeAnimation("T11B_H_Talk_to_C_M")
	kAM.FreeAnimation("T11B_H_Talk_to_E_M")
	kAM.FreeAnimation("T11B_H_Talk_to_S_M")
	kAM.FreeAnimation("T11B_H_Talk_to_T_M")
	kAM.FreeAnimation("T11B_H_Talk_fin_C_M")
	kAM.FreeAnimation("T11B_H_Talk_fin_E_M")
	kAM.FreeAnimation("T11B_H_Talk_fin_S_M")
	kAM.FreeAnimation("T11B_H_Talk_fin_T_M")
	
	# Large animations
	# Tactical Movement
	kAM.FreeAnimation("T11_stand_t_l")
	kAM.FreeAnimation("T11_seated_t_l")
	kAM.FreeAnimation("T11_seatedm_t_l")
	kAM.FreeAnimation("T11_face_capt_t")
	kAM.FreeAnimation("T11_chair_T_face_capt")
	kAM.FreeAnimation("T11_face_capt_t_reverse")
	kAM.FreeAnimation("T11_chair_T_face_capt_reverse")
	kAM.FreeAnimation("T11_hit_t")

	# Tactical Console Slides and Button Pushes
	kAM.FreeAnimation("T11B_T_console_slide_A")
	kAM.FreeAnimation("T11B_T_console_slide_B")
	kAM.FreeAnimation("T11B_T_console_slide_C")
	kAM.FreeAnimation("T11B_T_console_slide_D")

	kAM.FreeAnimation("T11B_T_pushing_buttons_A")
	kAM.FreeAnimation("T11B_T_pushing_buttons_B")
	kAM.FreeAnimation("T11B_T_pushing_buttons_C")
	kAM.FreeAnimation("T11B_T_pushing_buttons_D")
	kAM.FreeAnimation("T11B_T_pushing_buttons_E")
	kAM.FreeAnimation("T11B_T_pushing_buttons_F")

	# Tactical Talking to other stations
	kAM.FreeAnimation("T11B_T_Talk_to_H_L")
	kAM.FreeAnimation("T11B_T_Talk_to_G2_L")
	kAM.FreeAnimation("T11B_T_Talk_to_G3_L")

	kAM.FreeAnimation("T11B_T_Talk_fin_H_L")
	kAM.FreeAnimation("T11B_T_Talk_fin_G2_L")
	kAM.FreeAnimation("T11B_T_Talk_fin_G3_L")


	return

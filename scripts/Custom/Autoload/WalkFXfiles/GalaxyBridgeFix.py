# Well I think wowbagger or l_j did this, who ever it was it's great but redistributing galaxybridge.py isn't really useful
# as I don't think overriding stock files is really neccessary. So what am I doing here? I'm just trying to stabilize WFX and fixes 
# for future new bridges with similar problems

import App

def GalBridgeFix(pBridgeSet):
    
    	iDetail = App.g_kImageManager.GetImageDetail()
	pcDetail = [ "Low/", "Medium/", "High/" ]
	pcEnvPath = "data/Models/Sets/DBridge/" + pcDetail[iDetail]

	# Pre-load the Bridge model and viewscreen model with our env path
	App.g_kModelManager.LoadModel("data/Models/Sets/DBridge/DBridge.nif", None, pcEnvPath)
	App.g_kModelManager.LoadModel("data/Models/Sets/DBridge/DBridgeViewScreen.nif", None, pcEnvPath)

	# Load the viewscreen and set it up specially with SetViewScreen()
	pViewScreen = App.ViewScreenObject_Create("data/Models/Sets/DBridge/DBridgeViewScreen.nif")
	pBridgeSet.SetViewScreen(pViewScreen, "viewscreen")

	# Setup bridge object
	pBridgeObject = App.BridgeObjectClass_Create("data/Models/Sets/DBridge/DBridge.nif")
	pBridgeSet.AddObjectToSet(pBridgeObject, "bridge")
	pBridgeObject.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	pBridgeObject.SetAngleAxisRotation(0.000000, 1.000000, 0.000000, 0.000000)

	# setup hardpoints for dbridge.
	pPropertySet = pBridgeObject.GetPropertySet()
	from Bridge import DBridgeProperties
	App.g_kModelPropertyManager.ClearLocalTemplates()
	reload(DBridgeProperties)
	DBridgeProperties.LoadPropertySet(pPropertySet)

	# Create camera
	lPos = GetBaseCameraPosition()
	pCamera = App.ZoomCameraObjectClass_Create(lPos[0], lPos[1], lPos[2], 1.570796, -0.000665, -0.087559, 0.996159, "maincamera")
	pCamera.SetMinZoom(0.64)
	pCamera.SetMaxZoom(1.0)
	pCamera.SetZoomTime(0.375)
	pBridgeSet.AddCameraToSet(pCamera, "maincamera")

	# Put the GalaxyBridgeCaptain mode on this camera.
	#pCamera.PushCameraMode( pCamera.GetNamedCameraMode("GalaxyBridgeCaptain") )

	pCamera.Update( App.g_kUtopiaModule.GetGameTime() )
	App.g_kVarManager.SetFloatVariable("global", "fZoomTuneState", 0)

	# Load any Galaxy bridge specific sounds.
	LoadSounds()

def GetBaseCameraPosition():
	return (0.683736, 86.978439, 50.0)
	
	
def LoadSounds():

	pGame = App.Game_GetCurrentGame()
	pGame.LoadSoundInGroup("sfx/door.wav",  "LiftDoor", "BridgeGeneric")

###############################################################################
##	Filename:	CamFX.py
##	
##	A Preview of an upcoming Camera Mod Version 0.1
##	
##	Created:	03/11/2003 - NanoByte a.k.a Michael T. Braams
###############################################################################
import App
import Custom.NanoFXv2.NanoFX_Config

###############################################################################
## "F1" FlyBy Camera Setup
###############################################################################
def NanoFlyByCamera(pCamera):
	
	pMode = App.CameraMode_Create("DropAndWatch", pCamera)

	for pFunc, sAttr, kValue in (
		( pMode.SetAttrFloat,	"AwayDistance",			Custom.NanoFXv2.NanoFX_Config.cFX_AwayDistance ),
		( pMode.SetAttrFloat,	"RotateSpeed",			0.0 ),
		( pMode.SetAttrFloat,	"AnticipationTime",		2.0 ),
		( pMode.SetAttrFloat,	"ForwardOffset",		Custom.NanoFXv2.NanoFX_Config.cFX_ForwardDistance ),
		( pMode.SetAttrFloat,	"SideOffset",			2.5 ),
		( pMode.SetAttrFloat,	"AwayDistanceFactor",		1.1 ),
		( pMode.SetAttrFloat,	"AxisAvoidAngles",		0.5 ),
		( pMode.SetAttrFloat,	"SlowSpeedThreshold",		0.1 ),
		( pMode.SetAttrFloat,	"SlowRotationThreshold",	0.1 ),
		( pMode.SetAttrFloat,	"RotateSpeedAccel",		0.005 ),
		( pMode.SetAttrFloat,	"MaxRotateSpeed",		0.05 ),
		):
		pFunc(sAttr, kValue)

	return pMode

###############################################################################
## ViewScreen Camera Setup
###############################################################################
def NanoViewScreenZoom(pCamera):
		
	pMode = App.CameraMode_Create("ZoomTarget", pCamera)

	for pFunc, sAttr, kValue in (
		( pMode.SetAttrFloat,	"SweepTime",			0.5 ),
		( pMode.SetAttrFloat,	"PositionThreshold",		5.01 ),
		( pMode.SetAttrFloat,	"DotThreshold",			0.98 ),
		( pMode.SetAttrFloat,	"MinimumDistance",		2.0 ),
		( pMode.SetAttrFloat,	"Distance",			Custom.NanoFXv2.NanoFX_Config.cFX_ViewScreenDefault ),
		( pMode.SetAttrFloat,	"MaximumDistance",		Custom.NanoFXv2.NanoFX_Config.cFX_ViewScreenMax ),
		( pMode.SetAttrFloat,	"MaxLagDist",			1.0)
		):
		pFunc(sAttr, kValue)

	return pMode

###############################################################################
## Fixes the warp camera
###############################################################################
def NanoFixWarpCam(pAction, sSetName, sCameraName):
	pSet = App.g_kSetManager.GetSet(sSetName)

	if pSet == None:
		return 0

	pCamera = App.CameraObjectClass_GetObject(pSet, sCameraName)

	if pCamera == None:
		return 0

	# Force an update of the camera that will reposition the camera.
	pMode = pCamera.GetCurrentCameraMode()
	if pMode == None:
		return 0
	
	pMode.SetAttrFloat("AwayDistance", 6.0)
	pMode.SetAttrFloat("ForwardOffset", 3.5)
	pMode.SetAttrFloat("SideOffset", 4.5)
	pMode.SetAttrFloat("AxisAvoidAngles", 2.0)
	pMode.Update()
	pMode.SetAttrFloat("AwayDistance", 100000.0)

	return 0

###############################################################################
## End of Nano CameraFX
###############################################################################

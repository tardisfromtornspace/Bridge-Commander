from bcdebug import debug
import App
import Custom.GalaxyCharts.Cartographer

SET_NAME = "AITravelSet"
def Initialize():
	debug(__name__ + ", Initialize")
	global SET_NAME
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, SET_NAME)

	pSet.SetRegionModule("Custom.GalaxyCharts.TravelerSystems.AITravelSet")

	pSet.SetProximityManagerActive(1)

	LoadPlacements(SET_NAME)
	LoadBackdrops(pSet)

	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	Custom.GalaxyCharts.Cartographer.RegionManager.AddRegion(SET_NAME, "Custom.GalaxyCharts.TravelerSystems.AITravelSet", None, None)

	return pSet

def GetSetName():
	debug(__name__ + ", GetSetName")
	return SET_NAME

def GetSet():
	debug(__name__ + ", GetSet")
	return App.g_kSetManager.GetSet(SET_NAME)

def Terminate():
	debug(__name__ + ", Terminate")
	App.g_kSetManager.DeleteSet(SET_NAME)

def LoadPlacements(sSetName):
	debug(__name__ + ", LoadPlacements")
	vPlayer = (0.0, 0.0, 0.0)
	vLight = (-2000.0, 0.0, 0.0)

	# Light position "Ambient Light"
	kThis = App.LightPlacement_Create("Ambient Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(vLight[0], vLight[1], vLight[2])
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigAmbientLight(1.0, 1.0, 1.0, 0.4)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

	# Position "Player Start"
	kThis = App.Waypoint_Create("Player Start", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(vPlayer[0], vPlayer[1], vPlayer[2])
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.0, 0.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 1.0, 0.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.0)
	kThis.Update(0)
	kThis = None
	# End position "Player Start"


def LoadBackdrops(pSet):
	# Star Sphere "Backdrop stars"
	debug(__name__ + ", LoadBackdrops")
	kThis = App.StarSphere_Create()
	kThis.SetName("Backdrop stars")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.185766, 0.947862, -0.258938)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.049821, 0.254100, 0.965894)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/stars.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(1.000000)
	kThis.SetVerticalSpan(1.000000)
	kThis.SetSphereRadius(35000.000000)
	kThis.SetTextureHTile(22.000000)
	kThis.SetTextureVTile(11.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop stars")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop stars"
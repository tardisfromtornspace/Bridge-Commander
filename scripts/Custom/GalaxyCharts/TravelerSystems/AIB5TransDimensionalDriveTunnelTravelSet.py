# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# GC is ALL Rights Reserved by USS Frontier, but since GC supports Plugins it is fair to release a new TravellingMethod, patch an old one or add new Sytems for the plugin as long as the source files remain unmodified.
# AIB5TransDimensionalDriveTunnelTravelSet.py, file made by Alex SL Gato
# Based on the prototype TravelSet template set by USS Frontier (TravelSet.py, original template) and certain common Systems like Vesuvi (by Totally Games).
# 13th April 2025
# Version 0.1

from bcdebug import debug
import App
import Custom.GalaxyCharts.Cartographer

SET_NAME = "AIB5TransDimensionalDriveTunnelTravelSet"
def Initialize():
	debug(__name__ + ", Initialize")
	global SET_NAME
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, SET_NAME)

	pSet.SetRegionModule("Custom.GalaxyCharts.TravelerSystems.AIB5TransDimensionalDriveTunnelTravelSet")

	pSet.SetProximityManagerActive(1)

	LoadPlacements(SET_NAME)
	LoadBackdrops(pSet)

	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	Custom.GalaxyCharts.Cartographer.RegionManager.AddRegion(SET_NAME, "Custom.GalaxyCharts.TravelerSystems.AIB5TransDimensionalDriveTunnelTravelSet", None, None)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "B5TransDimensionalDriveTunnelTravelSet_S.py" file with an Initialize function that creates them.
	try:
		import B5TransDimensionalDriveTunnelTravelSet_S
		B5TransDimensionalDriveTunnelTravelSet_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

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
	vAmbientLight = (0.0, 0.0, 0.0)
	vLight = (3714.28564453, 3000.0, 0.0)
	vLight2 = (3714.28564453, -3000.0, 0.0)

	# --------------------------------------------- AMBIENT LIGHTNING

	# Light position "Ambient Light"
	kThis = App.LightPlacement_Create("Ambient Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(vAmbientLight[0], vAmbientLight[1], vAmbientLight[2])
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigAmbientLight(1.0, 1.0, 1.0, 0.4)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

	# --------------------------------------------------- DIRECTIONAL LIGHTNING
	
	# Light position "Sun Light"
	kThis = App.LightPlacement_Create("Directional Light 1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(vLight[0], vLight[1], vLight[2])
	kForward = App.TGPoint3()
	kForward.SetXYZ(-1.0, 0.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 1.0, 0.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(1.0, 0.9, 0.9, 0.80)
	kThis.Update(0)
	kThis = None
	# End position "Sun Light"

	# Light position "Sun Light"
	kThis = App.LightPlacement_Create("Directional Light 2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(vLight2[0], vLight2[1], vLight2[2])
	kForward = App.TGPoint3()
	kForward.SetXYZ(-1.0, 0.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 1.0, 0.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(0.9, 0.9, 1.0, 0.80)
	kThis.Update(0)
	kThis = None
	# End position "Sun Light"

	# ----------------------------------------------------- A Few Waypoints...

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
	kThis.SetTextureFileName("data/jumpspaceback.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(1.000000)
	kThis.SetVerticalSpan(1.000000)
	kThis.SetSphereRadius(35000.000000)
	kThis.SetTextureHTile(11.000000)
	kThis.SetTextureVTile(11.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop stars")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop stars"
from bcdebug import debug
import App
import Systems.FoundationUtils

def Initialize():
	# Create the set ("Sol9")
	debug(__name__ + ", Initialize")
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "Sol9")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.Sol.Sol9")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)


	# Load the placements and backdrops for this set.
	LoadPlacements("Sol9")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "Sol9_S.py" file with an Initialize function that creates them.
	try:
		import Sol9_S
		Sol9_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	debug(__name__ + ", GetSetName")
	return "Sol9"

def GetSet():
	debug(__name__ + ", GetSet")
	return App.g_kSetManager.GetSet("Sol9")

def Terminate():
	debug(__name__ + ", Terminate")
	App.g_kSetManager.DeleteSet("Sol9")

def LoadPlacements(sSetName):
	debug(__name__ + ", LoadPlacements")
	placer = Systems.FoundationUtils.SystemPlacer(130.86, 5, 5)

	# Position "Planet1"
	kThis = App.Waypoint_Create("Pluto", sSetName, None)
	kThis.SetStatic(1)
	coord = placer.SetOnOrbit()
	kThis.SetTranslateXYZ(coord[0], coord[1], coord[2])
	kForward = App.TGPoint3()
	coord = placer.SetFacing()
	kForward.SetXYZ(coord[0], coord[1], coord[2])
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Planet1"

	# Position "Planet1" - 19,640 km average average distance
	kThis = App.Waypoint_Create("Charon", sSetName, None)
	kThis.SetStatic(1)
	coord = placer.SetOnOrbit(1122.29)
	kThis.SetTranslateXYZ(coord[0], coord[1], coord[2])
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Planet1"

	placer = None
	coord = None

	# Light position "Ambient Light"
	kThis = App.LightPlacement_Create("Ambient Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigAmbientLight(1.000000, 1.000000, 1.000000, 0.1)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

	# Light position "Directional Light"
	kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-0.044018, 0.572347, 0.029146)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.076971, 0.995795, 0.049676)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.006766, -0.050345, 0.998709)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(1, 1, 1, .9)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"

	# Position "Sun"
	kThis = App.Waypoint_Create("Sun", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(0.0, -268571428.57, -3000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun"

	# Position "Player Start"
	kThis = App.Waypoint_Create("Player Start", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(2000.0, 4000.0, 3000.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Player Start"

	# Position "Starbase1 Location"
	kThis = App.Waypoint_Create("Starbase1 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.0, 20000.0, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Starbase1 Location"

import App

def LoadBackdrops(pSet):

	#Draw order is implicit. First object gets drawn first

	# Star Sphere "Backdrop stars"
	debug(__name__ + ", LoadBackdrops")
	kThis = App.StarSphere_Create()
	kThis.SetName("Backdrop stars")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.185766, 0.947862, -0.258938)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.049825, 0.254099, 0.965894)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/stars.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(1.000000)
	kThis.SetVerticalSpan(1.000000)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(22.000000)
	kThis.SetTextureVTile(11.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop stars")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop stars"

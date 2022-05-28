import App

def Initialize():
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "GalaxyEdge1")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.GalaxyEdge.GalaxyEdge1")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)

	# Load the placements and backdrops for this set.
	LoadPlacements("GalaxyEdge1")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "GalaxyEdge1_S.py" file with an Initialize function that creates them.
	try:
		import GalaxyEdge1_S
		GalaxyEdge1_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "GalaxyEdge"

def GetSet():
	return App.g_kSetManager.GetSet("GalaxyEdge1")

def Terminate():
	App.g_kSetManager.DeleteSet("GalaxyEdge1")

def LoadPlacements(sSetName):

	# Light position "Ambient Light"
	kThis = App.LightPlacement_Create("Ambient Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigAmbientLight(1.000000, 1.000000, 1.000000, 0.05)
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
	kThis.ConfigDirectionalLight(.5, .5, 1, .1)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"

	# Position "Sun"
	kThis = App.Waypoint_Create("Sun", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(4298000.0, -317000.0, 40000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun"

	# Position "Nav Black Star 1"
	kThis = App.Waypoint_Create("Nuetron Star 1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(4295000.0, -314000.0, 37000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Black Star 1"

	# Position "Sun2"
	kThis = App.Waypoint_Create("Sun2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(6298000.0, -917000.0, 43000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun2"

	# Position "Nav Nuetron Star 2"
	kThis = App.Waypoint_Create("Nuetron Star 2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(6295000.0, -914000.0, 37000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Nuetron Star 2"

	# Position "Sun3"
	kThis = App.Waypoint_Create("Sun3", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(938000.0, 214000.0, 3000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun3"

	# Position "Nav Nuetron Star 3"
	kThis = App.Waypoint_Create("Nuetron Star 3", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(935000.0, 211000.0, 2700.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Nuetron Star 3"

	# Position "Sun4"
	kThis = App.Waypoint_Create("Sun4", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-2224000.0, -1900.0, -1500.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun4"

	# Position "Nav Distant Blue Star"
	kThis = App.Waypoint_Create("Distant Blue Star", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-2218000.0, -1400.0, -1100.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Distant Blue Star"

	# Position "Sun5"
	kThis = App.Waypoint_Create("Sun5", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-98500.0, -69000.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun5"

	# Position "Nearby Yellow Star"
	kThis = App.Waypoint_Create("Nearby System", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-89250.0, -67500.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Nearby Yellow Star"

	# Position "Planet"
	kThis = App.Waypoint_Create("Planet1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-8200.00, -8500, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Planet"

	# Position "Planet2"
	kThis = App.Waypoint_Create("Planet2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-2200.00, -500, 25.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Planet2"

	# Position "Sun6"
	kThis = App.Waypoint_Create("Sun6", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-60000.0, -473000.0, -53000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun6"

	# Position "Sun7"
	kThis = App.Waypoint_Create("Sun7", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(72000.0, -22100.0, 77900.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun7"

	# Position "White Dwarf"
	kThis = App.Waypoint_Create("White Dwarf", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(69000.0, -19600.0, 74900.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "White Dwarf"

	# Position "Sun8"
	kThis = App.Waypoint_Create("Sun8", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(20000.0, -40100.0, 99900.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun8"

	# Position "White Star 2"
	kThis = App.Waypoint_Create("White Star 2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(18000.0, -38000.0, 96000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "White Star 2"

	# Position "Player Start"
	kThis = App.Waypoint_Create("Accidental Warp Point, Navigational Error", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(0.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 0.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Player Start"

	# Position "Nav Milky Way"
	kThis = App.Waypoint_Create("Milky Way Galaxy, Alpha Quadrant", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(0.0, -89500000.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Nav Milky Way"

import App

def LoadBackdrops(pSet):

	#Draw order is implicit. First object gets drawn first

	# Star Sphere "Backdrop fewstars"
	kThis = App.StarSphere_Create()
	kThis.SetName("Backdrop fewstars")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.185766, 0.947862, -0.258938)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.049825, 0.254099, 0.965894)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/fewstars.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(1.000000)
	kThis.SetVerticalSpan(1.000000)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(22.000000)
	kThis.SetTextureVTile(11.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop fewstars")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop fewstars"

	# Backdrop Sphere "zmAndromedaCustomGalaxy"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("zmAndromedaCustomGalaxy")
	kThis.SetTranslateXYZ(0, 0, 0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, -9.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 0.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/zmAndromedaCustomGalaxy.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.13)
	kThis.SetVerticalSpan(0.23)
	kThis.SetSphereRadius(300.0)
	kThis.SetTextureHTile(1)
	kThis.SetTextureVTile(1)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"zmAndromedaCustomGalaxy")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "zmAndromedaCustomGalaxy"

	# Backdrop Sphere "largegalcustom1"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("largegalcustom1")
	kThis.SetTranslateXYZ(0, 0, 0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.619916, 0.784394, -0.020738)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.012776, 0.016335, 0.999785)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/Backgrounds/largegalcustom1.tga")
	kThis.SetTargetPolyCount(208)
	kThis.SetHorizontalSpan(0.034938)
	kThis.SetVerticalSpan(0.060100)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"largegalcustom1")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "largegalcustom1"

	# Backdrop Sphere "treknebulabz4"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebulabz4")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.0, 0.0, 0.5)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.5, 0.00, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/Backgrounds/treknebulabz4.tga")
	kThis.SetTargetPolyCount(208)
	kThis.SetHorizontalSpan(0.02)
	kThis.SetVerticalSpan(0.04)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"treknebulabz4")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "treknebulabz4"
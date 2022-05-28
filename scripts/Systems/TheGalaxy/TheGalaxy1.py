import App

def Initialize():
	# Create the set ("TheGalaxy1")
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "TheGalaxy1")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.TheGalaxy.TheGalaxy1")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)

	# Load the placements and backdrops for this set.
	LoadPlacements("TheGalaxy1")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "TheGalaxy1_S.py" file with an Initialize function that creates them.
	try:
		import TheGalaxy1_S
		TheGalaxy1_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "TheGalaxy1"

def GetSet():
	return App.g_kSetManager.GetSet("TheGalaxy1")

def Terminate():
	App.g_kSetManager.DeleteSet("TheGalaxy1")

def LoadPlacements(sSetName):
	# Light position "Ambient Light"
	kThis = App.LightPlacement_Create("Ambient Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigAmbientLight(0.100000, 0.100000, 0.400000, 0.2)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

	# Light position "Directional Light"
	kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(14.928001, 0.000001, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-1.0, 0.5, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.141766, -0.114260, 0.983284)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(.8, .8, .9, .7)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"

	# Light position "Directional Light3"
	kThis = App.LightPlacement_Create("Directional Light3", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(14.928001, -0.400001, -0.200000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-1.0, 0.5, 0.2)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.5, -0.3, 0.983284)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(.8, .4, .1, .8)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light3"

	# Light position "Directional Light4"
	kThis = App.LightPlacement_Create("Directional Light4", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-1.928001, 0.000001, -1.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, -1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.141766, 0.114260, 0.983284)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(.2, .4, .8, .6)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light4"

	# Position "Star"
	kThis = App.Waypoint_Create("Star", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-3100.0, 15896.0, 2700.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Star"

	# Position "Sunq"
	kThis = App.Waypoint_Create("Sunq", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(23100.0, 25895.0, -42702.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sunq"

	# Position "Sun2"
	kThis = App.Waypoint_Create("Sun2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-31000.0, 15895.0, 12702.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun2"

	# Position "Sun3"
	kThis = App.Waypoint_Create("Sun3", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-3200.0, 10045.0, -10010.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun3"
	
	# Position "Sun4"
	kThis = App.Waypoint_Create("Sun4", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(2900.0, 10010.0, -40035.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun4"
	
	# Position "Sun5"
	kThis = App.Waypoint_Create("Sun5", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(13500.0, 9950.0, 90075.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun5"
	
	# Position "Sun6"
	kThis = App.Waypoint_Create("Sun6", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-10000.0, 12000.0, -10000.0)
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
	kThis.SetTranslateXYZ(30000.0, -10045.0, 9700.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun7"
	
	# Position "Sun8"
	kThis = App.Waypoint_Create("Sun8", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(1000, 10000, 50000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun8"

	# Position "Sun9"
	kThis = App.Waypoint_Create("Sun9", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-3000.0, 60045.0, -4700.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun9"
	
	# Position "Sun10"
	kThis = App.Waypoint_Create("Sun10", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(1000, -60000, -150.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun10"

	# Position "Sun11"
	kThis = App.Waypoint_Create("Sun11", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(40000.0, -100.0, -8700.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun11"

	# Position "Sun12"
	kThis = App.Waypoint_Create("Sun12", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(1000, -60, 42050.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun12"

	# Position "Sun13"
	kThis = App.Waypoint_Create("Sun13", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(81000, 21860, 12050.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun13"

	# Position "Sun14"
	kThis = App.Waypoint_Create("Sun14", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-41000, 59060, -72050.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun14"

	# Position "Sun15"
	kThis = App.Waypoint_Create("Sun15", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(35000, 36000, 42050.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun15"

	# Position "Sun16"
	kThis = App.Waypoint_Create("Sun16", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-75000, -36000, -22050.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun16"

	# Position "Center1"
	kThis = App.Waypoint_Create("Center1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-2500.0, 14500.0, 2120.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 1.0, 0.1)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.1, -1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Center1"
	
	# Position "Center2"
	kThis = App.Waypoint_Create("Center2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-2420.0, 14550.0, 1950.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.6, -0.3, 0.3)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Center2"
	
	# Position "Center3"
	kThis = App.Waypoint_Create("Center3", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-2620.0, 14550.0, 1950.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.1, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.6, 0.1, 0.3)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Center3"
	
	# Position "Inner1"
	kThis = App.Waypoint_Create("Inner1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-2575.0, 14490.000000, 2000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.483651, 0.589455, 0.647012)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.864987, 0.434828, 0.250444)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Inner1"
	
	# Position "Inner2"
	kThis = App.Waypoint_Create("Inner2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-2545.0, 14490.0, 1970.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.483651, 0.589455, 0.647012)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.864987, 0.434828, 0.250444)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Inner2"
	
	# Position "Inner3"
	kThis = App.Waypoint_Create("Inner3", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-2545.0, 14490.0, 2030.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.483651, 0.589455, 0.647012)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.864987, 0.434828, 0.250444)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Inner3"
	
	# Position "Inner4"
	kThis = App.Waypoint_Create("Inner4", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-2480.0, 14490.0, 2000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.483651, 0.589455, 0.647012)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.864987, 0.434828, 0.250444)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Inner4"
	
	# Position "Inner5"
	kThis = App.Waypoint_Create("Inner5", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-2515.0, 14490.0, 2030.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.483651, 0.589455, 0.647012)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.864987, 0.434828, 0.250444)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Inner5"
	
	# Position "Inner6"
	kThis = App.Waypoint_Create("Inner6", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-2515.0, 14490.0, 1970.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.483651, 0.589455, 0.647012)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.864987, 0.434828, 0.250444)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Inner6"
	
import App

def LoadBackdrops(pSet):

	#Draw order is implicit. First object gets drawn first

	# Star Sphere "Backdrop starsbz1"
	kThis = App.StarSphere_Create()
	kThis.SetName("Backdrop starsbz1")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.185766, 0.247862, -0.258937)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.059823, 0.254099, 0.965894)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/starsbz1.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(1.000000)
	kThis.SetVerticalSpan(1.000000)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(7.000000)
	kThis.SetTextureVTile(6.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop starsbz1")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop starsbz1"

	# Backdrop Sphere "Backdrop treknebula"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebula")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-1.0, 0.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/treknebula.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.6)
	kThis.SetVerticalSpan(0.8)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebula")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop treknebula"

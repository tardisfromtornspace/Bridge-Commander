import App

def Initialize():
	# Create the set ("Obstacles1")
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "Obstacles1")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.Obstacles.Obstacles1")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)

	# Load the placements and backdrops for this set.
	LoadPlacements("Obstacles1")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "Obstacles1_S.py" file with an Initialize function that creates them.
	try:
		import Obstacles1_S
		Obstacles1_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "Obstacles1"

def GetSet():
	return App.g_kSetManager.GetSet("Obstacles1")

def Terminate():
	App.g_kSetManager.DeleteSet("Obstacles1")

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

	# Light position "Directional Light2"
	kThis = App.LightPlacement_Create("Directional Light2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(2.928001, 0.000001, 14.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.2, 1.0, 0.2)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.141766,-0.114260, 0.983284)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(.7, .5, .0, .8)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light2"

	# Position "Star"
	kThis = App.Waypoint_Create("Star", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(6100.0, 25896.0, 3700.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Star"
	
	# Position "Planet"
	kThis = App.Waypoint_Create("Planet", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-1800.0, 1296.0, 1000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Planet"
	
	# Position "Moon"
	kThis = App.Waypoint_Create("Moon", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-800.0, 1296.0, 1000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Moon"
	
	# Position "Station"
	kThis = App.Waypoint_Create("Station", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-300.0, -600.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Station"
	
	# Position "Nav 1"
	kThis = App.Waypoint_Create("Nav 1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(1000.0, 2000.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Nav 1"
	
	# Position "Nav 2"
	kThis = App.Waypoint_Create("Nav 2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-3500.0, 1550.0, 2075.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Nav 2"
	
	# Position "Nav 3"
	kThis = App.Waypoint_Create("Nav 3", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-2500.0, 50.0, -1000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Nav 3"
	
	# Position "Nav 4"
	kThis = App.Waypoint_Create("Nav 4", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-500.0, -500.0, -505.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Nav 4"

	# Asteroid Field Position "Asteroid Field 1"
	kThis = App.AsteroidFieldPlacement_Create("Asteroid Field 1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-2500.0, 50.0, -1000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208041, 0.724122, -0.657546)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.439904, 0.531161, 0.724122)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetFieldRadius(700.000000)
	kThis.SetNumTilesPerAxis(3)
	kThis.SetNumAsteroidsPerTile(15)
	kThis.SetAsteroidSizeFactor(3.000000)
	kThis.UpdateNodeOnly()
	kThis.ConfigField()
	kThis.Update(0)
	kThis = None
	# End position "Asteroid Field 1"

import App

def LoadBackdrops(pSet):

	#Draw order is implicit. First object gets drawn first

	# Star Sphere "Backdrop stars"
	kThis = App.StarSphere_Create()
	kThis.SetName("Backdrop stars")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.185766, 0.247862, -0.258937)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.059823, 0.254099, 0.965894)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/stars.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(1.000000)
	kThis.SetVerticalSpan(1.000000)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(30.000000)
	kThis.SetTextureVTile(35.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop stars")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop stars"

	# Backdrop Sphere "Backdrop treknebulabz2"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebulabz2")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.0, 0.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/treknebulabz2.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.08)
	kThis.SetVerticalSpan(0.09)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebulabz2")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop treknebulabz2"

	# Backdrop Sphere "Backdrop treknebulabz10"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebulabz10")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.5, 0.5, -0.5)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.1, 0.1, 0.9)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/treknebulabz10.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.1)
	kThis.SetVerticalSpan(0.12)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebulabz10")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop treknebulabz10"

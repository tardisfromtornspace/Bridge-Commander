import App

def Initialize():
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "Kastra1")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.Kastra.Kastra1")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)

	# Load the placements and backdrops for this set.
	LoadPlacements("Kastra1")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "Kastra1_S.py" file with an Initialize function that creates them.
	try:
		import Kastra1_S
		Kastra1_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "Kastra1"

def GetSet():
	return App.g_kSetManager.GetSet("Kastra1")

def Terminate():
	App.g_kSetManager.DeleteSet("Kastra1")

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
	kThis.ConfigAmbientLight(1.000000, 1.000000, 1.000000, 0.100000)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

	# Light position "Directional Light"
	kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.313284, 0.935567, 0.162996)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.350176, -0.045736, 0.935567)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(0.800000, 0.800000, 1.000000, 0.600000)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"

	# Light position "Directional Light 2"
	kThis = App.LightPlacement_Create("Directional Light 2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-10.264078, 4.454040, -8.641300)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.637224, -0.172051, -0.751228)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.555090, -0.573732, 0.602251)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(0.700000, 0.700000, 0.500000, 0.200000)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light 2"

	# Position "Sun"
	kThis = App.Waypoint_Create("Sun", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(0.0, -45500, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun"

	# Position "Nav Kastra"
	kThis = App.Waypoint_Create("Kastra", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(0.0, -39525.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Nav Kastra"

	# Asteroid Field Position "Inner Asteroid Field"
	kThis = App.AsteroidFieldPlacement_Create("Inner Asteroid Field", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(1000.00, -17250.00, 1268.00)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetFieldRadius(8000.00)
	kThis.SetNumTilesPerAxis(3)
	kThis.SetNumAsteroidsPerTile(25)
	kThis.SetAsteroidSizeFactor(11.000000)
	kThis.UpdateNodeOnly()
	kThis.ConfigField()
	kThis.Update(0)
	kThis = None
	# End position "Inner Asteroid Field"

	# Position "Nav Inner Field"
	kThis = App.Waypoint_Create("Inner Asteroid Field", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(1000.00, -17250.00, 1268.00)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Nav Inner Field"

	# Position "Kastra1"
	kThis = App.Waypoint_Create("Planet Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(500.00, -1100, 200.00)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Kastra1"

	# Position "Kastra 2"
	kThis = App.Waypoint_Create("Planet2 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(250.00, 2250.00, -450.00)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Kastra2"

	# Position "Moon1"
	kThis = App.Waypoint_Create("Moon1 Location", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(16900.00, -5250.00, 6000.00)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.00, 0.00)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.000011, -0.008944, 0.999960)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Moon1"

	# Asteroid Field Position "Asteroid Field"
	kThis = App.AsteroidFieldPlacement_Create("Asteroid Field", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(1000.00, 13500.00, 1268.00)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetFieldRadius(8000.00)
	kThis.SetNumTilesPerAxis(3)
	kThis.SetNumAsteroidsPerTile(40)
	kThis.SetAsteroidSizeFactor(7.000000)
	kThis.UpdateNodeOnly()
	kThis.ConfigField()
	kThis.Update(0)
	kThis = None
	# End position "Asteroid Field"

	# Position "Nav Field"
	kThis = App.Waypoint_Create("Asteroid Field", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(1000.00, 9500.00, 1268.00)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Nav Field"

	# Position "Moon2"
	kThis = App.Waypoint_Create("Moon2 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-750.00, 14850.00, 1075.00)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Moon2"

	# Position "Player Start"
	kThis = App.Waypoint_Create("Player Start", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(0.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Player Start"
import App

def LoadBackdrops(pSet):

	#Draw order is implicit. First object gets drawn first

	# Star Sphere "Backdrop stars"
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
	# End Backdrop Sphere "Backdrop kstars"

	# Backdrop Sphere "Backdrop treknebula4"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebula4")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.607303, 0.125438, 0.784505)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.323697, -0.862711, 0.388524)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/Backgrounds/treknebula4.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.155986)
	kThis.SetVerticalSpan(0.156905)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebula4")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop treknebula4"

	# Backdrop Sphere "Backdrop treknebula"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebula")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.0, 0.0, 0.5)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.5, 0.00, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/treknebula9.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.494477)
	kThis.SetVerticalSpan(0.404660)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebula")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop treknebula"
	
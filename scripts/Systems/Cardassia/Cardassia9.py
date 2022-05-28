# unused System
import App

def Initialize():
	# Create the set ("Cardassia9")
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "Cardassia9")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.Cardassia.Cardassia9")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)


	# Load the placements and backdrops for this set.
	LoadPlacements("Cardassia9")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "Cardassia9_S.py" file with an Initialize function that creates them.
	try:
		import Cardassia9_S
		Cardassia9_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "Cardassia9"

def GetSet():
	return App.g_kSetManager.GetSet("Cardassia9")

def Terminate():
	App.g_kSetManager.DeleteSet("Cardassia9")

def LoadPlacements(sSetName):
	# Light position "Ambient Light"
	kThis = App.LightPlacement_Create("Ambient Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(0.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.0, 0.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigAmbientLight(1.0, 0.7, 0.7, 0.13)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

	# Light position "Directional Light"
	kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(0.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.0, 0.0, 0.01)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(1, 0.75, 0.6, 0.7)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"

	# Position "Sun"
	kThis = App.Waypoint_Create("Sun", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-4857142.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.0)
	kThis.Update(0)
	kThis = None
	# End position "Sun"
	
	# Position "The Sun"
	kThis = App.Waypoint_Create("The Sun", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-4617000.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.0)
	kThis.Update(0)
	kThis = None
	# End position "The Sun"
	
	# Position "Cardassia-1"
	kThis = App.Waypoint_Create("Cardassia-1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
#	kThis.SetTranslateXYZ(0.00, 3000.00, 0.00)
	kThis.SetTranslateXYZ(4000.0, 200.0, -700.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.00, 0.00)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.000011, -0.008944, 0.999960)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Cardassia-1"
	
	# Position "Cardassia-2"
	kThis = App.Waypoint_Create("Cardassia-2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)	
#	kThis.SetTranslateXYZ(0.00, 3000.00, 0.00)
	kThis.SetTranslateXYZ(7000.0, 300.0, 300.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.00, 0.00)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.000011, -0.008944, 0.999960)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Cardassia-2"
	
	# Asteroid Field Position "Asteroid Field"
	kThis = App.AsteroidFieldPlacement_Create("Asteroid Field 1", sSetName, None)
	kThis.SetStatic(1)
#	kThis.SetTranslateXYZ(11000.0, 0.0, 0.0)
	kThis.SetTranslateXYZ(18000.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.0, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetFieldRadius(7000.0)
	kThis.SetNumTilesPerAxis(3)
	kThis.SetNumAsteroidsPerTile(80)
	kThis.SetAsteroidSizeFactor(6.0)
	kThis.UpdateNodeOnly()
	kThis.ConfigField()
	kThis.Update(0)
	kThis = None
	# End position "Asteroid Field"

	# Position "Nav Field"
	kThis = App.Waypoint_Create("Asteroid Field 1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
#	kThis.SetTranslateXYZ(11000.0, 0.0, 0.0)
	kThis.SetTranslateXYZ(18000.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.0, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.0)
	kThis.Update(0)
	kThis = None
	# End position "Nav Field"
	
	# Position "Cardassia-3"
	kThis = App.Waypoint_Create("Cardassia-3", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
#	kThis.SetTranslateXYZ(0.00, 3000.00, 0.00)
	kThis.SetTranslateXYZ(29000.0, 0.0, 3000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.00, 0.00)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.000011, -0.008944, 0.999960)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Cardassia-3"
	
	# Position "Cardassia-4"
	kThis = App.Waypoint_Create("Cardassia-4", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
#	kThis.SetTranslateXYZ(0.00, 5000.00, 0.00)
	kThis.SetTranslateXYZ(32000.0, -3000.0, 3000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.00, 0.00)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.000011, -0.008944, 0.999960)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Cardassia-4"
	
	# Position "Cardassia-5"
	kThis = App.Waypoint_Create("Cardassia-5", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
#	kThis.SetTranslateXYZ(0.00, 5000.00, 0.00)
	kThis.SetTranslateXYZ(35000.0, -3000.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.00, 0.00)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.000011, -0.008944, 0.999960)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Cardassia-5"
	
	# Position "Cardassia-6"
	kThis = App.Waypoint_Create("Cardassia-6", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
#	kThis.SetTranslateXYZ(700.0, 8000.0, 0.0)
	kThis.SetTranslateXYZ(38700.0, -3000.0, -3000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.999996, 0.002645, 0.000035)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.000011, -0.008944, 0.999960)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.0)
	kThis.Update(0)
	kThis = None
	# End position "Cardassia-6"

	# Position "Moon"
	kThis = App.Waypoint_Create("Moon", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
#	kThis.SetTranslateXYZ(-20.0, 3000.0, 150.0)
	kThis.SetTranslateXYZ(37980.0, -1500.0, -1150.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.999996, 0.002645, 0.000035)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.0)
	kThis.Update(0)
	kThis = None
	# End position "Moon"
	
	# Asteroid Field Position "Asteroid Field"
	kThis = App.AsteroidFieldPlacement_Create("Asteroid Field 2", sSetName, None)
	kThis.SetStatic(1)
#	kThis.SetTranslateXYZ(11000.0, 0.0, 0.0)
	kThis.SetTranslateXYZ(49000.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.0, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetFieldRadius(7000.0)
	kThis.SetNumTilesPerAxis(5)
	kThis.SetNumAsteroidsPerTile(100)
	kThis.SetAsteroidSizeFactor(12.0)
	kThis.UpdateNodeOnly()
	kThis.ConfigField()
	kThis.Update(0)
	kThis = None
	# End position "Asteroid Field"

	# Position "Nav Field"
	kThis = App.Waypoint_Create("Asteroid Field 2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
#	kThis.SetTranslateXYZ(11000.0, 0.0, 0.0)
	kThis.SetTranslateXYZ(49000.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.0, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.0)
	kThis.Update(0)
	kThis = None
	# End position "Nav Field"		
	
	# Position "Cardassia-7"
	kThis = App.Waypoint_Create("Cardassia-7", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
#	kThis.SetTranslateXYZ(700.0, 3000.0, 0.0)
	kThis.SetTranslateXYZ(58000.0, 0.0, -3000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.999996, 0.002645, 0.000035)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.05, -0.05, 0.9)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.0)
	kThis.Update(0)
	kThis = None
	# End position "Cardassia-7"
	
	# Position "Cardassia-8"
	kThis = App.Waypoint_Create("Cardassia-8", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
#	kThis.SetTranslateXYZ(-100.00, 20000.00, 0.00)
	kThis.SetTranslateXYZ(68000.00, 0.00, 0.00)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.999996, 0.002645, 0.000035)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.05, -0.05, 0.9)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Cardassia-8"
	
	# Position "Player Start"
	kThis = App.Waypoint_Create("Player Start", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-35000.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.0)
	kThis.Update(0)
	kThis = None
	# End position "Player Start"
	
import App

def LoadBackdrops(pSet):

	#Draw order is implicit. First object gets drawn first

	# Star Sphere "Backdrop stars"
	kThis = App.StarSphere_Create()
	kThis.SetName("Backdrop stars")
	kThis.SetTranslateXYZ(0.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.185766, 0.947862, -0.258937)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.049814, 0.254101, 0.965894)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/stars.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(1.0)
	kThis.SetVerticalSpan(1.0)
	kThis.SetSphereRadius(300.0)
	kThis.SetTextureHTile(22.0)
	kThis.SetTextureVTile(11.0)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop stars")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop stars"

	# Backdrop Sphere "Nebula"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Nebula")
	kThis.SetTranslateXYZ(0.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.860219, -0.122382, 0.495021)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.490086, 0.069723, 0.868881)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/Backgrounds/treknebula.tga")
	kThis.SetTargetPolyCount(512)
	kThis.SetHorizontalSpan(0.07)
	kThis.SetVerticalSpan(0.12)
	kThis.SetSphereRadius(300.0)
	kThis.SetTextureHTile(1.0)
	kThis.SetTextureVTile(1.0)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Nebula")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Nebula"

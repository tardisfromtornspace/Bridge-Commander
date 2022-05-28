import App

def Initialize():
	# Create the set ("DS9FXCardassia1")
	pSet = App.SetClass_Create()

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.DS9FXCardassia.DS9FXCardassia1")

	App.g_kSetManager.AddSet(pSet, "DS9FXCardassia1")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)


	# Load the placements and backdrops for this set.
	LoadPlacements("DS9FXCardassia1")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create ();
	pSet.AddObjectToSet(pGrid, "grid");
	pGrid.SetHidden(1);

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "DS9FXCardassia1_S.py" file with an Initialize function that creates them.
	try:
		import DS9FXCardassia1_S
		DS9FXCardassia1_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass
	# Done.

def GetSetName():
	return "DS9FXCardassia1"

def GetSet():
	return App.g_kSetManager.GetSet("DS9FXCardassia1")

def Terminate():
	App.g_kSetManager.DeleteSet("DS9FXCardassia1")

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
	kThis.ConfigAmbientLight(0.980392, 0.980392, 0.529412, 0.196078)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

	# Light position "Directional Light"
	kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(0.0, -270000.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.0, 0.0, 0.01)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(0.984314, 0.623529, 0.301961, 0.882353)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"

	# Position "Player Start"
	kThis = App.Waypoint_Create("Player Start", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.0)
	kThis.Update(0)
	kThis = None
	# End position "Player Start"
	
	kThis = App.Waypoint_Create("Pos1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(457.0, -7589.0, 1550.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.0)
	kThis.Update(0)
	kThis = None
	
	kThis = App.Waypoint_Create("Pos2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(278.0, -8589.0, -1550.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.0)
	kThis.Update(0)
	kThis = None
	
	kThis = App.Waypoint_Create("Pos3", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-57.0, -1270.0, 670.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.0)
	kThis.Update(0)
	kThis = None
	
	kThis = App.Waypoint_Create("Pos4", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(2500.0, -2589.0, 799.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.0)
	kThis.Update(0)
	kThis = None
	
	kThis = App.Waypoint_Create("Pos5", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(1011.0, -6589.0, -559.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.0)
	kThis.Update(0)
	kThis = None

	# Position "Sun"
	kThis = App.Waypoint_Create("Sun", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-270000.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.0)
	kThis.Update(0)
	kThis = None
	# End position "Sun"

	# Position "SunStr"
	kThis = App.Waypoint_Create("SunStr", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-280000.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.0, 0.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.0)
	kThis.Update(0)
	kThis = None
	# End position "SunStr"

	# Position "Cardassia 1"
	kThis = App.Waypoint_Create("Cardassia 1", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(-90000.00, 10000.00, 500.00)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.00, 0.00)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.000011, -0.008944, 0.999960)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Cardassia 1"

	# Position "Cardassia 2"
	kThis = App.Waypoint_Create("Cardassia 2", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(-75000.00, 4000.00, -500.00)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.00, 0.00)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.000011, -0.008944, 0.999960)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Cardassia 2"

	kThis = App.Waypoint_Create("Cardassia 3", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(-59000.00, -4000.00, -100.00)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.00, 0.00)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.000011, -0.008944, 0.999960)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None

	# Position "Cardassia 4"
	kThis = App.Waypoint_Create("Cardassia 4", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(-37000.00, 1000.00, 250.00)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.00, 0.00)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.000011, -0.008944, 0.999960)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Cardassia 4"

	# Position "Cardassia 5"
	kThis = App.Waypoint_Create("Cardassia 5", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(-20000.00, 12000.00, 750.00)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.00, 0.00)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.000011, -0.008944, 0.999960)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Cardassia 5"

	# Position "Cardassia 6"
	kThis = App.Waypoint_Create("Cardassia 6", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(-7000.00, -2000.00, 0.00)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.00, 0.00)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.000011, -0.008944, 0.999960)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Cardassia 6"

	# Position "Cardassia 7"
	kThis = App.Waypoint_Create("Cardassia 7", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(1200.00, -1500.00, -100.00)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.00, 0.00)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.000011, -0.008944, 0.999960)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Cardassia 7"

	# Position "Cardassia 8"
	kThis = App.Waypoint_Create("Cardassia 8", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(12000.00, 15000.00, 400.00)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.00, 0.00)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.000011, -0.008944, 0.999960)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Cardassia 8"

	# Asteroid Field Position "Asteroid Field"
	kThis = App.AsteroidFieldPlacement_Create("Asteroid Field", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(25000.0, 700.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.0, 0.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.0, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetFieldRadius(7000.0)
	kThis.SetNumTilesPerAxis(3)
	kThis.SetNumAsteroidsPerTile(80)
	kThis.SetAsteroidSizeFactor(10.0)
	kThis.UpdateNodeOnly()
	kThis.ConfigField()
	kThis.Update(0)
	kThis = None
	# End position "Asteroid Field"

	# Position "Nav Field"
	kThis = App.Waypoint_Create("Asteroid Field", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(25000.0, 700.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.0, 0.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.0, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.0)
	kThis.Update(0)
	kThis = None
	# End position "Nav Field"

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
	kThis.SetTextureFileName("data/sovstars.tga")
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

	# Backdrop Sphere "Backdrop Cardassia"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop Cardassia")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.799987, 0.000499, -0.005087)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.005087, -0.000011, 0.699987)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/Cardassia01.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.252500)
	kThis.SetVerticalSpan(0.505000)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop back1")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop Cardassia"
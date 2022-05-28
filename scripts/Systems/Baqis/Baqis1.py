def Initialize():
	# Create the set ("Baqis1")
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "Baqis1")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.Baqis.Baqis1")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)

	# Load the placements and backdrops for this set.
	LoadPlacements("Baqis1")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "Baqis1_S.py" file with an Initialize function that creates them.
	try:
		import Baqis1_S
		Baqis1_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "Baqis"

def GetSet():
	return App.g_kSetManager.GetSet("Baqis1")

def Terminate():
	App.g_kSetManager.DeleteSet("Baqis1")

def LoadPlacements(sSetName):

	# Light position "Directional Light"
	kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.0, 0.0, -1.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0, 0, 1)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, -1.0, 0.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(1.5, .1, .1, .4)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"

	# Light position "Directional Light2"
	kThis = App.LightPlacement_Create("Directional Light2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(2.928001, 0.000001, 14.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(.1, 0, -1.7)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0, 1, 0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(1.4, .4, .1, .9)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light2"

	# Position "Sun1"
	kThis = App.Waypoint_Create("Sun1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(18000.0, 26500.0, 15800.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun1"

	# Position "Sun2"
	kThis = App.Waypoint_Create("Sun2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(42000.0, 11000, 12000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun2"

	# Position "Sun3"
	kThis = App.Waypoint_Create("Sun3", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(10200.0, 9500.0, 12000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun3"

	# Position "Cool Blue"
	kThis = App.Waypoint_Create("Cool Blue", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(16500.0, 26500.0, 15800.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Cool Blue"

	# Position "Baqis Red Giant"
	kThis = App.Waypoint_Create("Baqis Red Giant (closest approach)", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(32000.0, 7000, 7000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Baqis Red Giant"

	# Position "Baqis Red Star"
	kThis = App.Waypoint_Create("Baqis Red Star", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(7200.0, 9500.0, 12000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Baqis Red Star"

	# Asteroid Field Position "Asteroid Field 1"
	kThis = App.AsteroidFieldPlacement_Create("Asteroid Field 1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(797.714355, 977.248474, 1268.854858)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208041, 0.724122, -0.657546)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.439904, 0.531161, 0.724122)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetFieldRadius(1000.000000)
	kThis.SetNumTilesPerAxis(3)
	kThis.SetNumAsteroidsPerTile(15)
	kThis.SetAsteroidSizeFactor(7.000000)
	kThis.UpdateNodeOnly()
	kThis.ConfigField()
	kThis.Update(0)
	kThis = None
	# End position "Asteroid Field 1"

	# Position "Planetary Remains"
	kThis = App.Waypoint_Create("Planetary Remains", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(622.812866, 68.898300, 146.147476)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Planetary Remains"

	# Position "Baqis Nebula Edge"
	kThis = App.Waypoint_Create("Baqis Nebula Edge", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(4725.0, -910.0, -735.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Baqis Nebula Edge"

	# Position "Baqis Nebula Center"
	kThis = App.Waypoint_Create("Baqis Nebula Center", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(9800.0, 945.0, -3600.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Baqis Nebula Center"

	# Position "Vanishing Point"
	kThis = App.Waypoint_Create("Vanishing Point", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-8500.0, -2500.0, -10600.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Vanishing Point"

	# Position "Player Start"
	kThis = App.Waypoint_Create("Player Start", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-1000.320533, -930.761717, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
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
	kForward.SetXYZ(0.185766, 0.947862, -0.258937)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.049823, 0.254099, 0.965894)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/stars.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(1.000000)
	kThis.SetVerticalSpan(1.000000)
	kThis.SetSphereRadius(320.000000)
	kThis.SetTextureHTile(25.000000)
	kThis.SetTextureVTile(15.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop stars")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop stars"
	
	# Backdrop Sphere "RedNebCustom1"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("RedNebCustom1")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.00, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/RedNebCustom1.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.164477)
	kThis.SetVerticalSpan(0.284660)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"RedNebCustom1")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "RedNebCustom1"
	
	# Backdrop Sphere "Backdrop treknebula7"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebula7")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, -1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.00, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/treknebula7.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.264477)
	kThis.SetVerticalSpan(0.384660)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebula7")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop treknebula7"
	
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
	

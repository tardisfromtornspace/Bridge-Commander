import App

def Initialize():
	# Create the set ("Promellian1")
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "Promellian1")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.Promellian.Promellian1")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)

	# Load the placements and backdrops for this set.
	LoadPlacements("Promellian1")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "Promellian1_S.py" file with an Initialize function that creates them.
	try:
		import Promellian1_S
		Promellian1_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "Promellian1"

def GetSet():
	return App.g_kSetManager.GetSet("Promellian1")

def Terminate():
	App.g_kSetManager.DeleteSet("Promellian1")

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
	kThis.ConfigAmbientLight(0.100000, 0.120000, 0.150000, 10.900000)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

	# Light position "Directional Light"
	kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(14.928001, 0.000001, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.965661, 0.159977, -0.204709)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.259590, -0.626138, 0.735231)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(1.000000, 0.600000, 0.600000, 1.00000)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"

	# Light position "Directional Light2"
	kThis = App.LightPlacement_Create("Directional Light2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(2.928001, 0.000001, 14.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.969090, -0.218624, 0.114315)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.141626, 0.113590, -0.983382)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(0.500000, 0.000000, 0.600000, 0.200000)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light2"

	# Position "Sun"
	kThis = App.Waypoint_Create("Sun", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(33000.000000, -85000.000000, 20.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.483651, 0.589455, 0.647012)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.864987, 0.434828, 0.250444)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun"

	# Asteroid Field Position "Asteroid Field 1"
	kThis = App.AsteroidFieldPlacement_Create("Asteroid Field 1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.000000, 15.000000, 20.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208041, 0.724122, -0.657546)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.439904, 0.531161, 0.724122)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetFieldRadius(600.000000)
	kThis.SetNumTilesPerAxis(3)
	kThis.SetNumAsteroidsPerTile(15)
	kThis.SetAsteroidSizeFactor(7.000000)
	kThis.UpdateNodeOnly()
	kThis.ConfigField()
	kThis.Update(0)
	kThis = None
	# End position "Asteroid Field 1"

	# Position "BirdsEye"
	kThis = App.Waypoint_Create("BirdsEye", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-700.000000, 3800.000000, 320.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208769, 0.512881, 0.832688)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "BirdsEye"

	# Position "FallBack"
	kThis = App.Waypoint_Create("FallBack", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(100.000000, 80.000000, -150.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208769, 0.512881, 0.832688)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "FallBack"

	# Position "Transwarp6"
	kThis = App.Waypoint_Create("Transwarp6", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 0.512792, 0.858513)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, -0.858513, 0.512792)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Transwarp6"

	# Position "Inner3"
	kThis = App.Waypoint_Create("Inner3", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(6.000000, 7.000000, 20.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.000000, 0.000000, -1.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(1.000000, 0.000000, -0.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Inner3"

	# Position "Shuttle Location"
	kThis = App.Waypoint_Create("Shuttle Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(10.000000, 10.000000, 8.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(1115.000000)
	kThis.Update(0)
	kThis = None
	# End position "Shuttle Location"

	# Position "SL2"
	kThis = App.Waypoint_Create("SL2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(1.000000, 4.000000, 15.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(1115.000000)
	kThis.Update(0)
	kThis = None
	# End position "SL2"

	# Position "Player Start"
	kThis = App.Waypoint_Create("Player Start", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(3.792000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.326288, 0.900793, -0.286546)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.898685, 0.389602, 0.201435)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Player Start"

import App

def LoadBackdrops(pSet):

	#Draw order is implicit. First object gets drawn first

	# Star Sphere "Backdrop starsbz1"
	kThis = App.StarSphere_Create()
	kThis.SetName("Backdrop starsbz1")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.185766, 0.947862, -0.258938)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.049825, 0.254099, 0.965894)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/starsbz1.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(1.000000)
	kThis.SetVerticalSpan(1.000000)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(22.000000)
	kThis.SetTextureVTile(11.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop starsbz1")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop starsbz1"

	# Backdrop Sphere "Backdrop treknebulabz4"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebulabz4")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.000000, 0.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/treknebulabz4.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.100000)
	kThis.SetVerticalSpan(0.150000)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebulabz4")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop treknebulabz4"

	# Backdrop Sphere "Backdrop treknebula4"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebula4")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.000000, -1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/treknebula4.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.300000)
	kThis.SetVerticalSpan(0.350000)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebula4")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop treknebula4"


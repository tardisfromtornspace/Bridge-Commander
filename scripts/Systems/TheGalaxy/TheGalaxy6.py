import App

def Initialize():
	# Create the set ("TheGalaxy6")
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "TheGalaxy6")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.TheGalaxy.TheGalaxy6")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)

	# Load the placements and backdrops for this set.
	LoadPlacements("TheGalaxy6")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "TheGalaxy6_S.py" file with an Initialize function that creates them.
	try:
		import TheGalaxy6_S
		TheGalaxy6_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "TheGalaxy6"

def GetSet():
	return App.g_kSetManager.GetSet("TheGalaxy6")

def Terminate():
	App.g_kSetManager.DeleteSet("TheGalaxy6")

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
	kThis.ConfigAmbientLight(0.01, 0.01, 0.40, 0.05)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

	# Light position "Directional Light"
	kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(14.928001, 0.000001, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, -1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.141766, -0.114260, 0.983284)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(.7, .7, .9, .2)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"

	# Position "Sun"
	kThis = App.Waypoint_Create("Sun", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-7000.0, 90000.0, -60000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun"

	# Position "Sun 1"
	kThis = App.Waypoint_Create("Sun 1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(40000.0, 30000.0, -4000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun 1"

	# Position "Sun 2"
	kThis = App.Waypoint_Create("Sun 2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-10000.0, 37000.0, -16000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun 2"

	# Position "Sun 3"
	kThis = App.Waypoint_Create("Sun 3", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(9000.0, 20000.0, -30000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun 3"

	# Position "Sun 4"
	kThis = App.Waypoint_Create("Sun 4", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(12000.0, 15000.0, -8000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun 4"

	# Position "Sun 5"
	kThis = App.Waypoint_Create("Sun 5", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-5000.0, 62000.0, -30000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun 5"

	# Position "Sun 6"
	kThis = App.Waypoint_Create("Sun 6", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(25000.0, 9000.0, -17000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun 6"

	# Position "Sun 7"
	kThis = App.Waypoint_Create("Sun 7", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-2000.0, 15000.0, -19000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun 7"

	# Position "Sun 8"
	kThis = App.Waypoint_Create("Sun 8", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-80000.0, 27500.0, 9000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun 8"

	# Position "Sun 9"
	kThis = App.Waypoint_Create("Sun 9", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(4000.0, -15000.0, 19000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun 9"

	# Position "Kaled1"
	kThis = App.Waypoint_Create("Kaled1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(8000.0, 18000.0, -26000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Kaled1"

	# Position "Tiamat1"
	kThis = App.Waypoint_Create("Tiamat1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-72000.0, 27000.0, 7000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Tiamat1"

	# Position "Chimera1"
	kThis = App.Waypoint_Create("Chimera1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-70000.0, 25500.0, 5500.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Chimera1"

	# Position "Borealis1"
	kThis = App.Waypoint_Create("Borealis1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(10000.0, 12000.0, -7000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Borealis1"

	# Position "Entry Point"
	kThis = App.Waypoint_Create("Entry Point", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(0.0, -1.0, -1.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Entry Point"

	# Position "No Return"
	kThis = App.Waypoint_Create("No Return", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(0.0, -50000.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "No Return"

import App

def LoadBackdrops(pSet):

	# Star Sphere "Backdrop starsbz1"
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
	kThis.SetHorizontalSpan(0.500000)
	kThis.SetVerticalSpan(0.500000)
	kThis.SetSphereRadius(900.000000)
	kThis.SetTextureHTile(2.000000)
	kThis.SetTextureVTile(2.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop stars")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop stars"

	# Backdrop Sphere "Backdrop treknebulabz8"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebulabz8")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.5, 0.7, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/treknebulabz8.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.250)
	kThis.SetVerticalSpan(0.12)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebulabz8")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop treknebulabz8"
	
	# Backdrop Sphere "Backdrop treknebulabz8a"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebulabz8a")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.5, 0.7, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/treknebulabz8.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.250)
	kThis.SetVerticalSpan(0.12)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebulabz8a")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop treknebulabz8a"
	
	# Backdrop Sphere "Backdrop treknebulabz8b"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebulabz8b")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0 , 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, -1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/treknebulabz8.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.20)
	kThis.SetVerticalSpan(0.2)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebulabz8b")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop treknebulabz8b"

	# Backdrop Sphere "Backdrop treknebulabz11"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebulabz11")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.5, -0.4)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.5, 0.5)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/treknebulabz11.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.06)
	kThis.SetVerticalSpan(0.06)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebulabz11")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop treknebulabz11"

	# Backdrop Sphere "Backdrop treknebulabz5"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebulabz5")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.0, -1.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 1.0, 0.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/treknebulabz5.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.1)
	kThis.SetVerticalSpan(0.15)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebulabz5")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop treknebulabz5"

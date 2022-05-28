import App

def Initialize():
	# Create the set ("BeyondTheGalaxy1")
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "BeyondTheGalaxy1")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.BeyondTheGalaxy.BeyondTheGalaxy1")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)

	# Load the placements and backdrops for this set.
	LoadPlacements("BeyondTheGalaxy1")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "BeyondTheGalaxy_S.py" file with an Initialize function that creates them.
	try:
		import BeyondTheGalaxy1_S
		BeyondTheGalaxy1_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "BeyondTheGalaxy1"

def GetSet():
	return App.g_kSetManager.GetSet("BeyondTheGalaxy1")

def Terminate():
	App.g_kSetManager.DeleteSet("BeyondTheGalaxy1")

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
	kThis.SetTranslateXYZ(-7000.0, 90000.0, -6000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun"

	# Position "Asteroid1"
	kThis = App.Waypoint_Create("Asteroid", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(2502.0, -10005.0, -3202.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Asteroid1"

	# Position "Nav One"
	kThis = App.Waypoint_Create("Magnetic Anomaly", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(2500.0, -12000.0, -3200.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Nav One"
	
	# Position "Damaged Cardassian"
	kThis = App.Waypoint_Create("Gul Cardass", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(3.0, 65.0, 1000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Damaged Cardassian"	
	
	# Position "Damaged Cardassian2"
	kThis = App.Waypoint_Create("Son of Dukat", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(93.0, 65.0, 300.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Damaged Cardassian2"
	
	# Position "Damaged Cardassian3"
	kThis = App.Waypoint_Create("Son of Damar", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(2502.0, -991.0, -202.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Damaged Cardassian3"	
	
	# Position "Galaxy"
	kThis = App.Waypoint_Create("Galaxy", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(3.0, 65.0, 8.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Galaxy"	

import App

def LoadBackdrops(pSet):

	# Star Sphere "Backdrop starsbz2"
	kThis = App.StarSphere_Create()
	kThis.SetName("Backdrop stars")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.185766, 0.947862, -0.258937)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.049823, 0.254099, 0.965894)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/starsbz2.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(1.000000)
	kThis.SetVerticalSpan(1.000000)
	kThis.SetSphereRadius(900.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop starsbz2")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop starsbz2"

	# Backdrop Sphere "Backdrop treknebulabz4"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebulabz4")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/treknebulabz4.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.05)
	kThis.SetVerticalSpan(0.08)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebulabz4")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop treknebulabz4"

	# Backdrop Sphere "Backdrop treknebulabz5"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebulabz5")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, -1.0, -0.2)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/treknebulabz5.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.05)
	kThis.SetVerticalSpan(0.10)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebulabz5")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop treknebulabz5"

	# Backdrop Sphere "Backdrop treknebulabz7"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebulabz7")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.0, -0.5, 0.2)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/treknebulabz7.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.03)
	kThis.SetVerticalSpan(0.04)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebulabz7")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop treknebulabz7"

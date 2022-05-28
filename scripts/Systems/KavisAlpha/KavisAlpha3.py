import App

def Initialize():
	# Create the set ("KavisAlpha3")
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "KavisAlpha3")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.KavisAlpha.KavisAlpha3")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)

	# Load the placements and backdrops for this set.
	LoadPlacements("KavisAlpha3")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "KavisAlpha3_S.py" file with an Initialize function that creates them.
	try:
		import KavisAlpha3_S
		KavisAlpha3_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "KavisAlpha3"

def GetSet():
	return App.g_kSetManager.GetSet("KavisAlpha3")

def Terminate():
	App.g_kSetManager.DeleteSet("KavisAlpha3")

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
	kThis.ConfigAmbientLight(1.000000, 0.700000, 0.700000, 0.100000)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

	# Light position "Directional Light"
	kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-0.044018, 0.572347, 0.029146)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.076971, 0.995795, 0.049677)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.006759, -0.050345, 0.998709)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(1.000000, 0.700000, 0.500000, 0.7)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"

	# Position "Sun"
	kThis = App.Waypoint_Create("Sun", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.000000, -625000.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun"

	# Position "Sun2"
	kThis = App.Waypoint_Create("Sun2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-17500.000000, -450000.000000, 4000.000000)
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
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(17500.000000, 1700000.000000, -2000.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun3"

	# Position "Kavis Beta"
	kThis = App.Waypoint_Create("Kavis Beta", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(17500.000000, 1550000.000000, -2000.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Kavis Beta"

	# Position "Kavis Nuetron Star - Accreation cloud"
	kThis = App.Waypoint_Create("Kavis Nuetron Star - Accreation cloud", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-43500.000000, -500000.000000, 4000.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Kavis Nuetron Star - Accreation cloud"

	# Position "Kavis Alpha - Observation Point"
	kThis = App.Waypoint_Create("Kavis Alpha - Observation Point", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-5500.000000, -378000.000000, 1000.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Kavis Alpha - Observation Point"

	# Position "Planet Location"
	kThis = App.Waypoint_Create("Planet Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(280.000000, -3750.000000, 2000.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Planet Location"

	# Position "Player Start"
	kThis = App.Waypoint_Create("Player Start", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
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
	kThis.SetSphereRadius(320.000000)
	kThis.SetTextureHTile(2.000000)
	kThis.SetTextureVTile(2.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop stars")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop stars"

	# Backdrop Sphere "Backdrop zmNebcustom3"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop zmNebcustom3")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.302035, -0.953278, 0.005955)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.008883, 0.009061, 0.999920)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/Backgrounds/High/zmNebcustom3.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.164025)
	kThis.SetVerticalSpan(0.328050)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop zmNebcustom3")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop zmNebcustom3"

	# Backdrop Sphere "Backdrop zmNebcustom4"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop zmNebcustom4")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.207927, -0.946019, 0.248624)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.061027, 0.241138, 0.968570)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/Backgrounds/High/zmNebcustom4.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.111451)
	kThis.SetVerticalSpan(0.202638)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop zmNebcustom4")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop zmNebcustom4"

	# Backdrop Sphere "Backdrop treknebula7"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebula7")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.245580, 0.964443, 0.097674)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.119808, -0.130184, 0.984225)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/Backgrounds/High/treknebula7.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.230686)
	kThis.SetVerticalSpan(0.350137)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebula7")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop treknebula7"


def Initialize():
	# Create the set ("Procyon1")
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "Procyon1")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.Procyon.Procyon1")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)

	# Load the placements and backdrops for this set.
	LoadPlacements("Procyon1")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "Beol1_S.py" file with an Initialize function that creates them.
	try:
		import Procyon1_S
		Procyon1_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "Procyon1"

def GetSet():
	return App.g_kSetManager.GetSet("Procyon1")

def Terminate():
	App.g_kSetManager.DeleteSet("Procyon1")

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
	kThis.ConfigAmbientLight(0.100000, 0.100000, 0.100000, 0.2)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

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

	# Position "Sun"
	kThis = App.Waypoint_Create("Sun", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(8000.0, 9500.0, 12000.0)
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
	kThis.SetTranslateXYZ(8650.0, 11000, 12000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun2"

	# Position "Procyon Binary"
	kThis = App.Waypoint_Create("Procyon Binary", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(6000.0, 8500.0, 10000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Procyon Binary"

	# Position "Player Start"
	kThis = App.Waypoint_Create("Player Start", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.00, 0.00, 1000.00)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.020647, -0.480066, -0.876990)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.037678, -0.876180, 0.480509)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Player Start"

	# Position "Planet Location"
	kThis = App.Waypoint_Create("Planet Location", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(0.00, 1000.00, 0.00)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.00, 0.00)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.000011, -0.008944, 0.999960)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Planet Location"

	# Position "Moon1 Location"
	kThis = App.Waypoint_Create("Moon1 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-951.521820, 484.500259, -199.616520)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Moon1 Location"

	# Position "Moon2 Location"
	kThis = App.Waypoint_Create("Moon2 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-951.521820, 984.500259, -199.616520)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Moon2 Location"

	# Position "Procyon 1 Nebula Center"
	kThis = App.Waypoint_Create("Procyon 1 Nebula Center", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(9800.0, 4945.0, -3600.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Procyon 1 Nebula Center"

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
	

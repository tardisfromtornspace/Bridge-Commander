import App

def Initialize():
	# Create the set ("SystemJ251")
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "SystemJ251")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.SystemJ25.SystemJ251")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)

	# Load the placements and backdrops for this set.
	LoadPlacements("SystemJ251")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "SystemJ251_S.py" file with an Initialize function that creates them.
	try:
		import SystemJ251_S
		SystemJ251_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "SystemJ251"

def GetSet():
	return App.g_kSetManager.GetSet("SystemJ251")

def Terminate():
	App.g_kSetManager.DeleteSet("SystemJ251")

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
	kThis.ConfigAmbientLight(0.100000, 0.100000, 0.100000, 0.5)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

	# Light position "Directional Light"
	kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.607303, -0.125438, -0.784505)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 0.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(1.5, .1, .1, .6)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"

	# Position "Sun"
	kThis = App.Waypoint_Create("Sun", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(205000.0, -9500.0, 0.0)
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
	kThis.SetTranslateXYZ(-491000.0, 25895.0, 82702.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(20.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun2"

	# Position "Cirtrux"
	kThis = App.Waypoint_Create("Cirtrux", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-475000.0, 23895.0, 82702.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Cirtrux"

	# Position "J25 Red Giant"
	kThis = App.Waypoint_Create("J25 Red Giant", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(160000.0, -9500.0, 0.00)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "J25 Red Giant"

	# Position "Draconis Nebula Center"
	kThis = App.Waypoint_Create("Draconis Nebula Center", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(20800.0, 5500.0, 250.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Draconis Nebula Center"

	# Position "Planet Location"
	kThis = App.Waypoint_Create("Planet Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(135.000450, -1274.912262, -1206.616592)
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
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
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
	# End Backdrop Sphere "Backdrop stars"

	# Backdrop Sphere "RedNebCustom1"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("RedNebCustom1")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 1.0, 0.9)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/RedNebCustom1.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.294477)
	kThis.SetVerticalSpan(0.384660)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"RedNebCustom1")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "RedNebCustom1"

	# Backdrop Sphere "largegalcustom1"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("largegalcustom1")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.619916, 0.784394, -0.020738)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.012776, 0.016335, 0.999785)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/Backgrounds/largegalcustom1.tga")
	kThis.SetTargetPolyCount(208)
	kThis.SetHorizontalSpan(0.054938)
	kThis.SetVerticalSpan(0.080100)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"largegalcustom1")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "largegalcustom1"

	# Backdrop Sphere "orangeclustercustom1"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("orangeclustercustom1")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.607303, 0.125438, 0.784505)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.023697, 0.062711, 0.005524)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/Backgrounds/orangeclustercustom1.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.355986)
	kThis.SetVerticalSpan(0.356905)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"orangeclustercustom1")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "orangeclustercustom1"

import App

def Initialize():
	# Create the set ("DS9FXTrivas1")
	pSet = App.SetClass_Create()

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.DS9FXTrivas.DS9FXTrivas1")

	App.g_kSetManager.AddSet(pSet, "DS9FXTrivas1")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)


	# Load the placements and backdrops for this set.
	LoadPlacements("DS9FXTrivas1")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create ();
	pSet.AddObjectToSet(pGrid, "grid");
	pGrid.SetHidden(1);

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "DS9FXTrivas1_S.py" file with an Initialize function that creates them.
	try:
		import DS9FXTrivas1_S
		DS9FXTrivas1_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass
	# Done.

def GetSetName():
	return "DS9FXTrivas1"

def GetSet():
	return App.g_kSetManager.GetSet("DS9FXTrivas1")

def Terminate():
	App.g_kSetManager.DeleteSet("DS9FXTrivas1")

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
	kThis.ConfigAmbientLight(0.376471, 0.388235, 0.909804, 0.352941)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

	# Light position "Directional Light"
	kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(0.0, -350000.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.0, 0.0, 0.01)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(0.235294, 0.274510, 0.870588, 0.941176)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"

	# Position "Player Start"
	kThis = App.Waypoint_Create("Player Start", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.0, 1.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.0)
	kThis.Update(0)
	kThis = None
	# End position "Player Start"

	# Position "Sun"
	kThis = App.Waypoint_Create("Sun", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(0, -350000.0, 0.0)
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
	kThis.SetTranslateXYZ(0, -360000.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.0, 0.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.0)
	kThis.Update(0)
	kThis = None
	# End position "SunStr"

	# Position "Trivas 1"
	kThis = App.Waypoint_Create("Trivas 1", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(-5000.00, -100000.00, 1250.00)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.00, 0.00)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.000011, -0.008944, 0.999960)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Trivas 1"

	# Position "Trivas 2"
	kThis = App.Waypoint_Create("Trivas 2", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(-8000.00, -75000.00, 500.00)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.00, 0.00)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.000011, -0.008944, 0.999960)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Trivas 2"

	# Position "Trivas 3"
	kThis = App.Waypoint_Create("Trivas 3", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(-4000.00, -47000.00, 5500.00)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.00, 0.00)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.000011, -0.008944, 0.999960)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Trivas 3"

	# Position "Trivas 4"
	kThis = App.Waypoint_Create("Trivas 4", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(2500.00, -17000.00, -250.00)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.00, 0.00)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.000011, -0.008944, 0.999960)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Trivas 4"

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

	# Backdrop Sphere "Backdrop Trivas 1"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop Trivas 1")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.999987, 0.000499, -0.005087)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.005087, -0.000011, 0.999987)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/Trivas01.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.505000)
	kThis.SetVerticalSpan(0.353500)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop back1")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop Trivas 1"

	# Backdrop Sphere "Backdrop Trivas 2"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop Trivas 2")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.999987, 0.000499, -0.005087)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.005087, 0.000011, 0.999987)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/Trivas01.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.353500)
	kThis.SetVerticalSpan(0.505000)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop back2")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop Trivas 2"
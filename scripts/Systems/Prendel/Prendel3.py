import App

def Initialize():
	# Create the set ("Prendel3")
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "Prendel3")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.Prendel.Prendel3")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)


	# Load the placements and backdrops for this set.
	LoadPlacements("Prendel3")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "Prendel3_S.py" file with an Initialize function that creates them.
	try:
		import Prendel3_S
		Prendel3_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "Prendel3"

def GetSet():
	return App.g_kSetManager.GetSet("Prendel3")

def Terminate():
	App.g_kSetManager.DeleteSet("Prendel3")

def LoadPlacements(sSetName):
	# Light position "Ambient Light"
	kThis = App.LightPlacement_Create("Ambient Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigAmbientLight(1.000000, 1.000000, 1.000000, 0.1)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

	# Light position "Directional Light"
	kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.000000, 0.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(1, 1, .8, .45)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"

	# Position "Sun"
	kThis = App.Waypoint_Create("Sun", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-70000.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun"

	# Position "Player Start"
	kThis = App.Waypoint_Create("Player Start", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(0.320533, 30.761717, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Player Start"

	# Position "Planet"
	kThis = App.Waypoint_Create("Planet", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-1000.000000, 1500.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.332255, -0.942401, -0.038562)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.002558, -0.041785, 0.999123)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Planet"

	# Position "Moon1"
	kThis = App.Waypoint_Create("Moon1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(400.000000, 5000.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.332255, -0.942401, -0.038562)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.002558, -0.041785, 0.999123)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Moon1"

	# Position "Moon2"
	kThis = App.Waypoint_Create("Moon2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-5000.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.332255, -0.942401, -0.038562)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.002558, -0.041785, 0.999123)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Moon2"

	# Light position "Light 1"
	kThis = App.LightPlacement_Create("Light 1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-1.063015, 0.000000, 0.597946)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.919261, 0.388660, 0.062470)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.019270, -0.202934, 0.979003)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(1.000000, 0.600000, 0.200000, 0.300000)
	kThis.Update(0)
	kThis = None
	# End position "Light 1"

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

	# Backdrop Sphere "Backdrop treknebula7"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebula7")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.905811, 0.407705, -0.115251)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.105094, 0.047308, 0.993336)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/treknebula7.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.204477)
	kThis.SetVerticalSpan(0.324660)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebula7")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop treknebula7"


import App

def Initialize():
	# Create the set ("Comet1")
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "Comet1")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.Comet.Comet1")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)

	# Load the placements and backdrops for this set.
	LoadPlacements("Comet1")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "Comet1_S.py" file with an Initialize function that creates them.
	try:
		import Comet1_S
		Comet1_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "Comet1"

def GetSet():
	return App.g_kSetManager.GetSet("Comet1")

def Terminate():
	App.g_kSetManager.DeleteSet("Comet1")

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
	kThis.ConfigAmbientLight(0.100000, 0.100000, 0.400000, 0.0)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

	# Light position "Directional Light"
	kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.000000, 0.00000, 0.00000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, -1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(.8, .7, .9, .9)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"

	# Light position "Directional Light2"
	kThis = App.LightPlacement_Create("Directional Light2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.000000, 0.00000, 0.00000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.5, 0.5, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(.6, .6, .8, .8)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light2"

	# Light position "Directional Light3"
	kThis = App.LightPlacement_Create("Directional Light3", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.000000, -1.00000, 0.00000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.0, 0.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(.1, .1, .6, .3)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light3"

	# Position "Sun"
	kThis = App.Waypoint_Create("Sun", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(1500.0, -8000.0, 15000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.000000, 0.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun"

	# Position "Station"
	kThis = App.Waypoint_Create("Station", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(290.0, 1800.0, 290.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Station"

	# Position "CometHead"
	kThis = App.Waypoint_Create("Comet Head", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(320.0, 2500.0, 310.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "CometHead"

	# Position "CometTail"
	kThis = App.Waypoint_Create("Comet Tail", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-250.0, 3300.0, 800.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.1, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "CometTail"

	# Position "Standoff"
	kThis = App.Waypoint_Create("Standoff", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(0.0, 2700.0, 1100.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Standoff"
	
import App

def LoadBackdrops(pSet):

	#Draw order is implicit. First object gets drawn first

	# Star Sphere "Backdrop starsbz1"
	kThis = App.StarSphere_Create()
	kThis.SetName("Backdrop stars")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.185766, 0.947862, -0.258937)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.049823, 0.254099, 0.965894)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/starsbz1.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(1.000000)
	kThis.SetVerticalSpan(1.000000)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(4.000000)
	kThis.SetTextureVTile(5.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop starsbz1")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop starsbz1"
	
	# Backdrop Sphere "Backdrop treknebulabz10"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebulabz10")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.135811, -0.107705, -0.615251)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.105094, 0.047308, 0.993336)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/treknebulabz10.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.1)
	kThis.SetVerticalSpan(0.15)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebulabz10")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop treknebula10"
	
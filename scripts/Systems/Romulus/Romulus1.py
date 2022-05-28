import App

def Initialize():
	# Create the set ("Romulus1")
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "Romulus1")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.Romulus.Romulus1")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)

	# Load the placements and backdrops for this set.
	LoadPlacements("Romulus1")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "Romulus_S.py" file with an Initialize function that creates them.
	try:
		import Romulus1_S
		Romulus1_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "Romulus1"

def GetSet():
	return App.g_kSetManager.GetSet("Romulus1")

def Terminate():
	App.g_kSetManager.DeleteSet("Romulus1")

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
	kThis.ConfigAmbientLight(0.100000, 0.100000, 0.400000, 0.2)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

	# Light position "Directional Light"
	kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.928001, 15.000001, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.5, 0.5, -0.5)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.5, 0.5)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(.9, .7, .6, .7)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"

	# Light position "Directional Light2"
	kThis = App.LightPlacement_Create("Directional Light2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(1.928001, -5.000001, 2.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, -1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.141766, 0.114260, 0.983284)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(.5, .2, .9, .3)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light2"

	# Position "Sun"
	kThis = App.Waypoint_Create("Sun", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(23000.0, -85000, 20.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.483651, 0.589455, 0.647012)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.864987, 0.434828, 0.250444)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun"

	# Position "Earth"
	kThis = App.Waypoint_Create("RomulusL", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-1800.0, 22496.0, 1700.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-1.000000, 0.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Earth"
	
	# Position "MoonL"
	kThis = App.Waypoint_Create("MoonL", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-1200.0, 25896.0, -1700.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "MoonL"

	# Position "Viewpoint"
	kThis = App.Waypoint_Create("BirdsEye", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-700.0, 15800.0, 1320.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "TranswarpHub"
	
	# Position "Rift"
	kThis = App.Waypoint_Create("TheRift", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-9500.0, 1050.0, 4075.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Rift"

	# Position "Romulan6 Location"
	kThis = App.Waypoint_Create("Romulan6 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-215.0, 19250.0, 200.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.002558, -0.041785, 0.999123)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Romulan6 Location"
	
	# Position "Romulan9 Location"
	kThis = App.Waypoint_Create("Romulan9 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(900.000000,  50.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.002558, -0.041785, 0.999123)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Romulan9 Location"
	
	# Position "Romulan8 Location"
	kThis = App.Waypoint_Create("Romulan8 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(100.8,  44.5, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.002558, -0.041785, 0.999123)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Romulan8 Location"
	
	# Position "Romulan10 Location"
	kThis = App.Waypoint_Create("Romulan10 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(222.6,  -111.0, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.002558, -0.041785, 0.999123)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Romulan10 Location"	


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
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(22.000000)
	kThis.SetTextureVTile(11.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop stars")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop stars"
	
	# Backdrop Sphere "Backdrop treknebula4"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebula4")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-1.0, 0.2, 0.1)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/treknebula4.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.25)
	kThis.SetVerticalSpan(0.25)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebula4")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop treknebula4"

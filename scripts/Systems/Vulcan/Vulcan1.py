import App

def Initialize():
	# Create the set ("Vulcan1")
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "Vulcan1")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.Vulcan.Vulcan1")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)

	# Load the placements and backdrops for this set.
	LoadPlacements("Vulcan1")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "Vulcan1_S.py" file with an Initialize function that creates them.
	try:
		import Vulcan1_S
		Vulcan1_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "Vulcan1"

def GetSet():
	return App.g_kSetManager.GetSet("Vulcan1")

def Terminate():
	App.g_kSetManager.DeleteSet("Vulcan1")

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
	kThis.ConfigAmbientLight(0.000000, 0.000000, 0.400000, 0.1)
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
	kThis.ConfigDirectionalLight(1, .5, 0, 1)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"

	# Light position "Directional Light2"
	kThis = App.LightPlacement_Create("Directional Light2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(2.928001, 0.000001, 14.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, -1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.141766, 0.114260, -0.983284)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(.5, .0, .6, .2)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light2"

	# Position "Sun"
	kThis = App.Waypoint_Create("Sun", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(33000.0, -85000, 20.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.483651, 0.589455, 0.647012)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.864987, 0.434828, 0.250444)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun"

	# Position "RomulusL"
	kThis = App.Waypoint_Create("RomulusL", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-1800.0, 10496.0, 1700.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-1.000000, 0.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "RomulusL"

	# Position "Inner6"
	kThis = App.Waypoint_Create("Inner6", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(5101.0, 8896.0, 1201.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Inner6"

	# Position "Inner6a"
	kThis = App.Waypoint_Create("Inner6a", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(5100.0, 8895.0, 1200.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Inner6a"

	# Position "Kali"
	kThis = App.Waypoint_Create("Kali", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-7000.0, 3000.0, 200.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Kali"

	# Position "Viewpoint"
	kThis = App.Waypoint_Create("BirdsEye", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-700.0, 3800.0, 320.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "TranswarpHub"
	
	# Position "FallBack"
	kThis = App.Waypoint_Create("FallBack", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(100.0, 80.0, -150.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "FallBack"

	# Position "Starfleet Command"
	kThis = App.Waypoint_Create("Transwarp2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-2220.0, 9410.0, 2107.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0, 0, 1)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0, -1, 0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Transwarp2"

	# Position "Paris"
	kThis = App.Waypoint_Create("Transwarp6", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-902.0, 10194.0, 2497.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.1, 0.9)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, -0.9, 0.1)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Transwarp6"

	# Position "Tokyo"
	kThis = App.Waypoint_Create("Transwarp8", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-2720.0, 11200.0, 2410.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.0, 1.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 1.0, 0.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Transwarp8"
	
	# Position "Sydney"
	kThis = App.Waypoint_Create("Inner2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-2886.0, 11151.0, 1305.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.0, 1.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-1.0, 0.1, 0.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Inner2"
	
	# Position "Honolulu"
	kThis = App.Waypoint_Create("Inner3", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-3000.0, 10390.0, 1900.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.0, 1.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-1.0, 0.0, 0.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Inner3"
	
	# Position "Shuttle"
	kThis = App.Waypoint_Create("Shuttle Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-700.0, 3100.0, 320.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Shuttle"
	
	# Position "Transport"
	kThis = App.Waypoint_Create("Transport", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-1800.0, 7496.0, 1700.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Transport"	
	
	# Position "FR"
	kThis = App.Waypoint_Create("FR", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-180.0, 7496.0, 1700.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "FR"
	
	# Position "T2"
	kThis = App.Waypoint_Create("Transport2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-180.0, 7496.0, 100.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "T2"	
	
	# Position "T3"
	kThis = App.Waypoint_Create("Transport3", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-10.0, 796.0, 100.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "T3"	
	
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
	kThis.SetTextureHTile(22.000000)
	kThis.SetTextureVTile(11.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop starsbz1")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop stars"
	
	# Backdrop Sphere "Backdrop treknebulabz4"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebulabz4")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.0, 0.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/treknebulabz4.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.10)
	kThis.SetVerticalSpan(0.15)
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
	kForward.SetXYZ(0.0, -1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/treknebula4.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.30)
	kThis.SetVerticalSpan(0.35)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebula4")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop treknebula4"
	
import App

def Initialize():
	# Create the set ("TheGalaxy2")
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "TheGalaxy2")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.TheGalaxy.TheGalaxy2")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)

	# Load the placements and backdrops for this set.
	LoadPlacements("TheGalaxy2")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "TheGalaxy2_S.py" file with an Initialize function that creates them.
	try:
		import TheGalaxy2_S
		TheGalaxy2_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "TheGalaxy2"

def GetSet():
	return App.g_kSetManager.GetSet("TheGalaxy2")

def Terminate():
	App.g_kSetManager.DeleteSet("TheGalaxy2")

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
	kThis.SetTranslateXYZ(2000.0, -265000, 25000.0)
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
	kThis = App.Waypoint_Create("EarthL", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-1800.0, 10496.0, 1700.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-1.000000, 0.000000, -0.100000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, -0.200000, 0.900000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Earth"
	
	# Position "MoonL"
	kThis = App.Waypoint_Create("MoonL", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(200.0, 15896.0, 1700.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "MoonL"

	# Position "Mercury"
	kThis = App.Waypoint_Create("MercuryL", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(12000.0, -175000, 20000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-1.000000, 0.000000, -0.100000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, -0.200000, 0.900000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Mercury"

	# Position "Venus"
	kThis = App.Waypoint_Create("VenusL", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-62000.0, -135000, 10000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-1.000000, 0.000000, -0.100000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, -0.200000, 0.900000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Venus"

	# Position "Mars"
	kThis = App.Waypoint_Create("MarsL", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(47800.0, 85496.0, 700.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-1.000000, 0.000000, -0.100000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, -0.200000, 0.900000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Mars"

	# Position "Jupiter"
	kThis = App.Waypoint_Create("JupiterL", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-162800.0, 160496.0, -4700.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-1.000000, 0.000000, -0.100000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, -0.200000, 0.900000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Jupiter"
	
	# Position "Saturn"
	kThis = App.Waypoint_Create("SaturnL", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(169800.0, 195496.0, -9700.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-1.000000, 0.000000, -0.100000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, -0.200000, 0.900000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Saturn"
	
	# Position "Neptune"
	kThis = App.Waypoint_Create("NeptuneL", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-65800.0, 280496.0, -4700.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-1.000000, 0.000000, -0.100000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, -0.200000, 0.900000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Neptune"
	
	# Position "Uranus"
	kThis = App.Waypoint_Create("UranusL", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(221800.0, 310496.0, -6100.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-1.000000, 0.000000, -0.100000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, -0.200000, 0.900000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Uranus"
	
	# Position "Pluto"
	kThis = App.Waypoint_Create("PlutoL", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-291800.0, 340496.0, -61700.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-1.000000, 0.000000, -0.100000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, -0.200000, 0.900000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Pluto"
	
	# Position "Viewpoint"
	kThis = App.Waypoint_Create("BirdsEye", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-700.0, 6800.0, 1320.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "TranswarpHub"
	
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
	
	# Position "London"
	kThis = App.Waypoint_Create("Transwarp3", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-980.0, 10184.0, 2600.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.1, 0.9)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, -0.9, 0.1)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Transwarp3"
	
	# Position "New York"
	kThis = App.Waypoint_Create("Transwarp4", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-1455.0, 9350.0, 2100.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0, 0, 1)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0, -1, 0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Transwarp4"
	
	# Position "Georgia"
	kThis = App.Waypoint_Create("Georgia", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-1550.0, 9152.0, 1900.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0, 0, 1)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0, -1, 0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Georgia"
	
	# Position "Paris"
	kThis = App.Waypoint_Create("Transwarp6", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-908.0, 10196.0, 2500.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.1, 0.9)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, -0.9, 0.1)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Transwarp6"
	
	# Position "Moscow"
	kThis = App.Waypoint_Create("Transwarp7", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-1400.0, 11180, 2850.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.0, 1.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(1.0, 0.0, 0.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Transwarp7"
	
	# Position "Tokyo"
	kThis = App.Waypoint_Create("Transwarp8", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-2708.0, 11195.0, 2423.0)
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
	kThis.SetTranslateXYZ(-2878.0, 11151.0, 1315.0)
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
	
	# Position "Lake Armstrong"
	kThis = App.Waypoint_Create("Inner5", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(200.0, 15676.0, 1795.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.0, 1.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, -1.0, 0.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Inner5"
	
	# Position "Starbase 1"
	kThis = App.Waypoint_Create("Inner6", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-2215.0, 7250.0, 700.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.0, 1.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, -1.0, 0.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Inner6"
	
	# Position "Shipyard1"
	kThis = App.Waypoint_Create("Ship1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-1515.0, 7500.0, 800.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.0, 1.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, -1.0, 0.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Inner6"
	
	# Position "Shipyard2"
	kThis = App.Waypoint_Create("Ship2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-1500.0, 7602.0, 810.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.0, 1.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, -1.0, 0.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Inner6"
	
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

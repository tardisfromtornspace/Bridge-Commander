import App

def Initialize():
	# Create the set ("Universe1")
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "Universe1")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.Universe.Universe1")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)

	# Load the placements and backdrops for this set.
	LoadPlacements("Universe1")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "Universe1_S.py" file with an Initialize function that creates them.
	try:
		import Universe1_S
		Universe1_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "Universe1"

def GetSet():
	return App.g_kSetManager.GetSet("Universe1")

def Terminate():
	App.g_kSetManager.DeleteSet("Universe1")

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
	kThis.SetTranslateXYZ(14.928001, 0.000001, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-1.0, 0.5, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.141766, -0.114260, 0.983284)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(.8, .8, .9, .7)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"

	# Light position "Directional Light4"
	kThis = App.LightPlacement_Create("Directional Light4", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-1.928001, 0.000001, -1.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, -1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.141766, 0.114260, 0.983284)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(.3, .1, .6, .3)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light4"

	# Position "Star"
	kThis = App.Waypoint_Create("Star", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-49000.0, 95896.0, 40700.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Star"

	# Position "Sunq"
	kThis = App.Waypoint_Create("Sunq", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-47500.0, 94000.0, 39500.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sunq"

	# Position "Sun2"
	kThis = App.Waypoint_Create("Sun2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-61000.0, 25895.0, 82702.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun2"

	# Position "Sun3"
	kThis = App.Waypoint_Create("Sun3", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-60200.0, 2045.0, -90010.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun3"
	
	# Position "Sun4"
	kThis = App.Waypoint_Create("Sun4", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(20900.0, 180010.0, -80035.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun4"
	
	# Position "Sun5"
	kThis = App.Waypoint_Create("Sun5", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(83500.0, 90950.0, 9075.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun5"
	
	# Position "Sun6"
	kThis = App.Waypoint_Create("Sun6", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-70000.0, 22000.0, -100000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun6"
	
	# Position "Sun7"
	kThis = App.Waypoint_Create("Sun7", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(30000.0, -10045.0, 109700.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun7"
	
	# Position "Sun8"
	kThis = App.Waypoint_Create("Sun8", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(60000, 10000, 50000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun8"

	# Position "Sun10"
	kThis = App.Waypoint_Create("Sun10", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(10000, -60000, -150000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun10"

	# Position "Sun11"
	kThis = App.Waypoint_Create("Sun11", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(40000.0, -140000.0, -87000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun11"
	
	# Position "Sun12"
	kThis = App.Waypoint_Create("Sun12", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(10000, -6000, 12050.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun12"
	
	# Position "Sun13"
	kThis = App.Waypoint_Create("Sun13", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-60000.0, 9000.0, -60000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun13"

	# Position "Sun14"
	kThis = App.Waypoint_Create("Sun14", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(45000.0, 1045.0, 700.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun14"

	# Position "Sun15"
	kThis = App.Waypoint_Create("Sun15", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(4000.0, 1045.0, -37000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun15"

	# Position "Sun16"
	kThis = App.Waypoint_Create("Sun16", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(34000.0, -11045.0, -17000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun16"




	# Position "Devron"
	kThis = App.Waypoint_Create("Devron", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(69400.0, 80850.0, 175.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Devron"

	# Position "Wolf359"
	kThis = App.Waypoint_Create("Wolf359", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-30000.0, 10045.0, -47000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Wolf359"

	# Position "Smoke"
	kThis = App.Waypoint_Create("SmokeScreen", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-29400.0, -30900.0, -75000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Smoke"

	# Position "Praxis"
	kThis = App.Waypoint_Create("Praxis", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(24200.0, -6645.0, 59000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Praxis"

	
	
	# Position "Risa"
	kThis = App.Waypoint_Create("Risa1L", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-58000.0, 4045.0, -90910.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Risa"

	# Position "Sol3"
	kThis = App.Waypoint_Create("Sol3L", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(17900.0, 176010.0, -81035.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sol3"

	# Position "Romulus1"
	kThis = App.Waypoint_Create("Romulus1L", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(86000.0, 90050.0, 10575.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Romulus1"

	# Position "Romulus2"
	kThis = App.Waypoint_Create("Romulus2L", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(86500.0, 90050.0, 10575.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Romulus2"
	
	# Position "Kronos"
	kThis = App.Waypoint_Create("KronosL", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(27000.0, -11045.0, 106700.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Kronos"

	# Position "Card"
	kThis = App.Waypoint_Create("CardL", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-72000.0, 22000.0, -100000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Card"

	# Position "DS9"
	kThis = App.Waypoint_Create("DS9", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-58000.0, 12000.0, -56000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "DS9"

	# Position "Bajora"
	kThis = App.Waypoint_Create("Bajora", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-57800.0, 11700.0, -55600.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Bajora"

	# Position "FerengiL"
	kThis = App.Waypoint_Create("FerengiL", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(52000, 6000, 53000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "FerengiL"

	# Position "Vulcan1L"
	kThis = App.Waypoint_Create("Vulcan1L", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(36000.0, -9045.0, -16500.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Vulcan1L"

	# Position "StationL"
	kThis = App.Waypoint_Create("StationL", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(43000.0, -2545.0, 1700.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "StationL"
	
	# Position "Hive"
	kThis = App.Waypoint_Create("Hive", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(9000, -59000, -149000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Hive"

	# Position "wreck1"
	kThis = App.Waypoint_Create("wreck1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-30005.0, 10040.0, -47005.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "wreck1"

	# Position "wreck2"
	kThis = App.Waypoint_Create("wreck2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-30015.0, 10030.0, -47015.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "wreck2"

	# Position "wreck5"
	kThis = App.Waypoint_Create("wreck5", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-30000.0, 10050.0, -47000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "wreck5"

	# Position "wreck10"
	kThis = App.Waypoint_Create("wreck10", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-30050.0, 10030.0, -47025.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "wreck10"

	# Position "wreck13"
	kThis = App.Waypoint_Create("wreck13", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-29995.0, 9990.0, -46960.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "wreck13"
	
	# Position "Wolf359 Rescue Ship"
	kThis = App.Waypoint_Create("RS Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(17900.0, 176010.0, -71035.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Wolf359 Rescue Ship"
	
	# Position "USS Venture"
	kThis = App.Waypoint_Create("Venture Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-58000.0, 14777.0, -56000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Venture"
	
	# Position "Warbird"
	kThis = App.Waypoint_Create("Warbird Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(86250.0, 90050.0, 10575.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Warbird"	
	
	# Position "Vorcha"
	kThis = App.Waypoint_Create("Vorcha Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(2420.9, -6645.0, 59000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Vorcha"	
	
	# Position "Sovereign"
	kThis = App.Waypoint_Create("Sovereign Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(17900.0, 175010.0, -81035.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sovereign"
	
	# Position "Farragut"
	kThis = App.Waypoint_Create("Farragut Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-30000.0, 10030.0, -47000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Farragut
	
	# Asteroid Field Position "Asteroid Field 1"
	kThis = App.AsteroidFieldPlacement_Create("Asteroid Field 1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(25000.0, -7045.0, 59700.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208041, 0.724122, -0.657546)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.439904, 0.531161, 0.724122)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetFieldRadius(1900.000000)
	kThis.SetNumTilesPerAxis(3)
	kThis.SetNumAsteroidsPerTile(35)
	kThis.SetAsteroidSizeFactor(7.000000)
	kThis.UpdateNodeOnly()
	kThis.ConfigField()
	kThis.Update(0)
	kThis = None
	# End position "Asteroid Field 1"

import App

def LoadBackdrops(pSet):

	#Draw order is implicit. First object gets drawn first

	# Star Sphere "Backdrop stars"
	kThis = App.StarSphere_Create()
	kThis.SetName("Backdrop stars")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.185766, 0.247862, -0.258937)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.059823, 0.254099, 0.965894)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/stars.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(1.000000)
	kThis.SetVerticalSpan(1.000000)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(20.000000)
	kThis.SetTextureVTile(25.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop stars")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop stars"

	# Backdrop Sphere "Backdrop treknebulabz2"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebulabz2")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-1.0, 0.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/treknebulabz2.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.3)
	kThis.SetVerticalSpan(0.25)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebulabz2")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop treknebulabz2"

	# Backdrop Sphere "Backdrop treknebulabz5"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebulabz5")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.0, 0.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/treknebulabz5.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.2)
	kThis.SetVerticalSpan(0.2)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebulabz5")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop treknebulabz5"

	# Backdrop Sphere "Backdrop treknebulabz11"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebulabz11")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.2, 0.2, -1.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.1, 1.0, 0.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/treknebulabz11.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.07)
	kThis.SetVerticalSpan(0.06)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebulabz11")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop treknebulabz11"

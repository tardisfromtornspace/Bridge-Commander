import App

def Initialize():
	# Create the set ("String1")
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "String1")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.String.String1")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)

	# Load the placements and backdrops for this set.
	LoadPlacements("String1")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "String1_S.py" file with an Initialize function that creates them.
	try:
		import String1_S
		String1_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "String1"

def GetSet():
	return App.g_kSetManager.GetSet("String1")

def Terminate():
	App.g_kSetManager.DeleteSet("String1")

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
	kThis.ConfigAmbientLight(0.3, 0.0, 0.4, 0.2)
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
	kThis.ConfigDirectionalLight(.8, .5, .1, .6)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light2"

	# Position "Sun"
	kThis = App.Waypoint_Create("Sun", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(250.0, 12650.0, 300.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun"

	# Position "Sunx"
	kThis = App.Waypoint_Create("Sunx", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(240.0, 12665.0, 306.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sunx"

	# Position "Suny"
	kThis = App.Waypoint_Create("Suny", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(230.0, 12670.0, 310.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Suny"

	# Position "Suna"
	kThis = App.Waypoint_Create("Suna", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(220.0, 12675.0, 312.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Suna"

	# Position "Sunax"
	kThis = App.Waypoint_Create("Sunax", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(205.0, 12688.0, 318.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sunax"

	# Position "Sun2"
	kThis = App.Waypoint_Create("Sun2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(190.0, 12700.0, 325.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun2"

	# Position "Sun2x"
	kThis = App.Waypoint_Create("Sun2x", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(175.0, 12709.0, 335.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun2x"

	# Position "Sun2y"
	kThis = App.Waypoint_Create("Sun2y", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(160.0, 12717.0, 345.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun2y"

	# Position "Sun2a"
	kThis = App.Waypoint_Create("Sun2a", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(150.0, 12725.0, 350.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun2a"

	# Position "Sun2ax"
	kThis = App.Waypoint_Create("Sun2ax", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(135.0, 12750.0, 360.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun2ax"

	# Position "Sun3"
	kThis = App.Waypoint_Create("Sun3", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(120.0, 12775.0, 375.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun3"

	# Position "Sun3x"
	kThis = App.Waypoint_Create("Sun3x", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(100.0, 12795.0, 395.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun3x"

	# Position "Sun3a"
	kThis = App.Waypoint_Create("Sun3a", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(80.0, 12825.0, 410.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun3a"
	
	# Position "Sun4"
	kThis = App.Waypoint_Create("Sun4", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(40.0, 12875.0, 450.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun4"
	
	# Position "Sun4a"
	kThis = App.Waypoint_Create("Sun4a", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(0.0, 12950.0, 500.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun4a"
	
	# Position "Sun4ax"
	kThis = App.Waypoint_Create("Sun4ax", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-25.0, 12980.0, 530.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun4ax"
	
	# Position "Sun5"
	kThis = App.Waypoint_Create("Sun5", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-50.0, 13000.0, 550.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun5"
	
	# Position "Sun5x"
	kThis = App.Waypoint_Create("Sun5x", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-60.0, 13030.0, 570.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun5x"
	
	# Position "Sun5y"
	kThis = App.Waypoint_Create("Sun5y", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-80.0, 13050.0, 590.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun5y"
	
	# Position "Sun5a"
	kThis = App.Waypoint_Create("Sun5a", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-100.0, 13075.0, 615.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun5a"
	
	# Position "Sun5ax"
	kThis = App.Waypoint_Create("Sun5ax", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-120.0, 13105.0, 635.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun5ax"
	
	# Position "Sun5ay"
	kThis = App.Waypoint_Create("Sun5ay", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-140.0, 13120.0, 655.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun5ay"
	
	# Position "Sun6"
	kThis = App.Waypoint_Create("Sun6", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-150.0, 13150.0, 675.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun6"
	
	# Position "Sun6x"
	kThis = App.Waypoint_Create("Sun6x", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-155.0, 13175.0, 700.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun6x"

	# Position "Sun6a"
	kThis = App.Waypoint_Create("Sun6a", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-160.0, 13200.0, 725.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun6a"

	# Position "Sun6ax"
	kThis = App.Waypoint_Create("Sun6ax", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-165.0, 13232.0, 750.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun6ax"

	# Position "Sun6b"
	kThis = App.Waypoint_Create("Sun6b", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-170.0, 13266.0, 775.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun6b"

	# Position "Sun6bx"
	kThis = App.Waypoint_Create("Sun6bx", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-173.0, 13290.0, 800.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun6bx"

	# Position "Sun7"
	kThis = App.Waypoint_Create("Sun7", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-177.0, 13325.0, 825.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun7"

	# Position "Sun7x"
	kThis = App.Waypoint_Create("Sun7x", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-185.0, 13350.0, 854.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun7x"

	# Position "Sun7a"
	kThis = App.Waypoint_Create("Sun7a", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-190.0, 13376.0, 875.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun7a"

	# Position "Sun7ax"
	kThis = App.Waypoint_Create("Sun7ax", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-200.0, 13393.0, 890.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun7ax"
	
	# Position "Sun8"
	kThis = App.Waypoint_Create("Sun8", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-210.0, 13400.0, 900.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun8"
	
	# Position "Sun8x"
	kThis = App.Waypoint_Create("Sun8x", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-215.0, 13430.0, 925.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun8x"
	
	# Position "Sun8a"
	kThis = App.Waypoint_Create("Sun8a", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-230.0, 13460.0, 950.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun8a"

	# Position "Sun9"
	kThis = App.Waypoint_Create("Sun9", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-235.0, 13525.0, 1000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun9"
	
	# Position "Sun10"
	kThis = App.Waypoint_Create("Sun10", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-245.0, 13575.0, 1065.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun10"
	
	# Position "Sun10x"
	kThis = App.Waypoint_Create("Sun10x", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-255.0, 13600.0, 1100.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun10x"

	# Position "Sun11"
	kThis = App.Waypoint_Create("Sun11", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-260.0, 13625.0, 1130.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun11"

	# Position "Sun11x"
	kThis = App.Waypoint_Create("Sun11x", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-262.0, 13675.0, 1170.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun11x"
	
	# Position "Sun12"
	kThis = App.Waypoint_Create("Sun12", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-270.0, 13750.0, 1200.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun12"
	
	# Position "Sun12x"
	kThis = App.Waypoint_Create("Sun12x", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-280.0, 13800.0, 1235.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun12x"

	# Position "Sun13"
	kThis = App.Waypoint_Create("Sun13", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-285.0, 13875.0, 1270.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun13"

	# Position "Sun13x"
	kThis = App.Waypoint_Create("Sun13x", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-295.0, 13900.0, 1285.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun13x"

	# Position "Sun13y"
	kThis = App.Waypoint_Create("Sun13y", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-305.0, 13915.0, 1295.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun13y"

	# Position "Station"
	kThis = App.Waypoint_Create("Station", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(290.0, 12500.0, 290.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Station"

	# Position "Station2"
	kThis = App.Waypoint_Create("Station2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-620.0, 13960.0, 1350.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Station2"

	# Position "StringHead"
	kThis = App.Waypoint_Create("String Head", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(300.0, 12600.0, 250.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "StringHead"

	# Position "StringTail"
	kThis = App.Waypoint_Create("String Tail", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-450.0, 13950.0, 1310.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.1, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "StringTail"

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
	kThis.SetTextureHTile(2.000000)
	kThis.SetTextureVTile(4.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop stars")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop stars"

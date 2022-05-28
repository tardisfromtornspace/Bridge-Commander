import App

def Initialize():
	# Create the set ("CJones5")
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "CJones5")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.CJones.CJones5")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)


	# Load the placements and backdrops for this set.
	LoadPlacements("CJones5")
	
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "CJones5_S.py" file with an Initialize function that creates them.
	try:
		import CJones5_S
		CJones5_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "CJones5"

def GetSet():
	return App.g_kSetManager.GetSet("CJones5")

def Terminate():
	App.g_kSetManager.DeleteSet("CJones5")

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
	kThis = App.Waypoint_Create("Kelios", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(3900.0, 45000.0, 1000.0)
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
	kThis = App.Waypoint_Create("Unknown Dwarf", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(25500.827942, 27000.803833, 1000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun2"
	
	# Position "Red Dwarf"
	kThis = App.Waypoint_Create("Near Red Dwarf", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(25500.827942, 25800.803833, 1000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Red Dwarf"
	
	# Position "Player Start"
	kThis = App.Waypoint_Create("Player Start", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.417716, 0.620277, 0.663905)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.898685, 0.389602, 0.201435)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(30.000000)
	kThis.Update(0)
	kThis = None
	# End position "Player Start"
	
	# Position "Asteroid Field"
	kThis = App.Waypoint_Create("Asteroid Field", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(900.0, 900.0, 900.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Asteroid Field"	

	# Position "Kelios"
	kThis = App.Waypoint_Create("Kelios 1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(15024.827942, 888.803833, 975.455322)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.483651, 0.589455, 0.647012)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.864987, 0.434828, 0.250444)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Kelios"	

	# Position "Kelios 2 Location"
	kThis = App.Waypoint_Create("Kelios 2 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(57700, 2000, 175.455322)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.483651, 0.589455, 0.647012)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.864987, 0.434828, 0.250444)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Kelios 2 Location"	
	
	# Position "Kelios 3 Location"
	kThis = App.Waypoint_Create("Kelios 3 Location", sSetName, None)
        kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(2400, -77000.5, 175.459322)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.483651, 0.589455, 0.647012)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.864987, 0.434828, 0.250444)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Kelios 3 Location"
	
	# Position "Kelios 4 Location"
	kThis = App.Waypoint_Create("Kelios 4 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(15000, 11000, 1000.455322)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.483651, 0.589455, 0.647012)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.864987, 0.434828, 0.250444)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Kelios 4 Location"	

	# Position "Red Giant Planet"
	kThis = App.Waypoint_Create("Kelios 5 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(9000.0, 7000.0, -21000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.483651, 0.589455, 0.647012)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.864987, 0.434828, 0.250444)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Red Giant Planet"	

	# Position "Warp Point"
	kThis = App.Waypoint_Create("Warp Point", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-1000.0, 12000.0, 1.2)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Warp Point"	
	
	# Position "Shuttledam"
	kThis = App.Waypoint_Create("Shuttledam Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(810.0, 900.0, 850.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Shuttledam"
	
	# Position "Back Home"
	kThis = App.Waypoint_Create("Kelios Home", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-10.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Back Home"
	
	# Position "Transport"
	kThis = App.Waypoint_Create("Transport Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(0.0, 100.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Transport"
	
	# Position "Akira"
	kThis = App.Waypoint_Create("Akira", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(0.0, 100.0, -970.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Akira"	
	
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
	
	# Backdrop Sphere "Backdrop"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebulabz4")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.0, 0.0, 0.0)
	kUp = App.TGPoint3()
	# This "kForward" and "kUp" will set where the nebula appears on the background sphere.
	kUp.SetXYZ(-20000.0, 0.0, 100.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/galaxy5.tga")
	kThis.SetTargetPolyCount(256)
	# The Horizontal and Vertical Span is how big the nebula will be. 1.0 will fill the entire sky! 
	kThis.SetHorizontalSpan(0.2)
	kThis.SetVerticalSpan(0.2)
	kThis.SetSphereRadius(29.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebula")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop"
	


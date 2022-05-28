import App

def Initialize():
	# Create the set ("CJones4")
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "CJones4")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.CJones.CJones4")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)


	# Load the placements and backdrops for this set.
	LoadPlacements("CJones4")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "CJones4_S.py" file with an Initialize function that creates them.
	try:
		import CJones4_S
		CJones4_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "CJones4"

def GetSet():
	return App.g_kSetManager.GetSet("CJones4")

def Terminate():
	App.g_kSetManager.DeleteSet("CJones4")

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
	kThis.SetTranslateXYZ(-0.044018, 0.572347, 0.029146)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.076971, 0.995795, 0.049676)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.006766, -0.050345, 0.998709)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(1, 1, 1, .9)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"
	
	# Position "Player Start"
	kThis = App.Waypoint_Create("Player Start", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0, 0, 0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.417716, 0.620277, 0.663905)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.898685, 0.389602, 0.201435)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Player Start"
	
	# Position "Sun"
	kThis = App.Waypoint_Create("Barnard's Star", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(0.0, -15000.0, 500.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun"	
	
	# Position "Spot"
	kThis = App.Waypoint_Create("Barnard's Spot", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(201.0, -15000.0, 500.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Spot"
	
	# Position "PC"
	kThis = App.Waypoint_Create("Proxima Centauri", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-90000.0, 98000.0, 100.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "PC"
	
	# Position "RK"
	kThis = App.Waypoint_Create("Rigil Kentaurus", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-70000.0, 18000.0, 100.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "RK"
	
	# Position "ACB"
	kThis = App.Waypoint_Create("Alpha Centauri B", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-89000.0, 18000.0, 100.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "ACB"
	
	# Position "Distant Stars"
	kThis = App.Waypoint_Create("Near Proxima Centauri", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-90000.0, 97100.0, 100.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Distant Stars"	
	
	# Position "Distant Stars"
	kThis = App.Waypoint_Create("Near Rigil Kentaraus aka Alpha Centauri A", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-70000.0, 16900.0, 100.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Distant Stars"	
	
	# Position "Distant Stars"
	kThis = App.Waypoint_Create("Near Alpha Centauri B", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-89000.0, 16900.0, 100.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Distant Stars"	
	
	# Position "Back Home"
	kThis = App.Waypoint_Create("Barnard's Star Home", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(0.0, -14200.0, 500.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Back Home"
	
	# Position "Solar Data"
	kThis = App.Waypoint_Create("SD", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(90.8, 90.8, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Solar Data"

	## Position "Galor"
	kThis = App.Waypoint_Create("Galorize locale", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(90.8, 90.8, -100.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Solar Data"
	
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
	kThis.SetTextureFileName("data/backgrounds/treknebula6.tga")
	kThis.SetTargetPolyCount(256)
	# The Horizontal and Vertical Span is how big the nebula will be. 1.0 will fill the entire sky! 
	kThis.SetHorizontalSpan(0.6)
	kThis.SetVerticalSpan(0.2)
	kThis.SetSphereRadius(29.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebula")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop"	

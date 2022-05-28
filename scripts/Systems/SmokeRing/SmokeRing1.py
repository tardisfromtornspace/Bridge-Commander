import App

def Initialize():
	# Create the set ("SmokeRing1")
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "SmokeRing1")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.SmokeRing.SmokeRing1")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)

	# Load the placements and backdrops for this set.
	LoadPlacements("SmokeRing1")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "SmokeRing1_S.py" file with an Initialize function that creates them.
	try:
		import SmokeRing1_S
		SmokeRing1_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "SmokeRing1"

def GetSet():
	return App.g_kSetManager.GetSet("SmokeRing1")

def Terminate():
	App.g_kSetManager.DeleteSet("SmokeRing1")

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
	kThis.ConfigAmbientLight(0.1, 0.6, 0.3, 0.4)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

	# Light position "Directional Light"
	kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(14.928001, 0.000001, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.0, 1.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 1.0, 0.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(.6, .6, .9, .6)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"

	# Position "Sun"
	kThis = App.Waypoint_Create("Sun", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(300.0, 1600.0, -300.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun"
	
	# Position "SmokeRing"
	kThis = App.Waypoint_Create("Smoke Ring", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(300.0, 1400.0, -250.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "SmokeRing"
	
	# Position "SmokeRing2"
	kThis = App.Waypoint_Create("Smoke Ring 2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(300.0, 1800.0, -350.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "SmokeRing2"
	
	# Position "Overhead"
	kThis = App.Waypoint_Create("Overhead", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(300.0, 1600.0, 250.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Overhead"
	
	# Position "Underneath"
	kThis = App.Waypoint_Create("Underneath", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(300.0, 1600.0, -850.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.208765, 0.512881, 0.832689)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.249968, 0.851151, -0.461582)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Underneath"
		
	# Position "Matter1"
	kThis = App.Waypoint_Create("Matter1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(301.0, 1805.0, -308.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Matter1"
	
	# Position "Matter2"
	kThis = App.Waypoint_Create("Matter2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(422.0, 1722.0, -323.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Matter2"
	
	# Position "Damaged Cardassian"
	kThis = App.Waypoint_Create("Galor", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(3.0, 65.0, -3.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Damaged Cardassian"	
	
	# Position "Galaxy"
	kThis = App.Waypoint_Create("Galaxy", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(3.0, 65.0, 8.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(15.000000)
	kThis.Update(0)
	kThis = None
	# End position "Galaxy"	
	
import App

def LoadBackdrops(pSet):

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

	# Backdrop Sphere "Backdrop treknebulabz6"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebulabz6")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-1.0, 0.0, -0.5)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.5, 0.00, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/treknebulabz6.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.12)
	kThis.SetVerticalSpan(0.15)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebulabz6")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop treknebulabz6"
	
	# Backdrop Sphere "Backdrop treknebula4"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebula4")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.0, -1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/treknebula4.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.20)
	kThis.SetVerticalSpan(0.30)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebula4")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop treknebula4"
	
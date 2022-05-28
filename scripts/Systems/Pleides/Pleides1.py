import App

def Initialize():
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "Pleides1")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.Pleides.Pleides1")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)

	# Load the placements and backdrops for this set.
	LoadPlacements("Pleides1")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "Pleides_S.py" file with an Initialize function that creates them.
	try:
		import Pleides1_S
		Pleides1_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "Pleides1"

def GetSet():
	return App.g_kSetManager.GetSet("Pleides1")

def Terminate():
	App.g_kSetManager.DeleteSet("Pleides1")

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
	kThis.ConfigAmbientLight(1.000000, 1.000000, 1.000000, 0.1)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

	# Light position "Directional Light"
	kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.607303, -0.125438, -0.784505)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 0.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(.5, .5, 1, 1.1)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"

	# Light position "Directional Light 2"
	kThis = App.LightPlacement_Create("Directional Light 2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.607303, 0.125438, 0.784505)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 0.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(.5, .5, 1, 1.1)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light 2"

	# Position "The Seven sisters"
	kThis = App.Waypoint_Create("The Seven Sisters", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(22000.0, 6000.0, 3000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "The Seven Sisters"

	# Position "Sun"
	kThis = App.Waypoint_Create("Sun", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(70000.0, 1000.0, 1500.0)
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
	kThis = App.Waypoint_Create("Sun2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(20000.0, 5000.0, 9000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun2"

	# Position "Sun3"
	kThis = App.Waypoint_Create("Sun3", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(30000.0, 15000.0, 13000.0)
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
	kThis.SetTranslateXYZ(45000.0, 9000.0, 11000.0)
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
	kThis.SetTranslateXYZ(30000.0, 9000.0, -3000.0)
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
	kThis.SetTranslateXYZ(14000.0, 3000.0, 0.0)
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
	kThis.SetTranslateXYZ(95000.0, -3000.0, -1500.0)
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
	kThis.SetTranslateXYZ(105000.0, -8000.0, -2000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun8"

	# Position "Sun9"
	kThis = App.Waypoint_Create("Sun9", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-494000.0, 12000.0, 1000.0)
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
	kThis.SetTranslateXYZ(-18000.0, 9500.0, 3000.0)
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
	kThis.SetTranslateXYZ(9018000.0, 5500.0, 1000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun11"

	# Position "Player Start"
	kThis = App.Waypoint_Create("Vantage Point", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(16.415028, 10.864594, 18.766428)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.020647, -0.480066, -0.876990)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.037678, -0.876180, 0.480509)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Player Start"

	# Position "Pleidian Nebula"
	kThis = App.Waypoint_Create("Pleidian Nebula Center", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(24000.0, 12500.0, 3000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Pleidian Nebula Center"

	# Position "Distant Yellow Star"
	kThis = App.Waypoint_Create("Distant Yellow Star", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-470000.0, 12000.0, 1000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Distant Yellow Star"

	# Position "Betelgeuse"
	kThis = App.Waypoint_Create("Betelgeuse", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(9014000.0, 5500.0, 1000.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Betelgeuse"

	# Position "Planet Location"
	kThis = App.Waypoint_Create("Planet Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(12225.0, 5600.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.08, 1.0)
	kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Planet Location"

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

	# Backdrop Sphere "BlueClusterCustom"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("BlueClusterCustom")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.607303, 0.125438, 0.784505)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.023697, 0.062711, 0.005524)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/Backgrounds/BlueClusterCustom.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.255986)
	kThis.SetVerticalSpan(0.256905)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"BlueClusterCustom")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "BlueClusterCustom"

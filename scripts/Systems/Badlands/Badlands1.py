import App

def Initialize():
	# Create the set ("Badlands1")
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "Badlands1")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.Badlands.Badlands1")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)

	# Load the placements and backdrops for this set.
	LoadPlacements("Badlands1")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "Badlands1_S.py" file with an Initialize function that creates them.
	try:
		import Badlands1_S
		Badlands1_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "Badlands1"

def GetSet():
	return App.g_kSetManager.GetSet("Badlands1")

def Terminate():
	App.g_kSetManager.DeleteSet("Badlands1")

def LoadPlacements(sSetName):
	# Light position "Ambient Light"
	kThis = App.LightPlacement_Create("Ambient Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 0.000000, 1.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.000345, 1.000000, 0.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigAmbientLight(1.000000, 0.200000, 0.200000, 0.050000)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

	# Light position "Directional Light"
	kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-1.000000, 0.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigAmbientLight(0.200000, 0.200000, 0.500000, 0.090000)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"

	# Light position "Light 3"
	kThis = App.LightPlacement_Create("Light 3", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-2.064474, -5074.915527, -151.019547)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.168215, 0.617383, 0.768467)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.518891, -0.607370, 0.601543)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(1.000000, 0.400000, 0.700000, 1.000000)
	kThis.Update(0)
	kThis = None
	# End position "Light 3"

	# Position "Badlands Center- (HAZARD WARNING)"
	kThis = App.Waypoint_Create("Badlands Center- (HAZARD WARNING)", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-244.000000, -4494.000000, 9.550000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Badlands Center- (HAZARD WARNING)"

	# Position "Badlands Near Edge"
	kThis = App.Waypoint_Create("Badlands Near Edge", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(0.000000, -1500.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Badlands Near Edge"

	# Asteroid Field Position "Asteroid Field 1"
	kThis = App.AsteroidFieldPlacement_Create("Asteroid Field 1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(6050.000000, 2400.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetFieldRadius(900.000000)
	kThis.SetNumTilesPerAxis(3)
	kThis.SetNumAsteroidsPerTile(8)
	kThis.SetAsteroidSizeFactor(7.000000)
	kThis.UpdateNodeOnly()
	kThis.ConfigField()
	kThis.Update(0)
	kThis = None
	# End position "Asteroid Field 1"

	# Asteroid Field Position "Asteroid Field 2"
	kThis = App.AsteroidFieldPlacement_Create("Asteroid Field 2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(650.000000, -4400.000000, -50.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetFieldRadius(900.000000)
	kThis.SetNumTilesPerAxis(3)
	kThis.SetNumAsteroidsPerTile(8)
	kThis.SetAsteroidSizeFactor(7.000000)
	kThis.UpdateNodeOnly()
	kThis.ConfigField()
	kThis.Update(0)
	kThis = None
	# End position "Asteroid Field 2"

	# Asteroid Field Position "Asteroid Field 3"
	kThis = App.AsteroidFieldPlacement_Create("Asteroid Field 3", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(650.000000, -6000.000000, -50.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetFieldRadius(1200.000000)
	kThis.SetNumTilesPerAxis(3)
	kThis.SetNumAsteroidsPerTile(9)
	kThis.SetAsteroidSizeFactor(9.000000)
	kThis.UpdateNodeOnly()
	kThis.ConfigField()
	kThis.Update(0)
	kThis = None
	# End position "Asteroid Field 3"

	# Asteroid Field Position "Asteroid Field 4"
	kThis = App.AsteroidFieldPlacement_Create("Asteroid Field 4", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.000000, -10450.000000, -1500.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetFieldRadius(1800.000000)
	kThis.SetNumTilesPerAxis(3)
	kThis.SetNumAsteroidsPerTile(7)
	kThis.SetAsteroidSizeFactor(3.000000)
	kThis.UpdateNodeOnly()
	kThis.ConfigField()
	kThis.Update(0)
	kThis = None
	# End position "Asteroid Field 4"

	# Position "Vortex - Unreachable"
	kThis = App.Waypoint_Create("Vortex - Unreachable", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(650.000000, -4500.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Vortex - Unreachable"

	# Position "Nav Beta"
	kThis = App.Waypoint_Create("Nav Beta", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(0.000000, -5000.000000, 5500.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Nav Beta"

	# Position "Nav Sierra"
	kThis = App.Waypoint_Create("Nav Sierra", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(419.000000, -4653.600098, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Nav Sierra"

	# Position "Nav Delta"
	kThis = App.Waypoint_Create("Nav Delta", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(339.000000, -4678.200195, -10.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Nav Delta"

	# Position "Badlands Far Edge"
	kThis = App.Waypoint_Create("Badlands Far Edge", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(0.000000, -10950.000000, -1500.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Badlands Far Edge"

	# Position "Plasma1"
	kThis = App.Waypoint_Create("Plasma1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(200.000000, -5000.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(100.000000)
	kThis.Update(0)
	kThis = None
	# End position "Plasma1"

	# Position "Plasma2"
	kThis = App.Waypoint_Create("Plasma2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-200.000000, -5000.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(100.000000)
	kThis.Update(0)
	kThis = None
	# End position "Plasma2"

	# Position "Plasma3"
	kThis = App.Waypoint_Create("Plasma3", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.000000, -5290.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(100.000000)
	kThis.Update(0)
	kThis = None
	# End position "Plasma3"

	# Position "Plasma4"
	kThis = App.Waypoint_Create("Plasma4", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.000000, -4700.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(100.000000)
	kThis.Update(0)
	kThis = None
	# End position "Plasma4"

	# Position "Plasma5"
	kThis = App.Waypoint_Create("Plasma5", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(150.000000, -4875.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(100.000000)
	kThis.Update(0)
	kThis = None
	# End position "Plasma5"

	# Position "Plasma6"
	kThis = App.Waypoint_Create("Plasma6", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-550.000000, -5150.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(100.000000)
	kThis.Update(0)
	kThis = None
	# End position "Plasma6"

	# Position "Plasma7"
	kThis = App.Waypoint_Create("Plasma7", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(250.000000, -4250.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(100.000000)
	kThis.Update(0)
	kThis = None
	# End position "Plasma7"

	# Position "Plasma8"
	kThis = App.Waypoint_Create("Plasma8", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(550.000000, -5900.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(100.000000)
	kThis.Update(0)
	kThis = None
	# End position "Plasma8"

	# Position "Plasma9"
	kThis = App.Waypoint_Create("Plasma9", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.000000, -5700.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(100.000000)
	kThis.Update(0)
	kThis = None
	# End position "Plasma9"

	# Position "Plasma10"
	kThis = App.Waypoint_Create("Plasma10", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-750.000000, -5700.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(100.000000)
	kThis.Update(0)
	kThis = None
	# End position "Plasma10"

	# Position "Plasma11"
	kThis = App.Waypoint_Create("Plasma11", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(750.000000, -4700.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(100.000000)
	kThis.Update(0)
	kThis = None
	# End position "Plasma11"

	# Position "Plasma12"
	kThis = App.Waypoint_Create("Plasma12", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(350.000000, -6700.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(100.000000)
	kThis.Update(0)
	kThis = None
	# End position "Plasma12"

	# Position "Plasma13"
	kThis = App.Waypoint_Create("Plasma13", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-900.000000, -5975.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(100.000000)
	kThis.Update(0)
	kThis = None
	# End position "Plasma13"

	# Position "Plasma14"
	kThis = App.Waypoint_Create("Plasma14", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.000000, -5000.000000, 1000.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(100.000000)
	kThis.Update(0)
	kThis = None
	# End position "Plasma14"

	# Position "Plasma15"
	kThis = App.Waypoint_Create("Plasma15", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.000000, -3000.000000, 500.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(100.000000)
	kThis.Update(0)
	kThis = None
	# End position "Plasma15"

	# Position "wreck"
	kThis = App.Waypoint_Create("wreck", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.000000, -5075.000000, -150.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "wreck"
	
	# Position "Keldon"
	kThis = App.Waypoint_Create("Keldon Locale", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.000000, -725.000000, -10.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Keldon"	
	
	# Position "Keldon2"
	kThis = App.Waypoint_Create("Keldon2 Locale", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(30.000000, -735.000000, -10.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Keldon2"		

	# Position "Player Start"
	kThis = App.Waypoint_Create("Player Start", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.000000, -1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.080718, 0.000000, 0.996737)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Player Start"

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
	kThis.SetSphereRadius(320.000000)
	kThis.SetTextureHTile(2.000000)
	kThis.SetTextureVTile(2.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop stars")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop stars"

	# Backdrop Sphere "zmNebCustom1"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("zmNebCustom1")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.335398, 0.142660, -0.931212)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.906235, 0.318915, -0.277545)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/backgrounds/zmNebCustom1.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.045000)
	kThis.SetVerticalSpan(0.089100)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"zmNebCustom1")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "zmNebCustom1"

	# Backdrop Sphere "Backdrop zmNebcustom2"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop zmNebcustom2")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.078479, -0.996710, 0.020274)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.734121, -0.071538, -0.675240)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/Backgrounds/High/zmNebcustom2.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.090275)
	kThis.SetVerticalSpan(0.162495)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop zmNebcustom2")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop zmNebcustom2"


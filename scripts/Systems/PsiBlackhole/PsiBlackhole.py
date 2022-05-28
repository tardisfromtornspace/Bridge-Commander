from bcdebug import debug
import App

def Initialize():
	# Create the set ("PsiBlackhole")
	debug(__name__ + ", Initialize")
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "PsiBlackhole")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.PsiBlackhole.PsiBlackhole")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)

	# Load the placements and backdrops for this set.
	LoadPlacements("PsiBlackhole")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "PsiBlackhole_S.py" file with an Initialize function that creates them.
	try:
		import PsiBlackhole_S
		PsiBlackhole_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	debug(__name__ + ", GetSetName")
	return "PsiBlackhole"

def GetSet():
	debug(__name__ + ", GetSet")
	return App.g_kSetManager.GetSet("PsiBlackhole")

def Terminate():
	debug(__name__ + ", Terminate")
	App.g_kSetManager.DeleteSet("PsiBlackhole")

#make the blackhole initial location a global because it *may* be used later
vBlackhole = []
def LoadPlacements(sSetName):
	debug(__name__ + ", LoadPlacements")
	global vBlackhole
	vSun = (33400.0, -2600.0, 200.0)
	vPlanet = (26400.0, 2900.0, -100.0)
	vPlaSunNAV = (29900.0, 150.0, 50.0)
	vPlayer = (0.0, 0.0, 0.0)
	vBlackhole = (-30400.0, -19100.0, 0.0)
	vAsteroids = (-2000.0, 200.0, 0.0)

	# Light position "Ambient Light"
	kThis = App.LightPlacement_Create("Ambient Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(vBlackhole[0], vBlackhole[1], vBlackhole[2])
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigAmbientLight(0.100000, 0.100000, 0.100000, 0.05)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

	# Light position "Sun Light"
	kThis = App.LightPlacement_Create("Sun Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(vSun[0], vSun[1], vSun[2])
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(0.4, 0.4, 1, 0.5)
	kThis.Update(0)
	kThis = None
	# End position "Sun Light"

	# Asteroid Field Position "Asteroid Field 1"
	kThis = App.AsteroidFieldPlacement_Create("Asteroid Field 1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(vAsteroids[0], vAsteroids[1], vAsteroids[2])
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.0, 0.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 1.0, 0.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetFieldRadius(1000.000000)
	kThis.SetNumTilesPerAxis(3)
	kThis.SetNumAsteroidsPerTile(15)
	kThis.SetAsteroidSizeFactor(7.000000)
	kThis.UpdateNodeOnly()
	kThis.ConfigField()
	kThis.Update(0)
	kThis = None
	# End position "Asteroid Field 1"

	# Position "Sun"
	kThis = App.Waypoint_Create("Sun", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(vSun[0], vSun[1], vSun[2])
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun"

	# Position "Sun And Planet NAV"
	kThis = App.Waypoint_Create("Sun And Planet NAV", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(vPlaSunNAV[0], vPlaSunNAV[1], vPlaSunNAV[2])
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Sun And Planet NAV"

	# Position "Player Start"
	kThis = App.Waypoint_Create("Player Start", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(vPlayer[0], vPlayer[1], vPlayer[2])
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 0.0, 1.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 0.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.0)
	kThis.Update(0)
	kThis = None
	# End position "Player Start"

	# Position "Planet Location"
	kThis = App.Waypoint_Create("Planet Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(vPlanet[0], vPlanet[1], vPlanet[2])
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.000000, 0.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Planet Location"

	# Position "Blackhole Start"
	kThis = App.Waypoint_Create("Blackhole Start", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(vBlackhole[0], vBlackhole[1], vBlackhole[2])
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Blackhole Start"

	# Position "Asteroids NAV"
	kThis = App.Waypoint_Create("Asteroids NAV", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(vAsteroids[0], vAsteroids[1], vAsteroids[2])
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Asteroids NAV"



def LoadBackdrops(pSet):

	#Draw order is implicit. First object gets drawn first

	# Star Sphere "Backdrop stars"
	debug(__name__ + ", LoadBackdrops")
	kThis = App.StarSphere_Create()
	kThis.SetName("Backdrop stars")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.185766, 0.947862, -0.258938)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.049821, 0.254100, 0.965894)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/stars.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(1.000000)
	kThis.SetVerticalSpan(1.000000)
	kThis.SetSphereRadius(35000.000000)
	kThis.SetTextureHTile(22.000000)
	kThis.SetTextureVTile(11.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop stars")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop stars"

	# Backdrop Sphere "Backdrop treknebula8 2"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Backdrop treknebula8 2")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.494816, 0.686146, -0.533255)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.736909, 0.656541, 0.160991)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/Backgrounds/treknebula8.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(0.289075)
	kThis.SetVerticalSpan(0.116102)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(1.000000)
	kThis.SetTextureVTile(1.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop treknebula8 2")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop treknebula8 2"


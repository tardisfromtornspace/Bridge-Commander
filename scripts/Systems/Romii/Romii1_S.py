from bcdebug import debug
import traceback
import App
import loadspacehelper
import MissionLib
import Tactical.LensFlares

def Initialize(pSet):

        # Sun1
	debug(__name__ + ", Initialize")
	# pSun = App.Sun_Create(6000.0, 6500, 500, "data/Textures/SunWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	# pSet.AddObjectToSet(pSun, "Sun")
	
	# Place the object at the specified location.
	# pSun.PlaceObjectByName( "Sun" )
	# pSun.UpdateNodeOnly()

	# Builds a Blue lens flare for Sun 1
	# Tactical.LensFlares.BlueGlareBright(pSet, pSun)

        # Sun2
	pSun2 = App.Sun_Create(2600.0, 2650, 500, "data/Textures/SunWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun2, "Sun")
	
	# Place the object at the specified location.
	pSun2.PlaceObjectByName( "Sun2" )
	pSun2.UpdateNodeOnly()

	# Builds a Blue lens flare for Sun 2
	Tactical.LensFlares.WhiteLensFlare(pSet, pSun2)


	pRomii = App.Planet_Create(360.0, "data/Models/Environment/Planet/Romii.NIF")
	pSet.AddObjectToSet(pRomii, "Romii Planet")

	pRomii.PlaceObjectByName("Planet")
	pRomii.UpdateNodeOnly()
	
	shouldWeSpin = 0
	try:
		from Custom.NanoFXv2.SpecialFX.AtmosphereALT import AddRotatingBody
		AddRotatingBody(pRomii, (App.g_kSystemWrapper.GetRandomNumber(5) + 3) / 10000.0)
		shouldWeSpin = 1
	except:
		shouldWeSpin = 0
		traceback.print_exc()

	if shouldWeSpin:
		pClouds = App.Planet_Create(370.0, "data/Models/Environment/Planet/Romii.NIF")
		pSet.AddObjectToSet(pClouds, "Romii")

		pClouds.PlaceObjectByName("PlanetClouds")
		pClouds.UpdateNodeOnly()
		pRomii.AttachObject(pClouds)
		AddRotatingBody(pClouds, 0.0009)


	# Model and placement for Moon 1
	pMoon = App.Planet_Create(175.0, "data/Models/Environment/MClass1.nif")
	pSet.AddObjectToSet(pMoon, "Moon Planet")

	#Place the object at the specified location.
	pMoon.PlaceObjectByName("Moon1")
	pMoon.UpdateNodeOnly()
	if shouldWeSpin:
		AddRotatingBody(pMoon, 0.0000)


	pRomii1 = App.Planet_Create(320.0, "data/Models/Environment/NClass1.NIF")
	pSet.AddObjectToSet(pRomii1, "Romii 1 Planet")

	pRomii1.PlaceObjectByName("Planet2")
	pRomii1.UpdateNodeOnly()
	if shouldWeSpin:
		AddRotatingBody(pRomii1, 0.0005)


	pNBump = App.Planet_Create(321.3, "data/Models/Environment/NClass2.NIF")
	pSet.AddObjectToSet(pNBump, "Romii 1")

	pNBump.PlaceObjectByName("Planet2Clouds")
	pNBump.UpdateNodeOnly()
	pRomii1.AttachObject(pNBump)
	if shouldWeSpin:
		AddRotatingBody(pNBump, 0.0005)
	
	# Create the station here so we don't have to worry about it
	# when it appears in later missions
        if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
	        loadspacehelper.CreateShip("RomulanOutpost", pSet, "Romulan Station", "Station Location")

#Nebula info reads (R,G,B, Vision-distance, Sensor interference, "neblua texture", "nebula external texture")

	# Center Neb Placement
	# pNebula1 = App.MetaNebula_Create(100.0 / 255.0, 99.0 / 255.0, 146.0 / 255.0, 5000.0, 2500.0, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	# pNebula1.SetupDamage(2500.0, 500.0)

	# pNebula1.AddNebulaSphere(0.0, -225500, 0.0, 16500.0)
	# Puts the nebula in the set
	# pSet.AddObjectToSet(pNebula1, "Nebula1")

def AddRotatingBody(pObject, fSpeed):
	global g_lRotatingBodies

	g_lRotatingBodies.append([pObject.GetObjID(), 0.0, fSpeed])

	StartRotationTimer()

def StartRotationTimer():
	global g_bRotationTimerRunning

	if g_bRotationTimerRunning:
		return

	g_bRotationTimerRunning = 1

	MissionLib.CreateTimer(App.Game_GetNextEventType(), __name__ + ".RotateTimer", App.g_kUtopiaModule.GetGameTime() + 0.1, 0, 0)

def RotateTimer(pObject, pEvent):
	global g_lRotatingBodies

	for lBody in g_lRotatingBodies:
		iID = lBody[0]
		fRot = lBody[1]
		fSpeed = lBody[2]

		pBody = App.ObjectClass_GetObjectByID(None, iID)

		if pBody:
			fRot = fRot + fSpeed

			pBody.SetAngleAxisRotation(fRot, 0, 0, 1)
			pBody.UpdateNodeOnly()

			lBody[1] = fRot

	MissionLib.CreateTimer(App.Game_GetNextEventType(), __name__ + ".RotateTimer", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)

	return 0
###############################################################################
#	Filename:	TheGalaxy3_S.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard
#	
#	Creates TheGalaxy3 static objects.  Called by TranswarpHub1.py when region is created
#	
#	Created:	09/17/00 
#	Modified:	10/04/01 - Tony Evans
#	Modified:	08/25/02 - Ben Howard
###############################################################################
import App
import loadspacehelper
import MissionLib
import Tactical.LensFlares

def Initialize(pSet):


	# Add a sun, far far away
	pSun = App.Sun_Create(1500, 2000, 500, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresOrange.tga")
	pSet.AddObjectToSet(pSun, "Kling")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()
	
	Tactical.LensFlares.YellowLensFlare(pSet, pSun)

	# Model and placement for Earth
	pPlanet = App.Planet_Create(1202, "data/models/environment/RootBeerPlanet.nif")
	pSet.AddObjectToSet(pPlanet, "Kronos")

	#Place the object at the specified location.
	pPlanet.PlaceObjectByName("EarthL")
	pPlanet.UpdateNodeOnly()
	pPlanet.SetAtmosphereRadius(150)

	# Model and placement for Moon
	pPlanet3 = App.Planet_Create(400, "data/models/environment/BlueRockyPlanet.nif")
	pSet.AddObjectToSet(pPlanet3, "Takoth")

	#Place the object at the specified location.
	pPlanet3.PlaceObjectByName("MoonL")
	pPlanet3.UpdateNodeOnly()

        if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
	        # Create our static stations and such
	        pHub4	= loadspacehelper.CreateShip("City", pSet, "Hall of Heroes", "Inner3")
	        if (pHub4 != None):
		        # Turn off the ships repair
		        MissionLib.HideSubsystems(pHub4)
		        pHub4.SetAlertLevel(App.ShipClass.GREEN_ALERT)
	
	        # Create our static stations and such
	        pHub2	= loadspacehelper.CreateShip("City", pSet, "High Council Chambers", "Inner2")
	        if (pHub2 != None):
		        # Turn off the ships repair
		        MissionLib.HideSubsystems(pHub2)
		        pHub2.SetAlertLevel(App.ShipClass.GREEN_ALERT)

	        # Create our static stations and such
	        pHub11	= loadspacehelper.CreateShip("City", pSet, "Warrior Monument", "Transwarp6")
	        if (pHub11 != None):
		        # Turn off the ships repair
		        MissionLib.HideSubsystems(pHub11)
		        pHub11.SetAlertLevel(App.ShipClass.GREEN_ALERT)
	
	        # Create our static stations and such
	        pHub8	= loadspacehelper.CreateShip("City", pSet, "Emperors Palace", "Transwarp8")
	        if (pHub8 != None):
		        # Turn off the ships repair
		        MissionLib.HideSubsystems(pHub8)
		        pHub8.SetAlertLevel(App.ShipClass.GREEN_ALERT)
	
	        # Create our static stations and such
	        pHub12	= loadspacehelper.CreateShip("City", pSet, "Hall of Records", "Transwarp4")
	        if (pHub12 != None):
		        # Turn off the ships repair
		        MissionLib.HideSubsystems(pHub12)
		        pHub12.SetAlertLevel(App.ShipClass.GREEN_ALERT)
	
	        # Create our static stations and such
	        pHub7	= loadspacehelper.CreateShip("City", pSet, "Fleet Academy", "Transwarp2")
	        if (pHub7 != None):
		        # Turn off the ships repair
		        MissionLib.HideSubsystems(pHub7)
		        pHub7.SetAlertLevel(App.ShipClass.GREEN_ALERT)

	pNebula = App.MetaNebula_Create(245.0 / 255.0, 90.0 / 255.0, 105.0 / 255.0, 145.0, 10.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula.SetupDamage(1.0, 5.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula.AddNebulaSphere(301.0, 1801.0, 201.0, 250.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula, "Nebula1")

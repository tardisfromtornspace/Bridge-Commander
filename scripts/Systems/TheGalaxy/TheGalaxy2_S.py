###############################################################################
#	Filename:	TheGalaxy2_S.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard
#	
#	Creates TheGalaxy 1 static objects.  Called by TranswarpHub1.py when region is created
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
	pSun = App.Sun_Create(5000, 5000, 500, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresYellow.tga")
	pSet.AddObjectToSet(pSun, "Sol")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()
	
	Tactical.LensFlares.YellowLensFlare(pSet, pSun)
	

	# Model and placement for Mercury
	pPlanet3 = App.Planet_Create(210, "data/models/environment/RockyPlanet.nif")
	pSet.AddObjectToSet(pPlanet3, "Mercury")

	#Place the object at the specified location.
	pPlanet3.PlaceObjectByName("MercuryL")
	pPlanet3.UpdateNodeOnly()
	pPlanet3.SetAtmosphereRadius(1)


	# Model and placement for Venus
	pPlanet4 = App.Planet_Create(1210, "data/models/environment/BrownPlanet.nif")
	pSet.AddObjectToSet(pPlanet4, "Venus")

	#Place the object at the specified location.
	pPlanet4.PlaceObjectByName("VenusL")
	pPlanet4.UpdateNodeOnly()
	pPlanet4.SetAtmosphereRadius(100)

	# Model and placement for Earth
	pPlanet = App.Planet_Create(1210, "data/models/environment/earth.nif")
	pSet.AddObjectToSet(pPlanet, "Earth")

	#Place the object at the specified location.
	pPlanet.PlaceObjectByName("EarthL")
	pPlanet.UpdateNodeOnly()
	pPlanet.SetAtmosphereRadius(150)

	# Model and placement for Moon
	pPlanet2 = App.Planet_Create(217, "data/models/environment/moon.nif")
	pSet.AddObjectToSet(pPlanet2, "Moon")

	#Place the object at the specified location.
	pPlanet2.PlaceObjectByName("MoonL")
	pPlanet2.UpdateNodeOnly()

	# Model and placement for Mars
	pPlanet5 = App.Planet_Create(1010, "data/models/environment/RedPlanet.nif")
	pSet.AddObjectToSet(pPlanet5, "Mars")

	#Place the object at the specified location.
	pPlanet5.PlaceObjectByName("MarsL")
	pPlanet5.UpdateNodeOnly()
	pPlanet5.SetAtmosphereRadius(15)

	# Model and placement for Jupiter
	pPlanet6 = App.Planet_Create(4010, "data/models/environment/TanPlanet.nif")
	pSet.AddObjectToSet(pPlanet6, "Jupiter")

	#Place the object at the specified location.
	pPlanet6.PlaceObjectByName("JupiterL")
	pPlanet6.UpdateNodeOnly()
	pPlanet6.SetAtmosphereRadius(1005)

	# Model and placement for Saturn
	pPlanet7 = App.Planet_Create(1410, "data/models/environment/saturn.nif")
	pSet.AddObjectToSet(pPlanet7, "Saturn")

	#Place the object at the specified location.
	pPlanet7.PlaceObjectByName("SaturnL")
	pPlanet7.UpdateNodeOnly()
	pPlanet7.SetAtmosphereRadius(815)

	# Model and placement for Neptune
	pPlanet8 = App.Planet_Create(1110, "data/models/environment/BlueWhiteGasPlanet.nif")
	pSet.AddObjectToSet(pPlanet8, "Neptune")

	#Place the object at the specified location.
	pPlanet8.PlaceObjectByName("NeptuneL")
	pPlanet8.UpdateNodeOnly()
	pPlanet8.SetAtmosphereRadius(185)

	# Model and placement for Uranus
	pPlanet9 = App.Planet_Create(1210, "data/models/environment/BlueGrayPlanet.nif")
	pSet.AddObjectToSet(pPlanet9, "Uranus")

	#Place the object at the specified location.
	pPlanet9.PlaceObjectByName("UranusL")
	pPlanet9.UpdateNodeOnly()
	pPlanet9.SetAtmosphereRadius(105)

	# Model and placement for Pluto
	pPlanet10 = App.Planet_Create(810, "data/models/environment/IcePlanet.nif")
	pSet.AddObjectToSet(pPlanet10, "Pluto")

	#Place the object at the specified location.
	pPlanet10.PlaceObjectByName("PlutoL")
	pPlanet10.UpdateNodeOnly()
	pPlanet10.SetAtmosphereRadius(1)

	if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
                return
                
	# Create our static stations and such
	pHub2	= loadspacehelper.CreateShip("City", pSet, "Starfleet Command", "Transwarp2")
	if (pHub2 != None):
		# Turn off the ships repair
		MissionLib.HideSubsystems(pHub2)
		pHub2.SetAlertLevel(App.ShipClass.GREEN_ALERT)
	
	# Create our static stations and such
	pHub3	= loadspacehelper.CreateShip("City", pSet, "New York", "Transwarp4")
	if (pHub3 != None):
		# Turn off the ships repair
		MissionLib.HideSubsystems(pHub3)
		pHub3.SetAlertLevel(App.ShipClass.GREEN_ALERT)
	
	# Create our static stations and such
	pHub4	= loadspacehelper.CreateShip("City", pSet, "London", "Transwarp3")
	if (pHub4 != None):
		# Turn off the ships repair
		MissionLib.HideSubsystems(pHub4)
		pHub4.SetAlertLevel(App.ShipClass.GREEN_ALERT)
	
	# Create our static stations and such
	pHub7	= loadspacehelper.CreateShip("City", pSet, "Moscow", "Transwarp7")
	if (pHub7 != None):
		# Turn off the ships repair
		MissionLib.HideSubsystems(pHub7)
		pHub7.SetAlertLevel(App.ShipClass.GREEN_ALERT)
	
	# Create our static stations and such
	pHub8	= loadspacehelper.CreateShip("City", pSet, "Tokyo", "Transwarp8")
	if (pHub8 != None):
		# Turn off the ships repair
		MissionLib.HideSubsystems(pHub8)
		pHub8.SetAlertLevel(App.ShipClass.GREEN_ALERT)
	
	# Create our static stations and such
	pHub12	= loadspacehelper.CreateShip("City", pSet, "Honolulu", "Inner3")
	if (pHub12 != None):
		# Turn off the ships repair
		MissionLib.HideSubsystems(pHub12)
		pHub12.SetAlertLevel(App.ShipClass.GREEN_ALERT)
	
	# Create our static stations and such
	pHub6	= loadspacehelper.CreateShip("City", pSet, "Paris", "Transwarp6")
	if (pHub6 != None):
		# Turn off the ships repair
		MissionLib.HideSubsystems(pHub6)
		pHub6.SetAlertLevel(App.ShipClass.GREEN_ALERT)
	
	# Create our static stations and such
	pHub11	= loadspacehelper.CreateShip("City", pSet, "Sydney", "Inner2")
	if (pHub11 != None):
		# Turn off the ships repair
		MissionLib.HideSubsystems(pHub11)
		pHub11.SetAlertLevel(App.ShipClass.GREEN_ALERT)
	
	# Create our static stations and such
	pHub14	= loadspacehelper.CreateShip("City", pSet, "Lake Armstrong", "Inner5")
	if (pHub14 != None):
		# Turn off the ships repair
		MissionLib.HideSubsystems(pHub14)
		pHub14.SetAlertLevel(App.ShipClass.GREEN_ALERT)
	
	# Create our static stations and such
	pHub18	= loadspacehelper.CreateShip("City", pSet, "Augusta Georgia", "Georgia")
	if (pHub18 != None):
		# Turn off the ships repair
		MissionLib.HideSubsystems(pHub18)
		pHub18.SetAlertLevel(App.ShipClass.GREEN_ALERT)

	# Create our static stations and such
	pHub15	= loadspacehelper.CreateShip("FedStarbase", pSet, "Starbase 1", "Inner6")

	# Create our static stations and such
	pHub16	= loadspacehelper.CreateShip("DryDock", pSet, "Shipyard 1", "Ship1")

	# Create our static stations and such
	pHub17	= loadspacehelper.CreateShip("DryDock", pSet, "Shipyard 2", "Ship2")

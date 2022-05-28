###############################################################################
#	Filename:	TheGalaxy5_S.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard
#	
#	Creates TheGalaxy5 static objects.  Called by TranswarpHub1.py when region is created
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
	pSun = App.Sun_Create(1000.0, 5000, 500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresYellow.tga")
	pSet.AddObjectToSet(pSun, "Rom")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Builds a Red-Orange lens flare, attached to the sun
	Tactical.LensFlares.WhiteLensFlare(pSet, pSun)

	# Model and placement for Romulus
	pPlanet = App.Planet_Create(1202, "data/models/environment/AquaPlanet.nif")
	pSet.AddObjectToSet(pPlanet, "Romulus1")

	#Place the object at the specified location.
	pPlanet.PlaceObjectByName("RomulusL")
	pPlanet.UpdateNodeOnly()
	pPlanet.SetAtmosphereRadius(150)


	# Model and placement for Moon
	pPlanet2 = App.Planet_Create(217, "data/models/environment/BlueRockyPlanet.nif")
	pSet.AddObjectToSet(pPlanet2, "Remus")

	#Place the object at the specified location.
	pPlanet2.PlaceObjectByName("MoonL")
	pPlanet2.UpdateNodeOnly()



	pNebula2 = App.MetaNebula_Create(25.0 / 255.0, 140.0 / 255.0, 85.0 / 255.0, 3000.0, 15.0, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula2.SetupDamage(1.0, 1.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula2.AddNebulaSphere(-10500.0, 1950.0, 5075.0,  5000.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula2, "Nebula2")


        if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
	        # Create our static stations and such
	        pHub4	= loadspacehelper.CreateShip("City", pSet, "Imperial Palace", "Inner3")
	        if (pHub4 != None):
        		# Turn off the ships repair
		        MissionLib.HideSubsystems(pHub4)
		        pHub4.SetAlertLevel(App.ShipClass.GREEN_ALERT)
	
	        # Create our static stations and such
	        pHub2	= loadspacehelper.CreateShip("City", pSet, "Fleet Control", "Inner2")
	        if (pHub2 != None):
        		# Turn off the ships repair
	        	MissionLib.HideSubsystems(pHub2)
		        pHub2.SetAlertLevel(App.ShipClass.GREEN_ALERT)

	        # Create our static stations and such
	        pHub11	= loadspacehelper.CreateShip("City", pSet, "Firefalls", "Transwarp6")
	        if (pHub11 != None):
		        # Turn off the ships repair
		        MissionLib.HideSubsystems(pHub11)
		        pHub11.SetAlertLevel(App.ShipClass.GREEN_ALERT)
	
	        # Create our static stations and such
	        pHub8	= loadspacehelper.CreateShip("City", pSet, "Valley of Chuma", "Transwarp8")
	        if (pHub8 != None):
		        # Turn off the ships repair
		        MissionLib.HideSubsystems(pHub8)
		        pHub8.SetAlertLevel(App.ShipClass.GREEN_ALERT)
	
	        # Create our static stations and such
	        pHub7	= loadspacehelper.CreateShip("City", pSet, "Senate Chambers", "Transwarp2")
	        if (pHub7 != None):
		        # Turn off the ships repair
		        MissionLib.HideSubsystems(pHub7)
		        pHub7.SetAlertLevel(App.ShipClass.GREEN_ALERT)

	        # Create our static stations and such
	        pHub14	= loadspacehelper.CreateShip("City", pSet, "Mining Facility", "Inner5")
	        if (pHub14 != None):
		        # Turn off the ships repair
		        MissionLib.HideSubsystems(pHub14)
		        pHub14.SetAlertLevel(App.ShipClass.GREEN_ALERT)

	        # Create our static stations and such
	        pHub15	= loadspacehelper.CreateShip("CardStarbase", pSet, "Tal ShiAr", "shiar")
	
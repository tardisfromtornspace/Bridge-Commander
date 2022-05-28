###############################################################################
#	Filename:	Obstacles1_S.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard
#	
#	Creates Obstacles1 static objects.  Called by TranswarpHub.py when region is created
#	
#	Created:	09/17/00 
#	Modified:	10/04/01 - Tony Evans
#	Modified:	09/25/02 - Ben Howard
###############################################################################
import App
import loadspacehelper
import MissionLib
import Tactical.LensFlares

def Initialize(pSet):

	pSun = App.Sun_Create(2000.0, 2000, 500, "data/Textures/SunBrown.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun, "Star")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Star" )
	pSun.UpdateNodeOnly()

	Tactical.LensFlares.WhiteLensFlare(pSet, pSun)


	# Model and placement for Obstacles1a
	pPlanet = App.Planet_Create(500.0, "data/models/environment/RedPlanet.nif")
	pSet.AddObjectToSet(pPlanet, "Blocker 1")

	#Place the object at the specified location.
	pPlanet.PlaceObjectByName("Planet")
	pPlanet.UpdateNodeOnly()

	# Model and placement for Obstacles1b
	pPlanet2 = App.Planet_Create(20.0, "data/models/environment/IcePlanet.nif")
	pSet.AddObjectToSet(pPlanet2, "Moon")

	#Place the object at the specified location.
	pPlanet2.PlaceObjectByName("Moon")
	pPlanet2.UpdateNodeOnly()
	
	# Create the station here so we don't have to worry about it
	# when it appears in later missions
        if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
	        pHelpStation	=loadspacehelper.CreateShip("FedStarbase", pSet, "Spectators", "Station")
	        if (pHelpStation != None):
		        pHelpStation.SetAlertLevel(App.ShipClass.RED_ALERT)
		        import HelpbaseAI
		        pHelpStation.SetAI(HelpbaseAI.CreateAI(pHelpStation))

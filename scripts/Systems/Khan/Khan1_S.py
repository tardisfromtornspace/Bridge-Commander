###############################################################################
#	Filename:	Khan1_S.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard
#	
#	Creates Khan 1 static objects.  Called by Khan1.py when region is created
#	
#	Created:	09/17/00 
#	Modified:	10/04/01 - Tony Evans
#	Modified:	04/05/02 - Ben Howard
###############################################################################
import App
import loadspacehelper
import Tactical.LensFlares
import MissionLib

def Initialize(pSet):

	# Add a sun, far far away
	pSun = App.Sun_Create(600.0, 900, 100, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresOrange.tga")
	pSet.AddObjectToSet(pSun, "Regula Prime")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Builds a Red-Orange lens flare, attached to the sun
	Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun)
	
	pSun2 = App.Sun_Create(800.0, 1400, 100, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun2, "Ceti Alpha")
	
	# Place the object at the specified location.
	pSun2.PlaceObjectByName( "Sun2" )
	pSun2.UpdateNodeOnly()


	# Model and placement for Regulus
	pPlanet = App.Planet_Create(600.0, "data/models/environment/BrownPlanet.nif")
	pSet.AddObjectToSet(pPlanet, "Regula")

	#Place the object at the specified location.
	pPlanet.PlaceObjectByName("Regula")
	pPlanet.UpdateNodeOnly()

	# Model and placement for Ceti1
	pPlanet = App.Planet_Create(100.0, "data/models/environment/RedPlanet.nif")
	pSet.AddObjectToSet(pPlanet, "Ceti Alpha1")

	#Place the object at the specified location.
	pPlanet.PlaceObjectByName("Ceti1")
	pPlanet.UpdateNodeOnly()

	# Model and placement for Ceti2
	pPlanet = App.Planet_Create(400.0, "data/models/environment/PurpleWhitePlanet.nif")
	pSet.AddObjectToSet(pPlanet, "Ceti Alpha2")

	#Place the object at the specified location.
	pPlanet.PlaceObjectByName("Ceti2")
	pPlanet.UpdateNodeOnly()

	# Model and placement for Ceti3
	pPlanet = App.Planet_Create(350.0, "data/models/environment/TanPlanet.nif")
	pSet.AddObjectToSet(pPlanet, "Ceti Alpha3")

	#Place the object at the specified location.
	pPlanet.PlaceObjectByName("Ceti3")
	pPlanet.UpdateNodeOnly()

	# Model and placement for Ceti4
	pPlanet = App.Planet_Create(280.0, "data/models/environment/BlueWhiteGasPlanet.nif")
	pSet.AddObjectToSet(pPlanet, "Ceti Alpha4")

	#Place the object at the specified location.
	pPlanet.PlaceObjectByName("Ceti4")
	pPlanet.UpdateNodeOnly()

	# Model and placement for Ceti5
	pPlanet = App.Planet_Create(130.0, "data/models/environment/moon.nif")
	pSet.AddObjectToSet(pPlanet, "Ceti Alpha5")

	#Place the object at the specified location.
	pPlanet.PlaceObjectByName("Ceti5")
	pPlanet.UpdateNodeOnly()

	# Model and placement for Ceti6
	pPlanet = App.Planet_Create(90.0, "data/models/environment/DryPlanet.nif")
	pSet.AddObjectToSet(pPlanet, "Ceti Alpha6")

	#Place the object at the specified location.
	pPlanet.PlaceObjectByName("Ceti6")
	pPlanet.UpdateNodeOnly()
	
	

	# MetaNebula_Create params are:
	# r, g, b : (floats [0.0 , 1.0]) 
	# visibility distance inside the nebula (float in world units)
	# sensor density of nebula(value to scale sensor range by)
    	# name of internal texture (needs alpha)
	# name of external texture (no need for alpha)
	
	pNebula = App.MetaNebula_Create(230.0 / 255.0, 30.0 / 255.0, 15.0  / 255.0, 400.0, 20.5, "data/Backgrounds/nebulaoverlayred.tga", "data/Backgrounds/nebulaexternalred.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula.SetupDamage(0.0, 400.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula.AddNebulaSphere(1800.0, -1900.0, -800.0, 2300.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula, "Nebula1")
	
	pNebula2 = App.MetaNebula_Create(30.0 / 255.0, 10.0 / 255.0, 165.0  / 255.0, 150.0, 20.5, "data/Backgrounds/nebulaoverlayred.tga", "data/Backgrounds/nebulaexternalred.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula2.SetupDamage(0.0, 400.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula2.AddNebulaSphere(1900.0, -2000.0, -100.0, 600.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula2, "Nebula2")
	
	pNebula3 = App.MetaNebula_Create(30.0 / 255.0, 160.0 / 255.0, 45.0  / 255.0, 70.0, 20.5, "data/Backgrounds/nebulaoverlayred.tga", "data/Backgrounds/nebulaexternalred.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula3.SetupDamage(0.0, 400.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula3.AddNebulaSphere(1100.0, -2700.0, -1100.0, 800.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula3, "Nebula3")
	
	pNebula4 = App.MetaNebula_Create(180.0 / 255.0, 110.0 / 255.0, 45.0  / 255.0, 50.0, 20.5, "data/Backgrounds/nebulaoverlayred.tga", "data/Backgrounds/nebulaexternalred.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula4.SetupDamage(0.0, 400.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula4.AddNebulaSphere(2200.0, -900.0, -700.0, 800.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula4, "Nebula4")
	
	pNebula5 = App.MetaNebula_Create(180.0 / 255.0, 190.0 / 255.0, 225.0  / 255.0, 20.0, 20.5, "data/Backgrounds/nebulaoverlayred.tga", "data/Backgrounds/nebulaexternalred.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula5.SetupDamage(0.0, 400.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula5.AddNebulaSphere(950.0, -400.0, 300.0, 400.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula5, "Nebula5")


	if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
		# Create our static stations and such
		pRegStation	= loadspacehelper.CreateShip("FedOutpost", pSet, "Regula Science Facility", "Station Location")
		if (pRegStation != None):
			# Damage the station and give it rotation
			MissionLib.SetRandomRotation(pRegStation, 9.0)
			# Damage it's hull
			pRepair = pRegStation.GetRepairSubsystem()
			pProp 	= pRepair.GetProperty()
			pProp.SetMaxRepairPoints(0.0)
			pRegStation.SetAlertLevel(App.ShipClass.GREEN_ALERT)
	
		# Create our static stations and such
		pBotanyBay	= loadspacehelper.CreateShip("Transport", pSet, "Botany Bay", "BBay")
		if (pBotanyBay != None):
			# Damage it's hull
			pRepair = pBotanyBay.GetRepairSubsystem()
			pProp 	= pRepair.GetProperty()
			pProp.SetMaxRepairPoints(0.0)
			pBotanyBay.DamageSystem(pBotanyBay.GetHull(), pBotanyBay.GetHull().GetMaxCondition() * 0.30)
			MissionLib.HideSubsystems(pBotanyBay)
			pBotanyBay.DisableGlowAlphaMaps()
			pBotanyBay.SetAlertLevel(App.ShipClass.GREEN_ALERT)

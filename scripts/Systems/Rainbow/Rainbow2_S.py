###############################################################################
#	Filename:	Rainbow2_S.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard
#	
#	Creates Rainbow2 static objects.  Called by ArenaB1.py when region is created
#	
#	Created:	09/17/00 
#	Modified:	10/04/01 - Tony Evans
#	Modified:	03/15/02 - Ben Howard
###############################################################################
import App
import loadspacehelper
import MissionLib
import Tactical.LensFlares

def Initialize(pSet):

#	To create a colored sun:
#	pSun = App.Sun_Create(fRadius, fAtmosphereThickness, fDamagePerSec, fBaseTexture , fFlareTexture)
#
#	for fBaseTexture you can use:
#		data/Textures/SunBase.tga 
#		data/Textures/SunRed.tga
#		data/Textures/SunRedOrange.tga
#		data/Textures/SunYellow.tga
#		data/Textures/SunBlueWhite.tga
#	for fFlareTexture you can use:
#		data/Textures/Effects/SunFlaresOrange.tga
#		data/Textures/Effects/SunFlaresRed.tga
#		data/Textures/Effects/SunFlaresRedOrange.tga
#		data/Textures/Effects/SunFlaresYellow.tga
#		data/Textures/Effects/SunFlaresBlue.tga
#		data/Textures/Effects/SunFlaresWhite.tga

	# Add a sun, far far away
	pSun = App.Sun_Create(160.0, 200, 500, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresYellow.tga")
	pSet.AddObjectToSet(pSun, "Valhalla")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	pSun2 = App.Sun_Create(160.0, 500, 500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresOrange.tga")
	pSet.AddObjectToSet(pSun2, "Rainbow")
	
	# Place the object at the specified location.
	pSun2.PlaceObjectByName( "Sun2" )
	pSun2.UpdateNodeOnly()

	pSun3 = App.Sun_Create(160.0, 900, 500, "data/Textures/SunPurple.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun3, "Stellar Matter")
	
	# Place the object at the specified location.
	pSun3.PlaceObjectByName( "Sun3" )
	pSun3.UpdateNodeOnly()

	pSun4 = App.Sun_Create(160.0, 1200, 500, "data/Textures/SunDrkBlue.tga", "data/Textures/Effects/SunFlaresBlue.tga")
	pSet.AddObjectToSet(pSun4, "Radiation Hazard")
	
	# Place the object at the specified location.
	pSun4.PlaceObjectByName( "Sun4" )
	pSun4.UpdateNodeOnly()
	
	# Model and placement for Odin
	pPlanet = App.Planet_Create(400.0, "data/models/environment/TanPlanet.nif")
	pSet.AddObjectToSet(pPlanet, "Odin")

	#Place the object at the specified location.
	pPlanet.PlaceObjectByName("Odinloc")
	pPlanet.UpdateNodeOnly()

	# Model and placement for Thought
	pPlanet = App.Planet_Create(20.0, "data/models/environment/BrownPlanet.nif")
	pSet.AddObjectToSet(pPlanet, "Thought")
	pPlanet.SetAtmosphereRadius(80)

	#Place the object at the specified location.
	pPlanet.PlaceObjectByName("Thought")
	pPlanet.UpdateNodeOnly()

	# Model and placement for Moon 1
	pPlanet = App.Planet_Create(30.0, "data/models/environment/TanGasPlanet.nif")
	pSet.AddObjectToSet(pPlanet, "Memory")

	#Place the object at the specified location.
	pPlanet.PlaceObjectByName("Memory")
	pPlanet.UpdateNodeOnly()


	# Create our static stations and such
	pHive	= loadspacehelper.CreateShip("CardOutpost", pSet, "Insectoid Hive", "Station Location")
	if (pHive != None):
		pHive.SetAlertLevel(App.ShipClass.RED_ALERT)
		import HiveAI
		pHive.SetAI(HiveAI.CreateAI(pHive))

	# MetaNebula_Create params are:
	# r, g, b : (floats [0.0 , 1.0]) 
	# visibility distance inside the nebula (float in world units)
	# sensor density of nebula(value to scale sensor range by)
 	# name of internal texture (needs alpha)
	# name of external texture (no need for alpha)
	
	pNebula = App.MetaNebula_Create(60.0 / 255.0, 90.0 / 255.0, 185.0  / 255.0, 170.0, 10.5, "data/Backgrounds/nebulaoverlaybz1.tga", "data/Backgrounds/nebulaexternalbz1.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula.SetupDamage(10.0, 75.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula.AddNebulaSphere(-400, 3501.0, 1000.0, 560.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula, "Nebula1")

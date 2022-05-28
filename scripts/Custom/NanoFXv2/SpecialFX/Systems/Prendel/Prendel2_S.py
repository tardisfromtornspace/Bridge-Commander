###############################################################################
#	Filename:	Prendel1_S.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games
#	
#	Creates Prendel 1 static objects.  Called by Prendel1.py when region is created
#	
#	Created:	10/02/01 - Tony Evans (Added Header)
#	Modified:	10/04/01 - Tony Evans
###############################################################################
import App
import Tactical.LensFlares

def Initialize(pSet):
	# Add a sun, far far away
	pSun = App.Sun_Create(3000.0, 3000, 500, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresYellow.tga")
	pSet.AddObjectToSet(pSun, "Sun")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Builds a Yellow lens flare, attached to the sun
	Tactical.LensFlares.YellowLensFlare(pSet, pSun)

	#Blue White Planet
	pPlanet = App.Planet_Create(180.0, "data/models/environment/BrownPlanet.nif")
	pSet.AddObjectToSet(pPlanet, "Prendel 2")

	# Place the object at the specified location.
	pPlanet.PlaceObjectByName( "Planet" )
	pPlanet.UpdateNodeOnly()

	import Custom.NanoFXv2.NanoFX_Lib
	Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/models/environment/BrownPlanet.nif", "Class-H")


###############################################################################
#	Filename:	Poseidon1_S.py
#
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#
#	Creates Poseidon 1 static objects.  
#	Called by Poseidon1.py when region is created
#
#	Created:	10/02/01 - Tony Evans
#	Modified:	10/04/01 - Tony Evans
###############################################################################
import App
import Tactical.LensFlares

def Initialize(pSet):

#	To create a colored sun:
#	pSun = App.Sun_Create(fRadius, fAtmosphereThickness, fDamagePerSec, fBaseTexture , fFlareTexture)
#
#	for fBaseTexture you can use:
#		data/Textures/SunBase.tga 
#		data/Textures/SunRed.tga
#		data/Textures/SunRedOrange.tga
#	for fFlareTexture you can use:
#		data/Textures/Effects/SunFlaresOrange.tga
#		data/Textures/Effects/SunFlaresRed.tga
#		data/Textures/Effects/SunFlaresRedOrange.tga

	# Add a sun, far far away
	pSun = App.Sun_Create(5000.0, 5000, 500)
	pSet.AddObjectToSet(pSun, "Sun")

	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Builds a Red-Orange lens flare, attached to the sun
	Tactical.LensFlares.YellowLensFlare(pSet, pSun)

	# Planet and placement for "Poseidon 1" in Poseidon1 set
	pPlanet = App.Planet_Create(90.0, "data/models/environment/moon.nif")
	pSet.AddObjectToSet(pPlanet, "Poseidon 1")

	#Place the object at the specified location.
	pPlanet.PlaceObjectByName("Planet Location")
	pPlanet.UpdateNodeOnly()

	import Custom.NanoFXv2.NanoFX_Lib
	Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/models/environment/moon.nif", "Class-M")


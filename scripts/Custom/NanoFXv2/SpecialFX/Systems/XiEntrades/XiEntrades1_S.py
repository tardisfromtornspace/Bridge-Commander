###############################################################################
#	Filename:	XiEntrades1_S.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games
#	
#	Creates Xi Entrades 1 static objects.  Called by XiEntrades1.py when region is created
#	
#	Created:	10/02/01 - Tony Evans (Added Header)
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
	pSun = App.Sun_Create(7000.0, 7000, 500, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresRedOrange.tga")
	pSet.AddObjectToSet(pSun, "Sun")

	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Builds a Red-Orange lens flare, attached to the sun
	Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun)

	# Blue White Planet
	pPlanet = App.Planet_Create(150.0, "data/models/environment/DryPlanet.nif")
	pSet.AddObjectToSet(pPlanet, "Xi Entrades 1")

	# Place the object at the specified location.
	pPlanet.PlaceObjectByName( "Planet" )
	pPlanet.UpdateNodeOnly()

	import Custom.NanoFXv2.NanoFX_Lib
	Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/models/environment/dryplanet.nif", "Class-K")
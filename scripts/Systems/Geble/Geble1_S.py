###############################################################################
#	Filename:	Geble1_S.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games
#	
#	Creates Geble 1 static objects.  Called by Geble1.py when region is created
#	
#	Created:	09/24/01 - Ben Schulson
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
	pSun = App.Sun_Create(4000.0, 4000, 500, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresYellow.tga")
	pSet.AddObjectToSet(pSun, "Sun")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Builds a Yellow lens flare, attached to the sun
	Tactical.LensFlares.YellowLensFlare(pSet, pSun)

	# Model and placement for Geble 1 in Geble1 set
	pPlanet = App.Planet_Create(90.0, "data/models/environment/dryplanet.nif")
	pSet.AddObjectToSet(pPlanet, "Geble 1")

	#Place the object at the specified location.
	pPlanet.PlaceObjectByName("Planet Location")
	pPlanet.UpdateNodeOnly()

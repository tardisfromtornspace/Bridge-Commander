###############################################################################
#	Filename:	Cardassia1_S.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games
#	
#	Creates Cardassia 1 static objects.  Called by Cardassia1.py when region is created
#	
#	Created:	10/04/01 - Tony Evans (Added Header)
#	Modified:	08/11/04 - Klaus Kann
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
	pSun = App.Sun_Create(240000.0, 45000.0, 500, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun, "Sun")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Builds a Red-Orange lens flare, attached to the sun
	Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun)
	
	######
	# Create the Planet
	pCardassia1 = App.Planet_Create(278.80, "data/models/environment/EClass1.nif")
	pSet.AddObjectToSet(pCardassia1, "Cardassia 1") # Klasse B

	# Place the object at the specified location.
	pCardassia1.PlaceObjectByName( "Cardassia-1" )
	pCardassia1.SetAtmosphereRadius(0.001)	
	pCardassia1.UpdateNodeOnly()
	
#        try:    
#                import Custom.NanoFXv2.NanoFX_Lib
#                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia1, "data/models/environment/EClass1.nif", "Class-B")        
#        except ImportError:
#                # Couldn't find NanoFx2.  That's ok.  Do nothing...
#                pass  	

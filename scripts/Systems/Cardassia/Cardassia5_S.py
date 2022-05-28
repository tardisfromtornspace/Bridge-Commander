###############################################################################
#	Filename:	Cardassia5_S.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games
#	
#	Creates Cardassia 5 static objects.  Called by Cardassia5.py when region is created
#	
#	Created:	10/04/01 - Tony Evans (Added Header)
#	Modified:	08/11/04 - Klaus Kann
###############################################################################
import App
import Tactical.LensFlares

def Initialize(pSet):

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
	pCardassia5 = App.Planet_Create(800.0, "data/models/environment/SlimeGreenPlanet.nif")
	pSet.AddObjectToSet(pCardassia5, "Cardassia 5 / Minor") # Klasse M
	
	# Place the object at the specified location.
	pCardassia5.PlaceObjectByName( "Cardassia-5" )
	pCardassia5.SetAtmosphereRadius(0.01)
	pCardassia5.UpdateNodeOnly()

        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia5, "data/models/environment/SlimeGreenPlanet.nif", "Class-M")        
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
                pass  	
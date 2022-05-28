###############################################################################
#	Filename:	Cardassia6_S.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games
#	
#	Creates Cardassia 6 static objects.  Called by Cardassia6.py when region is created
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
	pCardassia6 = App.Planet_Create(728.91, "data/models/environment/GreenPlanet.nif")
	pSet.AddObjectToSet(pCardassia6, "Cardassia 6 / Prime") # Klasse M

	# Place the object at the specified location.
	pCardassia6.PlaceObjectByName( "Cardassia-6" )
	pCardassia6.SetAtmosphereRadius(0.005)
	pCardassia6.UpdateNodeOnly()
	
        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia6, "data/models/environment/GreenPlanet.nif", "Class-M")        
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
                pass  	
	
	######
	# Create the Planet
	pCardassiaMoon = App.Planet_Create(198.57, "data/models/environment/SlimeGreenPlanet.nif")
	pSet.AddObjectToSet(pCardassiaMoon, "Cardassia Prime Moon")

	# Place the object at the specified location.
	pCardassiaMoon.PlaceObjectByName( "Moon" )
	pCardassiaMoon.SetAtmosphereRadius(0.005)
	pCardassiaMoon.UpdateNodeOnly()
		
        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassiaMoon, "data/models/environment/SlimeGreenPlanet.nif", "Class-M")        
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
                pass  	
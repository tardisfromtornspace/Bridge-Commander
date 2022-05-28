# unused System
################################################################################
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
	
	######
	# Create the Planet
	pCardassia2 = App.Planet_Create(278.0, "data/models/environment/Io.nif")
	pSet.AddObjectToSet(pCardassia2, "Cardassia 2") # Klasse B

	# Place the object at the specified location.
	pCardassia2.PlaceObjectByName( "Cardassia-2" )
	pCardassia2.SetAtmosphereRadius(0.001)	
	pCardassia2.UpdateNodeOnly()
	
	######
	# Create the Planet
	pCardassia3 = App.Planet_Create(388.23, "data/models/environment/FClass1.nif")
	pSet.AddObjectToSet(pCardassia3, "Cardassia 3") # Klasse M

	# Place the object at the specified location.
	pCardassia3.PlaceObjectByName( "Cardassia-3" )
	pCardassia3.SetAtmosphereRadius(0.01)
	pCardassia3.UpdateNodeOnly()

        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia3, "data/models/environment/FClass1.nif", "Class-M")        
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
                pass 
                
	######
	# Create the Planet
	pCardassia4 = App.Planet_Create(728.91, "data/models/environment/YClass1.nif")
	pSet.AddObjectToSet(pCardassia4, "Cardassia 4 / Hutel") # Klasse M

	# Place the object at the specified location.
	pCardassia4.PlaceObjectByName( "Cardassia-4" )
	pCardassia4.SetAtmosphereRadius(0.01)
	pCardassia4.UpdateNodeOnly()

        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia4, "data/models/environment/YClass1.nif", "Class-M")        
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
                pass  	
                
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
                
	######
	# Create the Planet
	pCardassia7 = App.Planet_Create(388.23, "data/models/environment/Mercury.nif")
	pSet.AddObjectToSet(pCardassia7, "Cardassia 7") # Klasse Q

	# Place the object at the specified location.
	pCardassia7.PlaceObjectByName( "Cardassia-7" )
	pCardassia7.UpdateNodeOnly()
	
	######
	# Create the Planet
	pCardassia8 = App.Planet_Create(7347.745, "data/models/environment/Saturn.nif")
	pSet.AddObjectToSet(pCardassia8, "Cardassia 8") # Klasse I
	
	# Place the object at the specified location.
	pCardassia8.PlaceObjectByName( "Cardassia-8" )
	pCardassia8.SetAtmosphereRadius(0.01)
	pCardassia8.UpdateNodeOnly()

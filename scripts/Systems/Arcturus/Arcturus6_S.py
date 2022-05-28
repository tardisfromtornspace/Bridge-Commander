import App
import Tactical.LensFlares

def Initialize(pSet):

	# Sun 1
	pSun = App.Sun_Create(8000.00, 8050.0, 8100.0, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresYellow.tga")
	pSet.AddObjectToSet(pSun, "Sun")

	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Builds a Red-Orange lens flare, attached to the sun
	Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun)

	# Sun2
	pSun2 = App.Sun_Create(2400.0, 2450, 2500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun2, "Sun2")
	
	# Place the object at the specified location.
	pSun2.PlaceObjectByName( "Sun2" )
	pSun2.UpdateNodeOnly()

	pPlanet = App.Planet_Create(4320.0, "data/models/environment/Neptune.NIF")
	pSet.AddObjectToSet(pPlanet, "Arcturus 6")

	pPlanet.PlaceObjectByName("Planet Location")
	pPlanet.UpdateNodeOnly()
	
        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/models/environment/Neptune.NIF", "Class-J")        
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
                pass    
	

	pMoon1 = App.Planet_Create(133.0, "data/models/environment/RockyPlanet.NIF")
	pSet.AddObjectToSet(pMoon1, "Arcturus 6, Moon 1")
	
	pMoon1.PlaceObjectByName("Moon1")
	pMoon1.UpdateNodeOnly()
	
        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/models/environment/RockyPlanet.NIF", "Class-C")        
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
                pass  	
	

	pMoon2 = App.Planet_Create(145.0, "data/models/environment/TurquoisePlanet.NIF")
	pSet.AddObjectToSet(pMoon2, "Arcturus 6, Moon 2(Class C)")

	pMoon2.PlaceObjectByName("Moon2")
	pMoon2.UpdateNodeOnly()
	
        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/models/environment/TurquoisPlanetabort.NIF", "Class-C")        
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
                pass  	
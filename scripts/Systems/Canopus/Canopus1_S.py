import App
import Tactical.LensFlares

def Initialize(pSet):

	# Sun1
	pSun = App.Sun_Create(15500.0, 16000, 16500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun, "Sun")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Builds a Blue lens flare for Sun 1
	Tactical.LensFlares.BlueGlareSuperBright(pSet, pSun)

	pPlanet = App.Planet_Create(8090.0, "data/models/environment/JClass4.NIF")
	pSet.AddObjectToSet(pPlanet, "Canopus 1")

	pPlanet.PlaceObjectByName("Planet1")
	pPlanet.UpdateNodeOnly()
	
        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/models/environment/JClass4.NIF", "Class-J")        
        except ImportError:
                # If NanoFx2 not installed..  That's ok.  Do nothing...
                pass  	

	pMoon = App.Planet_Create(60.0, "data/models/environment/FClass1.NIF")
	pSet.AddObjectToSet(pMoon, "Canopus 1 Moon 1(Class F)")

	pMoon.PlaceObjectByName("Moon1")
	pMoon.UpdateNodeOnly()
	
        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/models/environment/FClass1.NIF", "Class-F")        
        except ImportError:
                # If NanoFx2 not installed..  That's ok.  Do nothing...
                pass 	

	pMoon2 = App.Planet_Create(28.0, "data/models/environment/asteroidh3.NIF")
	pSet.AddObjectToSet(pMoon2, "Canopus 1 Moon 2(Class D)")

	pMoon2.PlaceObjectByName("Moon2")
	pMoon2.UpdateNodeOnly()
	
	
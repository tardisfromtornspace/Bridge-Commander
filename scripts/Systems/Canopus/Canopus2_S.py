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
	Tactical.LensFlares.BlueGlareBright(pSet, pSun)

	pPlanet = App.Planet_Create(4090.0, "data/models/environment/JClass3.NIF")
	pSet.AddObjectToSet(pPlanet, "Canopus 2 (Class J)")

	pPlanet.PlaceObjectByName("Planet1")
	pPlanet.UpdateNodeOnly()

	pMoon = App.Planet_Create(83.0, "data/models/environment/Moon.NIF")
	pSet.AddObjectToSet(pMoon, "Canopus 2 Moon 1(Class D)")

	pMoon.PlaceObjectByName("Moon1")
	pMoon.UpdateNodeOnly()

	pMoon2 = App.Planet_Create(48.0, "data/models/environment/SulphuricPlanetZM1.NIF")
	pSet.AddObjectToSet(pMoon2, "Canopus 2 Moon 2(Class N)")

	pMoon2.PlaceObjectByName("Moon2")
	pMoon2.UpdateNodeOnly()

	pMoon3 = App.Planet_Create(39.0, "data/models/environment/Titania.NIF")
	pSet.AddObjectToSet(pMoon3, "Canopus 2 Moon 3(Class D)")

	pMoon3.PlaceObjectByName("Moon3")
	pMoon3.UpdateNodeOnly()
	
	try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/models/environment/JClass3.NIF", "Class-K")        
	except ImportError:
		# Couldn't find NanoFx2.  That's ok.  Do nothing...
	        pass 
	        
	try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pMoon, "data/models/environment/Moon.NIF", "Class-H")        
	except ImportError:
		# Couldn't find NanoFx2.  That's ok.  Do nothing...
	        pass	        
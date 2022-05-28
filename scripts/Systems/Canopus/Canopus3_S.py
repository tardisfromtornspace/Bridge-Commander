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
	Tactical.LensFlares.DimBlueFlares(pSet, pSun)

	pPlanet = App.Planet_Create(1075.0, "data/models/environment/EClass2Rings.NIF")
	pSet.AddObjectToSet(pPlanet, "Canopus 3 (Class E)")

	pPlanet.PlaceObjectByName("Planet1")
	pPlanet.UpdateNodeOnly()

	pMoon1 = App.Planet_Create(75.0, "data/models/environment/Rhea.NIF")
	pSet.AddObjectToSet(pMoon1, "Canopus 3, Moon1 (Class D)")

	pMoon1.PlaceObjectByName("Moon1")
	pMoon1.UpdateNodeOnly()

	pMoon2 = App.Planet_Create(55.0, "data/models/environment/SnowPlanet.NIF")
	pSet.AddObjectToSet(pMoon2, "Canopus 3, Moon2 (Class P)")

	pMoon2.PlaceObjectByName("Moon2")
	pMoon2.UpdateNodeOnly()
	
	try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/models/environment/EClass2Rings.NIF", "Class-K")        
	except ImportError:
		# Couldn't find NanoFx2.  That's ok.  Do nothing...
	        pass 	
	
	

import App
import Tactical.LensFlares

def Initialize(pSet):

	# Sun 1
	pSun = App.Sun_Create(8000.00, 8100.0, 8150.0, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresYellow.tga")
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
	
	pPlanet = App.Planet_Create(7805.0, "data/models/environment/JClass2.NIF")
	pSet.AddObjectToSet(pPlanet, "Arcturus 5")
	
        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/models/environment/JClass2.NIF", "Class-J")        
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
                pass    
	

	pPlanet.PlaceObjectByName("Planet Location")
	pPlanet.UpdateNodeOnly()

	pMoon1 = App.Planet_Create(133.0, "data/models/environment/NClass1.NIF")
	pSet.AddObjectToSet(pMoon1, "Arcturus 5, Moon 1")
	
        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pMoon1, "data/models/environment/NClass1.NIF", "Class-N")        
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
                pass 	

	pMoon1.PlaceObjectByName("Moon1")
	pMoon1.UpdateNodeOnly()

	pMoon2 = App.Planet_Create(145.0, "data/models/environment/Europa.NIF")
	pSet.AddObjectToSet(pMoon2, "Arcturus 5, Moon 2(Class P)")
	
        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pMoon2, "data/models/environment/Europa.NIF", "Class-P")        
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
                pass    
	

	pMoon2.PlaceObjectByName("Moon2")
	pMoon2.UpdateNodeOnly()

	pMoon3 = App.Planet_Create(82.0, "data/models/environment/Callisto.NIF")
	pSet.AddObjectToSet(pMoon3, "Arcturus 5, Moon 3(Class L)")

	pMoon3.PlaceObjectByName("Moon3")
	pMoon3.UpdateNodeOnly()

	pMoon4 = App.Planet_Create(57.0, "data/models/environment/Ganymede.NIF")
	pSet.AddObjectToSet(pMoon4, "Arcturus 5, Moon 4(Class L)")

	pMoon4.PlaceObjectByName("Moon4")
	pMoon4.UpdateNodeOnly()

	pMoon5 = App.Planet_Create(41.0, "data/models/environment/PClass1.NIF")
	pSet.AddObjectToSet(pMoon5, "Arcturus 5, Moon 5(Class P)")

	pMoon5.PlaceObjectByName("Moon5")
	pMoon5.UpdateNodeOnly()

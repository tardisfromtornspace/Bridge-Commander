import App
import Tactical.LensFlares

def Initialize(pSet):

	# Sun 1
	pSun = App.Sun_Create(8000.00, 8200.0, 8250.0, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresYellow.tga")
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

	pPlanet = App.Planet_Create(92.0, "data/models/environment/NClass2.NIF")
	pSet.AddObjectToSet(pPlanet, "Arcturus 3 (Class N)")

	pPlanet.PlaceObjectByName("Planet Location")
	pPlanet.UpdateNodeOnly()
	
        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/models/environment/NClass2.nif", "N-Class 2")        
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
                pass 	

	pMoon1 = App.Planet_Create(32.0, "data/models/environment/RedPlanet.NIF")
	pSet.AddObjectToSet(pMoon1, "Arcturus 3, Moon 1(Class K)")
	
        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pMoon1, "data/models/environment/RedPlanet.NIF", "Class-K")        
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
                pass 	
	

	pMoon1.PlaceObjectByName("Moon1")
	pMoon1.UpdateNodeOnly()

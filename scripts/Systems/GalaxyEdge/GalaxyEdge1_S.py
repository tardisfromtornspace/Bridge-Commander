# NanoFx2 Atmospheres added 4/4/04 by Chris Jones. Class E Swirling Gas texture by Ken Jones

import App
import Tactical.LensFlares

def Initialize(pSet):

	# Sun1
	pSun = App.Sun_Create(2000.0, 2200, 2500, "data/Textures/SunBlack.tga", "data/Textures/Effects/SunFlaresBlack.tga")
	pSet.AddObjectToSet(pSun, "Sun")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

        # Builds a Black lens flare for this Sun
	Tactical.LensFlares.BlackFlares(pSet, pSun)

	# Sun2
	pSun2 = App.Sun_Create(2000.0, 2200, 2500, "data/Textures/SunBlack.tga", "data/Textures/Effects/SunFlaresBlack.tga")
	pSet.AddObjectToSet(pSun2, "Sun2")
	
	# Place the object at the specified location.
	pSun2.PlaceObjectByName( "Sun2" )
	pSun2.UpdateNodeOnly()

        # Builds a Black lens flare for this Sun
	Tactical.LensFlares.BlackFlares(pSet, pSun2)

	# Sun3
	pSun3 = App.Sun_Create(2000.0, 2200, 2500, "data/Textures/SunBlack.tga", "data/Textures/Effects/SunFlaresBlack.tga")
	pSet.AddObjectToSet(pSun3, "Sun3")
	
	# Place the object at the specified location.
	pSun3.PlaceObjectByName( "Sun3" )
	pSun3.UpdateNodeOnly()

        # Builds a Black lens flare for this Sun
	Tactical.LensFlares.BlackFlares(pSet, pSun3)

	# Sun4
	pSun4 = App.Sun_Create(12000.0, 16000, 17000, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun4, "Sun4")
	
	# Place the object at the specified location.
	pSun4.PlaceObjectByName( "Sun4" )
	pSun4.UpdateNodeOnly()

	# Builds a Blue lens flare for this Sun
	Tactical.LensFlares.DimBlueFlares(pSet, pSun4)

	# Sun5
	pSun5 = App.Sun_Create(4750.0, 4825, 9000, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresYellow.tga")
	pSet.AddObjectToSet(pSun5, "Sun5")
	
	# Place the object at the specified location.
	pSun5.PlaceObjectByName( "Sun5" )
	pSun5.UpdateNodeOnly()

        # Builds a Yellow lens flare for this Sun
	Tactical.LensFlares.YellowLensFlare(pSet, pSun5)

	# Sun6
	pSun6 = App.Sun_Create(11000.0, 11250, 11300, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun6, "Sun6")
	
	# Place the object at the specified location.
	pSun6.PlaceObjectByName( "Sun6" )
	pSun6.UpdateNodeOnly()

        # Sun7
	pSun7 = App.Sun_Create(215.0, 219, 220, "data/Textures/SunWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun7, "Sun7")
	
	# Place the object at the specified location.
	pSun7.PlaceObjectByName( "Sun7" )
	pSun7.UpdateNodeOnly()

        # Sun8
	pSun8 = App.Sun_Create(5000.0, 5500, 6000, "data/Textures/SunWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun8, "Sun8")
	
	# Place the object at the specified location.
	pSun8.PlaceObjectByName( "Sun8" )
	pSun8.UpdateNodeOnly()

	pPlanet = App.Planet_Create(140.0, "data/models/environment/MClass1.NIF")
	pSet.AddObjectToSet(pPlanet, "Unknown")

	pPlanet.PlaceObjectByName("Planet1")
	pPlanet.UpdateNodeOnly()
	
        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/models/environment/MClass1.NIF", "Class-M")        
        except ImportError:
                # If NanoFx2 not installed..  That's ok.  Do nothing...
                pass	

	pPlanet2 = App.Planet_Create(75.0, "data/models/environment/EClass1.NIF")
	pSet.AddObjectToSet(pPlanet2, "Uncharted")

	pPlanet2.PlaceObjectByName("Planet2")
	pPlanet2.UpdateNodeOnly()
	
        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/models/environment/EClass1.NIF", "Class-E")        
        except ImportError:
                # If NanoFx2 not installed..  That's ok.  Do nothing...
                pass	
	
import App
import Tactical.LensFlares

def Initialize(pSet):

        # Sun1
        pSun = App.Sun_Create(19500.0, 20000, 22500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
        pSet.AddObjectToSet(pSun, "Sun")
        
        # Place the object at the specified location.
        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        # Builds a Blue lens flare for Sun 1
        Tactical.LensFlares.DimBlueFlares(pSet, pSun)

        pPlanet = App.Planet_Create(275.0, "data/models/environment/AquaPlanet.NIF")
        pSet.AddObjectToSet(pPlanet, "Hakares 1")       

        pPlanet.PlaceObjectByName("Planet1")
        pPlanet.UpdateNodeOnly()
        
        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/models/environment/AquaPlanet.NIF", "Class-O")        
        except ImportError:
                # If NanoFx2 is not installed.  That's ok.  Do nothing...
                pass    

        pMoon1 = App.Planet_Create(75.0, "data/models/environment/BrownPlanet.NIF")
        pSet.AddObjectToSet(pMoon1, "Moon 1")

        pMoon1.PlaceObjectByName("Moon1")
        pMoon1.UpdateNodeOnly()
        
        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pMoon1, "data/models/environment/BrownPlanet.NIF", "Class-D")        
        except ImportError:
                # If NanoFx2 is not installed.  That's ok.  Do nothing...
                pass    

        pMoon2 = App.Planet_Create(55.0, "data/models/environment/SlimeGreenPlanet.NIF")
        pSet.AddObjectToSet(pMoon2, "Moon 2")
        

        pMoon2.PlaceObjectByName("Moon2")
        pMoon2.UpdateNodeOnly()
        
        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pMoon2, "data/models/environment/SlimeGreenPlanet.NIF", "N-Class 2")        
        except ImportError:
                # If NanoFx2 is not installed.  That's ok.  Do nothing...
                pass    

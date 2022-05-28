# by Sov

import App
import MissionLib
import Tactical.LensFlares
from Custom.DS9FX import DS9FXmain
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig
from Custom.DS9FX.DS9FXSunStreak import SunStreak

def Initialize(pSet):
        from Custom.DS9FX.DS9FXObjects import NewBajorShips

        NewBajorShips.NewBajorSetShips()
        
        pSun = App.Sun_Create(3725.0, 3725.0, 3725, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
        pSet.AddObjectToSet(pSun, "New Bajor Sun")

        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun)
        SunStreak.Create(pSet, "SunStr", 75000.0, "Red", "2")
        
        reload(DS9FXSavedConfig)
        if DS9FXSavedConfig.NewBajorMapPlanetDetail == 3:
                if DS9FXSavedConfig.NewBajorPlanets == 1:
                        pPlanet = App.Planet_Create(200.0, "data/Models/Environment/DS9FX/HighRes/Planet004.nif")
                        pSet.AddObjectToSet(pPlanet, "New Bajor 1")

                        pPlanet.PlaceObjectByName("Planet1")
                        pPlanet.UpdateNodeOnly()

                        pPlanet2 = App.Planet_Create(80.0, "data/Models/Environment/DS9FX/HighRes/NewBajor.nif")
                        pSet.AddObjectToSet(pPlanet2, "New Bajor Colony")

                        pPlanet2.PlaceObjectByName("Planet2")
                        pPlanet2.UpdateNodeOnly()

                        pPlanet3 = App.Planet_Create(110.0, "data/Models/Environment/DS9FX/HighRes/Planet004.nif")
                        pSet.AddObjectToSet(pPlanet3, "New Bajor 3")

                        pPlanet3.PlaceObjectByName("Planet3")
                        pPlanet3.UpdateNodeOnly()

                        pPlanet4 = App.Planet_Create(275.0, "data/Models/Environment/DS9FX/HighRes/Gamma1High.nif")
                        pSet.AddObjectToSet(pPlanet4, "New Bajor 4")

                        pPlanet4.PlaceObjectByName("Planet4")
                        pPlanet4.UpdateNodeOnly()

                        if DS9FXSavedConfig.NewBajorNanoFX == 1:
                                try:
                                        import Custom.NanoFXv2.NanoFX_Lib
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/HighRes/Planet004.nif", "Class-O")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/HighRes/NewBajor.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/HighRes/Planet004.nif", "Class-O")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/HighRes/Gamma1High.nif", "Class-H")
                                except:
                                        print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

        elif DS9FXSavedConfig.NewBajorMapPlanetDetail == 2:
                if DS9FXSavedConfig.NewBajorPlanets == 1:
                        pPlanet = App.Planet_Create(200.0, "data/Models/Environment/DS9FX/StandardRes/Planet004.nif")
                        pSet.AddObjectToSet(pPlanet, "New Bajor 1")

                        pPlanet.PlaceObjectByName("Planet1")
                        pPlanet.UpdateNodeOnly()

                        pPlanet2 = App.Planet_Create(80.0, "data/Models/Environment/DS9FX/StandardRes/NewBajor.nif")
                        pSet.AddObjectToSet(pPlanet2, "New Bajor Colony")

                        pPlanet2.PlaceObjectByName("Planet2")
                        pPlanet2.UpdateNodeOnly()

                        pPlanet3 = App.Planet_Create(110.0, "data/Models/Environment/DS9FX/StandardRes/Planet004.nif")
                        pSet.AddObjectToSet(pPlanet3, "New Bajor 3")

                        pPlanet3.PlaceObjectByName("Planet3")
                        pPlanet3.UpdateNodeOnly()

                        pPlanet4 = App.Planet_Create(275.0, "data/Models/Environment/DS9FX/StandardRes/Gamma1High.nif")
                        pSet.AddObjectToSet(pPlanet4, "New Bajor 4")

                        pPlanet4.PlaceObjectByName("Planet4")
                        pPlanet4.UpdateNodeOnly()

                        if DS9FXSavedConfig.NewBajorNanoFX == 1:
                                try:
                                        import Custom.NanoFXv2.NanoFX_Lib
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/StandardRes/Planet004.nif", "Class-O")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/StandardRes/NewBajor.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/StandardRes/Planet004.nif", "Class-O")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/StandardRes/Gamma1High.nif", "Class-H")
                                except:
                                        print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

        elif DS9FXSavedConfig.NewBajorMapPlanetDetail == 1:
                if DS9FXSavedConfig.NewBajorPlanets == 1:
                        pPlanet = App.Planet_Create(200.0, "data/Models/Environment/DS9FX/LowRes/Planet004.nif")
                        pSet.AddObjectToSet(pPlanet, "New Bajor 1")

                        pPlanet.PlaceObjectByName("Planet1")
                        pPlanet.UpdateNodeOnly()

                        pPlanet2 = App.Planet_Create(80.0, "data/Models/Environment/DS9FX/LowRes/NewBajor.nif")
                        pSet.AddObjectToSet(pPlanet2, "New Bajor Colony")

                        pPlanet2.PlaceObjectByName("Planet2")
                        pPlanet2.UpdateNodeOnly()

                        pPlanet3 = App.Planet_Create(110.0, "data/Models/Environment/DS9FX/LowRes/Planet004.nif")
                        pSet.AddObjectToSet(pPlanet3, "New Bajor 3")

                        pPlanet3.PlaceObjectByName("Planet3")
                        pPlanet3.UpdateNodeOnly()

                        pPlanet4 = App.Planet_Create(275.0, "data/Models/Environment/DS9FX/LowRes/Gamma1High.nif")
                        pSet.AddObjectToSet(pPlanet4, "New Bajor 4")

                        pPlanet4.PlaceObjectByName("Planet4")
                        pPlanet4.UpdateNodeOnly()

                        if DS9FXSavedConfig.NewBajorNanoFX == 1:
                                try:
                                        import Custom.NanoFXv2.NanoFX_Lib
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/LowRes/Planet004.nif", "Class-O")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/LowRes/NewBajor.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/LowRes/Planet004.nif", "Class-O")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/LowRes/Gamma1High.nif", "Class-H")
                                except:
                                        print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

        else:
                if DS9FXSavedConfig.NewBajorPlanets == 1:
                        pPlanet = App.Planet_Create(200.0, "data/Models/Environment/DS9FX/LowestRes/Planet004.nif")
                        pSet.AddObjectToSet(pPlanet, "New Bajor 1")

                        pPlanet.PlaceObjectByName("Planet1")
                        pPlanet.UpdateNodeOnly()

                        pPlanet2 = App.Planet_Create(80.0, "data/Models/Environment/DS9FX/LowestRes/NewBajor.nif")
                        pSet.AddObjectToSet(pPlanet2, "New Bajor Colony")

                        pPlanet2.PlaceObjectByName("Planet2")
                        pPlanet2.UpdateNodeOnly()

                        pPlanet3 = App.Planet_Create(110.0, "data/Models/Environment/DS9FX/LowestRes/Planet004.nif")
                        pSet.AddObjectToSet(pPlanet3, "New Bajor 3")

                        pPlanet3.PlaceObjectByName("Planet3")
                        pPlanet3.UpdateNodeOnly()

                        pPlanet4 = App.Planet_Create(275.0, "data/Models/Environment/DS9FX/LowestRes/Gamma1High.nif")
                        pSet.AddObjectToSet(pPlanet4, "New Bajor 4")

                        pPlanet4.PlaceObjectByName("Planet4")
                        pPlanet4.UpdateNodeOnly()

                        if DS9FXSavedConfig.NewBajorNanoFX == 1:
                                try:
                                        import Custom.NanoFXv2.NanoFX_Lib
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/LowestRes/Planet004.nif", "Class-O")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/LowestRes/NewBajor.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/LowestRes/Planet004.nif", "Class-O")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/LowestRes/Gamma1High.nif", "Class-H")
                                except:
                                        print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

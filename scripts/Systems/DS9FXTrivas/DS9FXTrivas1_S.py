import App
import MissionLib
import Tactical.LensFlares
from Custom.DS9FX import DS9FXmain
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig
from Custom.DS9FX.DS9FXSunStreak import SunStreak

def Initialize(pSet):
        pSun = App.Sun_Create(4000.0, 4000.0, 4000, "data/Textures/SunDrkBlue.tga", "data/Textures/Effects/SunFlaresBlue.tga")
        pSet.AddObjectToSet(pSun, "Trivas Sun")

        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        Tactical.LensFlares.BlueLensFlare(pSet, pSun, 1, 0.35, 0.35)
        SunStreak.Create(pSet, "SunStr", 70000.0, "DarkBlue", "2")

        reload(DS9FXSavedConfig)
        if DS9FXSavedConfig.TrivasMapPlanetDetail == 3:
                if DS9FXSavedConfig.TrivasPlanets == 1:
                        pTrivas1 = App.Planet_Create(90.0, "data/models/environment/DS9FX/HighRes/Planet002.nif")
                        pSet.AddObjectToSet(pTrivas1, "Trivas 1")

                        pTrivas1.PlaceObjectByName( "Trivas 1" )
                        pTrivas1.UpdateNodeOnly()

                        pTrivas2 = App.Planet_Create(60.0, "data/models/environment/DS9FX/HighRes/Planet004.nif")
                        pSet.AddObjectToSet(pTrivas2, "Trivas 2")

                        pTrivas2.PlaceObjectByName( "Trivas 2" )
                        pTrivas2.UpdateNodeOnly()

                        pTrivas3 = App.Planet_Create(120.0, "data/models/environment/DS9FX/HighRes/Planet001.nif")
                        pSet.AddObjectToSet(pTrivas3, "Trivas 3")

                        pTrivas3.PlaceObjectByName( "Trivas 3" )
                        pTrivas3.UpdateNodeOnly()

                        pTrivas4 = App.Planet_Create(110.0, "data/models/environment/DS9FX/HighRes/Planet006.nif")
                        pSet.AddObjectToSet(pTrivas4, "Trivas 4")

                        pTrivas4.PlaceObjectByName( "Trivas 4" )
                        pTrivas4.UpdateNodeOnly()

                        if DS9FXSavedConfig.TrivasNanoFX == 1:
                                try:
                                        import Custom.NanoFXv2.NanoFX_Lib
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pTrivas1, "data/models/environment/DS9FX/HighRes/Planet002.nif", "Class-K")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pTrivas2, "data/models/environment/DS9FX/HighRes/Planet004.nif", "Class-H")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pTrivas3, "data/models/environment/DS9FX/HighRes/Planet001.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pTrivas4, "data/models/environment/DS9FX/HighRes/Planet006.nif", "Class-M")
                                except:
                                        print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"      			

        elif DS9FXSavedConfig.TrivasMapPlanetDetail == 2:
                if DS9FXSavedConfig.TrivasPlanets == 1:
                        pTrivas1 = App.Planet_Create(90.0, "data/models/environment/DS9FX/StandardRes/Planet002.nif")
                        pSet.AddObjectToSet(pTrivas1, "Trivas 1")

                        pTrivas1.PlaceObjectByName( "Trivas 1" )
                        pTrivas1.UpdateNodeOnly()

                        pTrivas2 = App.Planet_Create(60.0, "data/models/environment/DS9FX/StandardRes/Planet004.nif")
                        pSet.AddObjectToSet(pTrivas2, "Trivas 2")

                        pTrivas2.PlaceObjectByName( "Trivas 2" )
                        pTrivas2.UpdateNodeOnly()

                        pTrivas3 = App.Planet_Create(120.0, "data/models/environment/DS9FX/StandardRes/Planet001.nif")
                        pSet.AddObjectToSet(pTrivas3, "Trivas 3")

                        pTrivas3.PlaceObjectByName( "Trivas 3" )
                        pTrivas3.UpdateNodeOnly()

                        pTrivas4 = App.Planet_Create(110.0, "data/models/environment/DS9FX/StandardRes/Planet006.nif")
                        pSet.AddObjectToSet(pTrivas4, "Trivas 4")

                        pTrivas4.PlaceObjectByName( "Trivas 4" )
                        pTrivas4.UpdateNodeOnly()

                        if DS9FXSavedConfig.TrivasNanoFX == 1:
                                try:
                                        import Custom.NanoFXv2.NanoFX_Lib
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pTrivas1, "data/models/environment/DS9FX/StandardRes/Planet002.nif", "Class-K")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pTrivas2, "data/models/environment/DS9FX/StandardRes/Planet004.nif", "Class-H")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pTrivas3, "data/models/environment/DS9FX/StandardRes/Planet001.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pTrivas4, "data/models/environment/DS9FX/StandardRes/Planet006.nif", "Class-M")
                                except:
                                        print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!" 

        elif DS9FXSavedConfig.TrivasMapPlanetDetail == 1:
                if DS9FXSavedConfig.TrivasPlanets == 1:
                        pTrivas1 = App.Planet_Create(90.0, "data/models/environment/DS9FX/LowRes/Planet002.nif")
                        pSet.AddObjectToSet(pTrivas1, "Trivas 1")

                        pTrivas1.PlaceObjectByName( "Trivas 1" )
                        pTrivas1.UpdateNodeOnly()

                        pTrivas2 = App.Planet_Create(60.0, "data/models/environment/DS9FX/LowRes/Planet004.nif")
                        pSet.AddObjectToSet(pTrivas2, "Trivas 2")

                        pTrivas2.PlaceObjectByName( "Trivas 2" )
                        pTrivas2.UpdateNodeOnly()

                        pTrivas3 = App.Planet_Create(120.0, "data/models/environment/DS9FX/LowRes/Planet001.nif")
                        pSet.AddObjectToSet(pTrivas3, "Trivas 3")

                        pTrivas3.PlaceObjectByName( "Trivas 3" )
                        pTrivas3.UpdateNodeOnly()

                        pTrivas4 = App.Planet_Create(110.0, "data/models/environment/DS9FX/LowRes/Planet006.nif")
                        pSet.AddObjectToSet(pTrivas4, "Trivas 4")

                        pTrivas4.PlaceObjectByName( "Trivas 4" )
                        pTrivas4.UpdateNodeOnly()

                        if DS9FXSavedConfig.TrivasNanoFX == 1:
                                try:
                                        import Custom.NanoFXv2.NanoFX_Lib
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pTrivas1, "data/models/environment/DS9FX/LowRes/Planet002.nif", "Class-K")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pTrivas2, "data/models/environment/DS9FX/LowRes/Planet004.nif", "Class-H")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pTrivas3, "data/models/environment/DS9FX/LowRes/Planet001.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pTrivas4, "data/models/environment/DS9FX/LowRes/Planet006.nif", "Class-M")
                                except:
                                        print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"        
        else:
                if DS9FXSavedConfig.TrivasPlanets == 1:
                        pTrivas1 = App.Planet_Create(90.0, "data/models/environment/DS9FX/LowestRes/Planet002.nif")
                        pSet.AddObjectToSet(pTrivas1, "Trivas 1")

                        pTrivas1.PlaceObjectByName( "Trivas 1" )
                        pTrivas1.UpdateNodeOnly()

                        pTrivas2 = App.Planet_Create(60.0, "data/models/environment/DS9FX/LowestRes/Planet004.nif")
                        pSet.AddObjectToSet(pTrivas2, "Trivas 2")

                        pTrivas2.PlaceObjectByName( "Trivas 2" )
                        pTrivas2.UpdateNodeOnly()

                        pTrivas3 = App.Planet_Create(120.0, "data/models/environment/DS9FX/LowestRes/Planet001.nif")
                        pSet.AddObjectToSet(pTrivas3, "Trivas 3")

                        pTrivas3.PlaceObjectByName( "Trivas 3" )
                        pTrivas3.UpdateNodeOnly()

                        pTrivas4 = App.Planet_Create(110.0, "data/models/environment/DS9FX/LowestRes/Planet006.nif")
                        pSet.AddObjectToSet(pTrivas4, "Trivas 4")

                        pTrivas4.PlaceObjectByName( "Trivas 4" )
                        pTrivas4.UpdateNodeOnly()

                        if DS9FXSavedConfig.TrivasNanoFX == 1:
                                try:
                                        import Custom.NanoFXv2.NanoFX_Lib
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pTrivas1, "data/models/environment/DS9FX/LowestRes/Planet002.nif", "Class-K")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pTrivas2, "data/models/environment/DS9FX/LowestRes/Planet004.nif", "Class-H")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pTrivas3, "data/models/environment/DS9FX/LowestRes/Planet001.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pTrivas4, "data/models/environment/DS9FX/LowestRes/Planet006.nif", "Class-M")
                                except:
                                        print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!" 

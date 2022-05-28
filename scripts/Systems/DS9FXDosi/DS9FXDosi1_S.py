# by Sov

import App
import MissionLib
import Tactical.LensFlares
from Custom.DS9FX import DS9FXmain
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig
from Custom.DS9FX.DS9FXSunStreak import SunStreak

def Initialize(pSet):   
    pSun = App.Sun_Create(3300.0, 3300.0, 3300.0, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresBlue.tga")
    pSet.AddObjectToSet(pSun, "Dosi Sun")
    
    pSun.PlaceObjectByName( "Sun" )
    pSun.UpdateNodeOnly()
    
    Tactical.LensFlares.BlueLensFlare(pSet, pSun)
    SunStreak.Create(pSet, "SunStr", 105000.0, "Blue", "4")
                    
    reload(DS9FXSavedConfig)
    if DS9FXSavedConfig.DosiMapPlanetDetail == 3:
        if DS9FXSavedConfig.DosiPlanets == 1:    
                    pPlanet3 = App.Planet_Create(88.0, "data/Models/Environment/DS9FX/HighRes/Planet003.nif")
                    pSet.AddObjectToSet(pPlanet3, "Dosi 1")

                    pPlanet3.PlaceObjectByName("Planet3")
                    pPlanet3.UpdateNodeOnly()

                    pPlanet2 = App.Planet_Create(105.0, "data/Models/Environment/DS9FX/HighRes/Planet001.nif")
                    pSet.AddObjectToSet(pPlanet2, "Dosi 2")

                    pPlanet2.PlaceObjectByName("Planet2")
                    pPlanet2.UpdateNodeOnly()

                    pPlanet = App.Planet_Create(65.0, "data/Models/Environment/DS9FX/HighRes/Dosi.nif")
                    pSet.AddObjectToSet(pPlanet, "Dosi Homeworld")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    if DS9FXSavedConfig.DosiNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/HighRes/Dosi.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/HighRes/Planet001.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/HighRes/Planet003.nif", "Class-O")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

    elif DS9FXSavedConfig.DosiMapPlanetDetail == 2:
        if DS9FXSavedConfig.DosiPlanets == 1:    
                    pPlanet3 = App.Planet_Create(88.0, "data/Models/Environment/DS9FX/StandardRes/Planet003.nif")
                    pSet.AddObjectToSet(pPlanet3, "Dosi 1")

                    pPlanet3.PlaceObjectByName("Planet3")
                    pPlanet3.UpdateNodeOnly()

                    pPlanet2 = App.Planet_Create(105.0, "data/Models/Environment/DS9FX/StandardRes/Planet001.nif")
                    pSet.AddObjectToSet(pPlanet2, "Dosi 2")

                    pPlanet2.PlaceObjectByName("Planet2")
                    pPlanet2.UpdateNodeOnly()

                    pPlanet = App.Planet_Create(65.0, "data/Models/Environment/DS9FX/StandardRes/Dosi.nif")
                    pSet.AddObjectToSet(pPlanet, "Dosi Homeworld")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    if DS9FXSavedConfig.DosiNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/StandardRes/Dosi.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/StandardRes/Planet001.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/StandardRes/Planet003.nif", "Class-O")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

    elif DS9FXSavedConfig.DosiMapPlanetDetail == 1:
        if DS9FXSavedConfig.DosiPlanets == 1:    
                    pPlanet3 = App.Planet_Create(88.0, "data/Models/Environment/DS9FX/LowRes/Planet003.nif")
                    pSet.AddObjectToSet(pPlanet3, "Dosi 1")

                    pPlanet3.PlaceObjectByName("Planet3")
                    pPlanet3.UpdateNodeOnly()

                    pPlanet2 = App.Planet_Create(105.0, "data/Models/Environment/DS9FX/LowRes/Planet001.nif")
                    pSet.AddObjectToSet(pPlanet2, "Dosi 2")

                    pPlanet2.PlaceObjectByName("Planet2")
                    pPlanet2.UpdateNodeOnly()

                    pPlanet = App.Planet_Create(65.0, "data/Models/Environment/DS9FX/LowRes/Dosi.nif")
                    pSet.AddObjectToSet(pPlanet, "Dosi Homeworld")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    if DS9FXSavedConfig.DosiNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/LowRes/Dosi.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/LowRes/Planet001.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/LowRes/Planet003.nif", "Class-O")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

    else:
        if DS9FXSavedConfig.DosiPlanets == 1:    
                    pPlanet3 = App.Planet_Create(88.0, "data/Models/Environment/DS9FX/LowestRes/Planet003.nif")
                    pSet.AddObjectToSet(pPlanet3, "Dosi 1")

                    pPlanet3.PlaceObjectByName("Planet3")
                    pPlanet3.UpdateNodeOnly()

                    pPlanet2 = App.Planet_Create(105.0, "data/Models/Environment/DS9FX/LowestRes/Planet001.nif")
                    pSet.AddObjectToSet(pPlanet2, "Dosi 2")

                    pPlanet2.PlaceObjectByName("Planet2")
                    pPlanet2.UpdateNodeOnly()

                    pPlanet = App.Planet_Create(65.0, "data/Models/Environment/DS9FX/LowestRes/Dosi.nif")
                    pSet.AddObjectToSet(pPlanet, "Dosi Homeworld")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    if DS9FXSavedConfig.DosiNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/LowestRes/Dosi.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/LowestRes/Planet001.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/LowestRes/Planet003.nif", "Class-O")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

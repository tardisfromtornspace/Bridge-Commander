# by Sov

import App
import MissionLib
import Tactical.LensFlares
from Custom.DS9FX import DS9FXmain
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig
from Custom.DS9FX.DS9FXSunStreak import SunStreak

def Initialize(pSet):    
    pSun = App.Sun_Create(4700.0, 4700.0, 4700.0, "data/Textures/SunPurple.tga", "data/Textures/Effects/SunFlaresWhite.tga")
    pSet.AddObjectToSet(pSun, "T-Rogoran Sun")
    
    pSun.PlaceObjectByName( "Sun" )
    pSun.UpdateNodeOnly()
    
    Tactical.LensFlares.PurpleLensFlare(pSet, pSun)
    SunStreak.Create(pSet, "SunStr", 125000.0, "Purple", "2")    
    
    reload(DS9FXSavedConfig)
    if DS9FXSavedConfig.TRogoranMapPlanetDetail == 3:
        if DS9FXSavedConfig.TRogoranPlanets == 1:    
                    pPlanet = App.Planet_Create(20.0, "data/Models/Environment/DS9FX/HighRes/Planet004.nif")
                    pSet.AddObjectToSet(pPlanet, "T-Rogoran 1")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    pPlanet2 = App.Planet_Create(120.0, "data/Models/Environment/DS9FX/HighRes/bajor1High.nif")
                    pSet.AddObjectToSet(pPlanet2, "T-Rogoran 2")

                    pPlanet2.PlaceObjectByName("Planet2")
                    pPlanet2.UpdateNodeOnly()

                    pPlanet3 = App.Planet_Create(75.0, "data/Models/Environment/DS9FX/HighRes/T-Rogoran.nif")
                    pSet.AddObjectToSet(pPlanet3, "T-Rogoran Homeworld")

                    pPlanet3.PlaceObjectByName("Planet3")
                    pPlanet3.UpdateNodeOnly()

                    if DS9FXSavedConfig.TRogoranNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/HighRes/Planet004.nif", "Class-O")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/HighRes/bajor1High.nif", "Class-O")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/HighRes/T-Rogoran.nif", "Class-M")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

    elif DS9FXSavedConfig.TRogoranMapPlanetDetail == 2:
        if DS9FXSavedConfig.TRogoranPlanets == 1:    
                    pPlanet = App.Planet_Create(20.0, "data/Models/Environment/DS9FX/StandardRes/Planet004.nif")
                    pSet.AddObjectToSet(pPlanet, "T-Rogoran 1")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    pPlanet2 = App.Planet_Create(120.0, "data/Models/Environment/DS9FX/StandardRes/bajor1High.nif")
                    pSet.AddObjectToSet(pPlanet2, "T-Rogoran 2")

                    pPlanet2.PlaceObjectByName("Planet2")
                    pPlanet2.UpdateNodeOnly()

                    pPlanet3 = App.Planet_Create(75.0, "data/Models/Environment/DS9FX/StandardRes/T-Rogoran.nif")
                    pSet.AddObjectToSet(pPlanet3, "T-Rogoran Homeworld")

                    pPlanet3.PlaceObjectByName("Planet3")
                    pPlanet3.UpdateNodeOnly()

                    if DS9FXSavedConfig.TRogoranNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/StandardRes/Planet004.nif", "Class-O")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/StandardRes/bajor1High.nif", "Class-O")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/StandardRes/T-Rogoran.nif", "Class-M")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

    elif DS9FXSavedConfig.TRogoranMapPlanetDetail == 1:
        if DS9FXSavedConfig.TRogoranPlanets == 1:    
                    pPlanet = App.Planet_Create(20.0, "data/Models/Environment/DS9FX/LowRes/Planet004.nif")
                    pSet.AddObjectToSet(pPlanet, "T-Rogoran 1")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    pPlanet2 = App.Planet_Create(120.0, "data/Models/Environment/DS9FX/LowRes/bajor1High.nif")
                    pSet.AddObjectToSet(pPlanet2, "T-Rogoran 2")

                    pPlanet2.PlaceObjectByName("Planet2")
                    pPlanet2.UpdateNodeOnly()

                    pPlanet3 = App.Planet_Create(75.0, "data/Models/Environment/DS9FX/LowRes/T-Rogoran.nif")
                    pSet.AddObjectToSet(pPlanet3, "T-Rogoran Homeworld")

                    pPlanet3.PlaceObjectByName("Planet3")
                    pPlanet3.UpdateNodeOnly()

                    if DS9FXSavedConfig.TRogoranNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/LowRes/Planet004.nif", "Class-O")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/LowRes/bajor1High.nif", "Class-O")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/LowRes/T-Rogoran.nif", "Class-M")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

    else:
        if DS9FXSavedConfig.TRogoranPlanets == 1:    
                    pPlanet = App.Planet_Create(20.0, "data/Models/Environment/DS9FX/LowestRes/Planet004.nif")
                    pSet.AddObjectToSet(pPlanet, "T-Rogoran 1")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    pPlanet2 = App.Planet_Create(120.0, "data/Models/Environment/DS9FX/LowestRes/bajor1High.nif")
                    pSet.AddObjectToSet(pPlanet2, "T-Rogoran 2")

                    pPlanet2.PlaceObjectByName("Planet2")
                    pPlanet2.UpdateNodeOnly()

                    pPlanet3 = App.Planet_Create(75.0, "data/Models/Environment/DS9FX/LowestRes/T-Rogoran.nif")
                    pSet.AddObjectToSet(pPlanet3, "T-Rogoran Homeworld")

                    pPlanet3.PlaceObjectByName("Planet3")
                    pPlanet3.UpdateNodeOnly()

                    if DS9FXSavedConfig.TRogoranNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/LowestRes/Planet004.nif", "Class-O")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/LowestRes/bajor1High.nif", "Class-O")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/LowestRes/T-Rogoran.nif", "Class-M")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

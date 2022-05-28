# by Sov

import App
import MissionLib
import Tactical.LensFlares
from Custom.DS9FX import DS9FXmain
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig
from Custom.DS9FX.DS9FXSunStreak import SunStreak

def Initialize(pSet): 
    pSun = App.Sun_Create(3780.0, 3780.0, 3780.0, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresYellow.tga")
    pSet.AddObjectToSet(pSun, "Vandros Sun")
    
    pSun.PlaceObjectByName( "Sun" )
    pSun.UpdateNodeOnly()
    
    Tactical.LensFlares.YellowLensFlare(pSet, pSun, 1, 0.33, 0.33)
    SunStreak.Create(pSet, "SunStr", 95000.0, "Yellow", "2")
                    
    reload(DS9FXSavedConfig)
    if DS9FXSavedConfig.VandrosMapPlanetDetail == 3:
        if DS9FXSavedConfig.VandrosPlanets == 1:    
                    pPlanet = App.Planet_Create(40.0, "data/Models/Environment/DS9FX/HighRes/Planet005.nif")
                    pSet.AddObjectToSet(pPlanet, "Vandros I")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    pPlanet2 = App.Planet_Create(70.0, "data/Models/Environment/DS9FX/HighRes/Planet001.nif")
                    pSet.AddObjectToSet(pPlanet2, "Vandros II")

                    pPlanet2.PlaceObjectByName("Planet2")
                    pPlanet2.UpdateNodeOnly()

                    pPlanet3 = App.Planet_Create(100.0, "data/Models/Environment/DS9FX/HighRes/Planet003.nif")
                    pSet.AddObjectToSet(pPlanet3, "Vandros III")

                    pPlanet3.PlaceObjectByName("Planet3")
                    pPlanet3.UpdateNodeOnly()

                    pPlanet4 = App.Planet_Create(90.0, "data/Models/Environment/DS9FX/HighRes/VandrosIV.nif")
                    pSet.AddObjectToSet(pPlanet4, "Vandros IV")

                    pPlanet4.PlaceObjectByName("Planet4")
                    pPlanet4.UpdateNodeOnly()

                    if DS9FXSavedConfig.VandrosNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/HighRes/Planet005.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/HighRes/Planet001.nif", "Class-O")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/HighRes/Planet003.nif", "Class-O")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/HighRes/VandrosIV.nif", "Class-M")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

    elif DS9FXSavedConfig.VandrosMapPlanetDetail == 2:
        if DS9FXSavedConfig.VandrosPlanets == 1:    
                    pPlanet = App.Planet_Create(40.0, "data/Models/Environment/DS9FX/StandardRes/Planet005.nif")
                    pSet.AddObjectToSet(pPlanet, "Vandros I")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    pPlanet2 = App.Planet_Create(70.0, "data/Models/Environment/DS9FX/StandardRes/Planet001.nif")
                    pSet.AddObjectToSet(pPlanet2, "Vandros II")

                    pPlanet2.PlaceObjectByName("Planet2")
                    pPlanet2.UpdateNodeOnly()

                    pPlanet3 = App.Planet_Create(100.0, "data/Models/Environment/DS9FX/StandardRes/Planet003.nif")
                    pSet.AddObjectToSet(pPlanet3, "Vandros III")

                    pPlanet3.PlaceObjectByName("Planet3")
                    pPlanet3.UpdateNodeOnly()

                    pPlanet4 = App.Planet_Create(90.0, "data/Models/Environment/DS9FX/StandardRes/VandrosIV.nif")
                    pSet.AddObjectToSet(pPlanet4, "Vandros IV")

                    pPlanet4.PlaceObjectByName("Planet4")
                    pPlanet4.UpdateNodeOnly()

                    if DS9FXSavedConfig.VandrosNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/StandardRes/Planet005.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/StandardRes/Planet001.nif", "Class-O")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/StandardRes/Planet003.nif", "Class-O")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/StandardRes/VandrosIV.nif", "Class-M")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

    elif DS9FXSavedConfig.VandrosMapPlanetDetail == 1:
        if DS9FXSavedConfig.VandrosPlanets == 1:    
                    pPlanet = App.Planet_Create(40.0, "data/Models/Environment/DS9FX/LowRes/Planet005.nif")
                    pSet.AddObjectToSet(pPlanet, "Vandros I")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    pPlanet2 = App.Planet_Create(70.0, "data/Models/Environment/DS9FX/LowRes/Planet001.nif")
                    pSet.AddObjectToSet(pPlanet2, "Vandros II")

                    pPlanet2.PlaceObjectByName("Planet2")
                    pPlanet2.UpdateNodeOnly()

                    pPlanet3 = App.Planet_Create(100.0, "data/Models/Environment/DS9FX/LowRes/Planet003.nif")
                    pSet.AddObjectToSet(pPlanet3, "Vandros III")

                    pPlanet3.PlaceObjectByName("Planet3")
                    pPlanet3.UpdateNodeOnly()

                    pPlanet4 = App.Planet_Create(90.0, "data/Models/Environment/DS9FX/LowRes/VandrosIV.nif")
                    pSet.AddObjectToSet(pPlanet4, "Vandros IV")

                    pPlanet4.PlaceObjectByName("Planet4")
                    pPlanet4.UpdateNodeOnly()

                    if DS9FXSavedConfig.VandrosNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/LowRes/Planet005.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/LowRes/Planet001.nif", "Class-O")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/LowRes/Planet003.nif", "Class-O")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/LowRes/VandrosIV.nif", "Class-M")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

    else:
        if DS9FXSavedConfig.VandrosPlanets == 1:    
                    pPlanet = App.Planet_Create(40.0, "data/Models/Environment/DS9FX/LowestRes/Planet005.nif")
                    pSet.AddObjectToSet(pPlanet, "Vandros I")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    pPlanet2 = App.Planet_Create(70.0, "data/Models/Environment/DS9FX/LowestRes/Planet001.nif")
                    pSet.AddObjectToSet(pPlanet2, "Vandros II")

                    pPlanet2.PlaceObjectByName("Planet2")
                    pPlanet2.UpdateNodeOnly()

                    pPlanet3 = App.Planet_Create(100.0, "data/Models/Environment/DS9FX/LowestRes/Planet003.nif")
                    pSet.AddObjectToSet(pPlanet3, "Vandros III")

                    pPlanet3.PlaceObjectByName("Planet3")
                    pPlanet3.UpdateNodeOnly()

                    pPlanet4 = App.Planet_Create(90.0, "data/Models/Environment/DS9FX/LowestRes/VandrosIV.nif")
                    pSet.AddObjectToSet(pPlanet4, "Vandros IV")

                    pPlanet4.PlaceObjectByName("Planet4")
                    pPlanet4.UpdateNodeOnly()

                    if DS9FXSavedConfig.VandrosNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/LowestRes/Planet005.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/LowestRes/Planet001.nif", "Class-O")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/LowestRes/Planet003.nif", "Class-O")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/LowestRes/VandrosIV.nif", "Class-M")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

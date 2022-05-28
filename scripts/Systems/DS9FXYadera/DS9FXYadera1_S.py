# by Sov

import App
import MissionLib
import Tactical.LensFlares
from Custom.DS9FX import DS9FXmain
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig
from Custom.DS9FX.DS9FXSunStreak import SunStreak

def Initialize(pSet):  
    pSun = App.Sun_Create(5755.0, 5755.0, 5775.0, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresRedOrange.tga")
    pSet.AddObjectToSet(pSun, "Yadera Sun")
    
    pSun.PlaceObjectByName( "Sun" )
    pSun.UpdateNodeOnly()
    
    Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun)
    SunStreak.Create(pSet, "SunStr", 130000.0, "RedOrange", "6")
                    
    reload(DS9FXSavedConfig)
    if DS9FXSavedConfig.YaderaMapPlanetDetail == 3:
        if DS9FXSavedConfig.YaderaPlanets == 1:    
                    pPlanet = App.Planet_Create(80.0, "data/Models/Environment/DS9FX/HighRes/Planet002.nif")
                    pSet.AddObjectToSet(pPlanet, "Yadera 1")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    pPlanet2 = App.Planet_Create(55.0, "data/Models/Environment/DS9FX/HighRes/Planet006.nif")
                    pSet.AddObjectToSet(pPlanet2, "Yadera 2")

                    pPlanet2.PlaceObjectByName("Planet2")
                    pPlanet2.UpdateNodeOnly()

                    pPlanet3 = App.Planet_Create(88.0, "data/Models/Environment/DS9FX/HighRes/Planet005.nif")
                    pSet.AddObjectToSet(pPlanet3, "Yadera 3")

                    pPlanet3.PlaceObjectByName("Planet3")
                    pPlanet3.UpdateNodeOnly()

                    pPlanet4 = App.Planet_Create(95.0, "data/Models/Environment/DS9FX/HighRes/YaderaPrime.nif")
                    pSet.AddObjectToSet(pPlanet4, "Yadera Prime")

                    pPlanet4.PlaceObjectByName("Planet4")
                    pPlanet4.UpdateNodeOnly()

                    pPlanet5 = App.Planet_Create(180.0, "data/Models/Environment/DS9FX/HighRes/Planet003.nif")
                    pSet.AddObjectToSet(pPlanet5, "Yadera 5")

                    pPlanet5.PlaceObjectByName("Planet5")
                    pPlanet5.UpdateNodeOnly()

                    if DS9FXSavedConfig.YaderaNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/HighRes/Planet002.nif", "Class-H")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/HighRes/Planet006.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/HighRes/Planet005.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/HighRes/YaderaPrime.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet5, "data/Models/Environment/DS9FX/HighRes/Planet003.nif", "Class-O")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

    elif DS9FXSavedConfig.YaderaMapPlanetDetail == 2:
        if DS9FXSavedConfig.YaderaPlanets == 1:    
                    pPlanet = App.Planet_Create(80.0, "data/Models/Environment/DS9FX/StandardRes/Planet002.nif")
                    pSet.AddObjectToSet(pPlanet, "Yadera 1")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    pPlanet2 = App.Planet_Create(55.0, "data/Models/Environment/DS9FX/StandardRes/Planet006.nif")
                    pSet.AddObjectToSet(pPlanet2, "Yadera 2")

                    pPlanet2.PlaceObjectByName("Planet2")
                    pPlanet2.UpdateNodeOnly()

                    pPlanet3 = App.Planet_Create(88.0, "data/Models/Environment/DS9FX/StandardRes/Planet005.nif")
                    pSet.AddObjectToSet(pPlanet3, "Yadera 3")

                    pPlanet3.PlaceObjectByName("Planet3")
                    pPlanet3.UpdateNodeOnly()

                    pPlanet4 = App.Planet_Create(95.0, "data/Models/Environment/DS9FX/StandardRes/YaderaPrime.nif")
                    pSet.AddObjectToSet(pPlanet4, "Yadera Prime")

                    pPlanet4.PlaceObjectByName("Planet4")
                    pPlanet4.UpdateNodeOnly()

                    pPlanet5 = App.Planet_Create(180.0, "data/Models/Environment/DS9FX/StandardRes/Planet003.nif")
                    pSet.AddObjectToSet(pPlanet5, "Yadera 5")

                    pPlanet5.PlaceObjectByName("Planet5")
                    pPlanet5.UpdateNodeOnly()

                    if DS9FXSavedConfig.YaderaNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/StandardRes/Planet002.nif", "Class-H")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/StandardRes/Planet006.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/StandardRes/Planet005.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/StandardRes/YaderaPrime.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet5, "data/Models/Environment/DS9FX/StandardRes/Planet003.nif", "Class-O")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

    elif DS9FXSavedConfig.YaderaMapPlanetDetail == 1:
        if DS9FXSavedConfig.YaderaPlanets == 1:    
                    pPlanet = App.Planet_Create(80.0, "data/Models/Environment/DS9FX/LowRes/Planet002.nif")
                    pSet.AddObjectToSet(pPlanet, "Yadera 1")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    pPlanet2 = App.Planet_Create(55.0, "data/Models/Environment/DS9FX/LowRes/Planet006.nif")
                    pSet.AddObjectToSet(pPlanet2, "Yadera 2")

                    pPlanet2.PlaceObjectByName("Planet2")
                    pPlanet2.UpdateNodeOnly()

                    pPlanet3 = App.Planet_Create(88.0, "data/Models/Environment/DS9FX/LowRes/Planet005.nif")
                    pSet.AddObjectToSet(pPlanet3, "Yadera 3")

                    pPlanet3.PlaceObjectByName("Planet3")
                    pPlanet3.UpdateNodeOnly()

                    pPlanet4 = App.Planet_Create(95.0, "data/Models/Environment/DS9FX/LowRes/YaderaPrime.nif")
                    pSet.AddObjectToSet(pPlanet4, "Yadera Prime")

                    pPlanet4.PlaceObjectByName("Planet4")
                    pPlanet4.UpdateNodeOnly()

                    pPlanet5 = App.Planet_Create(180.0, "data/Models/Environment/DS9FX/LowRes/Planet003.nif")
                    pSet.AddObjectToSet(pPlanet5, "Yadera 5")

                    pPlanet5.PlaceObjectByName("Planet5")
                    pPlanet5.UpdateNodeOnly()

                    if DS9FXSavedConfig.YaderaNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/LowRes/Planet002.nif", "Class-H")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/LowRes/Planet006.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/LowRes/Planet005.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/LowRes/YaderaPrime.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet5, "data/Models/Environment/DS9FX/LowRes/Planet003.nif", "Class-O")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

    else:
        if DS9FXSavedConfig.YaderaPlanets == 1:    
                    pPlanet = App.Planet_Create(80.0, "data/Models/Environment/DS9FX/LowestRes/Planet002.nif")
                    pSet.AddObjectToSet(pPlanet, "Yadera 1")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    pPlanet2 = App.Planet_Create(55.0, "data/Models/Environment/DS9FX/LowestRes/Planet006.nif")
                    pSet.AddObjectToSet(pPlanet2, "Yadera 2")

                    pPlanet2.PlaceObjectByName("Planet2")
                    pPlanet2.UpdateNodeOnly()

                    pPlanet3 = App.Planet_Create(88.0, "data/Models/Environment/DS9FX/LowestRes/Planet005.nif")
                    pSet.AddObjectToSet(pPlanet3, "Yadera 3")

                    pPlanet3.PlaceObjectByName("Planet3")
                    pPlanet3.UpdateNodeOnly()

                    pPlanet4 = App.Planet_Create(95.0, "data/Models/Environment/DS9FX/LowestRes/YaderaPrime.nif")
                    pSet.AddObjectToSet(pPlanet4, "Yadera Prime")

                    pPlanet4.PlaceObjectByName("Planet4")
                    pPlanet4.UpdateNodeOnly()

                    pPlanet5 = App.Planet_Create(180.0, "data/Models/Environment/DS9FX/LowestRes/Planet003.nif")
                    pSet.AddObjectToSet(pPlanet5, "Yadera 5")

                    pPlanet5.PlaceObjectByName("Planet5")
                    pPlanet5.UpdateNodeOnly()

                    if DS9FXSavedConfig.YaderaNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/LowestRes/Planet002.nif", "Class-H")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/LowestRes/Planet006.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/LowestRes/Planet005.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/LowestRes/YaderaPrime.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet5, "data/Models/Environment/DS9FX/LowestRes/Planet003.nif", "Class-O")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

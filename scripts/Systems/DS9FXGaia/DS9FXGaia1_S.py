# by Sov

import App
import MissionLib
import Tactical.LensFlares
from Custom.DS9FX import DS9FXmain
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig
from Custom.DS9FX.DS9FXSunStreak import SunStreak

def Initialize(pSet):
    pSun = App.Sun_Create(2800.0, 2800.0, 2800.0, "data/Textures/SunDrkBlue.tga", "data/Textures/Effects/SunFlaresBlue.tga")
    pSet.AddObjectToSet(pSun, "Gaia Sun")
    
    pSun.PlaceObjectByName( "Sun" )
    pSun.UpdateNodeOnly()
    
    Tactical.LensFlares.DimBlueLensFlare(pSet, pSun)
    SunStreak.Create(pSet, "SunStr", 105000.0, "DarkBlue", "8")

    reload(DS9FXSavedConfig)
    if DS9FXSavedConfig.GaiaMapPlanetDetail == 3:
        if DS9FXSavedConfig.GaiaPlanets == 1:    
                    pPlanet = App.Planet_Create(35.0, "data/Models/Environment/DS9FX/HighRes/Planet004.nif")
                    pSet.AddObjectToSet(pPlanet, "Gaia I")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    pPlanet2 = App.Planet_Create(55.0, "data/Models/Environment/DS9FX/HighRes/Planet004.nif")
                    pSet.AddObjectToSet(pPlanet2, "Gaia II")

                    pPlanet2.PlaceObjectByName("Planet2")
                    pPlanet2.UpdateNodeOnly()

                    pPlanet3 = App.Planet_Create(250.0, "data/Models/Environment/DS9FX/HighRes/Gamma1High.nif")
                    pSet.AddObjectToSet(pPlanet3, "Gaia III")

                    pPlanet3.PlaceObjectByName("Planet3")
                    pPlanet3.UpdateNodeOnly()

                    pPlanet4 = App.Planet_Create(100.0, "data/Models/Environment/DS9FX/HighRes/GaiaIV.nif")
                    pSet.AddObjectToSet(pPlanet4, "Gaia IV")

                    pPlanet4.PlaceObjectByName("Planet4")
                    pPlanet4.UpdateNodeOnly()

                    if DS9FXSavedConfig.GaiaNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/HighRes/Planet004.nif", "Class-H")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/HighRes/Planet004.nif", "Class-H")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/HighRes/Gamma1High.nif", "Class-O")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/HighRes/GaiaIV.nif", "Class-M")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

    elif DS9FXSavedConfig.GaiaMapPlanetDetail == 2:
        if DS9FXSavedConfig.GaiaPlanets == 1:    
                    pPlanet = App.Planet_Create(35.0, "data/Models/Environment/DS9FX/StandardRes/Planet004.nif")
                    pSet.AddObjectToSet(pPlanet, "Gaia I")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    pPlanet2 = App.Planet_Create(55.0, "data/Models/Environment/DS9FX/StandardRes/Planet004.nif")
                    pSet.AddObjectToSet(pPlanet2, "Gaia II")

                    pPlanet2.PlaceObjectByName("Planet2")
                    pPlanet2.UpdateNodeOnly()

                    pPlanet3 = App.Planet_Create(250.0, "data/Models/Environment/DS9FX/StandardRes/Gamma1High.nif")
                    pSet.AddObjectToSet(pPlanet3, "Gaia III")

                    pPlanet3.PlaceObjectByName("Planet3")
                    pPlanet3.UpdateNodeOnly()

                    pPlanet4 = App.Planet_Create(100.0, "data/Models/Environment/DS9FX/StandardRes/GaiaIV.nif")
                    pSet.AddObjectToSet(pPlanet4, "Gaia IV")

                    pPlanet4.PlaceObjectByName("Planet4")
                    pPlanet4.UpdateNodeOnly()

                    if DS9FXSavedConfig.GaiaNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/StandardRes/Planet004.nif", "Class-H")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/StandardRes/Planet004.nif", "Class-H")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/StandardRes/Gamma1High.nif", "Class-O")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/StandardRes/GaiaIV.nif", "Class-M")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

    elif DS9FXSavedConfig.GaiaMapPlanetDetail == 1:
        if DS9FXSavedConfig.GaiaPlanets == 1:    
                    pPlanet = App.Planet_Create(35.0, "data/Models/Environment/DS9FX/LowRes/Planet004.nif")
                    pSet.AddObjectToSet(pPlanet, "Gaia I")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    pPlanet2 = App.Planet_Create(55.0, "data/Models/Environment/DS9FX/LowRes/Planet004.nif")
                    pSet.AddObjectToSet(pPlanet2, "Gaia II")

                    pPlanet2.PlaceObjectByName("Planet2")
                    pPlanet2.UpdateNodeOnly()

                    pPlanet3 = App.Planet_Create(250.0, "data/Models/Environment/DS9FX/LowRes/Gamma1High.nif")
                    pSet.AddObjectToSet(pPlanet3, "Gaia III")

                    pPlanet3.PlaceObjectByName("Planet3")
                    pPlanet3.UpdateNodeOnly()

                    pPlanet4 = App.Planet_Create(100.0, "data/Models/Environment/DS9FX/LowRes/GaiaIV.nif")
                    pSet.AddObjectToSet(pPlanet4, "Gaia IV")

                    pPlanet4.PlaceObjectByName("Planet4")
                    pPlanet4.UpdateNodeOnly()

                    if DS9FXSavedConfig.GaiaNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/LowRes/Planet004.nif", "Class-H")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/LowRes/Planet004.nif", "Class-H")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/LowRes/Gamma1High.nif", "Class-O")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/LowRes/GaiaIV.nif", "Class-M")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

    else:
        if DS9FXSavedConfig.GaiaPlanets == 1:    
                    pPlanet = App.Planet_Create(35.0, "data/Models/Environment/DS9FX/LowestRes/Planet004.nif")
                    pSet.AddObjectToSet(pPlanet, "Gaia I")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    pPlanet2 = App.Planet_Create(55.0, "data/Models/Environment/DS9FX/LowestRes/Planet004.nif")
                    pSet.AddObjectToSet(pPlanet2, "Gaia II")

                    pPlanet2.PlaceObjectByName("Planet2")
                    pPlanet2.UpdateNodeOnly()

                    pPlanet3 = App.Planet_Create(250.0, "data/Models/Environment/DS9FX/LowestRes/Gamma1High.nif")
                    pSet.AddObjectToSet(pPlanet3, "Gaia III")

                    pPlanet3.PlaceObjectByName("Planet3")
                    pPlanet3.UpdateNodeOnly()

                    pPlanet4 = App.Planet_Create(100.0, "data/Models/Environment/DS9FX/LowestRes/GaiaIV.nif")
                    pSet.AddObjectToSet(pPlanet4, "Gaia IV")

                    pPlanet4.PlaceObjectByName("Planet4")
                    pPlanet4.UpdateNodeOnly()

                    if DS9FXSavedConfig.GaiaNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/LowestRes/Planet004.nif", "Class-H")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/LowestRes/Planet004.nif", "Class-H")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/LowestRes/Gamma1High.nif", "Class-O")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/LowestRes/GaiaIV.nif", "Class-M")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

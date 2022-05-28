# by Sov

import App
import MissionLib
import Tactical.LensFlares
from Custom.DS9FX import DS9FXmain
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig
from Custom.DS9FX.DS9FXSunStreak import SunStreak

def Initialize(pSet):
        from Custom.DS9FX.DS9FXObjects import FoundersShips
        FoundersShips.FoundersSetShips()

        if DS9FXSavedConfig.FoundersReinforcements == 1:
                SetupEvents(pSet)
                
        pSun = App.Sun_Create(4500.0, 4500.0, 4500.0, "data/Textures/SunPurple.tga", "data/Textures/Effects/SunFlaresWhite.tga")
        pSet.AddObjectToSet(pSun, "Founders Sun")

        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        Tactical.LensFlares.PurpleLensFlare(pSet, pSun, 1, 0.35, 0.35)
        SunStreak.Create(pSet, "SunStr", 125000.0, "Purple", "2")
                
        reload(DS9FXSavedConfig)
        if DS9FXSavedConfig.FoundersMapPlanetDetail == 3:
                if DS9FXSavedConfig.FoundersPlanets == 1:
                        pPlanet = App.Planet_Create(75.0, "data/Models/Environment/DS9FX/HighRes/FounderHomeworld.nif")
                        pSet.AddObjectToSet(pPlanet, "Founders Homeworld")

                        pPlanet.PlaceObjectByName("Planet1")
                        pPlanet.UpdateNodeOnly()

                        if DS9FXSavedConfig.FoundersNanoFX == 1:
                                try:
                                        import Custom.NanoFXv2.NanoFX_Lib
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/HighRes/FounderHomeworld.nif", "Class-M")
                                except:
                                        print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

        elif DS9FXSavedConfig.FoundersMapPlanetDetail == 2:
                if DS9FXSavedConfig.FoundersPlanets == 1:
                        pPlanet = App.Planet_Create(75.0, "data/Models/Environment/DS9FX/StandardRes/FounderHomeworld.nif")
                        pSet.AddObjectToSet(pPlanet, "Founders Homeworld")

                        pPlanet.PlaceObjectByName("Planet1")
                        pPlanet.UpdateNodeOnly()

                        if DS9FXSavedConfig.FoundersNanoFX == 1:
                                try:
                                        import Custom.NanoFXv2.NanoFX_Lib
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/StandardRes/FounderHomeworld.nif", "Class-M")
                                except:
                                        print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

        elif DS9FXSavedConfig.FoundersMapPlanetDetail == 1:
                if DS9FXSavedConfig.FoundersPlanets == 1:
                        pPlanet = App.Planet_Create(75.0, "data/Models/Environment/DS9FX/LowRes/FounderHomeworld.nif")
                        pSet.AddObjectToSet(pPlanet, "Founders Homeworld")

                        pPlanet.PlaceObjectByName("Planet1")
                        pPlanet.UpdateNodeOnly()

                        if DS9FXSavedConfig.FoundersNanoFX == 1:
                                try:
                                        import Custom.NanoFXv2.NanoFX_Lib
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/LowRes/FounderHomeworld.nif", "Class-M")
                                except:
                                        print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

        else:
                if DS9FXSavedConfig.FoundersPlanets == 1:
                        pPlanet = App.Planet_Create(75.0, "data/Models/Environment/DS9FX/LowestRes/FounderHomeworld.nif")
                        pSet.AddObjectToSet(pPlanet, "Founders Homeworld")

                        pPlanet.PlaceObjectByName("Planet1")
                        pPlanet.UpdateNodeOnly()

                        if DS9FXSavedConfig.FoundersNanoFX == 1:
                                try:
                                        import Custom.NanoFXv2.NanoFX_Lib
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/LowestRes/FounderHomeworld.nif", "Class-M")
                                except:
                                        print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

def SetupEvents(pSet):
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pSet, __name__ + ".EnterSet")

def EnterSet(pObject, pEvent):
        try:
                pShip = App.ShipClass_Cast(pEvent.GetDestination())
                pPlayer = App.Game_GetCurrentPlayer()

                if pShip.GetObjID() != pPlayer.GetObjID():
                        return
        except AttributeError:
                return

        if pShip.GetContainingSet().GetName() == "DS9FXFoundersHomeworld1":
                CallReinforcements()

def CallReinforcements():
        from Custom.DS9FX.DS9FXObjects import FoundersReinforcements
        FoundersReinforcements.ReinforcementHandler()    

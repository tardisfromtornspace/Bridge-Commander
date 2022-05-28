###############################################################################
#       Filename:       Universe1_S.py
#       
#       Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard
#       
#       Creates Universe1 static objects.  Called by Universe.py when region is created
#       
#       Created:        09/17/00 
#       Modified:       10/04/01 - Tony Evans
#       Modified:       01/15/03 - Ben Howard
#       Modified:       Sept. 2003 - Chris Jones
# Adapted for Multi-Player 12/21/03 - Chris Jones
###############################################################################
import App
import loadspacehelper
import MissionLib
import SelfDefenseAI
import RouteAI
import DefendAI

def Initialize(pSet):

        pSun = App.Sun_Create(1200.0, 800, 500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
        pSet.AddObjectToSet(pSun, "Banzai Prime")
        
        # Place the object at the specified location.
        pSun.PlaceObjectByName( "Star" )
        pSun.UpdateNodeOnly()

        # Add a sun, far far away
        pSunq = App.Sun_Create(100.0, 300, 500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresBlue.tga")
        pSet.AddObjectToSet(pSunq, "Banzai Dwarf")

        # Place the object at the specified location.
        pSunq.PlaceObjectByName( "Sunq" )
        pSunq.UpdateNodeOnly()

        # Add a sun, far far away
        pSun2 = App.Sun_Create(325.0, 200, 500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresBlue.tga")
        pSet.AddObjectToSet(pSun2, "Sirius")
        
        # Place the object at the specified location.
        pSun2.PlaceObjectByName( "Sun2" )
        pSun2.UpdateNodeOnly()

        # Add a sun, far far away
        pSun3 = App.Sun_Create(180.0, 950, 500, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pSun3, "Risa")
        
        # Place the object at the specified location.
        pSun3.PlaceObjectByName( "Sun3" )
        pSun3.UpdateNodeOnly()

        # Model and placement for Risa 1
        pRisa1 = App.Planet_Create(60.0, "data/models/environment/PurpleWhitePlanet.nif")
        pSet.AddObjectToSet(pRisa1, "Risa 1")

        #Place the object at the specified location.
        pRisa1.PlaceObjectByName("Risa1L")
        pRisa1.UpdateNodeOnly()

        # Add a sun, far far away
        pSun4 = App.Sun_Create(500.0, 500, 500, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresWhite.tga")
        pSet.AddObjectToSet(pSun4, "Sol")
        
        # Place the object at the specified location.
        pSun4.PlaceObjectByName( "Sun4" )
        pSun4.UpdateNodeOnly()

        # Model and placement for Sol 3
        pSol3 = App.Planet_Create(40.0, "data/models/environment/earth.nif")
        pSet.AddObjectToSet(pSol3, "Earth")

        #Place the object at the specified location.
        pSol3.PlaceObjectByName("Sol3L")
        pSol3.UpdateNodeOnly()

        # Add a sun, far far away
        pSun5 = App.Sun_Create(430.0, 50, 500, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresOrange.tga")
        pSet.AddObjectToSet(pSun5, "Romulus")
        
        # Place the object at the specified location.
        pSun5.PlaceObjectByName( "Sun5" )
        pSun5.UpdateNodeOnly()

        # Model and placement for Romulus1
        pRomulus1 = App.Planet_Create(50.0, "data/models/environment/AquaPlanet.nif")
        pSet.AddObjectToSet(pRomulus1, "Romulus 1")

        #Place the object at the specified location.
        pRomulus1.PlaceObjectByName("Romulus1L")
        pRomulus1.UpdateNodeOnly()

        # Model and placement for Romulus2
        pRomulus2 = App.Planet_Create(20.0, "data/models/environment/BlueRockyPlanet.nif")
        pSet.AddObjectToSet(pRomulus2, "Remus")

        #Place the object at the specified location.
        pRomulus2.PlaceObjectByName("Romulus2L")
        pRomulus2.UpdateNodeOnly()

        # Add a sun, far far away
        pSun6 = App.Sun_Create(400.0, 400, 500, "data/Textures/SunDrkBlue.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pSun6, "Cardassia")
        
        # Place the object at the specified location.
        pSun6.PlaceObjectByName( "Sun6" )
        pSun6.UpdateNodeOnly()

        # Model and placement for Card
        pCard = App.Planet_Create(60.0, "data/models/environment/TurquoisePlanet.nif")
        pSet.AddObjectToSet(pCard, "Cardassia Prime")

        #Place the object at the specified location.
        pCard.PlaceObjectByName("CardL")
        pCard.UpdateNodeOnly()

        # Add a sun, far far away
        pSun7 = App.Sun_Create(270.0, 150, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresBlue.tga")
        pSet.AddObjectToSet(pSun7, "Kling")
        
        # Place the object at the specified location.
        pSun7.PlaceObjectByName( "Sun7" )
        pSun7.UpdateNodeOnly()

        # Model and placement for Kronos
        pKronos = App.Planet_Create(80.0, "data/models/environment/RootBeerPlanet.nif")
        pSet.AddObjectToSet(pKronos, "Kronos")

        #Place the object at the specified location.
        pKronos.PlaceObjectByName("KronosL")
        pKronos.UpdateNodeOnly()

        # Add a sun, far far away
        pSun8 = App.Sun_Create(250.0, 1250, 500, "data/Textures/SunPurple.tga", "data/Textures/Effects/SunFlaresRed.tga")
        pSet.AddObjectToSet(pSun8, "Ferengal")
        
        # Place the object at the specified location.
        pSun8.PlaceObjectByName( "Sun8" )
        pSun8.UpdateNodeOnly()

        # Model and placement for Ferengi
        pFerengi = App.Planet_Create(60.0, "data/models/environment/SlimeGreenPlanet.nif")
        pSet.AddObjectToSet(pFerengi, "Ferengi")

        #Place the object at the specified location.
        pFerengi.PlaceObjectByName("FerengiL")
        pFerengi.UpdateNodeOnly()

        # Add a sun, far far away
        pSun10 = App.Sun_Create(250.0, 50, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresRed.tga")
        pSet.AddObjectToSet(pSun10, "Antares")
        
        # Place the object at the specified location.
        pSun10.PlaceObjectByName( "Sun10" )
        pSun10.UpdateNodeOnly()

        # Add a sun, far far away
        pSun11 = App.Sun_Create(450.0, 350, 500, "data/Textures/SunCyan.tga", "data/Textures/Effects/SunFlaresRedOrange.tga")
        pSet.AddObjectToSet(pSun11, "Vega")
        
        # Place the object at the specified location.
        pSun11.PlaceObjectByName( "Sun11" )
        pSun11.UpdateNodeOnly()

        # Add a sun, far far away
        pSun12 = App.Sun_Create(950.0, 1250, 500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresWhite.tga")
        pSet.AddObjectToSet(pSun12, "Rigel")
        
        # Place the object at the specified location.
        pSun12.PlaceObjectByName( "Sun12" )
        pSun12.UpdateNodeOnly()

        # Add a sun, far far away
        pSun13 = App.Sun_Create(450.0, 450, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pSun13, "Bajor")
        
        # Place the object at the specified location.
        pSun13.PlaceObjectByName( "Sun13" )
        pSun13.UpdateNodeOnly()

        # Model and placement for Bajora
        pBajora = App.Planet_Create(30.0, "data/models/environment/BrownBluePlanet.nif")
        pSet.AddObjectToSet(pBajora, "Bajora")

        #Place the object at the specified location.
        pBajora.PlaceObjectByName("Bajora")
        pBajora.UpdateNodeOnly()

        # Add a sun, far far away
        pSun14 = App.Sun_Create(350.0, 450, 500, "data/Textures/SunBrown.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pSun14, "Khitomer")
        
        # Place the object at the specified location.
        pSun14.PlaceObjectByName( "Sun14" )
        pSun14.UpdateNodeOnly()

        # Add a sun, far far away
        pSun16 = App.Sun_Create(650.0, 250, 500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pSun16, "Vulcan")
        
        # Place the object at the specified location.
        pSun16.PlaceObjectByName( "Sun16" )
        pSun16.UpdateNodeOnly()

        # Model and placement for Vulcan1
        pVulcan1 = App.Planet_Create(40.0, "data/models/environment/RootBeerPlanet.nif")
        pSet.AddObjectToSet(pVulcan1, "Vulcan1")

        #Place the object at the specified location.
        pVulcan1.PlaceObjectByName("Vulcan1L")
        pVulcan1.UpdateNodeOnly()

        # Add a sun, far far away
        pSun15 = App.Sun_Create(50.0, 250, 500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresRed.tga")
        pSet.AddObjectToSet(pSun15, "Stellar Matter")
        
        # Place the object at the specified location.
        pSun15.PlaceObjectByName( "Sun15" )
        pSun15.UpdateNodeOnly()


        pNebula = App.MetaNebula_Create(205.0 / 255.0, 40.0 / 255.0, 185.0 / 255.0, 50.0, 20.0, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula.SetupDamage(1.0, 100.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula.AddNebulaSphere(69402.0, 80852.0, 173.0,  800.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula, "Nebula1")

        pNebula2 = App.MetaNebula_Create(205.0 / 255.0, 40.0 / 255.0, 185.0 / 255.0, 150.0, 10.0, "data/Backgrounds/nebulaoverlaybz1.tga", "data/Backgrounds/nebulaexternabz1l.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula2.SetupDamage(1.0, 100.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula2.AddNebulaSphere(-29500.0, -30950.0, -75075.0,  8000.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula2, "Nebula2")

        pNebula3 = App.MetaNebula_Create(205.0 / 255.0, 40.0 / 255.0, 185.0 / 255.0, 150.0, 10.0, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula3.SetupDamage(10.0, 10.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula3.AddNebulaSphere(3999.0, 1044.0, -37000.0,  500.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula3, "Nebula3")
        
        pNebula4 = App.MetaNebula_Create(205.0 / 255.0, 40.0 / 255.0, 185.0 / 255.0, 450.0, 5.0, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula4.SetupDamage(1.0, 1.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula4.AddNebulaSphere(4105.0, 540.0, -37205.0,  900.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula4, "Nebula4")
                
        pNebula5 = App.MetaNebula_Create(205.0 / 255.0, 40.0 / 255.0, 185.0 / 255.0, 2050.0, 1.0, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula5.SetupDamage(1.0, 1.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula5.AddNebulaSphere(4405.0, -300.0, -37605.0,  1700.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula5, "Nebula5")

        if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
        
                pStarbase       =loadspacehelper.CreateShip("FedStarbase", pSet, "Khitomer Colony", "StationL")
                MissionLib.SetTotalTorpsAtStarbase("Photon", -1)
                MissionLib.SetTotalTorpsAtStarbase("Quantum", -1)

                # Create our static stations and such
                pDS9    = loadspacehelper.CreateShip("ds9", pSet, "DS9", "DS9")

                # Create our static stations and such
                pHive   = loadspacehelper.CreateShip("CardOutpost", pSet, "Insect Hive", "Hive")
                
                # Create ship
                pGalaxy = loadspacehelper.CreateShip("Galaxy", pSet, "USS Venture", "Venture Location")
                pGalaxy.ReplaceTexture("data/Models/SharedTextures/FedShips/Venture.tga", "ID") 
                
                # Create ship
                pWarbird        = loadspacehelper.CreateShip("Warbird", pSet, "Denatra II", "Warbird Location")
                
                # Create ship
                pVorcha         = loadspacehelper.CreateShip("Vorcha", pSet, "IKV Kang", "Vorcha Location")
                
                # Create ship
                pSovereign      = loadspacehelper.CreateShip("Sovereign", pSet, "USS Sovereign", "Sovereign Location")
                
                # Create ship
                pFarragut       = loadspacehelper.CreateShip("Nebula", pSet, "USS Farragut", "Farragut Location")
                                
                pHulk1          = loadspacehelper.CreateShip("Ambassador", pSet, "Saratoga", "wreck1")
                pHulk2          = loadspacehelper.CreateShip("Nebula", pSet, "Kyushu", "wreck2")
                pHulk5          = loadspacehelper.CreateShip("Galaxy", pSet, "Yamaguchi", "wreck5")
                pHulk10         = loadspacehelper.CreateShip("Nebula", pSet, "Melbourne", "wreck10")
                pHulk13         = loadspacehelper.CreateShip("Ambassador", pSet, "Tolstoy", "wreck13")
                
                # Create ship
                pTransport      = loadspacehelper.CreateShip("Transport", pSet, "W359 Rescue", "RS Location")
                      
        def DamageWrecks(pHulk1, pHulk2, pHulk5, pHulk10, pHulk13):

                # Import our damaged script ship and apply it to the Hulk1
                pHulk1.SetHailable(0)
                import DamageAmbas1
                DamageAmbas1.AddDamage(pHulk1)
                # Turn off the ships repair
                pRepair = pHulk1.GetRepairSubsystem()
                pProp   = pRepair.GetProperty()
                pProp.SetMaxRepairPoints(0.0)
                # Damage the Hulk1...
                # Turn off the shields
                pAlertEvent = App.TGIntEvent_Create()
                pAlertEvent.SetDestination(pHulk1)
                pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
                pAlertEvent.SetInt(pHulk1.GREEN_ALERT)
                App.g_kEventManager.AddEvent(pAlertEvent)
                # Damage the hull - 500 pts left
                pHulk1.DamageSystem(pHulk1.GetHull(), 2500)
                pHulk1.DisableGlowAlphaMaps()
                # Dont allow the user to see the sub-systems
                MissionLib.HideSubsystems(pHulk1)
                # Spin the hulk
                MissionLib.SetRandomRotation(pHulk1, 5)
                
                # Import our damaged script ship and apply it to the Hulk2
                pHulk2.SetHailable(0)
                import DamageNebula1
                DamageNebula1.AddDamage(pHulk2)
                # Turn off the ships repair
                pRepair = pHulk2.GetRepairSubsystem()
                pProp   = pRepair.GetProperty()
                pProp.SetMaxRepairPoints(0.0)
                # Damage the Hulk2...
                # Turn off the shields
                pAlertEvent = App.TGIntEvent_Create()
                pAlertEvent.SetDestination(pHulk2)
                pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
                pAlertEvent.SetInt(pHulk2.GREEN_ALERT)
                App.g_kEventManager.AddEvent(pAlertEvent)
                # Damage the hull - 500 pts left
                pHulk2.DamageSystem(pHulk2.GetHull(), 3000)
                pHulk2.DisableGlowAlphaMaps()
                # Dont allow the user to see the sub-systems
                MissionLib.HideSubsystems(pHulk2)
                # Spin the hulk
                MissionLib.SetRandomRotation(pHulk2, 10)
                
                # Import our damaged script ship and apply it to the Hulk5
                pHulk5.SetHailable(0)
                import DamageGal1
                DamageGal1.AddDamage(pHulk5)
                # Turn off the ships repair
                pRepair = pHulk5.GetRepairSubsystem()
                pProp   = pRepair.GetProperty()
                pProp.SetMaxRepairPoints(0.0)
                # Damage the pHulk5...
                # Turn off the shields
                pAlertEvent = App.TGIntEvent_Create()
                pAlertEvent.SetDestination(pHulk5)
                pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
                pAlertEvent.SetInt(pHulk5.GREEN_ALERT)
                App.g_kEventManager.AddEvent(pAlertEvent)
                # Damage the hull - 500 pts left
                pHulk5.DamageSystem(pHulk5.GetHull(), 3000)
                pHulk5.DisableGlowAlphaMaps()
                # Dont allow the user to see the sub-systems
                MissionLib.HideSubsystems(pHulk5)
                # Spin the hulk
                MissionLib.SetRandomRotation(pHulk5, 8)
                
                # Import our damaged script ship and apply it to the pHulk10
                pHulk10.SetHailable(0)
                import DamageNeb2
                DamageNeb2.AddDamage(pHulk10)
                # Turn off the ships repair
                pRepair = pHulk10.GetRepairSubsystem()
                pProp   = pRepair.GetProperty()
                pProp.SetMaxRepairPoints(0.0)
                # Damage the pHulk10...
                # Turn off the shields
                pAlertEvent = App.TGIntEvent_Create()
                pAlertEvent.SetDestination(pHulk10)
                pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
                pAlertEvent.SetInt(pHulk10.GREEN_ALERT)
                App.g_kEventManager.AddEvent(pAlertEvent)
                # Damage the hull - 500 pts left
                pHulk10.DamageSystem(pHulk10.GetHull(), 4500)
                pHulk10.DisableGlowAlphaMaps()
                # Dont allow the user to see the sub-systems
                MissionLib.HideSubsystems(pHulk10)
                # Spin the hulk
                MissionLib.SetRandomRotation(pHulk10, 6)
                # Spin the hulk
                MissionLib.SetRandomRotation(pHulk10, 7)
                
                # Import our damaged script ship and apply it to the pHulk13
                pHulk13.SetHailable(0)
                import DamageAmbas2
                DamageAmbas2.AddDamage(pHulk13)
                # Turn off the ships repair
                pRepair = pHulk13.GetRepairSubsystem()
                pProp   = pRepair.GetProperty()
                pProp.SetMaxRepairPoints(0.0)
                # Damage the pHulk13...
                # Turn off the shields
                pAlertEvent = App.TGIntEvent_Create()
                pAlertEvent.SetDestination(pHulk13)
                pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
                pAlertEvent.SetInt(pHulk13.GREEN_ALERT)
                App.g_kEventManager.AddEvent(pAlertEvent)
                # Damage the hull - 500 pts left
                pHulk13.DamageSystem(pHulk13.GetHull(), 3000)
                pHulk13.DisableGlowAlphaMaps()
                # Dont allow the user to see the sub-systems
                MissionLib.HideSubsystems(pHulk13)
                # Spin the hulk
                MissionLib.SetRandomRotation(pHulk13, 7)

                global pFriendlies 
                global pEnemies
                
                pGame = App.Game_GetCurrentGame() 
                pEpisode = pGame.GetCurrentEpisode() 
                pMission = pEpisode.GetCurrentMission() 
                pEnemies = MissionLib.GetEnemyGroup()
                pEnemies.AddName("Khitomer Colony")
                pEnemies.AddName("DS9")
                pEnemies.AddName("Insect Hive")
                pNeutrals = pMission.GetNeutralGroup()
                pNeutrals.AddName("W359 Rescue")


                # Set up AI's
                import StarbaseMPAI
                pStarbase.SetAI(StarbaseMPAI.CreateAI(pStarbase))
                pDS9.SetAI(StarbaseMPAI.CreateAI(pDS9))
                pHive.SetAI(StarbaseMPAI.CreateAI(pHive))
                pGalaxy.SetAI(DefendAI.CreateAI(pGalaxy, pDS9))
                pWarbird.SetAI(SelfDefenseAI.CreateAI(pWarbird))
                pVorcha.SetAI(SelfDefenseAI.CreateAI(pVorcha))
                pFarragut.SetAI(SelfDefenseAI.CreateAI(pFarragut))
                pSovereign.SetAI(SelfDefenseAI.CreateAI(pSovereign))
                pTransport.SetAI(RouteAI.CreateAI(pTransport, pSol3, pHulk10))

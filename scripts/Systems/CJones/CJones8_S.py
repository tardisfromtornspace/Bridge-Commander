from bcdebug import debug
###############################################################################
#       Filename:       CJones8_S.py
#       
#       Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard
#       
#       Creates Vger 1 static objects.  Called by CJones8.py when region is created
#       
#       Created:        09/17/00 
#       Modified:       10/04/01 - Tony Evans
#       Modified:       03/15/02 - Ben Howard
#       Added to Multiplayer 12/11/03 Chris Jones
###############################################################################
import App
import MissionLib
import loadspacehelper

def Initialize(pSet):

        # Add a sun, far far away
        debug(__name__ + ", Initialize")
        pSun = App.Sun_Create(90.0, 300, 500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresBlue.tga")
        pSet.AddObjectToSet(pSun, "Sensor Anomaly")
        
        # Place the object at the specified location.
        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        # MetaNebula_Create params are:
        # r, g, b : (floats [0.0 , 1.0]) 
        # visibility distance inside the nebula (float in world units)
        # sensor density of nebula(value to scale sensor range by)
        # name of internal texture (needs alpha)
        # name of external texture (no need for alpha)
        
        pNebula = App.MetaNebula_Create(30.0 / 255.0,  30.0 / 255.0, 40.0  / 255.0, 3000.0, 1.5, "data/Backgrounds/nebulaoverlayblue.tga", "data/Backgrounds/nebulaexternalblue.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula.SetupDamage(0.1, 0.1)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula.AddNebulaSphere(100.0, 20500.0, 50.000000, 3000.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula, "Nebula1")
        
        pNebula2 = App.MetaNebula_Create(100.0 / 255.0, 100.0 / 255.0, 125.0  / 255.0, 1000.0, 5, "data/Backgrounds/nebulaoverlayblue.tga", "data/Backgrounds/nebulaexternalblue.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula2.SetupDamage(0.1, 0.1)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula2.AddNebulaSphere(100.0, 20400.0, 50.000000, 1500.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula2, "Nebula2")
        
        pNebula3 = App.MetaNebula_Create(180.0 / 255.0, 180.0 / 255.0, 220.0  / 255.0, 10.0, 10, "data/Backgrounds/nebulaoverlayblue.tga", "data/Backgrounds/nebulaexternalblue.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula3.SetupDamage(0.1, 0.1)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula3.AddNebulaSphere(100.0, 20600.0, 50.000000, 550.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula3, "Nebula3")

        if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):

                # Create our static stations and such
                pVG     = loadspacehelper.CreateShip("CardStarbase", pSet, "Vger", "evil")

                # Create our static stations and such
                pBasestar2      = loadspacehelper.CreateShip("CardStarbase", pSet, "V-ger", "evil2")

        ##      pHulk1          = loadspacehelper.CreateShip("Vorcha", pSet, "War Hammer", "wreck1")
                pHulk2          = loadspacehelper.CreateShip("BirdOfPrey", pSet, "Raptor", "wreck2")
                pHulk3          = loadspacehelper.CreateShip("BirdOfPrey", pSet, "Dagger", "wreck3")
        ##      pHulk4          = loadspacehelper.CreateShip("Nebula", pSet, "Magellan", "wreck4")
                
                # Import our damaged script ship and apply it to the Hulk2
                pHulk2.SetHailable(0)
                import DamageBoP1
                DamageBoP1.AddDamage(pHulk2)
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
                pHulk2.DamageSystem(pHulk2.GetHull(), 1500)
                pHulk2.DisableGlowAlphaMaps()
                # Dont allow the user to see the sub-systems
                MissionLib.HideSubsystems(pHulk2)
                # Spin the hulk
                MissionLib.SetRandomRotation(pHulk2, 3)
                
                # Import our damaged script ship and apply it to the Hulk3
                pHulk3.SetHailable(0)
                import DamageBoP2
                DamageBoP2.AddDamage(pHulk3)
                # Turn off the ships repair
                pRepair = pHulk3.GetRepairSubsystem()
                pProp   = pRepair.GetProperty()
                pProp.SetMaxRepairPoints(0.0)
                # Damage the Hulk3...
                # Turn off the shields
                pAlertEvent = App.TGIntEvent_Create()
                pAlertEvent.SetDestination(pHulk3)
                pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
                pAlertEvent.SetInt(pHulk3.GREEN_ALERT)
                App.g_kEventManager.AddEvent(pAlertEvent)
                # Damage the hull - 500 pts left
                pHulk3.DamageSystem(pHulk3.GetHull(), 1500)
                pHulk3.DisableGlowAlphaMaps()
                # Dont allow the user to see the sub-systems
                MissionLib.HideSubsystems(pHulk3)
                # Spin the hulk
                MissionLib.SetRandomRotation(pHulk3, 8)

        if (App.g_kUtopiaModule.IsMultiplayer()):
                pMission = MissionLib.GetMission ()
                SetupEventHandlers(pMission)
        else:
		# Setup Affiliations
                global pFriendlies
                global pEnemies
                
                pGame = App.Game_GetCurrentGame()
                pEpisode = pGame.GetCurrentEpisode()
                pMission = pEpisode.GetCurrentMission()
                pNeutrals = pMission.GetNeutralGroup()

def SetupEventHandlers(pMission):
        debug(__name__ + ", SetupEventHandlers")
        import Multiplayer.MissionShared
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_CREATED_NOTIFY, pMission, __name__ + ".ObjectCreatedHandler")

        return 0


def ObjectCreatedHandler (TGObject, pEvent):
        debug(__name__ + ", ObjectCreatedHandler")
        import Multiplayer.SpeciesToShip

        # We only care about ships.
        pShip = App.ShipClass_Cast (pEvent.GetDestination ())
        if (pShip):
                # We only care about ships.
                if (pShip.IsPlayerShip ()):
                        ResetEnemyFriendlyGroups ()
                elif (pShip.GetNetType () == Multiplayer.SpeciesToShip.FEDSTARBASE):
                        pass
        return 0

def ResetEnemyFriendlyGroups ():
        # Go through player list, trying to find all the ships

        debug(__name__ + ", ResetEnemyFriendlyGroups")
        pNetwork = App.g_kUtopiaModule.GetNetwork ()
        pGame = App.MultiplayerGame_Cast (App.Game_GetCurrentGame ())

        if (pNetwork and pGame):
                pMission = MissionLib.GetMission ()
                pEnemyGroup = MissionLib.GetEnemyGroup ()
                pNeutralGroup = pMission.GetNeutralGroup ()

                pSet = App.g_kSetManager.GetSet("CJones8")
                pVG = App.ShipClass_GetObject(pSet, "VGer")
                if pVG != None:
                   pEnemyGroup.AddName("VGer")
                   import StarbaseMPAI
                   pVG.SetAI(StarbaseMPAI.CreateAI(pVG))



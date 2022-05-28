###############################################################################
#       Filename:       Kronos1_S.py
#       
#       Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard
#       
#       Creates TheGalaxy3 static objects.  Called by Kronos1.py when region is created
#       
#       Created:        09/17/00 
#       Modified:       10/04/01 - Tony Evans
#       Modified:       08/25/02 - Ben Howard - TheGalaxy3
#       Modified:       Chris Jones - Sept. 2003 (ships added)
#       Adapted for MultiPlayer - 12/16/03 - Chris Jones
###############################################################################
import App
import loadspacehelper
import MissionLib
import Tactical.LensFlares
import SelfDefenseAI

def Initialize(pSet):

        # Add a sun, far far away
        pSun = App.Sun_Create(1500, 2000, 500, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresOrange.tga")
        pSet.AddObjectToSet(pSun, "Kling")
        
        # Place the object at the specified location.
        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()
        
        Tactical.LensFlares.YellowLensFlare(pSet, pSun)

        # Model and placement for Kronos
        pPlanet = App.Planet_Create(1202, "data/models/environment/RootBeerPlanet.nif")
        pSet.AddObjectToSet(pPlanet, "Kronos")

        #Place the object at the specified location.
        pPlanet.PlaceObjectByName("Kronos")
        pPlanet.UpdateNodeOnly()
        pPlanet.SetAtmosphereRadius(150)

        # Model and placement for Moon
        pPlanet3 = App.Planet_Create(400, "data/models/environment/BlueRockyPlanet.nif")
        pSet.AddObjectToSet(pPlanet3, "Takoth")

        #Place the object at the specified location.
        pPlanet3.PlaceObjectByName("Takoth")
        pPlanet3.UpdateNodeOnly()

        pNebula = App.MetaNebula_Create(245.0 / 255.0, 90.0 / 255.0, 105.0 / 255.0, 145.0, 10.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula.SetupDamage(1.0, 5.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula.AddNebulaSphere(301.0, 1801.0, 201.0, 250.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula, "Nebula1")
        
        if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
        
                #Klingon
                pKlingon15      = loadspacehelper.CreateShip("Vorcha", pSet, "IKV Gowron", "Klingon15 Location")
  
                #Klingon
                pKlingon16      = loadspacehelper.CreateShip("BirdOfPrey", pSet, "Son Of Worf", "Klingon16 Location")

                #Klingon
                pKlingon20      = loadspacehelper.CreateShip("Vorcha", pSet, "Lust of Lursa", "Klingon20 Location")
        

        if (App.g_kUtopiaModule.IsMultiplayer()):
                pMission = MissionLib.GetMission ()
                SetupEventHandlers(pMission)
        else:
                pKlingon15.SetAI(SelfDefenseAI.CreateAI(pKlingon15))
                pKlingon16.SetAI(SelfDefenseAI.CreateAI(pKlingon16))
                pKlingon20.SetAI(SelfDefenseAI.CreateAI(pKlingon20))       
###############################################################################
#       SetupEventHandlers()
#
#       Set up event handlers used by the Starbase 12 set.
#
#       Args:   pSet    - The Starbase 12 set.
#
#       Return: none
###############################################################################
def SetupEventHandlers(pMission):
        import Multiplayer.MissionShared
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_CREATED_NOTIFY, pMission, __name__ + ".ObjectCreatedHandler")

        return 0


def ObjectCreatedHandler (TGObject, pEvent):
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

        pNetwork = App.g_kUtopiaModule.GetNetwork ()
        pGame = App.MultiplayerGame_Cast (App.Game_GetCurrentGame ())

        if (pNetwork and pGame):
                pMission = MissionLib.GetMission ()
                pEnemyGroup = MissionLib.GetEnemyGroup ()
                pNeutralGroup = pMission.GetNeutralGroup ()
                
                pSet = App.g_kSetManager.GetSet("Kronos1")
                pKlingon15 = App.ShipClass_GetObject(pSet, "IKV Gowron")
                pKlingon16 = App.ShipClass_GetObject(pSet, "Son Of Worf")
                pKlingon20 = App.ShipClass_GetObject(pSet, "Lust of Lursa")
                if pKlingon15 != None:   
                        pKlingon15.SetAI(SelfDefenseAI.CreateAI(pKlingon15))
                if pKlingon16 != None:   
                        pKlingon16.SetAI(SelfDefenseAI.CreateAI(pKlingon16))
                if pKlingon16 != None:   
                        pKlingon20.SetAI(SelfDefenseAI.CreateAI(pKlingon20))       

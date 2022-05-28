###############################################################################
#       Filename:       Romulus1_S.py
#       
#       Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard
#       
#       Creates TheGalaxy5 static objects.  Called by Romulus1.py when region is created
#       
#       Created:        09/17/00 
#       Modified:       10/04/01 - Tony Evans
#       Modified:       08/25/02 - Ben Howard
#       Modified:       Sept. 2003 - Chris Jones
#       Modified for Multiplayer 12/16/03 Chris Jones
###############################################################################
import App
import loadspacehelper
import MissionLib
import Tactical.LensFlares
import SelfDefenseAI
##import StarbaseAI

def Initialize(pSet):

        # Add a sun, far far away
        pSun = App.Sun_Create(1000.0, 5000, 500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pSun, "Rom")
        
        # Place the object at the specified location.
        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        # Builds a Red-Orange lens flare, attached to the sun
        Tactical.LensFlares.WhiteLensFlare(pSet, pSun)

        # Model and placement for Romulus
        pPlanet = App.Planet_Create(1202, "data/models/environment/AquaPlanet.nif")
        pSet.AddObjectToSet(pPlanet, "Romulus1")

        #Place the object at the specified location.
        pPlanet.PlaceObjectByName("RomulusL")
        pPlanet.UpdateNodeOnly()
        pPlanet.SetAtmosphereRadius(150)

        # Model and placement for Moon
        pPlanet2 = App.Planet_Create(217, "data/models/environment/BlueRockyPlanet.nif")
        pSet.AddObjectToSet(pPlanet2, "Remus")

        #Place the object at the specified location.
        pPlanet2.PlaceObjectByName("MoonL")
        pPlanet2.UpdateNodeOnly()

        pNebula2 = App.MetaNebula_Create(25.0 / 255.0, 140.0 / 255.0, 85.0 / 255.0, 3000.0, 15.0, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula2.SetupDamage(1.0, 1.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula2.AddNebulaSphere(-10500.0, 1950.0, 5075.0,  5000.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula2, "Nebula2")
        
        if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):

                #Romulan
                pRomulan6       = loadspacehelper.CreateShip("Warbird", pSet, "Tal Shiar", "Romulan6 Location")
         
                #Romulan
                pRomulan8       = loadspacehelper.CreateShip("Warbird", pSet, "High Council", "Romulan8 Location")

                #Romulan
                pRomulan9       = loadspacehelper.CreateShip("Warbird", pSet, "Tasha Yar", "Romulan9 Location")

                #Romulan
                pRomulan10      = loadspacehelper.CreateShip("Warbird", pSet, "Imperial Warbird", "Romulan10 Location")



        if (App.g_kUtopiaModule.IsMultiplayer()):
                pMission = MissionLib.GetMission ()
                SetupEventHandlers(pMission)
        else:
                pRomulan6.SetAI(SelfDefenseAI.CreateAI(pRomulan6))
                pRomulan8.SetAI(SelfDefenseAI.CreateAI(pRomulan8))
                pRomulan9.SetAI(SelfDefenseAI.CreateAI(pRomulan9))    
                pRomulan10.SetAI(SelfDefenseAI.CreateAI(pRomulan10))
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

                # First clear the groups.  We will be reading everybody
                # so we want to start with an empty group.
                #pEnemyGroup.RemoveAllNames ()

                #pPlayerList = pNetwork.GetPlayerList ()
                #iNumPlayers = pPlayerList.GetNumPlayers ()

                #for i in range(iNumPlayers):
                        #pPlayer = pPlayerList.GetPlayerAtIndex (i)
                        #iPlayerID = pPlayer.GetNetID ()
                        #pShip = pGame.GetShipFromPlayerID (iPlayerID)           

                        #if (pShip):
                        #        # Good, there is a ship for this player
                        #        # Determine which team the player is on
                        #        pEnemyGroup.AddName (pShip.GetName ())

                
                pSet = App.g_kSetManager.GetSet("Romulus1")
                pRomulan6 = App.ShipClass_GetObject(pSet, "Tal Shiar")
                pRomulan8 = App.ShipClass_GetObject(pSet, "High Council")
                pRomulan9 = App.ShipClass_GetObject(pSet, "Tasha Yar")
                pRomulan10 = App.ShipClass_GetObject(pSet, "Imperial Warbird")
                if pRomulan6 != None:
                        pRomulan6.SetAI(SelfDefenseAI.CreateAI(pRomulan6))
                if pRomulan8 != None:   
                        pRomulan8.SetAI(SelfDefenseAI.CreateAI(pRomulan8))
                if pRomulan9 != None:   
                        pRomulan9.SetAI(SelfDefenseAI.CreateAI(pRomulan9))    
                if pRomulan10 != None:   
                        pRomulan10.SetAI(SelfDefenseAI.CreateAI(pRomulan10))

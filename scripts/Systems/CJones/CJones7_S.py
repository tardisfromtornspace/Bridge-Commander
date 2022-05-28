###############################################################################
#       Filename:       CJones7_S.py
#       
#       Confidential and Proprietary, Copyright 2001 by Totally Games
#       
#       Creates Proxima Centauri static objects.  Called by CJones7.py when region is created
#       
#       Created:        09/17/00 
#       Modified:       10/04/01 - Tony Evans
#                       August 2003 - Chris Jones
#       MultiPlayer:    December 2003 - Chris Jones
###############################################################################
import App
import Tactical.LensFlares
import loadspacehelper
import MissionLib
import SelfDefenseAI

def Initialize(pSet):

        pSun = App.Sun_Create(8200.0, 6000, 1000, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
        pSet.AddObjectToSet(pSun, "Proxima Centauri")   
        pSun.PlaceObjectByName( "Proxima Centauri" )
        pSun.UpdateNodeOnly()
        Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun)
        
        pRigil = App.Sun_Create(200.0, 500, 1000, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pRigil, "Rigil Kentaurus")  
        pRigil.PlaceObjectByName( "Rigil Kentaurus" )
        pRigil.UpdateNodeOnly()         
        
        pACB = App.Sun_Create(200.0, 500, 900, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pACB, "Alpha Centauri B")   
        pACB.PlaceObjectByName( "Alpha Centauri B" )
        pACB.UpdateNodeOnly()   
        
        # Model and placement for Proxima1
        pPlanet1 = App.Planet_Create(100.0, "data/models/environment/IcePlanet.NIF")
        pSet.AddObjectToSet(pPlanet1, "Proxima 1")
        pPlanet1.PlaceObjectByName("Proxima 1")
        pPlanet1.UpdateNodeOnly()
        
        if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
        
                pStellarCosmos = loadspacehelper.CreateShip("Transport", pSet, "Stellar Cosmos", "Stellar Cosmos locale")

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
                pNeutrals.AddName("Stellar Cosmos")
                pStellarCosmos.SetAI(SelfDefenseAI.CreateAI(pStellarCosmos))

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

                pSet = App.g_kSetManager.GetSet("CJones7")
                pStellarCosmos = App.ShipClass_GetObject(pSet, "Stellar Cosmos")
                if pStellarCosmos != None:
                   pNeutralGroup.AddName("Stellar Cosmos")           
                   pStellarCosmos.SetAI(SelfDefenseAI.CreateAI(pStellarCosmos))

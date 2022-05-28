###############################################################################
#       Filename:       CJones1_S.py
#       
#       Confidential and Proprietary, Copyright 2001 by Totally Games
#       
#       Creates CJones1 static objects.  Called by CJones1.py when region is created
#       
#       Created:        09/17/00 
#       Modified:       10/04/01 - Tony Evans
#                       June/August 2003 - Chris Jones
#       Multiplayer version 12/10/03 Chris Jones
###############################################################################
import App
import Tactical.LensFlares
import loadspacehelper
import MissionLib
import SelfDefenseAI

def Initialize(pSet):

#       To create a colored sun:
#       pSun = App.Sun_Create(fRadius, fAtmosphereThickness, fDamagePerSec, fBaseTexture , fFlareTexture)
#
#       for fBaseTexture you can use:
#               data/Textures/SunBase.tga 
#               data/Textures/SunRed.tga
#               data/Textures/SunRedOrange.tga
#               data/Textures/SunYellow.tga
#               data/Textures/SunBlueWhite.tga
#       for fFlareTexture you can use:
#               data/Textures/Effects/SunFlaresOrange.tga
#               data/Textures/Effects/SunFlaresRed.tga
#               data/Textures/Effects/SunFlaresRedOrange.tga
#               data/Textures/Effects/SunFlaresYellow.tga
#               data/Textures/Effects/SunFlaresBlue.tga
#               data/Textures/Effects/SunFlaresWhite.tga

        # Add a sun, far far away
        pSun = App.Sun_Create(3000.0, 1000, 500)
        pSet.AddObjectToSet(pSun, "Sun 1")      
        pSun.PlaceObjectByName( "Sun59" )
        pSun.UpdateNodeOnly()

        pSun2 = App.Sun_Create(4000.0, 5000, 900, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
        pSet.AddObjectToSet(pSun2, "Sun 2")
        
        # Place the object at the specified location.
        pSun2.PlaceObjectByName( "Sun63" )
        pSun2.UpdateNodeOnly()

        # Builds a Red-Orange lens flare, attached to the sun
        Tactical.LensFlares.YellowLensFlare(pSet, pSun)

        # Model and placement for CJones
        pPlanet1 = App.Planet_Create(200.0, "data/models/environment/AquaPlanet.nif")
        pSet.AddObjectToSet(pPlanet1, "CJones")
        pPlanet1.PlaceObjectByName("Planet Location")
        pPlanet1.UpdateNodeOnly()
                
        # Model and placement for Wife
        pPlanet2 = App.Planet_Create(200.0, "data/models/environment/AquaPlanet.nif")
        pSet.AddObjectToSet(pPlanet2, "Wife")
        
        #Place the object at the specified location.
        pPlanet2.PlaceObjectByName("Wife Location")
        pPlanet2.UpdateNodeOnly()
        
        # Model and placement for Son
        pPlanet3 = App.Planet_Create(140.0, "data/models/environment/RedPlanet.nif")
        pSet.AddObjectToSet(pPlanet3, "Son")
                
        #Place the object at the specified location.
        pPlanet3.PlaceObjectByName("Son Location")
        pPlanet3.UpdateNodeOnly()
        
        # Model and placement for Daughter
        pPlanet4 = App.Planet_Create(160.0, "data/models/environment/SlimeGreenPlanet.nif")
        pSet.AddObjectToSet(pPlanet4, "Daughter")
                        
        #Place the object at the specified location.
        pPlanet4.PlaceObjectByName("Daughter Location")
        pPlanet4.UpdateNodeOnly()

        # Model and placement for Red Giant Planet
        pPlanet5 = App.Planet_Create(2000.0, "data/models/environment/PurplePlanet.nif")
        pSet.AddObjectToSet(pPlanet5, "Uncharted")
                        
        #Place the object at the specified location.
        pPlanet5.PlaceObjectByName("Red Planet Location")
        pPlanet5.UpdateNodeOnly()

        if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
                # Create ship
                pTransport1 = loadspacehelper.CreateShip("Shuttle", pSet, "Solar Science", "Solar Science Location")
         
                # Create ship
                pFreighter1 = loadspacehelper.CreateShip("Transport", pSet, "Supply Ship", "Supply Ship Location")

                # Create ship
                pFreighter3 = loadspacehelper.CreateShip("Transport", pSet, "Playstation XVII", "Playstation")
        
                pPhasers = pFreighter3.GetPhaserSystem()
                pMax    = pPhasers.GetMaxCondition()    
                sPhaser = pMax * 0.5    
                pFreighter3.DamageSystem(pFreighter3.GetPhaserSystem(), sPhaser)

                pRenegade = loadspacehelper.CreateShip("Transport", pSet, "Renegade", "Renegade locale")
        
                # Create a Communications Relay
                pArray  = loadspacehelper.CreateShip("CommArray", pSet, "Comm Array", "Array Location")
                pArray.SetTargetable(0) 
        
                # Create a Communications Relay
                pArray2 = loadspacehelper.CreateShip("CommLight", pSet, "Comm Array 2", "Array 2 Location")
                pArray2.SetTargetable(1)

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
                pFriendlies = MissionLib.GetFriendlyGroup() 
                pEnemies = MissionLib.GetEnemyGroup()
                pNeutrals = pMission.GetNeutralGroup()
                pNeutrals.AddName("Supply Ship")
                pNeutrals.AddName("Playstation XVII")
                pNeutrals.AddName("Solar Science")
                pEnemies.AddName("Renegade")

                import AttackNoWarpAI
                pRenegade.SetAI(AttackNoWarpAI.CreateAI(pRenegade))
                pTransport1.SetAI(SelfDefenseAI.CreateAI(pTransport1)) 
                pFreighter1.SetAI(SelfDefenseAI.CreateAI(pFreighter1))
                import RouteAI
                pFreighter3.SetAI(RouteAI.CreateAI(pFreighter3, pPlanet1, pPlanet2))

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
                pFriendlyGroup = MissionLib.GetFriendlyGroup()
                pNeutralGroup = pMission.GetNeutralGroup ()

                pSet = App.g_kSetManager.GetSet("CJones1")
                pPlanet1 = App.Planet_GetObject(pSet, "CJones")
                pPlanet2 = App.Planet_GetObject(pSet, "Wife")
                pSolar = App.ShipClass_GetObject(pSet, "Solar Science")
                pSupply = App.ShipClass_GetObject(pSet, "Supply Ship")
                pPlaystation = App.ShipClass_GetObject(pSet, "Playstation XVII")
                pRenegade = App.ShipClass_GetObject(pSet, "Renegade")
                if pRenegade != None:
                   pFriendlyGroup.AddName("Renegade")
                   import AttackNoWarpAI
                   pRenegade.SetAI(AttackNoWarpAI.CreateAI(pRenegade))     
                if pSolar != None:   
                   pNeutralGroup.AddName("Solar Science")
                   pSolar.SetAI(SelfDefenseAI.CreateAI(pSolar))
                if pSupply != None:   
                   pNeutralGroup.AddName("Supply Ship")
                   pSupply.SetAI(SelfDefenseAI.CreateAI(pSupply))
                if pPlaystation != None:   
                   pNeutralGroup.AddName("Playstation XVII")     
                   import RouteAI
                   pPlaystation.SetAI(RouteAI.CreateAI(pPlaystation, pPlanet1, pPlanet2))

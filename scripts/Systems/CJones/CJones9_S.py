###############################################################################
#       Original Filename:     JLWMP1_S.py -- jwatts test system. Converted to CJones9_S.py
#       
#       Confidential and Proprietary, Copyright 2001 by Totally Games
#       
#       Creates JLWMP 1 static objects.  Called by JLWMP1.py when region is created
#       
#       Created:        10/02/01 - Tony Evans (Added Header)
#       Modified:       10/04/01 - Tony Evans
# Modified for MultiPlayer Dec. 2003 - Chris Jones
###############################################################################
import App
import loadspacehelper
import MissionLib
import Tactical.LensFlares
import SelfDefenseAI
import BadGuysAI
import Akira1AI
import Akira2AI

def Initialize(pSet):
        pSun = App.Sun_Create(500.0, 17000, 6000, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresBlue.tga")
        pSet.AddObjectToSet(pSun, "White Blue Giant")   
        pSun.PlaceObjectByName( "White Blue Giant" )
        pSun.UpdateNodeOnly()
        Tactical.LensFlares.BlueLensFlare(pSet, pSun)
        
        # Add a sun, far far away
        pSun2 = App.Sun_Create(6.0, 12, 500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
        pSet.AddObjectToSet(pSun2, "Protostar 2")
        
        # Place the object at the specified location.
        pSun2.PlaceObjectByName( "Sun2" )
        pSun2.UpdateNodeOnly()

        # Add a sun, far far away
        pSun3 = App.Sun_Create(8.0, 25, 500, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pSun3, "Protostar 3")
        
        # Place the object at the specified location.
        pSun3.PlaceObjectByName( "Sun3" )
        pSun3.UpdateNodeOnly()

        # Add a sun, far far away
        pSun4 = App.Sun_Create(3.0, 10, 500, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresWhite.tga")
        pSet.AddObjectToSet(pSun4, "Protostar 4")
        
        # Place the object at the specified location.
        pSun4.PlaceObjectByName( "Sun4" )
        pSun4.UpdateNodeOnly()

        # Add a sun, far far away
        pSun5 = App.Sun_Create(3.0, 15, 500, "data/Textures/SunPurple.tga", "data/Textures/Effects/SunFlaresOrange.tga")
        pSet.AddObjectToSet(pSun5, "Protostar 5")
        
        # Place the object at the specified location.
        pSun5.PlaceObjectByName( "Sun5" )
        pSun5.UpdateNodeOnly()

        # Add a sun, far far away
        pSun6 = App.Sun_Create(20.0, 400, 500, "data/Textures/SunGreen.tga", "data/Textures/Effects/SunFlaresWhite.tga")
        pSet.AddObjectToSet(pSun6, "Protostar 6")
        
        # Place the object at the specified location.
        pSun6.PlaceObjectByName( "Sun6" )
        pSun6.UpdateNodeOnly()

        # Add a sun, far far away
        pSun7 = App.Sun_Create(7.0, 25, 500, "data/Textures/SunBrown.tga", "data/Textures/Effects/SunFlaresWhite.tga")
        pSet.AddObjectToSet(pSun7, "Protostar 7")
        
        # Place the object at the specified location.
        pSun7.PlaceObjectByName( "Sun7" )
        pSun7.UpdateNodeOnly()

        # Add a sun, far far away
        pSun8 = App.Sun_Create(5.0, 1250, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresRed.tga")
        pSet.AddObjectToSet(pSun8, "Protostar 8")
        
        # Place the object at the specified location.
        pSun8.PlaceObjectByName( "Sun8" )
        pSun8.UpdateNodeOnly()  
        
        if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
                # Create a Communications Relay
                pArray  = loadspacehelper.CreateShip("CommArray", pSet, "Comm Array", "Array Location")
                pArray.SetTargetable(1) 
                
                # Create ship
                pWarbird = loadspacehelper.CreateShip("Warbird", pSet, "RIS Tomalok", "Warbird Location")
                
                # Create ship
                pAkira  = loadspacehelper.CreateShip("Akira", pSet, "Akira", "Akira Location")
                
                # Create ship
                pAkira2 = loadspacehelper.CreateShip("Akira", pSet, "Akira2", "Akira2 Location")
                
                # Create ship
                pWarbird2 = loadspacehelper.CreateShip("Warbird", pSet, "Tasha Yar", "Warbird2 Location")
                
                # Create ship
                pKeldon = loadspacehelper.CreateShip("Keldon", pSet, "Cardassia II", "Keldon Location")

                # Create ship
                pKeldon2 = loadspacehelper.CreateShip("Keldon", pSet, "Dukat Revenge", "Keldon2 Location")
                
                # Create ship
                pTransportF = loadspacehelper.CreateShip("Transport", pSet, "SS Xhosa", "Freighter Location")

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
		pEnemies = pMission.GetEnemyGroup()
                pNeutrals.AddName("SS Xhosa")
                pEnemies.AddName("RIS Tomalok")

                # Set up AI's
                import AttackAI
                pWarbird.SetAI(AttackAI.CreateAI(pWarbird))
                pAkira.SetAI(Akira1AI.CreateAI(pAkira)) 
                pAkira2.SetAI(Akira2AI.CreateAI(pAkira2))               
                pWarbird2.SetAI(BadGuysAI.CreateAI(pWarbird2))
                pKeldon.SetAI(BadGuysAI.CreateAI(pKeldon))
                pKeldon2.SetAI(SelfDefenseAI.CreateAI(pKeldon2)) 
                pTransportF.SetAI(SelfDefenseAI.CreateAI(pTransportF))      

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
                pNeutralGroup = pMission.GetNeutralGroup()
                
                pSet = App.g_kSetManager.GetSet("CJones9")
                pWarbird = App.ShipClass_GetObject(pSet, "RIS Tomalok")
                pAkira = App.ShipClass_GetObject(pSet, "Akira")
                pAkira2 = App.ShipClass_GetObject(pSet, "Akira2")
                pWarbird2 = App.ShipClass_GetObject(pSet, "Tasha Yar")
                pKeldon = App.ShipClass_GetObject(pSet, "Cardassia II")
                pKeldon2 = App.ShipClass_GetObject(pSet, "Dukat Revenge")
                pTransportF = App.ShipClass_GetObject(pSet, "SS Xosha")
                pArray = App.ShipClass_GetObject(pSet, "Comm Array")
                import AttackAI
                if pWarbird != None:
                   pEnemyGroup.AddName("RIS Tomalok")
                   pWarbird.SetAI(AttackAI.CreateAI(pWarbird))
                if pAkira != None:
                   pAkira.SetAI(Akira1AI.CreateAI(pAkira)) 
                if pAkira2 != None:
                   pAkira2.SetAI(Akira2AI.CreateAI(pAkira2))
                if pWarbird2 != None:
                   pWarbird2.SetAI(AttackAI.CreateAI(pWarbird2))
                if pKeldon != None:
                   pKeldon.SetAI(BadGuysAI.CreateAI(pKeldon))
                if pKeldon2 != None:
                   pKeldon2.SetAI(SelfDefenseAI.CreateAI(pKeldon2)) 
                if pTransportF != None:
                   pNeutralGroup.AddName("SS Xhosa")
                   pTransportF.SetAI(SelfDefenseAI.CreateAI(pTransportF))
                if pArray != None:
                   pNeutralGroup.AddName("Comm Array")   

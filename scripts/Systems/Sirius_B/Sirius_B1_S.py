from bcdebug import debug
###############################################################################
#       Filename:       Sirius_B1_S.py
#       
#       Confidential and Proprietary, Copyright 2001 by Totally Games
#       
#       Creates Sirius_B static objects.  Called by Sirius_B1.py when region is created
#       
#       Created:        09/17/00 
#       Modified:       10/04/01 - Tony Evans
#                       August 2003 for BC2 - Chris Jones/Jeff Watts, Jr
# Modified for the Multi-Player all out inter-race war Dec. 2003 - Chris Jones
###############################################################################
import App
import Tactical.LensFlares
import loadspacehelper
import MissionLib

def Initialize(pSet):
 ##     pSun = App.Sun_Create(79428.57, 14000.0, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        debug(__name__ + ", Initialize")
        pSun = App.Sun_Create(1350.2857, 2380.0, 700, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
        pSet.AddObjectToSet(pSun, "Sirius A")

        # Place the object at the specified location.
        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

 ##     pSun2 = App.Sun_Create(79.42857, 14.0000, 100, "data/Textures/SunWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
        pSun2 = App.Sun_Create(13502.57, 2380.0, 700, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
        pSet.AddObjectToSet(pSun2, "Sirius B")

        # Place the object at the specified location.
        pSun2.PlaceObjectByName( "Sun2" )
        pSun2.UpdateNodeOnly()  
        
        if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
                # Create a Communications Relay
                pArray  = loadspacehelper.CreateShip("CommArray", pSet, "Comm Array", "Array Location")
                                
                # Create ship
                pWarbird = loadspacehelper.CreateShip("Warbird", pSet, "Tasha II", "Warbird Location")
                
                # Create ship
                pAkira  = loadspacehelper.CreateShip("Sovereign", pSet, "USS Sovereign", "Akira Location") 
                
                # Create ship
                pAkira2 = loadspacehelper.CreateShip("KessokHeavy", pSet, "Kessok", "Akira2 Location")               
                
                # Create ship
                pWarbird2 = loadspacehelper.CreateShip("Vorcha", pSet, "IKV Worf", "Warbird2 Location")
                
                # Create ship
                pKeldon = loadspacehelper.CreateShip("Keldon", pSet, "Liberator", "Keldon Location")

                # Create ship
                pKeldon2 = loadspacehelper.CreateShip("CardHybrid", pSet, "Dukat Revenge", "Keldon2 Location") 
                
                # Create ship
                pTransportF = loadspacehelper.CreateShip("Transport", pSet, "SS Xhosa II", "Freighter Location")
                
     

        if (App.g_kUtopiaModule.IsMultiplayer()):
                pMission = MissionLib.GetMission ()
        else:
                # Setup Affiliations
                pFriendlies = MissionLib.GetFriendlyGroup()
                pEnemies = MissionLib.GetEnemyGroup()
                
                pGame = App.Game_GetCurrentGame()
                pEpisode = pGame.GetCurrentEpisode()
                pMission = pEpisode.GetCurrentMission()
                pEnemies.AddName("Tasha II")
                pEnemies.AddName("USS Sovereign")
                pEnemies.AddName("Kessok")
                pEnemies.AddName("IKV Worf")
                pEnemies.AddName("Liberator")
                pEnemies.AddName("Dukat Revenge")
                pEnemies.AddName("SS Xhosa II")          

                # Set up AI's
                import AttackAI
                import AttackAIE
                pWarbird.SetAI(AttackAI.CreateAI(pWarbird))
                pAkira.SetAI(AttackAI.CreateAI(pAkira))
                pAkira2.SetAI(AttackAI.CreateAI(pAkira2))
                pWarbird2.SetAI(AttackAI.CreateAI(pWarbird2))
                pKeldon.SetAI(AttackAIE.CreateAI(pKeldon))
                pKeldon2.SetAI(AttackAIE.CreateAI(pKeldon2))
                pTransportF.SetAI(AttackAI.CreateAI(pTransportF))

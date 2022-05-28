from bcdebug import debug
###############################################################################
#       Filename:       CJones4_S.py
#       
#       Confidential and Proprietary, Copyright 2001 by Totally Games
#       
#       Creates Proxima Centauri static objects.  Called by CJones4.py when region is created
#       
#       Created:        09/17/00 
#       Modified:       10/04/01 - Tony Evans
#                       August 2003 - Chris Jones
#       Added to MultiPlayer 12/10/03 Chris Jones
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
#       Lensflares available:
#               Tactical.LensFlares.RedOrangeLensFlare
#               Tactical.LensFlares.YellowLensFlare
#               Tactical.LensFlares.BlueLensFlare
#               Tactical.LensFlares.WhiteLensFlare


        debug(__name__ + ", Initialize")
        pSun = App.Sun_Create(1200.0, 4000, 4000, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
        pSet.AddObjectToSet(pSun, "Barnard's Star")     
        pSun.PlaceObjectByName( "Barnard's Star" )
        pSun.UpdateNodeOnly()
        Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun)
        
        pSpot = App.Sun_Create(102.0, 1000, 2000, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresBlue.tga")
        pSet.AddObjectToSet(pSpot, "Barnard's Spot")    
        pSpot.PlaceObjectByName( "Barnard's Spot" )
        pSpot.UpdateNodeOnly()
        Tactical.LensFlares.BlueLensFlare(pSet, pSpot)
        
        pProx = App.Sun_Create(100.0, 1000, 1000, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
        pSet.AddObjectToSet(pProx, "Proxima Centauri")  
        pProx.PlaceObjectByName( "Proxima Centauri" )
        pProx.UpdateNodeOnly()
        Tactical.LensFlares.RedOrangeLensFlare(pSet, pProx)
        
        pRigil = App.Sun_Create(100.0, 200, 1000, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pRigil, "Rigil Kentaurus")  
        pRigil.PlaceObjectByName( "Rigil Kentaurus" )
        pRigil.UpdateNodeOnly()
        Tactical.LensFlares.YellowLensFlare(pSet, pRigil)
        
        pACB = App.Sun_Create(100.0, 200, 900, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pACB, "Alpha Centauri B")   
        pACB.PlaceObjectByName( "Alpha Centauri B" )
        pACB.UpdateNodeOnly()
        Tactical.LensFlares.YellowLensFlare(pSet, pACB)
        
        if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
        
                pSolarData = loadspacehelper.CreateShip("Shuttle", pSet, "Solar Data", "SD")

                pCard = loadspacehelper.CreateShip("Galor", pSet, "Galorize", "Galorize locale")
                
        if (App.g_kUtopiaModule.IsMultiplayer()):
                pMission = MissionLib.GetMission ()
                SetupEventHandlers(pMission)
        else:                   
                # Setup Affiliations 
                pFriendlies = MissionLib.GetFriendlyGroup()
                pEnemies = MissionLib.GetEnemyGroup()
                        
                pGame = App.Game_GetCurrentGame() 
                pEpisode = pGame.GetCurrentEpisode() 
                pMission = pEpisode.GetCurrentMission() 
                pNeutrals = pMission.GetNeutralGroup() 
                pNeutrals.AddName("Solar Data")
                pEnemies.AddName("Galorize")

                import AttackNoWarpAI
                pCard.SetAI(AttackNoWarpAI.CreateAI(pCard))
                pSolarData.SetAI(SelfDefenseAI.CreateAI(pSolarData))

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

                pSet = App.g_kSetManager.GetSet("CJones4")
                pSolarData = App.ShipClass_GetObject(pSet, "Solar Data")
                pCard = App.ShipClass_GetObject(pSet, "Galorize")                
                if pCard != None:
                   pEnemyGroup.AddName("Galorize")
                   import AttackNoWarpAI
                   pCard.SetAI(AttackNoWarpAI.CreateAI(pCard))
                if pSolarData != None:   
                   pNeutralGroup.AddName("Solar Data")
                   pSolarData.SetAI(SelfDefenseAI.CreateAI(pSolarData))    

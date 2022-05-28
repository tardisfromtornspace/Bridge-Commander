###############################################################################
#       Filename:       CJones3_S.py
#       
#       Confidential and Proprietary, Copyright 2001 by Totally Games
#       
#       Creates Procyon static objects.  Called by CJones3.py when region is created
#       
#       Created:        09/17/00 
#       Modified:       10/04/01 - Tony Evans
#                       August 2003 - Chris Jones
#       MultiPlayer 12/16/03 - Chris Jones
###############################################################################
import App
import Tactical.LensFlares
import MissionLib
import loadspacehelper
import SelfDefenseAI

def Initialize(pSet):

        pProA = App.Sun_Create(800.0, 4000, 2000, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresWhite.tga")
        pSet.AddObjectToSet(pProA, "Procyon A") 
        pProA.PlaceObjectByName( "Procyon A" )
        pProA.UpdateNodeOnly()
        Tactical.LensFlares.YellowLensFlare(pSet, pProA)
        
        pProB = App.Sun_Create(300.0, 700, 2000, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
        pSet.AddObjectToSet(pProB, "Procyon B") 
        pProB.PlaceObjectByName( "Procyon B" )
        pProB.UpdateNodeOnly()
        Tactical.LensFlares.WhiteLensFlare(pSet, pProB)
        
        # Asteroid Field Position "Asteroid Field 1"
        kThis = App.AsteroidFieldPlacement_Create("Asteroid Field 1", pSet.GetName(), None)
        kThis.SetStatic(0)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-1000.05, 9000.02, 710.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.000000, 0.997209, -0.074666)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.000345, 0.074666, 0.997209)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetFieldRadius(5200.0000)
        kThis.SetNumTilesPerAxis(3)
        kThis.SetNumAsteroidsPerTile(12)
        kThis.SetAsteroidSizeFactor(9.000000)
        kThis.UpdateNodeOnly()
        kThis.ConfigField()
        kThis.Update(0)
        kThis = None
        # End position "Asteroid Field 1"       
        
        if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
        
                pFreighter = loadspacehelper.CreateShip("Transport", pSet, "Solar Observer", "SO")
                pVorcha = loadspacehelper.CreateShip("Vorcha", pSet, "Gowron II", "Gowron locale")
                
        
        if (App.g_kUtopiaModule.IsMultiplayer()):
                pMission = MissionLib.GetMission ()
                SetupEventHandlers(pMission)
        else:
                pFreighter.SetAI(SelfDefenseAI.CreateAI(pFreighter))
                pVorcha.SetAI(SelfDefenseAI.CreateAI(pVorcha))

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

                pSet = App.g_kSetManager.GetSet("CJones3")
                pFreighter = App.ShipClass_GetObject(pSet, "Solar Observer")
                pVorcha = App.ShipClass_GetObject(pSet, "Gowron II")
                if pFreighter != None:
                        pFreighter.SetAI(SelfDefenseAI.CreateAI(pFreighter))
                if pVorcha != None:
                        pVorcha.SetAI(SelfDefenseAI.CreateAI(pVorcha))

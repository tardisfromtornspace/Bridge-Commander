# by Sov

import App
import loadspacehelper
import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXShips, DS9FXLifeSupportLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

def ReinforcementHandler():
    reload(DS9FXSavedConfig)
    if not DS9FXSavedConfig.FoundersReinforcements == 1:
        return
        
    DialogueWarn()
    ShipCountdown()
    
def DialogueWarn():
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    pDatabase = pMission.SetDatabase("data/TGL/DS9FXDialogueDatabase.tgl")
    pSequence = App.TGSequence_Create()
    pSet = App.g_kSetManager.GetSet("bridge")
    pCharacter = App.CharacterClass_GetObject(pSet, "Science")
    pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SAY_LINE, "StrikeForce", None, 0, pDatabase))
    pSequence.Play()

def ShipCountdown():
    i = GetRandomNumber(120, 1)
    pSequence = App.TGSequence_Create()
    pAction = App.TGScriptAction_Create(__name__, "ShipArrival")
    pSequence.AddAction(pAction, None, i)
    i = i+2
    pAction = App.TGScriptAction_Create(__name__, "DialogueEnemyArrival")
    pSequence.AddAction(pAction, None, i)
    pSequence.Play()

def DialogueEnemyArrival(pAction):
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    pDatabase = pMission.SetDatabase("data/TGL/DS9FXDialogueDatabase.tgl")
    pSequence = App.TGSequence_Create()
    pSet = App.g_kSetManager.GetSet("bridge")
    pCharacter = App.CharacterClass_GetObject(pSet, "Tactical")
    pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SAY_LINE, "EnemiesEnteringTheSet", None, 0, pDatabase))
    pSequence.Play()

    return 0

def ShipArrival(pAction):
    sSet = __import__("Systems.DS9FXFoundersHomeworld.DS9FXFoundersHomeworld1")
    pSet = sSet.GetSet()           

    reload(DS9FXSavedConfig)
    
    if DS9FXSavedConfig.DominionSide == 1:
        iCount = GetRandomNumber(9,2)
        for i in range(1, iCount):
                sShip = "Bugship Patrol " + str(i)
                pShip = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, sShip, "Dummy Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(sShip)
                pMission.GetFriendlyGroup().AddName(sShip)

                import Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI
                pShip = MissionLib.GetShip(sShip, pSet) 
                pShip = App.ShipClass_Cast(pShip)
                pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI.CreateAI(pShip))

                pPlayer = MissionLib.GetPlayer()
                pLocation = pPlayer.GetWorldLocation()
                pX = pLocation.GetX()
                pY = pLocation.GetY()
                pZ = pLocation.GetZ()
                adX = GetRandomNumber(300, 100)
                adY = GetRandomNumber(300, 100)
                adZ = GetRandomNumber(300, 100)
                pX = pX + adX
                pY = pY + adY
                pZ = pZ + adZ
                pShip.SetTranslateXYZ(pX, pY, pZ)
                pShip.UpdateNodeOnly()

    else:
        iCount = GetRandomNumber(9,2)
        for i in range(1, iCount):
                sShip = "Bugship Patrol " + str(i)
                pShip = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, sShip, "Dummy Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(sShip)
                pMission.GetEnemyGroup().AddName(sShip)

                import Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI
                pShip = MissionLib.GetShip(sShip, pSet) 
                pShip = App.ShipClass_Cast(pShip)
                pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI.CreateAI(pShip))

                pPlayer = MissionLib.GetPlayer()
                pLocation = pPlayer.GetWorldLocation()
                pX = pLocation.GetX()
                pY = pLocation.GetY()
                pZ = pLocation.GetZ()
                adX = GetRandomNumber(300, 100)
                adY = GetRandomNumber(300, 100)
                adZ = GetRandomNumber(300, 100)
                pX = pX + adX
                pY = pY + adY
                pZ = pZ + adZ
                pShip.SetTranslateXYZ(pX, pY, pZ)
                pShip.UpdateNodeOnly()

    return 0

def GetRandomNumber(iNum, iStat):
    return App.g_kSystemWrapper.GetRandomNumber(iNum) + iStat

"""
Here it is finally, fully integrated into the DS9FX Module

by USS Sovereign
"""

import App
import MissionLib
from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents
from Custom.DS9FX.DS9FXLib import DS9FXShips, DS9FXMenuLib, DS9FXPrintTextLib
from Custom.DS9FX import DS9FXmain

iWormholeAnimated = 0


def KillManualEntry():
    MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "ManualEntryAnimation")
    MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "ManualEntrySwap")
    MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "FacingTheWormhole")


def ManualEntryHandler():
    pPlayer = App.Game_GetCurrentPlayer()    	
    if not pPlayer:
        return 0

    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()

    # Any duplicates?
    KillManualEntry()

    pDS9FXWormhole = "Bajoran Wormhole Navpoint"

    pSet = pPlayer.GetContainingSet()

    sPlayerName = pPlayer.GetName()

    lNoEnter = ["Bajoran Wormhole", "USS Excalibur", "Deep_Space_9", "USS Defiant",
                "USS Oregon", "USS_Lakota", "Bugship 1", "Bugship 2", "Bugship 3",
                "Comet Alpha", "Bajoran Wormhole Navpoint", "Bajoran Wormhole Dummy",
                "Sensor Anomaly", "Unknown Nebula", "Unknown Anomaly", "MVAMTemp", 
                "Verde", "Guadiana", "Lankin", "Maroni", "Kuban", "Paraguay", "Tigris"]

    if sPlayerName in lNoEnter:
        ShowNoEnterMessage()
        print "DS9FX: System specific objects cannot enter the wormhole, manual wormhole entry shutting down..."
        return

    DS9FXmain.ScaleWormholePrevention = 0

    DistanceCheckCondition = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 50, pPlayer.GetName(), pDS9FXWormhole)
    MissionLib.CallFunctionWhenConditionChanges(pMission, __name__, "ManualEntryAnimation", DistanceCheckCondition)

def ShowNoEnterMessage():
    sText = "We won't be able to enter wormhole with this ship sir."
    iPos = 6
    iFont = 12
    iDur = 5
    iDelay = 1
    DS9FXPrintTextLib.PrintText(sText, iPos, iFont, iDur, iDelay)
    
def ManualEntryAnimation(bInRange):
    global iWormholeAnimated

    iWormholeAnimated = 1
    KillManualEntry()

    pPlayer = App.Game_GetCurrentPlayer()    	
    if not pPlayer:
        return 0

    pSet = pPlayer.GetContainingSet()

    pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)

    pDS9FXWormhole.SetScale(0.01)
    pDS9FXWormhole.SetHidden(1)

    pPlayerBackward = pPlayer.GetWorldBackwardTG()
    pPlayerDown = pPlayer.GetWorldDownTG()

    pDS9FXWormhole.AlignToVectors(pPlayerBackward, pPlayerDown)
    pDS9FXWormhole.UpdateNodeOnly()

    DummyProperties()

    TimerHandlingProperties(None, None)

    App.g_kSoundManager.PlaySound("DS9FXWormOpen")

    from Custom.DS9FX.DS9FXWormholeFlash.DS9FXEnterWormholeFlash import StartGFX, CreateGFX

    StartGFX()
    for i in range(1):
        CreateGFX(pDS9FXWormhole)

    pDS9FXWormhole.SetHidden(0)

    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), "Custom.DS9FX.DS9FXmain" + ".ScaleWormhole", App.g_kUtopiaModule.GetGameTime() + 2, 0, 0)


def TimerHandlingProperties(pObject, pEvent):
    global iWormholeAnimated

    pPlayer = App.Game_GetCurrentPlayer()    	
    if not pPlayer:
        return 0

    pSet = pPlayer.GetContainingSet()

    pDS9FXNav = MissionLib.GetShip("Bajoran Wormhole Navpoint", pSet)

    if iWormholeAnimated == 1:

        # So you decided not to enter the wormhole?
        if DistanceCheck(pDS9FXNav) >= 65:
            DS9FXmain.ScaleWormholePrevention = 1
            iWormholeAnimated = 2

        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".TimerHandlingProperties", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)

    elif iWormholeAnimated == 2:
        # We've been called once so just on the next timer run, don't do anything
        iWormholeAnimated = 0

        DS9FXmain.ScaleWormholePrevention = 1

        KillManualEntry()

        from Custom.DS9FX.DS9FXLib import DS9FXManualEntryHelperLib

        DS9FXManualEntryHelperLib.StartScaling()

        ManualEntryHandler()


def DummyProperties():    
    pPlayer = App.Game_GetCurrentPlayer()    	
    if not pPlayer:
        return 0

    pSet = pPlayer.GetContainingSet()

    pDS9FXWormholeDummy = MissionLib.GetShip("Bajoran Wormhole Navpoint", pSet)

    pPlayerBackward = pPlayer.GetWorldBackwardTG()
    pPlayerDown = pPlayer.GetWorldDownTG()

    pDS9FXWormholeDummy.AlignToVectors(pPlayerBackward, pPlayerDown)
    pDS9FXWormholeDummy.UpdateNodeOnly()

    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()

    pDS9FXWormhole = "Bajoran Wormhole Navpoint"

    DistanceCheckCondition = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 5, pPlayer.GetName(), pDS9FXWormhole)
    MissionLib.CallFunctionWhenConditionChanges(pMission, __name__, "FacingTheWormhole", DistanceCheckCondition)


def FacingTheWormhole(bFacing):
    pPlayer = App.Game_GetCurrentPlayer()    	
    if not pPlayer:
        return 0

    pSet = pPlayer.GetContainingSet()

    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()

    pDS9FXWormhole = "Bajoran Wormhole"

    # Now... we must be absolutely certain that you are facing the mouth of the wormhole!    
    FaceTheWormhole = App.ConditionScript_Create("Conditions.ConditionFacingToward", "ConditionFacingToward", pDS9FXWormhole, pPlayer.GetName(), 45.0, App.TGPoint3_GetModelForward(), 1)
    MissionLib.CallFunctionWhenConditionChanges(pMission, __name__, "ManualEntrySwap", FaceTheWormhole)


def ManualEntrySwap(bInRange):
    global iWormholeAnimated

    pPlayer = App.Game_GetCurrentPlayer()    	
    if not pPlayer:
        return 0

    pSet = pPlayer.GetContainingSet()

    pDS9FXNav = MissionLib.GetShip("Bajoran Wormhole Navpoint", pSet)

    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()

    pDS9FXWormhole = "Bajoran Wormhole Navpoint"

    if not DistanceCheck(pDS9FXNav) <= 20:
        KillManualEntry()
        DistanceCheckCondition = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 5, pPlayer.GetName(), pDS9FXWormhole)
        MissionLib.CallFunctionWhenConditionChanges(pMission, __name__, "FacingTheWormhole", DistanceCheckCondition)
        return 0

    iWormholeAnimated = 0
    DS9FXGlobalEvents.Trigger_Stop_Manual_Entry_Trigger(MissionLib.GetPlayer())

    # Finally just give control to the core
    DS9FXmain.TransferShips(None, None)


def DistanceCheck(pObject):
    try:
        pPlayer = App.Game_GetCurrentGame().GetPlayer()
        vDifference = pObject.GetWorldLocation()
        vDifference.Subtract(pPlayer.GetWorldLocation())

        return vDifference.Length()    
    except:
        return 100

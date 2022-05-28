# Selects which music type to play

# by Sov

import App
import DynamicMusic
import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXSets

sMusicCon = None
lCombatStates = ["Combat Confident", "Combat Neutral", "Combat Panic"]

def SelectType(pCon = None):
    if pCon == None:
        return
    if pCon == "MusicConChanged":
        pSequence = App.TGSequence_Create()
        pAction = App.TGScriptAction_Create(__name__, "DelaySelection", 1)
        pSequence.AddAction(pAction, None, 1)
        pSequence.Play()
    else:
        pSequence = App.TGSequence_Create()
        pAction = App.TGScriptAction_Create(__name__, "DelaySelection", 0)
        pSequence.AddAction(pAction, None, 1)
        pSequence.Play()

def DelaySelection(pAction, bCheckState):
    global sMusicCon

    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return 0
    
    pSet = pPlayer.GetContainingSet()
    if not pSet:
        return 0

    lSets = DS9FXSets.lDS9FXSets
    if not pSet.GetName() in lSets:
        ResumeNormalMusic()
        sMusicCon = DynamicMusic.sCurrentMusicState
        return 0
    
    if DynamicMusic.sCurrentMusicState in lCombatStates:
        if bCheckState:
            if not sMusicCon in lCombatStates:
                from Custom.DS9FX.DS9FXSoundManager import CombatMusic
                CombatMusic.EvaluateMusicState()
        else:
                from Custom.DS9FX.DS9FXSoundManager import CombatMusic
                CombatMusic.EvaluateMusicState()
    elif DynamicMusic.sCurrentMusicState == "Starting Ambient":
        from Custom.DS9FX.DS9FXSoundManager import MusicManager
        MusicManager.InitialCheck()

    sMusicCon = DynamicMusic.sCurrentMusicState

    return 0

def ResumeNormalMusic():
    from Custom.DS9FX.DS9FXSoundManager import StandardMusicList
    dMusic = StandardMusicList.GetMusic()
    lMusic = []
    for key, value in dMusic.items():
        lMusic.append(key)
    lMusic.append("DS9FXDummy")
    from Custom.DS9FX.DS9FXSoundManager import DynamicMusicHandling
    sCurrMusic = DynamicMusicHandling.GetMusicName()
    if sCurrMusic in lMusic:
        pVol = App.g_kMusicManager.GetVolume()
        App.g_kMusicManager.SetVolume(0)
        for i in range(3):
            App.g_kMusicManager.StopMusic()
        DynamicMusic.ProcessQueue()
        App.g_kMusicManager.SetVolume(pVol)

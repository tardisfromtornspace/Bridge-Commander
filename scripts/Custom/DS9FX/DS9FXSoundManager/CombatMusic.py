# Plays DS9FX Combat music in DS9FX Sets

# by Sov

import App
import DynamicMusic
import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

bAllow = 1

def EvaluateMusicState():
    global bAllow
    
    if not bAllow:
        return 0

    pPlaying = CombatMusicPlayingCheck()
    if pPlaying:
        return 0
    
    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return 0
    
    pSet = pPlayer.GetContainingSet()
    if not pSet:
        return 0

    bAllow = 0
    
    reload(DS9FXSavedConfig)
    dOpts = {"DeepSpace91" : DS9FXSavedConfig.DS9Music,
             "BajoranWormhole1" : DS9FXSavedConfig.WormholeMusic,
             "GammaQuadrant1" : DS9FXSavedConfig.GammaMusic,
             "DS9FXBadlands1" : DS9FXSavedConfig.BadlandsMusic,
             "DS9FXKaremma1" : DS9FXSavedConfig.KaremmaMusic,
             "DS9FXDosi1" : DS9FXSavedConfig.DosiMusic,
             "DS9FXYadera1" : DS9FXSavedConfig.YaderaMusic,
             "DS9FXNewBajor1" : DS9FXSavedConfig.NewBajorMusic,
             "DS9FXGaia1" : DS9FXSavedConfig.GaiaMusic,
             "DS9FXKurill1" : DS9FXSavedConfig.KurrillMusic,
             "DS9FXTrialus1" : DS9FXSavedConfig.TrialusMusic,
             "DS9FXTRogoran1" : DS9FXSavedConfig.TRogoranMusic,
             "DS9FXVandros1" : DS9FXSavedConfig.VandrosMusic,
             "DS9FXQonos1" : DS9FXSavedConfig.QonosMusic,
             "DS9FXFoundersHomeworld1" : DS9FXSavedConfig.FoundersMusic,
             "DS9FXChintoka1" : DS9FXSavedConfig.ChintokaMusic,
             "DS9FXCardassia1" : DS9FXSavedConfig.CardassiaMusic,
             "DS9FXTrivas1" : DS9FXSavedConfig.TrivasMusic,             
             "DS9FXVela1" : DS9FXSavedConfig.VelaMusic}
    if dOpts.has_key(pSet.GetName()):
        pOpt = dOpts[pSet.GetName()]
        if pOpt != 0:
            from Custom.DS9FX.DS9FXSoundManager import CombatMusicList
            pMusic = CombatMusicList.GetCombatMusic()
            i = len(pMusic) * 100 - 2
            pSelection = GetRandomNumber(i, 1)
            pSelection = pSelection / 100
            iLen = len(pMusic) - 1
            if pSelection < 0:
                pSelection = 0
            elif pSelection > iLen:
                pSelection = iLen
            sMusic = pMusic[pSelection]
            PlayMusic(sMusic)               

    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".OverflowPrevention", App.g_kUtopiaModule.GetGameTime() + 3, 0, 0)

def OverflowPrevention(pObject, pEvent):
    global bAllow
    bAllow = 1

def CombatMusicPlayingCheck():
    from Custom.DS9FX.DS9FXSoundManager import CombatMusicList
    lMusic = CombatMusicList.GetCombatMusic()

    from Custom.DS9FX.DS9FXSoundManager import DynamicMusicHandling
    sCurrMusic = DynamicMusicHandling.GetMusicName()

    if sCurrMusic in lMusic:
        return 1

    return 0

def PlayMusic(sMusic):
    from Custom.DS9FX.DS9FXSoundManager import DynamicMusicHandling
    DynamicMusicHandling.InsertMusic(sMusic)
    
    pVol = App.g_kMusicManager.GetVolume()
    App.g_kMusicManager.SetVolume(0)
    for i in range(3):
        App.g_kMusicManager.StopMusic()
    DynamicMusic.PlayFanfare(sMusic)
    App.g_kMusicManager.SetVolume(pVol)
     
def GetRandomNumber(iRnd, iStat):
    return App.g_kSystemWrapper.GetRandomNumber(iRnd) + iStat

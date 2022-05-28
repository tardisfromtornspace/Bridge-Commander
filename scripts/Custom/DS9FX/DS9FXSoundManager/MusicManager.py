# This handles set music type

# by Sov

import App
import DynamicMusic
import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

bAllow = 1

def InitialCheck():
    global bAllow
    
    if not bAllow:
        return 0
    
    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return 0
    
    pSet = pPlayer.GetContainingSet()
    if not pSet:
        return 0
    
    pPlaying = SetMusicAlreadyPlaying(pSet)
    if pPlaying:
        return 0    

    bAllow = 0
    
    from Custom.DS9FX.DS9FXSoundManager import SetMusic
    dMusics = {"DeepSpace91" : SetMusic.GetDS9Music(),
               "BajoranWormhole1" : SetMusic.GetWormholeMusic(),
               "GammaQuadrant1" : SetMusic.GetIdranMusic(),
               "DS9FXBadlands1" : SetMusic.GetBadlandsMusic(),
               "DS9FXKaremma1" : SetMusic.GetKaremmaMusic(),
               "DS9FXDosi1" : SetMusic.GetDosiMusic(),
               "DS9FXYadera1" : SetMusic.GetYaderaMusic(),
               "DS9FXNewBajor1" : SetMusic.GetNewBajorMusic(),
               "DS9FXGaia1" : SetMusic.GetGaiaMusic(),
               "DS9FXKurill1" : SetMusic.GetKurrillMusic(),
               "DS9FXTrialus1" : SetMusic.GetTrialusMusic(),
               "DS9FXTRogoran1" : SetMusic.GetTRogoranMusic(),
               "DS9FXVandros1" : SetMusic.GetVandrosMusic(),
               "DS9FXQonos1" : SetMusic.GetQonosMusic(),
               "DS9FXFoundersHomeworld1" : SetMusic.GetFoundersMusic(),
               "DS9FXChintoka1" : SetMusic.GetChintokaMusic(),
               "DS9FXCardassia1" : SetMusic.GetCardassiaMusic(),
               "DS9FXTrivas1" : SetMusic.GetTrivasMusic(),                     
               "DS9FXVela1" : SetMusic.GetVelaMusic()}
    if dMusics.has_key(pSet.GetName()):
        pMusic = dMusics[pSet.GetName()]
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
            i = pOpt - 1
            if i <= -1:
                bAllow = 1
                return 0
            iLen = len(pMusic) - 1
            if i > iLen:
                from Custom.DS9FX.DS9FXSoundManager import RandomizeMusic
                RandomizeMusic.InitialCheck()
            else:
                sMusic = pMusic[i]
                PlayMusic(sMusic)

    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".OverflowPrevention", App.g_kUtopiaModule.GetGameTime() + 3, 0, 0)

def OverflowPrevention(pObject, pEvent):
    global bAllow
    bAllow = 1
    
def SetMusicAlreadyPlaying(pSet):
    pName = pSet.GetName()
    if not pName:
        return 0
    
    from Custom.DS9FX.DS9FXSoundManager import SetMusic
    dMusics = {"DeepSpace91" : SetMusic.GetDS9Music(),
               "BajoranWormhole1" : SetMusic.GetWormholeMusic(),
               "GammaQuadrant1" : SetMusic.GetIdranMusic(),
               "DS9FXBadlands1" : SetMusic.GetBadlandsMusic(),
               "DS9FXKaremma1" : SetMusic.GetKaremmaMusic(),
               "DS9FXDosi1" : SetMusic.GetDosiMusic(),
               "DS9FXYadera1" : SetMusic.GetYaderaMusic(),
               "DS9FXNewBajor1" : SetMusic.GetNewBajorMusic(),
               "DS9FXGaia1" : SetMusic.GetGaiaMusic(),
               "DS9FXKurill1" : SetMusic.GetKurrillMusic(),
               "DS9FXTrialus1" : SetMusic.GetTrialusMusic(),
               "DS9FXTRogoran1" : SetMusic.GetTRogoranMusic(),
               "DS9FXVandros1" : SetMusic.GetVandrosMusic(),
               "DS9FXQonos1" : SetMusic.GetQonosMusic(),
               "DS9FXFoundersHomeworld1" : SetMusic.GetFoundersMusic(),
               "DS9FXChintoka1" : SetMusic.GetChintokaMusic(),
               "DS9FXCardassia1" : SetMusic.GetCardassiaMusic(),
               "DS9FXTrivas1" : SetMusic.GetTrivasMusic(),                 
               "DS9FXVela1" : SetMusic.GetVelaMusic()}

    if not dMusics.has_key(pName):
        return 0

    lMusic = dMusics[pName]

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
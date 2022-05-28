# This script just randomizes set music, if the selection is set to random naturally.

# by Sov

# Imports
import App
import MissionLib
import DynamicMusic
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib

bAllow = 1

# Functions
def InitialCheck():
    global bAllow
    
    if not bAllow:
        return

    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return
    
    pSet = pPlayer.GetContainingSet()
    if not pSet:
        return
    
    sSet = pSet.GetName()
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

    if dMusics.has_key(sSet):
        pMusic = dMusics[sSet]
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

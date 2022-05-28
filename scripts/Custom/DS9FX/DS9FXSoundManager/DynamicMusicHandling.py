# Interaction with DynamicMusic

# by Sov

import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXSets
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

sCurrentMusic = None

def InsertMusic(sMusicName):
    global sCurrentMusic
    sCurrentMusic = sMusicName
    import DynamicMusic
    DynamicMusic.sCurrentMusicName = sMusicName

def GetMusicName():
    import DynamicMusic
    sMusic = DynamicMusic.sCurrentMusicName
    return sMusic

def InjectDummyMusicName():
    sMusic = "DS9FXDummy"
    
    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return 0
    
    pSet = pPlayer.GetContainingSet()
    if not pSet:
        return 0

    sCurrMusic = GetMusicName()
    
    bFreePass = 0
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
    pName = pSet.GetName()
    if dMusics.has_key(pName):
        lMusic = dMusics[pName]
        if sCurrMusic in lMusic:
            bFreePass = 1
    
    if not bFreePass:
        from Custom.DS9FX.DS9FXSoundManager import CombatMusicList
        lMusic = CombatMusicList.GetCombatMusic()
        if not sCurrMusic in lMusic:
            return 0

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
    if dOpts.has_key(pName):
        pOpt = dOpts[pName]
        if pOpt == 0:
            return 0
        InsertMusic(sMusic)
    
def RestoreMusicName():
    global sCurrentMusic

    if sCurrentMusic is None:
        return 0
    
    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return 0
    
    pSet = pPlayer.GetContainingSet()
    if not pSet:
        return 0
    
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
        if pOpt == 0:
            return 0
        InsertMusic(sCurrentMusic)   
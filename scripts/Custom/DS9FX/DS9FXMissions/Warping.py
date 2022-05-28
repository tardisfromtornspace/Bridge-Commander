# by Sov

import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib

lButtons = ["Idran System", "Karemma System", "Dosi System", "Yadera System", "New Bajor System",
            "Gaia System", "Kurill System", "Trialus System", "T-Rogoran System", "Vandros System",
            "Founders Homeworld"]
lSets = ["GammaQuadrant1", "DS9FXKaremma1", "DS9FXDosi1", "DS9FXYadera1", "DS9FXNewBajor1",
         "DS9FXGaia1", "DS9FXKurill1", "DS9FXTrialus1", "DS9FXTRogoran1", "DS9FXVandros1",
         "DS9FXFoundersHomeworld1"]

def DisableGammaWarping():
    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return
    
    pSet = pPlayer.GetContainingSet()
    if not pSet:
        return
    
    sSet = pSet.GetName()
    if sSet in lSets:
        for s in lButtons:
            try:
                pButton = DS9FXMenuLib.GetSubMenuButton(str(s), "Helm", "DS9FX", "Warp To...")
                pButton.SetDisabled()
            except:    
                pass
            
def EnableGammaWarping():
    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return
    
    pSet = pPlayer.GetContainingSet()
    if not pSet:
        return
    
    sSet = pSet.GetName()
    # 1.5.2 python = no enumerate()?
    indSet = 0
    indBtn = 0
    if sSet in lSets:
        for s in lSets:
            indSet = indSet + 1
            if s == sSet:
                break

        for s in lButtons:
            indBtn = indBtn + 1
            if indSet == indBtn:
                continue
            try:
                pButton = DS9FXMenuLib.GetSubMenuButton(str(s), "Helm", "DS9FX", "Warp To...")
                pButton.SetEnabled()
            except:    
                pass            

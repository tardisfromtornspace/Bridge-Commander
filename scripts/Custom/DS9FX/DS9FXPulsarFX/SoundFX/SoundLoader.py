# This script doesn't actually load sounds but instead inserts to soundlist for DS9FX to load

import nt
import string
from Custom.DS9FX.DS9FXSoundManager import GameSoundList

def InsertSounds():
    sDir = "scripts\\Custom\\DS9FX\\DS9FXPulsarFX\\SoundFX"
    lLoaded = []
    
    list = nt.listdir(sDir)
    list.sort()
    
    for fl in list:
        s = string.split(fl, '.')
        if len(s) <= 1:
            continue
        
        Extension = s[-1]
        Filename = string.join(s[:-1], '.')
        if Filename == "__init__" or Filename == __name__:
            continue        
        
        sModule = "Custom.DS9FX.DS9FXPulsarFX.SoundFX." + str(Filename)
        if Extension == "py" and not Filename in lLoaded:
            lLoaded.append(Filename)
            try:
                pModule = __import__(sModule)
            except:
                continue
            
            if hasattr(pModule, "sName") and hasattr(pModule, "sPath"):
                pName = pModule.sName
                pPath = pModule.sPath
                GameSoundList.dSounds[pName] = pPath
            else:
                continue
                
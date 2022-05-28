# by Sov

import nt
import string
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib

lActivePlugins = []

def IsModActive():
    global lActivePlugins

    sDir = "scripts\\Custom\\DS9FX\\DS9FXLifeSupport\\Plugins"

    lLoaded = []
    lActivePlugins = []

    list = nt.listdir(sDir)
    list.sort()

    for fl in list:
        s = string.split(fl, '.')
        if len(s) <= 1:
            continue

        Extension = s[-1]
        Filename = string.join(s[:-1], '.')
        if Filename == "__init__":
            continue

        sModule = "Custom.DS9FX.DS9FXLifeSupport.Plugins." + str(Filename)

        if Extension == "py" and not Filename in lLoaded:
            lLoaded.append(Filename)
            try:
                pModule = __import__(sModule)
            except:
                continue

            if hasattr(pModule, "GetMutatorName") and hasattr(pModule, "GetScript") and hasattr(pModule, "CanKillCrewMembers"):
                pInstalled = pModule.GetScript()
                if pInstalled:
                    sMutator = pModule.GetMutatorName()
                    pActive = DS9FXMenuLib.CheckModInstallation(sMutator)
                    if pActive:
                        lActivePlugins.append(Filename)                                           
            else:
                print 'DS9FX: Life Support plugin is invalid - ', str(Filename)
                continue

def RetriveStatus(pObject, pEvent):
    global lActivePlugins

    iPlugins = len(lActivePlugins)
    iPass = 0
    for fl in lActivePlugins:
        sModule = "Custom.DS9FX.DS9FXLifeSupport.Plugins." + str(fl)
        pModule = __import__(sModule)
        bCanKill = pModule.CanKillCrewMembers(pObject, pEvent)
        if bCanKill:
            iPass = iPass + 1

    if iPass == iPlugins:
        return 1
    return 0

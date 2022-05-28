# by Sov

import App
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

sPath = "scripts/Custom/DS9FX/DS9FXSunStreak/"

def Create(pSet, sPosition, fSize, sType, sPoint):
    reload(DS9FXSavedConfig)
    if DS9FXSavedConfig.SunStreaks != 1:
        return
    
    try:
        sScript = __import__("Custom.DS9FX.DS9FXSunStreak." + sType)
    except:
        print "DS9FX: Sun Streak " + sType + " doesn't appear to exist"
        return

    lPoints = ["2", "4", "6", "8"]
    if not sPoint in lPoints:
        print "DS9FX: Invalid Sun Streak point - " + sPoint
        return
    
    if hasattr(sScript, "GetModelA") and hasattr(sScript, "GetModelB") and hasattr(sScript, "GetModelC") and hasattr(sScript, "GetModelD"):
        if sPoint == "2":
            sFile = sScript.GetModelA()
        elif sPoint == "4":
            sFile = sScript.GetModelB()
        elif sPoint == "6":
            sFile = sScript.GetModelC()
        elif sPoint == "8":
            sFile = sScript.GetModelD()
    else:
        print "DS9FX: Sun Streak " + sType + " doesn't contain valid models"
        return

    pProxManager = pSet.GetProximityManager()
    sModel = sPath + sFile
    sName = sPosition + " SunStreak"    
    pStreak = App.Planet_Create(fSize, sModel)
    pSet.AddObjectToSet(pStreak, sName)   
    pStreak.PlaceObjectByName(sPosition)
    pStreak.UpdateNodeOnly()
    pProxManager.RemoveObject(pStreak)
    
    if hasattr(pStreak, "SetDensity"):
        pStreak.SetDensity(0.1)
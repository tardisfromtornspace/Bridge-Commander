# Simulates normal BC GUI behaviour for GUI's which we specify

# by Sov

# Imports
import App

# Functions
def HelmMenuClosed():
    pBridge = App.g_kSetManager.GetSet("bridge")
    pHelm = App.CharacterClass_GetObject(pBridge, "Helm")
    pHelm.AddPythonFuncHandlerForInstance(App.ET_CHARACTER_MENU, __name__ + ".Close")

def Close(pObject, pEvent):
    pCharacter = App.CharacterClass_Cast(pEvent.GetDestination())
    if (pCharacter == None):
	    return    
    # Import the GUIs here
    try:
        from Custom.DS9FX.DS9FXLifeSupport import HandleTransportCrew
        HandleTransportCrew.KillGUI(None, None)
    except:
        raise RuntimeError, "Cannot Close HandleTransportCrew GUI..."

    try:
        from Custom.DS9FX.DS9FXLifeSupport import CaptureShip
        CaptureShip.KillGUI(None, None)
    except:
        raise RuntimeError, "Cannot Close CaptureShip GUI..."

    try:
        from Custom.DS9FX.DS9FXLifeSupport import ShipRecovery
        ShipRecovery.KillGUI(None, None)
    except:
        raise RuntimeError, "Cannot Close ShipRecovery GUI..."

    try:
        from Custom.DS9FX.DS9FXScan import ProvidePlayerInfo
        ProvidePlayerInfo.KillGUI(None, None)
    except:
        raise RuntimeError, "Cannot Close ProvidePlayerInfo GUI..."

    try:
        from Custom.DS9FX.DS9FXScan import ProvideShipInfo
        ProvideShipInfo.KillGUI(None, None)
    except:
        raise RuntimeError, "Cannot Close ProvideShipInfo GUI..."

    try:
        from Custom.DS9FX.DS9FXScan import ProvidePlanetInfo
        ProvidePlanetInfo.KillGUI(None, None)
    except:
        raise RuntimeError, "Cannot Close ProvidePlanetInfo GUI..."

    try:
        from Custom.DS9FX.DS9FXScan import ProvideRegionInfo
        ProvideRegionInfo.KillGUI(None, None)
    except:
        raise RuntimeError, "Cannot Close ProvideRegionInfo GUI..."
    
    try:
        from Custom.DS9FX.DS9FXMissions import MissionStatus
        MissionStatus.CloseMissionStatus(None, None)
    except:
        raise RuntimeError, "Cannot Close MissionStatus GUI..."

    
    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)  

# This script fixes the issue when you set a new game player, then the old player ship explodes and the tac ctrl weapons window is "killed"

# by Sov

# Imports
import App
import MissionLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

# Vars
bEnabled = 1
lPlayerIDs = []

# Events
ET_DUMMY = App.UtopiaModule_GetNextEventType()

# Functions
def FixTransportingBug(pObject, pEvent, param = None):
    global lPlayerIDs, bEnabled

    reload(DS9FXSavedConfig)
    if DS9FXSavedConfig.TransporterFix == 1:
        bEnabled = 1
    else:
        bEnabled = 0

    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return 0

    if param == "PlayerCreated":
        pID = pPlayer.GetObjID()
        lPlayerIDs.append(pID)
    elif param == "SetPlayer":
        pID = pPlayer.GetObjID()
        lPlayerIDs.append(pID)        
    elif param == "ObjectKilled":
        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if not pShip:
            return 0
        if pShip.GetObjID() in lPlayerIDs:
            pass
        else:
            return 0
    else:
        return 0

    if bEnabled:        
        pSequence = App.TGSequence_Create()
        pAction = App.TGScriptAction_Create(__name__, "Fix")
        pSequence.AddAction(pAction, None, 7)
        pSequence.Play()        

    else:
        return 0

def Fix(pAction):
    pTacWeaponsCtrl = App.TacWeaponsCtrl_GetTacWeaponsCtrl()
    if pTacWeaponsCtrl: 
        pTacWeaponsCtrl.Init()
        pTacWeaponsCtrl.RefreshPhaserSettings()
        pTacWeaponsCtrl.RefreshTorpedoSettings()
        pTacWeaponsCtrl.RefreshTractorToggle()
        pTacWeaponsCtrl.RefreshCloakToggle()

    # After speaking to Mleo, I figured that this can be done...
    try:
        # Fake an event
        pPlayer = MissionLib.GetPlayer()
        pEvent = App.TGEvent_Create()
        pEvent.SetEventType(ET_DUMMY)
        pEvent.SetDestination(pPlayer)
        App.g_kEventManager.AddEvent(pEvent)        
        from Custom.Autoload import ReSet
        if ReSet.mode.IsEnabled():
            ReSet.oPlayerChecking.__call__(None, pEvent)
    except:
        pass

    return 0

def ResetList():
    global lPlayerIDs
    lPlayerIDs = []


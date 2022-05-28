# This should fix some "reset" bugs and keep memory cleaner

# by Sov

import App
import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXSets, GalaxyCharts

bDeleteSets = 1

def KillSets(pObject, pEvent):
    pDisallow = GalaxyCharts.IsIncompatibleOn()
    if pDisallow:
        return 0
    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return 0
    pSet = pPlayer.GetContainingSet()
    if not pSet:
        return 0
    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    if not pShip:
        return 0
    if not pShip.GetObjID() == pPlayer.GetObjID():
        return 0
    
    # A bad fix implementation, but will do
    pSequence = App.TGSequence_Create()
    pAction = App.TGScriptAction_Create(__name__, "KillSetsDelay")
    pSequence.AddAction(pAction, None, 3)
    pSequence.Play()       
    
def KillSetsDelay(pAction):
    global bDeleteSets

    if not bDeleteSets:
        return 0

    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return 0
    
    pSet = pPlayer.GetContainingSet()
    if not pSet:
        return 0
    
    lSets = DS9FXSets.lDS9FXSets
    
    if not pSet.GetName() in lSets:
        return 0
    
    for s in lSets:
        if s == pSet.GetName():
            continue
        try:
            App.g_kSetManager.DeleteSet(s)
        except:
            pass
    
    return 0

def DisallowSetKilling():
    global bDeleteSets
    bDeleteSets = 0

    # Using timers when a new QB Mission is loading causes event "mixings", so better use sequence which doesn't cause any errors
    pSequence = App.TGSequence_Create()
    pAction = App.TGScriptAction_Create(__name__, "AllowSetKilling")
    pSequence.AddAction(pAction, None, 10)
    pSequence.Play()   
    
def AllowSetKilling(pAction):
    global bDeleteSets
    bDeleteSets = 1
    
    return 0
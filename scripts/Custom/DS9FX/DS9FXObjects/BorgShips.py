# This will globally override AI's of all large DS9FX Borg Ships, we could have done it the Foundation way but I want to maintain compatibility with BCUT

import App
import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXBorgAIOverrideShipTypes
from Custom.DS9FX.DS9FXLib import DS9FXLifeSupportLib
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib

dShips = {}

def BorgShipCheck(pObject, pEvent):
    global dShips
    
    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return 0
    
    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    if not pShip:
        return 0
    
    pPlID = pPlayer.GetObjID()
    if not pPlID:
        return 0
    
    pShID = pShip.GetObjID()
    if not pShID:
        return 0
    
    if pPlID == pShID:
        return 0
    
    pScript = DS9FXLifeSupportLib.GetShipType(pShip)
    if not pScript:
        return 0
    
    l = DS9FXBorgAIOverrideShipTypes.lShips
    if not pScript in l:
        return 0
    
    sName = pShip.GetName()
    if not sName:
        return 0
    
    pFriendly = MissionLib.GetFriendlyGroup()
    pEnemy = MissionLib.GetEnemyGroup()
    
    iOpt = 0
    if pFriendly.IsNameInGroup(sName):
        iOpt = 1
    elif pEnemy.IsNameInGroup(sName):
        iOpt = 2
        
    pID = pShip.GetObjID()
    dShips[pID] = iOpt
        
    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Delay", App.g_kUtopiaModule.GetGameTime() + 2, 0, 0)
    
def Delay(pObject, pEvent):    
    global dShips
        
    lToRemove = []
    for k, v in dShips.items():
        pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(k))
        iOpt = v
        lToRemove.append(k)
        if not pShip:
            continue
        if iOpt == 1:
            from Custom.DS9FX.DS9FXAILib import DS9FXBorgAI
            pShip.SetAI(DS9FXBorgAI.CreateAI(pShip, "Enemy"))
        elif iOpt == 2:
            from Custom.DS9FX.DS9FXAILib import DS9FXBorgAI        
            pShip.SetAI(DS9FXBorgAI.CreateAI(pShip, "Friendly"))
        pShip.SetCollisionsOn(0)
    
    for k in lToRemove:
        if dShips.has_key(k):
            del dShips[k]
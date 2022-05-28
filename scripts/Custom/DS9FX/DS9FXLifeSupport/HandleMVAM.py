# This will handle MVAM sep\rein processes

# by Sov

import App
from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents
from Custom.DS9FX.DS9FXLifeSupport import LifeSupport_dict, CaptureShip, AIBoarding

def HandleSep(pObject, pEvent):
    try:
        iCount = pEvent.GetInt()
    except AttributeError:
        return 0

    if iCount == 0:
        iCount = 1

    pOld = App.ShipClass_Cast(pEvent.GetSource())
    pNew = App.ShipClass_Cast(pEvent.GetDestination())

    if not pOld or not pNew:
        return 0

    pOldID = pOld.GetObjID()
    pNewID = pNew.GetObjID()

    if not pOldID or not pNewID:
        return 0

    if not LifeSupport_dict.dCrew.has_key(pOldID) or not LifeSupport_dict.dCrew.has_key(pNewID):
        return 0

    iOldCrew = LifeSupport_dict.dCrew[pOldID]
    iNewCrew = iOldCrew/iCount

    iOldCrew = iOldCrew - iNewCrew
    if iOldCrew <= 0:
        iOldCrew = 0

    if iNewCrew <= 0:
        iNewCrew = 0
        
    if CaptureShip.captureships.has_key(pOldID):
        lInfo = CaptureShip.captureships[pOldID]
        iAttackers = lInfo[0]/iCount
        if iAttackers <= 0:
            iAttackers = 0        
        iDefenders = iNewCrew - iAttackers
        if iDefenders <= 0:
            iDefenders = 0
        lNewInfo = lInfo[:]
        lInfo[0] = lInfo[0] - iAttackers
        if lInfo[0] <= 0:
            lInfo[0] = 0
        lInfo[1] = lInfo[1] - iDefenders
        if lInfo[1] <= 0:
            lInfo[1] = 0
        lNewInfo[0] = iAttackers
        lNewInfo[1] = iDefenders
        CaptureShip.captureships[pOldID] = lInfo
        CaptureShip.captureships[pNewID] = lNewInfo
        
        pSequence = App.TGSequence_Create()
        pAction = App.TGScriptAction_Create("Custom.DS9FX.DS9FXLifeSupport.CaptureShip", "KillCrew", pNewID)
        pSequence.AddAction(pAction, None, 5) 
        pSequence.Play()        
        
    if AIBoarding.dCombat.has_key(pOldID):
        dData = AIBoarding.dCombat[pOldID]
        iDef = dData["Defender"]
        iAtt = dData["Attacker"]
        pGroup = dData["Group"]
        pAttacker = dData["AttackerID"]        
        iAttackers = iAtt/iCount
        if iAttackers <= 0:
            iAttackers = 0  
        iDefenders = iNewCrew - iAttackers
        if iDefenders <= 0:
            iDefenders = 0
        iAtt = iAtt - iAttackers
        if iAtt <= 0:
            iAtt = 0
        iDef = iDef - iDefenders
        if iDef <= 0:
            iDef = 0
        dData["Defender"] = iDef
        dData["Attacker"] = iAtt
        dNewData = {}
        dNewData["Defender"] = iDefenders
        dNewData["Attacker"] = iAttackers
        dNewData["Group"] = pGroup
        dNewData["AttackerID"] = pAttacker
        AIBoarding.dCombat[pOldID] = dData
        AIBoarding.dCombat[pNewID] = dNewData

        pSequence = App.TGSequence_Create()
        pAction = App.TGScriptAction_Create("Custom.DS9FX.DS9FXLifeSupport.AIBoarding", "Fighting", pNewID)
        pSequence.AddAction(pAction, None, 3) 
        pSequence.Play()
       
    LifeSupport_dict.dCrew[pOldID] = iOldCrew
    LifeSupport_dict.dCrew[pNewID] = iNewCrew
    
    DS9FXGlobalEvents.Trigger_Combat_Effectiveness(pOld)  
    DS9FXGlobalEvents.Trigger_Combat_Effectiveness(pNew)  

def HandleRein(pObject, pEvent):
    try:
        bReset = pEvent.GetBool()
    except AttributeError:
        return 0

    pOld = App.ShipClass_Cast(pEvent.GetSource())
    pNew = App.ShipClass_Cast(pEvent.GetDestination())

    if not pOld or not pNew:
        return 0

    pOldID = pOld.GetObjID()
    pNewID = pNew.GetObjID()

    if not pOldID or not pNewID:
        return 0

    if not LifeSupport_dict.dCrew.has_key(pOldID) or not LifeSupport_dict.dCrew.has_key(pNewID):
        return 0

    iCrew = LifeSupport_dict.dCrew[pOldID]

    LifeSupport_dict.dCrew[pOldID] = 0

    if bReset:
        LifeSupport_dict.dCrew[pNewID] = 0
        
    if CaptureShip.captureships.has_key(pOldID):
        lInfo = CaptureShip.captureships[pOldID]
        iAttackers = lInfo[0]
        iDefenders = lInfo[1]
        lInfo[0] = 0
        lInfo[1] = 0        
        if CaptureShip.captureships.has_key(pNewID):
            lNewInfo = CaptureShip.captureships[pNewID]
        else:
            lNewInfo = lInfo[:]
        lNewInfo[0] = lNewInfo[0] + iAttackers
        lNewInfo[1] = lNewInfo[1] + iDefenders
        CaptureShip.captureships[pOldID] = lInfo
        CaptureShip.captureships[pNewID] = lNewInfo     
        
        if bReset:
            pSequence = App.TGSequence_Create()
            pAction = App.TGScriptAction_Create("Custom.DS9FX.DS9FXLifeSupport.CaptureShip", "KillCrew", pNewID)
            pSequence.AddAction(pAction, None, 5) 
            pSequence.Play()   
            
    if AIBoarding.dCombat.has_key(pOldID):        
        dData = AIBoarding.dCombat[pOldID]
        iDefenders = dData["Defender"]
        iAttackers = dData["Attacker"]  
        pGroup = dData["Group"]
        pAttacker = dData["AttackerID"]          
        dData["Defender"] = 0
        dData["Attacker"] = 0
        AIBoarding.dCombat[pOldID] = dData
        if AIBoarding.dCombat.has_key(pNewID): 
            dNewData = AIBoarding.dCombat[pNewID]
            dNewData["Defender"] = dNewData["Defender"] + iDefenders
            dNewData["Attacker"] = dNewData["Attacker"] + iAttackers
            AIBoarding.dCombat[pNewID] = dNewData            
        else:
            dNewData = {}
            dNewData["Defender"] = iDefenders
            dNewData["Attacker"] = iAttackers
            dNewData["Group"] = pGroup
            dNewData["AttackerID"] = pAttacker
            AIBoarding.dCombat[pNewID] = dNewData
            
        if bReset:
            pSequence = App.TGSequence_Create()
            pAction = App.TGScriptAction_Create("Custom.DS9FX.DS9FXLifeSupport.AIBoarding", "Fighting", pNewID)
            pSequence.AddAction(pAction, None, 3) 
            pSequence.Play()
                        
    LifeSupport_dict.dCrew[pNewID] = LifeSupport_dict.dCrew[pNewID] + iCrew
    
    DS9FXGlobalEvents.Trigger_Combat_Effectiveness(pNew)  



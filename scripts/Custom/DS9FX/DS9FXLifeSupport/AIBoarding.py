# This will handle AI ship boarding

# by Sov

import App
import CaptureShip
import MissionLib
import HandleTransportCrew
from Custom.DS9FX.DS9FXAILib import DS9FXGenericStaticEnemyAI, DS9FXGenericStaticFriendlyAI, DS9FXGenericStaticStarbaseEnemyAI, DS9FXGenericStaticStarbaseFriendlyAI
from Custom.DS9FX.DS9FXLib import DS9FXLifeSupportLib, DS9FXPrintTextLib
from Custom.DS9FX.DS9FXLifeSupport import LifeSupport_dict
from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents

dCombat = {}

def MissionStart():
    global dCombat
    dCombat = {}

def Boarding(pObject, pEvent):
    global dCombat

    pPlayer = MissionLib.GetPlayer()
    pDefender = App.ShipClass_Cast(pEvent.GetDestination())    
    pAttacker = App.ShipClass_Cast(pEvent.GetFiringObject())
    if not pAttacker or not pDefender:
        return 0
    
    if pDefender.IsCloaked() or pAttacker.IsCloaked():
        return 0

    pDefID = pDefender.GetObjID()
    pAttID = pAttacker.GetObjID()
    if not pDefID or not pAttID:
        return 0

    # If the player is the attacker bail. Capture ship takes care of that.
    if pPlayer:
        pPlID = pPlayer.GetObjID()
        if pPlID:
            if pPlID == pAttID:
                return 0

    if not LifeSupport_dict.dCrew.has_key(pAttID) or not LifeSupport_dict.dCrew.has_key(pDefID):
        return 0

    pDistance = DistanceCheck(pAttacker, pDefender)
    if pDistance > 300:
        return 0

    bCanTransport = CaptureShip.ShieldCheck(pDefID)
    if not bCanTransport:
        return 0

    iCrewPerc = DS9FXLifeSupportLib.GetCrewPercentage(pAttacker, pAttID)
    if iCrewPerc < 50:
        return 0

    iBoardingParty = LifeSupport_dict.dCrew[pAttID]
    fRandom = GetRandomRate(25, 25) / 100.0
    iBoardingParty = int(iBoardingParty * fRandom)
    
    # Make sure we still have at least 40% of crew aboard
    pAttInfo = DS9FXLifeSupportLib.GetShipMaxAndMinCrewCount(pAttacker, pAttID)
    pAttackerMax = pAttInfo["fMax"]
    pAttCurr = pAttInfo["fMin"]
    # We want the Defender count only not the whole count
    iAttackers = 0
    if CaptureShip.captureships.has_key(pAttID):
        lInfo = CaptureShip.captureships[pAttID]
        iAttackers = lInfo[0]
    if dCombat.has_key(pAttID):
        dData = dCombat[pAttID]
        iAttackers = iAttackers + dData["Attacker"] 
    pAttCurr = pAttCurr - iAttackers
    if pAttCurr <= 0:
        return 0
    iMaxAllowed = int(pAttackerMax * 0.4)
    if pAttCurr - iBoardingParty <  iMaxAllowed:
        iBoardingParty = pAttCurr - iMaxAllowed
        if iBoardingParty <= 0:
            return 0

    # Check if we are going over the limit here...
    iDefCrew = LifeSupport_dict.dCrew[pDefID]
    pDefenderInfo = DS9FXLifeSupportLib.GetShipMaxAndMinCrewCount(pDefender, pDefID)
    pDefMax = pDefenderInfo["fMax"]
    if pDefMax <= 0:
        return 0
    pDefMax = int(pDefMax * 1.5)
    if iDefCrew + iBoardingParty > pDefMax:
        iExtra = iDefCrew + iBoardingParty
        iExtra = iExtra - pDefMax
        iBoardingParty = iBoardingParty - iExtra

    # If the player is already boarding this ship and the attacker is friendly transfer the reinforcements to player control
    pFriend = MissionLib.GetFriendlyGroup()
    if pFriend.IsNameInGroup(pAttacker.GetName()):
        if CaptureShip.captureships.has_key(pDefID):
            lInfo = CaptureShip.captureships[pDefID]
            lInfo[0] = lInfo[0] + iBoardingParty
            lInfo[1] = lInfo[1] - iBoardingParty
            CaptureShip.captureships[pDefID] = lInfo
            LifeSupport_dict.dCrew[pAttID] = LifeSupport_dict.dCrew[pAttID] - iBoardingParty
            DS9FXGlobalEvents.Trigger_Combat_Effectiveness(pAttacker)
            # Tell the user AI reinforced our guys on the front
            s = pAttacker.GetName() + " has reinforced our troops in boarding " + pDefender.GetName() + "." + "\n" + "Their troops are now under our control."
            ShowMessage(s, 6)
            return 0

    if dCombat.has_key(pDefID):
        # Ship is already boarded, just reinforce the troopes then
        dFight = dCombat[pDefID]
        dFight["Attacker"] = dFight["Attacker"] + iBoardingParty
        dCombat[pDefID] = dFight
        bReinforcements = 1
    else:
        # Ship not boarded create a new dict entry for it
        dFight = {}
        dFight["Defender"] = LifeSupport_dict.dCrew[pDefID]
        dFight["Attacker"] = iBoardingParty
        lGroups = [MissionLib.GetEnemyGroup(), MissionLib.GetFriendlyGroup(), MissionLib.GetNeutralGroup(), App.ObjectGroup()]
        for group in lGroups:
            if group.IsNameInGroup(pAttacker.GetName()):
                dFight["Group"] = group
                break
        dFight["AttackerID"] = pAttID
        dCombat[pDefID] = dFight
        bReinforcements = 0

    LifeSupport_dict.dCrew[pDefID] = LifeSupport_dict.dCrew[pDefID] + iBoardingParty
    LifeSupport_dict.dCrew[pAttID] = LifeSupport_dict.dCrew[pAttID] - iBoardingParty
    DS9FXGlobalEvents.Trigger_Combat_Effectiveness(pDefender)
    DS9FXGlobalEvents.Trigger_Combat_Effectiveness(pAttacker)

    # Is the player being boarded? Tell him if he is...  
    if pPlayer:
        pPlID = pPlayer.GetObjID()
        if pPlID:
            if pPlID == pDefID:
                # Reinforcements or being boarded for the first time
                if bReinforcements:
                    ShowMessage("Additional enemy reinforcements have boarded us sir!", 8)
                else:
                    ShowMessage("We've been boarded by enemy troops sir!", 6)
                HandleTransportCrew.PlayTransportSound()

    # Don't start a duplicate sequence if a combat sequence for the ship is already initiated
    if bReinforcements:
        return 0

    # Combat sequence initing
    pSequence = App.TGSequence_Create()
    pAction = App.TGScriptAction_Create(__name__, "Fighting", pDefID)
    pSequence.AddAction(pAction, None, 3) 
    pSequence.Play()

def Fighting(pAction, pShipID):
    global dCombat
    
    if not dCombat.has_key(pShipID):
        return 0

    pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))
    if not pShip:
        if dCombat.has_key(pShipID):
            del dCombat[pShipID]
        return 0

    if not LifeSupport_dict.dCrew.has_key(pShipID) or LifeSupport_dict.dCrew[pShipID] == 0:
        if dCombat.has_key(pShipID):
            del dCombat[pShipID]
        return 0

    iCrew = LifeSupport_dict.dCrew[pShipID]
    dData = dCombat[pShipID]
    iDef = dData["Defender"]
    iAtt = dData["Attacker"]
    pGroup = dData["Group"]
    pAttacker = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(dData["AttackerID"]))

    # Readjust the parameters for the ship, in between some of the crew might have died in combat
    iTotal = iDef + iAtt
    if iTotal < iCrew:
        # This means that the defender got reinforcements
        iDiff = iCrew - iTotal
        iDef = iDef + iDiff
        dData["Defender"] = iDef
    elif iTotal > iCrew:
        # This means some of the crew has died in combat and we need to recalculate the stats
        iDiff = iTotal - iCrew
        iDefOffset = iDiff / 2
        iAttOffset = iDiff - iDefOffset
        iAtt = iAtt - iAttOffset
        iDef = iDef - iDefOffset
        dData["Attacker"] = iAtt
        dData["Defender"] = iDef
    else:
        # No data changed
        pass

    # In the meantime has the player sent his own troops to the ship, if so then transfer the attacking troops to his control
    pFriend = MissionLib.GetFriendlyGroup()
    if pGroup == pFriend:
        if CaptureShip.captureships.has_key(pShipID):
            lInfo = CaptureShip.captureships[pShipID]
            lInfo[0] = lInfo[0] + iAtt
            lInfo[1] = lInfo[1] - iAtt
            CaptureShip.captureships[pShipID] = lInfo
            if dCombat.has_key(pShipID):
                del dCombat[pShipID]
            s = pShip.GetName() + " is already under siege. All attacking troops are now under our control!"
            ShowMessage(s, 6)
            return 0

    # Combat calculation which is kinda randomized
    iChance = iDef - 1
    if iChance < 1:
        iChance = 1
    iDefChance = GetRandomRate(iChance, 1)
    iChance = iAtt - 1
    if iChance < 1:
        iChance = 1
    iAttChance = GetRandomRate(iChance, 1)
    if iDefChance > iAttChance:
        # Defender wins this round
        iKilledPerc = GetRandomRate(10, 5) / 100.0
        iKilledDef = iDef * iKilledPerc
        iDef = int(iDef - iKilledDef)
        if iDef <= 0:
            iDef = 0
        iKilledPerc = GetRandomRate(74, 1) / 100.0
        iKilledAtt = iKilledDef * iKilledPerc
        iAtt = int(iAtt - iKilledAtt)
        if iAtt <= 0:
            iAtt = 0
    elif iDefChance < iAttChance:
        # Attacker wins this round
        iKilledPerc = GetRandomRate(10, 5) / 100.0
        iKilledAtt = iAtt * iKilledPerc
        iAtt = int(iAtt - iKilledAtt)
        if iAtt <= 0:
            iAtt = 0
        iKilledPerc = GetRandomRate(74, 1) / 100.0
        iKilledDef = iKilledAtt * iKilledPerc
        iDef = int(iDef - iKilledDef)
        if iDef <= 0:
            iDef = 0
    else:
        # We have a draw
        iKilledPerc = GetRandomRate(5, 5) / 100.0
        if iAtt >= iDef:
            iKilledAtt = iAtt * iKilledPerc
            iAtt = int(iAtt - iKilledAtt)
            if iAtt <= 0:
                iAtt = 0
            iKilledPerc = GetRandomRate(74, 1) / 100.0
            iKilledDef = iKilledAtt * iKilledPerc
            iDef = int(iDef - iKilledDef)
            if iDef <= 0:
                iDef = 0
        else:
            iKilledDef = iDef * iKilledPerc
            iDef = int(iDef - iKilledDef)
            if iDef <= 0:
                iDef = 0
            iKilledPerc = GetRandomRate(74, 1) / 100.0
            iKilledAtt = iKilledDef * iKilledPerc
            iAtt = int(iAtt - iKilledAtt)
            if iAtt <= 0:
                iAtt = 0     

    dData["Defender"] = iDef
    dData["Attacker"] = iAtt

    LifeSupport_dict.dCrew[pShipID] = iAtt + iDef

    DS9FXGlobalEvents.Trigger_Combat_Effectiveness(pShip)

    # Ship dead in space?
    if iAtt <= 0 and iDef <= 0:
        pShip.ClearAI()
        DS9FXLifeSupportLib.GroupCheck(pShip)
        DS9FXLifeSupportLib.PlayerCheck(pShipID)
        DS9FXGlobalEvents.Trigger_Ship_Dead_In_Space(pShip)
        if dCombat.has_key(pShipID):
            del dCombat[pShipID]
        return 0

    # Defender won?
    if iAtt <= 0:
        if dCombat.has_key(pShipID):
            del dCombat[pShipID]
        return 0

    # Attacker won? Ship taken over?
    if iDef <= 0:
        DS9FXLifeSupportLib.GroupCheck(pShip)
        # Player goes bye bye if it was him who was taken over...
        DS9FXLifeSupportLib.PlayerCheck(pShipID)        
        Reassign(pShip, pGroup)
        if pAttacker:
            DS9FXGlobalEvents.Trigger_Ship_Taken_Over(pAttacker, pShip)
        pPlayer = MissionLib.GetPlayer()
        if pPlayer:
            pPlID = pPlayer.GetObjID()
            if pPlID:
                if pPlID == pShipID:
                    LifeSupport_dict.dCrew[pShipID] = 0
                    DS9FXGlobalEvents.Trigger_Ship_Dead_In_Space(pShip)
        if dCombat.has_key(pShipID):
            del dCombat[pShipID]        
        return 0

    # Replay sequence in the end
    pSequence = App.TGSequence_Create()
    pAction = App.TGScriptAction_Create(__name__, "Fighting", pShipID)
    pSequence.AddAction(pAction, None, 3) 
    pSequence.Play()

    return 0

def Reassign(pShip, pGroup):
    if not pGroup or not pShip:
        return 0

    pName = pShip.GetName()
    if not pName:
        return 0
    
    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        pass
    else:
        if pPlayer.GetName() == pName:
            return

    pGroup.AddName(str(pName))

    DS9FXLifeSupportLib.ResetAffiliationColors()

    import QuickBattle.QuickBattle
    try:
        import Custom.QuickBattleGame.QuickBattle
        bNoQBR = 0
    except:
        bNoQBR = 1

    # Grab all possible groups
    pFriendly = MissionLib.GetFriendlyGroup()
    pEnemy = MissionLib.GetEnemyGroup()
    pNeutral = MissionLib.GetNeutralGroup()
    pQBRGroup = App.ObjectGroup()

    # Do things the correct way, take QBR into account also. If GC 2.0 is installed it "fixes" our "mess" itself.
    if pFriendly.IsNameInGroup(pName):
        if QuickBattle.QuickBattle.pFriendlies:
            if (pShip.GetShipProperty().IsStationary() == 1):
                pShip.SetAI(DS9FXGenericStaticStarbaseFriendlyAI.CreateAI(pShip))
            else:
                pShip.SetAI(DS9FXGenericStaticFriendlyAI.CreateAI(pShip))
        if not bNoQBR:
            if Custom.QuickBattleGame.QuickBattle.pFriendlies:
                if (pShip.GetShipProperty().IsStationary() == 1):
                    pShip.SetAI(DS9FXGenericStaticStarbaseFriendlyAI.CreateAI(pShip))
                else:
                    pShip.SetAI(DS9FXGenericStaticFriendlyAI.CreateAI(pShip))
    elif pEnemy.IsNameInGroup(pName):
        if QuickBattle.QuickBattle.pEnemies:
            if (pShip.GetShipProperty().IsStationary() == 1):
                pShip.SetAI(DS9FXGenericStaticStarbaseEnemyAI.CreateAI(pShip))
            else:
                pShip.SetAI(DS9FXGenericStaticEnemyAI.CreateAI(pShip))
        if not bNoQBR:
            if Custom.QuickBattleGame.QuickBattle.pEnemies:
                if (pShip.GetShipProperty().IsStationary() == 1):
                    pShip.SetAI(DS9FXGenericStaticStarbaseEnemyAI.CreateAI(pShip))
                else:
                    pShip.SetAI(DS9FXGenericStaticEnemyAI.CreateAI(pShip))     
    elif pNeutral.IsNameInGroup(pName):
        if not bNoQBR:
            if Custom.QuickBattleGame.QuickBattle.pNeutrals:
                if (pShip.GetShipProperty().IsStationary() == 1):
                    import Custom.QuickBattleGame.StarbaseNeutralAI
                    pShip.SetAI(Custom.QuickBattleGame.StarbaseNeutralAI.CreateAI(pShip))
                else:
                    import Custom.QuickBattleGame.NeutralAI
                    pShip.SetAI(Custom.QuickBattleGame.NeutralAI.CreateAI(pShip, 1, 1))
    elif pQBRGroup.IsNameInGroup(pName):
        if not bNoQBR:
            if Custom.QuickBattleGame.QuickBattle.pNeutrals2:
                if (pShip.GetShipProperty().IsStationary() == 1):
                    import Custom.QuickBattleGame.StarbaseNeutralAI2
                    pShip.SetAI(Custom.QuickBattleGame.StarbaseNeutralAI2.CreateAI(pShip))
                else:
                    import Custom.QuickBattleGame.NeutralAI2
                    pShip.SetAI(Custom.QuickBattleGame.NeutralAI2.CreateAI(pShip, 1, 1))        

def DistanceCheck(pObject1, pObject2):
    try:
        vDifference = pObject1.GetWorldLocation()
        vDifference.Subtract(pObject2.GetWorldLocation())
        return vDifference.Length()
    except:
        return 5000

def GetRandomRate(iRandom, iStatic):
    return App.g_kSystemWrapper.GetRandomNumber(iRandom) + iStatic

def ShowMessage(sText, iPos):
    iFont = 12
    iDur = 5
    iDelay = 1
    DS9FXPrintTextLib.PrintText(sText, iPos, iFont, iDur, iDelay)
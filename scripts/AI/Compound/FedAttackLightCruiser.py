from bcdebug import debug
import App

def CreateAI(pShip, *lpTargets, **dKeywords):
    debug(__name__ + ", CreateAI")
    pAllTargetsGroup = App.ObjectGroup_ForceToGroup(lpTargets)
    sInitialTarget = None
    if pAllTargetsGroup.GetNameTuple():
    	sInitialTarget = pAllTargetsGroup.GetNameTuple()[0]
    Random = lambda fMin, fMax: ((App.g_kSystemWrapper.GetRandomNumber(((fMax - fMin) * 1000.0)) / 1000.0) - fMin)
    fTooCloseRange = (10.0 + Random(-10, 10))
    fTooFarRange = (30.0 + Random(-15, 10))
    fCloseRange = (40.0 + Random(-5, 15))
    fMidRange = (100.0 + Random(-10, 20))
    fLongRange = (350.0 + Random(-30, 20))
    pBuilderAI = App.BuilderAI_Create(pShip, 'AvoidObstaclesUpdated Builder', __name__)
    pBuilderAI.AddAIBlock('CheckWarpBeforeDeath', 'BuilderCreate1')
    pBuilderAI.AddDependencyObject('CheckWarpBeforeDeath', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('NoSensorsEvasive', 'BuilderCreate2')
    pBuilderAI.AddAIBlock('RearTorpRun', 'BuilderCreate3')
    pBuilderAI.AddDependencyObject('RearTorpRun', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('RearTorpsReadyRearShieldOk', 'BuilderCreate4')
    pBuilderAI.AddDependency('RearTorpsReadyRearShieldOk', 'RearTorpRun')
    pBuilderAI.AddDependencyObject('RearTorpsReadyRearShieldOk', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('RearTorp2', 'BuilderCreate5')
    pBuilderAI.AddDependencyObject('RearTorp2', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('UsingPulseWeapons_2', 'BuilderCreate6')
    pBuilderAI.AddDependency('UsingPulseWeapons_2', 'RearTorp2')
    pBuilderAI.AddAIBlock('ICOMoveOut', 'BuilderCreate7')
    pBuilderAI.AddDependencyObject('ICOMoveOut', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddDependencyObject('ICOMoveOut', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('TooClosePriorities', 'BuilderCreate8')
    pBuilderAI.AddDependency('TooClosePriorities', 'RearTorpsReadyRearShieldOk')
    pBuilderAI.AddDependency('TooClosePriorities', 'UsingPulseWeapons_2')
    pBuilderAI.AddDependency('TooClosePriorities', 'ICOMoveOut')
    pBuilderAI.AddAIBlock('TooClose', 'BuilderCreate9')
    pBuilderAI.AddDependency('TooClose', 'TooClosePriorities')
    pBuilderAI.AddDependencyObject('TooClose', 'fTooFarRange', fTooFarRange)
    pBuilderAI.AddDependencyObject('TooClose', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('TorpRun_3', 'BuilderCreate10')
    pBuilderAI.AddDependencyObject('TorpRun_3', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('TorpsReadyNotInterruptable', 'BuilderCreate11')
    pBuilderAI.AddDependency('TorpsReadyNotInterruptable', 'TorpRun_3')
    pBuilderAI.AddAIBlock('StationaryAttack_2', 'BuilderCreate12')
    pBuilderAI.AddDependencyObject('StationaryAttack_2', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('TorpsStillReadyFacingTowardNotInterruptable', 'BuilderCreate13')
    pBuilderAI.AddDependency('TorpsStillReadyFacingTowardNotInterruptable', 'StationaryAttack_2')
    pBuilderAI.AddDependencyObject('TorpsStillReadyFacingTowardNotInterruptable', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('PriorityList_3', 'BuilderCreate14')
    pBuilderAI.AddDependency('PriorityList_3', 'TorpsReadyNotInterruptable')
    pBuilderAI.AddDependency('PriorityList_3', 'TorpsStillReadyFacingTowardNotInterruptable')
    pBuilderAI.AddAIBlock('TorpRun_2', 'BuilderCreate15')
    pBuilderAI.AddDependencyObject('TorpRun_2', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('UsingPulseWeapons', 'BuilderCreate16')
    pBuilderAI.AddDependency('UsingPulseWeapons', 'TorpRun_2')
    pBuilderAI.AddAIBlock('ICOMoveIn_2', 'BuilderCreate17')
    pBuilderAI.AddDependencyObject('ICOMoveIn_2', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddDependencyObject('ICOMoveIn_2', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('SweepPhasers', 'BuilderCreate18')
    pBuilderAI.AddDependencyObject('SweepPhasers', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddDependencyObject('SweepPhasers', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('TooFarPriorities', 'BuilderCreate19')
    pBuilderAI.AddDependency('TooFarPriorities', 'PriorityList_3')
    pBuilderAI.AddDependency('TooFarPriorities', 'UsingPulseWeapons')
    pBuilderAI.AddDependency('TooFarPriorities', 'ICOMoveIn_2')
    pBuilderAI.AddDependency('TooFarPriorities', 'SweepPhasers')
    pBuilderAI.AddAIBlock('TooFar', 'BuilderCreate20')
    pBuilderAI.AddDependency('TooFar', 'TooFarPriorities')
    pBuilderAI.AddDependencyObject('TooFar', 'fTooCloseRange', fTooCloseRange)
    pBuilderAI.AddDependencyObject('TooFar', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('PriorityList_2', 'BuilderCreate21')
    pBuilderAI.AddDependency('PriorityList_2', 'TooClose')
    pBuilderAI.AddDependency('PriorityList_2', 'TooFar')
    pBuilderAI.AddAIBlock('FireAll', 'BuilderCreate22')
    pBuilderAI.AddDependency('FireAll', 'PriorityList_2')
    pBuilderAI.AddDependencyObject('FireAll', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddDependencyObject('FireAll', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('CloseRange', 'BuilderCreate23')
    pBuilderAI.AddDependency('CloseRange', 'FireAll')
    pBuilderAI.AddDependencyObject('CloseRange', 'fCloseRange', fCloseRange)
    pBuilderAI.AddDependencyObject('CloseRange', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('TorpRun', 'BuilderCreate24')
    pBuilderAI.AddDependencyObject('TorpRun', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('TorpsReady_FwdShieldStrong', 'BuilderCreate25')
    pBuilderAI.AddDependency('TorpsReady_FwdShieldStrong', 'TorpRun')
    pBuilderAI.AddAIBlock('MoveIn_2', 'BuilderCreate26')
    pBuilderAI.AddDependencyObject('MoveIn_2', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('MidRangePriorities', 'BuilderCreate27')
    pBuilderAI.AddDependency('MidRangePriorities', 'TorpsReady_FwdShieldStrong')
    pBuilderAI.AddDependency('MidRangePriorities', 'MoveIn_2')
    pBuilderAI.AddAIBlock('FireAll2', 'BuilderCreate28')
    pBuilderAI.AddDependency('FireAll2', 'MidRangePriorities')
    pBuilderAI.AddDependencyObject('FireAll2', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddDependencyObject('FireAll2', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('MidRange', 'BuilderCreate29')
    pBuilderAI.AddDependency('MidRange', 'FireAll2')
    pBuilderAI.AddDependencyObject('MidRange', 'fMidRange', fMidRange)
    pBuilderAI.AddDependencyObject('MidRange', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('MoveIn', 'BuilderCreate30')
    pBuilderAI.AddDependencyObject('MoveIn', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('LongRange', 'BuilderCreate31')
    pBuilderAI.AddDependency('LongRange', 'MoveIn')
    pBuilderAI.AddDependencyObject('LongRange', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('InterceptTarget', 'BuilderCreate32')
    pBuilderAI.AddDependencyObject('InterceptTarget', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('PriorityList', 'BuilderCreate33')
    pBuilderAI.AddDependency('PriorityList', 'CloseRange')
    pBuilderAI.AddDependency('PriorityList', 'MidRange')
    pBuilderAI.AddDependency('PriorityList', 'LongRange')
    pBuilderAI.AddDependency('PriorityList', 'InterceptTarget')
    pBuilderAI.AddAIBlock('SelectTarget', 'BuilderCreate34')
    pBuilderAI.AddDependency('SelectTarget', 'PriorityList')
    pBuilderAI.AddDependencyObject('SelectTarget', 'pAllTargetsGroup', pAllTargetsGroup)
    pBuilderAI.AddDependencyObject('SelectTarget', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddAIBlock('FollowTargetThroughWarp', 'BuilderCreate35')
    pBuilderAI.AddDependency('FollowTargetThroughWarp', 'SelectTarget')
    pBuilderAI.AddDependencyObject('FollowTargetThroughWarp', 'sInitialTarget', sInitialTarget)
    pBuilderAI.AddDependencyObject('FollowTargetThroughWarp', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('FollowThroughWarpFlag', 'BuilderCreate36')
    pBuilderAI.AddDependency('FollowThroughWarpFlag', 'FollowTargetThroughWarp')
    pBuilderAI.AddDependencyObject('FollowThroughWarpFlag', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('FleeAttackOrFollow', 'BuilderCreate37')
    pBuilderAI.AddDependency('FleeAttackOrFollow', 'CheckWarpBeforeDeath')
    pBuilderAI.AddDependency('FleeAttackOrFollow', 'NoSensorsEvasive')
    pBuilderAI.AddDependency('FleeAttackOrFollow', 'SelectTarget')
    pBuilderAI.AddDependency('FleeAttackOrFollow', 'FollowThroughWarpFlag')
    pBuilderAI.AddAIBlock('PowerManagement', 'BuilderCreate38')
    pBuilderAI.AddDependency('PowerManagement', 'FleeAttackOrFollow')
    pBuilderAI.AddDependencyObject('PowerManagement', 'dKeywords', dKeywords)
    pBuilderAI.AddAIBlock('AlertLevel', 'BuilderCreate39')
    pBuilderAI.AddDependency('AlertLevel', 'PowerManagement')
    pBuilderAI.AddAIBlock('AvoidObstaclesUpdated', 'BuilderCreate40')
    pBuilderAI.AddDependency('AvoidObstaclesUpdated', 'AlertLevel')
    return pBuilderAI


def BuilderCreate1(pShip, dKeywords):
    debug(__name__ + ", BuilderCreate1")
    import AI.Compound.Parts.WarpBeforeDeath
    pCheckWarpBeforeDeath = AI.Compound.Parts.WarpBeforeDeath.CreateAI(pShip, dKeywords)
    return pCheckWarpBeforeDeath


def BuilderCreate2(pShip):
    debug(__name__ + ", BuilderCreate2")
    import AI.Compound.Parts.NoSensorsEvasive
    pNoSensorsEvasive = AI.Compound.Parts.NoSensorsEvasive.CreateAI(pShip)
    return pNoSensorsEvasive


def BuilderCreate3(pShip, sInitialTarget):
    debug(__name__ + ", BuilderCreate3")
    pRearTorpRun = App.PlainAI_Create(pShip, 'RearTorpRun')
    pRearTorpRun.SetScriptModule('TorpedoRun')
    pRearTorpRun.SetInterruptable(1)
    pScript = pRearTorpRun.GetScriptInstance()
    pScript.SetTargetObjectName(sInitialTarget)
    pScript.SetTorpDirection(App.TGPoint3_GetModelBackward())
    return pRearTorpRun


def BuilderCreate4(pShip, pRearTorpRun, dKeywords):
    debug(__name__ + ", BuilderCreate4")
    pTorpsReady = App.ConditionScript_Create('Conditions.ConditionTorpsReady', 'ConditionTorpsReady', pShip.GetName(), App.TGPoint3_GetModelBackward())
    pUsingTorps = App.ConditionScript_Create('Conditions.ConditionUsingWeapon', 'ConditionUsingWeapon', App.CT_TORPEDO_SYSTEM)

    def EvalFunc(bTorpsReady, bUsingTorps):
        debug(__name__ + ", EvalFunc")
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if (bUsingTorps and bTorpsReady):
            return ACTIVE
        return DORMANT

    pRearTorpsReadyRearShieldOk = App.ConditionalAI_Create(pShip, 'RearTorpsReadyRearShieldOk')
    pRearTorpsReadyRearShieldOk.SetInterruptable(1)
    pRearTorpsReadyRearShieldOk.SetContainedAI(pRearTorpRun)
    pRearTorpsReadyRearShieldOk.AddCondition(pTorpsReady)
    pRearTorpsReadyRearShieldOk.AddCondition(pUsingTorps)
    pRearTorpsReadyRearShieldOk.SetEvaluationFunction(EvalFunc)
    return pRearTorpsReadyRearShieldOk


def BuilderCreate5(pShip, sInitialTarget):
    debug(__name__ + ", BuilderCreate5")
    pRearTorp2 = App.PlainAI_Create(pShip, 'RearTorp2')
    pRearTorp2.SetScriptModule('TorpedoRun')
    pRearTorp2.SetInterruptable(1)
    pScript = pRearTorp2.GetScriptInstance()
    pScript.SetTargetObjectName(sInitialTarget)
    pScript.SetTorpDirection(App.TGPoint3_GetModelBackward())
    return pRearTorp2


def BuilderCreate6(pShip, pRearTorp2):
    debug(__name__ + ", BuilderCreate6")
    pPulseWeapon = App.ConditionScript_Create('Conditions.ConditionUsingWeapon', 'ConditionUsingWeapon', App.CT_PULSE_WEAPON_SYSTEM)

    def EvalFunc(bPulseWeapon):
        debug(__name__ + ", EvalFunc")
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if bPulseWeapon:
            return ACTIVE
        return DORMANT

    pUsingPulseWeapons_2 = App.ConditionalAI_Create(pShip, 'UsingPulseWeapons_2')
    pUsingPulseWeapons_2.SetInterruptable(1)
    pUsingPulseWeapons_2.SetContainedAI(pRearTorp2)
    pUsingPulseWeapons_2.AddCondition(pPulseWeapon)
    pUsingPulseWeapons_2.SetEvaluationFunction(EvalFunc)
    return pUsingPulseWeapons_2


def BuilderCreate7(pShip, sInitialTarget, dKeywords):
    debug(__name__ + ", BuilderCreate7")
    import AI.Compound.Parts.ICOMove
    pICOMoveOut = AI.Compound.Parts.ICOMove.CreateAI(pShip, sInitialTarget, dKeywords, -0.7)
    return pICOMoveOut


def BuilderCreate8(pShip, pRearTorpsReadyRearShieldOk, pUsingPulseWeapons_2, pICOMoveOut):
    debug(__name__ + ", BuilderCreate8")
    pTooClosePriorities = App.PriorityListAI_Create(pShip, 'TooClosePriorities')
    pTooClosePriorities.SetInterruptable(1)
    pTooClosePriorities.AddAI(pRearTorpsReadyRearShieldOk, 1)
    pTooClosePriorities.AddAI(pUsingPulseWeapons_2, 2)
    pTooClosePriorities.AddAI(pICOMoveOut, 3)
    return pTooClosePriorities


def BuilderCreate9(pShip, pTooClosePriorities, fTooFarRange, sInitialTarget):
    debug(__name__ + ", BuilderCreate9")
    pInRange = App.ConditionScript_Create('Conditions.ConditionInRange', 'ConditionInRange', 25.0, sInitialTarget, pShip.GetName())

    def EvalFunc(bInRange):
        debug(__name__ + ", EvalFunc")
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if bInRange:
            return ACTIVE
        return DORMANT

    pTooClose = App.ConditionalAI_Create(pShip, 'TooClose')
    pTooClose.SetInterruptable(1)
    pTooClose.SetContainedAI(pTooClosePriorities)
    pTooClose.AddCondition(pInRange)
    pTooClose.SetEvaluationFunction(EvalFunc)
    return pTooClose


def BuilderCreate10(pShip, sInitialTarget):
    debug(__name__ + ", BuilderCreate10")
    pTorpRun_3 = App.PlainAI_Create(pShip, 'TorpRun_3')
    pTorpRun_3.SetScriptModule('TorpedoRun')
    pTorpRun_3.SetInterruptable(1)
    pScript = pTorpRun_3.GetScriptInstance()
    pScript.SetTargetObjectName(sInitialTarget)
    return pTorpRun_3


def BuilderCreate11(pShip, pTorpRun_3):
    debug(__name__ + ", BuilderCreate11")
    pReady = App.ConditionScript_Create('Conditions.ConditionTorpsReady', 'ConditionTorpsReady', pShip.GetName(), App.TGPoint3_GetModelForward())
    pUsingTorps = App.ConditionScript_Create('Conditions.ConditionUsingWeapon', 'ConditionUsingWeapon', App.CT_TORPEDO_SYSTEM)

    def EvalFunc(bReady, bUsingTorps):
        debug(__name__ + ", EvalFunc")
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if (bUsingTorps and bReady):
            return ACTIVE
        return DORMANT

    pTorpsReadyNotInterruptable = App.ConditionalAI_Create(pShip, 'TorpsReadyNotInterruptable')
    pTorpsReadyNotInterruptable.SetInterruptable(0)
    pTorpsReadyNotInterruptable.SetContainedAI(pTorpRun_3)
    pTorpsReadyNotInterruptable.AddCondition(pReady)
    pTorpsReadyNotInterruptable.AddCondition(pUsingTorps)
    pTorpsReadyNotInterruptable.SetEvaluationFunction(EvalFunc)
    return pTorpsReadyNotInterruptable


def BuilderCreate12(pShip, sInitialTarget):
    debug(__name__ + ", BuilderCreate12")
    pStationaryAttack_2 = App.PlainAI_Create(pShip, 'StationaryAttack_2')
    pStationaryAttack_2.SetScriptModule('StationaryAttack')
    pStationaryAttack_2.SetInterruptable(1)
    pScript = pStationaryAttack_2.GetScriptInstance()
    pScript.SetTargetObjectName(sInitialTarget)
    return pStationaryAttack_2


def BuilderCreate13(pShip, pStationaryAttack_2, sInitialTarget):
    debug(__name__ + ", BuilderCreate13")
    pTorpsReady = App.ConditionScript_Create('Conditions.ConditionTorpsReady', 'ConditionTorpsReady', pShip.GetName(), App.TGPoint3_GetModelForward())
    pFacingToward = App.ConditionScript_Create('Conditions.ConditionFacingToward', 'ConditionFacingToward', pShip.GetName(), sInitialTarget, 45.0, App.TGPoint3_GetModelForward(), 1)
    pUsingTorps = App.ConditionScript_Create('Conditions.ConditionUsingWeapon', 'ConditionUsingWeapon', App.CT_TORPEDO_SYSTEM)

    def EvalFunc(bTorpsReady, bFacingToward, bUsingTorps):
        debug(__name__ + ", EvalFunc")
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if (bUsingTorps and (bTorpsReady and bFacingToward)):
            return ACTIVE
        return DORMANT

    pTorpsStillReadyFacingTowardNotInterruptable = App.ConditionalAI_Create(pShip, 'TorpsStillReadyFacingTowardNotInterruptable')
    pTorpsStillReadyFacingTowardNotInterruptable.SetInterruptable(0)
    pTorpsStillReadyFacingTowardNotInterruptable.SetContainedAI(pStationaryAttack_2)
    pTorpsStillReadyFacingTowardNotInterruptable.AddCondition(pTorpsReady)
    pTorpsStillReadyFacingTowardNotInterruptable.AddCondition(pFacingToward)
    pTorpsStillReadyFacingTowardNotInterruptable.AddCondition(pUsingTorps)
    pTorpsStillReadyFacingTowardNotInterruptable.SetEvaluationFunction(EvalFunc)
    return pTorpsStillReadyFacingTowardNotInterruptable


def BuilderCreate14(pShip, pTorpsReadyNotInterruptable, pTorpsStillReadyFacingTowardNotInterruptable):
    debug(__name__ + ", BuilderCreate14")
    pPriorityList_3 = App.PriorityListAI_Create(pShip, 'PriorityList_3')
    pPriorityList_3.SetInterruptable(1)
    pPriorityList_3.AddAI(pTorpsReadyNotInterruptable, 1)
    pPriorityList_3.AddAI(pTorpsStillReadyFacingTowardNotInterruptable, 2)
    return pPriorityList_3


def BuilderCreate15(pShip, sInitialTarget):
    debug(__name__ + ", BuilderCreate15")
    pTorpRun_2 = App.PlainAI_Create(pShip, 'TorpRun_2')
    pTorpRun_2.SetScriptModule('TorpedoRun')
    pTorpRun_2.SetInterruptable(1)
    pScript = pTorpRun_2.GetScriptInstance()
    pScript.SetTargetObjectName(sInitialTarget)
    return pTorpRun_2


def BuilderCreate16(pShip, pTorpRun_2):
    debug(__name__ + ", BuilderCreate16")
    pPulseWeapon = App.ConditionScript_Create('Conditions.ConditionUsingWeapon', 'ConditionUsingWeapon', App.CT_PULSE_WEAPON_SYSTEM)

    def EvalFunc(bPulseWeapon):
        debug(__name__ + ", EvalFunc")
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if bPulseWeapon:
            return ACTIVE
        return DORMANT

    pUsingPulseWeapons = App.ConditionalAI_Create(pShip, 'UsingPulseWeapons')
    pUsingPulseWeapons.SetInterruptable(1)
    pUsingPulseWeapons.SetContainedAI(pTorpRun_2)
    pUsingPulseWeapons.AddCondition(pPulseWeapon)
    pUsingPulseWeapons.SetEvaluationFunction(EvalFunc)
    return pUsingPulseWeapons


def BuilderCreate17(pShip, sInitialTarget, dKeywords):
    debug(__name__ + ", BuilderCreate17")
    import AI.Compound.Parts.ICOMove
    pICOMoveIn_2 = AI.Compound.Parts.ICOMove.CreateAI(pShip, sInitialTarget, dKeywords, 0.8)
    return pICOMoveIn_2


def BuilderCreate18(pShip, sInitialTarget, dKeywords):
    debug(__name__ + ", BuilderCreate18")
    import AI.Compound.Parts.SweepPhasers
    pSweepPhasers = AI.Compound.Parts.SweepPhasers.CreateAI(pShip, sInitialTarget, 1.0, dKeywords)
    return pSweepPhasers


def BuilderCreate19(pShip, pPriorityList_3, pUsingPulseWeapons, pICOMoveIn_2, pSweepPhasers):
    debug(__name__ + ", BuilderCreate19")
    pTooFarPriorities = App.PriorityListAI_Create(pShip, 'TooFarPriorities')
    pTooFarPriorities.SetInterruptable(1)
    pTooFarPriorities.AddAI(pPriorityList_3, 1)
    pTooFarPriorities.AddAI(pUsingPulseWeapons, 2)
    pTooFarPriorities.AddAI(pICOMoveIn_2, 3)
    pTooFarPriorities.AddAI(pSweepPhasers, 4)
    return pTooFarPriorities


def BuilderCreate20(pShip, pTooFarPriorities, fTooCloseRange, sInitialTarget):
    debug(__name__ + ", BuilderCreate20")
    pInRange = App.ConditionScript_Create('Conditions.ConditionInRange', 'ConditionInRange', 85.0, sInitialTarget, pShip.GetName())

    def EvalFunc(bInRange):
        debug(__name__ + ", EvalFunc")
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if bInRange:
            return ACTIVE
        return DORMANT

    pTooFar = App.ConditionalAI_Create(pShip, 'TooFar')
    pTooFar.SetInterruptable(1)
    pTooFar.SetContainedAI(pTooFarPriorities)
    pTooFar.AddCondition(pInRange)
    pTooFar.SetEvaluationFunction(EvalFunc)
    return pTooFar


def BuilderCreate21(pShip, pTooClose, pTooFar):
    debug(__name__ + ", BuilderCreate21")
    pPriorityList_2 = App.PriorityListAI_Create(pShip, 'PriorityList_2')
    pPriorityList_2.SetInterruptable(1)
    pPriorityList_2.AddAI(pTooClose, 1)
    pPriorityList_2.AddAI(pTooFar, 2)
    return pPriorityList_2


def BuilderCreate22(pShip, pPriorityList_2, sInitialTarget, dKeywords):
    debug(__name__ + ", BuilderCreate22")
    import AI.Preprocessors
    pFireScript = apply(AI.Preprocessors.FireScript, (sInitialTarget,), dKeywords)
    for pSystem in [pShip.GetTorpedoSystem(), pShip.GetPhaserSystem(), pShip.GetPulseWeaponSystem()]:
        if (not App.IsNull(pSystem)):
            pFireScript.AddWeaponSystem(pSystem)

    pFireAll = App.PreprocessingAI_Create(pShip, 'FireAll')
    pFireAll.SetInterruptable(1)
    pFireAll.SetPreprocessingMethod(pFireScript, 'Update')
    pFireAll.SetContainedAI(pPriorityList_2)
    return pFireAll


def BuilderCreate23(pShip, pFireAll, fCloseRange, sInitialTarget):
    debug(__name__ + ", BuilderCreate23")
    pInRange = App.ConditionScript_Create('Conditions.ConditionInRange', 'ConditionInRange', 90, sInitialTarget, pShip.GetName())

    def EvalFunc(bInRange):
        debug(__name__ + ", EvalFunc")
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if bInRange:
            return ACTIVE
        return DORMANT

    pCloseRange = App.ConditionalAI_Create(pShip, 'CloseRange')
    pCloseRange.SetInterruptable(1)
    pCloseRange.SetContainedAI(pFireAll)
    pCloseRange.AddCondition(pInRange)
    pCloseRange.SetEvaluationFunction(EvalFunc)
    return pCloseRange


def BuilderCreate24(pShip, sInitialTarget):
    debug(__name__ + ", BuilderCreate24")
    pTorpRun = App.PlainAI_Create(pShip, 'TorpRun')
    pTorpRun.SetScriptModule('TorpedoRun')
    pTorpRun.SetInterruptable(1)
    pScript = pTorpRun.GetScriptInstance()
    pScript.SetTargetObjectName(sInitialTarget)
    return pTorpRun


def BuilderCreate25(pShip, pTorpRun):
    debug(__name__ + ", BuilderCreate25")
    pTorpsReady = App.ConditionScript_Create('Conditions.ConditionTorpsReady', 'ConditionTorpsReady', pShip.GetName(), App.TGPoint3_GetModelForward())
    pFrontLow = App.ConditionScript_Create('Conditions.ConditionSingleShieldBelow', 'ConditionSingleShieldBelow', pShip.GetName(), 0.4, App.ShieldClass.FRONT_SHIELDS)
    pUsingTorps = App.ConditionScript_Create('Conditions.ConditionUsingWeapon', 'ConditionUsingWeapon', App.CT_TORPEDO_SYSTEM)

    def EvalFunc(bTorpsReady, bFrontLow, bUsingTorps):
        debug(__name__ + ", EvalFunc")
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if (bUsingTorps and (bTorpsReady and (not bFrontLow))):
            return ACTIVE
        return DORMANT

    pTorpsReady_FwdShieldStrong = App.ConditionalAI_Create(pShip, 'TorpsReady_FwdShieldStrong')
    pTorpsReady_FwdShieldStrong.SetInterruptable(1)
    pTorpsReady_FwdShieldStrong.SetContainedAI(pTorpRun)
    pTorpsReady_FwdShieldStrong.AddCondition(pTorpsReady)
    pTorpsReady_FwdShieldStrong.AddCondition(pFrontLow)
    pTorpsReady_FwdShieldStrong.AddCondition(pUsingTorps)
    pTorpsReady_FwdShieldStrong.SetEvaluationFunction(EvalFunc)
    return pTorpsReady_FwdShieldStrong


def BuilderCreate26(pShip, sInitialTarget):
    debug(__name__ + ", BuilderCreate26")
    pMoveIn_2 = App.PlainAI_Create(pShip, 'MoveIn_2')
    pMoveIn_2.SetScriptModule('FollowObject')
    pMoveIn_2.SetInterruptable(1)
    pScript = pMoveIn_2.GetScriptInstance()
    pScript.SetFollowObjectName(sInitialTarget)
    return pMoveIn_2


def BuilderCreate27(pShip, pTorpsReady_FwdShieldStrong, pMoveIn_2):
    debug(__name__ + ", BuilderCreate27")
    pMidRangePriorities = App.PriorityListAI_Create(pShip, 'MidRangePriorities')
    pMidRangePriorities.SetInterruptable(1)
    pMidRangePriorities.AddAI(pTorpsReady_FwdShieldStrong, 1)
    pMidRangePriorities.AddAI(pMoveIn_2, 2)
    return pMidRangePriorities


def BuilderCreate28(pShip, pMidRangePriorities, sInitialTarget, dKeywords):
    debug(__name__ + ", BuilderCreate28")
    import AI.Preprocessors
    pFireScript = apply(AI.Preprocessors.FireScript, (sInitialTarget,), dKeywords)
    for pSystem in [pShip.GetTorpedoSystem(), pShip.GetPhaserSystem(), pShip.GetPulseWeaponSystem()]:
        if (not App.IsNull(pSystem)):
            pFireScript.AddWeaponSystem(pSystem)

    pFireAll2 = App.PreprocessingAI_Create(pShip, 'FireAll2')
    pFireAll2.SetInterruptable(1)
    pFireAll2.SetPreprocessingMethod(pFireScript, 'Update')
    pFireAll2.SetContainedAI(pMidRangePriorities)
    return pFireAll2


def BuilderCreate29(pShip, pFireAll2, fMidRange, sInitialTarget):
    debug(__name__ + ", BuilderCreate29")
    pInRange = App.ConditionScript_Create('Conditions.ConditionInRange', 'ConditionInRange', 200.0, sInitialTarget, pShip.GetName())

    def EvalFunc(bInRange):
        debug(__name__ + ", EvalFunc")
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if bInRange:
            return ACTIVE
        return DORMANT

    pMidRange = App.ConditionalAI_Create(pShip, 'MidRange')
    pMidRange.SetInterruptable(1)
    pMidRange.SetContainedAI(pFireAll2)
    pMidRange.AddCondition(pInRange)
    pMidRange.SetEvaluationFunction(EvalFunc)
    return pMidRange


def BuilderCreate30(pShip, sInitialTarget):
    debug(__name__ + ", BuilderCreate30")
    pMoveIn = App.PlainAI_Create(pShip, 'MoveIn')
    pMoveIn.SetScriptModule('FollowObject')
    pMoveIn.SetInterruptable(1)
    pScript = pMoveIn.GetScriptInstance()
    pScript.SetFollowObjectName(sInitialTarget)
    pScript.SetRoughDistances(fNear=395, fMid=400, fFar=401)
    return pMoveIn


def BuilderCreate31(pShip, pMoveIn, sInitialTarget):
    debug(__name__ + ", BuilderCreate31")
    pInRange = App.ConditionScript_Create('Conditions.ConditionInRange', 'ConditionInRange', 400.0, sInitialTarget, pShip.GetName())

    def EvalFunc(bInRange):
        debug(__name__ + ", EvalFunc")
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if bInRange:
            return ACTIVE
        return DORMANT

    pLongRange = App.ConditionalAI_Create(pShip, 'LongRange')
    pLongRange.SetInterruptable(1)
    pLongRange.SetContainedAI(pMoveIn)
    pLongRange.AddCondition(pInRange)
    pLongRange.SetEvaluationFunction(EvalFunc)
    return pLongRange


def BuilderCreate32(pShip, sInitialTarget):
    debug(__name__ + ", BuilderCreate32")
    pInterceptTarget = App.PlainAI_Create(pShip, 'InterceptTarget')
    pInterceptTarget.SetScriptModule('Intercept')
    pInterceptTarget.SetInterruptable(1)
    pScript = pInterceptTarget.GetScriptInstance()
    pScript.SetTargetObjectName(sInitialTarget)
    return pInterceptTarget


def BuilderCreate33(pShip, pCloseRange, pMidRange, pLongRange, pInterceptTarget):
    debug(__name__ + ", BuilderCreate33")
    pPriorityList = App.PriorityListAI_Create(pShip, 'PriorityList')
    pPriorityList.SetInterruptable(1)
    pPriorityList.AddAI(pCloseRange, 1)
    pPriorityList.AddAI(pMidRange, 2)
    pPriorityList.AddAI(pLongRange, 3)
    pPriorityList.AddAI(pInterceptTarget, 4)
    return pPriorityList


def BuilderCreate34(pShip, pPriorityList, pAllTargetsGroup, sInitialTarget):
    debug(__name__ + ", BuilderCreate34")
    import AI.Preprocessors
    pSelectionPreprocess = AI.Preprocessors.SelectTarget(pAllTargetsGroup)
    pSelectionPreprocess.ForceCurrentTargetString(sInitialTarget)
    pSelectTarget = App.PreprocessingAI_Create(pShip, 'SelectTarget')
    pSelectTarget.SetInterruptable(1)
    pSelectTarget.SetPreprocessingMethod(pSelectionPreprocess, 'Update')
    pSelectTarget.SetContainedAI(pPriorityList)
    return pSelectTarget


def BuilderCreate35(pShip, pSelectTarget, sInitialTarget, dKeywords):
    debug(__name__ + ", BuilderCreate35")
    import AI.Compound.FollowThroughWarp
    pFollowTargetThroughWarp = AI.Compound.FollowThroughWarp.CreateAI(pShip, sInitialTarget, Keywords=dKeywords)
    pSelectTarget.GetPreprocessingInstance().AddSetTargetTree(pFollowTargetThroughWarp)
    return pFollowTargetThroughWarp


def BuilderCreate36(pShip, pFollowTargetThroughWarp, dKeywords):
    debug(__name__ + ", BuilderCreate36")
    pFlagSet = App.ConditionScript_Create('Conditions.ConditionFlagSet', 'ConditionFlagSet', 'FollowTargetThroughWarp', dKeywords)

    def EvalFunc(bFlagSet):
        debug(__name__ + ", EvalFunc")
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if bFlagSet:
            return ACTIVE
        return DONE

    pFollowThroughWarpFlag = App.ConditionalAI_Create(pShip, 'FollowThroughWarpFlag')
    pFollowThroughWarpFlag.SetInterruptable(1)
    pFollowThroughWarpFlag.SetContainedAI(pFollowTargetThroughWarp)
    pFollowThroughWarpFlag.AddCondition(pFlagSet)
    pFollowThroughWarpFlag.SetEvaluationFunction(EvalFunc)
    return pFollowThroughWarpFlag


def BuilderCreate37(pShip, pCheckWarpBeforeDeath, pNoSensorsEvasive, pSelectTarget, pFollowThroughWarpFlag):
    debug(__name__ + ", BuilderCreate37")
    pFleeAttackOrFollow = App.PriorityListAI_Create(pShip, 'FleeAttackOrFollow')
    pFleeAttackOrFollow.SetInterruptable(1)
    pFleeAttackOrFollow.AddAI(pCheckWarpBeforeDeath, 1)
    pFleeAttackOrFollow.AddAI(pNoSensorsEvasive, 2)
    pFleeAttackOrFollow.AddAI(pSelectTarget, 3)
    pFleeAttackOrFollow.AddAI(pFollowThroughWarpFlag, 4)
    return pFleeAttackOrFollow


def BuilderCreate38(pShip, pFleeAttackOrFollow, dKeywords):
    debug(__name__ + ", BuilderCreate38")
    import AI.Preprocessors
    pPowerManager = AI.Preprocessors.ManagePower(0)
    pPowerManagement = App.PreprocessingAI_Create(pShip, 'PowerManagement')
    pPowerManagement.SetInterruptable(1)
    pPowerManagement.SetPreprocessingMethod(pPowerManager, 'Update')
    pPowerManagement.SetContainedAI(pFleeAttackOrFollow)
    return pPowerManagement


def BuilderCreate39(pShip, pPowerManagement):
    debug(__name__ + ", BuilderCreate39")
    import AI.Preprocessors
    pScript = AI.Preprocessors.AlertLevel(App.ShipClass.RED_ALERT)
    pAlertLevel = App.PreprocessingAI_Create(pShip, 'AlertLevel')
    pAlertLevel.SetInterruptable(1)
    pAlertLevel.SetPreprocessingMethod(pScript, 'Update')
    pAlertLevel.SetContainedAI(pPowerManagement)
    return pAlertLevel


def BuilderCreate40(pShip, pAlertLevel):
    debug(__name__ + ", BuilderCreate40")
    import AI.Compound.AvoidObstaclesUpdated
    pScript = AI.Compound.AvoidObstaclesUpdated.AvoidObstaclesUpdated()
    pAvoidObstaclesUpdated = App.PreprocessingAI_Create(pShip, 'AvoidObstaclesUpdated')
    pAvoidObstaclesUpdated.SetInterruptable(1)
    pAvoidObstaclesUpdated.SetPreprocessingMethod(pScript, 'Update')
    pAvoidObstaclesUpdated.SetContainedAI(pAlertLevel)
    return pAvoidObstaclesUpdated

# File: Z (Python 1.5)

import App
import MissionLib
import QuickBattle

def CreateAI(pShip, *lpTargets, **dKeywords):
    '''
    Friendly AI for the ZZVeritex.
    Waits 2 seconds before engaging, then uses CloakAttackWrapper aggressively.
    All available behaviors are listed for easy customization.
    Targets the enemy group (player\xe2\x80\x99s enemies).
    '''
    pEnemies = MissionLib.GetEnemyGroup()
    pEnemyGroup = App.ObjectGroupWithInfo()
    if pEnemies:
        for sName in pEnemies.GetNameTuple():
            pEnemyGroup.AddName(sName)
        
    
    import AI.Compound.CloakAttackWrapper
    pAttack = AI.Compound.CloakAttackWrapper.CreateAI(pShip, pEnemyGroup, Difficulty = dKeywords.get('Difficulty', 1.0), MaxFiringRange = 600.0, InaccurateTorps = 0, DumbFireTorps = 0, SmartTorpSelection = 1, AggressivePulseWeapons = 1, SmartPhasers = 1, AlwaysFire = 1, DisableBeforeDestroy = 0, DisableOnly = 0, CircleTarget = 1, EvadeTorps = 1, Intercept = 1, NeverSitStill = 1, UseSideArcs = 1, UseRearTorps = 1, FollowTargetThroughWarp = 1, FollowToSB12 = 0, SmartShields = 1, PowerManagement = 1, WarpOutBeforeDying = 0, AvoidTorps = 1, NoSensorsEvasive = 1, UseCloaking = 1, CloakDistance = 650.0, HighPower = 1, SmartWeaponBalance = 1)
    pTimePassed = App.ConditionScript_Create('Conditions.ConditionTimer', 'ConditionTimer', 2, 0)
    pWait = App.ConditionalAI_Create(pShip, 'WaitToEngage')
    pWait.SetInterruptable(1)
    pWait.SetContainedAI(pAttack)
    pWait.AddCondition(pTimePassed)
    
    def EvalFunc(bTimePassed):
        if bTimePassed:
            return App.ArtificialIntelligence.US_ACTIVE
        
        return App.ArtificialIntelligence.US_DORMANT

    pWait.SetEvaluationFunction(EvalFunc)
    import AI.Preprocessors
    pScript = AI.Preprocessors.AvoidObstacles()
    pAvoid = App.PreprocessingAI_Create(pShip, 'AvoidObstacles')
    pAvoid.SetInterruptable(1)
    pAvoid.SetPreprocessingMethod(pScript, 'Update')
    pAvoid.SetContainedAI(pWait)
    return pAvoid


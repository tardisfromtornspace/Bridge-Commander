import App
import QuickBattle

def CreateAI(pShip, aiLevel, warp):
    import AI.Compound.BasicAttack
    pAttack = AI.Compound.BasicAttack.CreateAI(pShip, App.ObjectGroup_FromModule('Custom.QuickBattleGame.QuickBattle', 'pEnemies'), Difficulty=aiLevel, FollowTargetThroughWarp=warp, UseCloaking=1)
    pTimePassed = App.ConditionScript_Create('Conditions.ConditionTimer', 'ConditionTimer', 7, 0)

    def EvalFunc(bTimePassed):
        ACTIVE = App.ArtificialIntelligence.US_ACTIVE
        DORMANT = App.ArtificialIntelligence.US_DORMANT
        DONE = App.ArtificialIntelligence.US_DONE
        if bTimePassed:
            return ACTIVE
        return DORMANT

    pWait = App.ConditionalAI_Create(pShip, 'Wait')
    pWait.SetInterruptable(1)
    pWait.SetContainedAI(pAttack)
    pWait.AddCondition(pTimePassed)
    pWait.SetEvaluationFunction(EvalFunc)
    import AI.Preprocessors
    pScript = AI.Preprocessors.AvoidObstacles()
    pAvoidObstacles = App.PreprocessingAI_Create(pShip, 'AvoidObstacles')
    pAvoidObstacles.SetInterruptable(1)
    pAvoidObstacles.SetPreprocessingMethod(pScript, 'Update')
    pAvoidObstacles.SetContainedAI(pWait)
    return pAvoidObstacles


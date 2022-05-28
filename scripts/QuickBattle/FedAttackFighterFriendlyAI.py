from bcdebug import debug
import App
import MissionLib
import Quickbattle

def CreateAI(pShip, pEnemies = MissionLib.GetEnemyGroup()):
    debug(__name__ + ", CreateAI")
    import AI.Compound.FedAttackFighter
    pAttack = AI.Compound.FedAttackFighter.CreateAI(pShip, pEnemies)
    pTimePassed = App.ConditionScript_Create('Conditions.ConditionTimer', 'ConditionTimer', 12, 0)

    def EvalFunc(bTimePassed):
        debug(__name__ + ", EvalFunc")
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
    return pWait


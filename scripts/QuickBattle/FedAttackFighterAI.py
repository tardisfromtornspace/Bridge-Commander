from bcdebug import debug
import App
import Quickbattle
import MissionLib
import AI.Compound.FedAttackFighter

def CreateAI(pShip):
    debug(__name__ + ", CreateAI")
    import AI.Compound.FedAttackFighter
    pAttack = AI.Compound.FedAttackFighter.CreateAI(pShip, MissionLib.GetFriendlyGroup())
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


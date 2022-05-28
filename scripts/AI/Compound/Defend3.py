import App
from bcdebug import debug

class TargetListPerparer:
        def __init__(self, pAttackGroup):
                debug(__name__ + ", __init__")
                self.pAttackers = pAttackGroup

        def SetAttackedCondition(self, pCondition):
                debug(__name__ + ", SetAttackedCondition")
                self.pAttackedCondition = pCondition

        def GetNextUpdateTime(self):
                debug(__name__ + ", GetNextUpdateTime")
                return 5.0

        def Update(self, dEndTime):
                debug(__name__ + ", Update")
                import MissionLib
                pFriendlies = MissionLib.GetFriendlyGroup()

                # Update the list of attackers from the condition.
                pScript = self.pAttackedCondition.GetConditionScript()
                lsAttackers = pScript.GetTargetList()

                if lsAttackers:
                        for sAttacker in lsAttackers:
                                # If this attacker is a Friendly object, don't add it to the
                                # list of targets.
##                              if pFriendlies and pFriendlies.IsNameInGroup(sAttacker):
##                                      continue

                                try:
                                        fShieldDamage = pScript.dfShieldDamage[sAttacker]
                                except KeyError:
                                        fShieldDamage = 0.0

                                try:
                                        fHullDamage = pScript.dfDamageDamage[sAttacker]
                                except KeyError:
                                        fHullDamage = 0.0

                                fPriority = fShieldDamage + fHullDamage
                                self.pAttackers[sAttacker] = { "Priority" : fPriority }

                return App.PreprocessingAI.PS_NORMAL



def CreateAI(pShip):
        debug(__name__ + ", CreateAI")
        pAttackGroup = App.ObjectGroupWithInfo()
        pAttackGroup[pShip.GetName()] = { "Priority" : -1000.0 }

        #########################################
        # Creating CompoundAI Attack at (120, 106)
        import AI.Compound.BasicAttack
        pAttack = AI.Compound.BasicAttack.CreateAI(pShip, pAttackGroup, AggressivePulseWeapons = 1, SmartPhasers = 1, UseCloaking = 1, WarpOutBeforeDying = 1)
        # Done creating CompoundAI Attack
        #########################################
        #########################################
        # Creating PreprocessingAI PrepTargetList at (118, 154)
        ## Setup:
        pTargetPrep = TargetListPerparer(pAttackGroup)
        ## The PreprocessingAI:
        pPrepTargetList = App.PreprocessingAI_Create(pShip, "PrepTargetList")
        pPrepTargetList.SetInterruptable(1)
        pPrepTargetList.SetPreprocessingMethod(pTargetPrep, "Update")
        pPrepTargetList.SetContainedAI(pAttack)
        # Done creating PreprocessingAI PrepTargetList
        #########################################
        #########################################
        # Creating ConditionalAI DefendeeAttacked at (117, 201)
        ## Conditions:
        #### Condition Attacked
        pAttacked = App.ConditionScript_Create("Conditions.ConditionAttacked", "ConditionAttacked", pShip.GetName(), 0.0001, 0.0001, 45)
        ## Evaluation function:
        def EvalFunc(bAttacked):
                debug(__name__ + ", EvalFunc")
                ACTIVE = App.ArtificialIntelligence.US_ACTIVE
                DORMANT = App.ArtificialIntelligence.US_DORMANT
                DONE = App.ArtificialIntelligence.US_DONE
                if bAttacked:
                        return ACTIVE
                return DORMANT
        ## The ConditionalAI:
        pDefendeeAttacked = App.ConditionalAI_Create(pShip, "DefendeeAttacked")
        pDefendeeAttacked.SetInterruptable(1)
        pDefendeeAttacked.SetContainedAI(pPrepTargetList)
        pDefendeeAttacked.AddCondition(pAttacked)
        pDefendeeAttacked.SetEvaluationFunction(EvalFunc)
        # Done creating ConditionalAI DefendeeAttacked
        #########################################
        pTargetPrep.SetAttackedCondition(pAttacked)
        return pDefendeeAttacked

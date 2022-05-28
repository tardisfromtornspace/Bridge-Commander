import App
import Quickbattle

def CreateAI(pShip):
	#########################################
	# Creating CompoundAI Attack at (150, 92)
	import AI.Compound.BasicAttack
	pAttack = AI.Compound.BasicAttack.CreateAI(pShip, App.ObjectGroup_FromModule("Custom.QuickBattleGame.QuickBattle", "pFriendlies"), Difficulty = 1.0, MaxFiringRange = 300.0, FollowTargetThroughWarp = 1, ChooseSubsystemTargets = 1, AggressivePulseWeapons = 0, DisableBeforeDestroy = 0, InaccurateTorps = 1, SmartWeaponBalance = 0, SmartShields = 1, UseSideArcs = 1, HighPower = 1, PowerManagement = 1)
	# Done creating CompoundAI Attack
	#########################################
	#########################################
	# Creating ConditionalAI TargetInRange at (86, 150)
	## Conditions:
	#### Condition InRange
	pInRange = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 4000, pShip.GetName(), App.ObjectGroup_FromModule("Custom.QuickBattleGame.QuickBattle", "pFriendlies"))
	## Evaluation function:
	def EvalFunc(bInRange):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if (bInRange):
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pTargetInRange = App.ConditionalAI_Create(pShip, "TargetInRange")
	pTargetInRange.SetInterruptable(1)
	pTargetInRange.SetContainedAI(pAttack)
	pTargetInRange.AddCondition(pInRange)
	pTargetInRange.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI TargetInRange
	#########################################
	return pTargetInRange

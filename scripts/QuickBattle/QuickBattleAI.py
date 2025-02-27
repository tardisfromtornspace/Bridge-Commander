# For Use With BorgAttack AI Only
import App
import MissionLib
import QuickBattle
def CreateAI(pShip):
	#########################################
	# Creating CompoundAI Attack at (113, 68)
	import AI.Compound.BasicAttack
	pAttack = AI.Compound.BasicAttack.CreateAI(pShip, MissionLib.GetFriendlyGroup(), Difficulty = QuickBattle.GetCurrentAILevel(), DisableBeforeDestroy = 0, AggressivePulseWeapons = 1, ChooseSubsystemTargets = 1, FollowTargetThroughWarp = 1, InaccurateTorps = 0, PowerManagement = 1, SmartPhasers = 1, SmartShields = 1, SmartTorpSelection = 1, SmartWeaponBalance = 1, UseRearTorps = 1, UseCloaking = 1, UseSideArcs = 1, WarpOutBeforeDying = 1)
	# Done creating CompoundAI Attack
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (72, 137)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 7, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pAttack)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	return pWait

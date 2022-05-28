# by USS Sovereign, a basic Starbase Attack AI

import App
import MissionLib

def CreateAI(pShip):
        pMission = MissionLib.GetMission ()
	pEnemyGroup = pMission.GetFriendlyGroup ()
	#########################################
	# Creating PlainAI LaunchFighters at (36, 67)
	pLaunchFighters = App.PlainAI_Create(pShip, "LaunchFighters")
	pLaunchFighters.SetScriptModule("RunScript")
	pLaunchFighters.SetInterruptable(1)
	pScript = pLaunchFighters.GetScriptInstance()
	pScript.SetScriptModule("Custom.DS9FX.DS9FXLib.DS9FXLauncher")
	pScript.SetFunction("LaunchEnemy")
	# Done creating PlainAI LaunchFighters
	#########################################
	#########################################
	# Creating ConditionalAI Attacked at (36, 139)
	## Conditions:
	#### Condition WasAttacked
	pWasAttacked = App.ConditionScript_Create("Conditions.ConditionAttacked", "ConditionAttacked", pShip.GetName(), 0, 0, 1)
	## Evaluation function:
	def EvalFunc(bWasAttacked):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bWasAttacked:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pAttacked = App.ConditionalAI_Create(pShip, "Attacked")
	pAttacked.SetInterruptable(1)
	pAttacked.SetContainedAI(pLaunchFighters)
	pAttacked.AddCondition(pWasAttacked)
	pAttacked.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Attacked
	#########################################
	#########################################
	# Creating CompoundAI DS9Attack at (194, 62)
	import AI.Compound.StarbaseAttack
	pDS9Attack = AI.Compound.StarbaseAttack.CreateAI(pShip, pEnemyGroup)
	# Done creating CompoundAI DS9Attack
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (193, 130)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 5, 0)
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
	pWait.SetContainedAI(pDS9Attack)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (35, 217)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (136, 179)
	pPriorityList.AddAI(pAttacked, 1)
	pPriorityList.AddAI(pWait, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	return pPriorityList

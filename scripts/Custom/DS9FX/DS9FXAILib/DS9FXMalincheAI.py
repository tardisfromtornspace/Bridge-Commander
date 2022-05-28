# by USS Sovereign, an AI for USS Malinche in a mini mission. It doesn't attack unless you attack it first!

import App
import MissionLib

def CreateAI(pShip):
        pPlayer = MissionLib.GetPlayer()
	#########################################
	# Creating CompoundAI Attackplayer at (78, 34)
	import AI.Compound.BasicAttack
	pAttackplayer = AI.Compound.BasicAttack.CreateAI(pShip, pPlayer.GetName(), Easy_Difficulty = 1.0, Easy_MaxFiringRange = 1000.0, Easy_AvoidTorps = 1, Easy_AggressivePulseWeapons = 1, Easy_ChooseSubsystemTargets = 1, Easy_SmartPhasers = 1, Easy_SmartShields = 1, Easy_SmartTorpSelection = 1, Difficulty = 1.0, MaxFiringRange = 1000.0, AvoidTorps = 1, AggressivePulseWeapons = 1, ChooseSubsystemTargets = 1, SmartPhasers = 1, SmartShields = 1, SmartTorpSelection = 1, Hard_Difficulty = 1.0, Hard_MaxFiringRange = 1000.0, Hard_AvoidTorps = 1, Hard_AggressivePulseWeapons = 1, Hard_ChooseSubsystemTargets = 1, Hard_SmartPhasers = 1, Hard_SmartShields = 1, Hard_SmartTorpSelection = 1)
	# Done creating CompoundAI Attackplayer
	#########################################
	#########################################
	# Creating ConditionalAI Attacked at (74, 130)
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
	pAttacked.SetContainedAI(pAttackplayer)
	pAttacked.AddCondition(pWasAttacked)
	pAttacked.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Attacked
	#########################################
	#########################################
	# Creating PlainAI Forward at (300, 178)
	pForward = App.PlainAI_Create(pShip, "Forward")
	pForward.SetScriptModule("GoForward")
	pForward.SetInterruptable(1)
	pScript = pForward.GetScriptInstance()
	pScript.SetImpulse(7)
	# Done creating PlainAI Forward
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (78, 174)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (210, 188)
	pPriorityList.AddAI(pAttacked, 1)
	pPriorityList.AddAI(pForward, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (62, 260)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pPriorityList)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	return pAvoidObstacles

# by USS Sovereign


import App
import MissionLib

def CreateAI(pShip):
        pMission = MissionLib.GetMission ()
	pEnemyGroup = pMission.GetEnemyGroup ()
	pPlayer = MissionLib.GetPlayer()
	#########################################
	# Creating CompoundAI Follow at (180, 126)
	import AI.Compound.FollowThroughWarp
	pFollow = AI.Compound.FollowThroughWarp.CreateAI(pShip, pPlayer.GetName(), FollowToSB12 = 1, FollowThroughMissions = 1)
	# Done creating CompoundAI Follow
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (181, 215)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 2, 0)
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
	pWait.SetContainedAI(pFollow)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	#########################################
	# Creating CompoundAI DS9FXGenericStaticAI at (332, 159)
	import AI.Compound.FedAttack
	pDS9FXGenericStaticAI = AI.Compound.FedAttack.CreateAI(pShip, pEnemyGroup)
	# Done creating CompoundAI DS9FXGenericStaticAI
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (293, 278)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (316, 255)
	pPriorityList.AddAI(pWait, 1)
	pPriorityList.AddAI(pDS9FXGenericStaticAI, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (295, 346)
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

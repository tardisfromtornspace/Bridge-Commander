# by USS Sovereign


import App
import MissionLib

def CreateAI(pShip):
        pMission = MissionLib.GetMission ()
	pEnemyGroup = pMission.GetEnemyGroup ()
	pPlayer = MissionLib.GetPlayer()
	#########################################
	# Creating CompoundAI Follow at (53, 239)
	import AI.Compound.FollowThroughWarp
	pFollow = AI.Compound.FollowThroughWarp.CreateAI(pShip, pPlayer.GetName(), FollowToSB12 = 1, FollowThroughMissions = 1)
	# Done creating CompoundAI Follow
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (61, 306)
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
	# Creating CompoundAI DS9FXGenericAI at (171, 223)
	import AI.Compound.FedAttack
	pDS9FXGenericAI = AI.Compound.FedAttack.CreateAI(pShip, pEnemyGroup)
	# Done creating CompoundAI DS9FXGenericAI
	#########################################
	#########################################
	# Creating PlainAI Forward1 at (167, 146)
	pForward1 = App.PlainAI_Create(pShip, "Forward1")
	pForward1.SetScriptModule("GoForward")
	pForward1.SetInterruptable(1)
	pScript = pForward1.GetScriptInstance()
	pScript.SetImpulse(3)
	# Done creating PlainAI Forward1
	#########################################
	#########################################
	# Creating PlainAI Forward2 at (190, 102)
	pForward2 = App.PlainAI_Create(pShip, "Forward2")
	pForward2.SetScriptModule("GoForward")
	pForward2.SetInterruptable(1)
	pScript = pForward2.GetScriptInstance()
	pScript.SetImpulse(7)
	# Done creating PlainAI Forward2
	#########################################
	#########################################
	# Creating PlainAI Stay at (299, 84)
	pStay = App.PlainAI_Create(pShip, "Stay")
	pStay.SetScriptModule("Stay")
	pStay.SetInterruptable(1)
	# Done creating PlainAI Stay
	#########################################
	#########################################
	# Creating PlainAI Forward3 at (400, 101)
	pForward3 = App.PlainAI_Create(pShip, "Forward3")
	pForward3.SetScriptModule("GoForward")
	pForward3.SetInterruptable(1)
	pScript = pForward3.GetScriptInstance()
	pScript.SetImpulse(2)
	# Done creating PlainAI Forward3
	#########################################
	#########################################
	# Creating RandomAI AISequence at (280, 220)
	pAISequence = App.RandomAI_Create(pShip, "AISequence")
	pAISequence.SetInterruptable(1)
	# SeqBlock is at (315, 179)
	pAISequence.AddAI(pForward1)
	pAISequence.AddAI(pForward2)
	pAISequence.AddAI(pStay)
	pAISequence.AddAI(pForward3)
	# Done creating RandomAI AISequence
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (209, 371)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (244, 334)
	pPriorityList.AddAI(pWait, 1)
	pPriorityList.AddAI(pDS9FXGenericAI, 2)
	pPriorityList.AddAI(pAISequence, 3)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (217, 432)
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

# USS Oregon's AI, which also moves rather pointlesly and attacks an enemy when it sees one

# by USS Sovereign


import App
import MissionLib

def CreateAI(pShip):
        pMission = MissionLib.GetMission ()
	pEnemyGroup = pMission.GetFriendlyGroup ()
	#########################################
	# Creating CompoundAI DS9FXOregonAI at (236, 186)
	import AI.Compound.NonFedAttack
	pDS9FXOregonAI = AI.Compound.NonFedAttack.CreateAI(pShip, pEnemyGroup)
	# Done creating CompoundAI DS9FXOregonAI
	#########################################
	#########################################
	# Creating PlainAI ManeuverLoop at (232, 85)
	pManeuverLoop = App.PlainAI_Create(pShip, "ManeuverLoop")
	pManeuverLoop.SetScriptModule("ManeuverLoop")
	pManeuverLoop.SetInterruptable(1)
	pScript = pManeuverLoop.GetScriptInstance()
	pScript.SetLoopFraction(fFraction = 8.0)
	pScript.SetTurnAxis(vAxis = App.TGPoint3_GetModelLeft())
	pScript.SetSpeeds(fStartSpeed = 5.0, fEndSpeed = 5.0)
	# Done creating PlainAI ManeuverLoop
	#########################################
	#########################################
	# Creating PlainAI Forward at (358, 82)
	pForward = App.PlainAI_Create(pShip, "Forward")
	pForward.SetScriptModule("GoForward")
	pForward.SetInterruptable(1)
	pScript = pForward.GetScriptInstance()
	pScript.SetImpulse(7)
	# Done creating PlainAI Forward
	#########################################
	#########################################
	# Creating RandomAI AISequence at (92, 36)
	pAISequence = App.RandomAI_Create(pShip, "AISequence")
	pAISequence.SetInterruptable(1)
	# SeqBlock is at (195, 10)
	pAISequence.AddAI(pManeuverLoop)
	pAISequence.AddAI(pForward)
	# Done creating RandomAI AISequence
	#########################################
	#########################################
	# Creating SequenceAI Sequence at (409, 195)
	pSequence = App.SequenceAI_Create(pShip, "Sequence")
	pSequence.SetInterruptable(1)
	pSequence.SetLoopCount(-1)
	pSequence.SetResetIfInterrupted(1)
	pSequence.SetDoubleCheckAllDone(1)
	pSequence.SetSkipDormant(0)
	# SeqBlock is at (90, 101)
	pSequence.AddAI(pAISequence)
	# Done creating SequenceAI Sequence
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (50, 273)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (174, 367)
	pPriorityList.AddAI(pDS9FXOregonAI, 1)
	pPriorityList.AddAI(pSequence, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (51, 386)
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

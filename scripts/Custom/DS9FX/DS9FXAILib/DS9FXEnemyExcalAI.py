# by USS Sovereign an AI which circles around DS9 and when sees an enemy it immediately attacks it

import App
import MissionLib
def CreateAI(pShip):
        pMission = MissionLib.GetMission ()
	pEnemyGroup = pMission.GetFriendlyGroup ()
	#########################################
	# Creating CompoundAI DS9FXExcalAI at (206, 224)
	import AI.Compound.BasicAttack
	pDS9FXExcalAI = AI.Compound.BasicAttack.CreateAI(pShip, pEnemyGroup, Easy_Difficulty = 1.0, Easy_MaxFiringRange = 1000.0, Easy_AvoidTorps = 1, Easy_AggressivePulseWeapons = 1, Easy_ChooseSubsystemTargets = 1, Easy_DisableBeforeDestroy = 1, Easy_SmartPhasers = 1, Easy_SmartShields = 1, Easy_SmartTorpSelection = 1, Difficulty = 1.0, MaxFiringRange = 1000.0, AvoidTorps = 1, AggressivePulseWeapons = 1, ChooseSubsystemTargets = 1, DisableBeforeDestroy = 1, SmartPhasers = 1, SmartShields = 1, SmartTorpSelection = 1, Hard_Difficulty = 1.0, Hard_MaxFiringRange = 1000.0, Hard_AvoidTorps = 1, Hard_AggressivePulseWeapons = 1, Hard_ChooseSubsystemTargets = 1, Hard_DisableBeforeDestroy = 1, Hard_SmartPhasers = 1, Hard_SmartShields = 1, Hard_SmartTorpSelection = 1)
	# Done creating CompoundAI DS9FXExcalAI
	#########################################
	#########################################
	# Creating PlainAI Move at (225, 56)
	pMove = App.PlainAI_Create(pShip, "Move")
	pMove.SetScriptModule("IntelligentCircleObject")
	pMove.SetInterruptable(1)
	pScript = pMove.GetScriptInstance()
	pScript.SetFollowObjectName("Deep_Space_9")
	pScript.SetCircleSpeed(fSpeed = 1.0)
	pScript.UseFixedCode(bUseFixed = 0)
	# Done creating PlainAI Move
	#########################################
	#########################################
	# Creating SequenceAI Sequence at (312, 323)
	pSequence = App.SequenceAI_Create(pShip, "Sequence")
	pSequence.SetInterruptable(1)
	pSequence.SetLoopCount(-1)
	pSequence.SetResetIfInterrupted(1)
	pSequence.SetDoubleCheckAllDone(1)
	pSequence.SetSkipDormant(0)
	# SeqBlock is at (373, 286)
	pSequence.AddAI(pMove)
	# Done creating SequenceAI Sequence
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (50, 172)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (180, 323)
	pPriorityList.AddAI(pDS9FXExcalAI, 1)
	pPriorityList.AddAI(pSequence, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI ExcalAvoidObstacles at (42, 264)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pExcalAvoidObstacles = App.PreprocessingAI_Create(pShip, "ExcalAvoidObstacles")
	pExcalAvoidObstacles.SetInterruptable(1)
	pExcalAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pExcalAvoidObstacles.SetContainedAI(pPriorityList)
	# Done creating PreprocessingAI ExcalAvoidObstacles
	#########################################
	return pExcalAvoidObstacles

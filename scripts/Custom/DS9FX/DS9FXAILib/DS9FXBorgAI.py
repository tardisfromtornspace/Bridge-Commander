# Borg AI for DS9FX assigned when a DS9FX Borg Object is created

import App
import MissionLib

def GetGroup(sGroup):
	lsTargets = None
	if sGroup == "Enemy":
		lsTargets = MissionLib.GetEnemyGroup()
	elif sGroup == "Friendly":
		lsTargets = MissionLib.GetFriendlyGroup()
	return lsTargets

def GetTarget(lsTargets):
	lTargets = lsTargets.GetNameTuple()
	i = len(lTargets)
	if i <= 0:
		sTarget = lTargets[0]
	else:
		iRand = App.g_kSystemWrapper.GetRandomNumber(i) + 1
		iRand = iRand - 1
		if iRand < 0:
			iRand = 0
		sTarget = lTargets[iRand]
	return sTarget

def CreateAI(pShip, sGroup):
	lsTargets = GetGroup(sGroup)
	if not lsTargets:
		return
	    
	sTarget = GetTarget(lsTargets)
	if not sTarget:
		return
	    
	#########################################
	# Creating PlainAI InterceptTarget at (232, 76)
	pInterceptTarget = App.PlainAI_Create(pShip, "InterceptTarget")
	pInterceptTarget.SetScriptModule("Intercept")
	pInterceptTarget.SetInterruptable(1)
	pScript = pInterceptTarget.GetScriptInstance()
	pScript.SetTargetObjectName(sTarget)
	# Done creating PlainAI InterceptTarget
	#########################################
	#########################################
	# Creating PreprocessingAI SelectTarget at (105, 134)
	## Setup:
	import AI.Preprocessors
	pSelectionPreprocess = AI.Preprocessors.SelectTarget(lsTargets)
	pSelectionPreprocess.ForceCurrentTargetString(sTarget)
	## The PreprocessingAI:
	pSelectTarget = App.PreprocessingAI_Create(pShip, "SelectTarget")
	pSelectTarget.SetInterruptable(1)
	pSelectTarget.SetPreprocessingMethod(pSelectionPreprocess, "Update")
	pSelectTarget.SetContainedAI(pInterceptTarget)
	# Done creating PreprocessingAI SelectTarget
	#########################################
	#########################################
	# Creating ConditionalAI MoveTime at (108, 246)
	## Conditions:
	#### Condition Timer
	pTimer = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 7)
	## Evaluation function:
	def EvalFunc(bTimer):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimer:
			return DORMANT
		return ACTIVE
	## The ConditionalAI:
	pMoveTime = App.ConditionalAI_Create(pShip, "MoveTime")
	pMoveTime.SetInterruptable(1)
	pMoveTime.SetContainedAI(pSelectTarget)
	pMoveTime.AddCondition(pTimer)
	pMoveTime.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI MoveTime
	#########################################
	#########################################
	# Creating CompoundAI StarbaseAttack at (366, 132)
	import AI.Compound.StarbaseAttack
	pStarbaseAttack = AI.Compound.StarbaseAttack.CreateAI(pShip,  lsTargets)
	# Done creating CompoundAI StarbaseAttack
	#########################################
	#########################################
	# Creating ConditionalAI FireTimer at (368, 243)
	## Conditions:
	#### Condition Timer
	pTimer = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 7)
	## Evaluation function:
	def EvalFunc(bTimer):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimer:
			return DORMANT
		return ACTIVE
	## The ConditionalAI:
	pFireTimer = App.ConditionalAI_Create(pShip, "FireTimer")
	pFireTimer.SetInterruptable(1)
	pFireTimer.SetContainedAI(pStarbaseAttack)
	pFireTimer.AddCondition(pTimer)
	pFireTimer.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI FireTimer
	#########################################
	#########################################
	# Creating SequenceAI Sequence at (235, 331)
	pSequence = App.SequenceAI_Create(pShip, "Sequence")
	pSequence.SetInterruptable(1)
	pSequence.SetLoopCount(-1)
	pSequence.SetResetIfInterrupted(1)
	pSequence.SetDoubleCheckAllDone(1)
	pSequence.SetSkipDormant(1)
	# SeqBlock is at (259, 303)
	pSequence.AddAI(pMoveTime)
	pSequence.AddAI(pFireTimer)
	# Done creating SequenceAI Sequence
	#########################################
	return pSequence

import App
import Quickbattle

def CreateAI(pShip, pTarget):
	if pTarget:
		sTarget = pTarget.GetName()
		fTargetRadius = pTarget.GetRadius()
	else:
		sTarget = ""
		fTargetRadius = 0.0
		
	lTargetSubsystems = [
		(App.CT_WEAPON_SYSTEM, 5),
		(App.CT_WEAPON, 5),
#		(App.CT_TRACTOR_BEAM_SYSTEM, 1),
#		(App.CT_SHIELD_SUBSYSTEM, 1),
#		(App.CT_CLOAKING_SUBSYSTEM, 2),
		(App.CT_HULL_SUBSYSTEM, 1),
		(App.CT_IMPULSE_ENGINE_SUBSYSTEM, 2) ]

	# Not useful to try to attack if we're farther than this distance.
	fMaxWeaponDist = 25.0 / 0.175		# 15 km base

	# add our ship and target ship's radius so that it's 15km from
	# surface to surface (approximately).  This will keep us from running
	# into big ships when we're attacking.
	fMaxWeaponDist = fMaxWeaponDist + pShip.GetRadius() + fTargetRadius





















	#########################################
	# Creating PlainAI TorpRun at (36, 23)
	pTorpRun = App.PlainAI_Create(pShip, "TorpRun")
	pTorpRun.SetScriptModule("TorpedoRun")
	pTorpRun.SetInterruptable(1)
	pScript = pTorpRun.GetScriptInstance()
	pScript.SetTargetObjectName(sTarget)
	pScript.SetPerpendicularMovementAdjustment(0.25)
	# Done creating PlainAI TorpRun
	#########################################
	#########################################
	# Creating PreprocessingAI AttackStatus_LiningUpFront at (36, 64)
	## Setup:
	import AI.Preprocessors
	pPreprocess = AI.Preprocessors.UpdateAIStatus("AttackStatus_LiningUpFront")
	## The PreprocessingAI:
	pAttackStatus_LiningUpFront = App.PreprocessingAI_Create(pShip, "AttackStatus_LiningUpFront")
	pAttackStatus_LiningUpFront.SetInterruptable(1)
	pAttackStatus_LiningUpFront.SetPreprocessingMethod(pPreprocess, "Update")
	pAttackStatus_LiningUpFront.SetContainedAI(pTorpRun)
	# Done creating PreprocessingAI AttackStatus_LiningUpFront
	#########################################
	#########################################
	# Creating ConditionalAI Torps_Ready at (37, 107)
	## Conditions:
	#### Condition Ready
	pReady = App.ConditionScript_Create("Conditions.ConditionTorpsReady", "ConditionTorpsReady", pShip.GetName(), App.TGPoint3_GetModelForward())
	#### Condition UsingTorps
	pUsingTorps = App.ConditionScript_Create("Conditions.ConditionUsingWeapon", "ConditionUsingWeapon", App.CT_TORPEDO_SYSTEM)
	#### Condition InRange
	pInRange = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 27.5/ 0.175, pShip.GetName(), sTarget)
	## Evaluation function:
	def EvalFunc(bReady, bUsingTorps, bInRange):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bReady and bUsingTorps and not bInRange:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pTorps_Ready = App.ConditionalAI_Create(pShip, "Torps_Ready")
	pTorps_Ready.SetInterruptable(0)
	pTorps_Ready.SetContainedAI(pAttackStatus_LiningUpFront)
	pTorps_Ready.AddCondition(pReady)
	pTorps_Ready.AddCondition(pUsingTorps)
	pTorps_Ready.AddCondition(pInRange)
	pTorps_Ready.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Torps_Ready
	#########################################
	#########################################
	# Creating PlainAI EvadeTorps at (123, 23)
	pEvadeTorps = App.PlainAI_Create(pShip, "EvadeTorps")
	pEvadeTorps.SetScriptModule("EvadeTorps")
	pEvadeTorps.SetInterruptable(1)
	# Done creating PlainAI EvadeTorps
	#########################################
	#########################################
	# Creating PreprocessingAI AttackStatus_EvadingTorps at (123, 64)
	## Setup:
	import AI.Preprocessors
	pPreprocess = AI.Preprocessors.UpdateAIStatus("AttackStatus_EvadingTorps1")
	## The PreprocessingAI:
	pAttackStatus_EvadingTorps = App.PreprocessingAI_Create(pShip, "AttackStatus_EvadingTorps")
	pAttackStatus_EvadingTorps.SetInterruptable(1)
	pAttackStatus_EvadingTorps.SetPreprocessingMethod(pPreprocess, "Update")
	pAttackStatus_EvadingTorps.SetContainedAI(pEvadeTorps)
	# Done creating PreprocessingAI AttackStatus_EvadingTorps
	#########################################
	#########################################
	# Creating ConditionalAI IncomingTorps at (124, 107)
	## Conditions:
	#### Condition Incoming
	pIncoming = App.ConditionScript_Create("Conditions.ConditionIncomingTorps", "ConditionIncomingTorps", pShip.GetName(), sTarget)
	## Evaluation function:
	def EvalFunc(bIncoming):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bIncoming:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pIncomingTorps = App.ConditionalAI_Create(pShip, "IncomingTorps")
	pIncomingTorps.SetInterruptable(1)
	pIncomingTorps.SetContainedAI(pAttackStatus_EvadingTorps)
	pIncomingTorps.AddCondition(pIncoming)
	pIncomingTorps.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI IncomingTorps
	#########################################
	#########################################
	# Creating PlainAI PhaserSweep at (211, 66)
	pPhaserSweep = App.PlainAI_Create(pShip, "PhaserSweep")
	pPhaserSweep.SetScriptModule("PhaserSweep")
	pPhaserSweep.SetInterruptable(1)
	pScript = pPhaserSweep.GetScriptInstance()
	pScript.SetTargetObjectName(sTarget)
	pScript.SetSweepPhasersDuringRun(100.0)
	pScript.SetSpeedFraction(1.0)
	pScript.SetPrimaryDirection(App.TGPoint3_GetModelForward())
	# Done creating PlainAI PhaserSweep
	#########################################
	#########################################
	# Creating PreprocessingAI AttackStatus_SweepingPhasers at (209, 108)
	## Setup:
	import AI.Preprocessors
	pPreprocess = AI.Preprocessors.UpdateAIStatus("AttackStatus_SweepingPhasers")
	## The PreprocessingAI:
	pAttackStatus_SweepingPhasers = App.PreprocessingAI_Create(pShip, "AttackStatus_SweepingPhasers")
	pAttackStatus_SweepingPhasers.SetInterruptable(1)
	pAttackStatus_SweepingPhasers.SetPreprocessingMethod(pPreprocess, "Update")
	pAttackStatus_SweepingPhasers.SetContainedAI(pPhaserSweep)
	# Done creating PreprocessingAI AttackStatus_SweepingPhasers
	#########################################
	#########################################
	# Creating PlainAI PhaserSweep_4 at (302, 28)
	pPhaserSweep_4 = App.PlainAI_Create(pShip, "PhaserSweep_4")
	pPhaserSweep_4.SetScriptModule("PhaserSweep")
	pPhaserSweep_4.SetInterruptable(1)
	pScript = pPhaserSweep_4.GetScriptInstance()
	pScript.SetTargetObjectName(sTarget)
	pScript.SetSweepPhasersDuringRun(100.0)
	pScript.SetSpeedFraction(1.0)
	pScript.SetPrimaryDirection(App.TGPoint3_GetModelForward())
	# Done creating PlainAI PhaserSweep_4
	#########################################
	#########################################
	# Creating PreprocessingAI AttackStatus_FallingBack at (303, 69)
	## Setup:
	import AI.Preprocessors
	pPreprocess = AI.Preprocessors.UpdateAIStatus("AttackStatus_FallingBack")
	## The PreprocessingAI:
	pAttackStatus_FallingBack = App.PreprocessingAI_Create(pShip, "AttackStatus_FallingBack")
	pAttackStatus_FallingBack.SetInterruptable(1)
	pAttackStatus_FallingBack.SetPreprocessingMethod(pPreprocess, "Update")
	pAttackStatus_FallingBack.SetContainedAI(pPhaserSweep_4)
	# Done creating PreprocessingAI AttackStatus_FallingBack
	#########################################
	#########################################
	# Creating RandomAI Random at (157, 152)
	pRandom = App.RandomAI_Create(pShip, "Random")
	pRandom.SetInterruptable(1)
	# SeqBlock is at (278, 159)
	pRandom.AddAI(pAttackStatus_SweepingPhasers)
	pRandom.AddAI(pAttackStatus_FallingBack)
	# Done creating RandomAI Random
	#########################################
	#########################################
	# Creating PriorityListAI TooFarPriorities at (2, 152)
	pTooFarPriorities = App.PriorityListAI_Create(pShip, "TooFarPriorities")
	pTooFarPriorities.SetInterruptable(1)
	# SeqBlock is at (99, 159)
	pTooFarPriorities.AddAI(pTorps_Ready, 1)
	pTooFarPriorities.AddAI(pIncomingTorps, 2)
	pTooFarPriorities.AddAI(pRandom, 3)
	# Done creating PriorityListAI TooFarPriorities
	#########################################
	#########################################
	# Creating ConditionalAI TooFar__MoreThan30km at (44, 204)
	## Conditions:
	#### Condition Close
	pClose = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 30.0 / 0.175, pShip.GetName(), sTarget)
	#### Condition TooFar
	pTooFar = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 50.0 / 0.175, pShip.GetName(), sTarget)
	## Evaluation function:
	def EvalFunc(bClose, bTooFar):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if not bClose and bTooFar:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pTooFar__MoreThan30km = App.ConditionalAI_Create(pShip, "TooFar__MoreThan30km")
	pTooFar__MoreThan30km.SetInterruptable(1)
	pTooFar__MoreThan30km.SetContainedAI(pTooFarPriorities)
	pTooFar__MoreThan30km.AddCondition(pClose)
	pTooFar__MoreThan30km.AddCondition(pTooFar)
	pTooFar__MoreThan30km.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI TooFar__MoreThan30km
	#########################################
	#########################################
	# Creating PlainAI EvadeTorps_2 at (322, 112)
	pEvadeTorps_2 = App.PlainAI_Create(pShip, "EvadeTorps_2")
	pEvadeTorps_2.SetScriptModule("EvadeTorps")
	pEvadeTorps_2.SetInterruptable(1)
	# Done creating PlainAI EvadeTorps_2
	#########################################
	#########################################
	# Creating PreprocessingAI AttackStatus_EvadingTorps_2 at (322, 154)
	## Setup:
	import AI.Preprocessors
	pPreprocess = AI.Preprocessors.UpdateAIStatus("AttackStatus_EvadingTorps1")
	## The PreprocessingAI:
	pAttackStatus_EvadingTorps_2 = App.PreprocessingAI_Create(pShip, "AttackStatus_EvadingTorps_2")
	pAttackStatus_EvadingTorps_2.SetInterruptable(1)
	pAttackStatus_EvadingTorps_2.SetPreprocessingMethod(pPreprocess, "Update")
	pAttackStatus_EvadingTorps_2.SetContainedAI(pEvadeTorps_2)
	# Done creating PreprocessingAI AttackStatus_EvadingTorps_2
	#########################################
	#########################################
	# Creating ConditionalAI IncomingTorps_2 at (324, 196)
	## Conditions:
	#### Condition Incoming
	pIncoming = App.ConditionScript_Create("Conditions.ConditionIncomingTorps", "ConditionIncomingTorps", pShip.GetName(), sTarget)
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 1.5, 0)
	## Evaluation function:
	def EvalFunc(bIncoming, bTimePassed):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bIncoming and not bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pIncomingTorps_2 = App.ConditionalAI_Create(pShip, "IncomingTorps_2")
	pIncomingTorps_2.SetInterruptable(1)
	pIncomingTorps_2.SetContainedAI(pAttackStatus_EvadingTorps_2)
	pIncomingTorps_2.AddCondition(pIncoming)
	pIncomingTorps_2.AddCondition(pTimePassed)
	pIncomingTorps_2.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI IncomingTorps_2
	#########################################
	#########################################
	# Creating PlainAI RearTorpRun at (410, 112)
	pRearTorpRun = App.PlainAI_Create(pShip, "RearTorpRun")
	pRearTorpRun.SetScriptModule("TorpedoRun")
	pRearTorpRun.SetInterruptable(1)
	pScript = pRearTorpRun.GetScriptInstance()
	pScript.SetTargetObjectName(sTarget)
	pScript.SetTorpDirection(App.TGPoint3_GetModelBackward())
	# Done creating PlainAI RearTorpRun
	#########################################
	#########################################
	# Creating PreprocessingAI AttackStatus_RearTorpRun at (411, 154)
	## Setup:
	import AI.Preprocessors
	pPreprocess = AI.Preprocessors.UpdateAIStatus("AttackStatus_RearTorpRun")
	## The PreprocessingAI:
	pAttackStatus_RearTorpRun = App.PreprocessingAI_Create(pShip, "AttackStatus_RearTorpRun")
	pAttackStatus_RearTorpRun.SetInterruptable(1)
	pAttackStatus_RearTorpRun.SetPreprocessingMethod(pPreprocess, "Update")
	pAttackStatus_RearTorpRun.SetContainedAI(pRearTorpRun)
	# Done creating PreprocessingAI AttackStatus_RearTorpRun
	#########################################
	#########################################
	# Creating ConditionalAI RearTorpedosReady at (411, 196)
	## Conditions:
	#### Condition TorpsReady
	pTorpsReady = App.ConditionScript_Create("Conditions.ConditionTorpsReady", "ConditionTorpsReady", pShip.GetName(), App.TGPoint3_GetModelBackward())
	#### Condition UsingTorps
	pUsingTorps = App.ConditionScript_Create("Conditions.ConditionUsingWeapon", "ConditionUsingWeapon", App.CT_TORPEDO_SYSTEM)
	## Evaluation function:
	def EvalFunc(bTorpsReady, bUsingTorps):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTorpsReady and bUsingTorps:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pRearTorpedosReady = App.ConditionalAI_Create(pShip, "RearTorpedosReady")
	pRearTorpedosReady.SetInterruptable(1)
	pRearTorpedosReady.SetContainedAI(pAttackStatus_RearTorpRun)
	pRearTorpedosReady.AddCondition(pTorpsReady)
	pRearTorpedosReady.AddCondition(pUsingTorps)
	pRearTorpedosReady.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI RearTorpedosReady
	#########################################
	#########################################
	# Creating PlainAI TorpRun_2 at (508, 177)
	pTorpRun_2 = App.PlainAI_Create(pShip, "TorpRun_2")
	pTorpRun_2.SetScriptModule("TorpedoRun")
	pTorpRun_2.SetInterruptable(1)
	pScript = pTorpRun_2.GetScriptInstance()
	pScript.SetTargetObjectName(sTarget)
	pScript.SetPerpendicularMovementAdjustment(0.25)
	# Done creating PlainAI TorpRun_2
	#########################################
	#########################################
	# Creating PreprocessingAI AttackStatus_LiningUpFront_2 at (508, 219)
	## Setup:
	import AI.Preprocessors
	pPreprocess = AI.Preprocessors.UpdateAIStatus("AttackStatus_LiningUpFront")
	## The PreprocessingAI:
	pAttackStatus_LiningUpFront_2 = App.PreprocessingAI_Create(pShip, "AttackStatus_LiningUpFront_2")
	pAttackStatus_LiningUpFront_2.SetInterruptable(1)
	pAttackStatus_LiningUpFront_2.SetPreprocessingMethod(pPreprocess, "Update")
	pAttackStatus_LiningUpFront_2.SetContainedAI(pTorpRun_2)
	# Done creating PreprocessingAI AttackStatus_LiningUpFront_2
	#########################################
	#########################################
	# Creating ConditionalAI Torps_Ready_2 at (422, 239)
	## Conditions:
	#### Condition Ready
	pReady = App.ConditionScript_Create("Conditions.ConditionTorpsReady", "ConditionTorpsReady", pShip.GetName(), App.TGPoint3_GetModelForward())
	#### Condition UsingTorps
	pUsingTorps = App.ConditionScript_Create("Conditions.ConditionUsingWeapon", "ConditionUsingWeapon", App.CT_TORPEDO_SYSTEM)
	#### Condition InRange
	pInRange = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 22.5/ 0.175, pShip.GetName(), sTarget)
	## Evaluation function:
	def EvalFunc(bReady, bUsingTorps, bInRange):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bReady and bUsingTorps and not bInRange:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pTorps_Ready_2 = App.ConditionalAI_Create(pShip, "Torps_Ready_2")
	pTorps_Ready_2.SetInterruptable(0)
	pTorps_Ready_2.SetContainedAI(pAttackStatus_LiningUpFront_2)
	pTorps_Ready_2.AddCondition(pReady)
	pTorps_Ready_2.AddCondition(pUsingTorps)
	pTorps_Ready_2.AddCondition(pInRange)
	pTorps_Ready_2.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Torps_Ready_2
	#########################################
	#########################################
	# Creating PlainAI PhaserSweep_3 at (436, 286)
	pPhaserSweep_3 = App.PlainAI_Create(pShip, "PhaserSweep_3")
	pPhaserSweep_3.SetScriptModule("PhaserSweep")
	pPhaserSweep_3.SetInterruptable(1)
	pScript = pPhaserSweep_3.GetScriptInstance()
	pScript.SetTargetObjectName(sTarget)
	pScript.SetSweepPhasersDuringRun(180.0)
	pScript.SetSpeedFraction(1.0)
	pScript.SetPrimaryDirection(App.TGPoint3_GetModelBackward())
	# Done creating PlainAI PhaserSweep_3
	#########################################
	#########################################
	# Creating PreprocessingAI AttackStatus_FallingBack_2 at (435, 327)
	## Setup:
	import AI.Preprocessors
	pPreprocess = AI.Preprocessors.UpdateAIStatus("AttackStatus_FallingBack")
	## The PreprocessingAI:
	pAttackStatus_FallingBack_2 = App.PreprocessingAI_Create(pShip, "AttackStatus_FallingBack_2")
	pAttackStatus_FallingBack_2.SetInterruptable(1)
	pAttackStatus_FallingBack_2.SetPreprocessingMethod(pPreprocess, "Update")
	pAttackStatus_FallingBack_2.SetContainedAI(pPhaserSweep_3)
	# Done creating PreprocessingAI AttackStatus_FallingBack_2
	#########################################
	#########################################
	# Creating PlainAI PhaserSweep_2 at (521, 285)
	pPhaserSweep_2 = App.PlainAI_Create(pShip, "PhaserSweep_2")
	pPhaserSweep_2.SetScriptModule("PhaserSweep")
	pPhaserSweep_2.SetInterruptable(1)
	pScript = pPhaserSweep_2.GetScriptInstance()
	pScript.SetTargetObjectName(sTarget)
	pScript.SetSweepPhasersDuringRun(180.0)
	pScript.SetSpeedFraction(1.0)
	pScript.SetPrimaryDirection(App.TGPoint3_GetModelBackward())
	# Done creating PlainAI PhaserSweep_2
	#########################################
	#########################################
	# Creating PreprocessingAI AttackStatus_SweepingPhasers_2 at (521, 327)
	## Setup:
	import AI.Preprocessors
	pPreprocess = AI.Preprocessors.UpdateAIStatus("AttackStatus_SweepingPhasers")
	## The PreprocessingAI:
	pAttackStatus_SweepingPhasers_2 = App.PreprocessingAI_Create(pShip, "AttackStatus_SweepingPhasers_2")
	pAttackStatus_SweepingPhasers_2.SetInterruptable(1)
	pAttackStatus_SweepingPhasers_2.SetPreprocessingMethod(pPreprocess, "Update")
	pAttackStatus_SweepingPhasers_2.SetContainedAI(pPhaserSweep_2)
	# Done creating PreprocessingAI AttackStatus_SweepingPhasers_2
	#########################################
	#########################################
	# Creating RandomAI Random_2 at (433, 370)
	pRandom_2 = App.RandomAI_Create(pShip, "Random_2")
	pRandom_2.SetInterruptable(1)
	# SeqBlock is at (527, 377)
	pRandom_2.AddAI(pAttackStatus_FallingBack_2)
	pRandom_2.AddAI(pAttackStatus_SweepingPhasers_2)
	# Done creating RandomAI Random_2
	#########################################
	#########################################
	# Creating PriorityListAI TooClosePriorities at (240, 221)
	pTooClosePriorities = App.PriorityListAI_Create(pShip, "TooClosePriorities")
	pTooClosePriorities.SetInterruptable(1)
	# SeqBlock is at (370, 274)
	pTooClosePriorities.AddAI(pIncomingTorps_2, 1)
	pTooClosePriorities.AddAI(pRearTorpedosReady, 2)
	pTooClosePriorities.AddAI(pTorps_Ready_2, 3)
	pTooClosePriorities.AddAI(pRandom_2, 4)
	# Done creating PriorityListAI TooClosePriorities
	#########################################
	#########################################
	# Creating ConditionalAI TooClose30km at (127, 241)
	## Conditions:
	#### Condition Close
	pClose = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 30.0 / 0.175, pShip.GetName(), sTarget)
	## Evaluation function:
	def EvalFunc(bClose):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bClose:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pTooClose30km = App.ConditionalAI_Create(pShip, "TooClose30km")
	pTooClose30km.SetInterruptable(1)
	pTooClose30km.SetContainedAI(pTooClosePriorities)
	pTooClose30km.AddCondition(pClose)
	pTooClose30km.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI TooClose30km
	#########################################
	#########################################
	# Creating PlainAI EvadeTorps_3 at (260, 260)
	pEvadeTorps_3 = App.PlainAI_Create(pShip, "EvadeTorps_3")
	pEvadeTorps_3.SetScriptModule("EvadeTorps")
	pEvadeTorps_3.SetInterruptable(1)
	# Done creating PlainAI EvadeTorps_3
	#########################################
	#########################################
	# Creating PreprocessingAI AttackStatus_EvadingTorps_3 at (260, 301)
	## Setup:
	import AI.Preprocessors
	pPreprocess = AI.Preprocessors.UpdateAIStatus("AttackStatus_EvadingTorps1")
	## The PreprocessingAI:
	pAttackStatus_EvadingTorps_3 = App.PreprocessingAI_Create(pShip, "AttackStatus_EvadingTorps_3")
	pAttackStatus_EvadingTorps_3.SetInterruptable(1)
	pAttackStatus_EvadingTorps_3.SetPreprocessingMethod(pPreprocess, "Update")
	pAttackStatus_EvadingTorps_3.SetContainedAI(pEvadeTorps_3)
	# Done creating PreprocessingAI AttackStatus_EvadingTorps_3
	#########################################
	#########################################
	# Creating ConditionalAI IncomingTorps_3 at (259, 343)
	## Conditions:
	#### Condition Incoming
	pIncoming = App.ConditionScript_Create("Conditions.ConditionIncomingTorps", "ConditionIncomingTorps", pShip.GetName(), sTarget)
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 5, 0)
	## Evaluation function:
	def EvalFunc(bIncoming, bTimePassed):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bIncoming and not bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pIncomingTorps_3 = App.ConditionalAI_Create(pShip, "IncomingTorps_3")
	pIncomingTorps_3.SetInterruptable(1)
	pIncomingTorps_3.SetContainedAI(pAttackStatus_EvadingTorps_3)
	pIncomingTorps_3.AddCondition(pIncoming)
	pIncomingTorps_3.AddCondition(pTimePassed)
	pIncomingTorps_3.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI IncomingTorps_3
	#########################################
	#########################################
	# Creating PlainAI MoveIn at (346, 328)
	pMoveIn = App.PlainAI_Create(pShip, "MoveIn")
	pMoveIn.SetScriptModule("FollowObject")
	pMoveIn.SetInterruptable(1)
	pScript = pMoveIn.GetScriptInstance()
	pScript.SetFollowObjectName(sTarget)
	# Done creating PlainAI MoveIn
	#########################################
	#########################################
	# Creating PreprocessingAI AttackStatus_MovingIn at (345, 370)
	## Setup:
	import AI.Preprocessors
	pPreprocess = AI.Preprocessors.UpdateAIStatus("AttackStatus_MovingIn")
	## The PreprocessingAI:
	pAttackStatus_MovingIn = App.PreprocessingAI_Create(pShip, "AttackStatus_MovingIn")
	pAttackStatus_MovingIn.SetInterruptable(1)
	pAttackStatus_MovingIn.SetPreprocessingMethod(pPreprocess, "Update")
	pAttackStatus_MovingIn.SetContainedAI(pMoveIn)
	# Done creating PreprocessingAI AttackStatus_MovingIn
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (167, 328)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (250, 377)
	pPriorityList.AddAI(pIncomingTorps_3, 1)
	pPriorityList.AddAI(pAttackStatus_MovingIn, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating ConditionalAI VeryFar__Over50km at (167, 370)
	## Conditions:
	#### Condition InRangeCond
	pInRangeCond = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 50.0 / 0.175, pShip.GetName(), sTarget)
	## Evaluation function:
	def EvalFunc(bInRangeCond):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bInRangeCond:
			return DORMANT
		return ACTIVE
	## The ConditionalAI:
	pVeryFar__Over50km = App.ConditionalAI_Create(pShip, "VeryFar__Over50km")
	pVeryFar__Over50km.SetInterruptable(1)
	pVeryFar__Over50km.SetContainedAI(pPriorityList)
	pVeryFar__Over50km.AddCondition(pInRangeCond)
	pVeryFar__Over50km.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI VeryFar__Over50km
	#########################################
	#########################################
	# Creating SequenceAI Sequence at (2, 289)
	pSequence = App.SequenceAI_Create(pShip, "Sequence")
	pSequence.SetInterruptable(1)
	pSequence.SetLoopCount(-1)
	pSequence.SetResetIfInterrupted(1)
	pSequence.SetDoubleCheckAllDone(1)
	pSequence.SetSkipDormant(1)
	# SeqBlock is at (126, 283)
	pSequence.AddAI(pTooFar__MoreThan30km)
	pSequence.AddAI(pTooClose30km)
	pSequence.AddAI(pVeryFar__Over50km)
	# Done creating SequenceAI Sequence
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (83, 310)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pSequence)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	#########################################
	# Creating PreprocessingAI Fire at (2, 330)
	## Setup:
	import AI.Preprocessors
	pFireScript = AI.Preprocessors.FireScript(sTarget, TargetSubsystems=lTargetSubsystems, MaxFiringRange = (50.0 / 0.175))
	for pSystem in [ pShip.GetTorpedoSystem(), pShip.GetPhaserSystem(), pShip.GetPulseWeaponSystem(), pShip.GetTractorBeamSystem()]:
		if pSystem:
			pFireScript.AddWeaponSystem( pSystem )
	pFireScript.UsePlayerSettings(1)
	## The PreprocessingAI:
	pFire = App.PreprocessingAI_Create(pShip, "Fire")
	pFire.SetInterruptable(1)
	pFire.SetPreprocessingMethod(pFireScript, "Update(1")
	pFire.SetContainedAI(pAvoidObstacles)
	# Done creating PreprocessingAI Fire
	#########################################
	#########################################
	# Creating PreprocessingAI SelectTarget at (83, 350)
	## Setup:
	import AI.Preprocessors
	import MissionLib
	pEnemies = MissionLib.GetMission().GetEnemyGroup()
	pSelectionPreprocess = AI.Preprocessors.SelectTarget(pEnemies)
	if sTarget:
		pSelectionPreprocess.SetRelativeImportance(fDistance = 21.0, fInFront = 0.2, fIsTarget = -0.1, fShield = 0.2, fWeapons = 15.0, fHull = 7.5, fDamage = 30.0, fPriority = 1.0, fPopularity = -1.1)
	pSelectionPreprocess.UsePlayerSettings()
	pSelectionPreprocess.UpdateTargetInfo(1.0)
	## The PreprocessingAI:
	pSelectTarget = App.PreprocessingAI_Create(pShip, "SelectTarget")
	pSelectTarget.SetInterruptable(1)
	pSelectTarget.SetPreprocessingMethod(pSelectionPreprocess, "Update(1")
	pSelectTarget.SetContainedAI(pFire)
	# Done creating PreprocessingAI SelectTarget
	#########################################
	#########################################
	# Creating PreprocessingAI FelixReport at (2, 370)
	## Setup:
	import AI.Preprocessors
	pPreprocess = AI.Preprocessors.FelixReportStatus()
	## The PreprocessingAI:
	pFelixReport = App.PreprocessingAI_Create(pShip, "FelixReport")
	pFelixReport.SetInterruptable(1)
	pFelixReport.SetPreprocessingMethod(pPreprocess, "Update")
	pFelixReport.SetContainedAI(pSelectTarget)
	# Done creating PreprocessingAI FelixReport
	#########################################
	return pFelixReport

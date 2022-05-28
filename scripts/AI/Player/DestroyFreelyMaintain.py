from bcdebug import debug
import App

def CreateAI(pShip, pTarget):
	debug(__name__ + ", CreateAI")
	if pTarget:
		sTarget = pTarget.GetName()
	else:
		sTarget = ""

	#########################################
	# Creating PlainAI TorpedoRun at (321, 162)
	pTorpedoRun = App.PlainAI_Create(pShip, "TorpedoRun")
	pTorpedoRun.SetScriptModule("TorpedoRun")
	pTorpedoRun.SetInterruptable(1)
	pScript = pTorpedoRun.GetScriptInstance()
	pScript.SetTargetObjectName(sTarget)
	pScript.SetPerpendicularMovementAdjustment(fSpeedFactor = 0.25)
	pScript.SetTorpDirection(vDirection = App.TGPoint3_GetModelForward())
	# Done creating PlainAI TorpedoRun
	#########################################
	#########################################
	# Creating PreprocessingAI AttackStatus_LiningUpFront at (313, 213)
	## Setup:
	import AI.Preprocessors
	pPreprocess = AI.Preprocessors.UpdateAIStatus("AttackStatus_LiningUpFront")
	## The PreprocessingAI:
	pAttackStatus_LiningUpFront = App.PreprocessingAI_Create(pShip, "AttackStatus_LiningUpFront")
	pAttackStatus_LiningUpFront.SetInterruptable(1)
	pAttackStatus_LiningUpFront.SetPreprocessingMethod(pPreprocess, "Update")
	pAttackStatus_LiningUpFront.SetContainedAI(pTorpedoRun)
	# Done creating PreprocessingAI AttackStatus_LiningUpFront
	#########################################
	#########################################
	# Creating ConditionalAI ForwardTorpsReady_2 at (316, 263)
	## Conditions:
	#### Condition TorpsReady
	pTorpsReady = App.ConditionScript_Create("Conditions.ConditionTorpsReady", "ConditionTorpsReady", pShip.GetName(), App.TGPoint3_GetModelForward())
	#### Condition UsingTorps
	pUsingTorps = App.ConditionScript_Create("Conditions.ConditionUsingWeapon", "ConditionUsingWeapon", App.CT_TORPEDO_SYSTEM)
	## Evaluation function:
	def EvalFunc(bTorpsReady, bUsingTorps):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTorpsReady and bUsingTorps:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pForwardTorpsReady_2 = App.ConditionalAI_Create(pShip, "ForwardTorpsReady_2")
	pForwardTorpsReady_2.SetInterruptable(1)
	pForwardTorpsReady_2.SetContainedAI(pAttackStatus_LiningUpFront)
	pForwardTorpsReady_2.AddCondition(pTorpsReady)
	pForwardTorpsReady_2.AddCondition(pUsingTorps)
	pForwardTorpsReady_2.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI ForwardTorpsReady_2
	#########################################
	#########################################
	# Creating PlainAI TurnAway at (425, 162)
	pTurnAway = App.PlainAI_Create(pShip, "TurnAway")
	pTurnAway.SetScriptModule("TurnToOrientation")
	pTurnAway.SetInterruptable(1)
	pScript = pTurnAway.GetScriptInstance()
	pScript.SetObjectName(sTarget)
	pScript.SetPrimaryDirection(App.TGPoint3_GetModelBackward())
	# Done creating PlainAI TurnAway
	#########################################
	#########################################
	# Creating PreprocessingAI AttackStatus_RearTorpRun at (418, 216)
	## Setup:
	import AI.Preprocessors
	pPreprocess = AI.Preprocessors.UpdateAIStatus("AttackStatus_RearTorpRun")
	## The PreprocessingAI:
	pAttackStatus_RearTorpRun = App.PreprocessingAI_Create(pShip, "AttackStatus_RearTorpRun")
	pAttackStatus_RearTorpRun.SetInterruptable(1)
	pAttackStatus_RearTorpRun.SetPreprocessingMethod(pPreprocess, "Update")
	pAttackStatus_RearTorpRun.SetContainedAI(pTurnAway)
	# Done creating PreprocessingAI AttackStatus_RearTorpRun
	#########################################
	#########################################
	# Creating ConditionalAI RearTorpsReady_2 at (418, 263)
	## Conditions:
	#### Condition TorpsReady
	pTorpsReady = App.ConditionScript_Create("Conditions.ConditionTorpsReady", "ConditionTorpsReady", pShip.GetName(), App.TGPoint3_GetModelBackward())
	#### Condition UsingTorps
	pUsingTorps = App.ConditionScript_Create("Conditions.ConditionUsingWeapon", "ConditionUsingWeapon", App.CT_TORPEDO_SYSTEM)
	## Evaluation function:
	def EvalFunc(bTorpsReady, bUsingTorps):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTorpsReady and bUsingTorps:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pRearTorpsReady_2 = App.ConditionalAI_Create(pShip, "RearTorpsReady_2")
	pRearTorpsReady_2.SetInterruptable(1)
	pRearTorpsReady_2.SetContainedAI(pAttackStatus_RearTorpRun)
	pRearTorpsReady_2.AddCondition(pTorpsReady)
	pRearTorpsReady_2.AddCondition(pUsingTorps)
	pRearTorpsReady_2.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI RearTorpsReady_2
	#########################################
	#########################################
	# Creating PlainAI ICOWeapons at (491, 323)
	pICOWeapons = App.PlainAI_Create(pShip, "ICOWeapons")
	pICOWeapons.SetScriptModule("IntelligentCircleObject")
	pICOWeapons.SetInterruptable(1)
	pScript = pICOWeapons.GetScriptInstance()
	pScript.SetFollowObjectName(sTarget)
	pScript.SetShieldAndWeaponImportance(0.1, 0.9)
	# Done creating PlainAI ICOWeapons
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (99, 153)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (333, 342)
	pPriorityList.AddAI(pForwardTorpsReady_2, 1)
	pPriorityList.AddAI(pRearTorpsReady_2, 2)
	pPriorityList.AddAI(pICOWeapons, 3)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles_DestroyFreelyMaintain at (46, 204)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles_DestroyFreelyMaintain = App.PreprocessingAI_Create(pShip, "AvoidObstacles_DestroyFreelyMaintain")
	pAvoidObstacles_DestroyFreelyMaintain.SetInterruptable(1)
	pAvoidObstacles_DestroyFreelyMaintain.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles_DestroyFreelyMaintain.SetContainedAI(pPriorityList)
	# Done creating PreprocessingAI AvoidObstacles_DestroyFreelyMaintain
	#########################################
	#########################################
	# Creating PreprocessingAI Fire at (30, 263)
	## Setup:
	import AI.Preprocessors
	pFireScript = AI.Preprocessors.FireScript(sTarget)
	for pSystem in [ pShip.GetTorpedoSystem(), pShip.GetPhaserSystem(), pShip.GetPulseWeaponSystem() ]:
		if pSystem:
			pFireScript.AddWeaponSystem( pSystem )
	## The PreprocessingAI:
	pFire = App.PreprocessingAI_Create(pShip, "Fire")
	pFire.SetInterruptable(1)
	pFire.SetPreprocessingMethod(pFireScript, "Update")
	pFire.SetContainedAI(pAvoidObstacles_DestroyFreelyMaintain)
	# Done creating PreprocessingAI Fire
	#########################################
	#########################################
	# Creating PreprocessingAI SelectTarget at (27, 307)
	## Setup:
	import AI.Preprocessors
	import MissionLib
	pEnemies = MissionLib.GetMission().GetEnemyGroup()
	pSelectionPreprocess = AI.Preprocessors.SelectTarget(pEnemies)
	if sTarget:
		pSelectionPreprocess.ForceCurrentTargetString(sTarget)
	pSelectionPreprocess.UsePlayerSettings()
	## The PreprocessingAI:
	pSelectTarget = App.PreprocessingAI_Create(pShip, "SelectTarget")
	pSelectTarget.SetInterruptable(1)
	pSelectTarget.SetPreprocessingMethod(pSelectionPreprocess, "Update")
	pSelectTarget.SetContainedAI(pFire)
	# Done creating PreprocessingAI SelectTarget
	#########################################
	#########################################
	# Creating PreprocessingAI FelixReport at (22, 357)
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

	######### AI Builder Begin #########
## BUILDER AI
##  This AI file has been mauled by the MakeBuilderAI script.
##  Modify at your own risk.
##  Or run MakeBuilderAI(filename, 1) to remove the BuilderAI code.
	########## AI Builder End ##########
import App
import AI.Compound.RamAttack


def SetRamAI(pShip, pAllTargetsGroup):
        pTarget = pShip.GetTarget()
        if pTarget:
                pShip.SetAI(AI.Compound.RamAttack.CreateAI(pShip, pTarget.GetName(), pAllTargetsGroup))


def DomAI(pShip, pAllTargetsGroup):
        pShip.SetAI(CreateAI(pShip, pAllTargetsGroup))
        

def CreateAI(pShip, *lpTargets, **dKeywords):
	# Make a group for all the targets...
	pAllTargetsGroup = App.ObjectGroup_ForceToGroup(lpTargets)
	sInitialTarget = pAllTargetsGroup.GetNameTuple()[0]

	Random = lambda fMin, fMax : App.g_kSystemWrapper.GetRandomNumber((fMax - fMin) * 1000.0) / 1000.0 - fMin

	# Range values used in the AI.
	fCloseRange = 100.0 + Random(-20, 10)
	fMidRange = 200.0 + Random(-25, 20)
	fLongRange = 350.0 + Random(-20, 10)


	######### AI Builder Begin #########
	pBuilderAI = App.BuilderAI_Create(pShip, "AlertLevel Builder", __name__)
	pBuilderAI.AddAIBlock("CheckWarpBeforeDeath", "BuilderCreate1")
	pBuilderAI.AddDependencyObject("CheckWarpBeforeDeath", "dKeywords", dKeywords)
	pBuilderAI.AddAIBlock("NoSensorsEvasive", "BuilderCreate2")
	pBuilderAI.AddAIBlock("Ram", "BuilderCreate3")
	pBuilderAI.AddDependencyObject("Ram", "pAllTargetsGroup", pAllTargetsGroup)
	pBuilderAI.AddAIBlock("ConditionPlayerStronger", "BuilderCreate4")
	pBuilderAI.AddDependency("ConditionPlayerStronger", "Ram")
	pBuilderAI.AddDependencyObject("ConditionPlayerStronger", "sInitialTarget", sInitialTarget)
	pBuilderAI.AddDependencyObject("ConditionPlayerStronger", "fCloseRange", fCloseRange)
	pBuilderAI.AddAIBlock("EvadeTorps_2", "BuilderCreate5")
	pBuilderAI.AddDependencyObject("EvadeTorps_2", "sInitialTarget", sInitialTarget)
	pBuilderAI.AddDependencyObject("EvadeTorps_2", "dKeywords", dKeywords)
	pBuilderAI.AddAIBlock("TorpRun_2", "BuilderCreate6")
	pBuilderAI.AddDependencyObject("TorpRun_2", "sInitialTarget", sInitialTarget)
	pBuilderAI.AddAIBlock("NoStopping", "BuilderCreate7")
	pBuilderAI.AddDependency("NoStopping", "TorpRun_2")
	pBuilderAI.AddDependencyObject("NoStopping", "dKeywords", dKeywords)
	pBuilderAI.AddAIBlock("StationaryAttack", "BuilderCreate8")
	pBuilderAI.AddDependencyObject("StationaryAttack", "sInitialTarget", sInitialTarget)
	pBuilderAI.AddAIBlock("PriorityList_2", "BuilderCreate9")
	pBuilderAI.AddDependency("PriorityList_2", "NoStopping")
	pBuilderAI.AddDependency("PriorityList_2", "StationaryAttack")
	pBuilderAI.AddAIBlock("FwdTorpsOrPulseReady", "BuilderCreate10")
	pBuilderAI.AddDependency("FwdTorpsOrPulseReady", "PriorityList_2")
	pBuilderAI.AddDependencyObject("FwdTorpsOrPulseReady", "dKeywords", dKeywords)
	pBuilderAI.AddAIBlock("ICOMoveAround", "BuilderCreate11")
	pBuilderAI.AddDependencyObject("ICOMoveAround", "dKeywords", dKeywords)
	pBuilderAI.AddDependencyObject("ICOMoveAround", "sInitialTarget", sInitialTarget)
	pBuilderAI.AddAIBlock("CloseRangePriorities", "BuilderCreate12")
	pBuilderAI.AddDependency("CloseRangePriorities", "EvadeTorps_2")
	pBuilderAI.AddDependency("CloseRangePriorities", "FwdTorpsOrPulseReady")
	pBuilderAI.AddDependency("CloseRangePriorities", "ICOMoveAround")
	pBuilderAI.AddAIBlock("FireAll", "BuilderCreate13")
	pBuilderAI.AddDependency("FireAll", "CloseRangePriorities")
	pBuilderAI.AddDependencyObject("FireAll", "sInitialTarget", sInitialTarget)
	pBuilderAI.AddDependencyObject("FireAll", "dKeywords", dKeywords)
	pBuilderAI.AddAIBlock("CloseRange", "BuilderCreate14")
	pBuilderAI.AddDependency("CloseRange", "FireAll")
	pBuilderAI.AddDependencyObject("CloseRange", "fCloseRange", fCloseRange)
	pBuilderAI.AddDependencyObject("CloseRange", "sInitialTarget", sInitialTarget)
	pBuilderAI.AddAIBlock("InterceptTarget", "BuilderCreate15")
	pBuilderAI.AddDependencyObject("InterceptTarget", "sInitialTarget", sInitialTarget)
	pBuilderAI.AddAIBlock("PriorityList", "BuilderCreate16")
	pBuilderAI.AddDependency("PriorityList", "ConditionPlayerStronger")
	pBuilderAI.AddDependency("PriorityList", "CloseRange")
	pBuilderAI.AddDependency("PriorityList", "InterceptTarget")
	pBuilderAI.AddAIBlock("SelectTarget", "BuilderCreate17")
	pBuilderAI.AddDependency("SelectTarget", "PriorityList")
	pBuilderAI.AddDependencyObject("SelectTarget", "pAllTargetsGroup", pAllTargetsGroup)
	pBuilderAI.AddDependencyObject("SelectTarget", "sInitialTarget", sInitialTarget)
	pBuilderAI.AddAIBlock("FollowTargetThroughWarp", "BuilderCreate18")
	pBuilderAI.AddDependency("FollowTargetThroughWarp", "SelectTarget")
	pBuilderAI.AddDependencyObject("FollowTargetThroughWarp", "sInitialTarget", sInitialTarget)
	pBuilderAI.AddDependencyObject("FollowTargetThroughWarp", "dKeywords", dKeywords)
	pBuilderAI.AddAIBlock("FollowThroughWarpFlag", "BuilderCreate19")
	pBuilderAI.AddDependency("FollowThroughWarpFlag", "FollowTargetThroughWarp")
	pBuilderAI.AddDependencyObject("FollowThroughWarpFlag", "dKeywords", dKeywords)
	pBuilderAI.AddAIBlock("FleeAttackOrFollow", "BuilderCreate20")
	pBuilderAI.AddDependency("FleeAttackOrFollow", "CheckWarpBeforeDeath")
	pBuilderAI.AddDependency("FleeAttackOrFollow", "NoSensorsEvasive")
	pBuilderAI.AddDependency("FleeAttackOrFollow", "SelectTarget")
	pBuilderAI.AddDependency("FleeAttackOrFollow", "FollowThroughWarpFlag")
	pBuilderAI.AddAIBlock("PowerManagement", "BuilderCreate21")
	pBuilderAI.AddDependency("PowerManagement", "FleeAttackOrFollow")
	pBuilderAI.AddDependencyObject("PowerManagement", "dKeywords", dKeywords)
	pBuilderAI.AddAIBlock("AlertLevel", "BuilderCreate22")
	pBuilderAI.AddDependency("AlertLevel", "PowerManagement")
	return pBuilderAI # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate1(pShip, dKeywords):
	########## AI Builder End ##########
	#########################################
	# Creating CompoundAI CheckWarpBeforeDeath at (205, 332)
	import AI.Compound.Parts.WarpBeforeDeath
	pCheckWarpBeforeDeath = AI.Compound.Parts.WarpBeforeDeath.CreateAI(pShip, dKeywords)
	# Done creating CompoundAI CheckWarpBeforeDeath
	#########################################
	# Builder AI Dependency Object (dKeywords)
	######### AI Builder Begin #########
	return pCheckWarpBeforeDeath  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate2(pShip):
	########## AI Builder End ##########
	#########################################
	# Creating CompoundAI NoSensorsEvasive at (221, 373)
	import AI.Compound.Parts.NoSensorsEvasive
	pNoSensorsEvasive = AI.Compound.Parts.NoSensorsEvasive.CreateAI(pShip)
	# Done creating CompoundAI NoSensorsEvasive
	#########################################
	######### AI Builder Begin #########
	return pNoSensorsEvasive  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate3(pShip, pAllTargetsGroup):
	########## AI Builder End ##########
	#########################################
	# Creating PlainAI Ram at (527, 528)
	pRam = App.PlainAI_Create(pShip, "Ram")
	pRam.SetScriptModule("RunScript")
	pRam.SetInterruptable(1)
	pScript = pRam.GetScriptInstance()
	pScript.SetScriptModule("AI.Compound.DomRamAI")
	pScript.SetFunction("SetRamAI")
	pScript.SetArguments(pShip, pAllTargetsGroup)
	pScript.SetRepeatTime(fRepeatTime = -1)
	# Done creating PlainAI Ram
	#########################################
	# Builder AI Dependency Object (pAllTargetsGroup)
	######### AI Builder Begin #########
	return pRam  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate4(pShip, pRam, sInitialTarget, fCloseRange):
	########## AI Builder End ##########
	#########################################
	# Creating ConditionalAI ConditionPlayerStronger at (388, 548)
	## Conditions:
	#### Condition PlayerStronger
	pPlayerStronger = App.ConditionScript_Create("Conditions.FriendliesInPlayerSetStronger", "FriendliesInPlayerSetStronger", 3.0)
	#### Condition InRange
	pInRange = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", fCloseRange, sInitialTarget, pShip.GetName())
	## Evaluation function:
	def EvalFunc(bPlayerStronger, bInRange):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bPlayerStronger and bInRange:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pConditionPlayerStronger = App.ConditionalAI_Create(pShip, "ConditionPlayerStronger")
	pConditionPlayerStronger.SetInterruptable(1)
	pConditionPlayerStronger.SetContainedAI(pRam)
	pConditionPlayerStronger.AddCondition(pPlayerStronger)
	pConditionPlayerStronger.AddCondition(pInRange)
	pConditionPlayerStronger.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI ConditionPlayerStronger
	#########################################
	# Builder AI Dependency Object (sInitialTarget)
	# Builder AI Dependency Object (fCloseRange)
	######### AI Builder Begin #########
	return pConditionPlayerStronger  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate5(pShip, sInitialTarget, dKeywords):
	########## AI Builder End ##########
	#########################################
	# Creating CompoundAI EvadeTorps_2 at (671, 366)
	import AI.Compound.Parts.EvadeTorps
	pEvadeTorps_2 = AI.Compound.Parts.EvadeTorps.CreateAI(pShip, sInitialTarget, dKeywords)
	# Done creating CompoundAI EvadeTorps_2
	#########################################
	# Builder AI Dependency Object (sInitialTarget)
	# Builder AI Dependency Object (dKeywords)
	######### AI Builder Begin #########
	return pEvadeTorps_2  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate6(pShip, sInitialTarget):
	########## AI Builder End ##########
	#########################################
	# Creating PlainAI TorpRun_2 at (870, 66)
	pTorpRun_2 = App.PlainAI_Create(pShip, "TorpRun_2")
	pTorpRun_2.SetScriptModule("TorpedoRun")
	pTorpRun_2.SetInterruptable(1)
	pScript = pTorpRun_2.GetScriptInstance()
	pScript.SetTargetObjectName(sInitialTarget)
	pScript.SetPerpendicularMovementAdjustment(0.5)
	# Done creating PlainAI TorpRun_2
	#########################################
	# Builder AI Dependency Object (sInitialTarget)
	######### AI Builder Begin #########
	return pTorpRun_2  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate7(pShip, pTorpRun_2, dKeywords):
	########## AI Builder End ##########
	#########################################
	# Creating ConditionalAI NoStopping at (829, 124)
	## Conditions:
	#### Condition FlagSet
	pFlagSet = App.ConditionScript_Create("Conditions.ConditionFlagSet", "ConditionFlagSet", "NeverSitStill", dKeywords)
	## Evaluation function:
	def EvalFunc(bFlagSet):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bFlagSet:
			return ACTIVE
		return DONE
	## The ConditionalAI:
	pNoStopping = App.ConditionalAI_Create(pShip, "NoStopping")
	pNoStopping.SetInterruptable(1)
	pNoStopping.SetContainedAI(pTorpRun_2)
	pNoStopping.AddCondition(pFlagSet)
	pNoStopping.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI NoStopping
	#########################################
	# Builder AI Dependency Object (dKeywords)
	######### AI Builder Begin #########
	return pNoStopping  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate8(pShip, sInitialTarget):
	########## AI Builder End ##########
	#########################################
	# Creating PlainAI StationaryAttack at (889, 167)
	pStationaryAttack = App.PlainAI_Create(pShip, "StationaryAttack")
	pStationaryAttack.SetScriptModule("StationaryAttack")
	pStationaryAttack.SetInterruptable(1)
	pScript = pStationaryAttack.GetScriptInstance()
	pScript.SetTargetObjectName(sInitialTarget)
	# Done creating PlainAI StationaryAttack
	#########################################
	# Builder AI Dependency Object (sInitialTarget)
	######### AI Builder Begin #########
	return pStationaryAttack  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate9(pShip, pNoStopping, pStationaryAttack):
	########## AI Builder End ##########
	#########################################
	# Creating PriorityListAI PriorityList_2 at (728, 167)
	pPriorityList_2 = App.PriorityListAI_Create(pShip, "PriorityList_2")
	pPriorityList_2.SetInterruptable(1)
	# SeqBlock is at (820, 174)
	pPriorityList_2.AddAI(pNoStopping, 1)
	pPriorityList_2.AddAI(pStationaryAttack, 2)
	# Done creating PriorityListAI PriorityList_2
	#########################################
	######### AI Builder Begin #########
	return pPriorityList_2  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate10(pShip, pPriorityList_2, dKeywords):
	########## AI Builder End ##########
	#########################################
	# Creating ConditionalAI FwdTorpsOrPulseReady at (687, 219)
	## Conditions:
	#### Condition TorpsReady
	pTorpsReady = App.ConditionScript_Create("Conditions.ConditionTorpsReady", "ConditionTorpsReady", pShip.GetName(), App.TGPoint3_GetModelForward())
	#### Condition PulseReady
	pPulseReady = App.ConditionScript_Create("Conditions.ConditionPulseReady", "ConditionPulseReady", pShip.GetName(), App.TGPoint3_GetModelForward())
	#### Condition AggroPulse
	pAggroPulse = App.ConditionScript_Create("Conditions.ConditionFlagSet", "ConditionFlagSet", "AggressivePulseWeapons", dKeywords)
	#### Condition UsingTorps
	pUsingTorps = App.ConditionScript_Create("Conditions.ConditionUsingWeapon", "ConditionUsingWeapon", App.CT_TORPEDO_SYSTEM)
	## Evaluation function:
	def EvalFunc(bTorpsReady, bPulseReady, bAggroPulse, bUsingTorps):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if (bUsingTorps and bTorpsReady)  or  (bAggroPulse and bPulseReady):
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pFwdTorpsOrPulseReady = App.ConditionalAI_Create(pShip, "FwdTorpsOrPulseReady")
	pFwdTorpsOrPulseReady.SetInterruptable(1)
	pFwdTorpsOrPulseReady.SetContainedAI(pPriorityList_2)
	pFwdTorpsOrPulseReady.AddCondition(pTorpsReady)
	pFwdTorpsOrPulseReady.AddCondition(pPulseReady)
	pFwdTorpsOrPulseReady.AddCondition(pAggroPulse)
	pFwdTorpsOrPulseReady.AddCondition(pUsingTorps)
	pFwdTorpsOrPulseReady.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI FwdTorpsOrPulseReady
	#########################################
	# Builder AI Dependency Object (dKeywords)
	######### AI Builder Begin #########
	return pFwdTorpsOrPulseReady  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate11(pShip, dKeywords, sInitialTarget):
	########## AI Builder End ##########
	#########################################
	# Creating CompoundAI ICOMoveAround at (703, 311)
	import AI.Compound.Parts.ICOMove
	pICOMoveAround = AI.Compound.Parts.ICOMove.CreateAI(pShip, sInitialTarget, dKeywords)
	# Done creating CompoundAI ICOMoveAround
	#########################################
	# Builder AI Dependency Object (dKeywords)
	# Builder AI Dependency Object (sInitialTarget)
	######### AI Builder Begin #########
	return pICOMoveAround  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate12(pShip, pEvadeTorps_2, pFwdTorpsOrPulseReady, pICOMoveAround):
	########## AI Builder End ##########
	#########################################
	# Creating PriorityListAI CloseRangePriorities at (565, 258)
	pCloseRangePriorities = App.PriorityListAI_Create(pShip, "CloseRangePriorities")
	pCloseRangePriorities.SetInterruptable(1)
	# SeqBlock is at (662, 265)
	pCloseRangePriorities.AddAI(pEvadeTorps_2, 1)
	pCloseRangePriorities.AddAI(pFwdTorpsOrPulseReady, 2)
	pCloseRangePriorities.AddAI(pICOMoveAround, 3)
	# Done creating PriorityListAI CloseRangePriorities
	#########################################
	######### AI Builder Begin #########
	return pCloseRangePriorities  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate13(pShip, pCloseRangePriorities, sInitialTarget, dKeywords):
	########## AI Builder End ##########
	#########################################
	# Creating PreprocessingAI FireAll at (524, 308)
	## Setup:
	import AI.Preprocessors
	pFireScript = apply(AI.Preprocessors.FireScript, (sInitialTarget,), dKeywords)
	for pSystem in [ pShip.GetTorpedoSystem(), pShip.GetPhaserSystem(), pShip.GetPulseWeaponSystem() ]:
		if not App.IsNull(pSystem):
			pFireScript.AddWeaponSystem( pSystem )
	## The PreprocessingAI:
	pFireAll = App.PreprocessingAI_Create(pShip, "FireAll")
	pFireAll.SetInterruptable(1)
	pFireAll.SetPreprocessingMethod(pFireScript, "Update")
	pFireAll.SetContainedAI(pCloseRangePriorities)
	# Done creating PreprocessingAI FireAll
	#########################################
	# Builder AI Dependency Object (sInitialTarget)
	# Builder AI Dependency Object (dKeywords)
	######### AI Builder Begin #########
	return pFireAll  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate14(pShip, pFireAll, fCloseRange, sInitialTarget):
	########## AI Builder End ##########
	#########################################
	# Creating ConditionalAI CloseRange at (404, 328)
	## Conditions:
	#### Condition InRange
	pInRange = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", fCloseRange, sInitialTarget, pShip.GetName())
	## Evaluation function:
	def EvalFunc(bInRange):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bInRange:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pCloseRange = App.ConditionalAI_Create(pShip, "CloseRange")
	pCloseRange.SetInterruptable(1)
	pCloseRange.SetContainedAI(pFireAll)
	pCloseRange.AddCondition(pInRange)
	pCloseRange.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI CloseRange
	#########################################
	# Builder AI Dependency Object (fCloseRange)
	# Builder AI Dependency Object (sInitialTarget)
	######### AI Builder Begin #########
	return pCloseRange  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate15(pShip, sInitialTarget):
	########## AI Builder End ##########
	#########################################
	# Creating PlainAI InterceptTarget at (528, 408)
	pInterceptTarget = App.PlainAI_Create(pShip, "InterceptTarget")
	pInterceptTarget.SetScriptModule("Intercept")
	pInterceptTarget.SetInterruptable(1)
	pScript = pInterceptTarget.GetScriptInstance()
	pScript.SetTargetObjectName(sInitialTarget)
	# Done creating PlainAI InterceptTarget
	#########################################
	# Builder AI Dependency Object (sInitialTarget)
	######### AI Builder Begin #########
	return pInterceptTarget  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate16(pShip, pConditionPlayerStronger, pCloseRange, pInterceptTarget):
	########## AI Builder End ##########
	#########################################
	# Creating PriorityListAI PriorityList at (278, 408)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (379, 415)
	pPriorityList.AddAI(pConditionPlayerStronger, 1)
	pPriorityList.AddAI(pCloseRange, 2)
	pPriorityList.AddAI(pInterceptTarget, 3)
	# Done creating PriorityListAI PriorityList
	#########################################
	######### AI Builder Begin #########
	return pPriorityList  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate17(pShip, pPriorityList, pAllTargetsGroup, sInitialTarget):
	########## AI Builder End ##########
	#########################################
	# Creating PreprocessingAI SelectTarget at (237, 459)
	## Setup:
	import AI.Preprocessors
	pSelectionPreprocess = AI.Preprocessors.SelectTarget(pAllTargetsGroup)
	pSelectionPreprocess.ForceCurrentTargetString(sInitialTarget)
	## The PreprocessingAI:
	pSelectTarget = App.PreprocessingAI_Create(pShip, "SelectTarget")
	pSelectTarget.SetInterruptable(1)
	pSelectTarget.SetPreprocessingMethod(pSelectionPreprocess, "Update")
	pSelectTarget.SetContainedAI(pPriorityList)
	# Done creating PreprocessingAI SelectTarget
	#########################################
	# Builder AI Dependency Object (pAllTargetsGroup)
	# Builder AI Dependency Object (sInitialTarget)
	######### AI Builder Begin #########
	return pSelectTarget  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate18(pShip, pSelectTarget, sInitialTarget, dKeywords):
	########## AI Builder End ##########
	#########################################
	# Creating CompoundAI FollowTargetThroughWarp at (363, 583)
	import AI.Compound.FollowThroughWarp
	pFollowTargetThroughWarp = AI.Compound.FollowThroughWarp.CreateAI(pShip, sInitialTarget, Keywords = dKeywords)
	# Done creating CompoundAI FollowTargetThroughWarp
	#########################################
	# Builder AI Dependency Object (sInitialTarget)
	# Builder AI Dependency Object (dKeywords)
	# Builder AI Dependency AI (SelectTarget)
	pSelectTarget.GetPreprocessingInstance().AddSetTargetTree( pFollowTargetThroughWarp )
	######### AI Builder Begin #########
	return pFollowTargetThroughWarp  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate19(pShip, pFollowTargetThroughWarp, dKeywords):
	########## AI Builder End ##########
	#########################################
	# Creating ConditionalAI FollowThroughWarpFlag at (253, 603)
	## Conditions:
	#### Condition FlagSet
	pFlagSet = App.ConditionScript_Create("Conditions.ConditionFlagSet", "ConditionFlagSet", "FollowTargetThroughWarp", dKeywords)
	## Evaluation function:
	def EvalFunc(bFlagSet):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bFlagSet:
			return ACTIVE
		return DONE
	## The ConditionalAI:
	pFollowThroughWarpFlag = App.ConditionalAI_Create(pShip, "FollowThroughWarpFlag")
	pFollowThroughWarpFlag.SetInterruptable(1)
	pFollowThroughWarpFlag.SetContainedAI(pFollowTargetThroughWarp)
	pFollowThroughWarpFlag.AddCondition(pFlagSet)
	pFollowThroughWarpFlag.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI FollowThroughWarpFlag
	#########################################
	# Builder AI Dependency Object (dKeywords)
	######### AI Builder Begin #########
	return pFollowThroughWarpFlag  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate20(pShip, pCheckWarpBeforeDeath, pNoSensorsEvasive, pSelectTarget, pFollowThroughWarpFlag):
	########## AI Builder End ##########
	#########################################
	# Creating PriorityListAI FleeAttackOrFollow at (115, 536)
	pFleeAttackOrFollow = App.PriorityListAI_Create(pShip, "FleeAttackOrFollow")
	pFleeAttackOrFollow.SetInterruptable(1)
	# SeqBlock is at (196, 512)
	pFleeAttackOrFollow.AddAI(pCheckWarpBeforeDeath, 1)
	pFleeAttackOrFollow.AddAI(pNoSensorsEvasive, 2)
	pFleeAttackOrFollow.AddAI(pSelectTarget, 3)
	pFleeAttackOrFollow.AddAI(pFollowThroughWarpFlag, 4)
	# Done creating PriorityListAI FleeAttackOrFollow
	#########################################
	######### AI Builder Begin #########
	return pFleeAttackOrFollow  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate21(pShip, pFleeAttackOrFollow, dKeywords):
	########## AI Builder End ##########
	#########################################
	# Creating PreprocessingAI PowerManagement at (74, 582)
	## Setup:
	import AI.Preprocessors
	pPowerManager = AI.Preprocessors.ManagePower(0)
	## The PreprocessingAI:
	pPowerManagement = App.PreprocessingAI_Create(pShip, "PowerManagement")
	pPowerManagement.SetInterruptable(1)
	pPowerManagement.SetPreprocessingMethod(pPowerManager, "Update")
	pPowerManagement.SetContainedAI(pFleeAttackOrFollow)
	# Done creating PreprocessingAI PowerManagement
	#########################################
	# Builder AI Dependency Object (dKeywords)
	######### AI Builder Begin #########
	return pPowerManagement  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate22(pShip, pPowerManagement):
	########## AI Builder End ##########
	#########################################
	# Creating PreprocessingAI AlertLevel at (33, 634)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AlertLevel(App.ShipClass.RED_ALERT)
	## The PreprocessingAI:
	pAlertLevel = App.PreprocessingAI_Create(pShip, "AlertLevel")
	pAlertLevel.SetInterruptable(1)
	pAlertLevel.SetPreprocessingMethod(pScript, "Update")
	pAlertLevel.SetContainedAI(pPowerManagement)
	# Done creating PreprocessingAI AlertLevel
	#########################################
	return pAlertLevel
	######### AI Builder Begin #########
	return pAlertLevel  # Builder Return
	########## AI Builder End ##########

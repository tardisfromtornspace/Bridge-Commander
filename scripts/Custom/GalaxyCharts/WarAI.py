from bcdebug import debug
import App

try:
	from bcdebug import debug
except:
	def debug(s):
		pass

def CreateWarAI(pShip):
	debug(__name__ + ", CreateWarAI")
	sLeadShipName = ""
	sShipName = pShip.GetName()
	#########################################
	# Creating CompoundAI LeadAttack at (695, 31)
	pLeadAttack = GetCompoundAttackAIforShip(pShip)
	# Done creating CompoundAI LeadAttack
	#########################################
	#########################################
	# Creating PreprocessingAI PreLeadAttackLog at (550, 496)
	## Setup:
	pPre_LeadAttack = FleetLogging("lead is Initiating attack procedures.", "lead is Cancelling attack procedure.")  #sGotMsg, sLostMsg
	## The PreprocessingAI:
	pPreLeadAttackLog = App.PreprocessingAI_Create(pShip, "PreLeadAttackLog")
	pPreLeadAttackLog.SetInterruptable(1)
	pPreLeadAttackLog.SetPreprocessingMethod(pPre_LeadAttack, "Update")
	pPreLeadAttackLog.SetContainedAI(pLeadAttack)
	# Done creating PreprocessingAI PreLeadAttackLog
	#########################################
	#########################################
	# Creating PlainAI ChaseEnemies at (779, 116)
	pChaseEnemies = App.PlainAI_Create(pShip, "ChaseEnemies")
	pChaseEnemies.SetScriptModule("FleetChaseEnemies")
	pChaseEnemies.SetInterruptable(1)
	# Done creating PlainAI ChaseEnemies
	#########################################
	#####
	#>>># Condition BattleIsStillOn (the next one): 
	#>>># might need another condition to check if fleet is IDLE, so that the fleet only moves to chase if they are IDLE...
	#####
	#########################################
	# Creating ConditionalAI BattleIsStillOn at (697, 116)
	## Conditions:
	#### Condition IsBattleStillOn
	pIsBattleStillOn = App.ConditionScript_Create(__name__, "ConditionCheckBattleStillOn", sShipName)
	## Evaluation function:
	def EvalFunc(bIsBattleStillOn):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bIsBattleStillOn:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pBattleIsStillOn = App.ConditionalAI_Create(pShip, "BattleIsStillOn")
	pBattleIsStillOn.SetInterruptable(1)
	pBattleIsStillOn.SetContainedAI(pChaseEnemies)
	pBattleIsStillOn.AddCondition(pIsBattleStillOn)
	pBattleIsStillOn.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI BattleIsStillOn
	#########################################
	#########################################
	# Creating PlainAI DoLeadDock at (965, 219)
	pDoLeadDock = App.PlainAI_Create(pShip, "DoLeadDock")
	pDoLeadDock.SetScriptModule("IntelligentShipDocking")
	pDoLeadDock.SetInterruptable(0)
	# Done creating PlainAI DoLeadDock
	#########################################
	#########################################
	# Creating PlainAI GoToNearestDockSet at (982, 288)
	pGoToNearestDockSet = App.PlainAI_Create(pShip, "GoToNearestDockSet")
	pGoToNearestDockSet.SetScriptModule("FleetGoToNearestDockableBase")
	pGoToNearestDockSet.SetInterruptable(1)
	# Done creating PlainAI GoToNearestDockSet
	#########################################
	#########################################
	# Creating ConditionalAI NeedFleetDocking at (693, 213)
	## Conditions:
	#### Condition CheckIfShipFleetNeedsDock
	pCheckIfShipFleetNeedsDock = App.ConditionScript_Create(__name__, "ConditionCheckFleetDocking", sShipName)
	#### Condition CanDockInSet
	pCanDockInSet = App.ConditionScript_Create(__name__, "ConditionCheckCanDockInSet", sShipName)
	## Evaluation function:
	def EvalFunc(bCheckIfShipFleetNeedsDock, bCanDockInSet):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bCheckIfShipFleetNeedsDock and not bCanDockInSet:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pNeedFleetDocking = App.ConditionalAI_Create(pShip, "NeedFleetDocking")
	pNeedFleetDocking.SetInterruptable(1)
	pNeedFleetDocking.SetContainedAI(pGoToNearestDockSet)
	pNeedFleetDocking.AddCondition(pCheckIfShipFleetNeedsDock)
	pNeedFleetDocking.AddCondition(pCanDockInSet)
	pNeedFleetDocking.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI NeedFleetDocking
	#########################################
	#########################################
	# Creating PlainAI Turn at (996, 389)
	pTurn = App.PlainAI_Create(pShip, "Turn")
	pTurn.SetScriptModule("ManeuverLoop")
	pTurn.SetInterruptable(1)
	pScript = pTurn.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelLeft())
	# Done creating PlainAI Turn
	#########################################
	#########################################
	# Creating PlainAI Turn_2 at (1013, 436)
	pTurn_2 = App.PlainAI_Create(pShip, "Turn_2")
	pTurn_2.SetScriptModule("ManeuverLoop")
	pTurn_2.SetInterruptable(1)
	pScript = pTurn_2.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelRight())
	# Done creating PlainAI Turn_2
	#########################################
	#########################################
	# Creating PlainAI Turn_3 at (1016, 473)
	pTurn_3 = App.PlainAI_Create(pShip, "Turn_3")
	pTurn_3.SetScriptModule("ManeuverLoop")
	pTurn_3.SetInterruptable(1)
	pScript = pTurn_3.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelUp())
	# Done creating PlainAI Turn_3
	#########################################
	#########################################
	# Creating PlainAI Turn_4 at (1014, 512)
	pTurn_4 = App.PlainAI_Create(pShip, "Turn_4")
	pTurn_4.SetScriptModule("ManeuverLoop")
	pTurn_4.SetInterruptable(1)
	pScript = pTurn_4.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelDown())
	# Done creating PlainAI Turn_4
	#########################################
	#########################################
	# Creating RandomAI FlyPointlessly at (896, 363)
	pFlyPointlessly = App.RandomAI_Create(pShip, "FlyPointlessly")
	pFlyPointlessly.SetInterruptable(1)
	# SeqBlock is at (942, 544)
	pFlyPointlessly.AddAI(pTurn)
	pFlyPointlessly.AddAI(pTurn_2)
	pFlyPointlessly.AddAI(pTurn_3)
	pFlyPointlessly.AddAI(pTurn_4)
	# Done creating RandomAI FlyPointlessly
	#########################################
	#########################################
	# Creating PreprocessingAI UpdateFleetShipStatus_2 at (813, 364)
	## Setup:
	pPreprocess = UpdateShipStatusInFleet()
	## The PreprocessingAI:
	pUpdateFleetShipStatus_2 = App.PreprocessingAI_Create(pShip, "UpdateFleetShipStatus_2")
	pUpdateFleetShipStatus_2.SetInterruptable(1)
	pUpdateFleetShipStatus_2.SetPreprocessingMethod(pPreprocess, "Update")
	pUpdateFleetShipStatus_2.SetContainedAI(pFlyPointlessly)
	# Done creating PreprocessingAI UpdateFleetShipStatus_2
	#########################################
	#########################################
	# Creating SequenceAI FlySequence at (693, 361)
	pFlySequence = App.SequenceAI_Create(pShip, "FlySequence")
	pFlySequence.SetInterruptable(1)
	pFlySequence.SetLoopCount(-1)
	pFlySequence.SetResetIfInterrupted(1)
	pFlySequence.SetDoubleCheckAllDone(1)
	pFlySequence.SetSkipDormant(0)
	# SeqBlock is at (783, 366)
	pFlySequence.AddAI(pUpdateFleetShipStatus_2)
	# Done creating SequenceAI FlySequence
	#########################################
	#########################################
	# Creating PriorityListAI LeadShipOrders at (558, 76)
	pLeadShipOrders = App.PriorityListAI_Create(pShip, "LeadShipOrders")
	pLeadShipOrders.SetInterruptable(1)
	# SeqBlock is at (627, 278)
	pLeadShipOrders.AddAI(pPreLeadAttackLog, 1)
	pLeadShipOrders.AddAI(pBattleIsStillOn, 2)
	pLeadShipOrders.AddAI(pDoLeadDock, 3)
	pLeadShipOrders.AddAI(pNeedFleetDocking, 4)
	pLeadShipOrders.AddAI(pFlySequence, 5)
	# Done creating PriorityListAI LeadShipOrders
	#########################################
	#########################################
	# Creating ConditionalAI CheckInAlliedHostile at (473, 76)
	## Conditions:
	#### Condition IsInAlliedSystem
	pIsInAlliedSystem = App.ConditionScript_Create(__name__, "ConditionCheckSystemAllegiance", sShipName,  "Friendly")
	#### Condition IsInHostileSystem
	pIsInHostileSystem = App.ConditionScript_Create(__name__, "ConditionCheckSystemAllegiance", sShipName, "Enemy")
	## Evaluation function:
	def EvalFunc(bIsInAlliedSystem, bIsInHostileSystem):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bIsInAlliedSystem or bIsInHostileSystem:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pCheckInAlliedHostile = App.ConditionalAI_Create(pShip, "CheckInAlliedHostile")
	pCheckInAlliedHostile.SetInterruptable(1)
	pCheckInAlliedHostile.SetContainedAI(pLeadShipOrders)
	pCheckInAlliedHostile.AddCondition(pIsInAlliedSystem)
	pCheckInAlliedHostile.AddCondition(pIsInHostileSystem)
	pCheckInAlliedHostile.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI CheckInAlliedHostile
	#########################################
	#########################################
	# Creating PlainAI GoToClosestAlliedSystem at (473, 305)
	pGoToClosestAlliedSystem = App.PlainAI_Create(pShip, "GoToClosestAlliedSystem")
	pGoToClosestAlliedSystem.SetScriptModule("FleetGoToClosestAlliedSystem")
	pGoToClosestAlliedSystem.SetInterruptable(1)
	# Done creating PlainAI GoToClosestAlliedSystem
	#########################################
	#########################################
	# Creating ConditionalAI CheckInNeutral at (392, 305)
	## Conditions:
	#### Condition IsInNeutralSystem
	pIsInNeutralSystem = App.ConditionScript_Create(__name__, "ConditionCheckSystemAllegiance", sShipName,  "Neutral")
	## Evaluation function:
	def EvalFunc(bIsInNeutralSystem):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bIsInNeutralSystem:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pCheckInNeutral = App.ConditionalAI_Create(pShip, "CheckInNeutral")
	pCheckInNeutral.SetInterruptable(1)
	pCheckInNeutral.SetContainedAI(pGoToClosestAlliedSystem)
	pCheckInNeutral.AddCondition(pIsInNeutralSystem)
	pCheckInNeutral.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI CheckInNeutral
	#########################################
	#########################################
	# Creating PriorityListAI LeadShipList at (325, 128)
	pLeadShipList = App.PriorityListAI_Create(pShip, "LeadShipList")
	pLeadShipList.SetInterruptable(1)
	# SeqBlock is at (440, 142)
	pLeadShipList.AddAI(pCheckInAlliedHostile, 1)
	pLeadShipList.AddAI(pCheckInNeutral, 2)
	# Done creating PriorityListAI LeadShipList
	#########################################
	#########################################
	# Creating ConditionalAI CheckIsLeadShip at (244, 130)
	## Conditions:
	#### Condition CheckIsFleetLead
	pCheckIsFleetLead = App.ConditionScript_Create(__name__, "ConditionIsShipLeadShip", sShipName)
	## Evaluation function:
	def EvalFunc(bCheckIsFleetLead):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bCheckIsFleetLead:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pCheckIsLeadShip = App.ConditionalAI_Create(pShip, "CheckIsLeadShip")
	pCheckIsLeadShip.SetInterruptable(1)
	pCheckIsLeadShip.SetContainedAI(pLeadShipList)
	pCheckIsLeadShip.AddCondition(pCheckIsFleetLead)
	pCheckIsLeadShip.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI CheckIsLeadShip
	#########################################
	#########################################
	# Creating CompoundAI NormalAttack at (626, 496)
	pNormalAttack = GetCompoundAttackAIforShip(pShip)
	# Done creating CompoundAI NormalAttack
	#########################################
	#########################################
	# Creating PreprocessingAI ConcentrateFire at (544, 496)
	## Setup:
	pSelectionPreprocess = FleetConcentrateFire()
	## The PreprocessingAI:
	pConcentrateFire = App.PreprocessingAI_Create(pShip, "ConcentrateFire")
	pConcentrateFire.SetInterruptable(1)
	pConcentrateFire.SetPreprocessingMethod(pSelectionPreprocess, "Update")
	pConcentrateFire.SetContainedAI(pNormalAttack)
	# Done creating PreprocessingAI ConcentrateFire
	#########################################
	#########################################
	# Creating PlainAI DoShipDock at (632, 559)
	pDoShipDock = App.PlainAI_Create(pShip, "DoShipDock")
	pDoShipDock.SetScriptModule("IntelligentShipDocking")
	pDoShipDock.SetInterruptable(0)
	# Done creating PlainAI DoShipDock
	#########################################
	#########################################
	# Creating PlainAI StickCloseToLead at (631, 624)
	pStickCloseToLead = App.PlainAI_Create(pShip, "StickCloseToLead")
	pStickCloseToLead.SetScriptModule("CircleFleetLeadShip")
	pStickCloseToLead.SetInterruptable(1)
	pScript = pStickCloseToLead.GetScriptInstance()
	pScript.SetFollowObjectName(sLeadShipName)
	pScript.SetCircleSpeed(fSpeed = 0.9)
	pScript.SetRoughDistances(fNearDistance = ConvertKMtoGU(20.0), fFarDistance = ConvertKMtoGU(65.0) )
	# Done creating PlainAI StickCloseToLead
	#########################################
	#########################################
	# Creating PreprocessingAI UpdateFleetShipStatus at (550, 624)
	## Setup:
	pPreprocess = UpdateShipStatusInFleet()
	## The PreprocessingAI:
	pUpdateFleetShipStatus = App.PreprocessingAI_Create(pShip, "UpdateFleetShipStatus")
	pUpdateFleetShipStatus.SetInterruptable(1)
	pUpdateFleetShipStatus.SetPreprocessingMethod(pPreprocess, "Update")
	pUpdateFleetShipStatus.SetContainedAI(pStickCloseToLead)
	# Done creating PreprocessingAI UpdateFleetShipStatus
	#########################################
	#########################################
	# Creating PriorityListAI NormalShipOrders at (407, 478)
	pNormalShipOrders = App.PriorityListAI_Create(pShip, "NormalShipOrders")
	pNormalShipOrders.SetInterruptable(1)
	# SeqBlock is at (493, 594)
	pNormalShipOrders.AddAI(pConcentrateFire, 1)
	pNormalShipOrders.AddAI(pDoShipDock, 2)
	pNormalShipOrders.AddAI(pUpdateFleetShipStatus, 3)
	# Done creating PriorityListAI NormalShipOrders
	#########################################
	#########################################
	# Creating ConditionalAI IsCloseToLead at (325, 478)
	## Conditions:
	#### Condition CheckLeadRange
	pCheckLeadRange = App.ConditionScript_Create(__name__, "ConditionCheckDistanceToLead", ConvertKMtoGU(70.0), sShipName)
	#### Condition CheckShipDocking
	pCheckShipDocking = App.ConditionScript_Create(__name__, "ConditionIsShipTryingToDock", sShipName)
	## Evaluation function:
	def EvalFunc(bCheckLeadRange, bCheckShipDocking):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bCheckLeadRange or bCheckShipDocking:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pIsCloseToLead = App.ConditionalAI_Create(pShip, "IsCloseToLead")
	pIsCloseToLead.SetInterruptable(1)
	pIsCloseToLead.SetContainedAI(pNormalShipOrders)
	pIsCloseToLead.AddCondition(pCheckLeadRange)
	pIsCloseToLead.AddCondition(pCheckShipDocking)
	pIsCloseToLead.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI IsCloseToLead
	#########################################
	#########################################
	# Creating PlainAI InterceptLead at (287, 608)
	pInterceptLead = App.PlainAI_Create(pShip, "InterceptLead")
	pInterceptLead.SetScriptModule("InterceptFleetLeadShip")
	pInterceptLead.SetInterruptable(1)
	pScript = pInterceptLead.GetScriptInstance()
	pScript.SetTargetObjectName(sLeadShipName)
	# Done creating PlainAI InterceptLead
	#########################################
	#########################################
	# Creating PriorityListAI NormalShipList_2 at (213, 528)
	pNormalShipList_2 = App.PriorityListAI_Create(pShip, "NormalShipList_2")
	pNormalShipList_2.SetInterruptable(1)
	# SeqBlock is at (295, 536)
	pNormalShipList_2.AddAI(pIsCloseToLead, 1)
	pNormalShipList_2.AddAI(pInterceptLead, 2)
	# Done creating PriorityListAI NormalShipList_2
	#########################################
	#########################################
	# Creating ConditionalAI IsInSameSetThanLead at (131, 528)
	## Conditions:
	#### Condition IISSTL
	pIISSTL = App.ConditionScript_Create(__name__, "ConditionIsInSameSetThanLead", sShipName)
	## Evaluation function:
	def EvalFunc(bIISSTL):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bIISSTL:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pIsInSameSetThanLead = App.ConditionalAI_Create(pShip, "IsInSameSetThanLead")
	pIsInSameSetThanLead.SetInterruptable(1)
	pIsInSameSetThanLead.SetContainedAI(pNormalShipList_2)
	pIsInSameSetThanLead.AddCondition(pIISSTL)
	pIsInSameSetThanLead.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI IsInSameSetThanLead
	#########################################
	#########################################
	# Creating PlainAI FollowLeadShip at (117, 664)
	pFollowLeadShip = App.PlainAI_Create(pShip, "FollowLeadShip")
	pFollowLeadShip.SetScriptModule("FollowFleetLeadShip")
	pFollowLeadShip.SetInterruptable(1)
	# Done creating PlainAI FollowLeadShip
	#########################################
	#########################################
	# Creating PriorityListAI NormalShipList at (40, 564)
	pNormalShipList = App.PriorityListAI_Create(pShip, "NormalShipList")
	pNormalShipList.SetInterruptable(1)
	# SeqBlock is at (122, 573)
	pNormalShipList.AddAI(pIsInSameSetThanLead, 1)
	pNormalShipList.AddAI(pFollowLeadShip, 2)
	# Done creating PriorityListAI NormalShipList
	#########################################
	#########################################
	# Creating PriorityListAI MainList at (29, 276)
	pMainList = App.PriorityListAI_Create(pShip, "MainList")
	pMainList.SetInterruptable(1)
	# SeqBlock is at (118, 283)
	pMainList.AddAI(pCheckIsLeadShip, 1)
	pMainList.AddAI(pNormalShipList, 2)
	# Done creating PriorityListAI MainList
	#########################################
	#########################################
	# Creating PreprocessingAI WarAIAvoidObstacles at (28, 192)
	## Setup:
	import AI.Preprocessors
	pScript = WarAvoidObstacles() #AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "WarAIAvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pMainList)
	# Done creating PreprocessingAI WarAIAvoidObstacles
	#########################################
	#########################################
	# Creating ConditionalAI WarAIStartTimer at (29, 127)
	## Conditions:
	#### Condition TimerCond
	pTimerCond = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 3, 0)
	## Evaluation function:
	def EvalFunc(bTimerCond):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimerCond:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pStartTimer = App.ConditionalAI_Create(pShip, "WarAIStartTimer")
	pStartTimer.SetInterruptable(1)
	pStartTimer.SetContainedAI(pAvoidObstacles)
	pStartTimer.AddCondition(pTimerCond)
	pStartTimer.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI WarAIStartTimer
	#########################################
	return pStartTimer

################################################################################
################################################################################
##													##
##   Dynamic Attack AI functions                             			##
##  these are used to dynamically acquire a compound attack AI for a ship.    ##
##  this way ships using the WarAI will still have their "natural" attack AIs ##
##  such as CloakAttack, BorgAttack, FedAttack, RamAttack, etc etc etc...  =) ##
##													##
################################################################################
################################################################################

def GetCompoundAttackAIforShip(pShip):
	debug(__name__ + ", GetCompoundAttackAIforShip")
	pShipDef = GetShipDef(pShip)
	if pShipDef == None:
		return
	pFriendlies = MissionLib.GetFriendlyGroup()
	pEnemies = MissionLib.GetEnemyGroup()
	pNeutrals = MissionLib.GetNeutralGroup()
		
	if pEnemies.IsNameInGroup(pShip.GetName()):
		pAIenemyGroup = pFriendlies
		sAI = pShipDef.StrEnemyAI()
		sAItoCheckTo = "QuickBattleAI"
		sStarbaseAItoCheckTo = "StarbaseAI"
	elif pFriendlies.IsNameInGroup(pShip.GetName()):
		pAIenemyGroup = pEnemies
		sAI = pShipDef.StrFriendlyAI()
		sAItoCheckTo = "QuickBattleFriendlyAI"
		sStarbaseAItoCheckTo = "StarbaseFriendlyAI"
	else:
		#neutral ships, or ships without a group defined.
		#WARNING: this might not work very nicely.... =/
		pAIenemyGroup = None
		sAI = ""
		sAItoCheckTo = ""

	if sAI == sAItoCheckTo:
		pAttackAI = CreateBasicAttackAI(pShip, pAIenemyGroup)
	elif sAI == sStarbaseAItoCheckTo:
		pAIenemyGroup.AddName(pShip.GetName())
		pAttackAI = CreateStarbaseAttackAI(pShip, pAIenemyGroup)
		pAIenemyGroup.RemoveName(pShip.GetName())
	else:
		try:
			pAIModule = __import__("QuickBattle." + sAI)
			try:
				pAttackAI = pAIModule.CreateAI(pShip, pAIenemyGroup)
			except:
				pAttackAI = pAIModule.CreateAI(pShip)
		except:
			pAttackAI = CreateBasicAttackAI(pShip, pAIenemyGroup)
	return pAttackAI

def CreateBasicAttackAI(pShip, pShipEnemiesGroup):
	#########################################
	# Creating CompoundAI Attack at (108, 133)
	debug(__name__ + ", CreateBasicAttackAI")
	import AI.Compound.BasicAttack
	if pShipEnemiesGroup != None:
		pAttack = AI.Compound.BasicAttack.CreateAI(pShip, pShipEnemiesGroup, Easy_Difficulty = 1.0, Easy_MaxFiringRange = 456.0, Easy_AvoidTorps = 1, Easy_AggressivePulseWeapons = 1, Easy_ChooseSubsystemTargets = 1, Easy_HighPower = 1, Easy_NeverSitStill = 1, Easy_PowerManagement = 1, Easy_SmartPhasers = 1, Easy_SmartShields = 1, Easy_SmartTorpSelection = 1, Easy_SmartWeaponBalance = 1, Easy_UseCloaking = 1, Easy_UseRearTorps = 1, Easy_UseSideArcs = 1, Difficulty = 1.0, MaxFiringRange = 503.0, AvoidTorps = 1, AggressivePulseWeapons = 1, ChooseSubsystemTargets = 1, HighPower = 1, NeverSitStill = 1, PowerManagement = 1, SmartPhasers = 1, SmartShields = 1, SmartTorpSelection = 1, SmartWeaponBalance = 1, UseCloaking = 1, UseRearTorps = 1, UseSideArcs = 1, Hard_Difficulty = 1.0, Hard_MaxFiringRange = 525.0, Hard_AvoidTorps = 1, Hard_AggressivePulseWeapons = 1, Hard_ChooseSubsystemTargets = 1, Hard_HighPower = 1, Hard_NeverSitStill = 1, Hard_PowerManagement = 1, Hard_SmartPhasers = 1, Hard_SmartShields = 1, Hard_SmartTorpSelection = 1, Hard_SmartWeaponBalance = 1, Hard_UseCloaking = 1, Hard_UseRearTorps = 1, Hard_UseSideArcs = 1)
	else:
		pAttack = AI.Compound.BasicAttack.CreateAI(pShip, Easy_Difficulty = 1.0, Easy_MaxFiringRange = 456.0, Easy_AvoidTorps = 1, Easy_AggressivePulseWeapons = 1, Easy_ChooseSubsystemTargets = 1, Easy_HighPower = 1, Easy_NeverSitStill = 1, Easy_PowerManagement = 1, Easy_SmartPhasers = 1, Easy_SmartShields = 1, Easy_SmartTorpSelection = 1, Easy_SmartWeaponBalance = 1, Easy_UseCloaking = 1, Easy_UseRearTorps = 1, Easy_UseSideArcs = 1, Difficulty = 1.0, MaxFiringRange = 503.0, AvoidTorps = 1, AggressivePulseWeapons = 1, ChooseSubsystemTargets = 1, HighPower = 1, NeverSitStill = 1, PowerManagement = 1, SmartPhasers = 1, SmartShields = 1, SmartTorpSelection = 1, SmartWeaponBalance = 1, UseCloaking = 1, UseRearTorps = 1, UseSideArcs = 1, Hard_Difficulty = 1.0, Hard_MaxFiringRange = 525.0, Hard_AvoidTorps = 1, Hard_AggressivePulseWeapons = 1, Hard_ChooseSubsystemTargets = 1, Hard_HighPower = 1, Hard_NeverSitStill = 1, Hard_PowerManagement = 1, Hard_SmartPhasers = 1, Hard_SmartShields = 1, Hard_SmartTorpSelection = 1, Hard_SmartWeaponBalance = 1, Hard_UseCloaking = 1, Hard_UseRearTorps = 1, Hard_UseSideArcs = 1)
	# Done creating CompoundAI Attack
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (29, 332)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 1, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pAttack)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	return pWait

def CreateStarbaseAttackAI(pShip, pShipEnemiesGroup):
	#if not pShipEnemiesGroup.GetNameTuple():
	#	pShipEnemiesGroup.AddName("This ship probably wont exist")
	#########################################
	# Creating CompoundAI StarbaseAttack at (194, 57)
	debug(__name__ + ", CreateStarbaseAttackAI")
	import AI.Compound.StarbaseAttack
	pStarbaseAttack = AI.Compound.StarbaseAttack.CreateAI(pShip, pShipEnemiesGroup)
	# Done creating CompoundAI StarbaseAttack
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (83, 155)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 1, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pStarbaseAttack)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	return pWait

################################################################################
################################################################################
##													##
##   Custom AI Blocks (Preprocessors, PlainAIs, Conditions, etc)			##
##													##
################################################################################
################################################################################
from Custom.GalaxyCharts.GalacticWarSimulator import *

###
###  CONDITIONS
###

class ConditionCheckSystemAllegiance:
	def __init__(self, pCodeCondition, sShipName, sAllegiance):
		debug(__name__ + ", __init__")
		self.pCodeCondition = pCodeCondition
		# Set our primary object's name..
		self.sShipName = sShipName
		self.sAllegiance = sAllegiance

		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		self.pModule = __import__(__name__)

		# Setup our interrupt handlers, for checking of the object
		# enters the set.
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)

		App.g_kEventManager.AddBroadcastPythonMethodHandler(ET_REGION_CONQUERED, self.pEventHandler, "RegionConquered")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_ENTERED_SET, self.pEventHandler, "EnteredSet")
		self.SetState()

	def __getstate__(self):
		debug(__name__ + ", __getstate__")
		dState = self.__dict__.copy()
		dState["pModule"] = self.pModule.__name__
		dState["pEventHandler"].pContainingInstance = self
		return dState
	def __setstate__(self, dict):
		debug(__name__ + ", __setstate__")
		self.__dict__ = dict
		self.pModule = __import__(self.pModule)
		del self.pEventHandler.pContainingInstance

	def SetState(self, pShip = None):
		debug(__name__ + ", SetState")
		if pShip == None and self.sShipName != "":
			pShip = App.ShipClass_Cast(App.ObjectClass_GetObject( None, self.sShipName ))
		bStatus = 0
		if pShip != None:
			pTravel = App.g_kTravelManager.GetTravel(pShip)
			if pTravel != None and pTravel.IsTravelling() == 1:
				bStatus = self.pCodeCondition.GetStatus()
			else:
				pSet = pShip.GetContainingSet()
				if pSet != None:
					pRegion = pSet.GetRegion()
					if pRegion != None:
						sShipRace = GetShipRaceByWarSim(pShip)
						sEmpire = pRegion.GetControllingEmpire()
						pRaceObj = GetRaceClassObj(sEmpire)
						if (sShipRace == sEmpire or AreRacesAllied(sShipRace, sEmpire) == 1) and pRaceObj != None:
							if self.sAllegiance == "Friendly":
								bStatus = 1
						elif AreRacesEnemies(sShipRace, sEmpire) == 1 and pRaceObj != None:
							if self.sAllegiance == "Enemy":
								bStatus = 1
						elif self.sAllegiance == "Neutral":
							bStatus = 1
		#print "Setting ConditionCheckSystemAllegiance (", self.sShipName, self.sAllegiance, ") to:", bStatus
		self.pCodeCondition.SetStatus(bStatus)
	def EnteredSet(self, pObjEvent):
		debug(__name__ + ", EnteredSet")
		pShip = App.ShipClass_Cast(pObjEvent.GetDestination())
		if pShip and pShip.GetName() == self.sShipName:
			# update state
			self.SetState(pShip)
		# Call the next handler for this event...
		self.pEventHandler.CallNextHandler(pObjEvent)
	def RegionConquered(self, pObjEvent):
		# update state
		debug(__name__ + ", RegionConquered")
		self.SetState()
		# Call the next handler for this event...
		self.pEventHandler.CallNextHandler(pObjEvent)

####################################################################################################################################################
class ConditionIsShipLeadShip:
	def __init__(self, pCodeCondition, sShipName):
		debug(__name__ + ", __init__")
		self.pCodeCondition = pCodeCondition
		# Set our primary object's name..
		self.sShipName = sShipName

		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		self.pModule = __import__(__name__)

		# Setup our interrupt handlers, for checking of the object
		# enters the set.
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)

		App.g_kEventManager.AddBroadcastPythonMethodHandler(ET_FLEET_UPDATED_LEAD, self.pEventHandler, "FleetUpdatedLeadShip")
		self.SetState()

	def __getstate__(self):
		debug(__name__ + ", __getstate__")
		dState = self.__dict__.copy()
		dState["pModule"] = self.pModule.__name__
		dState["pEventHandler"].pContainingInstance = self
		return dState
	def __setstate__(self, dict):
		debug(__name__ + ", __setstate__")
		self.__dict__ = dict
		self.pModule = __import__(self.pModule)
		del self.pEventHandler.pContainingInstance

	def SetState(self):
		debug(__name__ + ", SetState")
		pShip = None
		if self.sShipName != "":
			pShip = App.ShipClass_Cast(App.ObjectClass_GetObject( None, self.sShipName ))
		bStatus = 0
		if pShip != None:
			pFleet = FleetManager.GetFleetOfShip(pShip)
			if pFleet != None:
				if pFleet.GetLeadShipName() == pShip.GetName():
					bStatus = 1
		self.pCodeCondition.SetStatus(bStatus)
	def FleetUpdatedLeadShip(self, pObjEvent):
		debug(__name__ + ", FleetUpdatedLeadShip")
		sFleetName = pObjEvent.GetCString()
		pFleet = FleetManager.GetFleetByName(sFleetName)
		if pFleet != None:
			if pFleet.IsShipNameInFleet(self.sShipName) == 1:
				bStatus = 0
				if pFleet.GetLeadShipName() == self.sShipName:
					bStatus = 1
				#print "FleetUpdatedLeadShip: condition of", self.sShipName, " AI. Status:", bStatus
				self.pCodeCondition.SetStatus(bStatus)

		# Call the next handler for this event...
		self.pEventHandler.CallNextHandler(pObjEvent)

######################################################################################################################################################
import Conditions.ConditionInRange
class ConditionCheckDistanceToLead(Conditions.ConditionInRange.ConditionInRange):
	def __init__(self, pCodeCondition, fDistance, sShipName):
		debug(__name__ + ", __init__")
		pFleet = FleetManager.GetFleetOfShipName(sShipName)
		if pFleet != None:
			sLeadShipName = pFleet.GetLeadShipName()
		Conditions.ConditionInRange.ConditionInRange.__init__(self, pCodeCondition, fDistance, sLeadShipName, sShipName)
		App.g_kEventManager.AddBroadcastPythonMethodHandler(ET_FLEET_UPDATED_LEAD, self.pEventHandler, "FleetUpdatedLeadShip")
		self.sShipName = sShipName
	def SetTarget(self, sTarget):
		# Change self.sObject1.
		debug(__name__ + ", SetTarget")
		return
	def FleetUpdatedLeadShip(self, pObjEvent):
		debug(__name__ + ", FleetUpdatedLeadShip")
		sFleetName = pObjEvent.GetCString()
		pFleet = FleetManager.GetFleetByName(sFleetName)
		if pFleet != None:
			if pFleet.IsShipNameInFleet(self.sShipName) == 1:
				# our lead ship has changed, update accordingly.
				sLeadShip = pFleet.GetLeadShipName()
				if self.sObject1 != sLeadShip:
					#apply(self.SetObjects, (sLeadShip, self.pObjects))
					self.pSingleObjectGroup.RemoveName(self.sObject1)
					self.sObject1 = sLeadShip
					self.pSingleObjectGroup.AddName(self.sObject1)
					# Setup the proximity sphere.
					self.SetupProximitySphere()

		self.pEventHandler.CallNextHandler(pObjEvent)

#######################################################################################################################################################
class ConditionIsInSameSetThanLead:
	def __init__(self, pCodeCondition, sShipName):
		debug(__name__ + ", __init__")
		self.pCodeCondition = pCodeCondition
		# Set our primary object's name..
		self.sShipName = sShipName
		self.sLeadShipName = ""

		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		self.pModule = __import__(__name__)

		# Setup our interrupt handlers, for checking of the object
		# enters the set.
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)

		App.g_kEventManager.AddBroadcastPythonMethodHandler(ET_FLEET_UPDATED_LEAD, self.pEventHandler, "FleetUpdatedLeadShip")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_ENTERED_SET, self.pEventHandler, "ShipsChangedSet")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_EXITED_SET, self.pEventHandler, "ShipsChangedSet")
		self.DoSetCheck()

	def __getstate__(self):
		debug(__name__ + ", __getstate__")
		dState = self.__dict__.copy()
		dState["pModule"] = self.pModule.__name__
		dState["pEventHandler"].pContainingInstance = self
		return dState
	def __setstate__(self, dict):
		debug(__name__ + ", __setstate__")
		self.__dict__ = dict
		self.pModule = __import__(self.pModule)
		del self.pEventHandler.pContainingInstance

	def DoSetCheck(self):
		debug(__name__ + ", DoSetCheck")
		pShip = None
		pLeadShip = None
		bStatus = 0
		if self.sShipName != "":
			pShip = App.ShipClass_Cast(App.ObjectClass_GetObject( None, self.sShipName ))
		if pShip != None:
			pFleet = FleetManager.GetFleetOfShip(pShip)
			if pFleet != None:
				if pFleet.GetLeadShipName() != "":
					pLeadShip = App.ShipClass_Cast(App.ObjectClass_GetObject( None, pFleet.GetLeadShipName() ))
					self.sLeadShipName = pFleet.GetLeadShipName()
		if pShip != None and pLeadShip != None:
			pSet = pShip.GetContainingSet()
			pLeadSet = pLeadShip.GetContainingSet()
			if pSet != None and pLeadSet != None:
				if pSet.GetObjID() == pLeadSet.GetObjID():
					bStatus = 1
		self.pCodeCondition.SetStatus(bStatus)

	def FleetUpdatedLeadShip(self, pObjEvent):
		debug(__name__ + ", FleetUpdatedLeadShip")
		sFleetName = pObjEvent.GetCString()
		pFleet = FleetManager.GetFleetByName(sFleetName)
		if pFleet != None:
			if pFleet.IsShipNameInFleet(self.sShipName) == 1:
				# our lead ship has changed, update accordingly.
				self.DoSetCheck()
		self.pEventHandler.CallNextHandler(pObjEvent)

	def ShipsChangedSet(self, pObjEvent):
		debug(__name__ + ", ShipsChangedSet")
		pShip = App.ShipClass_Cast(pObjEvent.GetDestination())
		if pShip != None:
			# update state
			self.DoSetCheck()
		# Call the next handler for this event...
		self.pEventHandler.CallNextHandler(pObjEvent)

#######################################################################################################################################################
class ConditionCheckBattleStillOn:
	def __init__(self, pCodeCondition, sShipName):
		debug(__name__ + ", __init__")
		self.pCodeCondition = pCodeCondition
		# Set our primary object's name..
		self.sShipName = sShipName

		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		self.pModule = __import__(__name__)

		# Setup our interrupt handlers, for checking of the object
		# enters the set.
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)

		# yes, its rather strange but we need all these event handlers to listen if a battle has started or ended.
		# why? because besides starting and ending normally, a ship can also enter on a battle that has already started or leave a battle that
		# is still going...
		App.g_kEventManager.AddBroadcastPythonMethodHandler(ET_BATTLE_STARTED, self.pEventHandler, "BattleStatusChanged")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(ET_BATTLE_ATTACK_VICTORY, self.pEventHandler, "BattleStatusChanged")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(ET_BATTLE_DEFENCE_VICTORY, self.pEventHandler, "BattleStatusChanged")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_ENTERED_SET, self.pEventHandler, "ShipsChangedSet")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_EXITED_SET, self.pEventHandler, "ShipsChangedSet")
		self.DoSetCheck()

	def __getstate__(self):
		debug(__name__ + ", __getstate__")
		dState = self.__dict__.copy()
		dState["pModule"] = self.pModule.__name__
		dState["pEventHandler"].pContainingInstance = self
		return dState
	def __setstate__(self, dict):
		debug(__name__ + ", __setstate__")
		self.__dict__ = dict
		self.pModule = __import__(self.pModule)
		del self.pEventHandler.pContainingInstance

	def DoSetCheck(self):
		debug(__name__ + ", DoSetCheck")
		pShip = None
		bStatus = 0
		if self.sShipName != "":
			pShip = App.ShipClass_Cast(App.ObjectClass_GetObject( None, self.sShipName ))
		if pShip != None:
			pSet = pShip.GetContainingSet()
			if pSet != None:
				pRegion = pSet.GetRegion()
				if pRegion != None:
					bStatus = pRegion.RegionBattle.IsBattleOn()
		self.pCodeCondition.SetStatus(bStatus)

	def BattleStatusChanged(self, pObjEvent):
		# its easier for now to just do the check again, instead of checking if the battle status change was were our
		debug(__name__ + ", BattleStatusChanged")
		self.DoSetCheck()
		# Call the next handler for this event...
		self.pEventHandler.CallNextHandler(pObjEvent)

	def ShipsChangedSet(self, pObjEvent):
		debug(__name__ + ", ShipsChangedSet")
		pShip = App.ShipClass_Cast(pObjEvent.GetDestination())
		if pShip != None:
			if pShip.GetName() == self.sShipName:
				# update state
				self.DoSetCheck()
		# Call the next handler for this event...
		self.pEventHandler.CallNextHandler(pObjEvent)

#######################################################################################################################################################
class ConditionCheckCanDockInSet:
	def __init__(self, pCodeCondition, sShipName):
		debug(__name__ + ", __init__")
		self.pCodeCondition = pCodeCondition
		# Set our primary object's name..
		self.sShipName = sShipName

		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		self.pModule = __import__(__name__)

		# Setup our interrupt handlers, for checking of the object
		# enters the set.
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)

		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_ENTERED_SET, self.pEventHandler, "ShipsChangedSet")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_EXITED_SET, self.pEventHandler, "ShipsChangedSet")
		self.DoSetCheck()

	def __getstate__(self):
		debug(__name__ + ", __getstate__")
		dState = self.__dict__.copy()
		dState["pModule"] = self.pModule.__name__
		dState["pEventHandler"].pContainingInstance = self
		return dState
	def __setstate__(self, dict):
		debug(__name__ + ", __setstate__")
		self.__dict__ = dict
		self.pModule = __import__(self.pModule)
		del self.pEventHandler.pContainingInstance

	def DoSetCheck(self):
		debug(__name__ + ", DoSetCheck")
		pShip = None
		pSet = None
		bStatus = 0
		if self.sShipName != "":
			pShip = App.ShipClass_Cast(App.ObjectClass_GetObject( None, self.sShipName ))
		if pShip != None:
			pSet = pShip.GetContainingSet()
		if pSet != None:
			pRegion = pSet.GetRegion()
			if pRegion != None and pRegion.RegionBattle.IsBattleOn() == 0:
				sShipRace = GetShipRaceByWarSim(pShip)
				if sShipRace == pRegion.GetControllingEmpire() or AreRacesAllied(sShipRace, pRegion.GetControllingEmpire()) == 1:
					lDocks = GetDockableBasesOfSet(pSet)
					if len(lDocks) >= 1:
						bStatus = 1
		self.pCodeCondition.SetStatus(bStatus)

	def ShipsChangedSet(self, pObjEvent):
		debug(__name__ + ", ShipsChangedSet")
		pShip = App.ShipClass_Cast(pObjEvent.GetDestination())
		if pShip != None:
			if pShip.GetName() == self.sShipName or IsStation(pShip) == 1:
				# update state
				self.DoSetCheck()
		# Call the next handler for this event...
		self.pEventHandler.CallNextHandler(pObjEvent)

#######################################################################################################################################################
class ConditionIsShipInNeedOfRepairResupply:
	ET_SUBSYS_CONDITION_CHANGED = App.UtopiaModule_GetNextEventType()

	lDisableSystems = (
		# (attribute name,    system type,     condition percentage,   is critical)
		("pPowerDamaged", 	App.CT_POWER_SUBSYSTEM, 		0.6, 1),
		("pSensorDamaged", 	App.CT_SENSOR_SUBSYSTEM,		0.8, 0),
		("pHullDamaged", 		App.CT_HULL_SUBSYSTEM, 			0.7, 1),
		("pShieldDamaged", 	App.CT_SHIELD_SUBSYSTEM,		0.6, 0),
		("pRepairDamaged", 	App.CT_REPAIR_SUBSYSTEM,		0.4, 0),
		("pImpulseDamaged",	App.CT_IMPULSE_ENGINE_SUBSYSTEM,	0.6, 0),
		("pWarpDamaged",		App.CT_WARP_ENGINE_SUBSYSTEM, 	0.6, 0),
		("pWeaponsDamaged",	App.CT_WEAPON_SYSTEM,			0.8, 0),
		("Resupply", 		None, 					0.0, 0),
		("Recrew",  		None, 					0.0, 0)
		)

	def __init__(self, pCodeCondition, sShipName):
		# Set our parameters...
		debug(__name__ + ", __init__")
		self.pCodeCondition = pCodeCondition
		self.sShipName= sShipName
		self.bStats = {}
		self.bNeedsRecrew = 0

		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		self.pModule = __import__(__name__)

		# Setup our event handler wrapper.
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)

		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_TORPEDO_FIRED, self.pEventHandler, "TorpedoFired")
		try:
			from Custom.DS9FX import DS9FXVersionSignature
			from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig
			if DS9FXVersionSignature.DS9FXVersion == "Xtended" and DS9FXSavedConfig.LifeSupport == 1:
				from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents
				eCEA = DS9FXGlobalEvents.ET_COMBAT_EFFECTIVENESS_ADJUSTED
				App.g_kEventManager.AddBroadcastPythonMethodHandler(eCEA, self.pEventHandler, "CombatEffectivenessChanged")

				if self.sShipName != "":
					pShip = App.ShipClass_Cast(App.ObjectClass_GetObject( None, self.sShipName ))
					if pShip != None:
						from Custom.DS9FX.DS9FXLib import DS9FXLifeSupportLib
						iCrewPerc = DS9FXLifeSupportLib.GetCrewPercentage(pShip, pShip.GetObjID() )
						# iCrewPerc can be 
						#  = "N/A" ->  ship has no crew
						#  > 100 -> crew overload.   < 25 -> less than 25% of crew, oh noes...
						if iCrewPerc != "N/A":
							if iCrewPerc < 40:
								# I think less than 40% of crew is a good number to assume the ship needs recrewing...
								self.bNeedsRecrew = 1
		except:
			Galaxy.Logger.LogString("WarAI ISINORR: couldn't add Xtended COMBAT_EFFECTIVENESS event handler...")

		# Our condition handler.
		self.pConditionHandler = App.ConditionEventCreator()
		pEvent = App.TGEvent_Create()
		pEvent.SetEventType(self.ET_SUBSYS_CONDITION_CHANGED)
		pEvent.SetDestination(self.pEventHandler)
		self.pConditionHandler.SetEvent(pEvent)

		# Add conditions for the various subsystems we're watching.
		for sAttr, eSystemType, fSystemFraction, bIsCritical in self.lDisableSystems:
			self.bStats[sAttr] = 0
			if sAttr != "Resupply" and sAttr != "Recrew":
				# Create this condition...
				pCondition = App.ConditionScript_Create("Conditions.ConditionSystemBelow", "ConditionSystemBelow", self.sShipName, eSystemType, fSystemFraction)

				# Store a reference to it..
				setattr(self, sAttr, pCondition)

				# Add it to the condition handler.
				self.pConditionHandler.AddCondition( pCondition )

		# Set our initial state..
		self.CheckState()

		# Set an event handler listening for when our conditions change.
		self.pEventHandler.AddPythonMethodHandlerForInstance(self.ET_SUBSYS_CONDITION_CHANGED, "CheckState")

	def __getstate__(self):
		debug(__name__ + ", __getstate__")
		dState = self.__dict__.copy()
		dState["pModule"] = self.pModule.__name__
		dState["pEventHandler"].pContainingInstance = self
		return dState

	def __setstate__(self, dict):
		debug(__name__ + ", __setstate__")
		self.__dict__ = dict
		self.pModule = __import__(self.pModule)
		del self.pEventHandler.pContainingInstance

	def CheckState(self, pEvent = None):
		debug(__name__ + ", CheckState")
		bStatus = 0
		iNumOfOnes = 0
		pShip = None
		if self.sShipName != "":
			pShip = App.ShipClass_Cast(App.ObjectClass_GetObject( None, self.sShipName ))
		for sAttr, eSystemType, fSystemFraction, bIsCritical in self.lDisableSystems:
			if sAttr == "Resupply":
				#check if ships needs to resupply ammo
				self.bStats[sAttr] = 0
				if pShip != None:
					pTorpSys = pShip.GetTorpedoSystem()
					if pTorpSys != None:
						for i in range(pTorpSys.GetNumAmmoTypes()):
							pAmmoType = pTorpSys.GetAmmoType(i)
							iTorpsAvailable = pTorpSys.GetNumAvailableTorpsToType(i)
							fMaxTorps = float(pAmmoType.GetMaxTorpedoes())
							if fMaxTorps != 0.0:
								if (iTorpsAvailable / fMaxTorps) <= 0.5:
									self.bStats[sAttr] = 1
									break
			elif sAttr == "Recrew":
				self.bStats[sAttr] = self.bNeedsRecrew
			else:
				self.bStats[sAttr] = getattr(self, sAttr).GetStatus()
		for sAttr, eSystemType, fSystemFraction, bIsCritical in self.lDisableSystems:
			bStat = self.bStats[sAttr]
			if bIsCritical == 1 and bStat == 1:
				bStatus = 1
				break
			elif bStat == 1:
				iNumOfOnes = iNumOfOnes + 1
			if iNumOfOnes >= 2:
				bStatus = 1
				break
		#print "ISINORR:", self.sShipName, bStatus
		if bStatus != self.pCodeCondition.GetStatus():
			self.pCodeCondition.SetStatus(bStatus)
			if pShip == None:
				pShip = App.ShipClass_Cast(App.ObjectClass_GetObject( None, self.sShipName ))
			if pShip != None:
				pEvent = App.TGIntEvent_Create()
				pEvent.SetEventType(ET_SHIP_NEEDS_REPAIR_AND_RESUPPLY)
				pEvent.SetDestination(pShip)
				pEvent.SetInt(bStatus)
				App.g_kEventManager.AddEvent(pEvent)

	def TorpedoFired(self, pObjEvent):
		debug(__name__ + ", TorpedoFired")
		pTorp = App.Torpedo_Cast(pObjEvent.GetSource())
		if pTorp == None or self.sShipName == "":
			return
		pShip = App.ShipClass_Cast(App.ObjectClass_GetObject( None, self.sShipName ))
		if pShip == None:
			return
		if pShip.GetObjID() == pTorp.GetParentID():
			# update state
			self.CheckState()
		# Call the next handler for this event...
		self.pEventHandler.CallNextHandler(pObjEvent)

	def CombatEffectivenessChanged(self, pObjEvent):
		debug(__name__ + ", CombatEffectivenessChanged")
		try:
			pCheckShip = App.Torpedo_Cast(pObjEvent.GetDestination())
			if pCheckShip == None or self.sShipName == "":
				return
			pShip = App.ShipClass_Cast(App.ObjectClass_GetObject( None, self.sShipName ))
			if pShip == None:
				return
			if pShip.GetObjID() == pCheckShip.GetObjID():
				# get the crew percentage of the ship
				from Custom.DS9FX.DS9FXLib import DS9FXLifeSupportLib
				iCrewPerc = DS9FXLifeSupportLib.GetCrewPercentage(pShip, pShip.GetObjID() )
				# iCrewPerc can be 
				#  = "N/A" ->  ship has no crew
				#  > 100 -> crew overload.   < 25 -> less than 25% of crew, oh noes...
				if iCrewPerc != "N/A":
					bCrewStat = 0
					if iCrewPerc < 40:
						# I think less than 40% of crew is a good number to assume the ship needs recrewing...
						bCrewStat = 1
					# if our condition changed, already update state
					if self.bNeedsRecrew != bCrewStat:
						self.bNeedsRecrew = bCrewStat
						self.CheckState()
		except:
			Galaxy.Logger.LogString("WarAI ISINORR - Combat Effectiveness Changed handler failed...")
		# Call the next handler for this event...
		self.pEventHandler.CallNextHandler(pObjEvent)

#######################################################################################################################################################
class ConditionIsShipTryingToDock:
	def __init__(self, pCodeCondition, sShipName):
		debug(__name__ + ", __init__")
		self.pCodeCondition = pCodeCondition
		# Set our primary object's name..
		self.sShipName = sShipName

		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		self.pModule = __import__(__name__)

		# Setup our interrupt handlers, for checking of the object
		# enters the set.
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)

		App.g_kEventManager.AddBroadcastPythonMethodHandler(ET_SHIP_STARTED_DOCKING, self.pEventHandler, "ShipDocked")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(ET_SHIP_FINISHED_DOCKING, self.pEventHandler, "ShipDocked")
		self.CheckState()

	def __getstate__(self):
		debug(__name__ + ", __getstate__")
		dState = self.__dict__.copy()
		dState["pModule"] = self.pModule.__name__
		dState["pEventHandler"].pContainingInstance = self
		return dState
	def __setstate__(self, dict):
		debug(__name__ + ", __setstate__")
		self.__dict__ = dict
		self.pModule = __import__(self.pModule)
		del self.pEventHandler.pContainingInstance

	def CheckState(self):
		debug(__name__ + ", CheckState")
		pShip = None
		pSet = None
		bStatus = 0
		if self.sShipName != "":
			pShip = App.ShipClass_Cast(App.ObjectClass_GetObject( None, self.sShipName ))
		if pShip != None:
			pWSShip = WarSimulator.GetWSShipObjForShip(pShip)
			if pWSShip != None:
				bStatus = pWSShip.IsShipDocking()
		self.pCodeCondition.SetStatus(bStatus)

	def ShipDocked(self, pObjEvent):
		debug(__name__ + ", ShipDocked")
		pShip = App.ShipClass_Cast(pObjEvent.GetDestination())
		if pShip != None:
			if pShip.GetName() == self.sShipName:
				# update state
				self.CheckState()
		# Call the next handler for this event...
		self.pEventHandler.CallNextHandler(pObjEvent)

#######################################################################################################################################################
class ConditionCheckFleetDocking:
	def __init__(self, pCodeCondition, sShipName):
		debug(__name__ + ", __init__")
		self.pCodeCondition = pCodeCondition
		# Set our primary object's name..
		self.sShipName = sShipName

		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		self.pModule = __import__(__name__)

		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)
		App.g_kEventManager.AddBroadcastPythonMethodHandler(ET_SHIP_NEEDS_REPAIR_AND_RESUPPLY, self.pEventHandler, "CheckState")

		self.CheckState()

	def __getstate__(self):
		debug(__name__ + ", __getstate__")
		dState = self.__dict__.copy()
		dState["pModule"] = self.pModule.__name__
		dState["pEventHandler"].pContainingInstance = self
		return dState
	def __setstate__(self, dict):
		debug(__name__ + ", __setstate__")
		self.__dict__ = dict
		self.pModule = __import__(self.pModule)
		del self.pEventHandler.pContainingInstance

	def CheckState(self, pEvent = None):
		debug(__name__ + ", CheckState")
		bStatus = 0
		pFleet = None

		if self.sShipName != "":
			pOurShip = App.ShipClass_Cast(App.ObjectClass_GetObject( None, self.sShipName ))
			if pOurShip != None:
				pFleet = FleetManager.GetFleetOfShip(pOurShip)

		if pEvent != None and pFleet != None:
			pShip = App.ShipClass_Cast(pEvent.GetDestination())
			if pShip != None:
				if pFleet.IsShipNameInFleet(pShip.GetName()):
					if pEvent.GetInt() >= 1:
						bStatus = 1
					else:
						lShipNames = pFleet.GetShipNameList()
						lShipNames.remove(pShip.GetName())
						for sName in lShipNames:
							pWSShip = WarSimulator.GetWSShipObjForName(sName)
							if pWSShip.IsShipInNeedOfRepairAndResupply() == 1:
								bStatus = 1	
								break
		elif pFleet != None:
			bStatus = pFleet.IsFleetInNeedOfRepairAndResupply()		

		self.pCodeCondition.SetStatus(bStatus)

	def ShipsChangedSet(self, pObjEvent):
		debug(__name__ + ", ShipsChangedSet")
		pShip = App.ShipClass_Cast(pObjEvent.GetDestination())
		if pShip != None:
			if pShip.GetName() == self.sShipName:
				# update state
				self.CheckState()
		# Call the next handler for this event...
		self.pEventHandler.CallNextHandler(pObjEvent)

#######################################################################################################################################################

###
###  PREPROCESSORS
###
# these are the first preprocess I make... so lets hope they work lol =P
import AI.Preprocessors

class FleetConcentrateFire:
	def __init__(self):
		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		debug(__name__ + ", __init__")
		self.pModule = __import__(__name__)
		self.bUpdatingTargetInfo = 0
		self.sCurrentTarget = ""

	def __getstate__(self):
		debug(__name__ + ", __getstate__")
		dState = self.__dict__.copy()
		dState["pModule"] = self.pModule.__name__
		return dState

	def __setstate__(self, dict):
		debug(__name__ + ", __setstate__")
		self.__dict__ = dict
		self.pModule = __import__(self.pModule)

	def GetNextUpdateTime(self):
		# a fast update is probably better here... i'm not sure how the AI will behave >_<
		debug(__name__ + ", GetNextUpdateTime")
		return 0.1

	def Update(self, dEndTime):
		debug(__name__ + ", Update")
		pOurShip = self.pCodeAI.GetShip()
		if pOurShip == None:
			return App.PreprocessingAI.PS_DONE
		bCallExternalFunctions = 0
		if WarSimulator.IsInitialized() == 1:
			pFleet = FleetManager.GetFleetOfShip(pOurShip)
			if pFleet != None:
				pLeadShip = pFleet.GetLeadShipObj()
				if pLeadShip != None and pLeadShip.GetObjID() != pOurShip.GetObjID():
					pMasterTarget = App.ShipClass_Cast(pLeadShip.GetTarget())
					if pMasterTarget != None:
						sTargetName = pMasterTarget.GetName()
						sOurRace = GetShipRaceByWarSim(pOurShip)
						sTargetRace = GetShipRaceByWarSim(pMasterTarget)
						sCurrentTarget = ""
						if pOurShip.GetTarget() != None:
							sCurrentTarget = pOurShip.GetTarget().GetName()
							#if sCurrentTarget == pOurShip.GetName():
							#	sCurrentTarget = ""
						if sTargetName != sCurrentTarget and AreRacesEnemies(sOurRace, sTargetRace) == 1 and sTargetName != "":
							#print "Forcing Fleet Ship", pOurShip.GetName(), " target as lead ship target ", sTargetName
							pOurShip.SetTarget(sTargetName)
							self.sCurrentTarget = sTargetName
							bCallExternalFunctions = 1
		if bCallExternalFunctions == 1 or self.bUpdatingTargetInfo == 1:
			self.CallSetTargetFunctions(dEndTime)
		pSet = pOurShip.GetContainingSet()
		if self.IsThereEnemiesInSet(pOurShip, pSet) == 1:
			return App.PreprocessingAI.PS_NORMAL
		else:
			return App.PreprocessingAI.PS_SKIP_ACTIVE

	def CallSetTargetFunctions(self, dEndTime):
		# We'll call the externally registered SetTarget functions
		# on all AI's beneath us in the AI tree.
		debug(__name__ + ", CallSetTargetFunctions")
		lAIs = self.pCodeAI.GetAllAIsInTree()[1:]

		# Set flags so we know we're in the middle of updating.
		if not self.bUpdatingTargetInfo:
			self.bUpdatingTargetInfo = 1
			#print "Started Updating Target Info for ship", self.pCodeAI.GetShip().GetName()
			self.pCodeAI.ForceDormantStatus(App.PreprocessingAI.FDS_FALSE)
			#self.fUpdateTime = self.fUpdatingTargetInfoUpdateTime

			self.lAIUpdateIDs = []
			for pAI in lAIs:
				self.lAIUpdateIDs.append( pAI.GetID() )

		#updating remaining AI SetTarget functions.
		iOriginalLength = len(self.lAIUpdateIDs)
		while len(self.lAIUpdateIDs):
			idAI = self.lAIUpdateIDs[0]
			self.lAIUpdateIDs.remove(idAI)

			pAI = App.ArtificialIntelligence_GetAIByID(idAI)
			if pAI:
				pAI.CallExternalFunction("SetTarget", self.sCurrentTarget)

			# Check if we should stop.
			if App.g_kSystemWrapper.GetTimeSinceFrameStart() > dEndTime:
				break

		if len(self.lAIUpdateIDs) == 0:
			# Done updating the tree beneath us.
			del self.lAIUpdateIDs
			self.bUpdatingTargetInfo = 0
			#print "Finished Updating Target Info for ship", self.pCodeAI.GetShip().GetName()
			self.pCodeAI.ForceDormantStatus(App.PreprocessingAI.FDS_NORMAL)

	def IsThereEnemiesInSet(self, pShip, pSet):
		debug(__name__ + ", IsThereEnemiesInSet")
		pGame = App.Game_GetCurrentGame()
		pEpisode = pGame.GetCurrentEpisode()
		pMission = pEpisode.GetCurrentMission()
		pEnemies = pMission.GetEnemyGroup()
		pFriendlies = pMission.GetFriendlyGroup()
		if pFriendlies.IsNameInGroup(pShip.GetName()):
			pEnemyGroup = pFriendlies
		elif pEnemies.IsNameInGroup(pShip.GetName()):
			pEnemyGroup = pEnemies
		else:
			pEnemyGroup = None
		if pEnemyGroup != None:
			ObjTuple = pEnemyGroup.GetActiveObjectTupleInSet(pSet)
			if len(ObjTuple):
				for i in ObjTuple:
					pObj = App.ShipClass_Cast(i)
					if pObj:			
						return 1
		return 0

	def GotFocus(self):
		debug(__name__ + ", GotFocus")
		pShip = self.pCodeAI.GetShip()
		if pShip != None:
			pFleet = FleetManager.GetFleetOfShip(pShip)
			if pFleet != None:
				pFleet.Logger.LogString("WarAI_"+pShip.GetName()+": is attacking, concentrating fire.")

	def LostFocus(self):
		debug(__name__ + ", LostFocus")
		pShip = self.pCodeAI.GetShip()
		if pShip != None:
			pFleet = FleetManager.GetFleetOfShip(pShip)
			if pFleet != None:
				pFleet.Logger.LogString("WarAI_"+pShip.GetName()+": has stopped concentrating fire.")



#######################################################################################################################################################
# this preprocess is used to update the ship status in her fleet
# if it is active (has focus), it should set the ship as IDLE, or else (lost focus), as ACTIVE... 
class UpdateShipStatusInFleet:
	def __init__(self):
		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		debug(__name__ + ", __init__")
		self.pModule = __import__(__name__)

	def __getstate__(self):
		debug(__name__ + ", __getstate__")
		dState = self.__dict__.copy()
		dState["pModule"] = self.pModule.__name__
		return dState

	def __setstate__(self, dict):
		debug(__name__ + ", __setstate__")
		self.__dict__ = dict
		self.pModule = __import__(self.pModule)

	def GetNextUpdateTime(self):
		# We don't really need to be updated.  Our update
		# doesn't really do anything.
		debug(__name__ + ", GetNextUpdateTime")
		return 60

	def Update(self, dEndTime):
		debug(__name__ + ", Update")
		return App.PreprocessingAI.PS_NORMAL

	def GotFocus(self):
		debug(__name__ + ", GotFocus")
		pOurShip = self.pCodeAI.GetShip()
		if pOurShip != None:
			pFleet = FleetManager.GetFleetOfShip(pOurShip)
			if pFleet != None:
				pFleet.ChangeShipStatusTo(pOurShip, pFleet.IDLE)

	def LostFocus(self):
		debug(__name__ + ", LostFocus")
		pOurShip = self.pCodeAI.GetShip()
		if pOurShip != None:
			pFleet = FleetManager.GetFleetOfShip(pOurShip)
			if pFleet != None:
				pFleet.ChangeShipStatusTo(pOurShip, pFleet.ACTIVE)

#######################################################################################################################################################
# our "own" AvoidObstacles preprocess.
# it is the same than the AvoidObstacles preprocess, except for one thing: it will not work while the ship is trying to dock, otherwise the
# AvoidObstacles will fu** up the docking process.
class WarAvoidObstacles(AI.Preprocessors.AvoidObstacles):
	def __init__(self):
		# just initialize our base class. No need for anything else.
		debug(__name__ + ", __init__")
		AI.Preprocessors.AvoidObstacles.__init__(self)

	def Update(self, dEndTime):
		debug(__name__ + ", Update")
		pShip = self.pCodeAI.GetShip()
		#print "WAO mark start"
		if pShip != None:
			pWSShip = WarSimulator.GetWSShipObjForShip(pShip)
			if pWSShip != None:
				if pWSShip.IsShipDocking() == 1:
					#print "WAO returning"
					return App.PreprocessingAI.PS_NORMAL
		return AI.Preprocessors.AvoidObstacles.Update(self, dEndTime)


#######################################################################################################################################################
# this is a DEBUGGING preprocess. It is used to log a string when the AI gains or loses focus, on the fleet logger.
class FleetLogging:
	def __init__(self, sGotMsg, sLostMsg):
		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		debug(__name__ + ", __init__")
		self.pModule = __import__(__name__)
		self.gotMsg = sGotMsg
		self.lostMsg = sLostMsg

	def __getstate__(self):
		debug(__name__ + ", __getstate__")
		dState = self.__dict__.copy()
		dState["pModule"] = self.pModule.__name__
		return dState

	def __setstate__(self, dict):
		debug(__name__ + ", __setstate__")
		self.__dict__ = dict
		self.pModule = __import__(self.pModule)

	def GetNextUpdateTime(self):
		# We don't really need to be updated.  Our update
		# doesn't really do anything.
		debug(__name__ + ", GetNextUpdateTime")
		return 60

	def Update(self, dEndTime):
		debug(__name__ + ", Update")
		return App.PreprocessingAI.PS_NORMAL

	def GotFocus(self):
		debug(__name__ + ", GotFocus")
		pShip = self.pCodeAI.GetShip()
		if pShip != None:
			pFleet = FleetManager.GetFleetOfShip(pShip)
			if pFleet != None:
				pFleet.Logger.LogString("WarAI_"+pShip.GetName()+": "+self.gotMsg)

	def LostFocus(self):
		debug(__name__ + ", LostFocus")
		pShip = self.pCodeAI.GetShip()
		if pShip != None:
			pFleet = FleetManager.GetFleetOfShip(pShip)
			if pFleet != None:
				pFleet.Logger.LogString("WarAI_"+pShip.GetName()+": "+self.lostMsg)


#######################################################################################################################################################

###
###  PLAIN  AIs
### 
### NOTE: these PlainAIs are located in their own scripts in "BC\scripts\AI\PlainAI" since we need them there so that BC's AI constructor method
###	    can read and build them.
###

import App
import MissionLib
import Quickbattle

def CreateAI(pShip):
        pTargets        = grabOppositeTeamsQB(pShip)
        if not pTargets:
		return None

        if not pTargets.GetNameTuple():
                pTargets.AddName("This ship probably wont exist")
	#########################################
	# Creating CompoundAI Attack at (150, 92)
	import AI.Compound.BorgAttack
	pAttack = AI.Compound.BorgAttack.CreateAI(pShip, pTargets, Difficulty = 1.0, MaxFiringRange = 70.0, FollowTargetThroughWarp = 1, ChooseSubsystemTargets = 1, AggressivePulseWeapons = 0, DisableBeforeDestroy = 0, InaccurateTorps = 1, SmartWeaponBalance = 0, SmartShields = 1, UseSideArcs = 1, HighPower = 1, PowerManagement = 1)
	# Done creating CompoundAI Attack
	#########################################
	#########################################
	# Creating ConditionalAI TargetInRange at (86, 150)
	## Conditions:
	#### Condition InRange
	pInRange = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 1000, pShip.GetName(), MissionLib.GetEnemyGroup())
	## Evaluation function:
	def EvalFunc(bInRange):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if (bInRange):
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pTargetInRange = App.ConditionalAI_Create(pShip, "TargetInRange")
	pTargetInRange.SetInterruptable(1)
	pTargetInRange.SetContainedAI(pAttack)
	pTargetInRange.AddCondition(pInRange)
	pTargetInRange.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI TargetInRange
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (29, 332)
	# 3-second delay before AI starts attacking
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 3, 0)
	## Evaluation function:
	def EvalFuncWait(bTimePassed):
		ACTIVE  = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pTargetInRange)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFuncWait)
	# Done creating ConditionalAI Wait
	#########################################
	#########################################
	# Creating PreprocessingAI ShieldRotate at (126, 420)
	# Detects incoming torpedos via ConditionIncomingTorps and runs EvadeTorps
	# to rotate the strongest shield facing toward the threat automatically.
	import AI.PlainAI.EvadeTorps
	pEvade = App.PlainAI_Create(pShip, "EvadeTorps")
	pEvade.SetScriptModule("EvadeTorps")

	pIncomingTorps = App.ConditionScript_Create("Conditions.ConditionIncomingTorps", "ConditionIncomingTorps", pShip.GetName(), "None", 4.0)

	def EvalFuncEvade(bIncoming):
		ACTIVE  = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		if bIncoming:
			return ACTIVE
		return DORMANT

	pEvadeConditional = App.ConditionalAI_Create(pShip, "EvadeConditional")
	pEvadeConditional.SetInterruptable(1)
	pEvadeConditional.SetContainedAI(pEvade)
	pEvadeConditional.AddCondition(pIncomingTorps)
	pEvadeConditional.SetEvaluationFunction(EvalFuncEvade)
	# Done creating ConditionalAI EvadeConditional
	#########################################

	#########################################
	# Creating PriorityListAI - EvadeTorps takes priority over attack
	pPriority = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriority.SetInterruptable(1)
	pPriority.AddAI(pEvadeConditional, 1)
	pPriority.AddAI(pWait, 2)
	# Done creating PriorityListAI
	#########################################

	return pPriority

def grabOppositeTeamsQB(pShip):
	if not pShip or not hasattr(pShip, "GetObjID"):
		return None

	iShipID = pShip.GetObjID()
	if iShipID == None or iShipID == App.NULL_ID:
		return None
	
	pShip = App.ShipClass_GetObjectByID(None, iShipID)
	if not pShip:
		return None

	pMission        = MissionLib.GetMission()

	pFriendlies     = None
	pEnemies        = None
	pNeutrals       = None
	pNeutrals2      = None
	pTractors       = None
	myGroup = None
	if pMission:
		pcName = pShip.GetName()
		pFriendlies     = pMission.GetFriendlyGroup() 
		pEnemies        = pMission.GetEnemyGroup() 
		pNeutrals       = pMission.GetNeutralGroup()
		pTractors       = pMission.GetTractorGroup()	
		pNeutrals2      = App.ObjectGroup_FromModule("Custom.QuickBattleGame.QuickBattle", "pNeutrals2")
	
		if pFriendlies and pEnemies and pFriendlies.IsNameInGroup(pcName):
			myGroup = pEnemies
		if pEnemies and pFriendlies and pEnemies.IsNameInGroup(pcName):
			myGroup = pFriendlies
		if pNeutrals and pNeutrals2 and pNeutrals.IsNameInGroup(pcName):
			myGroup = pNeutrals2
		if pNeutrals2 and pNeutrals and pNeutrals2.IsNameInGroup(pcName):
			myGroup = pNeutrals
		if pTractors and pTractors.IsNameInGroup(pcName):
			myGroup = pTractors
		if pEnemies and myGroup == None:
			myGroup = pEnemies

	return myGroup
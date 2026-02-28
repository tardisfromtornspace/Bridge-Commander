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
	return pTargetInRange

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
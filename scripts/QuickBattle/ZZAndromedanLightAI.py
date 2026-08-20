# Andromedan Light enemy AI — same QB wrapper as ZZAndromedanAttackAI,
# but NonFedAttack instead of BorgAttack: stays farther out, does not
# chase through warp, evades, and warps out when systems are critical.
import App
import Quickbattle
import MissionLib

# Engage only when hostiles are this close (AndromedanAttack uses 1000).
ENGAGE_RANGE = 380
# Seconds to wait after spawn before fighting.
WAIT_SECONDS = 3

def CreateAI(pShip, *lpTargets):
	pTargets = grabOppositeTeamsQB(pShip)
	if not pTargets:
		return None

	if not pTargets.GetNameTuple():
		pTargets.AddName("This ship probably wont exist")

	import AI.Compound.NonFedAttack
	pAttack = AI.Compound.NonFedAttack.CreateAI(
		pShip, pTargets,
		MaxFiringRange = 280.0,
		FollowTargetThroughWarp = 0,
		FollowToSB12 = 0,
		WarpOutBeforeDying = 1,
		AvoidTorps = 1,
		SmartShields = 1,
		PowerManagement = 1,
		HighPower = 0,
		NeverSitStill = 1,
		UseSideArcs = 1,
		UseRearTorps = 1,
		UseCloaking = 1,
		AggressivePulseWeapons = 1,
		ChooseSubsystemTargets = 1,
		DisableBeforeDestroy = 0,
		InaccurateTorps = 1,
		SmartWeaponBalance = 0,
		SmartPhasers = 0,
		SmartTorpSelection = 0,
	)

	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", WAIT_SECONDS, 0)
	def EvalWait(bTimePassed):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		if bTimePassed:
			return ACTIVE
		return DORMANT
	pWait = App.ConditionalAI_Create(pShip, "WaitToEngage")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pAttack)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalWait)

	pInRange = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", ENGAGE_RANGE, pShip.GetName(), MissionLib.GetFriendlyGroup())
	def EvalRange(bInRange):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if (bInRange):
			return ACTIVE
		return DORMANT
	pTargetInRange = App.ConditionalAI_Create(pShip, "TargetInRange")
	pTargetInRange.SetInterruptable(1)
	pTargetInRange.SetContainedAI(pWait)
	pTargetInRange.AddCondition(pInRange)
	pTargetInRange.SetEvaluationFunction(EvalRange)

	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	pAvoid = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoid.SetInterruptable(1)
	pAvoid.SetPreprocessingMethod(pScript, "Update")
	pAvoid.SetContainedAI(pTargetInRange)
	return pAvoid

def grabOppositeTeamsQB(pShip):
	if not pShip or not hasattr(pShip, "GetObjID"):
		return None

	iShipID = pShip.GetObjID()
	if iShipID == None or iShipID == App.NULL_ID:
		return None

	pShip = App.ShipClass_GetObjectByID(None, iShipID)
	if not pShip:
		return None

	pMission = MissionLib.GetMission()

	pFriendlies = None
	pEnemies = None
	pNeutrals = None
	pNeutrals2 = None
	pTractors = None
	myGroup = None
	if pMission:
		pcName = pShip.GetName()
		pFriendlies = pMission.GetFriendlyGroup()
		pEnemies = pMission.GetEnemyGroup()
		pNeutrals = pMission.GetNeutralGroup()
		pTractors = pMission.GetTractorGroup()
		pNeutrals2 = App.ObjectGroup_FromModule("Custom.QuickBattleGame.QuickBattle", "pNeutrals2")

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
		if pFriendlies and myGroup == None:
			myGroup = pFriendlies

	return myGroup

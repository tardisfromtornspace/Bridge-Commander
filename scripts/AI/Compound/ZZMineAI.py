####
# ZZMineAI.py
# 4th January 2026
# Created originally from defiant's QBautostart Mines' MinesAI (that falls under the GPL license, according to Mines.py Modinfo), adapted by CharaToLoki on ZambieZan's request to allow Mines for SolidProjectiles.
# This file, being a CompoundAI, should be located at scripts.AI.Compound folder on a KMM install.
####

MODINFO = { "Author": "\"defiant, Alex SL Gato, ZambieZan\" mail@defiant.homedns.org, andromedavirgoa@gmail.com, alex400zz (on Discord)",
	    "Version": "0.42",
	    "License": "GPL",
	    "Description": "Read the small title above for more info",
	    "needBridge": 0
	    }

# Don't forget imports
import App

from bcdebug import debug
import traceback

import MissionLib


# Set AI
def CreateAI(pShip, pEnemies=MissionLib.GetEnemyGroup(), initTime=None, fRangeValue=50):
        debug(__name__ + ", CreateAI")
	return CreateAIWrapped(pShip, pEnemies, initTime, fRangeValue)

def CreateAIWrapped(pShip, pEnemies=MissionLib.GetEnemyGroup(), initTime=None, fRangeValue=50):
        debug(__name__ + ", CreateAIWrapped")
        if initTime == 0:
                import AI.Player.Stay
                pAttack = AI.Player.Stay.CreateAI(pShip)
        else:
	        pAttack = CreateAI2Wrapped(pShip, fRangeValue, pEnemies)
		if initTime == None:
			return pAttack
	# Done creating CompoundAI Attack
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (80, 77)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", initTime, 0)
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

def CreateAI2(pShip, *lsTargets):
        debug(__name__ + ", CreateAI2")
	fRangeValue = 50
	return CreateAI2Wrapped(pShip, fRangeValue, *lsTargets)

def CreateAI2Wrapped(pShip, fRangeValue, *lsTargets):
	# Make a group for all the targets...
	pAllTargetsGroup = App.ObjectGroup_ForceToGroup(lsTargets)
	sInitialTarget = None
	if pAllTargetsGroup.GetNameTuple():
		sInitialTarget = pAllTargetsGroup.GetNameTuple()[0]

        debug(__name__ + ", CreateAI2")
	#########################################
	# Creating PlainAI SelfDestruct_2 at (117, 91)
	pSelfDestruct_2 = App.PlainAI_Create(pShip, "SelfDestruct_2")
	pSelfDestruct_2.SetScriptModule("SelfDestruct")
	pSelfDestruct_2.SetInterruptable(1)
	# Done creating PlainAI SelfDestruct_2
	#########################################
	#########################################
	# Creating ConditionalAI SensorsDead at (76, 184)
	## Conditions:
	#### Condition Disabled
	pDisabled = App.ConditionScript_Create("Conditions.ConditionSystemDisabled", "ConditionSystemDisabled", pShip.GetName(), App.CT_SENSOR_SUBSYSTEM, 1)
	## Evaluation function:
	def EvalFunc(bDisabled):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bDisabled:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pSensorsDead = App.ConditionalAI_Create(pShip, "SensorsDead")
	pSensorsDead.SetInterruptable(1)
	pSensorsDead.SetContainedAI(pSelfDestruct_2)
	pSensorsDead.AddCondition(pDisabled)
	pSensorsDead.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI SensorsDead
	#########################################
	#########################################
	# Creating PlainAI SelfDestruct at (286, 61)
	pSelfDestruct = App.PlainAI_Create(pShip, "SelfDestruct")
	pSelfDestruct.SetScriptModule("SelfDestruct")
	pSelfDestruct.SetInterruptable(1)
	# Done creating PlainAI SelfDestruct
	#########################################
	#########################################
	# Creating ConditionalAI ConditionInRange at (245, 127)
	## Conditions:
	#### Condition InRange
	pInRange = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", fRangeValue, sInitialTarget, pShip.GetName())
	## Evaluation function:
	def EvalFunc(bInRange):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bInRange:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pConditionInRange = App.ConditionalAI_Create(pShip, "ConditionInRange")
	pConditionInRange.SetInterruptable(1)
	pConditionInRange.SetContainedAI(pSelfDestruct)
	pConditionInRange.AddCondition(pInRange)
	pConditionInRange.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI ConditionInRange
	#########################################
	#########################################
	# Creating ConditionalAI TargetsInSet at (184, 184)
	## Conditions:
	#### Condition SameSet
	pSameSet = App.ConditionScript_Create("Conditions.ConditionAnyInSameSet", "ConditionAnyInSameSet", pShip.GetName(), lsTargets)
	## Evaluation function:
	def EvalFunc(bSameSet):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bSameSet:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pTargetsInSet = App.ConditionalAI_Create(pShip, "TargetsInSet")
	pTargetsInSet.SetInterruptable(1)
	pTargetsInSet.SetContainedAI(pConditionInRange)
	pTargetsInSet.AddCondition(pSameSet)
	pTargetsInSet.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI TargetsInSet
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (42, 243)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (146, 250)
	pPriorityList.AddAI(pSensorsDead, 1)
	pPriorityList.AddAI(pTargetsInSet, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	return pPriorityList
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 13th December 2024
# The 'Borg AI Final' was one AI jayce (aka Resistance Is Futile) made on 2008 for Borg vessels, bringing a lot of functionality to those vessels.
# However, this AI presents one weird glitch when combined with GalaxyCharts which makes the game crash immediately if a ship travelled two systems while one Borg vessel was chasing them.
# I am not sure if it is "All Rights Reserved", but on the BorgAttack file it explicity says **Do Not Modify The Borg AI Final**, so just in case I will treat it as an All Rights Reserved as well, and in order to fix this conflict, I will make this Autoload file "FIX-BorgAttackAIforGC", made by myself as a derivative work and with the help of the AIEditor Tool, so the original file is unmodified.
# The functions we need to modify are fragments of CreateAI, plus BuilderCreate3 and BuilderCreate4.
#
MODINFO = { "Author": "\"jayce\" (original) and \"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "20241213",
	    "License": "All Rights Reserved to jayce, LGPL from Alex SL Gato changes, SDK for the rest",
	    "Description": "Read the small title above for more info"
	    }
#
#################################################################################################################
#

##########################################################################
## Borg AI Final - 10 July 2008                                         ##
## By: jayce AKA Resistance Is Futile                                   ##
##                                                                      ##
## This will be the final version of the Borg AI. It is also the        ##
## The smartest version of the Borg AI with improvements over the       ##
## Previous versions which includes: a smarter target selection         ##
## Process, the ability to focus group attacks on specific targets,     ##
## The ability to now intercept targets, the ability to now follow a    ##
## Target through warp, the ability to now avoid obstacles, and of      ##
## Course, the ability to attack multiple targets simutaniously while   ##
## Moving, not stationary. Online Friendly.                             ##
##                                                                      ##
## Special thanks once again to Defiant for turning me onto some of     ##
## The workings of the AI Distributes Building feature shown below.     ##
##                                                                      ##
## As always, use at your own risk. You are free to distribute but      ##
## **Do Not Modify The Borg AI Final**                                  ##
##########################################################################

	######### AI Builder Begin #########
## BUILDER AI
##  This AI file has been mauled by the MakeBuilderAI script.
##  Modify at your own risk.
##  Or run MakeBuilderAI(filename, 1) to remove the BuilderAI code.
	########## AI Builder End ##########
import App
from bcdebug import debug

def CreateAI(pShip, *lpTargets, **dKeywords):
	# Make a group for all the targets...
	debug(__name__ + ", CreateAI")
	pAllTargetsGroup = App.ObjectGroup_ForceToGroup(lpTargets)
	sInitialTarget = pAllTargetsGroup.GetNameTuple()[0]
	
	Random = lambda fMin, fMax : App.g_kSystemWrapper.GetRandomNumber((fMax-fMin) * 1000.0) / 1000.0 - fMin

	# Range values used in the AI... I do not think the original version of BorgAttack used them.
	fTooCloseRange = 50.0 + Random(-10, 10)
	fTooFarRange = 100.0 + Random(-15, 10)

	fCloseRange = 150.0 + Random(-5, 15)
	fMidRange = 200.0 + Random(-10, 20)
	fLongRange = 350.0 + Random(-30, 20)

	######### AI Builder Begin #########
	pBuilderAI = App.BuilderAI_Create(pShip, "AlertLevel Builder", __name__)
	pBuilderAI.AddAIBlock("AttackFriends", "BuilderCreate1")
	pBuilderAI.AddDependencyObject("AttackFriends", "pAllTargetsGroup", pAllTargetsGroup)
	pBuilderAI.AddAIBlock("2sec_InAttackPowerReserve", "BuilderCreate2")
	pBuilderAI.AddDependency("2sec_InAttackPowerReserve", "AttackFriends")

	pBuilderAI.AddAIBlock("FollowThroughWarp", "BuilderCreate3")                          #### TAGGED 2
	pBuilderAI.AddDependencyObject("FollowThroughWarp", "sInitialTarget", sInitialTarget) #### TAGGED 2

	pBuilderAI.AddDependencyObject("FollowThroughWarp", "dKeywords", dKeywords)           #### TAGGED 2 EXTRA ADDED TO-DO

	pBuilderAI.AddAIBlock("TargetWarpingAway", "BuilderCreate4")                          #### TAGGED 1
	pBuilderAI.AddDependencyObject("TargetWarpingAway", "sInitialTarget", sInitialTarget) #### TAGGED 1

	pBuilderAI.AddDependencyObject("TargetWarpingAway", "dKeywords", dKeywords)           #### TAGGED 1 EXTRA ADDED TO-DO

	pBuilderAI.AddDependency("TargetWarpingAway", "FollowThroughWarp")                    #### TAGGED 1
	pBuilderAI.AddAIBlock("Intercept", "BuilderCreate5")
	pBuilderAI.AddDependencyObject("Intercept", "sInitialTarget", sInitialTarget)
	pBuilderAI.AddAIBlock("TargetTooFar", "BuilderCreate6")
	pBuilderAI.AddDependencyObject("TargetTooFar", "sInitialTarget", sInitialTarget)
	pBuilderAI.AddDependency("TargetTooFar", "Intercept")
	pBuilderAI.AddAIBlock("MoveIn", "BuilderCreate7")
	pBuilderAI.AddDependencyObject("MoveIn", "sInitialTarget", sInitialTarget)
	pBuilderAI.AddAIBlock("Sequence_2", "BuilderCreate8")
	pBuilderAI.AddDependency("Sequence_2", "TargetWarpingAway")                           #### TAGGED 1
	pBuilderAI.AddDependency("Sequence_2", "TargetTooFar")
	pBuilderAI.AddDependency("Sequence_2", "MoveIn")
	pBuilderAI.AddAIBlock("SelectTarget", "BuilderCreate9")
	pBuilderAI.AddDependency("SelectTarget", "Sequence_2")
	pBuilderAI.AddDependencyObject("SelectTarget", "pAllTargetsGroup", pAllTargetsGroup)
	pBuilderAI.AddDependencyObject("SelectTarget", "sInitialTarget", sInitialTarget)
	pBuilderAI.AddAIBlock("AvoidObstacles", "BuilderCreate10")
	pBuilderAI.AddDependency("AvoidObstacles", "SelectTarget")
	pBuilderAI.AddAIBlock("ComputeNew_BearingIn5sec", "BuilderCreate11")
	pBuilderAI.AddDependency("ComputeNew_BearingIn5sec", "AvoidObstacles")
	pBuilderAI.AddAIBlock("Sequence", "BuilderCreate12")
	pBuilderAI.AddDependency("Sequence", "2sec_InAttackPowerReserve")
	pBuilderAI.AddDependency("Sequence", "ComputeNew_BearingIn5sec")
	pBuilderAI.AddAIBlock("PowerManagement", "BuilderCreate13")
	pBuilderAI.AddDependency("PowerManagement", "Sequence")
	pBuilderAI.AddAIBlock("AlertLevel", "BuilderCreate14")
	pBuilderAI.AddDependency("AlertLevel", "PowerManagement")
	return pBuilderAI # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate1(pShip, pAllTargetsGroup):
	########## AI Builder End ##########
	#########################################
	# Creating PlainAI AttackFriends at (81, 192)
	debug(__name__ + ", BuilderCreate1")
	pAttackFriends = App.PlainAI_Create(pShip, "AttackFriends")
	pAttackFriends.SetScriptModule("StarbaseAttack")
	pAttackFriends.SetInterruptable(1)
	pScript = pAttackFriends.GetScriptInstance()
	pScript.SetTargets(pAllTargetsGroup)
	# Done creating PlainAI AttackFriends
	#########################################
        # Builder AI Dependency Object (pAllTargetsGroup)
	######### AI Builder Begin #########
	return pAttackFriends  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate2(pShip, pAttackFriends):
	########## AI Builder End ##########
	#########################################
	# Creating ConditionalAI 2sec_InAttackPowerReserve at (81, 157)
	## Conditions:
	#### Condition TimePassed
	debug(__name__ + ", BuilderCreate2")
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 3, 1)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if not bTimePassed:
			return ACTIVE
		return DONE
	## The ConditionalAI:
	p2sec_InAttackPowerReserve = App.ConditionalAI_Create(pShip, "2sec_InAttackPowerReserve")
	p2sec_InAttackPowerReserve.SetInterruptable(1)
	p2sec_InAttackPowerReserve.SetContainedAI(pAttackFriends)
	p2sec_InAttackPowerReserve.AddCondition(pTimePassed)
	p2sec_InAttackPowerReserve.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI 2sec_InAttackPowerReserve
	#########################################
	######### AI Builder Begin #########
	return p2sec_InAttackPowerReserve  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate3(pShip, sInitialTarget, dKeywords):
	########## AI Builder End ##########

	#########################################
	# Creating CompoundAI FollowThroughWarp at (313, 399)
	debug(__name__ + ", BuilderCreate3")
	import AI.Compound.FollowThroughWarp
	pFollowThroughWarp = AI.Compound.FollowThroughWarp.CreateAI(pShip, sInitialTarget, Keywords = dKeywords, FollowToSB12 = 1, FollowThroughMissions = 1)
	# Done creating CompoundAI FollowThroughWarp
	#########################################

	# TO-DO BELOW ORIGINAL, ABOVE MODIFIED
#	#########################################
#	# Creating PlainAI FollowThroughWarp at (313, 399)
#	debug(__name__ + ", BuilderCreate3")
#	pFollowThroughWarp = App.PlainAI_Create(pShip, "FollowThroughWarp")
#	pFollowThroughWarp.SetScriptModule("FollowThroughWarp")
#	pFollowThroughWarp.SetInterruptable(1)
#	pScript = pFollowThroughWarp.GetScriptInstance()
#	pScript.SetFollowObjectName(sInitialTarget)
#	# Done creating PlainAI FollowThroughWarp
#	#########################################




	######### AI Builder Begin #########
	return pFollowThroughWarp  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate4(pShip, pFollowThroughWarp, sInitialTarget, dKeywords):
	########## AI Builder End ##########

	#########################################
	# Creating ConditionalAI TargetWarpingAway at (313, 365)
	## Conditions:
	#### Condition FlagSet
	debug(__name__ + ", BuilderCreate4")
	pFlagSet = App.ConditionScript_Create("Conditions.ConditionFlagSet", "ConditionFlagSet", "FollowTargetThroughWarp", dKeywords)
	#### Condition WarpingToSet
	pWarpingToSet = App.ConditionScript_Create("Conditions.ConditionWarpingToSet", "ConditionWarpingToSet", sInitialTarget)
	## Evaluation function:
	def EvalFunc(bFlagSet, bWarpingToSet):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bFlagSet and  bWarpingToSet:
			return ACTIVE
		return DONE
	## The ConditionalAI:
	pTargetWarpingAway = App.ConditionalAI_Create(pShip, "TargetWarpingAway")
	pTargetWarpingAway.SetInterruptable(0)
	pTargetWarpingAway.SetContainedAI(pFollowThroughWarp)
	pTargetWarpingAway.AddCondition(pFlagSet)
	pTargetWarpingAway.AddCondition(pWarpingToSet)
	pTargetWarpingAway.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI TargetWarpingAway
	#########################################

	# TO-DO BELOW ORIGINAL, ABOVE MODIFIED
#	#########################################
#	# Creating ConditionalAI TargetWarpingAway at (313, 365)
#	## Conditions:
#	#### Condition Warp
#	debug(__name__ + ", BuilderCreate4")
#	pWarp = App.ConditionScript_Create("Conditions.ConditionWarpingToSet", "ConditionWarpingToSet", sInitialTarget)
#	## Evaluation function:
#	def EvalFunc(bWarp):
#		debug(__name__ + ", EvalFunc")
#		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
#		DORMANT = App.ArtificialIntelligence.US_DORMANT
#		DONE = App.ArtificialIntelligence.US_DONE
#		if bWarp:
#			return ACTIVE
#		return DONE
#	## The ConditionalAI:
#	pTargetWarpingAway = App.ConditionalAI_Create(pShip, "TargetWarpingAway")
#	pTargetWarpingAway.SetInterruptable(0)
#	pTargetWarpingAway.SetContainedAI(pFollowThroughWarp)
#	pTargetWarpingAway.AddCondition(pWarp)
#	pTargetWarpingAway.SetEvaluationFunction(EvalFunc)
#	# Done creating ConditionalAI TargetWarpingAway
#	#########################################





	######### AI Builder Begin #########
	return pTargetWarpingAway  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate5(pShip, sInitialTarget):
	########## AI Builder End ##########
	#########################################
	# Creating PlainAI Intercept at (498, 397)
	debug(__name__ + ", BuilderCreate5")
	pIntercept = App.PlainAI_Create(pShip, "Intercept")
	pIntercept.SetScriptModule("Intercept")
	pIntercept.SetInterruptable(1)
	pScript = pIntercept.GetScriptInstance()
	pScript.SetTargetObjectName(sInitialTarget)
	pScript.SetInterceptDistance(572.0)
	# Done creating PlainAI Intercept
	#########################################
	######### AI Builder Begin #########
	return pIntercept  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate6(pShip, pIntercept, sInitialTarget):
	########## AI Builder End ##########
	#########################################
	# Creating ConditionalAI TargetTooFar at (498, 363)
	## Conditions:
	#### Condition Range
	debug(__name__ + ", BuilderCreate6")
	pRange = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 100.0 / 0.175, sInitialTarget, pShip.GetName())
	#### Condition Warp
	pWarp = App.ConditionScript_Create("Conditions.ConditionWarpingToSet", "ConditionWarpingToSet", sInitialTarget)
	## Evaluation function:
	def EvalFunc(bRange, bWarp):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bRange or bWarp:
			return DONE
		return ACTIVE
	## The ConditionalAI:
	pTargetTooFar = App.ConditionalAI_Create(pShip, "TargetTooFar")
	pTargetTooFar.SetInterruptable(0)
	pTargetTooFar.SetContainedAI(pIntercept)
	pTargetTooFar.AddCondition(pRange)
	pTargetTooFar.AddCondition(pWarp)
	pTargetTooFar.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI TargetTooFar
	#########################################
	######### AI Builder Begin #########
	return pTargetTooFar  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate7(pShip, sInitialTarget):
	########## AI Builder End ##########
	#########################################
	# Creating PlainAI MoveIn at (655, 340)
	debug(__name__ + ", BuilderCreate7")
	pMoveIn = App.PlainAI_Create(pShip, "MoveIn")
	pMoveIn.SetScriptModule("FollowObject")
	pMoveIn.SetInterruptable(1)
	pScript = pMoveIn.GetScriptInstance()
	pScript.SetFollowObjectName(sInitialTarget)
	# Done creating PlainAI MoveIn
	#########################################
	# Builder AI Dependency Object (sInitialTarget)
	######### AI Builder Begin #########
	return pMoveIn  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate8(pShip, pTargetWarpingAway, pTargetTooFar, pMoveIn):
	########## AI Builder End ##########
	#########################################
	# Creating SequenceAI Sequence_2 at (459, 282)
	debug(__name__ + ", BuilderCreate8")
	pSequence_2 = App.SequenceAI_Create(pShip, "Sequence_2")
	pSequence_2.SetInterruptable(1)
	pSequence_2.SetLoopCount(-1)
	pSequence_2.SetResetIfInterrupted(1)
	pSequence_2.SetDoubleCheckAllDone(1)
	pSequence_2.SetSkipDormant(1)
	# SeqBlock is at (473, 312)
	pSequence_2.AddAI(pTargetWarpingAway)
	pSequence_2.AddAI(pTargetTooFar)
	pSequence_2.AddAI(pMoveIn)
	# Done creating SequenceAI Sequence_2
	#########################################
	######### AI Builder Begin #########
	return pSequence_2  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate9(pShip, pSequence_2, pAllTargetsGroup, sInitialTarget):
	########## AI Builder End ##########
	#########################################
	# Creating PreprocessingAI SelectTarget at (459, 244)
	## Setup:
	debug(__name__ + ", BuilderCreate9")
	import AI.Preprocessors
	pSelectionPreprocess = AI.Preprocessors.SelectTarget(pAllTargetsGroup)
	pSelectionPreprocess.SetRelativeImportance(fDistance = 0.1, fInFront = 1.0, fIsTarget = 0.1, fShield = -0.1, fWeapons = 1.0, fHull = 0.1, fDamage = 30.0, fPriority = -0.1, fPopularity = 1.0)
	## The PreprocessingAI:
	pSelectTarget = App.PreprocessingAI_Create(pShip, "SelectTarget")
	pSelectTarget.SetInterruptable(1)
	pSelectTarget.SetPreprocessingMethod(pSelectionPreprocess, "Update")
	pSelectTarget.SetContainedAI(pSequence_2)
	# Done creating PreprocessingAI SelectTarget
	#########################################
	# Builder AI Dependency Object (pAllTargetsGroup)
	# Builder AI Dependency Object (sInitialTarget)
	######### AI Builder Begin #########
	return pSelectTarget  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate10(pShip, pSelectTarget):
	########## AI Builder End ##########
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (459, 197)
	## Setup:
	debug(__name__ + ", BuilderCreate10")
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pSelectTarget)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	######### AI Builder Begin #########
	return pAvoidObstacles  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate11(pShip, pAvoidObstacles):
	########## AI Builder End ##########
	#########################################
	# Creating ConditionalAI ComputeNew_BearingIn5sec at (459, 151)
	## Conditions:
	#### Condition TimePassed
	debug(__name__ + ", BuilderCreate11")
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 0.5, 1)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if not bTimePassed:
			return ACTIVE
		return DONE
	## The ConditionalAI:
	pComputeNew_BearingIn5sec = App.ConditionalAI_Create(pShip, "ComputeNew_BearingIn5sec")
	pComputeNew_BearingIn5sec.SetInterruptable(1)
	pComputeNew_BearingIn5sec.SetContainedAI(pAvoidObstacles)
	pComputeNew_BearingIn5sec.AddCondition(pTimePassed)
	pComputeNew_BearingIn5sec.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI ComputeNew_BearingIn5sec
	#########################################
	######### AI Builder Begin #########
	return pComputeNew_BearingIn5sec  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate12(pShip, p2sec_InAttackPowerReserve, pComputeNew_BearingIn5sec):
	########## AI Builder End ##########
	#########################################
	# Creating SequenceAI Sequence at (267, 95)
	debug(__name__ + ", BuilderCreate12")
	pSequence = App.SequenceAI_Create(pShip, "Sequence")
	pSequence.SetInterruptable(1)
	pSequence.SetLoopCount(-1)
	pSequence.SetResetIfInterrupted(1)
	pSequence.SetDoubleCheckAllDone(1)
	pSequence.SetSkipDormant(1)
	# SeqBlock is at (292, 126)
	pSequence.AddAI(p2sec_InAttackPowerReserve)
	pSequence.AddAI(pComputeNew_BearingIn5sec)
	# Done creating SequenceAI Sequence
	#########################################
	######### AI Builder Begin #########
	return pSequence  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate13(pShip, pSequence):
	########## AI Builder End ##########
	#########################################
	# Creating PreprocessingAI PowerManagement at (266, 56)
	## Setup:
	debug(__name__ + ", BuilderCreate13")
	import AI.Preprocessors
	pPowerManager = AI.Preprocessors.ManagePower(0)
	## The PreprocessingAI:
	pPowerManagement = App.PreprocessingAI_Create(pShip, "PowerManagement")
	pPowerManagement.SetInterruptable(1)
	pPowerManagement.SetPreprocessingMethod(pPowerManager, "Update")
	pPowerManagement.SetContainedAI(pSequence)
	# Done creating PreprocessingAI PowerManagement
	#########################################
	######### AI Builder Begin #########
	return pPowerManagement  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate14(pShip, pPowerManagement):
	########## AI Builder End ##########
	#########################################
	# Creating PreprocessingAI AlertLevel at (265, 15)
	## Setup:
	debug(__name__ + ", BuilderCreate14")
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

#################################################################################################################
##########	MONKEY PATCH
#################################################################################################################
import nt
import string
import traceback
import Foundation

milkyWay = "Custom.Autoload.LoadGalaxyCharts"
resistanceIsFutile = "AI.Compound.BorgAttack"
#pathOfMethodOverride = "Custom.GalaxyCharts.GalaxyLIB"

myContinueS = 0
try:
	banana = __import__(milkyWay, globals(), locals(), ["mode"])
	myContinueS = 1
except:
	myContinueS = 0
	print "FIX-BorgAttackAIforGC: Missing scripts.", milkyWay

if myContinueS == 1:
	if hasattr(banana, "mode"):
		mode = banana.mode
		myContinueR = 0
		try:
			pear = __import__(resistanceIsFutile, globals(), locals(), ["CreateAI", "BuilderCreate3", "BuilderCreate4"])
			myContinueR = 1
		except:
			myContinueR = 0
			print "FIX-BorgAttackAIforGC: Missing scripts.", resistanceIsFutile

		if myContinueR == 1:
			if hasattr(banana, "MethodOverrideDef"):
				print "FIX-BorgAttackAIforGC: Patching BorgAttack AI for GC..."
				if hasattr(pear, "CreateAI"):
					Foundation.OverrideDef('zzzGCBorgCreate_AI', 'AI.Compound.BorgAttack.CreateAI', __name__ +'.CreateAI', dict = { 'modes': [ mode ] } )
				if hasattr(pear, "BuilderCreate3"):
					Foundation.OverrideDef('zzzGCBorgBC3_AI', 'AI.Compound.BorgAttack.BuilderCreate3', __name__ +'.BuilderCreate3', dict = { 'modes': [ mode ] } )
				if hasattr(pear, "BuilderCreate4"):
					Foundation.OverrideDef('zzzGCBorgBC4_AI', 'AI.Compound.BorgAttack.BuilderCreate4', __name__ +'.BuilderCreate4', dict = { 'modes': [ mode ] } )

		else:
			print "FIX-BorgAttackAIforGC: Missing BorgAttack AI to patch. Skipping..."
	else:
		print "FIX-BorgAttackAIforGC: Error, Missing mode for LoadGalaxyCharts"
else:
	print "FIX-BorgAttackAIforGC: Skipping..."

#################################################################################################################
##########	END OF MONKEY PATCH
#################################################################################################################
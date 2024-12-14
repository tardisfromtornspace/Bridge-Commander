# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# 14th December 2024
# The 'Borg AI Final' was one AI jayce (aka Resistance Is Futile) modified at least until 2008 from an unknown author for Borg vessels, bringing a lot of functionality to those vessels. Inside the BorgAttack file and its readme it explicity says **Do Not Modify The Borg AI Final*
# However, this AI presents one weird glitch when combined with GalaxyCharts which makes the game crash immediately if a ship travelled two systems while one Borg vessel was chasing them.
# THIS IS an Autoload PATCH to fix this conflict, a patch which qualifies under fair use with original dependency, with the purpose to keep the original file unmodified.
# This patch works partially through Foundation's OverrideDef System and through wrappers and it is tied to GalaxyCharts's mutator being enabled, meaning that a mod without GC or with GC being disabled will make absolutely NO difference on the BorgAttack AI.
# The only areas I MIGHT even declare as even slightly mine (Alex SL Gato's) are the areas labeled as "OVERRIDES", two lines "EXTRA ADDED" on CreateAI, the changes done to "MODINFO" if just to keep track of any changes done with a glance for other modders, as well as the changes done to BuilderCreate3 and BuilderCreate4 with the help of the AIEditor Tool
#
#################################################################################################################
#
MODINFO = { "Author": "Unknown (original), \"jayce\" (Final), Alex SL Gato (small patch for GC)",
	    "Version": "20241214",
	    "License": "Original Dependency",
	    "Description": "Read the small title above for more info"
	    }
#
#################################################################################################################
#
import App
from bcdebug import debug
import Foundation
import nt
import string
import traceback

#################################################################################################################
##########	OVERRIDES
#################################################################################################################

CURRENTVERSION = "20241214"
FORCEUPDATE = 0 # If 1, this value will force a pre-existing scripts/AI/Compound/BorgAttack to be overriden 
milkyWay = "Custom.Autoload.LoadGalaxyCharts"
resistanceIsFutile = "AI.Compound.BorgAttack"
sResistanceIsFutile = "scripts\\AI\\Compound\\BorgAttack.py"

myContinueS = 0
myContinueR = 0
myContinueU = 0
mode = None
pear = None

CreateAI = None

attributesBorgAttackHas = {
	#First these which we have exact values
	'__doc__': "None",
	'__name__': '\'AI.Compound.BorgAttack\'',
	'__file__': "'.\\\\Scripts\\\\AI\\\\Compound\\\\BorgAttack.pyc'",
	'App': "<module 'App' from '.\Scripts\App.pyc'>",
	# Then those we must ignore
	'__builtins__': {"best to ignore": "yes"},
	
	# Then those which indicate they are a function
	'debug': "<function debug at ",
	#And finally those which are called on the function proper
	'CreateAI': "<function CreateAI at ",
	'BuilderCreate1': "<function BuilderCreate1 at ",
	'BuilderCreate2': "<function BuilderCreate2 at ",
	'BuilderCreate3': "<function BuilderCreate3 at ",
	'BuilderCreate4': "<function BuilderCreate4 at ",
	'BuilderCreate5': "<function BuilderCreate5 at ",
	'BuilderCreate6': "<function BuilderCreate6 at ",
	'BuilderCreate7': "<function BuilderCreate7 at ",
	'BuilderCreate8': "<function BuilderCreate8 at ",
	'BuilderCreate9': "<function BuilderCreate9 at ",
	'BuilderCreate10': "<function BuilderCreate10 at ",
	'BuilderCreate11': "<function BuilderCreate11 at ",
	'BuilderCreate12': "<function BuilderCreate12 at ",
	'BuilderCreate13': "<function BuilderCreate13 at ",
	'BuilderCreate14': "<function BuilderCreate14 at ",
}

attributesThatBorgAttackHas = ["CreateAI", "BuilderCreate1", "BuilderCreate2", "BuilderCreate3", "BuilderCreate4", "BuilderCreate5", "BuilderCreate6", "BuilderCreate7", "BuilderCreate8", "BuilderCreate9", "BuilderCreate10", "BuilderCreate11", "BuilderCreate12", "BuilderCreate13", "BuilderCreate14"]
def ModuleHasBorgAttackFinal2008Attributes(pear):
	debug(__name__ + ", ModuleHasBorgAttackFinal2008Attributes")
	hasAllAttributes = 0
	if pear == None:
		return hasAllAttributes

	pearDict = pear.__dict__
	if not pearDict:
		return hasAllAttributes

	pearKeys = pearDict.keys()
	
	missingAttribs = 0
	for attrib in attributesBorgAttackHas.keys():
		if not attrib in pearKeys:
			missingAttribs = missingAttribs + 1
			if attrib == 'CreateAI': # This means that whatever version of BorgAttack AI exists, it is broken
				print "FIX-BorgAttackAIforGC: just found out that your BorgAttack AI does not have a CreateAI function... this will be patched."
				FORCEUPDATE = 1
	
	if missingAttribs > 0:
		return hasAllAttributes

	validAttribs = 0
	invalidAttribs = 0
	numberAttribs = 0
	for key in pearDict.keys():
		#try:
			numberAttribs = numberAttribs + 1
			if key == '__builtins__':
				if type(pearDict[key]) == type({}):
					validAttribs = validAttribs + 1
				else:
					invalidAttribs = invalidAttribs + 1
				continue
			if not key in attributesBorgAttackHas.keys():
				if key == "VERSION":
					if hasattr(pear, "VERSION") and pear.VERSION >= CURRENTVERSION:
						validAttribs = validAttribs + 1
					else:
						invalidAttribs = invalidAttribs + 1
				else:
					invalidAttribs = invalidAttribs + 1
			else:
				myPartialRepr = attributesBorgAttackHas[key]
				myRepr = repr(pearDict[key])
				position = string.find(myRepr, myPartialRepr)
				if position != 0: # Either not found, or whatever was found is outside
					invalidAttribs = invalidAttribs + 1
				else:
					validAttribs = validAttribs + 1
		#except:
		#	print "FIX-BorgAttackAIforGC: Error while calling ModuleHasBorgAttackFinal2008Attributes:"
		#	traceback.print_exc()

	hasAllAttributes = (validAttribs == numberAttribs and invalidAttribs == 0)
	return hasAllAttributes

try:
	banana = __import__(milkyWay, globals(), locals(), ["mode"])
	myContinueS = 1
except:
	myContinueS = 0
	print "FIX-BorgAttackAIforGC: Missing scripts.", milkyWay

if myContinueS == 1:
	if hasattr(banana, "mode"):
		mode = banana.mode
		try:
			pear = __import__(resistanceIsFutile, globals(), locals(), ["CreateAI", "BuilderCreate3", "BuilderCreate4"])
			myContinueR = 1
		except:
			myContinueR = 0
			print "FIX-BorgAttackAIforGC: Missing scripts.", resistanceIsFutile

		if myContinueR == 1:
			if hasattr(banana, "MethodOverrideDef"):

				if ModuleHasBorgAttackFinal2008Attributes(pear): # This is to ensure your Borg AI is the final BorgAttack version, so we don't accidentally break your AI with this
					myContinueU = 1
					# This is the code I used before, it is safer since it updated yes or yes the BorgAttack AI someone had to the BorgAttack Final 2008 version by jayce, but it could possibly send us to a legal issue
					# Since I had to manually create a BorgAttack.py copy
					#Foundation.OverrideDef('zzzGCBorgCreate_AI', 'AI.Compound.BorgAttack.CreateAI', __name__ +'.CreateAI', dict = { 'modes': [ mode ] } )
					#Foundation.OverrideDef('zzzGCBorgBC3_AI', 'AI.Compound.BorgAttack.BuilderCreate3', __name__ +'.BuilderCreate3', dict = { 'modes': [ mode ] } )
					#Foundation.OverrideDef('zzzGCBorgBC4_AI', 'AI.Compound.BorgAttack.BuilderCreate4', __name__ +'.BuilderCreate4', dict = { 'modes': [ mode ] } )
				else:
					myContinueU = -1
					print "FIX-BorgAttackAIforGC: Your install's BorgAttack AI is not the final version to patch. Updating Instead"

		else:
			print "FIX-BorgAttackAIforGC: Missing BorgAttack AI to patch. Skipping..."
	else:
		print "FIX-BorgAttackAIforGC: Error, Missing mode for LoadGalaxyCharts"
else:
	print "FIX-BorgAttackAIforGC: Skipping..."

#################################################################################################################

oldBuilderCreate3 = None
oldBuilderCreate4 = None
oldCreateAI = None

#These two functions below are here just as a possible backup in case somebody grabbed an outdated version of BorgAttack.py
	######### AI Builder Begin #########
def BuilderCreate3Old(pShip, sInitialTarget, dKeywords={}):
	########## AI Builder End ##########
	#########################################
	# Creating PlainAI FollowThroughWarp at (313, 399)
	debug(__name__ + ", BuilderCreate3")
	pFollowThroughWarp = App.PlainAI_Create(pShip, "FollowThroughWarp")
	pFollowThroughWarp.SetScriptModule("FollowThroughWarp")
	pFollowThroughWarp.SetInterruptable(1)
	pScript = pFollowThroughWarp.GetScriptInstance()
	pScript.SetFollowObjectName(sInitialTarget)
	# Done creating PlainAI FollowThroughWarp
	#########################################
	######### AI Builder Begin #########
	return pFollowThroughWarp  # Builder Return
	########## AI Builder End ##########


	######### AI Builder Begin #########
def BuilderCreate4Old(pShip, pFollowThroughWarp, sInitialTarget, dKeywords={}):
	########## AI Builder End ##########

	#########################################
	# Creating ConditionalAI TargetWarpingAway at (313, 365)
	## Conditions:
	#### Condition Warp
	debug(__name__ + ", BuilderCreate4")
	pWarp = App.ConditionScript_Create("Conditions.ConditionWarpingToSet", "ConditionWarpingToSet", sInitialTarget)
	## Evaluation function:
	def EvalFunc(bWarp):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bWarp:
			return ACTIVE
		return DONE
	## The ConditionalAI:
	pTargetWarpingAway = App.ConditionalAI_Create(pShip, "TargetWarpingAway")
	pTargetWarpingAway.SetInterruptable(0)
	pTargetWarpingAway.SetContainedAI(pFollowThroughWarp)
	pTargetWarpingAway.AddCondition(pWarp)
	pTargetWarpingAway.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI TargetWarpingAway
	#########################################
	######### AI Builder Begin #########
	return pTargetWarpingAway  # Builder Return
	########## AI Builder End ##########

if myContinueU == 1: # If all goes well and the script is correct, then we just need to do this, else we default to the functions in what would have been correct
	from AI.Compound import BorgAttack
	oldBuilderCreate3 = BorgAttack.BuilderCreate3
	oldBuilderCreate4 = BorgAttack.BuilderCreate4
	oldCreateAI = BorgAttack.CreateAI
else:
	oldBuilderCreate3 = BuilderCreate3Old
	oldBuilderCreate4 = BuilderCreate4Old	

def BuilderCreate3(pShip, sInitialTarget, dKeywords={}): # Call to original
	debug(__name__ + ", BuilderCreate3")
	if mode == None or not (hasattr(mode, "IsEnabled") and mode.IsEnabled()):
		return oldBuilderCreate3(pShip, sInitialTarget)
	else:
		return BuilderCreate3GC(pShip, sInitialTarget, dKeywords)

def BuilderCreate3GC(pShip, sInitialTarget, dKeywords={}):  # Call to modified during GC
	#########################################
	# Creating CompoundAI FollowThroughWarp at (313, 399)
	debug(__name__ + ", BuilderCreate3GC")
	import AI.Compound.FollowThroughWarp
	pFollowThroughWarp = AI.Compound.FollowThroughWarp.CreateAI(pShip, sInitialTarget, Keywords = dKeywords, FollowToSB12 = 1, FollowThroughMissions = 1)
	# Done creating CompoundAI FollowThroughWarp
	#########################################

	return pFollowThroughWarp  # Builder Return

def BuilderCreate4(pShip, pFollowThroughWarp, sInitialTarget, dKeywords={}): # Call to original
	debug(__name__ + ", BuilderCreate4")
	if mode == None or not (hasattr(mode, "IsEnabled") and mode.IsEnabled()):
		return oldBuilderCreate4(pShip, pFollowThroughWarp, sInitialTarget)
	else:
		return BuilderCreate4GC(pShip, pFollowThroughWarp, sInitialTarget, dKeywords)

def BuilderCreate4GC(pShip, pFollowThroughWarp, sInitialTarget, dKeywords={}):  # Call to modified during GC
	#########################################
	# Creating ConditionalAI TargetWarpingAway at (313, 365)
	## Conditions:
	#### Condition FlagSet
	debug(__name__ + ", BuilderCreate4GC")
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

	return pTargetWarpingAway  # Builder Return

def NewCreateAI(pShip, *lpTargets, **dKeywords):
	debug(__name__ + ", NewCreateAI")
	pBuilderAI = apply(oldCreateAI, (pShip, ) + lpTargets, dKeywords)
	if pBuilderAI:
		if not mode == None and hasattr(mode, "IsEnabled") and mode.IsEnabled():
			pBuilderAI.AddDependencyObject("FollowThroughWarp", "dKeywords", dKeywords)           #### TAGGED 2 EXTRA LINE ADDED
			pBuilderAI.AddDependencyObject("TargetWarpingAway", "dKeywords", dKeywords)           #### TAGGED 1 EXTRA LINE ADDED
		return pBuilderAI
	else:
		print "FIX-BorgAttackAIforGC: ERROR WHILE Creating default BorgAttack AI"
		return oldCreateAI(pShip)

def CreateAIGC(pShip, *lpTargets, **dKeywords):
	debug(__name__ + ", CreateAIGC")
	pBuilderAI = apply(oldCreateAI, (pShip, ) + lpTargets, dKeywords)
	if pBuilderAI:
		if not mode == None and hasattr(mode, "IsEnabled") and mode.IsEnabled():
			pBuilderAI.AddDependencyObject("FollowThroughWarp", "dKeywords", dKeywords)           #### TAGGED 2 EXTRA LINE ADDED
			pBuilderAI.AddDependencyObject("TargetWarpingAway", "dKeywords", dKeywords)           #### TAGGED 1 EXTRA LINE ADDED
		return pBuilderAI
	else:
		print "FIX-BorgAttackAIforGC: ERROR WHILE Creating default BorgAttack AI"
		return oldCreateAI(pShip)

# I could totally just make it link to CreateAIGC and done, but in order not to get legal problems...

if myContinueU == 1:
	BorgAttack.BuilderCreate3 = BuilderCreate3
	#Foundation.OverrideDef('zzzGCBorgBC3_AI', __name__ +'.BuilderCreate3', __name__ +'.BuilderCreate3GC', dict = { 'modes': [ mode ] } )

	BorgAttack.BuilderCreate4 = BuilderCreate4
	#Foundation.OverrideDef('zzzGCBorgBC4_AI', __name__ +'.BuilderCreate4', __name__ +'.BuilderCreate4GC', dict = { 'modes': [ mode ] } )

	BorgAttack.CreateAI = NewCreateAI
	#Foundation.OverrideDef('zzzGCBorgCreate_AI', __name__ +'.NewCreateAI', __name__ +'.CreateAIGC', dict = { 'modes': [ mode ] } )

	# Adding Versioning because it is a real hadache to verify that the script we overrode was in fact the BorgAttack.pyc with the Borg Attack AI Final '10 July 2008' when according to its readme it should not have a .py stored there and it is just a .pyc without any actual unique attributes to extract info from

	BorgAttack.VERSION = CURRENTVERSION
	print "FIX-BorgAttackAIforGC: Patched BorgAttack AI for GC."

#################################################################################################################
##########	END OF OVERRIDES
#################################################################################################################

# And now, this below is just in case our script detected something extremely wrong with the AI - just sets the BorgAttack to the final version by jayce - setting it to the final version if the BorgAttack script on the install is not the final version should not be an issue, shouldn't it?

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

	pBuilderAI.AddAIBlock("FollowThroughWarp", "BuilderCreate3")
	pBuilderAI.AddDependencyObject("FollowThroughWarp", "sInitialTarget", sInitialTarget)

	pBuilderAI.AddDependencyObject("FollowThroughWarp", "dKeywords", dKeywords)           #### TAGGED 2 EXTRA LINE ADDED

	pBuilderAI.AddAIBlock("TargetWarpingAway", "BuilderCreate4")
	pBuilderAI.AddDependencyObject("TargetWarpingAway", "sInitialTarget", sInitialTarget) 

	pBuilderAI.AddDependencyObject("TargetWarpingAway", "dKeywords", dKeywords)           #### TAGGED 1 EXTRA LINE ADDED

	pBuilderAI.AddDependency("TargetWarpingAway", "FollowThroughWarp")
	pBuilderAI.AddAIBlock("Intercept", "BuilderCreate5")
	pBuilderAI.AddDependencyObject("Intercept", "sInitialTarget", sInitialTarget)
	pBuilderAI.AddAIBlock("TargetTooFar", "BuilderCreate6")
	pBuilderAI.AddDependencyObject("TargetTooFar", "sInitialTarget", sInitialTarget)
	pBuilderAI.AddDependency("TargetTooFar", "Intercept")
	pBuilderAI.AddAIBlock("MoveIn", "BuilderCreate7")
	pBuilderAI.AddDependencyObject("MoveIn", "sInitialTarget", sInitialTarget)
	pBuilderAI.AddAIBlock("Sequence_2", "BuilderCreate8")
	pBuilderAI.AddDependency("Sequence_2", "TargetWarpingAway")
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

#	######### AI Builder Begin #########
#def BuilderCreate3(pShip, sInitialTarget, dKeywords={}):
#	########## AI Builder End ##########
#
#	#########################################
#	# Creating CompoundAI FollowThroughWarp at (313, 399)
#	debug(__name__ + ", BuilderCreate3")
#	import AI.Compound.FollowThroughWarp
#	pFollowThroughWarp = AI.Compound.FollowThroughWarp.CreateAI(pShip, sInitialTarget, Keywords = dKeywords, FollowToSB12 = 1, FollowThroughMissions = 1)
#	# Done creating CompoundAI FollowThroughWarp
#	#########################################
#	# BELOW ORIGINAL, ABOVE MODIFIED
##	#########################################
##	# Creating PlainAI FollowThroughWarp at (313, 399)
##	debug(__name__ + ", BuilderCreate3")
##	pFollowThroughWarp = App.PlainAI_Create(pShip, "FollowThroughWarp")
##	pFollowThroughWarp.SetScriptModule("FollowThroughWarp")
##	pFollowThroughWarp.SetInterruptable(1)
##	pScript = pFollowThroughWarp.GetScriptInstance()
##	pScript.SetFollowObjectName(sInitialTarget)
##	# Done creating PlainAI FollowThroughWarp
##	#########################################
#
#	######### AI Builder Begin #########
#	return pFollowThroughWarp  # Builder Return
#	########## AI Builder End ##########
#	######### AI Builder Begin #########
#def BuilderCreate4(pShip, pFollowThroughWarp, sInitialTarget, dKeywords={}):
#	########## AI Builder End ##########
#
#	#########################################
#	# Creating ConditionalAI TargetWarpingAway at (313, 365)
#	## Conditions:
#	#### Condition FlagSet
#	debug(__name__ + ", BuilderCreate4")
#	pFlagSet = App.ConditionScript_Create("Conditions.ConditionFlagSet", "ConditionFlagSet", "FollowTargetThroughWarp", dKeywords)
#	#### Condition WarpingToSet
#	pWarpingToSet = App.ConditionScript_Create("Conditions.ConditionWarpingToSet", "ConditionWarpingToSet", sInitialTarget)
#	## Evaluation function:
#	def EvalFunc(bFlagSet, bWarpingToSet):
#		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
#		DORMANT = App.ArtificialIntelligence.US_DORMANT
#		DONE = App.ArtificialIntelligence.US_DONE
#		if bFlagSet and  bWarpingToSet:
#			return ACTIVE
#		return DONE
#	## The ConditionalAI:
#	pTargetWarpingAway = App.ConditionalAI_Create(pShip, "TargetWarpingAway")
#	pTargetWarpingAway.SetInterruptable(0)
#	pTargetWarpingAway.SetContainedAI(pFollowThroughWarp)
#	pTargetWarpingAway.AddCondition(pFlagSet)
#	pTargetWarpingAway.AddCondition(pWarpingToSet)
#	pTargetWarpingAway.SetEvaluationFunction(EvalFunc)
#	# Done creating ConditionalAI TargetWarpingAway
#	#########################################
#	# BELOW ORIGINAL, ABOVE MODIFIED
##	#########################################
##	# Creating ConditionalAI TargetWarpingAway at (313, 365)
##	## Conditions:
##	#### Condition Warp
##	debug(__name__ + ", BuilderCreate4")
##	pWarp = App.ConditionScript_Create("Conditions.ConditionWarpingToSet", "ConditionWarpingToSet", sInitialTarget)
##	## Evaluation function:
##	def EvalFunc(bWarp):
##		debug(__name__ + ", EvalFunc")
##		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
##		DORMANT = App.ArtificialIntelligence.US_DORMANT
##		DONE = App.ArtificialIntelligence.US_DONE
##		if bWarp:
##			return ACTIVE
##		return DONE
##	## The ConditionalAI:
##	pTargetWarpingAway = App.ConditionalAI_Create(pShip, "TargetWarpingAway")
##	pTargetWarpingAway.SetInterruptable(0)
##	pTargetWarpingAway.SetContainedAI(pFollowThroughWarp)
##	pTargetWarpingAway.AddCondition(pWarp)
##	pTargetWarpingAway.SetEvaluationFunction(EvalFunc)
##	# Done creating ConditionalAI TargetWarpingAway
##	#########################################
#
#	######### AI Builder Begin #########
#	return pTargetWarpingAway  # Builder Return
#	########## AI Builder End ##########

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


# THE OVERRIDE
if myContinueU == -1:
	if FORCEUPDATE and CreateAI != None:
		print "FIX-BorgAttackAIforGC has overriden the preexisting BorgAttack AI. If you don't want so, please remove scipts/Custom/Autoload/FIX-BorgAttackAIforGC or set FORCEUPDATE to 0. Please note that FORCEUPDATE automatically sets to 1 if your BorgAttack AI was already broken"
		BorgAttack.CreateAI = CreateAI
		BorgAttack.VERSION = CURRENTVERSION
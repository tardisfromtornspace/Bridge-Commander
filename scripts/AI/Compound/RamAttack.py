	######### AI Builder Begin #########
## BUILDER AI
##  This AI file has been mauled by the MakeBuilderAI script.
##  Modify at your own risk.
##  Or run MakeBuilderAI(filename, 1) to remove the BuilderAI code.
	########## AI Builder End ##########
import App

# setting Speed to 100 makes sure we go as fast as possible.
def CreateAI(pShip, pTargetName, pAllTargetsGroup, Speed = 100):
	######### AI Builder Begin #########
	pBuilderAI = App.BuilderAI_Create(pShip, "PriorityList Builder", __name__)
	pBuilderAI.AddAIBlock("Back", "BuilderCreate1")
	pBuilderAI.AddDependencyObject("Back", "pAllTargetsGroup", pAllTargetsGroup)
	pBuilderAI.AddAIBlock("noTarget", "BuilderCreate2")
	pBuilderAI.AddDependency("noTarget", "Back")
	pBuilderAI.AddAIBlock("Attack", "BuilderCreate3")
	pBuilderAI.AddDependencyObject("Attack", "pTargetName", pTargetName)
	pBuilderAI.AddAIBlock("ConditionInFrontOff", "BuilderCreate4")
	pBuilderAI.AddDependency("ConditionInFrontOff", "Attack")
	pBuilderAI.AddDependencyObject("ConditionInFrontOff", "pTargetName", pTargetName)
	pBuilderAI.AddAIBlock("FollowTroughWarp", "BuilderCreate5")
	pBuilderAI.AddDependencyObject("FollowTroughWarp", "pTargetName", pTargetName)
	pBuilderAI.AddAIBlock("RamAI", "BuilderCreate6")
	pBuilderAI.AddDependencyObject("RamAI", "pTargetName", pTargetName)
        pBuilderAI.AddDependencyObject("RamAI", "Speed", Speed)
	pBuilderAI.AddAIBlock("PriorityList", "BuilderCreate7")
	pBuilderAI.AddDependency("PriorityList", "noTarget")
	pBuilderAI.AddDependency("PriorityList", "ConditionInFrontOff")
	pBuilderAI.AddDependency("PriorityList", "FollowTroughWarp")
	pBuilderAI.AddDependency("PriorityList", "RamAI")
	return pBuilderAI # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate1(pShip, pAllTargetsGroup):
	########## AI Builder End ##########
	#########################################
	# Creating PlainAI Back at (283, 357)
	pBack = App.PlainAI_Create(pShip, "Back")
	pBack.SetScriptModule("RunScript")
	pBack.SetInterruptable(1)
	pScript = pBack.GetScriptInstance()
	pScript.SetScriptModule("AI.Compound.DomRamAI")
	pScript.SetFunction("DomAI")
	pScript.SetArguments(pShip, pAllTargetsGroup)
	# Done creating PlainAI Back
	#########################################
	# Builder AI Dependency Object (pAllTargetsGroup)

	######### AI Builder Begin #########
	return pBack  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate2(pShip, pBack):
	########## AI Builder End ##########
	#########################################
	# Creating ConditionalAI noTarget at (158, 377)
	## Conditions:
	#### Condition TargetExists
        if pShip.GetTarget():
	        pTargetExists = App.ConditionScript_Create("Conditions.ConditionExists", "ConditionExists", pShip.GetTarget().GetName())
        else:
                pTargetExists = App.ConditionScript_Create("Conditions.ConditionExists", "ConditionExists", None)
	## Evaluation function:
	def EvalFunc(bTargetExists):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if not bTargetExists:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pnoTarget = App.ConditionalAI_Create(pShip, "noTarget")
	pnoTarget.SetInterruptable(1)
	pnoTarget.SetContainedAI(pBack)
	pnoTarget.AddCondition(pTargetExists)
	pnoTarget.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI noTarget
	#########################################
	######### AI Builder Begin #########
	return pnoTarget  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate3(pShip, pTargetName):
	########## AI Builder End ##########
	#########################################
	# Creating PlainAI Attack at (270, 249)
	pAttack = App.PlainAI_Create(pShip, "Attack")
	pAttack.SetScriptModule("StationaryAttack")
	pAttack.SetInterruptable(1)
	pScript = pAttack.GetScriptInstance()
	pScript.SetTargetObjectName(pTargetName)
	# Done creating PlainAI Attack
	#########################################
	# Builder AI Dependency Object (pTargetName)
	######### AI Builder Begin #########
	return pAttack  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate4(pShip, pAttack, pTargetName):
	########## AI Builder End ##########
	#########################################
	# Creating ConditionalAI ConditionInFrontOff at (174, 269)
	## Conditions:
	#### Condition ConInArc
	pConInArc = App.ConditionScript_Create("Conditions.ConditionInPhaserFiringArc", "ConditionInPhaserFiringArc", pShip.GetName(), pTargetName, 1)
	## Evaluation function:
	def EvalFunc(bConInArc):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bConInArc:
			return DONE
		return ACTIVE
	## The ConditionalAI:
	pConditionInFrontOff = App.ConditionalAI_Create(pShip, "ConditionInFrontOff")
	pConditionInFrontOff.SetInterruptable(1)
	pConditionInFrontOff.SetContainedAI(pAttack)
	pConditionInFrontOff.AddCondition(pConInArc)
	pConditionInFrontOff.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI ConditionInFrontOff
	#########################################
	# Builder AI Dependency Object (pTargetName)
	######### AI Builder Begin #########
	return pConditionInFrontOff  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate5(pShip, pTargetName):
	########## AI Builder End ##########
	#########################################
	# Creating CompoundAI FollowTroughWarp at (190, 105)
	import AI.Compound.FollowThroughWarp
	pFollowTroughWarp = AI.Compound.FollowThroughWarp.CreateAI(pShip, pTargetName)
	# Done creating CompoundAI FollowTroughWarp
	#########################################
	# Builder AI Dependency Object (pTargetName)
	######### AI Builder Begin #########
	return pFollowTroughWarp  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate6(pShip, pTargetName, Speed):
	########## AI Builder End ##########
	#########################################
	# Creating PlainAI RamAI at (324, 50)
	pRamAI = App.PlainAI_Create(pShip, "RamAI")
	pRamAI.SetScriptModule("Ram")
	pRamAI.SetInterruptable(1)
	pScript = pRamAI.GetScriptInstance()
	pScript.SetTargetObjectName(pTargetName)
	pScript.SetMaximumSpeed(Speed)
	# Done creating PlainAI RamAI
	#########################################
	# Builder AI Dependency Object (pTargetName)
	# Builder AI Dependency Object (Speed)
	######### AI Builder Begin #########
	return pRamAI  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreate7(pShip, pnoTarget, pConditionInFrontOff, pFollowTroughWarp, pRamAI):
	########## AI Builder End ##########
	#########################################
	# Creating PriorityListAI PriorityList at (50, 50)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (149, 57)
	pPriorityList.AddAI(pnoTarget, 1)
	pPriorityList.AddAI(pConditionInFrontOff, 2)
	pPriorityList.AddAI(pFollowTroughWarp, 3)
	pPriorityList.AddAI(pRamAI, 4)
	# Done creating PriorityListAI PriorityList
	#########################################
	return pPriorityList
	######### AI Builder Begin #########
	return pPriorityList  # Builder Return
	########## AI Builder End ##########

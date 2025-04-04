import App
def CreateAI(pShip, pTargetGroup):

	#########################################
	# Creating CompoundAI BasicAttackTargets at (141, 106)
	import AI.Compound.BasicAttack
	pBasicAttackTargets = AI.Compound.BasicAttack.CreateAI(pShip, pTargetGroup, Easy_Difficulty = 0.22, Difficulty = 0.63, Hard_Difficulty = 1.0)
	# Done creating CompoundAI BasicAttackTargets
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (112, 175)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pBasicAttackTargets)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	return pAvoidObstacles

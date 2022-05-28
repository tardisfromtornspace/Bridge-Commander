import App

def CreateAI(pShip, pSaveMe):
	#########################################
	# Creating CompoundAI DefendStation at (50, 50)
	import AI.Compound.Defend2
	pDefendStation = AI.Compound.Defend2.CreateAI(pShip, pSaveMe.GetName())
	# Done creating CompoundAI DefendStation
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (45, 166)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pDefendStation)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	return pAvoidObstacles

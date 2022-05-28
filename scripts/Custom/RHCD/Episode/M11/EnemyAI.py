import App

def CreateAI(pShip):
	#########################################
	import AI.Compound.BasicAttack
	pAttack = AI.Compound.BasicAttack.CreateAI(pShip, ["player"], Easy_Difficulty = 0.35, Difficulty = 0.7, Hard_Difficulty = 1.0)
	#########################################
	#########################################
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pAttack)
	#########################################
	return pAvoidObstacles

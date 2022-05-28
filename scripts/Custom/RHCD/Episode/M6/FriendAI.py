import App
def CreateAI(pShip):
	#########################################
	import AI.Compound.BasicAttack
	pAttackWarbird = AI.Compound.BasicAttack.CreateAI(pShip, ["Warbird 1", "Warbird 2", "Warbird 3", "Warbird 4", "Warbird 5", 
	"Warbird 6", "Warbird 7", "Warbird8", "Warbird 9", "Warbird 10", "Warbird 11", "Warbird 12", "Warbird 13", "Warbird 14", 
	"Warbird 15", "Warbird 16", "Warbird 17", "Warbird 18", "Warbird 19", "Warbird 20", "Warbird 21", "Warbird 22", 
	"Warbird 23", "Warbird 24", "Warbird 25", "Warbird 26", "Warbird 27", "Warbird 28", "Warbird 29", "Warbird 30"])
	#########################################
	#########################################
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	pPriorityList.AddAI(pAttackWarbird, 1)
	#########################################
	#########################################
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pPriorityList)
	#########################################
	return pAvoidObstacles

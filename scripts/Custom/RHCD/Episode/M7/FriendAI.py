import App
def CreateAI(pShip):
	#########################################
	import AI.Compound.BasicAttack
	pAttackKeldon = AI.Compound.BasicAttack.CreateAI(pShip, ["Keldon 1", "Keldon 2", "Keldon 3", "Keldon 4", "Keldon 5", 
	"Keldon 6", "Keldon 7", "Keldon8", "Keldon 9", "Keldon 10", "Keldon 11", "Keldon 12", "Keldon 13", "Keldon 14", 
	"Keldon 15", "Keldon 16", "Keldon 17", "Keldon 18", "Keldon 19", "Keldon 20", "Keldon 21", "Keldon 22", 
	"Keldon 23", "Keldon 24", "Keldon 25", "Keldon 26", "Keldon 27", "Keldon 28", "Keldon 29", "Keldon 30"])
	#########################################
	#########################################
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	pPriorityList.AddAI(pAttackKeldon, 1)
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

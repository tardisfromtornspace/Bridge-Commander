import App
def CreateAI(pShip):
	#########################################
	import AI.Compound.BasicAttack
	pAttackVorcha = AI.Compound.BasicAttack.CreateAI(pShip, ["Vorcha 1", "Vorcha 2", "Vorcha 3", "Vorcha 4", "Vorcha 5", 
	"Vorcha 6", "Vorcha 7", "Vorcha8", "Vorcha 9", "Vorcha 10", "Vorcha 11", "Vorcha 12", "Vorcha 13", "Vorcha 14", 
	"Vorcha 15", "Vorcha 16", "Vorcha 17", "Vorcha 18", "Vorcha 19", "Vorcha 20", "Vorcha 21", "Vorcha 22", 
	"Vorcha 23", "Vorcha 24", "Vorcha 25", "Vorcha 26", "Vorcha 27", "Vorcha 28", "Vorcha 29", "Vorcha 30"])
	#########################################
	#########################################
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	pPriorityList.AddAI(pAttackVorcha, 1)
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

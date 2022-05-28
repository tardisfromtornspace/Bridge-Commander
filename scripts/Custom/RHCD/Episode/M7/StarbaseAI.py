import App
def CreateAI(pShip):
	#########################################
	import AI.Compound.CallDamageAI
	pCallDamageAI = AI.Compound.CallDamageAI.CreateAI(pShip)
	#########################################
	#########################################
	import AI.Compound.StarbaseAttack
	pStarbaseAttack = AI.Compound.StarbaseAttack.CreateAI(pShip, ["Keldon 1", "Keldon 2", "Keldon 3", "Keldon 4", "Keldon 5", 
	"Keldon 6", "Keldon 7", "Keldon8", "Keldon 9", "Keldon 10", "Keldon 11", "Keldon 12", "Keldon 13", "Keldon 14", 
	"Keldon 15", "Keldon 16", "Keldon 17", "Keldon 18", "Keldon 19", "Keldon 20", "Keldon 21", "Keldon 22", 
	"Keldon 23", "Keldon 24", "Keldon 25", "Keldon 26", "Keldon 27", "Keldon 28", "Keldon 29", "Keldon 30"])
	#########################################
	#########################################
	pStarbase12AI = App.PriorityListAI_Create(pShip, "Starbase12AI")
	pStarbase12AI.SetInterruptable(1)
	pStarbase12AI.AddAI(pCallDamageAI, 1)
	pStarbase12AI.AddAI(pStarbaseAttack, 2)
	#########################################
	return pStarbase12AI

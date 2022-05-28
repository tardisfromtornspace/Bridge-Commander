import App
def CreateAI(pShip):
	#########################################
	import AI.Compound.CallDamageAI
	pCallDamageAI = AI.Compound.CallDamageAI.CreateAI(pShip)
	#########################################
	#########################################
	import AI.Compound.StarbaseAttack
	pStarbaseAttack = AI.Compound.StarbaseAttack.CreateAI(pShip, ["Warbird 1", "Warbird 2", "Warbird 3", "Warbird 4", "Warbird 5", 
	"Warbird 6", "Warbird 7", "Warbird8", "Warbird 9", "Warbird 10", "Warbird 11", "Warbird 12", "Warbird 13", "Warbird 14", 
	"Warbird 15", "Warbird 16", "Warbird 17", "Warbird 18", "Warbird 19", "Warbird 20", "Warbird 21", "Warbird 22", 
	"Warbird 23", "Warbird 24", "Warbird 25", "Warbird 26", "Warbird 27", "Warbird 28", "Warbird 29", "Warbird 30"])
	#########################################
	#########################################
	pStarbase12AI = App.PriorityListAI_Create(pShip, "Starbase12AI")
	pStarbase12AI.SetInterruptable(1)
	pStarbase12AI.AddAI(pCallDamageAI, 1)
	pStarbase12AI.AddAI(pStarbaseAttack, 2)
	#########################################
	return pStarbase12AI

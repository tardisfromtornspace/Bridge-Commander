import App
def CreateAI(pShip):
	#########################################
	import AI.Compound.CallDamageAI
	pCallDamageAI = AI.Compound.CallDamageAI.CreateAI(pShip)
	#########################################
	#########################################
	import AI.Compound.StarbaseAttack
	pStarbaseAttack = AI.Compound.StarbaseAttack.CreateAI(pShip, ["Vorcha 1", "Vorcha 2", "Vorcha 3", "Vorcha 4", "Vorcha 5", 
	"Vorcha 6", "Vorcha 7", "Vorcha8", "Vorcha 9", "Vorcha 10", "Vorcha 11", "Vorcha 12", "Vorcha 13", "Vorcha 14", 
	"Vorcha 15", "Vorcha 16", "Vorcha 17", "Vorcha 18", "Vorcha 19", "Vorcha 20", "Vorcha 21", "Vorcha 22", 
	"Vorcha 23", "Vorcha 24", "Vorcha 25", "Vorcha 26", "Vorcha 27", "Vorcha 28", "Vorcha 29", "Vorcha 30"])
	#########################################
	#########################################
	pStarbase12AI = App.PriorityListAI_Create(pShip, "Starbase12AI")
	pStarbase12AI.SetInterruptable(1)
	pStarbase12AI.AddAI(pCallDamageAI, 1)
	pStarbase12AI.AddAI(pStarbaseAttack, 2)
	#########################################
	return pStarbase12AI

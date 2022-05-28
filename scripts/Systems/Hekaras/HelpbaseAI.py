import App
def CreateAI(pShip):
	#########################################
	import AI.Compound.CallDamageAI
	pCallDamageAI = AI.Compound.CallDamageAI.CreateAI(pShip)
	#########################################
	#########################################
	import AI.Compound.StarbaseAttack
	pStarbaseAttack = AI.Compound.StarbaseAttack.CreateAI(pShip, [App.ObjectGroup_FromModule("QuickBattle.QuickBattle", "pEnemies")])
	#########################################
	#########################################
	pGessiksBaseAI = App.PriorityListAI_Create(pShip, "GessiksBaseAI")
	pGessiksBaseAI.SetInterruptable(1)
	pGessiksBaseAI.AddAI(pCallDamageAI, 1)
	pGessiksBaseAI.AddAI(pStarbaseAttack, 2)
	#########################################
	return pGessiksBaseAI

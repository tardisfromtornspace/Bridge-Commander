import App
def CreateAI(pShip):
	#########################################
	import AI.Compound.CallDamageAI
	pCallDamageAI = AI.Compound.CallDamageAI.CreateAI(pShip)
	#########################################
	#########################################
	import AI.Compound.StarbaseAttack
	pStarbaseAttack = AI.Compound.StarbaseAttack.CreateAI(pShip, [App.ObjectGroup_FromModule("QuickBattle.QuickBattle", "pFriendlies"), App.ObjectGroup_FromModule("QuickBattle.QuickBattle", "pEnemies")])
	#########################################
	#########################################
	pVgerAI = App.PriorityListAI_Create(pShip, "VgerAI")
	pVgerAI.SetInterruptable(1)
	pVgerAI.AddAI(pCallDamageAI, 1)
	pVgerAI.AddAI(pStarbaseAttack, 2)
	#########################################
	return pVgerAI

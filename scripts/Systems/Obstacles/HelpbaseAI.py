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
	pHelpbaseAI = App.PriorityListAI_Create(pShip, "HelpbaseAI")
	pHelpbaseAI.SetInterruptable(1)
	pHelpbaseAI.AddAI(pCallDamageAI, 1)
	pHelpbaseAI.AddAI(pStarbaseAttack, 2)
	#########################################
	return pHelpbaseAI

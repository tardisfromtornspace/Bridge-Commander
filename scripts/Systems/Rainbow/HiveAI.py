import App
import MissionLib
def CreateAI(pShip):
	#########################################
	import AI.Compound.CallDamageAI
	pCallDamageAI = AI.Compound.CallDamageAI.CreateAI(pShip)
	#########################################
	#########################################
	import AI.Compound.StarbaseAttack
        pFriendlies = MissionLib.GetFriendlyGroup()
        pEnemies = MissionLib.GetEnemyGroup()
        if not pFriendlies.GetNameTuple():
                pFriendlies.AddName("This ship probably wont exist")
        if not pEnemies.GetNameTuple():
                pEnemies.AddName("This ship probably wont exist")
	pStarbaseAttack = AI.Compound.StarbaseAttack.CreateAI(pShip, pFriendlies, pEnemies)
	#########################################
	#########################################
	pHiveAI = App.PriorityListAI_Create(pShip, "HiveAI")
	pHiveAI.SetInterruptable(1)
	pHiveAI.AddAI(pCallDamageAI, 1)
	pHiveAI.AddAI(pStarbaseAttack, 2)
	#########################################
	return pHiveAI

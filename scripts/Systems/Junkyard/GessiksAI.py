import App
import MissionLib

def CreateAI(pShip):
	pFriendlies = MissionLib.GetFriendlyGroup()
	pEnemies = MissionLib.GetEnemyGroup()
        if not pFriendlies.GetNameTuple():
            pFriendlies.AddName("This ship probably wont exist")
        if not pEnemies.GetNameTuple():
            pEnemies.AddName("This ship probably wont exist")
	#########################################
	import AI.Compound.CallDamageAI
	pCallDamageAI = AI.Compound.CallDamageAI.CreateAI(pShip)
	#########################################
	#########################################
	import AI.Compound.StarbaseAttack
	pStarbaseAttack = AI.Compound.StarbaseAttack.CreateAI(pShip, [pFriendlies, pEnemies])
	#########################################
	#########################################
	pGessiksAI = App.PriorityListAI_Create(pShip, "GessiksAI")
	pGessiksAI.SetInterruptable(1)
	pGessiksAI.AddAI(pCallDamageAI, 1)
	pGessiksAI.AddAI(pStarbaseAttack, 2)
	#########################################
	return pGessiksAI

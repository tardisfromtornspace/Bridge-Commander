import App
def CreateAI(pShip):
	#########################################
	# Creating CompoundAI CallDamageAI at (281, 186)
	import AI.Compound.CallDamageAI
	pCallDamageAI = AI.Compound.CallDamageAI.CreateAI(pShip)
	# Done creating CompoundAI CallDamageAI
	#########################################
	#########################################
	# Creating CompoundAI AttackEnemies at (297, 148)
	import AI.Compound.BasicAttack
	pAttackEnemies = AI.Compound.BasicAttack.CreateAI(pShip, App.ObjectGroup_FromModule("Maelstrom.Episode7.E7M1.E7M1", "pEnemies"))
	# Done creating CompoundAI AttackEnemies
	#########################################
	#########################################
	# Creating PlainAI CircleStarbase at (313, 110)
	pCircleStarbase = App.PlainAI_Create(pShip, "CircleStarbase")
	pCircleStarbase.SetScriptModule("CircleObject")
	pCircleStarbase.SetInterruptable(1)
	pScript = pCircleStarbase.GetScriptInstance()
	pScript.SetFollowObjectName("Starbase 12")
	pScript.SetRoughDistances(400, 450)
	pScript.SetNearFacingVector( App.TGPoint3_GetModelRight() )
	# Done creating PlainAI CircleStarbase
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (113, 38)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (273, 46)
	pPriorityList.AddAI(pCallDamageAI, 1)
	pPriorityList.AddAI(pAttackEnemies, 2)
	pPriorityList.AddAI(pCircleStarbase, 3)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (30, 58)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pPriorityList)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	return pAvoidObstacles

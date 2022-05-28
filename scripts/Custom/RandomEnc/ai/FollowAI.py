import App

def CreateAI(pShip):
	import MissionLib
	pPlayer = MissionLib.GetPlayer()
	#########################################
	# Creating PlainAI FollowPlayer at (325, 106)
	pFollowPlayer = App.PlainAI_Create(pShip, "FollowPlayer")
	pFollowPlayer.SetScriptModule("FollowObject")
	pFollowPlayer.SetInterruptable(1)
	pScript = pFollowPlayer.GetScriptInstance()
	pScript.SetFollowObjectName(pPlayer.GetName())
	# Done creating PlainAI FollowPlayer
	#########################################
	#########################################
	# Creating CompoundAI FollowThroughWarp at (452, 116)
	import AI.Compound.FollowThroughWarp
	pFollowThroughWarp = AI.Compound.FollowThroughWarp.CreateAI(pShip, pPlayer.GetName(), FollowToSB12 = 1, FollowThroughMissions = 1)
	# Done creating CompoundAI FollowThroughWarp
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (202, 170)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (376, 284)
	pPriorityList.AddAI(pFollowPlayer, 1)
	pPriorityList.AddAI(pFollowThroughWarp, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (78, 219)
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

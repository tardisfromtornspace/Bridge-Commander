import App

def CreateAI(pShip):
	#########################################
	# Creating CompoundAI FollowThroughWarp at (143, 199)
	import AI.Compound.FollowThroughWarp
	import MissionLib
	pPlayer = MissionLib.GetPlayer()
	pFollowThroughWarp = AI.Compound.FollowThroughWarp.CreateAI(pShip, pPlayer.GetName(), FollowToSB12 = 1, FollowThroughMissions = 1)
	# Done creating CompoundAI FollowThroughWarp
	#########################################
	#########################################
	# Creating CompoundAI QuickBattleFriendlyAI at (276, 65)
	import QuickBattleFriendlyAI
	pQuickBattleFriendlyAI = QuickBattleFriendlyAI.CreateAI(pShip, 0.5, 0)
	# Done creating CompoundAI QuickBattleFriendlyAI
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (75, 119)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (185, 127)
	pPriorityList.AddAI(pFollowThroughWarp, 1)
	pPriorityList.AddAI(pQuickBattleFriendlyAI, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (13, 205)
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

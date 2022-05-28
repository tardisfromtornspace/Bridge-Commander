# by USS Sovereign


import App
import MissionLib

def CreateAI(pShip):
        pMission = MissionLib.GetMission ()
	pEnemyGroup = pMission.GetEnemyGroup ()
	#########################################
	# Creating CompoundAI DS9FXGenericStaticAI at (214, 166)
	import AI.Compound.FedAttack
	pDS9FXGenericStaticAI = AI.Compound.FedAttack.CreateAI(pShip, pEnemyGroup)
	# Done creating CompoundAI DS9FXGenericStaticAI
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (207, 236)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pDS9FXGenericStaticAI)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	return pAvoidObstacles

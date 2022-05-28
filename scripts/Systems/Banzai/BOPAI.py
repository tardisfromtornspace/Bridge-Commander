import App

def CreateAI(pShip):
	#########################################
	# Creating CompoundAI Attack at (306, 238)
	import AI.Compound.BasicAttack
	# Below are two lines showing two different ways to add targets to the AI.
	# the first uses a list (eveything in the brackets []), and the second gets
	# the list from the Custom.Campaign.Episode.Mission Globals.  They'll need to be
	# properly declared, though.  The latest patch to the BCMB does that.
	# This AI was modified from an Enemy AI I created to test the second line.
	# To change it back to an Enemy AI, just change "pFriendlies" to "pEnemies".
	#
	# -Jeff

	pAttack = AI.Compound.BasicAttack.CreateAI(pShip, ["Galor Gul", "Gul Damar"], FollowTargetThroughWarp = 1, SmartPhasers = 1, UseCloaking = 1)
	# pAttack = AI.Compound.BasicAttack.CreateAI(pShip, App.ObjectGroup_FromModule("Custom.Graveyard.Ep1.E1M0", "pEnemies"), FollowTargetThroughWarp = 1, SmartPhasers = 1, UseCloaking = 1)
	# Done creating CompoundAI Attack
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (74, 229)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pAttack)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	return pAvoidObstacles

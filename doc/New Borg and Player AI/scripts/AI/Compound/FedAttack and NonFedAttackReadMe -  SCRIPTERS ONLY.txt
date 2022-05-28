Changes to this file was necessary for the new Player AI to
function properly. If the new Player AI is used with any 
other mods that uses this same file, then the changes listed
below must be included, and by doing so, should not cause 
any conflicts between mods. These changes can only be made
using the AI Editor found in the SDK pack simply by just 
adding in the Avoid Obstacles Preprocess script.

pBuilderAI.AddDependency("PowerManagement", "AvoidObstacles")
-
-
-
-
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (x, xxx)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pFleeAttackOrFollow)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	######### AI Builder Begin #########
	return pAvoidObstacles  # Builder Return
	########## AI Builder End ##########
	######### AI Builder Begin #########
def BuilderCreatexx(pShip, pAvoidObstacles, dKeywords):
	########## AI Builder End ##########
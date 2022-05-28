#########################################################
#########################################################
##                                                     ##
##  Diamond BC - Redistribute Shields v1               ##
##  By MLeo Daalder                                    ##
##                                                     ##
##  This mod will prevent the game from freezing when  ##
##  RedistributeShields is called on a shield without  ##
##  uniform maximum shield vectors.                    ##
##                                                     ##
#########################################################
#########################################################

import App
import Appc
import new

App.ShieldClass.originalRedistributeShields = new.instancemethod(Appc.ShieldClass_RedistributeShields, None, App.ShieldClass)#App.ShieldClass.RedistributeShields
def ShieldClass_RedistributeShields(self):
	if not self.IsOn():
		# If we don't, then we will wreck our shields (that is, they will have a charge of 0)
		return

	lVectors = [0]*6

	vectorIndices = range(App.ShieldClass.NUM_SHIELDS)

	pProperty = self.GetProperty()
	for i in vectorIndices:
		lVectors[i] = self.GetMaxShields(i)
		pProperty.SetMaxShields(i, 1)
		self.SetCurShields(i, self.GetSingleShieldPercentage(i))

	self.originalRedistributeShields()

	for i in vectorIndices:
		max = lVectors[i]
		pProperty.SetMaxShields(i, max)
		self.SetCurShields(i, self.GetCurShields(i) * max)

App.ShieldClass.RedistributeShields = ShieldClass_RedistributeShields

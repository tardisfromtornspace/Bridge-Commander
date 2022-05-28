# by Defiant for KM

import Foundation

def __getstate__(self):
	self.Deactivate()
	dState = self.__dict__.copy()
	return dState

def __setstate__(self, dict):
	self.__dict__ = dict
	#self.Activate()

Foundation.OverrideDef.__getstate__ = __getstate__
Foundation.OverrideDef.__setstate__ = __setstate__

#
# ConditionUsingWeapon
#
# A condition that's hooked into the AI above it, that's true
# if the AI is trying to use the specified weapon type (it'll
# be fired if it's lined up), false if not.
#
import App
from bcdebug import debug

#NonSerializedObjects = ( "debug", )

#debug = App.CPyDebug(__name__).Print
#debug('Loading ' + __name__ + ' Condition module...')

class ConditionUsingWeapon:
	def __init__(self, pCodeCondition, eWeaponType):
		debug(__name__ + ", __init__")
		self.pCodeCondition = pCodeCondition
		self.eWeaponType = eWeaponType

		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		self.pModule = __import__(__name__)

		# Condition starts out false.
		self.pCodeCondition.SetStatus(0)

	def RegisterExternalFunctions(self, pAI):
		# AI will call the external "UsingWeaponType" function when it changes whether
		# or not it's trying to use torps.
		debug(__name__ + ", RegisterExternalFunctions")
		pAI.RegisterExternalFunction("UsingWeaponType", { "CodeID" : self.pCodeCondition.GetObjID(), "FunctionName" : "UsingWeaponType" })

	def UsingWeaponType(self, lWeapons):
		# External UsingWeaponType function has been called.  Check if any
		# of the weapon systems being used match self.eWeaponType.
		debug(__name__ + ", UsingWeaponType")
		for pWeapon in lWeapons:
			if pWeapon.IsTypeOf( self.eWeaponType ):
				self.pCodeCondition.SetStatus(1)
				return
		self.pCodeCondition.SetStatus(0)

	def __getstate__(self):
		debug(__name__ + ", __getstate__")
		dState = self.__dict__.copy()
		dState["pModule"] = self.pModule.__name__
		return dState

	def __setstate__(self, dict):
		debug(__name__ + ", __setstate__")
		self.__dict__ = dict
		self.pModule = __import__(self.pModule)

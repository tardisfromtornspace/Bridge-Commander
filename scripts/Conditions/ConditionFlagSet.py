#
# ConditionFlagSet
#
# This is true if the flag in the keyword dictionary given to it
# is true, false if it's either false or not present.
#
import App
from bcdebug import debug

#NonSerializedObjects = ( "debug", )

#debug = App.CPyDebug(__name__).Print
#debug("Loading " + __name__ + " Condition module...")

class ConditionFlagSet:
	def __init__(self, pCodeCondition, sFlagName, dKeywords):
		# Set our parameters...
		debug(__name__ + ", __init__")
		self.pCodeCondition = pCodeCondition

		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		self.pModule = __import__(__name__)

		if dKeywords.has_key(sFlagName)  and  dKeywords[sFlagName]:
			self.pCodeCondition.SetStatus(1)
		else:
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

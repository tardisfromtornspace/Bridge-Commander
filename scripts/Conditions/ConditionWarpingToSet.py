#
# ConditionWarpingToSet
#
# A condition that tests to see if an object is warping
# to a specified set.  If so, it's true.  If not, it's false.
# If no set is specified, this is true when the ship is
# warping, false when it's not warping.
#
import App
from bcdebug import debug

#NonSerializedObjects = ( "debug", )

#debug = App.CPyDebug(__name__).Print
#debug("Loading " + __name__ + " Condition module...")

class ConditionWarpingToSet:
	def __init__(self, pCodeCondition, sObjectName, sLongSetName = None):
		# Save our parameters.
		debug(__name__ + ", __init__")
		self.pCodeCondition = pCodeCondition
		self.sObject = sObjectName
		self.sSet = sLongSetName

		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		self.pModule = __import__(__name__)

		# Setup our event handlers, for checking when the warp
		# sequence is set for our object.
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)

		# We need to listen for ET_SET_WARP_SEQUENCE events.
		App.g_kEventManager.AddBroadcastPythonMethodHandler( App.ET_SET_WARP_SEQUENCE, self.pEventHandler, "SequenceSet" )

		# Check if we're true right now..  Might be, of our target is already warping.
		self.CheckState()

	def RegisterExternalFunctions(self, pAI):
		debug(__name__ + ", RegisterExternalFunctions")
		pAI.RegisterExternalFunction("SetTarget", { "CodeID" : self.pCodeCondition.GetObjID(), "FunctionName" : "SetTarget" })

	def SetTarget(self, sTarget):
		# Change the target we're watching.
		debug(__name__ + ", SetTarget")
		self.sObject = sTarget

		# Check if we're true right now..  Might be, of our target is already warping.
		self.CheckState()

	def __getstate__(self):
		debug(__name__ + ", __getstate__")
		dState = self.__dict__.copy()
		dState["pModule"] = self.pModule.__name__
		dState["pEventHandler"].pContainingInstance = self
		return dState

	def __setstate__(self, dict):
		debug(__name__ + ", __setstate__")
		self.__dict__ = dict
		self.pModule = __import__(self.pModule)
		del self.pEventHandler.pContainingInstance

	def CheckState(self):
		# Get our ship.
		debug(__name__ + ", CheckState")
		pShip = App.ShipClass_GetObject(None, self.sObject)
		if pShip:
			pWarpSystem = pShip.GetWarpEngineSubsystem()
			if pWarpSystem:
				pSequence = App.WarpSequence_Cast( pWarpSystem.GetWarpSequence() )

				self.SetStateFromSequence( pSequence )

	def SequenceSet(self, pEvent):
		# Get the ship that this event is going to..
		debug(__name__ + ", SequenceSet")
		pWarpSystem = App.WarpEngineSubsystem_Cast( pEvent.GetDestination() )
		pShip = pWarpSystem.GetParentShip()
		
		# Is it the ship we care about?
		if pShip.GetName() == self.sObject:
			# Yep..  Get the warp sequence.
			pSequence = App.WarpSequence_Cast( pWarpSystem.GetWarpSequence() )

			self.SetStateFromSequence(pSequence)
		debug(__name__ + ", SequenceSet END")

	def SetStateFromSequence(self, pWarpSequence):
		# Set our state based on which region the ship is warping into.
		debug(__name__ + ", SetStateFromSequence")
		if pWarpSequence and ((not self.sSet)  or  (pWarpSequence.GetDestination() == self.sSet)):
			self.pCodeCondition.SetStatus(1)
		else:
			self.pCodeCondition.SetStatus(0)

#
# ConditionReachedWaypoint
#
# A condition that's false until the specified ship reaches
# the specified waypoint.
#
import App
from bcdebug import debug

#kDebugObj = App.CPyDebug()
#kDebugObj.Print('Loading ' + __name__ + ' Condition module...')

class ConditionReachedWaypoint:
	def __init__(self, pCodeCondition, sShipName, sWaypointName):
		# Set the time we wait..
		debug(__name__ + ", __init__")
		self.pCodeCondition = pCodeCondition
		self.sShip = sShipName
		self.sWaypoint = sWaypointName

		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		self.pModule = __import__(__name__)

		# Our initial state is false.
		self.pCodeCondition.SetStatus(0)

		# Setup our interrupt handler, triggered when the
		# waypoint event goes off.
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)

		App.g_kEventManager.AddBroadcastPythonMethodHandler( App.ET_AI_REACHED_WAYPOINT, self.pEventHandler, "EventTriggered")

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

	def EventTriggered(self, pEvent):
		# Check if the destination matches the ship we're watching.
#		kDebugObj.Print(__name__ + ".EventTriggered")
		debug(__name__ + ", EventTriggered")
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		if (pShip != None):
#			kDebugObj.Print(__name__ + ": Ship(%s) reached(%s)" % (pShip.GetName(), pEvent.GetPlacement().GetName()))
			if pShip.GetName() == self.sShip:
				# Matched the ship.  Does this match
				# the waypoint?
				pPlacement = pEvent.GetPlacement()
				if pPlacement.GetName() == self.sWaypoint:
					# Yep, it matches.  Mark us True.
#					kDebugObj.Print(__name__ + ": True, true")
					self.pCodeCondition.SetStatus(1)

		self.pEventHandler.CallNextHandler(pEvent)

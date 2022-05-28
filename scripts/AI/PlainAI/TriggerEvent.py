from bcdebug import debug
#
# TriggerEvent
#
# Trigger an event.
#
import App
import BaseAI

#NonSerializedObjects = ( "debug", )

#debug = App.CPyDebug(__name__).Print
#debug("Loading " + __name__ + " AI module...")

class TriggerEvent(BaseAI.BaseAI):
	def __init__(self, pCodeAI):
		# Parent class constructor first...
		debug(__name__ + ", __init__")
		BaseAI.BaseAI.__init__(self, pCodeAI)

		# Set default values for parameters that have them.
		self.SetupDefaultParams()
		self.SetRequiredParams( ( "pEvent", "SetEvent" ) )
		self.SetExternalFunctions()

		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		self.pModule = __import__(__name__)

	# Set the name of the object we're fleeing from
	def SetEvent(self, pEvent): #AISetup
		self.pEvent = pEvent

	def GetNextUpdateTime(self):
		# We want to be updated immediately.
		debug(__name__ + ", GetNextUpdateTime")
		return 0

	def Update(self):
		debug(__name__ + ", Update")
		"Do our stuff"
		# Trigger our event.
		App.g_kEventManager.AddEvent(self.pEvent)

		# That's it.  We're done.
		return App.ArtificialIntelligence.US_DONE

#
# ConditionTimer
#
# A condition that's true once a specified amount of time has
# passed.  Time is specified in seconds.
#
import App
from bcdebug import debug

#kDebugObj = App.CPyDebug()
#kDebugObj.Print('Loading ' + __name__ + ' Condition module...')

class ConditionTimer:
	def __init__(self, pCodeCondition, fDelay, bResetOnActivate = 1):
		# Set the time we wait..
		debug(__name__ + ", __init__")
		self.fDelay = fDelay
		self.bResetOnActivate = bResetOnActivate
		self.pCodeCondition = pCodeCondition

		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		self.pModule = __import__(__name__)

		# Our initial state is false.
		self.pCodeCondition.SetStatus(0)

		# Setup our interrupt handler, triggered when our timer
		# goes off.
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)

		self.pEventHandler.AddPythonMethodHandlerForInstance( App.ET_AI_TIMER, "TimerTriggered" )
		
		# Setup our timer.
		self.SetupTimer()
	
	def __del__(self):
		debug(__name__ + ", __del__")
		if (self.pTimer != None):
			App.g_kTimerManager.DeleteTimer(self.pTimer.GetObjID())
			self.pTimer = None

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

	def SetupTimer(self):
		debug(__name__ + ", SetupTimer")
		pEvent = App.TGEvent_Create()
		pEvent.SetEventType(App.ET_AI_TIMER)
		pEvent.SetDestination(self.pEventHandler)
		
		self.pTimer = App.TGTimer_Create()
		self.pTimer.SetEvent(pEvent)
		self.pTimer.SetTimerStart( App.g_kUtopiaModule.GetGameTime() + self.fDelay )
		
		App.g_kTimerManager.AddTimer(self.pTimer)

	def Activate(self):
		debug(__name__ + ", Activate")
		if self.bResetOnActivate:
			# Reset our timer.
			if not self.pTimer:
				# Our timer must have been triggered.  Recreate
				# and reset it.
				self.SetupTimer()
			else:
				# Our timer already exists.  We just need
				# to change its time.
				App.g_kTimerManager.RemoveTimer(self.pTimer.GetObjID())
				self.pTimer.SetTimerStart( App.g_kUtopiaModule.GetGameTime() + self.fDelay )
				App.g_kTimerManager.AddTimer(self.pTimer)
				
			# The timer is running again, so we're false.
			self.pCodeCondition.SetStatus(0)

	def TimerTriggered(self, pEvent):

		debug(__name__ + ", TimerTriggered")
		pObject = App.ConditionScript_Cast(App.TGObject_GetTGObjectPtr(self.pCodeCondition.GetObjID()))
		
		if pObject:
			self.pCodeCondition.SetStatus(1)
		self.pTimer = None

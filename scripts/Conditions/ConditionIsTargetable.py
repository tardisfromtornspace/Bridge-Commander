#
# ConditionMissionEvent
#
# A condition that's false until an event type is triggered,
# after which it remains true.
#
import App
from bcdebug import debug

#kDebugObj = App.CPyDebug()
#kDebugObj.Print('Loading ' + __name__ + ' Condition module...')

class ConditionIsTargetable:
	def __init__(self, pCodeCondition, pShip, sInitialTarget, pAllTargetsGroup):
		# Set the time we wait..
                
		debug(__name__ + ", __init__")
		pSet = pShip.GetContainingSet()
		self.pTarget = App.ShipClass_GetObject(pSet, sInitialTarget)
                self.pCodeCondition = pCodeCondition
                self.pShip = pShip
		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		self.pModule = __import__(__name__)

		# Our initial state is false.
		self.pCodeCondition.SetStatus(0)

		# Setup a process to update us..
		self.pTimerProcess = None
                self.myTimerDelay = 5.0
		self.SetupTimer()

	def __getstate__(self):
		debug(__name__ + ", __getstate__")
		dState = self.__dict__.copy()
		dState["pModule"] = self.pModule.__name__
		dState["pTimerProcess"] = (self.pTimerProcess is not None)
		return dState

	def __setstate__(self, dict):
		debug(__name__ + ", __setstate__")
		self.__dict__ = dict
		self.pModule = __import__(self.pModule)

		if self.pTimerProcess:
			self.pTimerProcess = None
			self.SetupTimer()
		else:
			self.pTimerProcess = None

	def EvaluateTargetable(self, dEndTime = 0.0):
                debug(__name__ + ", EvaluateTargetable")
                if not self.pTarget:
                        self.UpdateTimerDelay(5.0)
                        return
                if self.pTarget.IsDead():
                        self.UpdateTimerDelay(5.0)
                        return
                pShipTarget = self.pShip.GetTarget()
                if pShipTarget:
                        if pShipTarget.GetName() != self.pTarget.GetName():
                                self.UpdateTimerDelay(5.0)
                                return
                print("check", self.pTarget.IsTargetable(), self.pCodeCondition.GetStatus())
                if self.pCodeCondition.GetStatus() == 1:
                        self.pCodeCondition.SetStatus(0)
                        return
                if self.pTarget.IsTargetable() == 0:
                        print (self.pShip.GetName(), "stop attacking", self.pTarget.GetName())
                        self.UpdateTimerDelay(0.1)
                        self.pCodeCondition.SetStatus(1)
                else:
                        self.pCodeCondition.SetStatus(0)

	def SetupTimer(self):
		debug(__name__ + ", SetupTimer")
		if self.pTimerProcess is not None:
			# We already have a timer.
			return

		self.pTimerProcess = App.PythonMethodProcess()
		self.pTimerProcess.SetInstance(self)
		self.pTimerProcess.SetFunction("EvaluateTargetable")
		self.pTimerProcess.SetDelay(self.myTimerDelay)
		self.pTimerProcess.SetPriority(App.TimeSliceProcess.LOW)

        def UpdateTimerDelay(self, newDelay):
                debug(__name__ + ", UpdateTimerDelay")
                self.myTimerDelay = newDelay
                self.pTimerProcess.SetDelay(self.myTimerDelay)

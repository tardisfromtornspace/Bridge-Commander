#
# ConditionTargetWarping
#
# A condition that returns true if the given object is warping.
#
import App
from bcdebug import debug

#NonSerializedObjects = ( "debug", )

#debug = App.CPyDebug(__name__).Print
#debug("Loading " + __name__ + " Condition module...")

class ConditionTargetWarping:
	def __init__(self, pCodeCondition, sObjectName, sShipName = ""):
		debug(__name__ + ", __init__")
		self.pCodeCondition = pCodeCondition
		# Set our primary object's name..
		self.sObjectName = sObjectName
		self.sShipName = sShipName

		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		self.pModule = __import__(__name__)

		# Setup our interrupt handlers, for checking of the object
		# enters or leaves the set.
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)

		self.pEventHandler.AddPythonMethodHandlerForInstance( App.ET_ENTERED_SET, "EnteredSet" )
		##self.pEventHandler.AddPythonMethodHandlerForInstance( App.ET_EXITED_SET, "ExitedSet" )
		self.SetState()

	def RegisterExternalFunctions(self, pAI):
		debug(__name__ + ", RegisterExternalFunctions")
		pAI.RegisterExternalFunction("SetTarget", { "CodeID" : self.pCodeCondition.GetObjID(), "FunctionName" : "SetTarget" })

	def SetTarget(self, sTarget):
		# Target changed
		debug(__name__ + ", SetTarget")
		self.sObjectName = sTarget
		self.SetState()

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

	def SetState(self):
		debug(__name__ + ", SetState")
		if self.sShipName != "":
			pObj = App.ObjectClass_GetObject( None, self.sShipName )
		else:
			pObj = None
		pTargObj = App.ObjectClass_GetObject( None, self.sObjectName)

		#pShip = None
		#pTarget = None
		#if pObj != None and pTargObj != None:
		#	pShip = App.ShipClass_Cast(pObj)
		#	pTarget = App.ShipClass_Cast(pTargObj)

		#if pShip != None and pTarget != None:
		#	pChaser = App.g_kTravelManager.CreateChaser(pShip, pTarget)
		#	if pChaser.Target == None:
		#		pChaser.SetTarget(pTarget)
		#	elif pChaser.Target.GetObjID() != pTarget.GetObjID():
		#		pChaser.SetTarget(pTarget)

		bStatus = 0
		### The following 4 lines of code were commented so that this condition never returns TRUE, thus making the
		### FollowThroughWarp CompoundAI never actually reaching the point of initiating warp.
		### Instead, what will happen is that this condition will also initiate and update the Chaser object of this
		### ship, and it'll then control if a ship follows her target.
		if pTargObj:
			pTravel = App.g_kTravelManager.GetTravel(pTargObj)
			if pTravel:
				bStatus = pTravel.IsTravelling()
		self.pCodeCondition.SetStatus(bStatus)

	def EnteredSet(self, pObjEvent):
		# Get the object...
		#pObj = App.ObjectClass_Cast(pObjEvent.GetObjPtr())
		#sSetName = pObj.GetContainingSet().GetName()
		debug(__name__ + ", EnteredSet")
		self.SetState()
		# Call the next handler for this event...
		self.pEventHandler.CallNextHandler(pObjEvent)

	def ExitedSet(self, pObjEvent):
		# Get the object...
		#pObj = App.ObjectClass_Cast(pObjEvent.GetObjPtr())
		debug(__name__ + ", ExitedSet")
		self.SetState()
		# Call the next handler for this event...
		self.pEventHandler.CallNextHandler(pObjEvent)

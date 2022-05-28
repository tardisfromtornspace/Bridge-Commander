from bcdebug import debug
#
# RunScript
#
# Call a script.
#
import App
import BaseAI

#NonSerializedObjects = ( "debug", )

#debug = App.CPyDebug(__name__).Print
#debug("Loading " + __name__ + " AI module...")

class RunScript(BaseAI.BaseAI):
	def __init__(self, pCodeAI):
		# Parent class constructor first...
		debug(__name__ + ", __init__")
		BaseAI.BaseAI.__init__(self, pCodeAI)

		# Set default values for parameters that have them.
		self.SetupDefaultParams(
			self.SetArguments,
			self.SetRepeatTime)
		self.SetRequiredParams(
			( "sModuleName", "SetScriptModule" ),
			( "sFunctionName", "SetFunction" ) )
		self.SetExternalFunctions()

		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		self.pModule = __import__(__name__)

	def SetScriptModule(self, sModuleName): #AISetup
		self.sModuleName = sModuleName

	def SetFunction(self, sFunctionName): #AISetup
		self.sFunctionName = sFunctionName

	def SetArguments(self, *lArguments): #AISetup
		self.lArguments = lArguments

	def SetRepeatTime(self, fRepeatTime = -1): #AISetup
		self.fRepeatTime = fRepeatTime





	def GetStatusInfo(self):
		debug(__name__ + ", GetStatusInfo")
		return "Module(%s), Function(%s), RepeatTime(%f), Arguments(%s)" % (
			self.sModuleName, self.sFunctionName, self.fRepeatTime, self.lArguments)

	def GetNextUpdateTime(self):
		debug(__name__ + ", GetNextUpdateTime")
		if self.fRepeatTime >= 0:
			return self.fRepeatTime
		return 1.0

	def Update(self):
		debug(__name__ + ", Update")
		"Do our stuff"
		# Call the script.
                try:
		        pModule = __import__(self.sModuleName)
		        pFunction = getattr(pModule, self.sFunctionName)
                except:
                        return App.ArtificialIntelligence.US_DONE

		apply(pFunction, self.lArguments)

		# If our repeat time is >= 0, we repeat forever; return
		# Active.  Otherwise, return Done.
		if self.fRepeatTime >= 0:
			return App.ArtificialIntelligence.US_ACTIVE
		return App.ArtificialIntelligence.US_DONE

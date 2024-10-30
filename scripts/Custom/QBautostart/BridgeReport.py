from bcdebug import debug
import App
import Lib.LibEngineering
from Libs.LibQBautostart import *
from conf.CrewReports import dReports, dNameToType

MODINFO = {     "Author": "\"Defiant\" erik@bckobayashimaru.de",
                "needBridge": 1
            }


g_pSayTimer = None

NonSerializedObjects = (
"g_pSayTimer"
)

def SaySomething(pCharacter):
	if not pCharacter:
		return
	if not dReports.has_key(pCharacter.GetCharacterName()):
		return
	lList = dReports[pCharacter.GetCharacterName()]
	iLen = len(lList)
	if iLen == 0:
		return
	lPlay = lList[App.g_kSystemWrapper.GetRandomNumber(iLen)]
	sDatabase = lPlay[0]
	sItem = lPlay[1]
	print sDatabase, sItem

	Say(sItem, dNameToType[pCharacter.GetCharacterName()], sDatabase)


def NothingToAdd(pObject, pEvent):
	debug(str(__name__) + ", NothingToAdd")
	# First, see if we should work with the thing that sent the event
	pCharacter = App.CharacterClass_Cast(pObject)
	if not (pCharacter):
		# Next, try the event as a string event
		pBridge = App.g_kSetManager.GetSet("bridge")
		pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
		kString = pDatabase.GetString("Communicate")
		App.g_kLocalizationManager.Unload(pDatabase)
		pEvent.GetString(kString)
		pCharacter = App.CharacterClass_GetObject(pBridge, kString.GetCString())
		if not (pCharacter):
			# Try in Engineering...
			pBridge = App.g_kSetManager.GetSet("Engineering")
			pCharacter = App.CharacterClass_GetObject(pBridge, kString.GetCString())

		if not (pCharacter):
			# No character of that name, give up
			pObject.CallNextHandler(pEvent)
			return

	# Have the character say "Nothing to add"
	if chance(10):
		# 10% chance to play usual stuff
		pCharacter.SpeakLine(pCharacter.GetDatabase(), pCharacter.GetCharacterName() + "NothingToAdd")
	else:
		SaySomething(pCharacter)


class SayTimer:
	def __init__(self):
		debug(__name__ + ", __init__")
		self.pTimerProcess = None
		self.SetupTimer()

        def SetupTimer(self):
                debug(__name__ + ", SetupTimer")
                if self.pTimerProcess:
                        # We already have a timer.
                        return

		self.pTimerProcess = App.PythonMethodProcess()
		self.pTimerProcess.SetInstance(self)
		self.pTimerProcess.SetFunction("Update")
		self.pTimerProcess.SetPriority(App.TimeSliceProcess.LOW)
		self.SetDelay()
		
	def SetDelay(self):
		debug(__name__ + ", SetDelay")
		self.pTimerProcess.SetDelay(60 + App.g_kSystemWrapper.GetRandomNumber(60))
	
	def Update(self, dTimeAvailable):
		debug(__name__ + ", Update")
		self.SetDelay()
		pBridge = App.g_kSetManager.GetSet("bridge")

		# get time of last talk
		iLowestTime = 60
		for sName in dNameToType.values():
			pCharacter = App.CharacterClass_GetObject(pBridge, sName)
			if pCharacter:
				iLast = App.g_kUtopiaModule.GetGameTime() - pCharacter.GetLastTalkTime()
				if iLast < iLowestTime:
					iLowestTime = iLast
		if iLowestTime > 30: # after > 30 seconds ago
			# Time to talk again
			l = dNameToType.values()
			iLen = len(l)
			if iLen == 0:
				return
			sCharacter = l[App.g_kSystemWrapper.GetRandomNumber(iLen)]
			pCharacter = App.CharacterClass_GetObject(pBridge, sCharacter)
			SaySomething(pCharacter)


def init():
	global g_pSayTimer
	
        if Lib.LibEngineering.CheckActiveMutator("Random Crew Reports"):
		g_pSayTimer = SayTimer()

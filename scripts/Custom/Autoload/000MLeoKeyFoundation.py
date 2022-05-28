from bcdebug import debug
import App
import Foundation

LoadedConfig = 0


class KeyConfig(Foundation.OverrideDef):
	def __init__(self, KeyName, EventName, EventKey = 0, KeyEventType = 0, KeyEventVal = 0, Panel = "Misc", dict = {}):
		debug(__name__ + ", __init__")
		self.name = __name__ + "." + str(App.g_kUtopiaModule.GetGameTime())
		self.KeyName = KeyName
		self.Panel = Panel
		self.EventName = EventName
		if EventKey:
			self.EventKey = EventKey
		else:
			self.EventKey = MakeUniqueID(EventName)
		#print EventName, self.EventKey
		self.KeyEventType = KeyEventType
		self.KeyEventVal = KeyEventVal
		self.dict = dict
		Foundation.OverrideDef.__init__(self, self.name, None, None, dict)

	def GetKeyName(self):
		debug(__name__ + ", GetKeyName")
		return self.KeyName

	def GetEvent(self):
		debug(__name__ + ", GetEvent")
		return self.EventKey

	def GetEventType(self):
		debug(__name__ + ", GetEventType")
		return self.KeyEventType

	def GetEventTypeVal(self):
		debug(__name__ + ", GetEventTypeVal")
		return self.KeyEventVal

	def GetEventName(self):
		debug(__name__ + ", GetEventName")
		return self.EventName

	def IsEnabled(self):
		debug(__name__ + ", IsEnabled")
		if(self.dict.has_key("modes")):
			return self.dict["modes"][0].IsEnabled()
		return 0

	def _SwapInModules(self, pre, post):		pass
	def _SwapOutModules(self, pre, post):		pass

	def __call__(self, pObject, pEvent, dict = {}):
		debug(__name__ + ", __call__")
		pass

	def Activate(self):				pass
	def Deactivate(self):				pass

	def Unbind(self):
		App.g_kKeyboardBinding.ClearBinding(self.EventKey, self.KeyEventType, self.KeyEventVal)


class KeyConfigBucket:
	debug(__name__ + ", Deactivate")
	def __init__(self):
		debug(__name__ + ", __init__")
		self.Subs = []

#	def __del__(self):
#		self.Subs = []

	def AddKeyConfig(self, add):
		debug(__name__ + ", AddKeyConfig")
		if add in self.Subs:
			for posAdd in self.Subs:
				if posAdd.KeyName == add.KeyName:
					posAdd.EventKey = add.EventKey
					break
		else:
			self.Subs.append(add)
		return add.GetEvent()

	def UnbindAll(self):
		for add in self.Subs:
			add.Unbind()

	def GetByString(self, pString):
		debug(__name__ + ", GetByString")
		for Sub in self.Subs:
			if(Sub.EventName == pString):
				return Sub
		return None

	def CheckString(self, pString):
		debug(__name__ + ", CheckString")
		global LoadedConfig
		if(LoadedConfig == 0):
			Foundation.LoadConfig()
			LoadedConfig = 1

		for Sub in self.Subs:
			if(Sub.EventName == pString and Sub.IsEnabled() == 1):
				return 1
		return 0

	def GetEventByString(self, pString):
		debug(__name__ + ", GetEventByString")
		if(self.CheckString(pString)):
			return self.GetByString(pString).GetEvent()

	def GetEventTypeByString(self, pString):
		debug(__name__ + ", GetEventTypeByString")
		if(self.CheckString(pString)):
			return self.GetByString(pString).GetEventType()

	def GetEventTypeValByString(self, pString):
		debug(__name__ + ", GetEventTypeValByString")
		if(self.CheckString(pString)):
			return self.GetByString(pString).GetEventTypeVal()

	def GetSubsForPanel(self, sPanel):
		debug(__name__ + ", GetSubsForPanel")
		list = []
		for Sub in self.Subs:
			if(Sub.Panel == sPanel and Sub.IsEnabled() == 1):
				list.append(Sub)
		return list


g_kKeyBucket = KeyConfigBucket()


Foundation.g_kKeyBucket = g_kKeyBucket
Foundation.KeyConfig = KeyConfig



def MakeUniqueID(name):
	debug(__name__ + ", MakeUniqueID")
	return App.Mission_GetNextEventType()
	retval = 0
	for char in name:
		retval = retval + ord(char)
	retval = (retval + len(name)) * len(name) * (retval + len(name)) * len(name)
	return retval

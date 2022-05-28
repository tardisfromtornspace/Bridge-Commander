import App

FALSE=0
TRUE=1

class ATP_Wrapper:
	Dict={}
	EventDict = {}
	ID=0
	
	def __init__(self):
		import math
		#assign an unique ID
		ID=0		
		while (TRUE):
			ID=ID+1
			if not ATP_Wrapper.Dict.has_key(ID):
				break

		self.ID=ID
		self.vLoc=App.TGPoint3()
		self.vLoc.SetXYZ(0.0,0.0,0.0)
		self.Random=0.5+0.5*math.cos(1000.0/math.pi*self.ID)
		self.Node=None
		self.sName="Object__"+str(self.ID)

		self.Wrapper = App.TGPythonInstanceWrapper()
		self.Wrapper.SetPyWrapper(self)

		self.timers={}
		self.handlers=[]

		ATP_Wrapper.Dict[self.ID]=self
		
	def AddHandler(self,eventType,sFunctionHandler):
		## Dict
		EventDict = ATP_Wrapper.EventDict

		## Wrapper event
		self.Wrapper.RemoveHandlerForInstance(eventType,sFunctionHandler)
		self.Wrapper.AddPythonMethodHandlerForInstance(eventType,sFunctionHandler)
		
		## Game Event
		App.g_kEventManager.RemoveBroadcastHandler(eventType,App.Game_GetCurrentGame(),__name__+".Redirect")
		App.g_kEventManager.AddBroadcastPythonFuncHandler(eventType,App.Game_GetCurrentGame(),__name__+".Redirect")

		if self.handlers.count((eventType,sFunctionHandler))==0:
			self.handlers.append((eventType,sFunctionHandler))

		## Indirect call mechanism
		if not EventDict.has_key(eventType):
			EventDict[eventType] = []
		if EventDict[eventType].count(self.Wrapper)==0:
			EventDict[eventType].append(self.Wrapper)
			
	def RemoveHandler(self,e,sFunctionHandler):
		## Dict
		EventDict = ATP_Wrapper.EventDict
		
		## Remove instances
		self.Wrapper.RemoveHandlerForInstance(e,sFunctionHandler)				
		self.handlers.remove((e,sFunctionHandler))

		## Update indirect call mechanism
		if EventDict.has_key(e):
			for Wrapper in EventDict[e][:]:
				if Wrapper.GetObjID()==self.Wrapper.GetObjID():
					EventDict[e].remove(Wrapper)
			if len(EventDict[e])==0:
				App.g_kEventManager.RemoveBroadcastHandler(e,App.Game_GetCurrentGame(),__name__+".Redirect")
				del EventDict[e]

	def AddClock(self,sFunctionHandler,fGranulation=1.0):
		e=App.Game_GetNextEventType()
		
		pEvent = App.TGIntEvent_Create()
		pEvent.SetInt(self.ID)
		pEvent.SetEventType(e)
		pEvent.SetDestination(self.Wrapper)
		
		timer=App.TGTimer_Create()
		timer.SetEvent(pEvent)
		timer.SetTimerStart(App.g_kUtopiaModule.GetGameTime()+fGranulation)
		timer.SetDelay(fGranulation)
		timer.SetDuration(-1.0)
		
		self.timers[sFunctionHandler]=timer.GetObjID(),e
		App.g_kTimerManager.AddTimer(timer)

		self.Wrapper.AddPythonMethodHandlerForInstance(e,sFunctionHandler)
		if self.handlers.count((e,sFunctionHandler))==0:
			self.handlers.append((e,sFunctionHandler))
		

	def RemoveClock(self,sFunctionHandler):
		##### lennie update:  error check; key may not be present
		try:
			ID = self.timers[sFunctionHandler][0]
			e  = self.timers[sFunctionHandler][1]
		
			self.Wrapper.RemoveHandlerForInstance(e,sFunctionHandler)
			self.handlers.remove((e,sFunctionHandler))

			App.g_kTimerManager.DeleteTimer(ID)
			del self.timers[sFunctionHandler]
		except:
			error = "No Entry Named " + sFunctionHandler
		###### end lennie update	

	def delete(self):
		for key in self.timers.keys():
			self.RemoveClock(key)
		for eventType,sFunctionHandler in self.handlers[:]:
			self.RemoveHandler(eventType,sFunctionHandler)
		if self.Node:
			if self.Node.IsTypeOf(App.CT_BASE_OBJECT):
				self.Node.SetDeleteMe(TRUE)
		if ATP_Wrapper.Dict.has_key(self.ID):
			del ATP_Wrapper.Dict[self.ID]

def Redirect(pGame,pEvent):
	## Needed to fix a not called bug
	EventDict = ATP_Wrapper.EventDict	
	e = pEvent.GetEventType()
	if EventDict.has_key(e):
		for Wrapper in EventDict[e]:
			Wrapper.ProcessEvent(pEvent)

import App
import MissionLib
import Lib.LibEngineering


MODINFO = {     "Author": "\"Defiant\" erik@bckobayashimaru.de",
                "Version": "0.1",
                "License": "BSD",
                "Description": "Nemesis style Collisions for BC",
                "needBridge": 0
            }


lUpdateObjects = None


class UpdateObjects:
	def __init__(self, iObjectID, fTime):
		self.pTimerProcess = None
		self.iObjectID = iObjectID
                self.iTimeRun = int(fTime + 0.5)
				
		self.SetupTimer()
		

	def SetupTimer(self):
		if self.pTimerProcess:
			# We already have a timer.
			return

		self.pTimerProcess = App.PythonMethodProcess()
		self.pTimerProcess.SetInstance(self)
		self.pTimerProcess.SetFunction("Update")
		self.pTimerProcess.SetDelay(0.01)
		self.pTimerProcess.SetPriority(App.TimeSliceProcess.CRITICAL)
                self.iNum = 0
	
	
	def Update(self, dTimeAvailable):
                pObject = App.DamageableObject_GetObjectByID(None, self.iObjectID)

                # check number this timer run and if the Object still exists
                if self.iNum > self.iTimeRun or not pObject:
                        # delete Timer
                        self.pTimerProcess = None
                else:
                        self.iNum = self.iNum + 1
                
                        kZero = App.TGPoint3()
                        kZero.SetXYZ(0, 0, 0)
                
                        pObject.SetVelocity(kZero)
                        pObject.SetAngularVelocity(kZero, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)
                        pObject.SetAcceleration(kZero)
                        pObject.SetAngularAcceleration(kZero)
                        pObject.UpdateNodeOnly()


def ObjectCollision(pObject, pEvent):
	pObjectHitting	= App.ObjectClass_Cast(pEvent.GetSource())
	pObjectHit	= App.ObjectClass_Cast(pEvent.GetDestination())
	ftime = pEvent.GetCollisionForce() / 25.0
        
        if pEvent.GetCollisionForce() > 5000.0:
                if pObjectHitting:
                        lUpdateObjects.append(UpdateObjects(pObjectHitting.GetObjID(), ftime))
                if pObjectHit:
                        lUpdateObjects.append(UpdateObjects(pObjectHit.GetObjID(), ftime))
        
        pObject.CallNextHandler(pEvent)
	
	
def init():
	global lUpdateObjects
	
        if Lib.LibEngineering.CheckActiveMutator("Nemesis Collisions"):
                pMission = MissionLib.GetMission()
                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_COLLISION, pMission, __name__ + ".ObjectCollision")
                lUpdateObjects = []


def Restart():
	global lUpdateObjects
	lUpdateObjects = []

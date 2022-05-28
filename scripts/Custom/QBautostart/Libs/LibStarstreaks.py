from bcdebug import debug
### Star Streaks
### Lost_Jedi 2006
### My contribution to KM 1.0 hehe
   
#########################
## Imports
import App
import math

#########################
## Constants
C_MAXWARP = float(10.0)
C_MAX_PULSEUPDATE = float(4.0)
C_PULSEUPDATESCALEFACTOR = float(C_MAX_PULSEUPDATE / C_MAXWARP)
C_MAXSTREAKSPERPULSE = 50
MAX_STREAK_DURATION = 13.0

C_FORWARDPROJECT = 50.0
C_WARPSETSIZEMULSHIPRADIUS = 3


#########################
## Globals
global lWarpingObjects
lWarpingObjects = []


#########################
## Classes

## A self defined point class cos i got SICK of using TGPoint3.  This is more flexible.  Use it. :P
class Point3:
	def __init__(self,x=0.0,y=0.0,z=0.0):
		debug(__name__ + ", __init__")
		self.x = x
		self.y = y
		self.z = z
	        
	def __str__(self):
		debug(__name__ + ", __str__")
		return '['+str(self.x)+','+str(self.y)+','+str(self.z)+']'

	def __add__(self,v):
		debug(__name__ + ", __add__")
		return Point3(self.x+v.x,self.y+v.y,self.z+v.z)
	
	def __sub__(self,v):
		debug(__name__ + ", __sub__")
		return Point3(self.x-v.x,self.y-v.y,self.z-v.z)

	def __mul__(self,v):
		debug(__name__ + ", __mul__")
		return Point3(self.x*v,self.y*v,self.z*v)

	def __rmul__(self,v):
		debug(__name__ + ", __rmul__")
		return self.__mul__(v)

	def __eq__(self,v):
		debug(__name__ + ", __eq__")
		return (self.x==v.x) and (self.y==v.y) and (self.z==v.z)

        def length(self):
                debug(__name__ + ", length")
                return math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z)
	    
	def __scale__(self,f):
		debug(__name__ + ", __scale__")
		self.x = self.x*f
		self.y = self.y*f
		self.z = self.z*f
		return self
	
	def rotate_z(self,fAngle):
                debug(__name__ + ", rotate_z")
                x = math.cos(fAngle)*self.x-math.sin(fAngle)*self.y
                y = math.sin(fAngle)*self.y+math.cos(fAngle)*self.y
                self.x = x
                self.y = y
                return self
	    
        def setTG(self,v):
                debug(__name__ + ", setTG")
                if isinstance(v,App.TGPoint3):
                    self.x = v.GetX()
                    self.y = v.GetY()
                    self.z = v.GetZ()
                return self
                
	def copy(self):
		debug(__name__ + ", copy")
		return Point3(self.x,self.y,self.z)
	    
	def copyTG(self):
		debug(__name__ + ", copyTG")
		pTG = App.TGPoint3()
		pTG.SetXYZ(self.x,self.y,self.z)
		debug(__name__ + ", copyTG Done")
		return pTG

	def random(self,x,y,z,bAbsolute = None):
                debug(__name__ + ", random")
                if App.g_kSystemWrapper.GetRandomNumber(2) == 1:    coef = 1
                else:   coef = -1
		if x > 0:
                	self.x = App.g_kSystemWrapper.GetRandomNumber(x)*coef
		else:
			x = 0
                if App.g_kSystemWrapper.GetRandomNumber(2) == 1:    coef = 1
                else:   coef = -1
		if y > 0:
                	self.y = App.g_kSystemWrapper.GetRandomNumber(y)*coef
		else:
			y = 0
                if App.g_kSystemWrapper.GetRandomNumber(2) == 1:    coef = 1
                else:   coef = -1
		if z > 0:
                	self.z = App.g_kSystemWrapper.GetRandomNumber(z)*coef
		else:
			z = 0
                if bAbsolute:
                    self = abs(self)
                return self

	def __abs__(self):
		debug(__name__ + ", __abs__")
		self.x = abs(self.x)
		self.y = abs(self.y)
		self.z = abs(self.z)
		return self



## Warp Tunnel Class
class WarpTunnel:

        def __init__(self, pWarpingObject, fWarpFactor):
            debug(__name__ + ", __init__")
            self.pTimerProcess = None
            
            fScaledWarpSpeed = float(fWarpFactor*C_PULSEUPDATESCALEFACTOR)
            self.__fUpdateTime = C_MAX_PULSEUPDATE - fScaledWarpSpeed          
                       
            self.iWarpingObjectID = pWarpingObject.GetObjID()
            self.fWarpFactor = fWarpFactor
            
            self.__buildtimer()

        def __buildtimer(self):

            debug(__name__ + ", __buildtimer")
            if not self.pTimerProcess:
		self.pTimerProcess = App.PythonMethodProcess()
		self.pTimerProcess.SetInstance(self)
		self.pTimerProcess.SetFunction("Update")
		self.pTimerProcess.SetDelay(self.__fUpdateTime)
		self.pTimerProcess.SetPriority(App.TimeSliceProcess.NORMAL)            

	def Update(self, pTickEvent):
                debug(__name__ + ", Update")
                pWarpingShip = App.ShipClass_GetObjectByID(None, self.iWarpingObjectID)
		if pWarpingShip:
			pWarpSystem = pWarpingShip.GetWarpEngineSubsystem()
		# do until we stopped warping
                if not pWarpingShip or not pWarpSystem or pWarpSystem.GetWarpState() != pWarpSystem.WES_WARPING:
                        self.pTimerProcess = None
                        WarpSetv2_KillByNode(self)
                        #print "Killed Node at " + str(self)
                else:
                        pSeq = App.TGSequence_Create()
                        for n in range(C_MAXSTREAKSPERPULSE):
                            pAction = self.SparkStreak(pWarpingShip)
                            pSeq.AddAction(pAction)
                        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "DestroyTGSequence", pSeq), 5)
                        pSeq.Play()


        def SparkStreak(self,pWarpingObject):

                debug(__name__ + ", SparkStreak")
                pController = App.SparkParticleController_Create(1.0, MAX_STREAK_DURATION - self.fWarpFactor, 1.0) #dur, life, emitrate
                                                                                # 1.0, 6.0, 1.0
                
                pController.SetTailLength(GetRandomTailLength()) # long tail

                SetupRandomColour(pController)

                pController.AddAlphaKey(0.0, 0.1)
                pController.AddAlphaKey(0.2, 0.5)
                pController.AddAlphaKey(0.4, 0.9)
                pController.AddAlphaKey(0.9, 1.0)
                pController.AddAlphaKey(1.0, 0.5)

                pController.AddSizeKey(0.0, 0.0)
                pController.AddSizeKey(1.0, float(App.g_kSystemWrapper.GetRandomNumber(10)/10))

                pController.CreateTarget("data/sphere.tga")
                
                               
                vWarpingObject_Pos = Point3().setTG(pWarpingObject.GetWorldLocation())
                vWarpingObject_Forward = Point3().setTG(pWarpingObject.GetWorldForwardTG())

                ## streak
                r = pWarpingObject.GetRadius()
		if r < 2:
			r = 2
                maxr = r*C_WARPSETSIZEMULSHIPRADIUS
                vRandom = Point3().random(maxr,maxr,maxr)
                if vRandom.length() < r:
                    vRandom = vRandom + Point3(r,r,r)
                
                vStreak_Pos = ((vWarpingObject_Pos.copy()+vRandom) + vWarpingObject_Forward.__scale__(C_FORWARDPROJECT))
                vStreak_Forward = vWarpingObject_Forward.copy().__scale__(-1)
                vStreak_Forward.__scale__(self.fWarpFactor/10.0)
                
                pController.SetGravity(vStreak_Forward.x, vStreak_Forward.y, vStreak_Forward.z)
                pController.SetEmitPositionAndDirection(vStreak_Pos.copyTG(),App.NiPoint3(0, 0, 0))
                
                pController.SetInheritsVelocity(0)
                pController.SetEmitVelocity(0)
                pController.SetDetachEmitObject(0)
                pSet = pWarpingObject.GetContainingSet()
                pController.AttachEffect(pSet.GetEffectRoot())
                return App.EffectAction_Create(pController)




## Warp Tunnel Instance Functions

def WarpSetv2_Create(pShip,fWarpFactor):
    debug(__name__ + ", WarpSetv2_Create")
    global lWarpingObjects
    oWarpEffect = WarpTunnel(pShip, fWarpFactor)
    lWarpingObjects.append(oWarpEffect)
    return oWarpEffect

def WarpSetv2_KillByNode(oNode):
    debug(__name__ + ", WarpSetv2_KillByNode")
    global lWarpingObjects
    iCounter = 0
    for element in lWarpingObjects:
        if str(element) == str(oNode):
            oWarpEffect = lWarpingObjects.pop(iCounter)
            oWarpEffect.pTimerProcess = None
        iCounter = iCounter + 1

def WarpSetv2_Flush():
    debug(__name__ + ", WarpSetv2_Flush")
    global lWarpingObjects
    lWarpingObjects = []




## Other Helper Functions
def DestroyTGSequence(pAction, pSequence):
	debug(__name__ + ", DestroyTGSequence")
	if pSequence:
		pSequence.Destroy()
	debug(__name__ + ", DestroyTGSequence End")
	return 0

def SetupRandomColour(pController):
    debug(__name__ + ", SetupRandomColour")
    pController.AddColorKey(0.0, 1.0, 1.0, 1.0)
    if not Chance100(20):
        pController.AddColorKey(0.5, 7.0, 5.0, 1.0)
        pController.AddColorKey(0.7, 1.0, 5.0, 6.0)
    else:
        pass
    pController.AddColorKey(1.0, 1.0, 1.0, 1.0)


def GetRandomTailLength(fMin = 30, fMaxRandom = 70):
    debug(__name__ + ", GetRandomTailLength")
    if fMaxRandom > 0:
    	return fMin + App.g_kSystemWrapper.GetRandomNumber(fMaxRandom)
    return 0


def Chance100(n=50):
    debug(__name__ + ", Chance100")
    if App.g_kSystemWrapper.GetRandomNumber(100) >= n:
        return 1
    else:
        return None



		

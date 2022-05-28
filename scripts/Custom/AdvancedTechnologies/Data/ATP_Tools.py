from bcdebug import debug
import math
import App

from ATP_Config import *

TRUE  = 1
FALSE = 0

ET_DUMMY = App.UtopiaModule_GetNextEventType()

NULL_VECTOR = App.TGPoint3()
NULL_VECTOR.SetXYZ(0.0,0.0,0.0)
eX = App.TGPoint3()
eX.SetXYZ(1.0,0.0,0.0)
eY = App.TGPoint3()
eY.SetXYZ(0.0,1.0,0.0)
eZ = App.TGPoint3()
eZ.SetXYZ(0.0,0.0,1.0)
e0 = App.TGPoint3()
e0.SetXYZ(0.0,0.0,0.0)

km = 1.0/App.UtopiaModule_ConvertGameUnitsToKilometers(1.0)

def AreSeperated(R1,r1,R2,r2):
	debug(__name__ + ", AreSeperated")
	R1=copyVector(R1)
	R2=copyVector(R2)

	R1.Subtract(R2)
	r0=R1.Length()
	r0=r0*math.sqrt(3.0)

	if r0<(r1+r2):
		return FALSE
	else:
		return TRUE

def copyVector(v):
	debug(__name__ + ", copyVector")
	X=App.TGPoint3()
	X.SetXYZ(v.GetX(),v.GetY(),v.GetZ())
	return X

def Vector(x,y,z):
	debug(__name__ + ", Vector")
	X=App.TGPoint3()
	X.SetXYZ(x,y,z)
	return X

def copyColour(C):
	debug(__name__ + ", copyColour")
	D = App.NiColorA()
	D.r = C.r
	D.g = C.g
	D.b = C.b
	D.a = C.a
	return D

def Colour(r,g,b,a=1.0):
	debug(__name__ + ", Colour")
	D = App.NiColorA()
	D.r = r
	D.g = g
	D.b = b
	D.a = a
	return D

def String(s):
	debug(__name__ + ", String")
	pString=App.TGString()
	pString.SetString(s)
	return pString

def BrightenColour(c,f=0.25):
	debug(__name__ + ", BrightenColour")
	d = f * min(c.r,c.g,c.b)
	c.r=c.r+d
	if c.r > 1.0:
		c.r = 1.0
	c.g=c.g+d
	if c.g > 1.0:
		c.g = 1.0
	c.b=c.b+d
	if c.b > 1.0:
		c.b = 1.0

def PasteliseColour(c,f=0.25):
	debug(__name__ + ", PasteliseColour")
	f = f + 1.0
	d = max(c.r,c.g,c.b)
	if c.r != d:
		c.r = c.r * f
	if c.r > 1.0:
		c.r = 1.0
	if c.g != d:
		c.g = c.g * f
	if c.g > 1.0:
		c.g = 1.0
	if c.b != d:
		c.b = c.b * f
	if c.b > 1.0:
		c.b = 1.0

def printVector(v):
	debug(__name__ + ", printVector")
	return "[ "+str(v.GetX())+" , "+str(v.GetY())+" , "+str(v.GetZ())+" ]"

def toDegree(a):
	debug(__name__ + ", toDegree")
	import math
	return a*180.0/math.pi

def toRad(fVal):
	debug(__name__ + ", toRad")
	import math
	return fVal*math.pi/180.0

def sign(x):
	debug(__name__ + ", sign")
	if x<0:
		return -1.0
	elif x==0:
		return 0.0
	else:
		return 1.0

def GetRandom(fVal1,fVal2):
	debug(__name__ + ", GetRandom")
	f = App.g_kSystemWrapper.GetRandomNumber(10001)*1.0
	f = f/10000.0
	
	if f<0.0:
		f=0.0
	elif f>1.0:
		f=1.0

	return (1-f)*fVal1+f*fVal2

def RandomRotation(x,y,fDist,fMinAngle,fMaxAngle,fRandom=0.0):
	debug(__name__ + ", RandomRotation")
	import math
	if fRandom==0.0:
		angle=Gaussian(fMinAngle,fMaxAngle)*sign(fRandom(-1.0,1.0))
		return x-fDist*math.cos(angle),y-fDist*math.sin(angle)
	else:
		angle=Gaussian(fMinAngle,fMaxAngle,fRandom)*sign(fRandom(-1.0,1.0,fRandom))
		return x-fDist*math.cos(angle),y-fDist*math.sin(angle)
		
def Gaussian(fVal1,fVal2,fRandom=0.0):
	debug(__name__ + ", Gaussian")
	return (fRandom(fVal1,fVal2,fRandom)+fRandom(fVal1,fVal2,fRandom)+fRandom(fVal1,fVal2,fRandom)+fRandom(fVal1,fVal2,fRandom))/4.0

def RaiseIntEvent(e,i,wrapper=None):
	debug(__name__ + ", RaiseIntEvent")
	pEvent = App.TGIntEvent_Create()
	pEvent.SetInt(i)
	pEvent.SetEventType(e)
	
	if not wrapper:
		App.Game_GetCurrentGame().ProcessEvent(pEvent)
	else:
		wrapper.ProcessEvent(pEvent)

def RaiseConceptualEvent(eventType,objectHandler,objectInvolved):
	debug(__name__ + ", RaiseConceptualEvent")
	RaiseIntEvent(eventType,objectInvolved.GetID(),objectHandler.GetWrapper())

def Dummy(castor,polux):
	debug(__name__ + ", Dummy")
	pass

#def debug(s):
#	debug(__name__ + ", debug")
#	if not DEBUG:
#		return
#	
#	import nt	
#	nt.write(debug_file,s+"\n")
#	nt.close(debug_file)
	
def IndirectCall(pObj,pEvent):
	debug(__name__ + ", IndirectCall")
	pass
	
def findEmittor(pShip,pName):
	# Find any object emitter properties on the ship.
	debug(__name__ + ", findEmittor")
	pPropSet = pShip.GetPropertySet()
	pEmitterInstanceList = pPropSet.GetPropertiesByType(App.CT_POSITION_ORIENTATION_PROPERTY)

	pEmitterInstanceList.TGBeginIteration()
	iNumItems = pEmitterInstanceList.TGGetNumItems()

	pLaunchProperty = None

	for i in range(iNumItems):
		pInstance = pEmitterInstanceList.TGGetNext()

		# Check to see if the property for this instance is a shuttle
		# emitter point.
		pProperty = App.PositionOrientationProperty_Cast(pInstance.GetProperty())

		pString=pProperty.GetName()
		pString2=App.TGString()
		pString2.SetString(pName[:])
		
		if (pProperty != None):
			if not pString.Compare(pString2):
				pLaunchProperty = pProperty
				break

	pEmitterInstanceList.TGDoneIterating()
	pEmitterInstanceList.TGDestroy()
	
	return pLaunchProperty


def PositionObjectFromLocalInfo(pObject,vPos, vFwd,vUp,Z=0.0):
	debug(__name__ + ", PositionObjectFromLocalInfo")
	M=App.TGMatrix3()
	M.MakeIdentity()
	M.MakeZRotation(toRad(Z))
	vPos.MultMatrixLeft(M)
	vFwd.MultMatrixLeft(M)
	vUp.MultMatrixLeft(M)

	# Move the waypoint to this position/orientation.
	pObject.SetTranslate(vPos)
	pObject.AlignToVectors(vFwd, vUp)
	pObject.UpdateNodeOnly()


def Decode(s,tokens):
	debug(__name__ + ", Decode")
	if not s:
		return ()
	import string
	token=tokens[0]
	seq = ()
	parts = string.split(s,token)
	more  = len(tokens) - 1
	for part in parts:
		if more:
			part  = Decode(part,tokens[1:])
		seq = seq + (part,)
	return seq

def expand(seq,i):
	debug(__name__ + ", expand")
	seq=seq[:]
	for j in range(i-len(seq)):
		seq = seq +( None, )
	return seq

def NamespaceToFolderNames(s):
	debug(__name__ + ", NamespaceToFolderNames")
	import string
	s1 = s[:string.rfind(s,'.')]
	s2 = "scripts/"+string.replace(s1,'.','/') 
	return s1,s2

CacheParentClass={}
def GetAllParentClasses(oClass):
	debug(__name__ + ", GetAllParentClasses")
	global CacheParentClass
	if CacheParentClass.has_key(oClass):
		return CacheParentClass[oClass]
	t=oClass.__bases__
	seq=[]
	for c in t:
		seq = seq + [c.__name__] + GetAllParentClasses(c)
	CacheParentClass[oClass] = seq
	return seq

def TurnToward(pShip, vDestination, vDestinationUp):
	debug(__name__ + ", TurnToward")
	vPositionDiff = App.TGPoint3()
	vPositionDiff.Set(vDestination)
	vPositionDiff.Subtract(pShip.GetWorldLocation())
	vPositionDiff.Unitize()
		
	vRight = vPositionDiff.Cross(vDestinationUp)
	vUp = vRight.Cross(vPositionDiff)
	vUp.Unitize()
		
	pShip.TurnTowardOrientation(vPositionDiff, vUp)
	

def WaypointDummy(pSet,sName,V,kForward,kUp):
	debug(__name__ + ", WaypointDummy")
	pWay = App.Waypoint_Create(sName,pSet.GetName(),None)
	pWay.SetNavPoint(FALSE)
	pWay.SetSpeed(5.0)
	pWay.SetStatic(FALSE)
	pWay.SetTranslate(V)
	pWay.AlignToVectors(kForward, kUp)
	pWay.UpdateNodeOnly()
	return pWay

def CreateProp(pSet,sName,sFolder,sGfx,fMass=1.0):
	## Load the model
	debug(__name__ + ", CreateProp")
	if not App.g_kLODModelManager.Contains(sGfx):
		pLODModel = App.g_kLODModelManager.Create(sGfx, 10000)
		pLODModel.AddLOD(sFolder+"/"+sGfx+".NIF", 10, 1.0e+8, 4.50, 4.50, 499, 500, None, None, None)
		pLODModel.SetTextureSharePath(sFolder)
		pLODModel.Load()

	## Create the obj
	pObj = App.DamageableObject_Create(sGfx)
	pObj.SetMass (fMass)
	pObj.SetNetType(0)
	pObj.SetStatic(1)
	pObj.SetScale(1.0)
	StringName = App.TGString ()
	StringName.SetString (sName)
	pSet.AddObjectToSet(pObj,sName)
	pObj.SetDisplayName(StringName)
	
	return pObj


## Buttons
def GetWarpButton():
	debug(__name__ + ", GetWarpButton")
	pass

def GetInterceptButton():
	debug(__name__ + ", GetInterceptButton")
	pass

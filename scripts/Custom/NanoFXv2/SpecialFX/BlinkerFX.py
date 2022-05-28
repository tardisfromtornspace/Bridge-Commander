###############################################################################
## Filename:	BlinkerFX.py
##	
## Adds Blinking Lights to our Trek Ships!
##
## Created:	11/24/2003 - NanoByte a.k.a Michael T. Braams
##
#############################################################################
import App
import Custom.NanoFXv2.NanoFX_ScriptActions

TRUE = 1
FALSE = 0
Blinkers = []
Static = []

# MLeo edit: Fixing Cloak problem... part 3
dContainers = {}

def CreateBlinkerFX(pShip):
	pBlinkers = None
	if pShip:
		pBlinkers = GetBlinkers(pShip)
	if not pBlinkers:
		return
	if pShip.GetName() == None:
		return	
	RemoveBlinkers(pShip)

	pSet = pShip.GetContainingSet()
	
	#kBlinkers = App.Waypoint_Create("Fun", pSet.GetName(), None)
	kBlinkers = App.ObjectClass_Create(None)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0,0,1)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0,0,1)
	kBlinkers.SetTranslateXYZ(0.0,0.0,0.0)
	kBlinkers.UpdateNodeOnly()
	kBlinkers.SetName(pShip.GetName() + "_Blinking_Lights")
	Blinkers.append(kBlinkers)
	pShip.AttachObject(kBlinkers)
	
	kStatic = App.ObjectClass_Create(None)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0,0,1)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0,0,1)
	kStatic.SetTranslateXYZ(0.0,0.0,0.0)
	kStatic.UpdateNodeOnly()
	kStatic.SetName(pShip.GetName() + "_Static_Lights")
	Static.append(kStatic)
	pShip.AttachObject(kStatic)
	
	sFile = "scripts/Custom/NanoFXv2/SpecialFX/Gfx/Blinker/Blinker.tga"
	### Setup for Effect ###
	pSequence = App.TGSequence_Create()
	
	for iBlinkers in range(len(pBlinkers)):
		pBlinker = pBlinkers[iBlinkers]
		vPos = pBlinker.GetPosition()
		pCol = pBlinker.GetColor()
		fPeriod = pBlinker.GetPeriod()
		fDuration = pBlinker.GetDuration()
		fLifeTime = 9999999
		vEmitPos = App.NiPoint3(vPos.GetX(), vPos.GetY(), vPos.GetZ())
		
		if fDuration == 0:
			fSize = pShip.GetRadius() * 0.018 * pBlinker.GetRadius()
			fDuration = 9999999
			fLifeTime = 0.1
			fPeriod = 1.0
			sType = "StaticBlinker"
			pAttachTo = kStatic.GetNode()
			pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pAttachTo)
		else:
			fSize = pShip.GetRadius() * 0.018 * pBlinker.GetRadius()
			fDuration = 9999999
			fLifeTime = 0.1
			fPeriod = 1.0
			sType = "StaticBlinker"
			pAttachTo = kBlinkers.GetNode()
			pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pAttachTo)
		
		pLight = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize * 1.1, vEmitPos, fFrequency = fPeriod, fLifeTime = fLifeTime, iTiming = fDuration, sType = sType, fRed = 255.0 * pCol.GetR(), fGreen = 255.0 * pCol.GetG(), fBlue = 255.0 * pCol.GetB())
		pSequence.AddAction(pLight)
		pLight = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize * 0.5, vEmitPos, fFrequency = fPeriod, fLifeTime = fLifeTime, iTiming = fDuration, sType = sType)
		pSequence.AddAction(pLight)
	
	pSequence.AppendAction(App.TGScriptAction_Create("Custom.NanoFXv2.NanoFX_ScriptActions", "DestroyTGSequence", pSequence), 1.0)
	pSequence.Play()
	
	## Create a container for the blinkers
	pContainer = BlinkerContainer()
	pContainer.SetNode(kBlinkers)

        # MLeo edit: Fixing cloak problem... part 4
        dContainers[pShip.GetName()] = pContainer
    
        # MLeo edit: Fixing cloak problem... Part 1
        pShip.AddPythonFuncHandlerForInstance(App.ET_CLOAK_BEGINNING, __name__ + ".CloakHandler")
        pShip.AddPythonFuncHandlerForInstance(App.ET_DECLOAK_BEGINNING, __name__ + ".DecloakHandler")


def Redirect(pObject, pEvent):
        return


from Custom.AdvancedTechnologies.Data.ATP_Wrapper import *
class BlinkerContainer(ATP_Wrapper):
	def __init__(self):
		ATP_Wrapper.__init__(self)
		self.Node = None

	def SetNode(self,Node):
		self.Node = Node
		self.RemoveClock("Swap")
		self.AddClock("Swap", 0.15)
		
		self.AddHandler(App.ET_EXIT_GAME, "DeleteContainer")
		self.AddHandler(App.ET_OBJECT_DESTROYED, "DeleteContainer")
		
	def Swap(self, pEvent):
		if self.Node:
                        try:
			        if self.Node.IsHidden():
				        self.Node.SetHidden(FALSE)
				        self.RemoveClock("Swap")
				        self.AddClock("Swap", 0.20)
			        else:
				        self.Node.SetHidden(TRUE)
				        self.RemoveClock("Swap")
				        self.AddClock("Swap", 2.0)	
                        except:
                                self.DeleteContainer(None)
				
	def DeleteContainer(self, pEvent):
        	#self.AddHandler(App.ET_EXIT_GAME, "DeleteContainer")
	        try:
        	    self.AddHandler(App.ET_OBJECT_DESTROYED, "DeleteContainer")
	            self.Node.SetDeleteMe(1)
        	    self.delete()
	        except:
        	    pass

def RemoveBlinkers(pShip):
	
	for pObject in Blinkers:
		if pObject.GetName() == pShip.GetName() + "_Blinking_Lights":
			pShip.DetachObject(pObject)
			pObject.SetDeleteMe(1)
			Blinkers.remove(pObject)
			
	for pObject in Static:
		if pObject.GetName() == pShip.GetName() + "_Static_Lights":
			pShip.DetachObject(pObject)
			pObject.SetDeleteMe(1)
			Static.remove(pObject)
	
def GetBlinkers(pShip):
	# Find any object emitter properties on the ship.
	pPropSet = pShip.GetPropertySet()
	pEmitterInstanceList = pPropSet.GetPropertiesByType(App.CT_BLINKING_LIGHT_PROPERTY)

	pEmitterInstanceList.TGBeginIteration()
	iNumItems = pEmitterInstanceList.TGGetNumItems()

	Blinkers=()
	for i in range(iNumItems):
		pInstance = pEmitterInstanceList.TGGetNext()

		# Check to see if the property for this instance is a Blinking Light
		# emitter point.
		pProperty = App.BlinkingLightProperty_Cast(pInstance.GetProperty())
		if (pProperty != None):
			Blinkers = Blinkers + (pProperty,)

	pEmitterInstanceList.TGDoneIterating()
	pEmitterInstanceList.TGDestroy()
	
	return Blinkers

# MLeo edit: Fixing cloak problem... Part 2
def CloakHandler(pEObject, pEvent):
    pShip = App.ShipClass_Cast(pEObject)
    if pShip:
        if dContainers.has_key(pShip.GetName()):
            pContainer = dContainers[pShip.GetName()]
            if pContainer:
                if not pContainer.Node.IsHidden():
                    pContainer.Swap(None)
                pContainer.RemoveClock("Swap")
        for pObject in Static:
            if pObject.GetName() == pShip.GetName() + "_Static_Lights":
                pObject.SetHidden(1)
    pEObject.CallNextHandler(pEvent)

def DecloakHandler(pEObject, pEvent):
    pShip = App.ShipClass_Cast(pEObject)
    if pShip:
        if dContainers.has_key(pShip.GetName()):
            pContainer = dContainers[pShip.GetName()]
            if pContainer:
                pContainer.Swap(None)
        for pObject in Static:
            if pObject.GetName() == pShip.GetName() + "_Static_Lights":
                pObject.SetHidden(0)

    pEObject.CallNextHandler(pEvent)

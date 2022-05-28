from bcdebug import debug
import App
import Foundation

oBridgePlugin = __import__("Custom.Autoload.000-Fixes20040612-LCBridgeAddon")
NonSerializedObjects = (
"oBridgePlugin"
)

counter = 0

dDefaultValues = {"Sensor Values": 
                 {1.0: (0.0,0.0),
                  0.8: (0.0,0.2),
                  0.6: (0.0,0.4),
                  0.4: (0.1,0.5),
                  0.2: (0.2,0.6),
                  0.1: (0.3,0.7),
                  0.0: (1.0,1.0)
}}

class ViewScreenStatic(Foundation.BridgePluginDef):
	def __call__(self, Plug, pBridgeSet, oBridgeInfo):
		debug(__name__ + ", __call__")
		pass # This mod requires a player ship

	def PlayerCreated(self, Plug, pBridgeSet, oBridgeInfo, pShip):
		debug(__name__ + ", PlayerCreated")
		global dDefaultValues
		pSensors = pShip.GetSensorSubsystem()
		if pSensors:
			lRanges = dDefaultValues["Sensor Values"].keys()#[1.0,0.80,0.60,0.40,0.20,0.0]
			if Plug.__dict__.has_key("SensorStatic"):
				lRanges = []
				for i in oBridgeInfo.SensorStatic["Sensor Values"].keys():
					lRanges.append(i/100.0)
			# Need an event for this range check..
			pSubsystemWatcher = pSensors.GetCombinedPercentageWatcher()
			for fRange in lRanges:
				pEvent = App.TGFloatEvent_Create()
				pEvent.SetEventType(App.ET_SUBSYSTEM_STATE_CHANGED)
				pEvent.SetDestination(pShip)
				pEvent.SetSource(pSensors)
				oBridgeInfo.lCurrentRangeChecks.append((pSubsystemWatcher.this, pSubsystemWatcher.AddRangeCheck(fRange, App.FloatRangeWatcher.FRW_BOTH, pEvent)))
			pShip.AddPythonFuncHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SensorChange")
			pShip.AddPythonFuncHandlerForInstance(App.ET_WEAPON_HIT, __name__ + ".WeaponHit")
			pShip.AddPythonFuncHandlerForInstance(App.ET_ENTERED_NEBULA, __name__ + ".EnterNebula")
			pShip.AddPythonFuncHandlerForInstance(App.ET_EXITED_NEBULA, __name__ + ".ExitNebula")
			pShip.AddPythonFuncHandlerForInstance(App.ET_CLOAK_BEGINNING, __name__ + ".CloakBeginning")
			pShip.AddPythonFuncHandlerForInstance(App.ET_DECLOAK_BEGINNING, __name__ + ".DecloakBeginning")

			# Set "default"

			dSensorStatic = dDefaultValues
			if oBridgePlugin.oBridgeInfo.__dict__.has_key("SensorStatic"):
				dSensorStatic = oBridgePlugin.oBridgeInfo.SensorStatic

			sGroup = "View Screen Static"
			if dSensorStatic.has_key("Static Group"):
				sGroup = dSensorStatic["Static Group"]
			global counter, fNebAdd, fCloAdd, lStatic
			counter = 0
			fNebAdd = 0.0
			fWepAdd = 0.0
			fCloAdd = 0.0
			lStatic = [0,0]

			SetStatic(0,0, sGroup)

oViewScreenStatic = ViewScreenStatic("Viewscreen Static Bridge Plugin")#, dict = {"modes": [mode]})

def SensorChange(pObject, pEvent):
	#print "Sensor Changing"
	debug(__name__ + ", SensorChange")
	global oBridgePlugin, dDefaultValues, counter
	if counter > 3: # Needed to fix the "default" static.
		dSensorStatic = dDefaultValues
		if oBridgePlugin.oBridgeInfo.__dict__.has_key("SensorStatic"):
			dSensorStatic = oBridgePlugin.oBridgeInfo.SensorStatic

		# The source of the event is set to the sensor system
		pSubsystem = App.ShipSubsystem_Cast(pEvent.GetSource())

		fCondition = pSubsystem.GetConditionPercentage()

		iClosest = FindClosest(fCondition, dSensorStatic["Sensor Values"].keys())

		sGroup = "View Screen Static"
		if dSensorStatic.has_key("Static Group"):
			sGroup = dSensorStatic["Static Group"]

		SetStatic(dSensorStatic["Sensor Values"][iClosest][0],dSensorStatic["Sensor Values"][iClosest][1], sGroup)
		counter = counter + 1

	if pObject and pEvent:
		pObject.CallNextHandler(pEvent)


def WeaponHit(pObject, pEvent):
	debug(__name__ + ", WeaponHit")
	global oBridgePlugin, lStatic
	if pEvent.IsHullHit():
		pShip = App.ShipClass_Cast(pObject)
		if pShip:
			pSensors = pShip.GetSensorSubsystem()
			pSensorPos = pSensors.GetPositionTG()

			kHitPos = pEvent.GetObjectHitPoint()
			pHitPos = App.TGPoint3()
			pHitPos.SetXYZ(kHitPos.x, kHitPos.y, kHitPos.z)
			pSensorPos.Subtract(pHitPos)
			fDist = pSensorPos.SqrLength()

			if fDist > 0.0:
				fLocalMod = 1.0/fDist
				fMin = lStatic[0]
				fMax = lStatic[1]
				pSequence = App.TGSequence_Create()
				pSequence.AppendAction(App.TGScriptAction_Create(__name__, "WeaponAction", fLocalMod), 1)
				pSequence.AppendAction(App.TGScriptAction_Create(__name__, "WeaponAction", 0), 2)
				pSequence.Play()
	if pObject and pEvent:
		pObject.CallNextHandler(pEvent)

def EnterNebula(pObject, pEvent):
	debug(__name__ + ", EnterNebula")
	global fNebAdd, lStatic
	fNebAdd = 1.0
	SetStatic(-1, -1)
	if pObject and pEvent:
		pObject.CallNextHandler(pEvent)

def ExitNebula(pObject, pEvent):
	debug(__name__ + ", ExitNebula")
	global fNebAdd, lStatic
	fNebAdd = 0.0
	SensorChange(None, None)
	if pObject and pEvent:
		pObject.CallNextHandler(pEvent)

def CloakBeginning(pObject, pEvent):
	debug(__name__ + ", CloakBeginning")
	global fCloAdd, lStatic
	fCloAdd = 0.4
	SetStatic(-1, -1)
	if pObject and pEvent:
		pObject.CallNextHandler(pEvent)

def DecloakBeginning(pObject, pEvent):
	debug(__name__ + ", DecloakBeginning")
	global fCloAdd, lStatic
	fCloAdd = 0.0
	SetStatic(-1, -1)
	if pObject and pEvent:
		pObject.CallNextHandler(pEvent)

lStatic = [0.0,0.0]
fNebAdd = 0.0
fWepAdd = 0.0
fCloAdd = 0.0

def SetStatic(fMin=-1, fMax=-1, sStaticGroup = "View Screen Static"):
	debug(__name__ + ", SetStatic")
	global lStatic, fMod, fNebAdd, fWepAdd, fCloAdd, oBridgePlugin
	pBridge = App.BridgeSet_Cast(App.g_kSetManager.GetSet("bridge"))
	if not pBridge:
		return
	pViewScreen = pBridge.GetViewScreen()

	if fMin != -1:
		lStatic[0] = fMin
	if fMax != -1:
		lStatic[1] = fMax

	if pViewScreen:
		pPlayer = App.Game_GetCurrentPlayer()
		if pPlayer:
			pSensors = pPlayer.GetSensorSubsystem()
			if pSensors and pSensors.GetConditionPercentage() <= 0.0:
				if oBridgePlugin.oBridgeInfo:
					pViewScreen.SetOffTexture(oBridgePlugin.oBridgeInfo.LoadingScreen)
				else:
					pViewScreen.SetOffTexture("data/Icons/ViewscreenLoading.tga")
				pViewScreen.SetIsOn(0)
				pViewScreen.SetStaticIsOn(0)
				return
		if not pViewScreen.IsOn():
			pViewScreen.SetIsOn(1)
		fAdd = fNebAdd + fWepAdd + fCloAdd
		if (lStatic[1]+fAdd > 0.001):
			pViewScreen.SetStaticTextureIconGroup(sStaticGroup)
			pViewScreen.SetStaticIsOn(1)
			pViewScreen.SetStaticVariation(lStatic[0]+fAdd, lStatic[1]+fAdd)
		else:
			pViewScreen.SetStaticVariation(0,0)
			pViewScreen.SetStaticIsOn(0)

def SetStaticAction(pAction, fMin, fMax, sStaticGroup = "View Screen Static"):
	debug(__name__ + ", SetStaticAction")
	SetStatic(fMin,fMax, sStaticGroup)
	return 0

def RestoreStaticAction(pAction):
	debug(__name__ + ", RestoreStaticAction")
	SensorChange(None, None)
	return 0

def WeaponAction(pAction, fAdd):
	debug(__name__ + ", WeaponAction")
	global fWepAdd

	if not oBridgePlugin.oBridgeInfo:
		return

	dSensorStatic = dDefaultValues
	if oBridgePlugin.oBridgeInfo.__dict__.has_key("SensorStatic"):
		dSensorStatic = oBridgePlugin.oBridgeInfo.SensorStatic

	sGroup = dSensorStatic.get("Static Group", "View Screen Static")

	fWepAdd = fAdd
	SetStatic(-1,-1, sGroup)
	return 0

def FindClosest(fValue, lOptions):
	debug(__name__ + ", FindClosest")
	lOptions.sort()
	for val in lOptions:
		if fValue <= val:
			return val
	return 0


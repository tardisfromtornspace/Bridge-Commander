# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 14th January 2024, by Alex SL Gato (CharaToLoki), partially based on the Shield.py script by the Foundation Technologies team and Dasher42's Foundation script, and the FedAblativeArmor.py found in scripts/ftb/Tech in KM 2011.10
# Also based on Conditions.ConditionSystemBelow, probably from the original STBC Team and Activision
# TODO: 1. Create Read Me
#	2. Create a clear guide on how to add this...
#
# Start on 2:
# This tech takes part on the defensive roles of ships with outstanding regeneration capabilities, such as the Borg, where destroyed systems and visible hull damage are repaired.
# just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "LowCube" with the abbrev
# Time: this field indicates how fast destroyed systems regenerate after destruction, in seconds. Default is 0.1. Values under 0 will be naturally ignored.
"""
Foundation.ShipDef.LowCube.dTechs = {
	'Automated Destroyed System Repair': {"Time": 1.0}
}
"""

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "0.3",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }

import App

import Foundation
import FoundationTech
import MissionLib

import Conditions

import nt
import math
import string

from bcdebug import debug
import traceback

vOverflow = 0
eAllSystemsat100Type = None
eAllSystemsat100RealType = None

# based on the FedAblativeArmour.py script, a fragment probably imported from ATP Functions by Apollo
def NiPoint3ToTGPoint3(p):
	kPoint = App.TGPoint3()
	kPoint.SetXYZ(p.x, p.y, p.z)
	return kPoint

def findShipInstance(pShip):
	pInstance = None
	try:
		pInstance = FoundationTech.dShips[pShip.GetName()]
		if pInstance == None:
			print "After looking, no pInstance for ship:", pShip.GetName(), "How odd..."
		
	except:
		print "Error while looking for pInstance for Borg technology:"
		traceback.print_exc()
		
	#finally:
	return pInstance

def findscriptsShipsField(pShip, thingToFind):
	thingFound = None
	pShipModule=__import__(pShip.GetScript())
	information = pShipModule.GetShipStats()
	if information != None and information.has_key(thingToFind):
		thingFound = information[thingToFind]
	return thingFound



#TO-DO IF ALL SYSTEMS ARE AT 100% THEN WE HEAL VISIBLE DAMAGE

class AutomatedDestroyedSystemRepairDef(FoundationTech.TechDef):
	def __init__(self, name):
		debug(__name__ + ", Initiated AutomatedDestroyedSystemRepair counter")
		FoundationTech.TechDef.__init__(self, name)
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_SUBSYSTEM_DESTROYED, self.pEventHandler, "UnDestroySystemDelay")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_SUBSYSTEM_DESTROYED, self.pEventHandler, "UnDestroySystemDelay")


	def Attach(self, pInstance):

		global vOverflow, eAllSystemsat100Type
		if not vOverflow:
			pGame = App.Game_GetCurrentGame()
			pEpisode = pGame.GetCurrentEpisode()
			pMission = pEpisode.GetCurrentMission()
			eAllSystemsat100Type = App.Mission_GetNextEventType()
			eAllSystemsat100RealType = App.Mission_GetNextEventType()

		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		if pShip != None:
			#pShip.pEventHandler = App.TGPythonInstanceWrapper()
			#pShip.pEventHandler.SetPyWrapper(pShip)
			#pShip.AddPythonFuncHandlerForInstance(App.ET_REPAIR_COMPLETED, __name__ + ".CheckTotalStatus")
			#TO-DO 
			#pHull = pShip.GetHull()

			global eAllSystemsat100Type

			#self.fFraction = 1.0 - (1.0/pHull.GetMaxCondition())

			pShipSet = pShip.GetPropertySet()
			pShipList = pShipSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
			iNumItems = pShipList.TGGetNumItems()

			pShipList.TGBeginIteration()
			for i in range(iNumItems):
				pShipProperty = App.SubsystemProperty_Cast(pShipList.TGGetNext().GetProperty())
				pSubsystem = pShip.GetSubsystemByProperty(pShipProperty)

				pEvent = App.TGFloatEvent_Create()
				pEvent.SetEventType( eAllSystemsat100Type )
				pEvent.SetDestination( self.pEventHandler )
				pEvent.SetSource( pSubsystem )

				fFraction = 1.0 - (1.0/pSubsystem.GetMaxCondition())
				pWatcher = pSubsystem.GetConditionWatcher()
				iRangeID = pWatcher.AddRangeCheck( fFraction, App.FloatRangeWatcher.FRW_BOTH, pEvent )
				if pInstance and pInstance.__dict__.has_key("Automated Destroyed System Repair"):
					if not pInstance.__dict__["Automated Destroyed System Repair"].has_key("SystemsToCheck"):
						pInstance.__dict__["Automated Destroyed System Repair"]["SystemsToCheck"] = {}
					pInstance.__dict__["Automated Destroyed System Repair"]["SystemsToCheck"][pSubsystem.GetObjID()] = {"Complies": 1, "Fraction": fFraction}
					pInstance.__dict__["Automated Destroyed System Repair"]["SystemsToCheck"][pSubsystem.GetObjID()]["Watcher"] = iRangeID

			pShipList.TGDoneIterating()

			#pWatcher = pHull.GetConditionWatcher()
			#iRangeID = pWatcher.AddRangeCheck( self.fFraction, App.FloatRangeWatcher.FRW_BOTH, pEvent ) # App.CT_HULL_SUBSYSTEM #App.CT_SUBSYSTEM_PROPERTY


		
		#	pShip.AddPythonMethodHandlerForInstance( eAllSystemsat100Type, __name__ + ".RefreshVisibleDamage" )
			App.g_kEventManager.AddBroadcastPythonMethodHandler(eAllSystemsat100Type, self.pEventHandler, "Test")
		else:
			#print "AutomatedDestroyedSystemRepair Error (at Attach): couldn't acquire ship of id", pInstance.pShipID
			pass
		pInstance.lTechs.append(self)
		#print "AutomatedDestroyedSystemRepair: attached to ship:", pShip.GetName()

	def Test(self, pFloatEvent):
		fFraction = pFloatEvent.GetFloat()
		pSubsystem = App.ShipSubsystem_Cast(pFloatEvent.GetSource())
		pShip = pSubsystem.GetParentShip()
		if pShip:
			pInstance = findShipInstance(pShip)
			if pInstance and pInstance.__dict__.has_key("Automated Destroyed System Repair") and pInstance.__dict__["Automated Destroyed System Repair"].has_key("SystemsToCheck"):
				myfFraction = 1.1 # Impossible to reach, ergo a good default value
				if pInstance.__dict__["Automated Destroyed System Repair"]["SystemsToCheck"].has_key(pSubsystem.GetObjID()) and pInstance.__dict__["Automated Destroyed System Repair"]["SystemsToCheck"][pSubsystem.GetObjID()].has_key("Fraction"):
					myfFraction = pInstance.__dict__["Automated Destroyed System Repair"]["SystemsToCheck"][pSubsystem.GetObjID()].has_key("Fraction")
					
				if fFraction >= myfFraction:
					pInstance.__dict__["Automated Destroyed System Repair"]["SystemsToCheck"][pSubsystem.GetObjID()]["Complies"] = 1
				else:
					pInstance.__dict__["Automated Destroyed System Repair"]["SystemsToCheck"][pSubsystem.GetObjID()]["Complies"] = 0

				totalComply = pInstance.__dict__["Automated Destroyed System Repair"]["SystemsToCheck"][pSubsystem.GetObjID()]["Complies"]
				for subSysID in pInstance.__dict__["Automated Destroyed System Repair"]["SystemsToCheck"].keys():
					if pInstance.__dict__["Automated Destroyed System Repair"]["SystemsToCheck"][subSysID]["Complies"] == 0:
						totalComply = 0
						break

				if totalComply == 1:
					RefreshVisibleDamage(pShip)
			else:
				RefreshVisibleDamage(pShip)

		self.pEventHandler.CallNextHandler(pFloatEvent)
		return 0

	def Detach(self, pInstance):
		global eAllSystemsat100Type
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		if pShip != None:

			#pShip.RemoveHandlerForInstance(App.ET_REPAIR_COMPLETED, __name__ + ".CheckTotalStatus")
			#pHull = pShip.GetHull()
			#pInstance = findShipInstance(pShip)

			pShipSet = pShip.GetPropertySet()
			pShipList = pShipSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
			iNumItems = pShipList.TGGetNumItems()

			pShipList.TGBeginIteration()
			for i in range(iNumItems):
				pShipProperty = App.SubsystemProperty_Cast(pShipList.TGGetNext().GetProperty())
				pSubsystem = pShip.GetSubsystemByProperty(pShipProperty)

				iInfo = None
				try:
					iInfo = pInstance.__dict__["Automated Destroyed System Repair"]["SystemsToCheck"][pSubsystem.GetObjID()]["Watcher"]
				except:
					iInfo = None

				if iInfo is not None:
					pWatcher = pSubsystem.GetConditionWatcher()
					pWatcher.RemoveRangeCheck( iInfo )
				
			pShipList.TGDoneIterating()

			del pInstance.__dict__["Automated Destroyed System Repair"]["SystemsToCheck"]

		else:
			#print "AutomatedDestroyedSystemRepair Error (at Detach): couldn't acquire ship of id", pInstance.pShipID
			pass
		pInstance.lTechs.remove(self)
		#print "AutomatedDestroyedSystemRepair: detached from ship:", pShip.GetName()

	def UnDestroySystemDelay(self, pEvent):
		pSubsystemToRepair = App.ShipSubsystem_Cast(pEvent.GetSource())

		pShip = pSubsystemToRepair.GetParentShip()
		if pShip:
			self.UnDestroySystemDelay2(pShip, pEvent)
		return 0

	def UnDestroySystemDelay2(self, pObject, pEvent):
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pObject.GetObjID()))
		if pShip:
			pInstance = findShipInstance(pShip)
			if pInstance.__dict__.has_key("Automated Destroyed System Repair"):
			
				pSubsystemToRepair = App.ShipSubsystem_Cast(pEvent.GetSource())
				if not pSubsystemToRepair:
					return

				destroyedSystemName = pSubsystemToRepair.GetName()
				delay = 0.1
				if pInstance.__dict__['Automated Destroyed System Repair'].has_key("Time") and pInstance.__dict__['Automated Destroyed System Repair']["Time"] >= 0.0:
					delay = pInstance.__dict__['Automated Destroyed System Repair']["Time"]
				if not pInstance.__dict__['Automated Destroyed System Repair'].has_key(destroyedSystemName):
					pInstance.__dict__['Automated Destroyed System Repair'][destroyedSystemName] = {}

				if pInstance.__dict__['Automated Destroyed System Repair'].has_key("Timer"):
					App.g_kTimerManager.DeleteTimer(pInstance.__dict__['Automated Destroyed System Repair'][destroyedSystemName]['Timer'].GetObjID())
					del pInstance.__dict__['Automated Destroyed System Repair'][destroyedSystemName]['Timer']

				pGame = App.Game_GetCurrentGame()
				pEpisode = pGame.GetCurrentEpisode()
				pMission = pEpisode.GetCurrentMission()
				eType = App.Mission_GetNextEventType()

				#pShip.AddPythonFuncHandlerForInstance(eType, __name__ + ".unDestroySystem")
				#App.g_kEventManager.AddBroadcastPythonMethodHandler(eType, __name__ + ".AutomatedDestroyedSystemRepairDef.pEventHandler", __name__ + ".UnDestroySystem")
				#App.g_kEventManager.AddBroadcastPythonMethodHandler(eType, pMission, __name__ + ".UnDestroySystem")
				App.g_kEventManager.AddBroadcastPythonMethodHandler(eType, self.pEventHandler, "UnDestroySystem")
	
				pEvent2 = App.TGStringEvent_Create()
				pEvent2.SetEventType(eType)
				pEvent2.SetSource(pEvent.GetSource())
				pEvent2.SetDestination(pEvent.GetDestination())
				pEvent2.SetString(str(destroyedSystemName))

				pTimer = App.TGTimer_Create()
				pTimer.SetTimerStart( App.g_kUtopiaModule.GetGameTime()+delay ) # TO-DO CUSTOMIZE
				pTimer.SetDelay(0)
				pTimer.SetDuration(0)
				pTimer.SetEvent(pEvent2)
				App.g_kTimerManager.AddTimer(pTimer)
				pInstance.__dict__['Automated Destroyed System Repair'][destroyedSystemName]['Timer'] = pTimer

		pObject.CallNextHandler(pEvent)

	def UnDestroySystem(self, pEvent):

		pSubsystemToRepair = App.ShipSubsystem_Cast(pEvent.GetSource())
		pShip = pSubsystemToRepair.GetParentShip()
		if pShip:
			UnDestroySystem(pShip, pEvent)
		return 0

		thisEventType = pEvent.GetEventType()
		#pShip.RemoveHandlerForInstance(thisEventType, __name__ + ".unDestroySystem")
		App.g_kEventManager.RemoveBroadcastHandler(thisEventType, self.pEventHandler, "UnDestroySystem")

def UnDestroySystem(pObject, pEvent):
	debug(__name__ + ", UnDestroySystem")
	pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pObject.GetObjID()))

	if pShip:
		pInstance = findShipInstance(pShip)
		if pInstance.__dict__.has_key("Automated Destroyed System Repair"):
			
			destroyedSystemName = pEvent.GetCString()
			pShipSet = pShip.GetPropertySet()
			pShipList = pShipSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)

			iNumItems = pShipList.TGGetNumItems()
			pShipList.TGBeginIteration()
			for i in range(iNumItems):
				pShipProperty = App.SubsystemProperty_Cast(pShipList.TGGetNext().GetProperty())
				pSubsystem = pShip.GetSubsystemByProperty(pShipProperty)
				if pSubsystem.GetName() == destroyedSystemName:
					pSubsysCondition = pSubsystem.GetCondition()
					if (pSubsysCondition <= 0):
						pSubsystem.SetCondition(pSubsystem.GetMaxCondition())
						pSubsystem.SetCondition(1)
					break

			pShipList.TGDoneIterating()
			if pInstance.__dict__['Automated Destroyed System Repair'].has_key(destroyedSystemName):
				App.g_kTimerManager.DeleteTimer(pInstance.__dict__['Automated Destroyed System Repair'][destroyedSystemName]['Timer'].GetObjID())
				del pInstance.__dict__['Automated Destroyed System Repair'][destroyedSystemName]['Timer']

	pObject.CallNextHandler(pEvent)

def RefreshVisibleDamage(pShip):
	pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShip.GetObjID()))
	if pShip:
		pShip.RemoveVisibleDamage()
		pShip.DamageRefresh(0.0)
	return 0
	

oAutomatedDestroyedSystemRepair = AutomatedDestroyedSystemRepairDef('Automated Destroyed System Repair')
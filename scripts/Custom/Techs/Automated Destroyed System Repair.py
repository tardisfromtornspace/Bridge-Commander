# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 17th March 2024, by Alex SL Gato (CharaToLoki), partially based on the Shield.py script by the Foundation Technologies team and Dasher42's Foundation script, and the FedAblativeArmor.py found in scripts/ftb/Tech in KM 2011.10
# Also based on Conditions.ConditionSystemBelow, probably from the original STBC Team and Activision
# TODO: 1. Create Read Me
#	2. Create a clear guide on how to add this...
#
# Start on 2:
# This tech takes part on the defensive roles of ships with outstanding regeneration capabilities, such as the Borg, where destroyed systems and visible hull damage are repaired.
# just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "LowCube" with the abbrev
# Time: this field indicates how fast destroyed systems regenerate after destruction, in seconds. Default is 0.1. Values under 0 will be naturally ignored.
# DoNotInterfere: this field is a 0.5 addition, it is done so if a certain type of ship has this at 0, it will do the RemoveVisibleDamage option, instead of reloading a ship's script. Both have their pros and cons:
# - RemoveVisibleDamage() option is faster and cleaner, but due to an stbc.exe bug, it only works once. Once done, that ship is as if it had visible damage off forever.
# - reloading a ship's script allows a ship to "rejuvenate" and heal all visible damage, while still allowing the ship to take further visible damage later on, this allows an enemy to cut a ship's arm only to regrow, and then can cut it
#   again and regrow again, indefinetely. However, this strategy is a bit slower and might interfere with some scripts that change a ship's model already, such as SubModels, some options of AdvArmorThree, and similar.
# *** IMPORTANT NOTE: it is required to have the "Tactical.Projectiles.AutomaticSystemRepairDummy" torpedo for the reloading a ship's script part ***
"""
Foundation.ShipDef.LowCube.dTechs = {
	'Automated Destroyed System Repair': {"Time": 1.0, "DoNotInterfere": 0}
}
"""

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "0.62",
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

REMOVE_POINTER_FROM_SET = 190
NO_COLLISION_MESSAGE = 192
REPLACE_MODEL_MSG = 208
SET_TARGETABLE_MSG = 209

eAllSystemsat100Type = App.UtopiaModule_GetNextEventType()
eType = App.UtopiaModule_GetNextEventType()

# based on the FedAblativeArmour.py script, a fragment probably imported from ATP Functions by Apollo
def NiPoint3ToTGPoint3(p):
	kPoint = App.TGPoint3()
	kPoint.SetXYZ(p.x, p.y, p.z)
	return kPoint

def findShipInstance(pShip):
	pInstance = None
	try:
		if not pShip:
			return pInstance
		if FoundationTech.dShips.has_key(pShip.GetName()):
			pInstance = FoundationTech.dShips[pShip.GetName()]
	except:
		pass

	return pInstance

def findscriptsShipsField(pShip, thingToFind):
	thingFound = None
	pShipModule=__import__(pShip.GetScript())
	information = pShipModule.GetShipStats()
	if information != None and information.has_key(thingToFind):
		thingFound = information[thingToFind]
	return thingFound


class AutomatedDestroyedSystemRepairDef(FoundationTech.TechDef):
	def __init__(self, name):
		debug(__name__ + ", Initiated AutomatedDestroyedSystemRepair counter")
		FoundationTech.TechDef.__init__(self, name)
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)

		App.g_kEventManager.RemoveBroadcastHandler(App.ET_SUBSYSTEM_DESTROYED, self.pEventHandler, "UnDestroySystemDelay")
		App.g_kEventManager.RemoveBroadcastHandler(eAllSystemsat100Type, self.pEventHandler, "Test")
		App.g_kEventManager.RemoveBroadcastHandler(eType, self.pEventHandler, "UnDestroySystem")

		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_SUBSYSTEM_DESTROYED, self.pEventHandler, "UnDestroySystemDelay")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(eAllSystemsat100Type, self.pEventHandler, "Test")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(eType, self.pEventHandler, "UnDestroySystem")


	def Attach(self, pInstance):

		global eAllSystemsat100Type

		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		if pShip != None:

			global eAllSystemsat100Type

			pInstanceDict = None
			pInstanceHasMyKey = 0
			if pInstance:
				pInstanceDict = pInstance.__dict__
				pInstanceHasMyKey = pInstanceDict.has_key("Automated Destroyed System Repair")

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
				if pInstance:
					if pInstanceHasMyKey:
						if not pInstanceDict.has_key("Automated Destroyed System Repair I"):
							pInstanceDict["Automated Destroyed System Repair I"] = {}

						pInstanceDict["Automated Destroyed System Repair I"][pSubsystem.GetObjID()] = {"Complies": 1, "Fraction": fFraction}
						pInstanceDict["Automated Destroyed System Repair I"][pSubsystem.GetObjID()]["Watcher"] = iRangeID

			pShipList.TGDoneIterating()

		else:
			#print "AutomatedDestroyedSystemRepair Error (at Attach): couldn't acquire ship of id", pInstance.pShipID
			pass
		pInstance.lTechs.append(self)

	def Test(self, pFloatEvent):
		fFraction = pFloatEvent.GetFloat()
		pSubsystem = App.ShipSubsystem_Cast(pFloatEvent.GetSource())
		if not pSubsystem:
			try:
				self.pEventHandler.CallNextHandler(pFloatEvent)
			except:
				pass
			return 0

		pShip = pSubsystem.GetParentShip()
		if pShip and hasattr(pShip, "GetObjID"):
			pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
			if pShip:
				pInstance = findShipInstance(pShip)
				if pInstance:
					pInstanceDict = pInstance.__dict__

					if pInstanceDict.has_key("Automated Destroyed System Repair") and pInstanceDict.has_key("Automated Destroyed System Repair I"):
						myfFraction = 1.1 # Impossible to reach, ergo a good default value
						if pInstanceDict["Automated Destroyed System Repair I"].has_key(pSubsystem.GetObjID()) and pInstanceDict["Automated Destroyed System Repair I"][pSubsystem.GetObjID()].has_key("Fraction"):
							myfFraction = pInstanceDict["Automated Destroyed System Repair I"][pSubsystem.GetObjID()]["Fraction"]
					
						if fFraction >= myfFraction:
							pInstanceDict["Automated Destroyed System Repair I"][pSubsystem.GetObjID()]["Complies"] = 1
						else:
							pInstanceDict["Automated Destroyed System Repair I"][pSubsystem.GetObjID()]["Complies"] = 0

						totalComply = pInstanceDict["Automated Destroyed System Repair I"][pSubsystem.GetObjID()]["Complies"]
						for subSysID in pInstanceDict["Automated Destroyed System Repair I"].keys():
							if pInstanceDict["Automated Destroyed System Repair I"][subSysID]["Complies"] == 0:
								totalComply = 0
								break

						if totalComply == 1:
							notfast = 1
							if pInstanceDict["Automated Destroyed System Repair"].has_key("DoNotInterfere"):
								notfast = pInstanceDict["Automated Destroyed System Repair"]["DoNotInterfere"]
							RefreshVisibleDamage(pShip, notfast)

					#else:
					#	if pInstanceDict.has_key("Automated Destroyed System Repair"):
					#		RefreshVisibleDamage(pShip)

		self.pEventHandler.CallNextHandler(pFloatEvent)
		return 0

	def Detach(self, pInstance):
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		if pShip != None:
			pShipSet = pShip.GetPropertySet()
			pShipList = pShipSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
			iNumItems = pShipList.TGGetNumItems()

			pShipList.TGBeginIteration()
			for i in range(iNumItems):
				pShipProperty = App.SubsystemProperty_Cast(pShipList.TGGetNext().GetProperty())
				pSubsystem = pShip.GetSubsystemByProperty(pShipProperty)

				iInfo = None
				try:
					iInfo = pInstance.__dict__["Automated Destroyed System Repair I"][pSubsystem.GetObjID()]["Watcher"]
				except:
					iInfo = None

				if iInfo is not None:
					pWatcher = pSubsystem.GetConditionWatcher()
					pWatcher.RemoveRangeCheck( iInfo )

				try:
					App.g_kTimerManager.DeleteTimer(pInstance.__dict__['Automated Destroyed System Repair I'][pSubsystem.GetObjID()]['Timer'].GetObjID())
				except:
					pass
					
				
			pShipList.TGDoneIterating()

			if pInstance and pInstance.__dict__.has_key("Automated Destroyed System Repair I"):
				del pInstance.__dict__["Automated Destroyed System Repair I"]

		else:
			if pInstance:
				pInstanceDict = pInstance.__dict__
				if pInstanceDict.has_key("Automated Destroyed System Repair I"):
					for subSysID in pInstanceDict["Automated Destroyed System Repair I"].keys():
						
						#iInfo = None
						#try:
						#	iInfo = pInstance.__dict__["Automated Destroyed System Repair I"][subSysID]["Watcher"]
						#except:
						#	iInfo = None

						#if iInfo is not None:
						#	pWatcher = pSubsystem.GetConditionWatcher()
						#	pWatcher.RemoveRangeCheck( iInfo )

						try:
							App.g_kTimerManager.DeleteTimer(pInstance.__dict__['Automated Destroyed System Repair I'][subSysID]['Timer'].GetObjID())
						except:
							pass

					del pInstance.__dict__["Automated Destroyed System Repair I"]

		if pInstance:
			pInstance.lTechs.remove(self)

		#print "AutomatedDestroyedSystemRepair: detached from ship:", pShip.GetName()

	def UnDestroySystemDelay(self, pEvent):
		pSubsystemToRepair = App.ShipSubsystem_Cast(pEvent.GetSource())
		if pSubsystemToRepair:
			pShip = pSubsystemToRepair.GetParentShip()
			if pShip:
				self.UnDestroySystemDelay2(pShip, pEvent)
		return 0

	def UnDestroySystemDelay2(self, pObject, pEvent):
		pShip = App.ShipClass_GetObjectByID(None, pObject.GetObjID())
		#pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pObject.GetObjID()))
		if pShip:
			pInstance = findShipInstance(pShip)
			if pInstance and pInstance.__dict__.has_key("Automated Destroyed System Repair"):
			
				pSubsystemToRepair = App.ShipSubsystem_Cast(pEvent.GetSource())
				if not pSubsystemToRepair:
					return

				destroyedSystemName = pSubsystemToRepair.GetObjID()
				delay = 0.1
				if pInstance.__dict__['Automated Destroyed System Repair'].has_key("Time") and pInstance.__dict__['Automated Destroyed System Repair']["Time"] >= 0.0:
					delay = pInstance.__dict__['Automated Destroyed System Repair']["Time"]

				if not pInstance.__dict__.has_key("Automated Destroyed System Repair I"):
					pInstance.__dict__["Automated Destroyed System Repair I"] = {}

				if not pInstance.__dict__['Automated Destroyed System Repair I'].has_key(destroyedSystemName):
					pInstance.__dict__['Automated Destroyed System Repair I'][destroyedSystemName] = {}

				if pInstance.__dict__['Automated Destroyed System Repair I'][destroyedSystemName].has_key("Timer"):
					App.g_kTimerManager.DeleteTimer(pInstance.__dict__['Automated Destroyed System Repair I'][destroyedSystemName]['Timer'].GetObjID())
					del pInstance.__dict__['Automated Destroyed System Repair I'][destroyedSystemName]['Timer']

				pEvent2 = App.TGIntEvent_Create()
				pEvent2.SetEventType(eType)
				pEvent2.SetSource(pEvent.GetSource())
				pEvent2.SetDestination(pEvent.GetDestination())
				pEvent2.SetInt(int(destroyedSystemName))

				pTimer = App.TGTimer_Create()
				pTimer.SetTimerStart( App.g_kUtopiaModule.GetGameTime()+delay )
				pTimer.SetDelay(0)
				pTimer.SetDuration(0)
				pTimer.SetEvent(pEvent2)
				App.g_kTimerManager.AddTimer(pTimer)
				pInstance.__dict__['Automated Destroyed System Repair I'][destroyedSystemName]['Timer'] = pTimer

		pObject.CallNextHandler(pEvent)

	def UnDestroySystem(self, pEvent):

		pSubsystemToRepair = App.ShipSubsystem_Cast(pEvent.GetSource())
		if pSubsystemToRepair:
			pShip = pSubsystemToRepair.GetParentShip()
			if pShip:
				pInstance = findShipInstance(pShip)
				if pInstance and pInstance.__dict__.has_key("Automated Destroyed System Repair"):
					UnDestroySystem(pShip, pEvent)

		return 0

def UnDestroySystem(pObject, pEvent):
	debug(__name__ + ", UnDestroySystem")
	#pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pObject.GetObjID()))
	pShip = App.ShipClass_GetObjectByID(None, pObject.GetObjID())
	if pShip:
		pInstance = findShipInstance(pShip)
		if pInstance and pInstance.__dict__.has_key("Automated Destroyed System Repair"):
			
			destroyedSystemName = pEvent.GetInt()
			pShipSet = pShip.GetPropertySet()
			pShipList = pShipSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)

			iNumItems = pShipList.TGGetNumItems()
			pShipList.TGBeginIteration()
			for i in range(iNumItems):
				pShipProperty = App.SubsystemProperty_Cast(pShipList.TGGetNext().GetProperty())
				pSubsystem = pShip.GetSubsystemByProperty(pShipProperty)
				if pSubsystem.GetObjID() == destroyedSystemName:
					pSubsysCondition = pSubsystem.GetCondition()
					if (pSubsysCondition <= 0):
						pSubsystem.SetCondition(pSubsystem.GetMaxCondition())
						pSubsystem.SetCondition(1)
					break

			pShipList.TGDoneIterating()
			if pInstance.__dict__.has_key("Automated Destroyed System Repair I") and pInstance.__dict__['Automated Destroyed System Repair I'].has_key(destroyedSystemName) and pInstance.__dict__['Automated Destroyed System Repair I'][destroyedSystemName].has_key('Timer'):
				App.g_kTimerManager.DeleteTimer(pInstance.__dict__['Automated Destroyed System Repair I'][destroyedSystemName]['Timer'].GetObjID())
				del pInstance.__dict__['Automated Destroyed System Repair I'][destroyedSystemName]['Timer']

	pObject.CallNextHandler(pEvent)

def RefreshVisibleDamage(pShip, fast=0):
	pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())

	if pShip:
		if fast == 0:
			pShip.RemoveVisibleDamage() # this works nicely, but only once
			pShip.DamageRefresh(1)
		elif not (pShip.IsDead() or pShip.IsDying()):
			# The following is a lengthier progress, and could interfere with some SubModel scripts
			ShipScript = __import__(pShip.GetScript())
			ShipScript.LoadModel()
			kStats = ShipScript.GetShipStats()

                	if App.g_kLODModelManager.AreGlowMapsEnabled() == 1 and App.g_kLODModelManager.GetDropLODLevel() == 0:
                        	App.g_kLODModelManager.SetGlowMapsEnabled(0)
                        	App.g_kLODModelManager.SetGlowMapsEnabled(1)

			pShip.SetupModel(kStats['Name'])

			# Did not find why it gets the ship black until it fires or gets fired upon... so we'll create our own dumb way of fixing that, we create a torpedo at a ridiculous position and force it to fire, and then die
			from ftb.Tech.ATPFunctions import *

			point = pShip.GetWorldLocation()
			pHitPoint = App.TGPoint3()
			pHitPoint.SetXYZ(point.x, point.y, point.z)

			pVec = pShip.GetVelocityTG()
			pVec.Scale(0.001)
			pHitPoint.Add(pVec)

			mod = "Tactical.Projectiles.AutomaticSystemRepairDummy" 
			try:
				pTempTorp = FireTorpFromPointWithVector(pHitPoint, pVec, mod, pShip.GetObjID(), pShip.GetObjID(), __import__(mod).GetLaunchSpeed())
				pTempTorp.SetLifetime(0.0)
			except:
				print "You are missing 'Tactical.Projectiles.AutomaticSystemRepairDummy' torpedo on your install, without that a weird black-texture-until-firing-or-fired bug may happen"

			if App.g_kUtopiaModule.IsMultiplayer():
				MPSentReplaceModelMessage(pShip, sNewShipScript)

	return 0

def MPSentReplaceModelMessage(pShip, sNewShipScript):
        # Setup the stream.
        # Allocate a local buffer stream.
        kStream = App.TGBufferStream()
        # Open the buffer stream with a 256 byte buffer.
        kStream.OpenBuffer(256)
        # Write relevant data to the stream.
        # First write message type.
        kStream.WriteChar(chr(REPLACE_MODEL_MSG))

	try:
		from Multiplayer.Episode.Mission4.Mission4 import dReplaceModel
		dReplaceModel[pShip.GetObjID()] = sNewShipScript
	except ImportError:
		pass

	# send Message
	kStream.WriteInt(pShip.GetObjID())
	iLen = len(sNewShipScript)
	kStream.WriteShort(iLen)
	kStream.Write(sNewShipScript, iLen)

        pMessage = App.TGMessage_Create()
        # Yes, this is a guaranteed packet
        pMessage.SetGuaranteed(1)
        # Okay, now set the data from the buffer stream to the message
        pMessage.SetDataFromStream(kStream)
        # Send the message to everybody but me.  Use the NoMe group, which
        # is set up by the multiplayer game.
        # TODO: Send it to asking client only
        pNetwork = App.g_kUtopiaModule.GetNetwork()
        if not App.IsNull(pNetwork):
                if App.g_kUtopiaModule.IsHost():
                        pNetwork.SendTGMessageToGroup("NoMe", pMessage)
                else:
                        pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
        # We're done.  Close the buffer.
        kStream.CloseBuffer()

oAutomatedDestroyedSystemRepair = AutomatedDestroyedSystemRepairDef('Automated Destroyed System Repair')
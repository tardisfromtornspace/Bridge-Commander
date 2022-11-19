#################################################################################################################
#         AutoTargeting
#                          by USS Frontier
#################################################################################################################
# Purpose of this Foundation Tech plugin is to give ships a auto-targeting and firing solution.
# That means that ships equipped with this will be able to pursue and fire at their targets as usual, but the
# weapons (of the specified weapon system) that are not firing in the current target will seek out the closest enemy 
# target and fire at it.
#############################################
# Usage Example:  Add this to the dTechs attribute of your ShipDef, in the Ship plugin file
# but modify the values accordingly to what you want, and for actual values since the following is just a general example
"""
Foundation.ShipDef.Sovereign.dTechs = {
	"AutoTargeting": {
		"weapon system type like Pulse or Phaser or Torpedo": [number_of_maximum_possible_secondary_targets, ifcan_target_subsystems],
		}
	}
}
"""
#######################################################################

import App
import MissionLib
import Foundation
import FoundationTech
import string
import time

try:
	from bcdebug import debug
except:
	def debug(s):
		pass

dAutoTargetHandlers = {}

class AutoTargetingTech(FoundationTech.TechDef):
	def Attach(self, pInstance):
		#print "Attaching AutoTargeting to instance", pInstance
		debug(__name__ + ", Attach")
		global dAutoTargetHandlers
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		#print "AutoTargeting SHIP:", pShip
		if pShip != None:
			dMasterDict = pInstance.__dict__['AutoTargeting']
			#print "AutoTargeting DICT:", dMasterDict
			pATH = AutoTargetHandler(pShip)
			bCanStart = 0
			for sType in dMasterDict.keys():
				if sType == "Pulse":
					bCanStart = 1
					pATH.SetPulseTargets( dMasterDict[sType] )
				if sType == "Phaser":
					bCanStart = 1
					pATH.SetPhaserTargets( dMasterDict[sType] )
				if sType == "Torpedo":
					bCanStart = 1
					pATH.SetTorpTargets( dMasterDict[sType] )
			if bCanStart == 1:
				pATH.Initialize()
				dAutoTargetHandlers[pShip.GetObjID()] = pATH
			else:
				del pATH
		pInstance.lTechs.append(self)


	def Detach(self, pInstance):
		debug(__name__ + ", Detach")
		global dAutoTargetHandlers
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		if pShip != None:
			dMasterDict = pInstance.__dict__['AutoTargeting']
			if dAutoTargetHandlers.has_key(pShip.GetObjID()):
				pATH = dAutoTargetHandlers[pShip.GetObjID()]
				pATH.Close()
				del dAutoTargetHandlers[pShip.GetObjID()]
				del pATH
		pInstance.lTechs.remove(self)


class AutoTargetHandler:
	pATSButton = None    #AutoTargeting Switch
	ET_AT_SWITCH = None  #AutoTargeting Switch Event code

	def __init__(self, pShip):
		self.Ship = pShip
		self.pEventHandler = None
		self.pulseTargets = -1
		self.phaserTargets = -1
		self.torpTargets = -1
		self.Online = 1
		self.dSysTargs = {}
		self.dSysTimes = {}
	def Initialize(self):
		#print "initialized Auto Target Handler for ship", self.Ship.GetName()
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_WEAPON_FIRED, self.pEventHandler, "WeaponFired")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_WEAPON_FIRED, self.pEventHandler, "WeaponFired")
		#handling button
		pPlayer = App.Game_GetCurrentPlayer()
		if pPlayer.GetObjID() == self.Ship.GetObjID():
			if self.pATSButton == None:
				pBridge = App.g_kSetManager.GetSet("bridge")
				pTac = App.CharacterClass_GetObject(pBridge, "Tactical")
				if pTac == None:
					return
				pTacMenu = pTac.GetMenu()
				if pTacMenu == None:
					return
				self.ET_AT_SWITCH = App.Mission_GetNextEventType()
				pEvent = App.TGIntEvent_Create()
				pEvent.SetEventType(self.ET_AT_SWITCH)
				pEvent.SetDestination(pTacMenu)
				pEvent.SetInt(1)
				self.pATSButton = App.STButton_CreateW(App.TGString("AutoTargeting: ON"), pEvent)
				pTacMenu.AddChild(self.pATSButton)
				App.g_kEventManager.AddBroadcastPythonMethodHandler(self.ET_AT_SWITCH, self.pEventHandler, "ATSwitch_Click")
			else:
				self.pATSButton.SetVisible()
				self.pATSButton.SetEnabled()
	def ATSwitch_Click(self, pEvent):
		if self.Online == 1:
			self.Online = 0
			self.pATSButton.SetName(App.TGString("AutoTargeting: OFF"))
		elif self.Online == 0:
			self.Online = 1
			self.pATSButton.SetName(App.TGString("AutoTargeting: ON"))
	def Close(self):
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_WEAPON_FIRED, self.pEventHandler, "WeaponFired")
		pPlayer = App.Game_GetCurrentPlayer()
		if pPlayer.GetObjID() == self.Ship.GetObjID():
			if self.pATSButton != None:
				self.pATSButton.SetNotVisible()
				self.pATSButton.SetDisabled()
		#print "closed Auto Target Handler for ship", self.Ship.GetName()
	def SetPulseTargets(self, x):
		self.pulseTargets = x
	def SetPhaserTargets(self, x):
		self.phaserTargets = x
	def SetTorpTargets(self, x):
		self.torpTargets = x
	def WeaponFired(self, pEvent = None):
		#print "-----WEAPON FIRED EVENT-----"
		if self.Online != 1:
			#auto targeting is offline
			return
		if pEvent == None:
			#print "no event obj..."
			return
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		if pShip == None:
			#print "no ship obj..."
			return
		if pShip.GetObjID() != self.Ship.GetObjID():
			#print "ship not equal to our ship..."
			return
		pWeaponFired = App.Weapon_Cast(pEvent.GetSource())
		if pWeaponFired == None:
			#print "no weapon fired obj..."
			return
		pParentFired = pWeaponFired.GetParentSubsystem()
		if pParentFired == None:
			#print "no weapon fired parent subsystem obj..."
			return

		if self.pulseTargets != -1:
			pPulseSystem = pShip.GetPulseWeaponSystem()
			if pPulseSystem != None:
				if pParentFired.GetObjID() == pPulseSystem.GetObjID():
					# pulse fired
					self.AutoFireWeapons(pPulseSystem, self.pulseTargets[0], self.pulseTargets[1])
		if self.torpTargets != -1:
			pTorpSystem = pShip.GetTorpedoSystem()
			if pTorpSystem != None:
				if pParentFired.GetObjID() == pTorpSystem.GetObjID():
					# torp fired
					self.AutoFireWeapons(pTorpSystem, self.torpTargets[0], self.torpTargets[1])
		if self.phaserTargets != -1:
			pBeamSystem = pShip.GetPhaserSystem()
			if pBeamSystem != None:
				if pParentFired.GetObjID() == pBeamSystem.GetObjID():
					# phaser fired
					self.AutoFireWeapons(pBeamSystem, self.phaserTargets[0], self.phaserTargets[1])
	def AutoFireWeapons(self, pWeaponSystem, iNumTargetShips, bCanTargetSubsystems):
		pShip = pWeaponSystem.GetParentShip()
		if pShip == None:
			return
		lTargets = GetClosestEnemyShips(pShip, iNumTargetShips)
		#print "AutoFiringWeapons of", pShip.GetName()
		for pTarget in lTargets:
			#print "Firing", pWeaponSystem.GetName(), "at target", pTarget.GetName()
			pTargSystem = None
			if bCanTargetSubsystems != 0:
				iTargetID = pTarget.GetObjID()
				#print "CHECKING Subsystem for Target:", pTarget.GetName(), iTargetID
				if self.dSysTargs.has_key(iTargetID):
					#I honestly dunno if this is working correctly...
					fCurrentTime = time.clock()
					fTimePassed = fCurrentTime - self.dSysTimes[iTargetID]
					if fTimePassed < 30.0:
						pTargSystem = self.dSysTargs[iTargetID]
						#print "Continuing with:", pTargSystem.GetName()
					else:
						pTargSystem = GetTargetSubsystemInShip(pTarget)
						#print "Updated subsystem for:", pTargSystem.GetName()
						self.dSysTargs[iTargetID] = pTargSystem
						self.dSysTimes[iTargetID] = fCurrentTime
				else:
					pTargSystem = GetTargetSubsystemInShip(pTarget)
					#print "Initially acquired:", pTargSystem.GetName()
					self.dSysTargs[iTargetID] = pTargSystem
					self.dSysTimes[iTargetID] = time.clock()
			if pTargSystem != None:
				#pShip.SetTargetSubsystem(pTargSystem)
				vNiPos = pTargSystem.GetPosition()
				pPos = App.TGPoint3()
				pPos.SetXYZ(vNiPos.x, vNiPos.y, vNiPos.z)
				pWeaponSystem.StartFiring(pTarget, pPos)
			else:
				pWeaponSystem.StartFiring(pTarget)
			pWeaponSystem.SetForceUpdate(1)

oAutoTargeting = AutoTargetingTech("AutoTargeting")

###################
# HELPERS
###################

#slightly modified MakeEnemyShipList from Mleo's FoundationTech
def MakeEnemyShipObjectList(pShip):
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pEnemies = pMission.GetEnemyGroup()
	pFriendlies = pMission.GetFriendlyGroup()
	if pFriendlies.IsNameInGroup(pShip.GetName()):
		pEnemyGroup = pEnemies
	elif pEnemies.IsNameInGroup(pShip.GetName()):
		pEnemyGroup = pFriendlies
	else:
		pEnemyGroup = None

	lEnemyShips = []
	if pEnemyGroup != None:
		ObjTuple = pEnemyGroup.GetActiveObjectTupleInSet(pShip.GetContainingSet())
		if len(ObjTuple):
			for i in ObjTuple:
				pObj = App.ShipClass_Cast(i)
				if pObj:			
					lEnemyShips.append(pObj)

	return lEnemyShips

def GetClosestEnemyShips(pShip, iNumShips):
	pShip = App.ShipClass_Cast(pShip)
	pEnemyList = MakeEnemyShipObjectList(pShip)
	
	#this might be useless too, but leave it here anyway...
	try:
		if pEnemyList[pEnemyList.index(pShip)]:
			pEnemyList.remove(pShip)
	except:
		pass
	
	#now to the real deal
	EnemyDistDict = {}
	for pEnemyShip in pEnemyList:
		#Define the distance and check it after checking if pShip is cloaked
		fDistance = DistanceCheck(pShip, pEnemyShip)
		if not pEnemyShip.IsCloaked():
			if 0 < fDistance:
				pHull = pEnemyShip.GetHull()
				if pHull.GetCondition() > 0:
					EnemyDistDict[fDistance] = pEnemyShip
	lDistances = EnemyDistDict.keys()
	lDistances.sort()
	iDistAmount = len(lDistances)
	lRet = []
	if iDistAmount > 0:
		if iNumShips <= iDistAmount:
			for i in range(iNumShips):
				 lRet.append(  EnemyDistDict[ lDistances[i] ]  )
		elif iNumShips > iDistAmount:
			for i in range(  iNumShips - (iNumShips - iDistAmount)  ):
				 lRet.append(  EnemyDistDict[ lDistances[i] ]  )
	return lRet

def GetTargetSubsystemInShip(pShip):
	lSubsystems = []

	pPropSet = pShip.GetPropertySet()
	pSubsystemList = pPropSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
	pSubsystemList.TGBeginIteration()
	for i in range(pSubsystemList.TGGetNumItems()):
		pProperty = App.SubsystemProperty_Cast(pSubsystemList.TGGetNext().GetProperty())
		sName = pProperty.GetName().GetCString()
		pSubsystem = MissionLib.GetSubsystemByName(pShip, sName)
		if pSubsystem != None and pSubsystem.IsInvincible() == 0 and pSubsystem.IsTargetable() == 1:
				if App.HullProperty_Cast(pProperty) != None:
					lSubsystems.append(pSubsystem)
				elif App.PowerProperty_Cast(pProperty) != None:
					lSubsystems.append(pSubsystem)
				elif App.CloakingSubsystemProperty_Cast(pProperty) != None:
					lSubsystems.append(pSubsystem)
				elif App.RepairSubsystemProperty_Cast(pProperty) != None:
					lSubsystems.append(pSubsystem)
				elif App.SensorProperty_Cast(pProperty) != None:
					lSubsystems.append(pSubsystem)
				elif App.ShieldProperty_Cast(pProperty) != None:
					lSubsystems.append(pSubsystem)
				elif App.EngineProperty_Cast(pProperty) != None:
					lSubsystems.append(pSubsystem)
				if App.TorpedoTubeProperty_Cast(pProperty) != None:
					lSubsystems.append(pSubsystem)
				elif App.PulseWeaponProperty_Cast(pProperty) != None:
					lSubsystems.append(pSubsystem)
				elif App.PhaserProperty_Cast(pProperty) != None:
					lSubsystems.append(pSubsystem)
	pSubsystemList.TGDoneIterating()
	pSubsystemList.TGDestroy()
	
	pRet = None
	if len(lSubsystems) >= 1:
		pRet = lSubsystems[ App.g_kSystemWrapper.GetRandomNumber( len(lSubsystems) ) ]
	del lSubsystems
	return pRet

#a distance check, tah dah!!
def DistanceCheck(pObject1, pObject2):
	vDifference = pObject1.GetWorldLocation()
	vDifference.Subtract(pObject2.GetWorldLocation())

	return vDifference.Length()
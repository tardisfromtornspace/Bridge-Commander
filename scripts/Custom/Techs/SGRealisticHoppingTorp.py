# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# Version 1.2

# TODO: 1. Create Read Me
#	2. Create a clear guide on how to add this...
#
# Start on 2:
# At the bottom of your torpedo projectile file add this (Between the """ and """):
"""
try:
        sYieldName = "SG Hopping Torpedo"

        import FoundationTech
        import Custom.Techs.SGRealisticHoppingTorp

        oFire = Custom.Techs.SGRealisticHoppingTorp.oSGRealisticHoppingTorp
        FoundationTech.dOnFires[__name__] = oFire

        oYield = FoundationTech.oTechs[sYieldName]
        FoundationTech.dYields[__name__] = oYield


except:
	print "SG Hopping Torpedo script not installed, or you are missing Foundation Tech"
"""
from bcdebug import debug
import traceback

import App

import Foundation
import FoundationTech

from ftb.Tech.ATPFunctions import *
from math import *

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
            "Version": "1.2",
            "License": "LGPL",
            "Description": "Read the small title above for more info"
            }

NonSerializedObjects = (
"oSGRealisticHoppingTorp",
)

#slightly modified MakeEnemyShipList from Mleo's FoundationTech, borrowed from AutoTargeting (as well as the function "GetClosestEnemyShips") and modified again
def DistanceCheck(pObject1, pObject2, alternateWorldLocation=None):
	if alternateWorldLocation != None:
		vDifference = alternateWorldLocation
	else:
		vDifference = pObject1.GetWorldLocation()
	vDifference.Subtract(pObject2.GetWorldLocation())

	return vDifference.Length()

def MakeEnemyVisibleShipObjectList(pShip):
	return MakeTeamVisibleShipObjectList(pShip, 1)

def MakeFriendlyVisibleShipObjectList(pShip):
	return MakeTeamVisibleShipObjectList(pShip, 0)

def MakeTeamVisibleShipObjectList(pShip, enemy):
		
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pEnemies = pMission.GetEnemyGroup()
	pFriendlies = pMission.GetFriendlyGroup()
	pNeutrals = pMission.GetNeutralGroup()
	if pFriendlies.IsNameInGroup(pShip.GetName()):
		if enemy == 0:
			pFriendlyGroup = pFriendlies
		else:
			pFriendlyGroup = pEnemies
	elif pEnemies.IsNameInGroup(pShip.GetName()):
		if enemy == 0:
			pFriendlyGroup = pEnemies
		else:
			pFriendlyGroup = pFriendlies
	else:
		pFriendlyGroup = pNeutrals
	lFriendlyShips = []
	if pFriendlyGroup != None:
		pSet = pShip.GetContainingSet()
		if pSet:
			ObjTuple = pFriendlyGroup.GetActiveObjectTupleInSet(pSet)
			if len(ObjTuple):
				for i in ObjTuple:
					pObj = App.ShipClass_Cast(i)
					if pObj:			
						lFriendlyShips.append(pObj)

	return lFriendlyShips

def GetClosestEnemyShips(pShip, pEnemyList, iNumShips, alternateWorldLocation=None):
	pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
	
	try:
		if pEnemyList[pEnemyList.index(pShip)]:
			pEnemyList.remove(pShip)
	except:
		pass
	
	#now to the real deal
	EnemyDistDict = {}
	for pEnemyShip in pEnemyList:
		#Define the distance and check it after checking if pShip is cloaked
		pEnemyShipCh = App.ShipClass_GetObjectByID(None, pEnemyShip.GetObjID())
		if pEnemyShip and not pEnemyShip.IsDead() and not pEnemyShip.IsDying() and not pEnemyShip.IsCloaked():
			fDistance = DistanceCheck(pShip, pEnemyShip, alternateWorldLocation)
			if 0 < fDistance:
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

class SGRealisticHoppingTorpedo(FoundationTech.TechDef):

	ricochetChance = 100.0

	def __init__(self, name, dict = {}):
		FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
		self.lYields = []
		self.__dict__.update(dict)
		self.lFired = []

	def IsDrainYield(self):
		debug(__name__ + ", IsDrainYield")
		return 0

	def IsPhaseYield(self):
		debug(__name__ + ", IsDrainYield")
		return 0

	def OnYield(self, pShip, pInstance, pEvent, pTorp):
		#if(pEvent.IsHullHit()):
		#	return

		#if pTorp.GetObjID() in self.lFired:
		#	pTorp.SetLifetime(0)
		pTorp.SetLifetime(0)

		#pShipID = pShip.GetObjID()

		#pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))

		pShipParentID = pTorp.GetParentID()

		pShip2 = App.ShipClass_GetObjectByID(None, pShipParentID)
		if not pShip2 :
			return

		pTorpLocation = pTorp.GetWorldLocation()

		pShipTargetID = pTorp.GetTargetID()
		pShipTarget = App.ShipClass_GetObjectByID(None, pShipTargetID)

		if (not pShipTarget) or pShipTarget.IsDead() or pShipTarget.IsDying():
			# 1.2 addition, let's look for new targets, if parent ship has enough energy!

			batt_chg = 0
			energyCommited = 0.0

			pPower = pShip2.GetPowerSubsystem()
			if pPower:
				batt_chg = pPower.GetMainBatteryPower()
				#batt_limit = pPower.GetMainBatteryLimit()
			
			pWeaponSystem2 = pShip2.GetTorpedoSystem()
			pWeaponSystem3 = pShip2.GetPulseWeaponSystem()


			if pWeaponSystem2:
				energyCommited = pWeaponSystem2.GetPowerPercentageWanted()
			elif pWeaponSystem3:
				energyCommited = pWeaponSystem3.GetPowerPercentageWanted()

			if batt_chg >= 999 and energyCommited > 1.2:
				# Look for the nearest enemy

				closestShips = []
				if not pShipTarget:
					enemyShipList = MakeEnemyVisibleShipObjectList(pShip2)
					if enemyShipList and len(enemyShipList) > 0: 
						closestShips = GetClosestEnemyShips(pShip2, enemyShipList, 1, pTorpLocation)
				else:
					#extra measure, shields down after it begins to die
					#pShipTargetShields = pShipTarget.GetShields()
					#if pShipTargetShields:
					#	pShipTargetShields.TurnOff()
					enemyShipList = MakeEnemyVisibleShipObjectList(pShip2)# MakeFriendlyVisibleShipObjectList(pShipTarget) works until an AI decides to switch sides or give up!
					if enemyShipList and len(enemyShipList) > 0:
						closestShips = GetClosestEnemyShips(pShipTarget, enemyShipList, 1, pTorpLocation)

				if closestShips and len(closestShips) > 0:
					#print "switched targets, from ", pShipTarget.GetName(), "of id ", pShipTargetID ," to"
					pShipTarget = closestShips[0]
					pShipTargetID = pShipTarget.GetObjID()
					pTorp.SetTarget(pShipTargetID)
					#print "new target targets", pShipTarget.GetName(), "of id ", pShipTargetID
				else:
					# Recall! Then if we can replenish the drone stash, better!
					# since this allows us to actually bring the torps towards the same target, but cannot register the hit at all, we'll have to make the torpedo replenisment before the actual recall :(
					pShipTarget = pShip2
					pShipTargetID = pShipParentID
					pTorp.SetTarget(pShipParentID)

					pTorpSys = pShip2.GetTorpedoSystem()
					if(pTorpSys):
						# Find proper torps..
						mod = pTorp.GetModuleName()
						banana = __import__(mod)
						if hasattr(mod, "GetName"):
							pcName = mod.GetName()
						else:
							pcName = "Drone"
						iNumTypes = pTorpSys.GetNumAmmoTypes()
						for iType in range(iNumTypes):
							pTorpType = pTorpSys.GetAmmoType(iType)

							if (pTorpType.GetAmmoName() == pcName):
								iLoad = pTorpSys.GetNumAvailableTorpsToType(iType)
								pTorpSys.LoadAmmoType(iType, 1) # this adds + 1 to that ammo
								break



		if not pShipTarget:
			return

		myChance = App.g_kSystemWrapper.GetRandomNumber(100)
		if myChance > self.ricochetChance:
			return

                pHitPoint = self.ConvertPointNiToTG(pTorpLocation)

		pVec = pTorp.GetVelocityTG()
                
		pHitPoint.Add(pVec)

		mod = pTorp.GetModuleName()
		if(self.__dict__.has_key("SubTorp")):
			mod = self.SubTorp

		pTempTorp = FireTorpFromPointWithVector(pHitPoint, pVec, mod, pShipTargetID, pShipParentID, __import__(mod).GetLaunchSpeed())
                pTempTorp.SetLifetime(15.0)
		self.lFired.append(pTempTorp.GetObjID())

	def AddTorpedo(self, path, myPercent):
		FoundationTech.dYields[path] = self
		self.ricochetChance = myPercent
		

	def ConvertPointNiToTG(self, point):
		retval = App.TGPoint3()
		retval.SetXYZ(point.x, point.y, point.z)
		return retval

	def IsInList(item, list):
		for i in list:
			if item == i:
				return 1
		return 0

oSGRealisticHoppingTorp = SGRealisticHoppingTorpedo("SG Hopping Torpedo")

# Just a few standard torps I know of that are Phased... 
# All but the first one, that is the first torp on my test bed ship...
# Should be commented out on release...
# oSGRealisticHoppingTorp.AddTorpedo("Tactical.Projectiles.Drones", 0.75)

print "SG Hopping Torp ready"

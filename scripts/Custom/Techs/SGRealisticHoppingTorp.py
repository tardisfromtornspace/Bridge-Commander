# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL

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

import App

import Foundation
import FoundationTech

from ftb.Tech.ATPFunctions import *
from math import *

NonSerializedObjects = (
"oSGRealisticHoppingTorp",
)

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

	def OnYield(self, pShip, pInstance, pEvent, pTorp):
		#if(pEvent.IsHullHit()):
		#	return

		#if pTorp.GetObjID() in self.lFired:
		#	pTorp.SetLifetime(0)
		pTorp.SetLifetime(0)

		#pShipID = pShip.GetObjID()

		#pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))
		if not pShip :
			return

		myChance = App.g_kSystemWrapper.GetRandomNumber(100)
		print myChance
		if myChance > self.ricochetChance:
			return
                pHitPoint = self.ConvertPointNiToTG(pTorp.GetWorldLocation())

		pVec = pTorp.GetVelocityTG()
                
		pHitPoint.Add(pVec)

		mod = pTorp.GetModuleName()
		if(self.__dict__.has_key("SubTorp")):
			mod = self.SubTorp

		pShipID = pTorp.GetParentID()

		pShip2 = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))
		if not pShip2 :
			return

		pTempTorp = FireTorpFromPointWithVector(pHitPoint, pVec, mod, pTorp.GetTargetID(), pTorp.GetParentID(), __import__(mod).GetLaunchSpeed())
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

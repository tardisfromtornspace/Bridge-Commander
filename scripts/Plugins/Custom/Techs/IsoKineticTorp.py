# TODO: 1. Create Read Me
#	2. Create a clear guide on how to add this...
#
# Start on 2:
# At the bottom of your torpedo projectile file add this (Between the """ and """):
"""
try:
	modIsoKineticTorp = __import__("Custom.Techs.IsoKineticTorp")
	if(modIsoKineticTorp):
		modIsoKineticTorp.oIsoKineticTorp.AddTorpedo(__name__)
except:
	print "IsoKinetic Torpedo script not installed, or you are missing Foundation Tech"
"""

import App
try:
	import Foundation
	import FoundationTech

	from ftb.Tech.ATPFunctions import *
	from math import *

	class IsoKineticTorpedo(FoundationTech.TechDef):
		def __init__(self, name, dict = {}):
			FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
			self.lYields = []
			self.__dict__.update(dict)
			self.lFired = []

		def OnYield(self, pShip, pInstance, pEvent, pTorp):
			if(pEvent.IsHullHit()):
				return

			pShipID = pShip.GetObjID()
			pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))
			if not pShip:
				return

			pHitPoint = ConvertPointNiToTG(pEvent.GetWorldHitPoint())

			pVec = pTorp.GetVelocityTG()
			pDisLoc = pTorp.GetVelocityTG()
			pDisLoc.Scale(-0.0005)
			pHitPoint.Add(pDisLoc)

			mod = pTorp.GetModuleName()

			pTempTorp = FireTorpFromPointWithVector(pHitPoint, pVec, mod, pTorp.GetTargetID(), pTorp.GetParentID(), __import__(mod).GetLaunchSpeed())

		def AddTorpedo(self, path):
			FoundationTech.dYields[path] = self

	def ConvertPointNiToTG(point):
		retval = App.TGPoint3()
		retval.SetXYZ(point.x, point.y, point.z)
		return retval

	def IsInList(item, list):
		for i in list:
			if item == i:
				return 1
		return 0

	oIsoKineticTorp = IsoKineticTorpedo("Isokinetic Cannon Round")

except:
	print "FoundationTech, or the FTB mod, or both are not installed, \nIsoKinetic Torpedoes are there for NOT enabled or present in your current BC installation"

# TODO: 1. Create Read Me
#	2. Create a clear guide on how to add this...
#
# Start on 2:
# At the bottom of your torpedo projectile file add this (Between the """ and """):
"""
try:
	modPhasedTorp = __import__("Custom.Techs.PhasedTorp")
	if(modPhasedTorp):
		modPhasedTorp.oPhasedTorp.AddTorpedo(__name__)
except:
	print "Phased Torpedo script not installed, or you are missing Foundation Tech"
"""

import App
try:
	import Foundation
	import FoundationTech

	from ftb.Tech.ATPFunctions import *
	from math import *

	class PhasedTorpedo(FoundationTech.TechDef):
		def __init__(self, name, dict = {}):
			FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
			self.lYields = []
			self.__dict__.update(dict)
			self.lFired = []

		def OnYield(self, pShip, pInstance, pEvent, pTorp):
			if(pEvent.IsHullHit()):
				return

			#if pTorp.GetObjID() in self.lFired:
			#	pTorp.SetLifetime(0)
			pTorp.SetLifetime(0)

			pShipID = pShip.GetObjID()

			pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))
			if not pShip:
				return

			pHitPoint = ConvertPointNiToTG(pEvent.GetWorldHitPoint())

			pVec = pTorp.GetVelocityTG()
			pVec.Scale(pEvent.GetRadius())
			pHitPoint.Add(pVec)

			mod = pTorp.GetModuleName()
			if(self.__dict__.has_key("SubTorp")):
				mod = self.SubTorp

			pTempTorp = FireTorpFromPointWithVector(pHitPoint, pVec, mod, pTorp.GetTargetID(), pTorp.GetParentID(), __import__(mod).GetLaunchSpeed())
			self.lFired.append(pTempTorp.GetObjID())

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

	oPhasedTorp = PhasedTorpedo("Phased Torpedo")
	# Just a few standard torps I know of that are Phased... 
	# All but the first one, that is the first torp on my test bed ship...
	# Should be commented out on release...
	oPhasedTorp.AddTorpedo("Tactical.Projectiles.PhasedPlasma")
except:
	print "FoundationTech, or the FTB mod, or both are not installed, \nPhased Torpedoes are there for NOT enabled or present in your current BC installation"

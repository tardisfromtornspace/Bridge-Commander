# TODO: 1. Create Read Me
#	2. Create a clear guide on how to add this...
#
# Start on 2:
# At the bottom of your torpedo projectile file add this (Between the """ and """):
# You can add a secondary torpedo version by copying the file and adding "_P" to the end of the new file name, which will be the torpedo after the shield
"""
try:
	modChronitonTorpe = __import__("Custom.Techs.ChronitonTorpe")
	if(modChronitonTorpe):
		modChronitonTorpe.oChronitonTorpe.AddTorpedo(__name__)
except:
	print "Chroniton Torpedo script not installed, or you are missing Foundation Tech"
"""
# You can also add your ship to an immunity list, not only the one below, in order to keep the files unaltered... just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"ChronitonTorpe Immune": 1
}
"""

import App
try:
	import Foundation
	import FoundationTech

	from ftb.Tech.ATPFunctions import *
	from math import *

	class ChronitonTorpedo(FoundationTech.TechDef):
		def __init__(self, name, dict = {}):
			FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
			self.lYields = []
			self.__dict__.update(dict)
			self.lFired = []

                def IsChronTorpYield(self):
			return 1

		def OnYield(self, pShip, pInstance, pEvent, pTorp):
			if(pEvent.IsHullHit()):
				return

			pTorp.SetLifetime(0)

			pShipID = pShip.GetObjID()

			pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))
			if not pShip:
				return

			pHitPoint = ConvertPointNiToTG(pEvent.GetWorldHitPoint())

			pVec = pTorp.GetVelocityTG()
			pVec.Scale(0.001)
			pHitPoint.Add(pVec)

			mod = pTorp.GetModuleName()

			try:
				projectile = mod + "_P"
				torpedoScript = __import__(projectile)
				mod = projectile
			except:
				mod = pTorp.GetModuleName()

			print mod

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

	oChronitonTorpe = ChronitonTorpedo("Chroniton Torpedo")
	# Just a few standard torps I know of that are Phased... 
	# All but the first one, that is the first torp on my test bed ship...
	# Should be commented out on release...
	oChronitonTorpe.AddTorpedo("Tactical.Projectiles.JLSKrenimChroniton")
except:
	print "FoundationTech, or the FTB mod, or both are not installed, \nChroni Torpedoes are there for NOT enabled or present in your current BC installation"

class ChronitonTorpeDef(FoundationTech.TechDef):

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		isThis = 0
		try:
			isThis = oYield.IsChronTorpYield()
		except:
			isThis = 0
		if oYield and isThis:
			return 1

	def Attach(self, pInstance):
		pInstance.lTorpDefense.append(self)


oChronitonTorpeImmunity = ChronitonTorpeDef('ChronitonTorpe Immune')




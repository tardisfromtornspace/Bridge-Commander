# Amodfication of a modification, by Alex SL Gato (CharaToLoki)
#
# TODO: 1. Create Read Me
#	2. Create a clear guide on how to add this...
#
# Start on 2:
# At the bottom of your torpedo projectile file add this (Between the """ and """):
# Note, your SpeciesToTorp value must be set to PHASEDPLASAMA for it to work
# pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)
"""
try:
	modTransphasicTorp = __import__("Custom.Techs.TransphasicTorp")
	if(modTransphasicTorp):
		modTransphasicTorp.oTransphasicTorp.AddTorpedo(__name__)
except:
	print "Transphasic Torpedo script not installed, or you are missing Foundation Tech"
"""
# You can also add your ship to an immunity list, not only the one below, in order to keep the files unaltered... just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"Transphasic Torpedo Immune": 1
}
"""

import App

import string

global lImmuneTransphasicShips # Some ships immune to this blow
lImmuneTransphasicShips = (
                "Aeon",
                "alexander",
                "ArmoredVoyager",
                "janeway",
                "JLSAeon",
                "Jubayr",
                "kirk",
                "mars",
                "saturn",
                "Tardis",
                "Thant",
                "VulcanXRT55D",
                "Wells",
                "32crossfield",
                "32C_crossfield",
                )


try:
	import Foundation
	import FoundationTech

	from ftb.Tech.ATPFunctions import *
	from math import *

	class TransphasicTorpedo(FoundationTech.TechDef):
		def __init__(self, name, dict = {}):
			FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
			self.lYields = []
			self.__dict__.update(dict)
			self.lFired = []

                def IsTransphasicYield(self):
			return 1

		def OnYield(self, pShip, pInstance, pEvent, pTorp):
			if(pEvent.IsHullHit()):
				return

			if not pShip:
				return

			#if pTorp.GetObjID() in self.lFired:
			#	pTorp.SetLifetime(0)
			#pTorp.SetLifetime(0)

			# Immunities, better here so all transphased things are consistent with each other
			global lImmuneTransphasicShips
			sScript     = pShip.GetScript()
			sShipScript = string.split(sScript, ".")[-1]
			if sShipScript in lImmuneTransphasicShips:
				return

                        pTorp.SetLifetime(100)

			pShipID = pShip.GetObjID()

                        pHitPoint = ConvertPointNiToTG(pTorp.GetWorldLocation())

			pVec = pTorp.GetVelocityTG()
			pVec.Scale(0.001)
			pHitPoint.Add(pVec)

			mod = pTorp.GetModuleName()
			if(self.__dict__.has_key("SubTorp")):
				mod = self.SubTorp

			pTempTorp = FireTorpFromPointWithVector(pHitPoint, pVec, mod, pTorp.GetTargetID(), pTorp.GetParentID(), __import__(mod).GetLaunchSpeed())
                        pTempTorp.SetLifetime(15.0)
			self.lFired.append(pTempTorp.GetObjID())
			pTempTorp.UpdateNodeOnly() 

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

	oTransphasicTorp = TransphasicTorpedo("Transphasic Torpedo")
	# Just a few standard torps I know of that are Transphasic... 
	# All but the first one, that is the first torp on my test bed ship, should be commented out on release...
	oTransphasicTorp.AddTorpedo("Tactical.Projectiles.Transphasic")
except:
	print "FoundationTech, or the FTB mod, or both are not installed, \nTrasphasic Torpedoes are there but NOT enabled or present in your current BC installation"


class TransphasicTorpedoDef(FoundationTech.TechDef):

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		if oYield and oYield.IsTransphasicYield():
			return 1

	def Attach(self, pInstance):
		pInstance.lTorpDefense.append(self)


oTransphasicTorpedoImmunity = TransphasicTorpedoDef('Transphasic Torpedo Immune')
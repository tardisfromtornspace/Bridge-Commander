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
	modExistentialUntetheringTorp = __import__("Custom.Techs.ExistentialUntetheringTorp")
	if(modExistentialUntetheringTorp):
		modExistentialUntetheringTorp.oExistentialUntetheringTorp.AddTorpedo(__name__)
except:
	print "Existential Untethering Torpedo script not installed, or you are missing Foundation Tech"
"""
# You can also add your ship to an immunity list, not only the one below, in order to keep the files unaltered... just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"Existential Untethering Immune": 1
}
"""

import App

import string

global lImmuneExistentialUntetheringShips # Some ships immune to this blow
lImmuneExistentialUntetheringShips = (
                )


try:
	import Foundation
	import FoundationTech

	from ftb.Tech.ATPFunctions import *
	from math import *

	class ExistentialUntetheringTorpedo(FoundationTech.TechDef):
		def __init__(self, name, dict = {}):
			FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
			self.lYields = []
			self.__dict__.update(dict)
			self.lFired = []

                def IsExistentialUntetheringYield(self):
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
			global lImmuneExistentialUntetheringShips
			sScript     = pShip.GetScript()
			sShipScript = string.split(sScript, ".")[-1]
			if sShipScript in lImmuneExistentialUntetheringShips:
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

	def accionDummy(self):
		
		pEnterSound = App.TGSound_Create("sfx/Weapons/ExistentialUntethering.wav", "ExistentialUntethering", 1)
		pEnterSound.SetSFX(0) 
		pEnterSound.SetInterface(1)

		App.g_kSoundManager.PlaySound("ExistentialUntethering")
		return 0

	oExistentialUntetheringTorp = ExistentialUntetheringTorpedo("Existential Untethering Torpedo")
	# Just a few standard torps I know of that are Existential Untethering... 
	# All but the first one, that is the first torp on my test bed ship, should be commented out on release...
	oExistentialUntetheringTorp.AddTorpedo("Tactical.Projectiles.ExistentialUnteatheringDevice")
	oExistentialUntetheringTorp.AddTorpedo("Tactical.Projectiles.DimenopointUnphaseDevice")
	oExistentialUntetheringTorp.AddTorpedo("Tactical.Projectiles.ExileIIExistentialUntethering")
except:
	print "FoundationTech, or the FTB mod, or both are not installed, \nExistential Untethering Torpedoes are there but NOT enabled or present in your current BC installation"


class ExistentialUntetheringTorpedoDef(FoundationTech.TechDef):

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		isThis = 0
		try:
			isThis = oYield.IsExistentialUntetheringYield()
		except:
			isThis = 0
		if oYield and isThis:
			return 1

	def Attach(self, pInstance):
		pInstance.lTorpDefense.append(self)


oExistentialUntetheringTorpedoImmunity = ExistentialUntetheringTorpedoDef('Existential Untethering Immune')
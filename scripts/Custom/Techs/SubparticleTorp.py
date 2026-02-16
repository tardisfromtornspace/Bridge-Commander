# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# A modfication of a modification, last modification by Alex SL Gato (CharaToLoki)
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
	modSubparticleTorp = __import__("Custom.Techs.SubparticleTorp")
	if(modSubparticleTorp):
		modSubparticleTorp.oSubparticleTorp.AddTorpedo(__name__)
except:
	print "Subparticle Torpedo script not installed, or you are missing Foundation Tech"
"""
# You can also add your ship to an immunity list, not only the one below, in order to keep the files unaltered... just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"Subparticle Torpedo Immune": 1
}
"""

import App

import string

global lImmuneSubparticleShips # Some ships immune to this blow
lImmuneSubparticleShips = (
                "Aeon",
                "alexander",
                "ArmoredVoyager",
                "DarkSongClass",
                "DarkWells",
                "DarkWellsRef",
		"EnterpriseM",
                "HGWells",
                "janeway",
                "JLSAeon",
                "Jubayr",
                "kirk",
                "mars",
                "Perpetuality",
                "saturn",
                "Sorites",
                "Tardis",
                "Thant",
                "VulcanXRT55D",
                "Wells",
                "32C_crossfield",
                )


try:
	import Foundation
	import FoundationTech

	from ftb.Tech.ATPFunctions import *
	from math import *

	class SubparticleTorpedo(FoundationTech.TechDef):
		def __init__(self, name, dict = {}):
			FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
			self.lYields = []
			self.__dict__.update(dict)
			self.lFired = []

		def IsSubparticleYield(self):
			return 1

		def IsPhaseYield(self):
			return 0

		def IsDrainYield(self):
			return 0

		def OnYield(self, pShip, pInstance, pEvent, pTorp):
			if(pEvent.IsHullHit()):
				return

			if not pShip:
				return

			#if pTorp.GetObjID() in self.lFired:
			#	pTorp.SetLifetime(0)
			#pTorp.SetLifetime(0)

			# Immunities, better here so all transphased things are consistent with each other
			global lImmuneSubparticleShips
			sScript     = pShip.GetScript()
			sShipScript = string.split(sScript, ".")[-1]
			if sShipScript in lImmuneSubparticleShips:
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
			else:
				try:
					projectile = mod + "_P"
					torpedoScript = __import__(projectile)
					mod = projectile
				except:
					mod = pTorp.GetModuleName()

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

	oSubparticleTorp = SubparticleTorpedo("Subparticle Torpedo")
	# Just a few standard torps I know of that are Subparticle... 
	# All but the first one, that is the first torp on my test bed ship, should be commented out on release...
	#oSubparticleTorp.AddTorpedo("Tactical.Projectiles.w_Subparticle")
except:
	print "FoundationTech, or the FTB mod, or both are not installed, \nTrasphasic Torpedoes are there but NOT enabled or present in your current BC installation"


class SubparticleTorpedoDef(FoundationTech.TechDef):

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		isThis = 0

		if oYield and hasattr(oYield, "IsSubparticleYield"):
			isThis = oYield.IsSubparticleYield()

		if oYield and isThis:
			return 1

	def Attach(self, pInstance):
		pInstance.lTorpDefense.append(self)


oSubparticleTorpedoImmunity = SubparticleTorpedoDef('Subparticle Torpedo Immune')
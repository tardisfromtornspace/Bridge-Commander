# TODO: 1. Create Read Me
#	2. Create a clear guide on how to add this...
#
# Start on 2:
# At the bottom of your torpedo projectile file add this (Between the """ and """):
"""
def GetPercentage():
	return 0.15 # This is the percentage all the shields will drop from 0.00 (0%) to 1.00 (100%)

try:
	modRefluxWeapon = __import__("Custom.Techs.RefluxWeapon")
	if(modRefluxWeapon):
		modRefluxWeapon.oRefluxWeapon.AddTorpedo(__name__, GetPercentage())
except:
	print "Reflux Weapon script not installed, or you are missing Foundation Tech"
"""
# You can also add your ship to an immunity list, not only the one below, in order to keep the files unaltered... just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"Reflux Weapon Immune": 1
}
"""
# You can also add your ship to a resistance or extra-weakness list, in order to keep the files unaltered... just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev and "5" with the desired amount from 0 to 1000000 (100% drain)
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"Reflux Weapon": 5
}
"""

import App

import string

global lImmuneRefluxWeaponShips # Some ships immune to this blow
lImmuneRefluxWeaponShips = (
                "Tardis",
                )

try:
	import Foundation
	import FoundationTech

	from ftb.Tech.ATPFunctions import *
	from math import *

	class RefluxWeapon(FoundationTech.TechDef):
                lThePercentage = 0.0

		def __init__(self, name, dict = {}):
			FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
			self.lYields = []
			self.__dict__.update(dict)
			self.lFired = []

                def IsRefluxWeaponYield(self):
			return 1

		def OnYield(self, pShip, pInstance, pEvent, pTorp):
			if(pEvent.IsHullHit()):
				return

			# Immunities, better here so all Reflux Weapon things are consistent with each other
			global lImmuneRefluxWeaponShips
			sScript     = pShip.GetScript()
			sShipScript = string.split(sScript, ".")[-1]
			if sShipScript in lImmuneRefluxWeaponShips:
				return

			# do the shield drain
			minYield = pEvent.GetDamage()
			Percentage = "a"
			try:
				Percentage = pInstance.__dict__['Reflux Weapon'] # This means the defender can modulate the percent drain, even heal from it.
				Percentage = (Percentage / 1000000.0) # User values are on a 1-1000000 range, we use 0.000000-1.000000 range
			except:
				Percentage = self.lThePercentage
				if not Percentage or Percentage == 0.0:
					Percentage = 0.01 # Default
			print Percentage

			pShields = pShip.GetShields()
			for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
				pShieldStatus = pShields.GetCurShields(shieldDir)
				pShieldChunk  = (pShields.GetMaxShields(shieldDir) * Percentage)
				if (minYield > pShieldChunk): # From experience this also makes the blow doubly crippling to the originally-hit shield par
					pShieldChunk=minYield
				fShieldStatus = pShieldStatus-pShieldChunk
				if (fShieldStatus < 0):
					fShieldStatus= 0
				pShields.SetCurShields(shieldDir, fShieldStatus)
			return

                        

		def AddTorpedo(self, path, myPercent):
			FoundationTech.dYields[path] = self
			self.lThePercentage = myPercent

	def IsInList(item, list):
		for i in list:
			if item == i:
				return 1
		return 0

	oRefluxWeapon = RefluxWeapon("Reflux Weapon")
	# Just a few standard torps I know of that are Reflux Weapons... 
	# All but the first one, that is the first torp on my test bed ship...
	# Should be commented out on release...
	# oRefluxWeapon.AddTorpedo("Tactical.Projectiles.N_Reflux_Quantum", 0.15)
except:
	print "FoundationTech, or the FTB mod, or both are not installed, \nReflux Weapons are there for NOT enabled or present in your current BC installation"

class RefluxWeaponDef(FoundationTech.TechDef):

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		isThis = 0
		try:
			isThis = oYield.IsRefluxWeaponYield()
		except:
			isThis = 0
		if oYield and isThis:
			return 1

	def Attach(self, pInstance):
		pInstance.lTorpDefense.append(self)


oRefluxWeaponImmunity = RefluxWeaponDef('Reflux Weapon Immune')
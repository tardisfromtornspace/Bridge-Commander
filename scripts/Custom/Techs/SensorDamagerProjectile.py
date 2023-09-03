#################################################################################################################
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
#         SensorDamagerProjectile.py by Alex SL Gato
#         Version 0.1
#         3rd September 2023
#         Based strongly on ChronitonTorpe.py by Alex Sl Gato (not to confuse with another ChronitonTorpe file) and RefluxWeapon by Alex SL Gato, both variants of a modified scripts\Custom\Techs\PhasedTorp.py by narrowcwfe, Alex SL Gato and (primarily) the FoundationTechnologies team.
#         Also based strongly on PointDefence.py by Defiant
#################################################################################################################
# TODO: 1. Create Read Me
#	2. Create a clear guide on how to add this...
#
# Start on 2:
# At the bottom of your torpedo projectile file add this (Between the """ and """):
"""
def GetPercentage():
	return 0.5 # This is the percentage of current sensor array power all the sensor arrays will drop from 0.00 (0%) to 1.00 (100%)

try:
	modSensorDamagerProjectile = __import__("Custom.Techs.SensorDamagerProjectile")
	if(modSensorDamagerProjectile):
		modSensorDamagerProjectile.oSensorDamagerProjectile.AddTorpedo(__name__, GetPercentage())
except:
	print "SensorDamagerProjectile script not installed, or you are missing Foundation Tech"
"""
# You can also add your ship to an immunity list, not only the one below, in order to keep the files unaltered... just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"SensorDamagerProjectile Immune": 1
}
"""
# You can also add your ship to a resistance or extra-weakness list, in order to keep the files unaltered... just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev and "5" with the desired amount from 0 to 1000000 (100% drain)
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"Sensor Damager Projectile": 500000
}
"""

import App
try:
	import Foundation
	import FoundationTech

	from ftb.Tech.ATPFunctions import *
	from math import *

	class SensorDamagerProjectile(FoundationTech.TechDef):
		lThePercentage = 0.0

		def __init__(self, name, dict = {}):
			FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
			self.lYields = []
			self.__dict__.update(dict)
			self.lFired = []

		def IsSensorDamagerProjectileYield(self):
			return 1

		def IsPhaseYield(self): # These two are kept here to avoid breaking the base Breen Drainer Immunity script in KM
			return 0

		def IsDrainYield(self): # These two are kept here to avoid breaking the base Breen Drainer Immunity script in KM
			return 0

		def OnYield(self, pShip, pInstance, pEvent, pTorp):
			if(pEvent.IsHullHit()):
				return

			pTorp.SetLifetime(0)

			if not pShip:
				return

			# do the sensor array drain
			Percentage = "a"
			try:
				Percentage = pInstance.__dict__['Sensor Damager Projectile'] # This means the defender can modulate the percent drain, even heal from it.
				Percentage = (Percentage / 1000000.0) # User values are on a 1-1000000 range, we use 0.000000-1.000000 range
			except:
				Percentage = self.lThePercentage
				if not Percentage or Percentage == 0.0:
					Percentage = 0.01 # Default

			pSensorArray = pShip.GetSensorSubsystem()
			self.HurtSubsystemPercentage(self, pSensorArray, Percentage)


		def AddTorpedo(self, path, myPercent):
			FoundationTech.dYields[path] = self
			self.lThePercentage = myPercent

		def HurtSubsystemPercentage(self, pSubsystem, fDamage):
			if not pSubsystem:
				return

			currentPercentage = pSubsystem.GetConditionPercentage()*fDamage
			if currentPercentage < 0.0:
				currentPercentage = 0.0 # not meant to instantly destroy the sensor array, but any hit after that will
			elif currentPercentage > 1.0:
				currentPercentage = 1.0
			pSubsystem.SetConditionPercentage(currentPercentage)

			iChildren = pSubsystem.GetNumChildSubsystems()
			if iChildren > 0:
				for iIndex in range(iChildren):
					pChild = pSubsystem.GetChildSubsystem(iIndex)
					self.HurtSubsystemPercentage(pSubsystem, fDamage)

			return

	def IsInList(item, list):
		for i in list:
			if item == i:
				return 1
		return 0

	oSensorDamagerProjectile = SensorDamagerProjectile("Sensor Damager Projectile")
	# Just a few standard torps I know of that are Phased... 
	# All but the first one, that is the first torp on my test bed ship...
	# Should be commented out on release...
	# oSensorDamagerProjectile.AddTorpedo("Tactical.Projectiles.Dummy", 0.5)
except:
	print "FoundationTech, or the FTB mod, or both are not installed, \nSensor Damager Projectiles are there but NOT enabled or present in your current BC installation"

class SensorDamagerProjectileDef(FoundationTech.TechDef):

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		if oYield and hasattr(oYield, "SensorDamagerProjectileYield") and oYield.SensorDamagerProjectileYield():
			return 1

	def Attach(self, pInstance):
		pInstance.lTorpDefense.append(self)


oSensorDamagerProjectileImmunity = SensorDamagerProjectileDef("SensorDamagerProjectile Immune")




#################################################################################################################
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
#         DampeningAOEDefensiveField.py by Alex SL Gato
#         Version 1.0.1
#         25th July 2023
#         Based strongly on scripts\Custom\DS9FX\DS9FXPulsarFX\PulsarManager by USS Sovereign, and slightly on TractorBeams.py, Inversion Beam and Power Drain Beam 1.0 by MLeo Daalder, Apollo, and Dasher; some team-switching torpedo by LJ; and GraviticLance by Alex SL Gato, which was based on FiveSecsGodPhaser by USS Frontier, scripts/ftb/Tech/TachyonProjectile by the FoundationTechnologies team, and scripts/ftb/Tech/FedAblativeArmour by the FoundationTechnologies team.
#                          
#################################################################################################################
# This tech gives a ship the ability to siphon energy from enemies or synergically give it to friends in an area. In both cases some energy can be given to you.
# Usage Example:  Add this to the dTechs attribute of your ShipDef, in the Ship plugin file (replace "Sovereign" with the proper abbrev).
# Distance: Range of effect of this ability. Logically cannot be equal or less than 0, so if you don't want this ship to drain, set it to 0. Default is 50 km.
# Power: How much power you drain from enemies. Set to negative to add power to friendlies. If you don't want this ship to drain, set it to 0. Default 50 energy.
# Efficiency: How much of the stolen power is transferred back. Default is 1 (so full transference).
# Resistance: against this tech, it fights how much it will be drained. To be immune to its effects, set it to 1 or more. Negative values are allowed for extra vulnerability. Default 0 (no resistance).
"""
Foundation.ShipDef.Sovereign.dTechs = {
	'Defensive AOE Siphoon' : { "Distance": 50.0, "Power": 1000.0, "Efficiency": 0.1, "Resistance": 1.0,}
}
"""

import App
#from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents
import Foundation
import FoundationTech
import Lib.LibEngineering
import loadspacehelper
import math
import MissionLib
import string
import time

from bcdebug import debug
import traceback

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
            "Version": "1.0.1",
            "License": "LGPL",
            "Description": "Read the small title above for more info"
            }

global lImmuneShips # A list meant only for backwards compatibility - do NOT edit
lImmuneShips = (
  "ActiveSupergate",
  "AncientCity",
  "AncientCruiser",
  "AncientSatellite",
  "AncientWarship",
  "AnArchlike",
  "Andromeda",
  "AndromedaBattleForm",
  "AndSlipFighter",
  "AndSlipFighterMK1",
  "AndSlipFighterMK2",
  "AndSlipFighterMK3",
  "AnubisFlagship",
  "ArmoredVoyager",
  "AsuranSatellite",
  "B5LordShip",
  "B5TriadTriumviron",
  "Battlecrab",
  "BattleTardis",
  "BattleTardisChamaleon",
  "CA8472",
  "CorsairTardis",
  "CorsairTardisChamaleon",
  "crossfield31",
  "DalekEmperorSaucer",
  "DalekGenesisArk",
  "DalekSaucer",
  "DalekSaucerShielded",
  "DalekVoidShip",
  "EAOmegaX",
  "EAShadow_Hybrid",
  "Firebird",
  "HaririrHatak",
  "janeway",
  "kirk",
  "MindridersThoughtforce",
  "PlanetExpress",
  "saturn",
  "Shadow_Fighter",
  "Shadow_Fighter1",
  "Shadow_Fighter2",
  "Shadow_Fighter3",
  "Shadow_Fighter4",
  "Shadow_Fighter5",
  "Shadow_Fighter6",
  "Shadow_Fighter7",
  "Shadow_FighterBall",
  "Shadow_Scout",
  "SigmaWalkerScienceLab",
  "Supergate",
  "SuperHiveShip",
  "Tardis",
  "TardisType89",
  "TardisType89Chamaleon",
  "TorvalusDarkKnife",
  "vger",
  "VOR_Destroyer",
  "VOR_DestroyerClosed",
  "VOR_Fighter",
  "VOR_FighterOpen",
  "VulcanXRT55D",
  "Wells",
  "Windrunner",
  "XOverAlteranWarship",
  "XOverAncientCityFed",
  "XOverAncientSatelliteFed",
  )

try:

	# Based on PulsarMonitor from DS9FX, thank you USS Sovereign - Alex SL Gato

	bOverflow = 0
	pTimer = None
	pAllShipsWithTheTech = {} # Has the ship, with the pInstances as keys
	ticksPerKilometer = 225/40 # 225 is approximately 40 km, so 225/40 is the number of ticks per kilometer

	def Start():
		global pTimer, bOverflow

		if not bOverflow:
			pTimer = SiphoonTargetDef()
		else:
			return

	class SiphoonTargetDef(FoundationTech.TechDef):

		
		# Future suggestion: "I preferred to have a single timer, that was a design choice though" - USS Sovereign

		def __init__(self, name):
			FoundationTech.TechDef.__init__(self, name)
			global bOverflow
			bOverflow = 1
			self.pTimer = None
			self.countdown()


		def Attach(self, pInstance):
			debug(__name__ + ", Attach")
			pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
			if pShip != None:
				global bOverflow, pAllShipsWithTheTech
				dMasterDict = pInstance.__dict__['Defensive AOE Siphoon']
				pAllShipsWithTheTech[pInstance] = pShip

				if not bOverflow:
					bOverflow = 1
					self.pTimer = None
					#print "DampeningField: initiating new countdown for:", pShip.GetName()
					self.countdown()
					
			else:
				print "DampeningField Error (at Attach): couldn't acquire ship of id", pInstance.pShipID
				pass

			pInstance.lTechs.append(self)
			print "DampeningField: attached to ship:", pShip.GetName()

		def Detach(self, pInstance):
			debug(__name__ + ", Detach")
			pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
			if pShip != None:
				global bOverflow, pAllShipsWithTheTech
				dMasterDict = pInstance.__dict__['Defensive AOE Siphoon']
				
				#pAllShipsWithTheTech.pop(pInstance, None)
				if pAllShipsWithTheTech.has_key(pInstance):
					print "key found, to remove ", pInstance
					del pAllShipsWithTheTech[pInstance]
				self.pShip = None
			else:
				#print "DampeningField Error (at Detach): couldn't acquire ship of id", pInstance.pShipID
				pass
			pInstance.lTechs.remove(self)
			print "EJGL: detached from ship:", pShip.GetName()

		def countdown(self):
			if not self.pTimer:
				self.pTimer = App.PythonMethodProcess()
				self.pTimer.SetInstance(self)
				self.pTimer.SetFunction("lookclosershipsEveryone")
				self.pTimer.SetDelay(4)
				self.pTimer.SetPriority(App.TimeSliceProcess.LOW)	
				self.pTimer.SetDelayUsesGameTime(1)

		def lookclosershipsEveryone(self, fTime):
			global pAllShipsWithTheTech
			for myShipInstance in pAllShipsWithTheTech.keys():
				self.lookcloserships(fTime, pAllShipsWithTheTech[myShipInstance], myShipInstance)

		def lookcloserships(self, fTime, pShip, pInstance):
			#
			if pShip == None or pInstance == None:
				return

			#print "The ship which is using it is ", pShip.GetName()

			pSet = pShip.GetContainingSet()
			if not pSet:
				return

			pProx = pSet.GetProximityManager()
			if not pProx:
				return

			# Allowing dynamic modification of this value mid-battle
			if not pInstance.__dict__['Defensive AOE Siphoon'].has_key("Distance"):
				pInstance.__dict__['Defensive AOE Siphoon']["Distance"] = 50.0

			iRange = pInstance.__dict__['Defensive AOE Siphoon']["Distance"]

			if iRange <= 0:
				return

			lDrain = []

			global ticksPerKilometer
			kIter = pProx.GetNearObjects(pShip.GetWorldLocation(), iRange * ticksPerKilometer, 1) 
			while 1:
				pObject = pProx.GetNextObject(kIter)
				if not pObject:
					break
				if pObject.IsTypeOf(App.CT_SHIP) and not pObject.GetName() == pShip.GetName():
					lDrain.append(pObject.GetObjID())

			pProx.EndObjectIteration(kIter)  
			
			self.giveEnergy(lDrain, pShip, pInstance) 

		def giveEnergy(self, lDrain, pShip, pInstance):
			if len(lDrain) == 0:
				return 0

			# We siphon as much energy as the defender says
			if pInstance.__dict__["Defensive AOE Siphoon"].has_key("Power"):
				fStrength = pInstance.__dict__["Defensive AOE Siphoon"]["Power"]
			else:
				fStrength = 50

			if pInstance.__dict__["Defensive AOE Siphoon"].has_key("Efficiency"):
				fEfficient = pInstance.__dict__["Defensive AOE Siphoon"]["Efficiency"]
			else:
				fEfficient = 1.0


			for kShip in lDrain:
				#print kShip
				pAttacker = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(kShip))
				if not pAttacker:
					continue

				#print pAttacker

				vibechecker = 1
				# Attacker instance
				try: 
					pAttackerInst = FoundationTech.dShips[pAttacker.GetName()]
					if pAttackerInst == None:
						#print "After looking, no instance for attacker:", pAttacker.GetName(), "How odd..."
						vibechecker = 0
				except:
					#print "Error, so no instance for attacker:", pAttacker.GetName(), "How odd..."
					vibechecker = 0

				if vibechecker == 0:
					continue

				effect = 0

				if pAttackerInst.__dict__.has_key("Defensive AOE Siphoon") and pAttackerInst.__dict__["Defensive AOE Siphoon"].has_key("Defensive AOE Siphoon") and pAttackerInst.__dict__["Defensive AOE Siphoon"].has_key("Resistance"):
					effect = pAttackerInst.__dict__["Defensive AOE Siphoon"]["Resistance"]
					
				if effect >= 1: # Immunity to the Siphoon, good and bad
					continue

				#print "Siphoning attacker ", pAttacker.GetName(), " energy..."
		
				fStrength = fStrength * (1 - effect)

				pMission        = MissionLib.GetMission() 
				pFriendlies     = pMission.GetFriendlyGroup() 
				pEnemies        = pMission.GetEnemyGroup() 
				pGroup          = pMission.GetNeutralGroup()
				thatShipGroup   = 0 # -1 enemy, 0 neutral, 1 friendly, with each other

				## Check the friendlies and enemy group for the ship
				if (pFriendlies.IsNameInGroup(pAttacker.GetName()) and pFriendlies.IsNameInGroup(pShip.GetName())) or (pEnemies.IsNameInGroup(pAttacker.GetName()) and pEnemies.IsNameInGroup(pShip.GetName()))  or (pGroup.IsNameInGroup(pAttacker.GetName()) and pGroup.IsNameInGroup(pShip.GetName())):
					thatShipGroup = 1
					#if fStrength > 0.0:
					#	continue
				elif not pGroup.IsNameInGroup(pShip.GetName()):
					thatShipGroup = -1
					#if fStrength < 0.0:
					#	continue

				#print "Ok we have seen that the friend determinator is ", thatShipGroup, "and the fStrength is", fStrength

				if fStrength > 0.0 and thatShipGroup == -1:
					#print "We are enemies then"
					global lImmuneShips
					sScript     = pAttacker.GetScript()
					sShipScript = string.split(sScript, ".")[-1]
					if not sShipScript in lImmuneShips:
						if pAttacker.GetPowerSubsystem():
							pAttacker.GetPowerSubsystem().StealPower(fStrength)
						if fStrength * fEfficient > 0:
							if pShip.GetPowerSubsystem():
								pShip.GetPowerSubsystem().AddPower(fStrength*fEfficient*0.1)
				# According to STO, this is synergic
				elif fStrength < 0.0 and thatShipGroup == 1:
					#print "we are friends then"
					if pAttacker.GetPowerSubsystem():
						pAttacker.GetPowerSubsystem().AddPower(-fStrength*fEfficient)
					if fStrength * fEfficient > 0:
						if pShip.GetPowerSubsystem():
							pShip.GetPowerSubsystem().AddPower(-fStrength*fEfficient)

			#print "Siphoning done, awaiting another drain"

	oSiphoonTarget = SiphoonTargetDef('Defensive AOE Siphoon')

except:
	print "Something went wrong wih DampeningAOEDefensiveField technology"
	traceback.print_exc()
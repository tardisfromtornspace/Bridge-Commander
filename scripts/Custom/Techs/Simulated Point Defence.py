#################################################################################################################
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
#         Simulated Point Defence.py by Alex SL Gato
#         Version 0.9
#         8th September 2023
#         Based strongly on DampeningAOEDefensiveField.py by Alex Sl Gato, which was based on scripts\Custom\DS9FX\DS9FXPulsarFX\PulsarManager by USS Sovereign, and slightly on TractorBeams.py, Inversion Beam and Power Drain Beam 1.0 by MLeo Daalder, Apollo, and Dasher; some team-switching torpedo by LJ; and GraviticLance by Alex SL Gato, which was based on FiveSecsGodPhaser by USS Frontier, scripts/ftb/Tech/TachyonProjectile by the FoundationTechnologies team, and scripts/ftb/Tech/FedAblativeArmour by the FoundationTechnologies team.
#         Also based strongly on PointDefence.py by Defiant
#################################################################################################################
# This tech gives a ship the ability to Simulate Point Defence without using phasers or pulse or torpedoes to intercept - done to simulate a defense without overworking the game as much as the traditional phaser point defence or an alternative pulse defense.
# Usage Example:  Add this (the lines under the triple ") to the dTechs attribute of your ShipDef, in the Ship plugin file (replace "Sovereign" with the proper abbrev).
# Distance: Max approx. range of effect of this ability, in km. Logically cannot be equal or less than 0, so if you don't want this ship to use point defence, set it to 0. Default is 50 km.
# InnerDistance: min approx. range if effectiveness, in km. Logically cannot be equal or less than 0, so if you don't want this range to not exist, set it to 0, or leave it by default, 0.
# Effectiveness: chance of ideally divert an incoming pulse or torpedo. Range is [0, 1], but gets multiplied by the power given to the shields, to an extent. Default is 0.5.
# LimitTurn: torps with this much angular acceleration or more will be even harder to intercept, it actually sets the minimum for these, as it is done as a gradient via formula "(1 - GetMaxAngularAccel/LimitTurn )", except for LimitTurn 0, which only makes it target pulses, not torps. If negative value, only targets torpedoes of the range (0, -LimitTurn]. If this field is not present these calculations are ignored and will target all regardless of turn.
# LimitSpeed: torps with this speed or more cannot be intercepted, done gradually according to function "chance = -0.5 * (3 ** (1/3)) * -((-(projectileSpeed - LimitSpeed)) ** (1.0/3.0) )" , with this chance capped at range [0, 1]. Default limitSpeed is 35.
# LimitDamage: torps dealing this much damage or more will have their chances at being hit cut ... unless it is Breen Drain or Jumpspace Tunnel. Negative values work the other way around, to make it so it only targets torpedoes beyond a certain damage threshold. If this value is not filled it is not calculated.
# Period: in seconds, but then internally multiplied by 10 to get it in a base slice. Default is 1.0 Also indirectly affected by power given to the shields.
# MaxNumberTorps: how many torps it can intercept in an area at a time. Default is 200.
# EXPERIMENTAL: Phaser, Torpedo and Pulse properties... only to use if you want a phaser/pulse/torpedo to react as well. They can have a "Priority" field inside to indicate priority when choosing weapons (1 = lowest but still above any default, higher positive nubmers are higher priorities). Note: this experimental field will make it neater, but it will also indirectly adjust to the weapon banks and tubes speed - and on the case of phaser bank, reduce it to the available ranges and time to fire - thus decrementing real effectivity and defensive capabilities when firing when compared with a non-experimental one. 
# Properties: on this case, it sets specific properties that may be understood as point defence systems - albeit due to how STBC works you would need to either disable the other subsystems for a sec before firing (not recommended) or create a hardpoint weapon group; so this field is mostly unused except for the following field
# Specially: if this field have a value higher than 0, the ship will not be able to use that point defense if all the subsystems indicated on the Properties field are disabled or destroyed

"""
Foundation.ShipDef.Sovereign.dTechs = {
	'Simulated Point Defence' : { "Distance": 50.0, "InnerDistance": 10.0, "Effectiveness": 0.5, "LimitTurn": 5.0, "LimitSpeed": 35, "LimitDamage": "150", "Period": 0.5, "MaxNumberTorps": 50, "Phaser": {"Priority": 1, "Properties": ["Phaser Bank Name 1"], "Specially": 0,}, "Pulse": {"Priority": 1, "Properties": ["Pulse Weapon Emmiter Name 1"], "Specially": 0,}, "Torpedo": {"Priority": 1, "Properties": ["Torpedo Tube Name 1"], "Specially": 0,}, "Tractor": {"Priority": 1, "Properties": ["Tractor Beam Name 1"], "Specially": 0,}},
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
            "Version": "0.8",
            "License": "LGPL",
            "Description": "Read the small title above for more info"
            }

try:

	# Based on PulsarMonitor from DS9FX, thank you USS Sovereign - Alex SL Gato

	FirePointName = "Total PointDefence Firepoint"
	firepointCount = 0
	dictFirePointToTorp = {}

	defaultDistance = 50.0
	defaultInnerDistance = 0.0
	defaultEffectiveness = 0.5
	defaultLimitSpeed = 35
	defaultPeriod = 1.0
	defaultSlice = 0.1
	defaultMaxNumberTorps = 200

	bOverflow = 0
	pTimer = None
	pAllShipsWithTheTech = {} # Has the ship, with the pInstances as keys
	ticksPerKilometer = 225/40 # 225 is approximately 40 km, so 225/40 is the number of ticks per kilometer


	global lImmuneTorps   #Some torps do not have an inner name, only empty, for this case we have a list of some weapons our point defence should not block - for example telepathic attacks done via dummy projectile
	lImmuneTorps = (
		"B5ThirdspaceTeleAttack",
		"B5ThirdspaceTeleAttack2",
		"Jumpspace Tunnel",
		"MinJW",
		"VorlonWeapon",
		)

	def Start():
		global pTimer, bOverflow

		if not bOverflow:
			pTimer = SimulatedPointDefenceDef()
		else:
			return

	class SimulatedPointDefenceDef(FoundationTech.TechDef):

		def __init__(self, name):
			FoundationTech.TechDef.__init__(self, name)
			global bOverflow
			if not bOverflow:
				#print "ATTENTION: Called Simulated Point Defence"
				self.pEventHandler = App.TGPythonInstanceWrapper()
				self.pEventHandler.SetPyWrapper(self)

				bOverflow = 1
				self.pTimer = None
				self.countdown()


		def Attach(self, pInstance):
			debug(__name__ + ", Attach")
			pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
			if pShip != None:
				global bOverflow, pAllShipsWithTheTech
				dMasterDict = pInstance.__dict__['Simulated Point Defence']
				pAllShipsWithTheTech[pInstance] = pShip
					
				if not bOverflow:
					bOverflow = 1
					self.pTimer = None
					print "SimulatedPointDefence: initiating new countdown for:", pShip.GetName()
					self.countdown()
					
			else:
				print "Simulated Point Defence Error (at Attach): couldn't acquire ship of id", pInstance.pShipID
				pass

			pInstance.lTechs.append(self)
			print "Simulated Point Defence: attached to ship:", pShip.GetName()

		def Detach(self, pInstance):
			debug(__name__ + ", Detach")
			global bOverflow, pAllShipsWithTheTech
			if pInstance == None:
				return

			if pAllShipsWithTheTech.has_key(pInstance):
				print "key found, to remove ", pInstance
				del pAllShipsWithTheTech[pInstance]
			pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
			if pShip != None:
				dMasterDict = pInstance.__dict__['Simulated Point Defence']
				#self.pShip = None
			else:
				print "SimulatedPointDefence Error (at Detach): couldn't acquire ship of id", pInstance.pShipID
				pass

			print "Simulated Point Defence: detached from ship"
			if pShip != None:
				print "---ship name:", pShip.GetName()

			pInstance.lTechs.remove(self)


		def Detach2(self, pInstance, pShip):
			debug(__name__ + ", Detach")
			global bOverflow, pAllShipsWithTheTech
			
			if not pInstance and pShip:
				try:
					pInstance = FoundationTech.dShips[pShip.GetName()]
					if pInstance == None:
						return
				except:
					print "Simulated Point Defence: cancelling, error in try from Detach2 found..."
					return
				
			if pAllShipsWithTheTech.has_key(pInstance):
				print "key found, to remove ", pInstance
				del pAllShipsWithTheTech[pInstance]
			if pShip == None and pInstance != None:
				pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
			if pShip != None and pInstance != None:
				dMasterDict = pInstance.__dict__['Simulated Point Defence']
			else:
				print "SimulatedPointDefence Error (at Detach): couldn't acquire ship"
				if pInstance != None:
					print "--- of id", pInstance.pShipID
				pass

			print "Simulated Point Defence: cleanup-detached from ship"
			if pShip != None:
				print "---ship name:", pShip.GetName()

			if pInstance != None:
				pInstance.lTechs.remove(self)

		def countdown(self):
			debug(__name__ + ", Countdown")
			if not self.pTimer:
				global defaultSlice
				self.pTimer = App.PythonMethodProcess()
				self.pTimer.SetInstance(self)
				self.pTimer.SetFunction("lookclosershipsEveryone")
				self.pTimer.SetDelay(defaultSlice)
				self.pTimer.SetPriority(App.TimeSliceProcess.LOW)	
				self.pTimer.SetDelayUsesGameTime(1)

		def lookclosershipsEveryone(self, fTime):
			debug(__name__ + ", lookclosershipsEveryone")
			global pAllShipsWithTheTech
			for myShipInstance in pAllShipsWithTheTech.keys():
				if myShipInstance != None:
					self.lookcloserProjectiles(fTime, pAllShipsWithTheTech[myShipInstance], myShipInstance)

		def lookcloserProjectiles(self, fTime, pShip, pInstance):
			debug(__name__ + ", lookcloserProjectiles")
			if pInstance == None:
				return

			if pShip == None or not pInstance.__dict__.has_key("Simulated Point Defence"):
				self.Detach2(pInstance, pShip)
				return

			#print "The ship which is using it is ", pShip.GetName()

			global defaultPeriod, defaultSlice
			if not pInstance.__dict__['Simulated Point Defence'].has_key("Period"):
				pInstance.__dict__['Simulated Point Defence']["Period"] = defaultPeriod

			if not pInstance.__dict__['Simulated Point Defence'].has_key("TimeRemaining"):
				pInstance.__dict__['Simulated Point Defence']["TimeRemaining"] = 0.0

			
			try:
				pInstanceAux = FoundationTech.dShips[pShip.GetName()]
				if pInstanceAux == None or not pInstanceAux.__dict__.has_key("Simulated Point Defence"):
					print "Simulated Point Defence: cancelling, no FTech Ship Instance obj"
					self.Detach2(pInstance, pShip)
					return
			except:
				print "Simulated Point Defence: cancelling, error in try found..."
				self.Detach2(pInstance, pShip)
				return

			energyCommited = 1.0
			pShields = pShip.GetShields()
			if pShields:
				energyCommited = pShields.GetPowerPercentageWanted()
				if energyCommited < 0.5:
					energyCommited = 0.5

			pInstance.__dict__['Simulated Point Defence']["TimeRemaining"] = pInstance.__dict__['Simulated Point Defence']["TimeRemaining"] - defaultSlice * energyCommited

			if pInstance.__dict__['Simulated Point Defence']["TimeRemaining"] > 0:	
				return
			else:
				pInstance.__dict__['Simulated Point Defence']["TimeRemaining"] = pInstance.__dict__['Simulated Point Defence']["Period"]

			pSet = pShip.GetContainingSet()
			if not pSet:
				return

			pProx = pSet.GetProximityManager()
			if not pProx:
				return

			# Allowing dynamic modification of this value mid-battle
			global defaultDistance, defaultInnerDistance

			if not pInstance.__dict__['Simulated Point Defence'].has_key("Distance"):
				pInstance.__dict__['Simulated Point Defence']["Distance"] = defaultDistance

			iRange = pInstance.__dict__['Simulated Point Defence']["Distance"]

			if not pInstance.__dict__['Simulated Point Defence'].has_key("InnerDistance"):
				pInstance.__dict__['Simulated Point Defence']["InnerDistance"] = defaultInnerDistance

			iMinRange = pInstance.__dict__['Simulated Point Defence']["InnerDistance"]

			lTorpTargets = []
			subSys = []  

			pMission        = MissionLib.GetMission() 
			pFriendlies     = pMission.GetFriendlyGroup() 
			pEnemies        = pMission.GetEnemyGroup() 
			pGroup          = pMission.GetNeutralGroup()

			thisShipInFriendlyGroup = pFriendlies.IsNameInGroup(pShip.GetName())
			thisShipInEnemyGroup = pEnemies.IsNameInGroup(pShip.GetName())
			thisShipInNeutralGroup = pGroup.IsNameInGroup(pShip.GetName())

			shipName = pShip.GetName()

			global ticksPerKilometer
			kIter = pProx.GetNearObjects(pShip.GetWorldLocation(), iRange * ticksPerKilometer, 1) 
			while 1:
				debug(__name__ + ", Checking Distance 1")
				pObject = pProx.GetNextObject(kIter)
				if not pObject:
					break

				if not pShip:
					return

				debug(__name__ + ", Checking Distance 2")
				isTorpedo = pObject.IsTypeOf(App.CT_TORPEDO)
				debug(__name__ + ", Checking Distance 2A")
				if isTorpedo:
					#objName = None
					#if pObject and hasattr(pObject, "GetName") and pObject.GetName() != None:
					#	objName = pObject.GetName()
					#debug(__name__ + ", Checking Distance 2B")
					#sameName = 0
					#if objName != None:
					#	sameName = (objName == shipName)
					#debug(__name__ + ", Checking Distance 2C")
					#if not sameName:
					debug(__name__ + ", Checking Distance 2D")
					if not (self.Distance(pShip, pObject, iMinRange * ticksPerKilometer) < (iMinRange * ticksPerKilometer)):
						
					

				
				#sameName = (objName == shipName)
				#debug(__name__ + ", Checking Distance 2B")

				#if pObject.IsTypeOf(App.CT_TORPEDO) and not pObject.GetName() == pShip.GetName() and not (self.Distance(pShip, pObject, iMinRange * ticksPerKilometer) < (iMinRange * ticksPerKilometer)):
				#if isTorpedo and not sameName and not (self.Distance(pShip, pObject, iMinRange * ticksPerKilometer) < (iMinRange * ticksPerKilometer)):
				
						debug(__name__ + ", Checking Distance 3")
						pTorp = App.Torpedo_GetObjectByID(None, pObject.GetObjID())
						debug(__name__ + ", Checking Distance 4")
						if pTorp:
							pFiredShip = App.ShipClass_GetObjectByID(None, pTorp.GetTargetID())
							debug(__name__ + ", Checking Distance 5")
							## Check the friendlies and enemy group for the ship. If that ship does not exist it is a stray torpedo and must be shot down in case it hits us
							if not pFiredShip or (pFriendlies.IsNameInGroup(pFiredShip.GetName()) and thisShipInFriendlyGroup) or (pEnemies.IsNameInGroup(pFiredShip.GetName()) and thisShipInEnemyGroup)  or (pGroup.IsNameInGroup(pFiredShip.GetName()) and thisShipInNeutralGroup):
								lTorpTargets.append(pObject.GetObjID())
							debug(__name__ + ", Checking Distance 6")

			debug(__name__ + ", Going to remove iterator")

			pProx.EndObjectIteration(kIter) 

			debug(__name__ + ", Finished Distance Check")			
			self.shootThemDown(lTorpTargets, pShip, pInstance, pSet)

		def shootThemDown(self, lTorpTargets, pShip, pInstance, pSet):
			debug(__name__ + ", shootThemDown")
			if len(lTorpTargets) == 0:
				return 0
			torpsFiredDown = 0

			global defaultEffectiveness, defaultLimitSpeed, defaultMaxNumberTorps

			if not pInstance.__dict__['Simulated Point Defence'].has_key("MaxNumberTorps"):
				pInstance.__dict__['Simulated Point Defence']["MaxNumberTorps"] = defaultMaxNumberTorps

			maxTorpsPerTurn = pInstance.__dict__['Simulated Point Defence']["MaxNumberTorps"]

			if not pInstance.__dict__['Simulated Point Defence'].has_key("Effectiveness"):
				pInstance.__dict__['Simulated Point Defence']["Effectiveness"] = defaultEffectiveness

			effectiveness = pInstance.__dict__['Simulated Point Defence']["Effectiveness"]
            
			hasLimitTurn = pInstance.__dict__['Simulated Point Defence'].has_key("LimitTurn")
			divider = 1
			if hasLimitTurn:
				divider = pInstance.__dict__['Simulated Point Defence']["LimitTurn"]

			damageLimit = 1000000
			hasLimitDamage = pInstance.__dict__['Simulated Point Defence'].has_key("LimitDamage")
			if hasLimitDamage:
					damageLimit = pInstance.__dict__['Simulated Point Defence']["LimitDamage"]

			energyCommited = 1.0
			pShields = pShip.GetShields()
			if pShields:
				energyCommited = pShields.GetPowerPercentageWanted()
				if energyCommited > 1.25:
					energyCommited = 1.25


			if not pInstance.__dict__['Simulated Point Defence'].has_key("LimitSpeed"):
				pInstance.__dict__['Simulated Point Defence']["LimitSpeed"] = defaultLimitSpeed

			dictLimitSpeed = pInstance.__dict__['Simulated Point Defence']["LimitSpeed"]

			preferredWeapon = "None"
			pWeaponSystem = None
			subSys = []

			havePhaser = pInstance.__dict__['Simulated Point Defence'].has_key("Phaser")
			havePulse = pInstance.__dict__['Simulated Point Defence'].has_key("Pulse")
			haveTorpedo = pInstance.__dict__['Simulated Point Defence'].has_key("Torpedo")
			haveTractor = pInstance.__dict__['Simulated Point Defence'].has_key("Tractor")
			nottooSpecificToSwitch = 0

			if havePhaser or havePulse or haveTorpedo or haveTractor:
				pSensorSubsystem = pShip.GetSensorSubsystem()
				if not pSensorSubsystem or pSensorSubsystem.IsDisabled():
					return

				priorityPhaser = 0
				priorityPulse = 0
				priorityTorp = 0
				priorityTractor = 0
				if havePhaser:
					if pInstance.__dict__['Simulated Point Defence']["Phaser"].has_key("Priority"):
						priorityPhaser = pInstance.__dict__['Simulated Point Defence']["Phaser"]["Priority"]
						if priorityPhaser < 0.0:
							priorityPhaser = 0.0
					else:
						priorityPhaser = 0.1

				if havePulse:
					if pInstance.__dict__['Simulated Point Defence']["Pulse"].has_key("Priority"):
						priorityPulse = pInstance.__dict__['Simulated Point Defence']["Pulse"]["Priority"]
						if priorityPulse < 0.0:
							priorityPulse = 0.0
					else:
						priorityPulse = 0.1
				if haveTorpedo:
					if pInstance.__dict__['Simulated Point Defence']["Torpedo"].has_key("Priority"):
						priorityTorp = pInstance.__dict__['Simulated Point Defence']["Torpedo"]["Priority"]
						if priorityTorp < 0.0:
							priorityTorp = 0.0
					else:
						priorityTorp = 0.1

				if haveTractor:
					if pInstance.__dict__['Simulated Point Defence']["Tractor"].has_key("Priority"):
						priorityTractor = pInstance.__dict__['Simulated Point Defence']["Tractor"]["Priority"]
						if priorityTractor < 0.0:
							priorityTractor = 0.0
					else:
						priorityTractor = 0.1

				pWeaponSystem1 = pShip.GetPhaserSystem()
				pWeaponSystem2 = pShip.GetPulseWeaponSystem()
				pWeaponSystem3 = pShip.GetTorpedoSystem()
				pWeaponSystem4 = pShip.GetTractorBeamSystem()

				if not pWeaponSystem1 or pWeaponSystem1.IsDisabled():
    					priorityPhaser = -1
				if not pWeaponSystem2 or pWeaponSystem2.IsDisabled():
					priorityPulse = -1
				if not pWeaponSystem3 or pWeaponSystem3.IsDisabled():
					priorityTorp = -1
				if not pWeaponSystem4 or pWeaponSystem4.IsDisabled():
					priorityTractor = -1

				#print "ok priorities now:", priorityPhaser, priorityPulse, priorityTorp, priorityTractor

				if priorityPhaser == -1 and priorityPulse == -1 and priorityTorp == -1  and priorityTractor == -1:
					#print "no systems to fire"
					return

				if priorityPhaser >= priorityPulse and priorityPhaser >= priorityTorp and priorityPhaser >= priorityTractor and havePhaser:
					pWeaponSystem = pWeaponSystem1
					preferredWeapon = "Phaser"
				else:
					priorityPhaser = -1
					if priorityPulse > priorityPhaser and priorityPulse >= priorityTorp and priorityPulse >= priorityTractor and havePulse:
						pWeaponSystem = pWeaponSystem2
						preferredWeapon = "Pulse"
					else:
						priorityPulse = -1
						if priorityTorp > priorityPhaser and priorityTorp > priorityPulse and priorityTorp >= priorityTractor and haveTorpedo:
							pWeaponSystem = pWeaponSystem3
							preferredWeapon = "Torpedo"
						elif haveTractor:
							pWeaponSystem = pWeaponSystem4
							preferredWeapon = "Tractor"

				#print "preferredWeapon is", preferredWeapon
				
				try:
					if (not preferredWeapon == "None") and pInstance.__dict__['Simulated Point Defence'].has_key(preferredWeapon) and pInstance.__dict__['Simulated Point Defence'][preferredWeapon].has_key("Properties"):
						subSysNames = pInstance.__dict__['Simulated Point Defence'][preferredWeapon]["Properties"]
						if pInstance.__dict__['Simulated Point Defence'][preferredWeapon].has_key("Specially") and pInstance.__dict__['Simulated Point Defence'][preferredWeapon]["Specially"] > 0:
							nottooSpecificToSwitch = 0
						else:
							nottooSpecificToSwitch = 1
						iChildren = pWeaponSystem.GetNumChildSubsystems()
						if iChildren > 0 and len(subSysNames) > 0:
							for iIndex in range(iChildren):
								pChild = pWeaponSystem.GetChildSubsystem(iIndex)
								if pChild.GetName() in subSysNames:
									if not pChild.IsDisabled():
										nottooSpecificToSwitch = nottooSpecificToSwitch + 1
										subSys.append(pChild)
					else:
						nottooSpecificToSwitch = 1
				except:
					print "Error found while assigning speciality in", pShip.GetName(), "Probably all assigned systems are disabled or destroyed"
					return

			for kTorp in lTorpTargets:
				pTorp = App.Torpedo_GetObjectByID(None, kTorp)
				if not pTorp:
					#print "No torp?"
					continue

				thisTorpDamage = pTorp.GetDamage()
				thisTorpSpeed = pTorp.GetLaunchSpeed()

				if thisTorpSpeed > dictLimitSpeed:
					continue

				thisTorpTurn = pTorp.GetMaxAngularAccel()
				thisTorpGuideLife = pTorp.GetGuidanceLifeTime()
				isLeTorpBreenDrain = 0
				leRicochetChance = 1

				#print "The torp has the damage, speed, turn and lifetime shown here: ", thisTorpDamage, thisTorpSpeed, thisTorpTurn, thisTorpGuideLife
				if hasattr(pTorp, "GetModuleName") and not pTorp.GetModuleName() == None:
					
					#print "There is a torp module, the module name is ", pTorp.GetModuleName()
					leTorpExtraInfo = __import__(pTorp.GetModuleName(), globals(), locals())
					if hasattr(leTorpExtraInfo, "GetName"):
						theTorpName = leTorpExtraInfo.GetName()
						#print "the name is", theTorpName
						if theTorpName == "":
							#print "Having to do a harsher search for not including a name..."
							global lImmuneTorps
							sTorpScriptName = string.split(pTorp.GetModuleName(), ".")[-1]
							if sTorpScriptName in lImmuneTorps:
								continue
							if sTorpScriptName == "BreenDrainer" or sTorpScriptName == "BreenDrain" or sTorpScriptName == "Breen Drainer":
								isLeTorpBreenDrain = 1
						if theTorpName == "Jumpspace Tunnel" or theTorpName == "Vorlon Weapon":
							#print "We cannot just shoot an interdimensional vortex on the face and with that make it collapse!"
							continue
						if theTorpName == "Breen Drainer" or theTorpName == "Breen Drain" or theTorpName == "Breen Drainer" or theTorpName == "Jumpspace Disruptor":
							isLeTorpBreenDrain = 1
					else:
						print "Having to do a harsher search for not including an attribute... no, really, this attribute should be here, even as an empty field for other parts of the game to work properly, please fix ", pTorp.GetModuleName(), " immediately"
						global lImmuneTorps
						sTorpScriptName = string.split(pTorp.GetModuleName(), ".")[-1]
						if sTorpScriptName in lImmuneTorps:
							continue
						if sTorpScriptName == "BreenDrainer" or sTorpScriptName == "BreenDrain" or sTorpScriptName == "Breen Drainer" or sTorpScriptName == "ShadHipDis":
							isLeTorpBreenDrain = 1

					if hasattr(leTorpExtraInfo, "RicochetChance"):
						#print "hey, this has ricochet chance and may evade our defense at the last moment", leTorpExtraInfo.RicochetChance()
						leRicochetChance = 1.2 - leTorpExtraInfo.RicochetChance()
						if leRicochetChance < 0.0:
							leRicochetChance = 0
						if leRicochetChance > 1.0:
							leRicochetChance = 1

				turnSpeedEffectiveness = 1
				if hasLimitTurn:
					if divider == 0: # Target pulses only
						if self.isAPulse(thisTorpGuideLife, thisTorpTurn):
							turnSpeedEffectiveness = 1
						else:
							continue
					else:
						temporaryGuide = 2.0
						if thisTorpGuideLife < 2:
							temporaryGuide = thisTorpGuideLife
						if divider > 0:
							#print "divider is greater than 0, we target all objectives. Now, thisTorpTurn*temporaryGuide/divider is ", thisTorpTurn, temporaryGuide, divider, thisTorpTurn*temporaryGuide/divider
							turnSpeedEffectiveness = (1 - thisTorpTurn*temporaryGuide/divider)
						else: # Target torps only
							if self.isAPulse(thisTorpGuideLife, thisTorpTurn):
								continue
							else:
								turnSpeedEffectiveness = (1 + thisTorpTurn*temporaryGuide/divider)
						if turnSpeedEffectiveness < 0:
							turnSpeedEffectiveness = 0

				linearSpeedEffectiveness = 1
				if dictLimitSpeed == 0:
					if thisTorpSpeed == 0:
						linearSpeedEffectiveness = 1
					else:
						continue
				else:
					linearSpeedEffectiveness = -0.5 * (3 ** (1/3)) * -((-(thisTorpSpeed - dictLimitSpeed)) ** (1.0/3.0) )
					if linearSpeedEffectiveness > 1.0:
						linearSpeedEffectiveness = 1.0
					if linearSpeedEffectiveness < 0.0:
						linearSpeedEffectiveness = 0.0

				damageEffectivenness = 1
				if hasLimitDamage:
					if damageLimit == 0:
						if thisTorpDamage == 0:
							continue
						else:
							damageEffectivenness = 1
					elif damageLimit > 0:
						if damageLimit < thisTorpDamage:
							damageEffectivenness =  (2 - thisTorpDamage/damageLimit)
					else:
						if -damageLimit > thisTorpDamage and not len(lTorpTargets) <= 1: # unless this is the only torpedo, we are not targeting a low-priority torpedo
							continue

				if damageEffectivenness > 1.0:
					damageEffectivenness = 1.0
				if damageEffectivenness < 0.0:
					damageEffectivenness = 0.0

				extraFactor = 1
				if isLeTorpBreenDrain:
					extraFactor = 0.1

				finalChance = effectiveness * extraFactor * energyCommited * leRicochetChance * turnSpeedEffectiveness * linearSpeedEffectiveness * damageEffectivenness

				#print "finalChance", finalChance, " = effectiveness", effectiveness, " * extraFactor", extraFactor, " * energyCommited", energyCommited, " * leRicochetChance", leRicochetChance, " * turnSpeedEffectiveness", turnSpeedEffectiveness, " * linearSpeedEffectiveness", linearSpeedEffectiveness, " * damageEffectivenness", damageEffectivenness 
				if preferredWeapon == "Tractor" or preferredWeapon == "Phaser" or App.g_kSystemWrapper.GetRandomNumber(100) <= 100 * finalChance:
					#print "This torp must be destroyed"
					if torpsFiredDown >= maxTorpsPerTurn:
						torpsFiredDown = 0
						return

					global FirePointName, firepointCount
					pTorpNameStripped = string.split(str(pTorp), '<')[-1]
					pTorpNameStripped2 = string.split(pTorpNameStripped, '>')[0]
					sThisFirePointName = FirePointName + " " + pShip.GetName() + " " + pTorpNameStripped2 #str(firepointCount)
					#print "sThisFirePointName is ", sThisFirePointName
					firepointCount = firepointCount + 1

					originalSingle = "Unused"
					if not preferredWeapon == "None":
						originalSingle = pWeaponSystem.IsSingleFire()
						pWeaponSystem.GetProperty().SetSingleFire(1)

					global dictFirePointToTorp
					
					donotneedtospamattack = 0
					pFirePoint = MissionLib.GetShip(sThisFirePointName)
					# if it does not exist we have to create it first
					if not pFirePoint:
						pFirePoint = loadspacehelper.CreateShip("BigFirepoint", pSet, sThisFirePointName, None)
						pFirePoint.SetTargetable(0)
						pFirePoint.AddPythonFuncHandlerForInstance(App.ET_WEAPON_HIT, __name__ + ".WeaponaHit")
						dictFirePointToTorp[sThisFirePointName] = pTorp

					else:
						donotneedtospamattack = 1
					if pFirePoint:
						pTarget = App.ShipClass_GetObjectByID(None, pTorp.GetTargetID()) # Suggestion for optimization - we already got the target in a previous function
						if pTarget:
							pFirePoint.EnableCollisionsWith(pTarget, 0)
						pAttacker = App.ShipClass_GetObjectByID(None, pTorp.GetParentID())
						if pAttacker: # Safety measure, if for some reason we were to point defence at the same moment a projectile fired.
							pFirePoint.EnableCollisionsWith(pAttacker, 0)

					# This should make sure that the clients in MP get the right position
					if App.g_kUtopiaModule.IsMultiplayer():
						kLocation = pTorp.GetWorldLocation()
						pFirePoint.SetTranslate(kLocation)
						pFirePoint.UpdateNodeOnly()
					else:
						if pWeaponSystem:
							pWeaponSystem.StopFiring()
						if preferredWeapon == "Phaser" or preferredWeapon == "Tractor":
							# little offset, so the Torpedo doesn't destroy our firepoint
							kLocation = App.TGPoint3()
							kLocation.SetXYZ(0, 0.5, 0)
							pFirePoint.SetTranslate(kLocation)
							pFirePoint.UpdateNodeOnly()
							pTorp.AttachObject(pFirePoint)

							#vSubsystemOffset = App.TGPoint3()
							#vSubsystemOffset.SetXYZ(0, 0, 0)

							#pWeaponSystem.StartFiring(pFirePoint, vSubsystemOffset)
							#print "Phaser Attack"
							if donotneedtospamattack == 0:
								torpsFiredDown = torpsFiredDown + 1
							pSeq = App.TGSequence_Create()
							#pSeq.AppendAction(App.TGScriptAction_Create(__name__, "attackaFirePoint", pWeaponSystem, pFirePoint, pShip, pInstance), 0.0)
							pSeq.AppendAction(App.TGScriptAction_Create(__name__, "DeleteFirePoint", sThisFirePointName), 3.0)
							pSeq.Play()

							vSubsystemOffset = App.TGPoint3()
							vSubsystemOffset.SetXYZ(0, 0, 0)
							if len(subSys) > 0:
								pWeaponSystem.StartFiring(pFirePoint, vSubsystemOffset)
								# Sorry, for these we would need to edit the groups on the hardpoint itself
								#for pChild in subSys:
									#pChild.StartFiring(pFirePoint, vSubsystemOffset) # test .FireDumb and .Fire
									#pChild.SetFiring(pFirePoint, vSubsystemOffset)
							else:
								if nottooSpecificToSwitch > 0:
									pWeaponSystem.StartFiring(pFirePoint, vSubsystemOffset)
						else:
							# normally we would do the same, but this time due to simplification we are only doing it for guaranteed torpedoes to destroy! So we really want the Torp to destroy our Firepoint.
							kLocation = App.TGPoint3()
							kLocation.SetXYZ(0, 0, 0)
							pFirePoint.SetTranslate(kLocation)
							pFirePoint.UpdateNodeOnly()
							pTorp.AttachObject(pFirePoint)

							if not preferredWeapon == "None":
								vSubsystemOffset = App.TGPoint3()
								vSubsystemOffset.SetXYZ(0, 0, 0)
								if len(subSys) > 0:
									pWeaponSystem.StartFiring(pFirePoint, vSubsystemOffset)
									# Sorry, for these we would need to edit the groups on the hardpoint itself
									#for pChild in subSys:
										#pChild.StartFiring(pFirePoint, vSubsystemOffset) # test .FireDumb and .Fire
										#pChild.SetFiring(pFirePoint, vSubsystemOffset)
								else:
									if nottooSpecificToSwitch > 0:
										pWeaponSystem.StartFiring(pFirePoint, vSubsystemOffset)

							pSeq = App.TGSequence_Create()
							pSeq.AppendAction(App.TGScriptAction_Create(__name__, "DeleteFirePoint", sThisFirePointName), 0.5)
							pSeq.Play()
							torpsFiredDown = torpsFiredDown + 1

							# get the World location of out Firepoint
							kLocation = pTorp.GetWorldLocation()
                                
							# For the Explosion Size
							if pFirePoint.GetPowerSubsystem():
								pFirePoint.GetPowerSubsystem().GetProperty().SetPowerOutput(pTorp.GetDamage() / 10)
                                
							# Detach it from the Torpedo
							if not App.g_kUtopiaModule.IsMultiplayer():
								pTorp.DetachObject(pFirePoint)
                                
							# and let the torpedo fly on our Firepoint to get destroyed
							pTorp.SetTarget(pFirePoint.GetObjID())
                                                                
							# tell other clients to also move the firepoint to the ship
							if App.g_kUtopiaModule.IsMultiplayer():
								MPSendRemoveTorpMessage(pTorp)
                                
							# Let the Torp destroy the Firepoint
							pFirePoint.SetTranslate(kLocation)
							pFirePoint.UpdateNodeOnly()

					if not preferredWeapon == "None":
						pWeaponSystem.GetProperty().SetSingleFire(originalSingle)


		def Distance(self, pObject1, pObject2, minMax):
			debug(__name__ + ", Distance")
			if pObject1 and pObject2:
				vDifference = pObject1.GetWorldLocation()
				vDifference.Subtract(pObject2.GetWorldLocation())

				return vDifference.Length()

			else:
				return minMax + 1 # Absurd value, one of those ships is not there anymore so we need to indicate that ship is no longer with us

		def isAPulse(self, thisTorpGuideLife, thisTorpTurn):
			debug(__name__ + ", isAPulse")
			return thisTorpGuideLife <= 0.0 or thisTorpTurn == 0.0

	def attackaFirePoint(pAction, pWeaponSystem, pFirePoint, pShip, pInstance):
		debug(__name__ + ", attackaFirePoint")
		pShipInst = None
		if pShip:
			pShipInst = FoundationTech.dShips[pShip.GetName()]
		if pInstance and not pShipInst == None: # and pShipInst == pInstance:
			vSubsystemOffset = App.TGPoint3()
			vSubsystemOffset.SetXYZ(0, 0, 0)
			#pWeaponSystem.Fire(pFirePoint, vSubsystemOffset)
			pWeaponSystem.StartFiring(pFirePoint, vSubsystemOffset)
		return 0
		

	def WeaponaHit(pObject, pEvent):
		debug(__name__ + ", WeaponaHit")
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
                #print "firepoint was hit, moving to block the torp"
		if pShip:
			global dictFirePointToTorp
			if dictFirePointToTorp.has_key(pShip.GetName()):
				pTorp = dictFirePointToTorp[pShip.GetName()]
                        
				# check if the torpedo still exists:
				if App.Torpedo_GetObjectByID(None, pTorp.GetObjID()):
					# get the World location of out Firepoint
					kLocation = pTorp.GetWorldLocation()
                                
					# For the Explosion Size
					if pShip.GetPowerSubsystem():
						pShip.GetPowerSubsystem().GetProperty().SetPowerOutput(pTorp.GetDamage() / 10)

					# Detach it from the Torpedo
					if not App.g_kUtopiaModule.IsMultiplayer():
						pTorp.DetachObject(pShip)
                                
					# and let the torpedo fly on our Firepoint to get destroyed
					pTorp.SetTarget(pShip.GetObjID())
                                                                
					# tell other clients to also move the firepoint to the ship
					if App.g_kUtopiaModule.IsMultiplayer():
						MPSendRemoveTorpMessage(pTorp)
                                
					# Let the Torp destroy the Firepoint
					pShip.SetTranslate(kLocation)
					pShip.UpdateNodeOnly()
                                
					del dictFirePointToTorp[pShip.GetName()]
        
		pObject.CallNextHandler(pEvent)
		return 0

	def DeleteFirePoint(pAction, sThisFirePointName):
		debug(__name__ + ", DeleteFirePoint")
		global dictFirePointToTorp
		#print "deleting firepoint"
		pFirepoint = MissionLib.GetShip(sThisFirePointName)
		if not pFirepoint:
			return 0

		pFirepoint.GetContainingSet().RemoveObjectFromSet(sThisFirePointName)

		if dictFirePointToTorp.has_key(sThisFirePointName):
			del dictFirePointToTorp[sThisFirePointName]
                
		# send clients to remove this object
		if App.g_kUtopiaModule.IsMultiplayer():
			# Now send a message to everybody else that the score was updated.
			# allocate the message.
			pMessage = App.TGMessage_Create()
			pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet
						
			# Setup the stream.
			kStream = App.TGBufferStream()		# Allocate a local buffer stream.
			kStream.OpenBuffer(256)				# Open the buffer stream with a 256 byte buffer.
	
			# Write relevant data to the stream.
			# First write message type.
			kStream.WriteChar(chr(REMOVE_POINTER_FROM_SET))

			# Write the name of killed ship
			for i in range(len(sThisFirePointName)):
				kStream.WriteChar(sThisFirePointName[i])
				# set the last char:
			kStream.WriteChar('\0')

			# Okay, now set the data from the buffer stream to the message
			pMessage.SetDataFromStream(kStream)

			# Send the message to everybody but me.  Use the NoMe group, which
			# is set up by the multiplayer game.
			pNetwork = App.g_kUtopiaModule.GetNetwork()
			if not App.IsNull(pNetwork):
				if App.g_kUtopiaModule.IsHost():
					pNetwork.SendTGMessageToGroup("NoMe", pMessage)
				else:
					pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)

			# We're done.  Close the buffer.
			kStream.CloseBuffer()
		#print "and I return"
		return 0

	def MPSendRemoveTorpMessage(pTorp):
		# Now send a message to everybody else that the score was updated.
		# allocate the message.
		debug(__name__ + ", MPSendRemoveTorpMessage")
		pMessage = App.TGMessage_Create()
		pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet
                        
		# Setup the stream.
		kStream = App.TGBufferStream()		# Allocate a local buffer stream.
		kStream.OpenBuffer(256)				# Open the buffer stream with a 256 byte buffer.
	
		# Write relevant data to the stream.
		# First write message type.
		kStream.WriteChar(chr(REMOVE_TORP_MESSAGE_AT))

		pNetwork = App.g_kUtopiaModule.GetNetwork()
        
        
		kStream.WriteInt(pNetwork.GetLocalID())
		kLocation = pTorp.GetWorldLocation()
		kStream.WriteFloat(kLocation.GetX())
		kStream.WriteFloat(kLocation.GetY())
		kStream.WriteFloat(kLocation.GetZ())

		# Okay, now set the data from the buffer stream to the message
		pMessage.SetDataFromStream(kStream)

		# Send the message to everybody but me.  Use the NoMe group, which
		# is set up by the multiplayer game.
		if not App.IsNull(pNetwork):
			if App.g_kUtopiaModule.IsHost():
				pNetwork.SendTGMessageToGroup("NoMe", pMessage)
			else:
				pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)

		# We're done.  Close the buffer.
		kStream.CloseBuffer()
		#print "end of MPSendRemoveTorpMessage"

	oSimulatedPointDefence = SimulatedPointDefenceDef('Simulated Point Defence')

except:
	print "Something went wrong wih Simulated Point Defence technology"
	traceback.print_exc()
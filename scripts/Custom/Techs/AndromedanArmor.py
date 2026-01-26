# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE FOUNDATION LGPL LICENSE AS WELL
# Andromedan.py
# 26th January 2026, by Alex SL Gato, based on a Cristalline armour adjusted for colors, fixed by Alex SL Gato (CharaToLoki), modified from Greystar's (which was likely an ftb AblativeArmour script copy)
# Also based on SlowStart.py by Alex SL Gato.
#
# Meant to be used alongside ftb AblativeArmour, in fact, it requires it to work properly. It also requires to have the FIX-AblativeArmour1dot0 too to work properly.
# It also changes how the armour it inherits from is used, now it can provide a third field
# Basically when hit, if the armour is still working, it will transform the damage onto energy for beam and pulse weapons!
"""
# Examples of use:
# FIRST, add the following to the scripts/Customs/Ships/whateverShip.py file you want to add this tech.
# NOTE: replace "saturn" for your ship's abbrev
# If oyou only want the basic one, where the health is the only thing determining that, and everytything else is default (that is, the hardpoint property will be the one stated on "GetSystemName", and all beams and pulses will recharge when hit) choose this:
Foundation.ShipDef.saturn.dTechs = {
	'Andromedan-type Armor': 485000,
}
# If you want to determine the hardpoint property name, choose something like this
Foundation.ShipDef.saturn.dTechs = {
	'Andromedan-type Armor': [485000, "Potato tasty chip"]
}
# If you want to determine what weapon properties benefit from this tech, choose this:
# Notes:
# - "GlobalFactor" determines how much they recharge (it's a multiplier of the event damage).
# - "HealDepletes" is also a multiplier, which indicates if a healing weapon will depower these instead (1), if it will ignore it (0) or if it will replenish energy too (-1), or if it will gain more or something in-between.
# - "Beams" lists a bunch of phaser beam properties, and "Pulses" does the same for pulse firing properties. If these fields do not apepar, it will assume all beams and all pusles can benefit from thsi tech.
# - "DmgStrMod" and "DmgRadMod" affect how much is the visible mesh affected when hit, multiplying, the visible strength of the impact and the visible radious when the armour hardpoint is not dead. If neither of them are there, it will not modify any visible armour setting.
Foundation.ShipDef.saturn.dTechs = {
	'Andromedan-type Armor': [485000, {"Beams": ["One phaser hardpoint name", "another laser hardpoint name"], "Pulses": ["One pulse hardpoint name", "Another disruptor hardpoint name"], "GlobalFactor": 1.0, "HealDepletes": 0, "DmgStrMod": 0.0, "DmgRadMod": 0.0}]
}

# If you want to do everything at once, do this:
Foundation.ShipDef.saturn.dTechs = {
	'Andromedan-type Armor': [485000, "Potato tasty chip", {"Beams": ["One phaser hardpoint name", "another laser hardpoint name"], "Pulses": ["One pulse hardpoint name", "Another disruptor hardpoint name"], "GlobalFactor": 1.0, "HealDepletes": 0, "DmgStrMod": 0.0, "DmgRadMod": 0.0}]
}
"""
# SECOND, you need to add a hardpoint health property (could be a hull subsystem, but can also be another kind of subsystem... anything with actual health, no OEP of blinking light properties, please!) on that ships's script/ships/Hardpoints/whatever.py file with the same name as those used on the scripts/Custom/Ships/whateverShip.py one.
# i.e. if you called an armour "Potato tasty chip", then a hardpoint property called exactly "Potato tasty chip" (case-sensitive) must exist!
# Also the hardpoint's max health will determine the final long-term resistance of the armour.
##################################
#
MODINFO = { "Author": "\"ftb Team\", \"Apollo\", \"Greystar\", \"Alex SL Gato\" (andromedavirgoa@gmail.com)",
	    "Version": "0.13",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }
#
#################################################################################################################
#
import App
from bcdebug import debug
import traceback

import Foundation
import FoundationTech


# TO-DO PLEASE AFTER TESTING TELL ME ANY PROBLEMS SO I CAN FIX THEM, PLUS ADD THE ACCESIBILITY FEATURE!
kEmptyColor = App.TGColorA()
kEmptyColor.SetRGBA(App.g_kSubsystemFillColor.r,App.g_kSubsystemFillColor.g,App.g_kSubsystemFillColor.b,App.g_kSubsystemFillColor.a)
kFillColor = App.TGColorA()
kFillColor.SetRGBA(100.0/255.0, 255.0/255.0, 255.0/255.0, App.g_kSubsystemFillColor.a)

AblativeArmour = None
oAndromedanArmor = None
try:
	AblativeArmour = __import__("ftb.Tech.AblativeArmour") #from ftb.Tech import AblativeArmour
except:
	try:
		AblativeArmour = __import__("Custom.Techs.AblativeArmour")
	except:
		AblativeArmour = None

if AblativeArmour != None:

	def findShipInstance(pShip):
		debug(__name__ + ", findShipInstance")
		pInstance = None
		try:
			if not pShip:
				return pInstance
			if FoundationTech.dShips.has_key(pShip.GetName()):
				pInstance = FoundationTech.dShips[pShip.GetName()]
		except:
			pass
		return pInstance

	def GetWellShipFromID(pShipID):
		pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShipID)
		if not pShip or pShip.IsDead() or pShip.IsDying():
			return None
		return pShip

	parentOnDefense = AblativeArmour.AblativeDef.OnDefense
	#parentAttach = AblativeArmour.AblativeDef.Attach
	class AndromedanArmorDef(AblativeArmour.AblativeDef):
		def GetSystemName(self):
			debug(__name__ + ", GetSystemName")
			return "Andromedan-type Armor"

		def GetFillColor(self):
			global kFillColor
			return kFillColor
		
		def GetEmptyColor(self):
			global kEmptyColor
			return kEmptyColor

		def Attach(self, pInstance):
			parentAttach(self, pInstance)


		def Attach(self, pInstance):
			debug(__name__ + ", Attach")
			pInstance.lTechs.append(self)
			pInstance.lTorpDefense.append(self)
			pInstance.lPulseDefense.append(self)
			pInstance.lBeamDefense.append(self)

			# Due to singletons, issues could happen
			pInstanceDict = pInstance.__dict__
			self.lName = str(self.name) + " L"
			self.lNameOld = self.lName + " Old"
			if not pInstanceDict.has_key(self.lName):
				if str(pInstanceDict[str(self.name)])[0] == "[":
					pInstanceDict[self.lName] = [0.0, str(self.GetSystemName()), {}]
					pInstanceDict[self.lNameOld] = [0.0, str(self.GetSystemName()), {}]

					myLen = len(pInstance.__dict__[str(self.name)])

					if myLen > 1:
						pInstanceDict[self.lName][0] = pInstance.__dict__[str(self.name)][0]
						pInstanceDict[self.lNameOld][0] = pInstance.__dict__[str(self.name)][0]
						if myLen < 3:
							extra = 1 + (type({}) == type(pInstance.__dict__[str(self.name)][1]))
							pInstanceDict[self.lName][extra] = pInstance.__dict__[str(self.name)][1]
							pInstanceDict[self.lNameOld][extra] = pInstance.__dict__[str(self.name)][1]

						else:
							pInstanceDict[self.lName][1] = pInstance.__dict__[str(self.name)][1]
							pInstanceDict[self.lNameOld][1] = pInstance.__dict__[str(self.name)][1]

							pInstanceDict[self.lName][2] = pInstance.__dict__[str(self.name)][2]
							pInstanceDict[self.lNameOld][2] = pInstance.__dict__[str(self.name)][2]
						
						self.conditionalVisibleDmgSwitch(pInstance, None, 1.0)
					else:
						pInstanceDict[self.lName] = pInstance.__dict__[str(self.name)][0]
						pInstanceDict[self.lNameOld] = pInstance.__dict__[str(self.name)][0]
				else:
					pInstanceDict[self.lName] = pInstance.__dict__[str(self.name)]
					pInstanceDict[self.lNameOld] = pInstance.__dict__[str(self.name)]


		def conditionalVisibleDmgSwitch(self, pInstance, pShip=None, repair=-1.0):
			try:
				if pInstance != None:
					pInstanceDict = pInstance.__dict__
					if hasattr(self, "lName") and hasattr(self, "lNameOld") and pInstanceDict.has_key(self.lName) and pInstanceDict.has_key(self.lNameOld):
						if str(pInstanceDict[str(self.name)])[0] == "[":
							myLen = len(pInstanceDict[str(self.name)])
							if myLen > 2:
								setDmgStrMod = "None"
								setDmgRadMod = "None"
								if pInstanceDict[self.lName][2].has_key("DmgStrMod"):
									setDmgStrMod = pInstanceDict[self.lName][2]["DmgStrMod"]

								if pInstanceDict[self.lName][2].has_key("DmgRadMod"):
									setDmgRadMod = pInstanceDict[self.lName][2]["DmgRadMod"]

								if (setDmgStrMod != None and setDmgStrMod != "None") or (setDmgRadMod != None and setDmgRadMod != "None"):
									iShipID = None
									if pShip != None and hasattr(pShip, "GetObjID"):
										iShipID = pShip.GetObjID()
									elif pInstance != None and hasattr(pInstance, "pShipID"):
										iShipID = pInstance.pShipID

									pShip2 = GetWellShipFromID(iShipID)
									if pShip2 != None:
										if repair > 0.0:
											self.SetDmgRadMod(pInstance, pShip2, setDmgRadMod, setDmgStrMod)
										else:
											self.SetDmgRadMod(pInstance, pShip2, None, None)
			except:
				print __name__, "Error on conditionalVisibleDmgSwitch:"
				traceback.print_exc()


		def SetDmgRadModif(self, pShip, dmgRd=None, dmgStr=None):
			myRad = 1.0
			myStr = 1.0
			pShipModule = None
			if pShip and hasattr(pShip, "GetScript"):
				pShipModule = __import__(pShip.GetScript())

			if not pShipModule:
				print "WARNING: Some vessel does not have a ship module???"
				return
			try:
				
				kStats=pShipModule.GetShipStats()
				if (kStats.has_key('DamageRadMod')):
					myRad = kStats['DamageRadMod']

				if (kStats.has_key('DamageStrMod')):
					myStr = kStats['DamageStrMod']
			except:
				print __name__, " Warning on SetDmgRadModif: "
				traceback.print_exc()
				try:
					if hasattr(pShipModule, "GetDamageRadMod"):
						myRad = pShipModule.GetDamageRadMod()
				except:
					myRad = 1.0

				try:
					if hasattr(pShipModule, "GetDamageStrMod"):
						myStr = pShipModule.GetDamageStrMod()
				except:
					myStr = 1.0

			if dmgRd == None:
				pShip.SetVisibleDamageRadiusModifier(myRad)
			elif dmgRd != "None":
				pShip.SetVisibleDamageRadiusModifier(dmgRd)				

			if dmgStr == None:
				pShip.SetVisibleDamageStrengthModifier(myStr)
			elif dmgStr != "None":
				pShip.SetVisibleDamageStrengthModifier(dmgStr)	

			
			
		def OnDefense(self, pShip, pInstance, oYield, pEvent):
			
			repair = pInstance.__dict__[self.lName]

			print 'TO-DO AndromedanArmorDef', pShip.GetName(), repair, pEvent.GetDamage()

			validSubsystems = None
			pSubName = self.GetSystemName()
			if str(repair)[0] == "[":
				pSubName = repair[1]
				repair = repair[0]
				validSubsystems = repair[2]
			
			if repair > 0.0:
				rechargeIs = pEvent.GetDamage()

				if validSubsystems.has_key("GlobalFactor"):
					rechargeIs = rechargeIs * validSubsystems["GlobalFactor"]

				if validSubsystems.has_key("HealDepletes"):
					if pEvent.GetDamage() < 0.0:
						rechargeIs = rechargeIs * validSubsystems["HealDepletes"]
					
				if validSubsystems.has_key("Beams"):
					if len(validSubsystems["Beams"]) > 0:
						print "TO-DO Found things, now to see"
						pWeaponSystem1 = pShip.GetPhaserSystem()

						if pWeaponSystem1:
							subsystemsOptions = validSubsystems["Beams"]	
							print "TO-DO I have beams to update"

							iChildren = pWeaponSystem1.GetNumChildSubsystems()
							if iChildren > 0:
								for iIndex in range(iChildren):
									pChild = pWeaponSystem1.GetChildSubsystem(iIndex)
									if pChild.GetName() in subsystemsOptions:
										self.setChargeToX(pChild, rechargeIs)
										self.setChildrenSubsystemsChargeToX(pChild, rechargeIs)
				else:
					print "TO-DO: I do not have beams key, I will assume all phasers have ", __name__, " ability"
					phasers = pShip.GetPhaserSystem()
					self.setChildrenSubsystemsChargeTo0(phasers)

				if validSubsystems.has_key("Pulses"):

					if len(validSubsystems["Pulses"]) > 0:
						pWeaponSystem1 = pShip.GetPulseWeaponSystem()

						if pWeaponSystem1:
							subsystemsOptions = validSubsystems["Pulses"]	

							iChildren = pWeaponSystem1.GetNumChildSubsystems()
							if iChildren > 0:
								for iIndex in range(iChildren):
									pChild = pWeaponSystem1.GetChildSubsystem(iIndex)
									if pChild.GetName() in subsystemsOptions:
										self.setChargeToX(pChild, rechargeIs)
										self.setChildrenSubsystemsChargeToX(pChild, rechargeIs)

					else:
						print "TO-DO: I do not have pulses key, I will assume all pulses have ", __name__, " ability"
						pulses = pShip.GetPulseWeaponSystem()
						self.setChildrenSubsystemsChargeTo0(pulses)

			repairV = -1
			if repair != None and (type(1.0) == type(repair) or type(1) == type(repair)):
				repairV = repair

			self.conditionalVisibleDmgSwitch(pInstance, pShip, repairV)

			parentOnDefense(self, pShip, pInstance, oYield, pEvent)

		def setChildrenSubsystemsChargeToX(self, pSystem, dmgAmount):
			if not pSystem:
				return
			for i in range(pSystem.GetNumChildSubsystems()):
				pChild = pSystem.GetChildSubsystem(i)
				self.setChargeToX(pChild, dmgAmount)
				self.setChildrenSubsystemsChargeToX(pChild, dmgAmount)


		def setChargeToX(self, pSubsystem, dmgAmount):
			try:
				print "Subsystem found to set charge to X"
				pWeapon = App.PhaserBank_Cast(pSubsystem)
				if not pWeapon:
					pWeapon = App.PulseWeapon_Cast(pSubsystem)
					if not pWeapon:
						pWeapon = App.EnergyWeapon_Cast(pSubsystem)

				if pWeapon and hasattr(pWeapon, "SetChargeLevel") and hasattr(pWeapon, "GetChargeLevel") and hasattr(pWeapon, "GetMaxCharge"):
					minCharge = 0.0
					maxCharge = pWeapon.GetMaxCharge()
					myCharge = pWeapon.GetChargeLevel() + dmgAmount
					if myCharge > maxCharge:
						myCharge = maxCharge
					elif  myCharge < minCharge:
						myCharge = minCharge
					
					pWeapon.SetChargeLevel(myCharge)
			except:
				print "error with ", __name__, ":"
				traceback.print_exc()


	oAndromedanArmor = AndromedanArmorDef('Andromedan-type Armor')
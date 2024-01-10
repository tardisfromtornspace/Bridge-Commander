#         Rainbow hardpoint
#         9th January 2024
#         Based strongly on TachyonBeam.py, DampeningAOEDefensiveField.py and RealityBomb.py by Alex Sl Gato, which was based on scripts\Custom\DS9FX\DS9FXPulsarFX\PulsarManager by USS Sovereign, and slightly on TractorBeams.py, Inversion Beam and Power Drain Beam 1.0 by MLeo Daalder, Apollo, and Dasher; some team-switching torpedo by LJ; and GraviticLance by Alex SL Gato, which was based on FiveSecsGodPhaser by USS Frontier, scripts/ftb/Tech/TachyonProjectile by the FoundationTechnologies team, and scripts/ftb/Tech/FedAblativeArmour by the FoundationTechnologies team.
#         Also based strongly on PulseTech.py by ed and ShieldGenerators.py by Defiant
#         Inspired by Greystar's random rainbow colors.
#################################################################################################################
# This tech gives a ship the ability to change its phaser colors and shields at random

# Usage Example:  Add this to the dTechs attribute of your ShipDef, in the Ship plugin file (replace "Sovereign" with the proper abbrev).
# "Period": this is more of how often is this ship supposed to change colors
# "Beams": if the field exists, it will affect the Beams. If the field exists but is empty, it will target all beams - else it will only target the named hardpoint properties.
# "Shields": if the field exists, it will affect the Shields. If the field exists but is empty, it will target all Shield Generators - else it will only target the named hardpoint properties.
# "Beam Transparency" and "Shield Transparency": if these fields exist, transparency of beams and shields will be randomized as well
# "BUG LANCE": if this field exists, it will try to constantly change in a more forced way, in such a way that it guarantess the colors change, but the phasers detach and start flying on their own and the ship may be slightly OP. Only kept for mere research purposes
# Distance: Range of effect of this ability. Logically cannot be equal or less than 0, so if you don't want this ship to do anything apart from sounds, set it to 0. Default is 1000000 km.

"""
Foundation.ShipDef.Sovereign.dTechs = {
	'Rainbow Hardpoint' : { "Beams": ["Beam Name 1", "Beam Name 2"], "Shields": ["Shield Generator name 1", "Shield Generator name 2"], "Beam Transparency": 0", Shield Transparency": 0, "BUG LANCE": 0}
}
"""

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "0.1",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }

import App
import traceback
from bcdebug import debug

import Foundation
import FoundationTech
import Lib.LibEngineering
import loadspacehelper
import math
import MissionLib
import string
import time

try:
	defaultPeriod = 0.5
	defaultSlice = 0.1

	bOverflow = 0 # may want to tweak this so if you don't end up having like 200 timers and make STBC explode

	pAllShipsWithTheTech = {} # Has the ship, with the pInstances as keys

	pTimer = None

	def Start():
		global pTimer, bOverflow
	
		if not bOverflow:
			pTimer = RainbowTorpTech()
		else:
			return
	class RainbowTorpTech(FoundationTech.TechDef):

		def __init__(self, name):

			#print "ATTENTION: Called Rainbow Hardpoint Script"
			FoundationTech.TechDef.__init__(self, name)
			global bOverflow
			
			self.pEventHandler = App.TGPythonInstanceWrapper()
			self.pEventHandler.SetPyWrapper(self)

			self.pTimer = None
			bOverflow = 1
			self.countdown()

		def countdown(self):
			debug(__name__ + ", Countdown")
			if not self.pTimer:
				global defaultSlice
				self.pTimer = App.PythonMethodProcess()
				self.pTimer.SetInstance(self)
				self.pTimer.SetFunction("lookAtThis")
				self.pTimer.SetDelay(defaultSlice)
				self.pTimer.SetPriority(App.TimeSliceProcess.LOW)	
				self.pTimer.SetDelayUsesGameTime(1)

		def Attach(self, pInstance):
			debug(__name__ + ", Attach")
			pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
			if pShip != None:
				global bOverflow, pAllShipsWithTheTech
				dMasterDict = pInstance.__dict__['Rainbow Hardpoint']
				pAllShipsWithTheTech[pInstance] = pShip

				if not bOverflow:
					bOverflow = 1
					self.pTimer = None
					#print "RainbowHardpoint: initiating new countdown for:", pShip.GetName()
					self.countdown()
					
			else:
				print "RainbowHardpoint Error (at Attach): couldn't acquire ship of id", pInstance.pShipID
				pass

			pInstance.lTechs.append(self)
			print "RainbowHardpoint: attached to ship:", pShip.GetName()

		def Detach(self, pInstance):
			debug(__name__ + ", Detach")
			pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
			if pShip != None:
				global bOverflow, pAllShipsWithTheTech
				dMasterDict = pInstance.__dict__['Rainbow Hardpoint']
				
				#pAllShipsWithTheTech.pop(pInstance, None)
				if pAllShipsWithTheTech.has_key(pInstance):
					print "key found, to remove ", pInstance
					del pAllShipsWithTheTech[pInstance]
				self.pShip = None
			else:
				#print "RainbowHardpoint Error (at Detach): couldn't acquire ship of id", pInstance.pShipID
				pass
			pInstance.lTechs.remove(self)
			print "DRB: detached from ship:"
			if pShip != None:
				print "---ship name:", pShip.GetName()

		def Detach2(self, pInstance, pShip):
			debug(__name__ + ", Detach2")
			global bOverflow, pAllShipsWithTheTech
			
			if not pInstance and pShip:
				try:
					pInstance = FoundationTech.dShips[pShip.GetName()]
					if pInstance == None:
						return
				except:
					print "Rainbow Hardpoint: cancelling, error in try from Detach2 found..."
					return
				
			if pAllShipsWithTheTech.has_key(pInstance):
				print "key found, to remove ", pInstance
				del pAllShipsWithTheTech[pInstance]
			if pShip == None and pInstance != None:
				pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
			if pShip != None and pInstance != None:
				dMasterDict = pInstance.__dict__['Rainbow Hardpoint']
			else:
				print "Rainbow Hardpoint Error (at Detach): couldn't acquire ship"
				if pInstance != None:
					print "--- of id", pInstance.pShipID
				pass

			print "Rainbow Hardpoint: cleanup-detached from ship"
			if pShip != None:
				print "---ship name:", pShip.GetName()

			if pInstance != None:
				pInstance.lTechs.remove(self)

		def lookAtThis(self, fTime):
			debug(__name__ + ", Rainbow Hardpoint Counter lookAtThis")
			global pAllShipsWithTheTech
			for myShipInstance in pAllShipsWithTheTech.keys():
				self.lookcloserships(fTime, pAllShipsWithTheTech[myShipInstance], myShipInstance)

		def lookcloserships(self, fTime, pShip, pInstance):
			debug(__name__ + ", Reality Bomb Counter lookcloserships")
			pShip2 = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID)) # If ship does not exist, do not continue
			if pShip == None or pInstance == None or pShip.IsDead() or pShip.IsDying() or not pShip2:
				self.Detach2(pInstance, pShip)
				return

			#print "The ship which is using it is ", pShip.GetName()

			global defaultPeriod, defaultSlice


			if not pInstance.__dict__["Rainbow Hardpoint"].has_key("Period"):
				pInstance.__dict__["Rainbow Hardpoint"]["Period"] = defaultPeriod

			if not pInstance.__dict__["Rainbow Hardpoint"].has_key("TimeRemaining"):
				pInstance.__dict__["Rainbow Hardpoint"]["TimeRemaining"] = 0.0

			pInstance.__dict__["Rainbow Hardpoint"]["TimeRemaining"] = pInstance.__dict__["Rainbow Hardpoint"]["TimeRemaining"] - defaultSlice

			if pInstance.__dict__["Rainbow Hardpoint"]["TimeRemaining"] > 0:	
				return
			else:
				pInstance.__dict__["Rainbow Hardpoint"]["TimeRemaining"] = pInstance.__dict__["Rainbow Hardpoint"]["Period"]
				
				pWeaponSystem1 = pShip.GetPhaserSystem()

				if pWeaponSystem1 and pInstance.__dict__['Rainbow Hardpoint'].has_key("Beams"):
					print "I have beams to update"
					lBeamNames = []
					if len(pInstance.__dict__['Rainbow Hardpoint']["Beams"]) > 0:
						lBeamNames = pInstance.__dict__['Rainbow Hardpoint']["Beams"]

					transparency = 0
					if pInstance.__dict__['Rainbow Hardpoint'].has_key("Beam Transparency"):
						transparency = 1

					iChildren = pWeaponSystem1.GetNumChildSubsystems()
					if iChildren > 0:
						for iIndex in range(iChildren):
							pChild = pWeaponSystem1.GetChildSubsystem(iIndex)
							self.Heal(lBeamNames, pChild, transparency)
					pWeaponSystem1.SetForceUpdate(1)	

				#else:
				#	print "FSTB: I do not have beams key or phaser control"

				pShieldSystem1 = pShip.GetShields()

				lShieldNames = []
				if pShieldSystem1 and pInstance.__dict__['Rainbow Hardpoint'].has_key("Shields"):
					print "I have shields to update"
					lBeamNames = []
					if len(pInstance.__dict__['Rainbow Hardpoint']["Shields"]) > 0:
						lShieldNames = pInstance.__dict__['Rainbow Hardpoint']["Shields"]

					transparency = 0
					if pInstance.__dict__['Rainbow Hardpoint'].has_key("Shield Transparency"):
						transparency = 1

					self.Healds(lShieldNames, pShieldSystem1, transparency)
					retlist = self.GetAllShieldGenerators(pShip)
					for shieldProp in retlist:
						self.Healds(lShieldNames, shieldProp, transparency)

				#else:
				#	print "FSTB: I do not have shields key or shield control"


				pShip.UpdateNodeOnly()
				if pInstance.__dict__['Rainbow Hardpoint'].has_key("BUG LANCE"):
					pShip.SetupProperties()

				#global pAllShipsWithTheTech
				#pAllShipsWithTheTech[pInstance] = pShip

			# App.g_kTimerManager.DeleteTimer(pTimer) ## or something similar to delete the timer once something in particular has happened to make it end 
			return 0

		def Healds(self, lBeamNames, pSubsystem, transparency=0):
			if pSubsystem.GetName() in lBeamNames or len(lBeamNames) <= 0:
				print "updating", pSubsystem.GetName()
				try:
					pWeapon = App.ShieldClass_Cast(pSubsystem)
					pthisShield = App.ShieldProperty_Cast(pWeapon.GetProperty())
					ShieldGeneratorShieldGlowColor = self.getPhaserColorRdm(transparency)
					pthisShield.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
				except:
					print "hm"
					traceback.print_exc()

			iChildren = pSubsystem.GetNumChildSubsystems()
			if iChildren > 0:
				for iIndex in range(iChildren):
					pChild = pSubsystem.GetChildSubsystem(iIndex)
					self.Healds(pInstance, pChild)


		def Heal(self, lBeamNames, pSubsystem, transparency=0):
			if pSubsystem.GetName() in lBeamNames or len(lBeamNames) <= 0:
				print "updating", pSubsystem.GetName()
				try:
					pWeapon = App.PhaserBank_Cast(pSubsystem)
					pthisPhaser = App.PhaserProperty_Cast(pWeapon.GetProperty())
					kColor = self.getPhaserColorRdm(transparency)
					pthisPhaser.SetOuterShellColor(kColor)
					kColor = self.getPhaserColorRdm(transparency)
					pthisPhaser.SetInnerShellColor(kColor)
					kColor = self.getPhaserColorRdm(transparency)
					pthisPhaser.SetOuterCoreColor(kColor)
					kColor = self.getPhaserColorRdm(transparency)
					pthisPhaser.SetInnerCoreColor(kColor)
					#pthisPhaser.UpdateNodeOnly()
					#pSubsystem.UpdateNodeOnly()
					#pSubsystem.Update()
					#pShip.UpdateNodeOnly()
				except:
					print "hm"
					traceback.print_exc()

			iChildren = pSubsystem.GetNumChildSubsystems()
			if iChildren > 0:
				for iIndex in range(iChildren):
					pChild = pSubsystem.GetChildSubsystem(iIndex)
					self.Heal(pInstance, pChild, pShip)

		def getPhaserColorRdm(self, transparency=0):
			kColor = App.TGColorA()
			
			rgba = self.getRandomSpectrum(transparency)
			kColor.SetRGBA(rgba[0], rgba[1], rgba[2], rgba[3])
			return kColor

		def getRandomSpectrum(self, transparency=0):
			red = App.g_kSystemWrapper.GetRandomNumber(255)/255.0
			green = App.g_kSystemWrapper.GetRandomNumber(255)/255.0
			blue = App.g_kSystemWrapper.GetRandomNumber(255)/255.0
			theA = 1.0
			if transparency:
				theA = App.g_kSystemWrapper.GetRandomNumber(255)/255.0

			myOutput = [red, green, blue, theA]
			return myOutput
			
		def GetAllShieldGenerators(self, pShip):
			retList = []
	
			pPropSet = pShip.GetPropertySet()
			pShipSubSystemPropInstanceList = pPropSet.GetPropertiesByType(App.CT_SHIELD_PROPERTY)
			iNumItems = pShipSubSystemPropInstanceList.TGGetNumItems()
			pShipSubSystemPropInstanceList.TGBeginIteration()
			for i in range(iNumItems):
				pInstance = pShipSubSystemPropInstanceList.TGGetNext()
				pProperty = App.ShieldProperty_Cast(pInstance.GetProperty())
				if not pProperty.IsPrimary():
					pSubSystem = pShip.GetSubsystemByProperty(pProperty)
					pShieldGenerator = App.ShieldClass_Cast(pSubSystem)
					retList.append(pShieldGenerator)
	
			pShipSubSystemPropInstanceList.TGDoneIterating()
			return retList

	oExample = RainbowTorpTech("Rainbow Hardpoint")

except:
	print "Something went wrong"
	traceback.print_exc()

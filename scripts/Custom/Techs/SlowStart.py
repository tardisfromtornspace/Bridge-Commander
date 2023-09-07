#################################################################################################################
#         TachyonBeam by Alex SL Gato
#         Version 0.1
#         7th September 2023
#         Based on FiveSecsGodPhaser by USS Frontier, scripts/ftb/Tech/TachyonProjectile by the FoundationTechnologies team, and scripts/ftb/Tech/FedAblativeArmour by the FoundationTechnologies team
#         NOTE: This is a proof of an untested idea/concept, only for energy weapons               
#################################################################################################################
# Little simple tech. Any ships with phasers/pulses and equipped with this will have a slow start on specified weapons.
#############################################
# Usage Example:  Add this to the dTechs attribute of your ShipDef, in the Ship plugin file
# but modify the values accordingly to what you want, and for actual values since the following is just a general example
# Beams: this field indicates which beams on your ship have tachyon beam properties. Don't add the field or leave it empty to consider all phasers tachyon beams
"""
Foundation.ShipDef.Sovereign.dTechs = {
	"Slow Start": {"Beams": ["PhaserName1", "PhaserName2", "PulseName1", "PulseName4"]}
}
"""

from bcdebug import debug

import App
import FoundationTech


class SlowStartWeapon(FoundationTech.TechDef):

	def setChargeTo0(self, pSubsystem):
		if hasattr(pSubsystem, "SetChargeLevel"):
			pSubsystem.SetChargeLevel(0.0)

	def setChildrenSubsystemsChargeTo0(self, pSystem):
		if not pSystem:
			return
		for i in range(pSystem.GetNumChildSubsystems()):
			pChild = pSystem.GetChildSubsystem(i)
			self.setChargeTo0(pChild)
			self.setChildrenSubsystemsChargeTo0(pChild)

	def Attach(self, pInstance):
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		if pShip != None:
			if not pInstance.__dict__.has_key("Slow Start"):
				print "Slow Start: cancelling, ship does not have Slow Start equipped..."
				return

			dMasterDict = pInstance.__dict__['Slow Start']
		
			if pInstance.__dict__['Slow Start'].has_key("Beams") and len(pInstance.__dict__['Slow Start']["Beams"]) > 0:


				subsystemsOptions = pInstance.__dict__['TachyonBeam']["Beams"]	

				kIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
				while (1):
					pSubsystem = pShip.GetNextSubsystemMatch(kIterator)
					if not pSubsystem:
						break
			
					if pSubsystem.GetName() in lArmorNames:
						self.setChargeTo0(pChild)
			
					for i in range(pSubsystem.GetNumChildSubsystems()):
						pChild = pSubsystem.GetChildSubsystem(i)
						if pSubsystem.GetName() in lArmorNames:
							self.setChargeTo0(pChild)

				pShip.EndGetSubsystemMatch(kIterator)

			else:
				print "Slow Start: I do not have beams key, I will assume all phasers and pulses have Slow Start ability"
				pulses = pShip.GetPulseWeaponSystem()
				phasers = pShip.GetPhaserSystem()
				self.setChildrenSubsystemsChargeTo0(pulses)
				self.setChildrenSubsystemsChargeTo0(phasers)
			print "Slow Start: attached to ship:", pShip.GetName()

		else:
			print "Slow Start Error (at Attach): couldn't acquire ship of id", pInstance.pShipID
			pass

		pInstance.lTechs.append(self)

	def Detach(self, pInstance):
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		if pShip != None:
			dMasterDict = pInstance.__dict__['Slow Start']
		else:
			#print "Slow Start Error (at Detach): couldn't acquire ship of id", pInstance.pShipID
			pass
		pInstance.lTechs.remove(self)
		#print "Slow Start: detached from ship:", pShip.GetName()
    
oSlowStartWeapon = SlowStartWeapon('Slow Start')

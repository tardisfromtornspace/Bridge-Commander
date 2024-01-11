#################################################################################################################
#         TachyonBeam by Alex SL Gato
#         11th January 2024
#         Based on FiveSecsGodPhaser by USS Frontier, scripts/ftb/Tech/TachyonProjectile by the FoundationTechnologies team, and scripts/ftb/Tech/FedAblativeArmour by the FoundationTechnologies team
#         NOTE: This is a tested proof of concept, only for energy weapons               
#################################################################################################################
# Little simple tech. Any ships with phasers/pulses and equipped with this will have a slow start on specified weapons. While this could also be used for tractors, I preferred to not include such option.
#############################################
# Usage Example:  Add this to the dTechs attribute of your ShipDef, in the Ship plugin file but modify the values accordingly to what you want, and for actual values since the following is just a general example
# Beams: this field indicates which beams on your ship have slow start properties. Leave the list empty to consider all phasers.
# Beams: this field indicates which pulses on your ship have slow start properties. Leave the list empty to consider all pulses.
"""
Foundation.ShipDef.Sovereign.dTechs = {
	"Slow Start": {"Beams": ["PhaserName1", "PhaserName2", "PhaserName3", "PhaserName4"], "Pulses": ["PulseName1", "PulseName2", "PulseName3", "PulseName4"]}
}
"""

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "0.2",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }

from bcdebug import debug

import App
import FoundationTech
import traceback

class SlowStartWeapon(FoundationTech.TechDef):

	#def __init__(self, name):
		#FoundationTech.TechDef.__init__(self, name)
		#self.pEventHandler = App.TGPythonInstanceWrapper()
		#self.pEventHandler.SetPyWrapper(self)
		#App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_CREATED, self.pEventHandler, "ObjectCreatedHandler")
		#App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_OBJECT_CREATED, self.pEventHandler, "ObjectCreatedHandler")
		#print "Initialized TachyonBeam"

	def setChargeTo0(self, pSubsystem):
		#if hasattr(pSubsystem, "SetChargeLevel"):
		try:
			print "Subsystem found to set charge to 0"
			pWeapon = App.PhaserBank_Cast(pSubsystem)
			#pthisPhaser = App.PhaserProperty_Cast(pWeapon.GetProperty())
			pWeapon.SetChargeLevel(0.0)
		except:
			print "error with slow start"
			traceback.print_exc()


	def ObjectCreatedHandler(self, pEvent):
		debug(__name__ + ", ObjectCreatedHandler")
	
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		if pShip != None:
			try:
				pInstance = FoundationTech.dShips[pShip.GetName()]
				if pInstance == None:
					#print "FSTB: cancelling, no FTech Ship Instance obj"
					return
			except:
				#print "FSTB: cancelling, error in try found..."
				return

			if not pInstance.__dict__.has_key("Slow Start"):
				print "Slow Start: cancelling, ship does not have Slow Start equipped..."
				return

			self.CommonStartPart(pShip, pInstance)

	def CommonStartPart(self, pShip, pInstance):
			#if pInstance.__dict__['Slow Start'].has_key("Already done"):
			#	print "Slow Start: cancelling, ship already had this done..."
			#	return

			#pInstance.__dict__['Slow Start']["Already done"] = 1
		
			if pInstance.__dict__['Slow Start'].has_key("Beams"):

				if len(pInstance.__dict__['Slow Start']["Beams"]) > 0:

					print "Found things, now to see"
					subsystemsOptions = pInstance.__dict__['Slow Start']["Beams"]	

					pWeaponSystem1 = pShip.GetPhaserSystem()

					if pWeaponSystem1:
						print "I have beams to update"

						iChildren = pWeaponSystem1.GetNumChildSubsystems()
						if iChildren > 0:
							for iIndex in range(iChildren):
								pChild = pWeaponSystem1.GetChildSubsystem(iIndex)
								if pChild.GetName() in subsystemsOptions:
									self.setChargeTo0(pChild)
									self.setChildrenSubsystemsChargeTo0(pChild)

				else:
					print "Slow Start: I do not have beams key, I will assume all phasers have Slow Start ability"
					phasers = pShip.GetPhaserSystem()
					self.setChildrenSubsystemsChargeTo0(phasers)

			if pInstance.__dict__['Slow Start'].has_key("Pulses"):

				if len(pInstance.__dict__['Slow Start']["Pulses"]) > 0:

					print "Found things, now to see"
					subsystemsOptions = pInstance.__dict__['Slow Start']["Pulses"]	

					pWeaponSystem1 = pShip.GetPulseWeaponSystem()

					if pWeaponSystem1:
						print "I have pulses to update"

						iChildren = pWeaponSystem1.GetNumChildSubsystems()
						if iChildren > 0:
							for iIndex in range(iChildren):
								pChild = pWeaponSystem1.GetChildSubsystem(iIndex)
								if pChild.GetName() in subsystemsOptions:
									self.setChargeTo0(pChild)
									self.setChildrenSubsystemsChargeTo0(pChild)

				else:
					print "Slow Start: I do not have beams key, I will assume all pulses have Slow Start ability"
					pulses = pShip.GetPulseWeaponSystem()
					self.setChildrenSubsystemsChargeTo0(pulses)

			print "Slow Start: attached to ship:", pShip.GetName()

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
			self.CommonStartPart(pShip, pInstance)
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

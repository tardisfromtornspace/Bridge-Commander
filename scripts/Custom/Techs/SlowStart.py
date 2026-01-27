#################################################################################################################
#         SlowStart by Alex SL Gato
#         27th January 2026
#         Based on FiveSecsGodPhaser by USS Frontier, scripts/ftb/Tech/TachyonProjectile by the FoundationTechnologies team, and scripts/ftb/Tech/FedAblativeArmour by the FoundationTechnologies team
#         Elminster did something similar for the DCMP Sau Paulo and for the BOBW Galaxy, but I really did not know of that script's existance at the time I made this script.        
#################################################################################################################
# Little simple tech. Any ships with phasers/pulses and equipped with this will have a slow start on specified weapons. While this could also be used for tractors, I preferred to not include such option.
#############################################
# Usage Example:  Add this to the dTechs attribute of your ShipDef, in the Ship plugin file but modify the values accordingly to what you want, and for actual values since the following is just a general example
# Beams: this field indicates which beams on your ship have slow start properties. Leave the list empty to consider all phasers.
# Pulses: this field indicates which pulses on your ship have slow start properties. Leave the list empty to consider all pulses.
# Torpedoes: same, but for torpedo tubes
# Tractors: same, but for tractors (normally this would not do a thing, tho).
# "GlobalFactor": multiplier of the charge available at start. default is 0
#  -- Note: you can also add particular multipliers to each weapon system separately.  (for example "BeamsFactor")
"""
Foundation.ShipDef.Sovereign.dTechs = {
	"Slow Start": {"Beams": ["PhaserName1", "PhaserName2", "PhaserName3", "PhaserName4"], "Pulses": ["PulseName1", "PulseName2", "PulseName3", "PulseName4"]}
}
"""

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "0.3",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }

from bcdebug import debug

import App
import FoundationTech
import traceback

validWeaponTypes = {"Beams": "GetPhaserSystem", "Pulses": "GetPulseWeaponSystem", "Tractors": "GetTractorBeamSystem", "Torpedoes": "GetTorpedoSystem"} # Relation between key names and the functions to obtain their control subsystems

class SlowStartWeapon(FoundationTech.TechDef):

	#def __init__(self, name):
		#FoundationTech.TechDef.__init__(self, name)
		#self.pEventHandler = App.TGPythonInstanceWrapper()
		#self.pEventHandler.SetPyWrapper(self)
		#App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_CREATED, self.pEventHandler, "ObjectCreatedHandler")
		#App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_OBJECT_CREATED, self.pEventHandler, "ObjectCreatedHandler")
		#print "Initialized TachyonBeam"

	def setChargeToX(self, pSubsystem, dmgAmount):
		try:
			pWeapon = App.PhaserBank_Cast(pSubsystem)
			if not pWeapon:
				pWeapon = App.PulseWeapon_Cast(pSubsystem)
				if not pWeapon:
					pWeapon = App.EnergyWeapon_Cast(pSubsystem)

			if pWeapon and hasattr(pWeapon, "SetChargeLevel") and hasattr(pWeapon, "GetChargeLevel") and hasattr(pWeapon, "GetMaxCharge"):
				minCharge = 0.0
				maxCharge = pWeapon.GetMaxCharge()
				myoldCharge = pWeapon.GetChargeLevel()
				myCharge = myoldCharge * dmgAmount
				if myCharge > maxCharge:
					myCharge = maxCharge
				elif  myCharge < minCharge:
					myCharge = minCharge
				if myoldCharge != myCharge:
					pWeapon.SetChargeLevel(myCharge)

			else:
				pWeapon = App.TorpedoTube_Cast(pSubsystem)
				if pWeapon and hasattr(pWeapon, "SetNumReady") and hasattr(pWeapon, "GetNumReady") and hasattr(pWeapon, "GetMaxReady"):
					minCharge = 0.0
					maxCharge = pWeapon.GetMaxReady()
					myoldCharge = pWeapon.GetNumReady()
					myCharge = myoldCharge * int(dmgAmount)
					if myCharge > maxCharge:
						myCharge = maxCharge
					elif  myCharge < minCharge:
						myCharge = minCharge
					if myoldCharge != myCharge:
						pWeapon.SetNumReady(myCharge)
		except:
			print "error with ", __name__, ":"
			traceback.print_exc()

	def setChargeTo0(self, pSubsystem):
		self.setChargeToX(pSubsystem, 0)

	def setChildrenSubsystemsChargeToX(self, pSystem, dmgAmount):
		if not pSystem:
			return
		for i in range(pSystem.GetNumChildSubsystems()):
			pChild = pSystem.GetChildSubsystem(i)
			self.setChargeToX(pChild, dmgAmount)
			self.setChildrenSubsystemsChargeToX(pChild, dmgAmount)

	def setChildrenSubsystemsChargeTo0(self, pSystem):
		self.setChildrenSubsystemsChargeToX(pSystem, 0)

	def CommonStartPart(self, pShip, pInstance):
		if pInstance:
			validSubsystems = {}
			pInstanceDict = pInstance.__dict__
			if pInstanceDict and pInstanceDict.has_key("Slow Start"):
				validSubsystems = pInstanceDict['Slow Start']

			rechargeIs = 0
			if validSubsystems.has_key("GlobalFactor"):
				rechargeIs = rechargeIs * validSubsystems["GlobalFactor"]

			for wpnType in validWeaponTypes.keys():
				try:
					self.checkWhichSubToChg(validSubsystems, pShip, wpnType, rechargeIs)
				except:
					traceback.print_exc()

			print __name__, ": attached to ship:", pShip.GetName()

	def checkWhichSubToChg(self, validSubsystems, pShip, key, rechargeIs):
		if validSubsystems.has_key(key) and len(validSubsystems[key]) > 0:
			keyFactor = str(key)+"Factor"
			if validSubsystems.has_key(keyFactor):
				rechargeIs = rechargeIs * validSubsystems[keyFactor]

			pWeaponSystem = self.getControlSys(pShip, key)
			self.chargeSubsystemTypes(pWeaponSystem, validSubsystems, key, rechargeIs)

	def getControlSys(self, pShip, key):
		pSubsystem = None
		if key != None and validWeaponTypes.has_key(key):
			if hasattr(pShip, validWeaponTypes[key]):
				try:
					getWpnSysF = getattr(pShip, validWeaponTypes[key])
					if getWpnSysF:
						pSubsystem = getWpnSysF()
				except:
					print __name__, " error on getControlSys: "
					traceback.print_exc()
					pSubsystem = None
		return pSubsystem

	def chargeSubsystemTypes(self, pWeaponSystem, validSubsystems, key, rechargeIs):
		if pWeaponSystem:
			subsystemsOptions = validSubsystems[key]	

			iChildren = pWeaponSystem.GetNumChildSubsystems()
			if iChildren > 0:
				for iIndex in range(iChildren):
					pChild = pWeaponSystem.GetChildSubsystem(iIndex)
					if pChild and pChild.GetName() in subsystemsOptions:
						self.setChargeToX(pChild, rechargeIs)
						self.setChildrenSubsystemsChargeToX(pChild, rechargeIs)

	def Attach(self, pInstance):
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		if pShip != None:
			if not pInstance.__dict__.has_key("Slow Start"):
				#print "Slow Start: cancelling, ship does not have Slow Start equipped..."
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


oSlowStartWeapon = SlowStartWeapon('Slow Start')

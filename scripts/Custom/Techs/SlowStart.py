#################################################################################################################
#         SlowStart by Alex SL Gato
#         18th March 2026
#         Based on FiveSecsGodPhaser by USS Frontier, scripts/ftb/Tech/TachyonProjectile by the FoundationTechnologies team, and scripts/ftb/Tech/FedAblativeArmour by the FoundationTechnologies team
#         Elminster did something similar for the DCMP Sau Paulo and for the BOBW Galaxy, but I really did not know of that script's existance at the time I made this script.        
#################################################################################################################
# Little simple tech. Any ships with phasers/pulses and equipped with this will have a slow start on specified weapons. While this could also be used for tractors, I preferred to not include such option.
#############################################
# Usage Example:  Add this to the dTechs attribute of your ShipDef, in the Ship plugin file but modify the values accordingly to what you want, and for actual values since the following is just a general example
# Beams: this field indicates which beams on your ship have slow start properties. Leave the list empty to consider all phasers.
# Pulses: this field indicates which pulses on your ship have slow start properties. Leave the list empty to consider all pulses.
# Torpedoes: same, but for torpedo tubes.
# -- "TorpedoesFix": a related field, called , meant to regulate a potential issue with torpedoes, where if you were to discharge normally and the torpedo tube got empty, it would never fire again until you changed torpedo load:
# ---- "TorpedoesFix": -2 : the ship will not use any safeties to prevent the torpedo tubes from totally unloading and no automatic torpedo load change fix will be applied - useful if you are actually interested on having some sort of "faulty" torpedo tubes.
# ---- "TorpedoesFix": -1: the ship will use a safety measure where none of the torpedo tubes will be totally emptied (will leave at least 1 torpedo ready).
# ---- "TorpedoesFix": 5: default behaviour, the ship will use a safety measure where none of the torpedo tubes will be totally emptied (will leave at least 1 torpedo ready) and if the percentage charge sent was meant to be 0%, then will force a change on the torpedo load.
# Tractors: same, but for tractors (normally this would not do a thing, tho).
# ---- "TorpedoesFix: 0 : same as "TorpedoesFix": 5, but the ammo is replenished instantly (when why would you even want to do this??? I'm not sure but better leave it as an option).
# ---- "TorpedoesFix": with any other value greater than 0, would do nearly the same as "TorpedoesFix": 5
# ---- "TorpedoesFix": -3 or even lesser values, do NOT apply those values unless you want to know what happens when you apply a negative value to a TorpedoSystem's SetAmmoType function.
# "GlobalFactor": multiplier of the charge available at start. default is 0
#  -- Note: you can also add particular multipliers to each weapon system separately.  (for example "BeamsFactor"), but not all of these depend on the global factor, so with a global factor of 0 you cannot give more energy to beams!
"""
Foundation.ShipDef.Sovereign.dTechs = {
	"Slow Start": {"Beams": ["PhaserName1", "PhaserName2", "PhaserName3", "PhaserName4"], "Pulses": ["PulseName1", "PulseName2", "PulseName3", "PulseName4"], "GlobalFactor": 0.5, "BeamsFactor": 0, "TorpedoesFix": -1}
}
"""

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "0.34",
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

	def setChargeToX(self, pSubsystem, dmgAmount, extraChg = 1):
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
					minCharge = 0
					maxCharge = pWeapon.GetMaxReady()
					myoldCharge = pWeapon.GetNumReady()
					myCharge = int(myoldCharge * int(dmgAmount)) + extraChg
					if myCharge > maxCharge:
						myCharge = maxCharge
					elif myCharge < (minCharge):
						myCharge = minCharge
					if myoldCharge != myCharge:
						pWeapon.SetNumReady(myCharge)

		except:
			print "error with ", __name__, ":"
			traceback.print_exc()

	def setChargeTo0(self, pSubsystem, extraChg = 0):
		self.setChargeToX(pSubsystem, 0, extraChg)

	def setChildrenSubsystemsChargeToX(self, pSystem, dmgAmount, extraChg=1):
		if not pSystem:
			return
		for i in range(pSystem.GetNumChildSubsystems()):
			pChild = pSystem.GetChildSubsystem(i)
			self.setChargeToX(pChild, dmgAmount, extraChg)
			self.setChildrenSubsystemsChargeToX(pChild, dmgAmount, extraChg)

	def setChildrenSubsystemsChargeTo0(self, pSystem, extraChg=1):
		self.setChildrenSubsystemsChargeToX(pSystem, 0, extraChg)

	def CommonStartPart(self, pShip, pInstance):
		if pInstance:
			validSubsystems = {}
			pInstanceDict = pInstance.__dict__
			if pInstanceDict and pInstanceDict.has_key(self.name):
				validSubsystems = pInstanceDict[self.name]

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
		if validSubsystems.has_key(key) and (type(validSubsystems[key]) == type ([])):
			keyFactor = str(key)+"Factor"
			if validSubsystems.has_key(keyFactor):
				rechargeIs = rechargeIs * validSubsystems[keyFactor]

			performRAfix = -1
			if str(key) == "Torpedoes":
				keyFix = str(key)+"Fix"
				if validSubsystems.has_key(keyFix) and validSubsystems[keyFix] != -1:
					performRAfix = validSubsystems[keyFix]
				else:
					performRAfix = 5

			extraChg = (performRAfix != -2)
			pWeaponSystem = self.getControlSys(pShip, key)
			self.chargeSubsystemTypes(pWeaponSystem, validSubsystems, key, rechargeIs, extraChg)

			if rechargeIs <= 0 and performRAfix != -1 and extraChg:
				if pWeaponSystem:
					iNumTypes = pWeaponSystem.GetNumAmmoTypes()
					if iNumTypes > 0:
						# Fill torpedo tubes.
						pWeaponSystem.SetAmmoType(0, int(performRAfix))
					pWeaponSystem.Update(1)
					pWeaponSystem.SetForceUpdate(1)

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

	def chargeSubsystemTypes(self, pWeaponSystem, validSubsystems, key, rechargeIs, extraChg=1):
		if pWeaponSystem:
			subsystemsOptions = validSubsystems[key]	

			iChildren = pWeaponSystem.GetNumChildSubsystems()
			if iChildren > 0:
				for iIndex in range(iChildren):
					pChild = pWeaponSystem.GetChildSubsystem(iIndex)
					if pChild and (len(subsystemsOptions) == 0 or pChild.GetName() in subsystemsOptions):
						self.setChargeToX(pChild, rechargeIs, extraChg)
						self.setChildrenSubsystemsChargeToX(pChild, rechargeIs, extraChg)

	def Attach(self, pInstance):
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		if pShip != None:
			if not pInstance.__dict__.has_key(self.name):
				#print self.name, ": cancelling, ship does not have ", self.name, " equipped..."
				return

			dMasterDict = pInstance.__dict__[self.name]
			self.CommonStartPart(pShip, pInstance)
		else:
			print self.name, ": Error (at Attach): couldn't acquire ship of id", pInstance.pShipID
			pass

		pInstance.lTechs.append(self)

	def Detach(self, pInstance):
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		if pShip != None:
			dMasterDict = pInstance.__dict__[self.name]
		else:
			#print self.name, ": Error (at Detach): couldn't acquire ship of id", pInstance.pShipID
			pass
		pInstance.lTechs.remove(self)
		#print self.name, ": detached from ship:", pShip.GetName()
    
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

			if not pInstance.__dict__.has_key(self.name):
				print self.name, ": cancelling, ship does not have ", self.name, " equipped..."
				return

			self.CommonStartPart(pShip, pInstance)


oSlowStartWeapon = SlowStartWeapon('Slow Start')

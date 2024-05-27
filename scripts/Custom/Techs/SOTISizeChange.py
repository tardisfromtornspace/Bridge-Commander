#################################################################################################################
#         SOTISizeChange by Alex SL Gato
#         26th May 2024
#         Based on StarcraftDefensiveMatrix by Alex SL Gato.
#                 
#################################################################################################################
# Little simple tech. Any ships with this SOTI Size tech will change size according to a subsystem type energy value.
# The technology will require to deactivate, then re-activate the desired subsystem to change the ship size - this is done so people can have a tiny ship and still use that subsystem at max power, or vice-versa.
#############################################
# Usage Example:  Add this to the dTechs attribute of your ShipDef, in the Ship plugin file.
# "Scale": default is 1, it is a multiplier to all sizes.
# "Power": basically this is going to also increase the max gap between min and max size, it will perform a size ^ Power.
# "Types": indicates a list of subsystems to check, according to power given to such subsystem. While more options from App.py could be checked, like other Powered Subsystems, it is heavily discouraged. Also better to keep it to only 1 type.
# -- For shields: "App.CT_SHIELD_SUBSYSTEM"
# -- For weapons: "App.CT_WEAPON_SYSTEM" for generic weapon, "App.CT_TORPEDO_SYSTEM", "App.CT_PHASER_SYSTEM", "App.CT_PULSE_WEAPON_SYSTEM", "App.CT_TRACTOR_BEAM_SYSTEM" for phaser, torpedo, pulse or tractor control subsystems, respectively.
# -- For sensors": "App.CT_SENSOR_SUBSYSTEM"
# -- For engines": "App.CT_WARP_ENGINE_SUBSYSTEM" are FTL engines, "App.CT_IMPULSE_ENGINE_SUBSYSTEM" are normal engines.
# -- For repairs": "App.CT_REPAIR_SUBSYSTEM"

"""
Foundation.ShipDef.Sovereign.dTechs = {
	"SOTI Size Change": {"Scale": 1.0, "Power": 1, "Types": [App.CT_SHIELD_SUBSYSTEM]}
}
"""

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "0.1",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }

from bcdebug import debug

import App
import FoundationTech
import traceback

def findShipInstance(pShip):
	pInstance = None
	try:
		pInstance = FoundationTech.dShips[pShip.GetName()]
		if pInstance == None:
			print "After looking, no tech pInstance for ship:", pShip.GetName(), "How odd..."
		
	except:
		pass

	return pInstance

class SOTISizeChange(FoundationTech.TechDef):

	def Attach(self, pInstance):
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		if pShip != None:
			if not pInstance.__dict__.has_key("SOTI Size Change"):
				print "SOTI Size Change: cancelling, ship does not have SOTI Size Change equipped..."
				return

			if not pInstance.__dict__.has_key("SOTI Size Change Active"): # This is the size, to avoid changing size when it isn't different
				pInstance.__dict__["SOTI Size Change Active"] = 1.0

			pShip.RemoveHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged")
			pShip.AddPythonFuncHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged")
		else:
			print "SOTI Size Change Error (at Attach): couldn't acquire ship of id", pInstance.pShipID
			#pass

		pInstance.lTechs.append(self)

	def Detach(self, pInstance):
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		if pShip != None:
			pShip.RemoveHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged")
			pShip.RemoveHandlerForInstance(App.ET_ENTERED_SET, __name__ + ".EnterSet")
		else:
			#print "SOTI Size Change Error (at Detach): couldn't acquire ship of id", pInstance.pShipID
			pass

		if pInstance.__dict__.has_key("SOTI Size Change Active"):
			del pInstance.__dict__["SOTI Size Change Active"]

		pInstance.lTechs.remove(self)
		#print "SOTI Size Change: detached from ship:", pShip.GetName()

	def ChangeSize(self, pShip, pInstance, scale = 1.0):
		pShip.SetScale(scale)
		pShip.UpdateNodeOnly()
    
oSOTISizeChange = SOTISizeChange('SOTI Size Change')

# called when a ship changes Power of one of its subsystems
# cause this is possibly also an alert event
def SubsystemStateChanged(pObject, pEvent):
	debug(__name__ + ", SubsystemStateChanged")

	if pObject == None:
		return

	pShipID = pObject.GetObjID()
	pShip = App.ShipClass_GetObjectByID(None, pShipID)
	if not pShip:
		return

	if pEvent == None:
		pObject.CallNextHandler(pEvent)
		return

        pSubsystem = pEvent.GetSource()
	if not pSubsystem:
		pObject.CallNextHandler(pEvent)
		return

	pSubsystem = App.PoweredSubsystem_Cast(pSubsystem)
	if not pSubsystem or not hasattr(pSubsystem, "GetPowerPercentageWanted"):
		pObject.CallNextHandler(pEvent)
		return

	powerWanted = pSubsystem.GetPowerPercentageWanted()

	pInstance = findShipInstance(pShip)
	if pInstance:
		instanceDict = pInstance.__dict__
		if instanceDict.has_key("SOTI Size Change"):
			if instanceDict["SOTI Size Change"].has_key("Types"):
				scale = 1.0
				power = 1.0

				if instanceDict["SOTI Size Change"].has_key("Scale"):
					scale = instanceDict["SOTI Size Change"]["Scale"]

				if instanceDict["SOTI Size Change"].has_key("Power"):
					power = instanceDict["SOTI Size Change"]["Power"]

				index = 0
				while index < len(instanceDict["SOTI Size Change"]["Types"]):
					if pSubsystem.IsTypeOf(instanceDict["SOTI Size Change"]["Types"][index]):
						try:
							if powerWanted != None:
								if powerWanted > 1.0:
									powerWanted = (powerWanted -1) * 10 + 1
								if powerWanted != instanceDict["SOTI Size Change Active"]:
									scale = scale * powerWanted
						except:
							print "Error while checking subsystem change in SOTI Size Change"
							traceback.print_exc()

						index = len(instanceDict["SOTI Size Change"]["Types"])
					index = index + 1

				if scale != 0:
					oSOTISizeChange.ChangeSize(pShip, pInstance, (scale**power))	
					
	pObject.CallNextHandler(pEvent)
	return


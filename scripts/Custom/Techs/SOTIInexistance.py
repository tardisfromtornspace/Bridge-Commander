#################################################################################################################
#         SOTIInexistance by Alex SL Gato
#         26th May 2024
#         Based on StarcraftDefensiveMatrix by Alex SL Gato.
#                 
#################################################################################################################
# Little simple tech. Any ships with this SOTI Inexistance tech cannot be hit from fire, planets or anything conventional as long as shields are active. It's like some Phase Cloak variants, except everyone can see you and fire at you,
# and the tech is actually shield-related.
#############################################
# Usage Example:  Add this to the dTechs attribute of your ShipDef, in the Ship plugin file. The number value "1" on this example is inconsequential.
"""
Foundation.ShipDef.Sovereign.dTechs = {
	"SOTI Inexistance": 1
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

class SOTIInexistance(FoundationTech.TechDef):

	def CommonStartPart(self, pShip, pInstance):

		pShipID = pShip.GetObjID()
		pShip = App.ShipClass_GetObjectByID(None, pShipID)
		if pShip and pInstance.__dict__.has_key('SOTI Inexistance'):
			pShields = pShip.GetShields()
			if pShields:
				pShields.TurnOn()

			pInstance.__dict__["SOTI Inexistance Active"] = 1
			self.ActivateDefense(pShip, pInstance, 1)

	def ActivateDefense(self, pShip, pInstance, activate = 0):
		pSet = pShip.GetContainingSet()
		if not pSet:
			return 0

		pProxManager = pSet.GetProximityManager()
		if pProxManager:
			if activate == 1:
				try:
					pProxManager.RemoveObject(pShip)
				except:
					print "Error while activating SOTI Inexistance"
					traceback.print_exc()
			else:
				try:
					pProxManager.AddObject(pShip)
				except:
					print "Error while deactivating SOTI Inexistance"
					traceback.print_exc()

	def Attach(self, pInstance):
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		if pShip != None:
			if not pInstance.__dict__.has_key("SOTI Inexistance"):
				print "SOTI Inexistance: cancelling, ship does not have SOTI Inexistance equipped..."
				return

			if not pInstance.__dict__.has_key("SOTI Inexistance Active"):
				pInstance.__dict__["SOTI Inexistance Active"] = 0

			pShip.RemoveHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged")
			pShip.RemoveHandlerForInstance(App.ET_ENTERED_SET, __name__ + ".EnterSet")
			pShip.AddPythonFuncHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged")
			pShip.AddPythonFuncHandlerForInstance(App.ET_ENTERED_SET, __name__ + ".EnterSet")
			self.CommonStartPart(pShip, pInstance)
		else:
			print "SOTI Inexistance Error (at Attach): couldn't acquire ship of id", pInstance.pShipID
			#pass

		pInstance.lTechs.append(self)

	def Detach(self, pInstance):
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		if pShip != None:
			pShip.RemoveHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged")
			pShip.RemoveHandlerForInstance(App.ET_ENTERED_SET, __name__ + ".EnterSet")
		else:
			#print "SOTI Inexistance Error (at Detach): couldn't acquire ship of id", pInstance.pShipID
			pass

		if pInstance.__dict__.has_key("SOTI Inexistance Active"):
			del pInstance.__dict__["SOTI Inexistance Active"]

		pInstance.lTechs.remove(self)
		#print "SOTI Inexistance: detached from ship:", pShip.GetName()
    
oSOTIInexistance = SOTIInexistance('SOTI Inexistance')

# called when a ship enters a Set.
# the tech calls for safety, when switching to another system, shields and this defense will be automatically activated.
def EnterSet(pObject, pEvent):
        debug(__name__ + ", EnterSet")

        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())

        if pShip:
            pInstance = findShipInstance(pShip)
            if pInstance:
                oSOTIInexistance.CommonStartPart(pShip, pInstance)

# called when a ship changes Power of one of its subsystems
# cause this is possibly also an alert event
def SubsystemStateChanged(pObject, pEvent):
	debug(__name__ + ", SubsystemStateChanged")

	if pObject == None:
		return

	pShipID = pObject.GetObjID()
	if not pShipID:
		return

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

        if pSubsystem.IsTypeOf(App.CT_SHIELD_SUBSYSTEM):
		wpnActiveState = 0
		if hasattr(pEvent, "GetBool"):
			wpnActiveState = pEvent.GetBool()
			pShields = pShip.GetShields()
			if pShields:
				pInstance = findShipInstance(pShip)
				if pInstance:
					instanceDict = pInstance.__dict__
					if instanceDict.has_key("SOTI Inexistance"):
						if wpnActiveState != instanceDict["SOTI Inexistance Active"]: # Means shields have changed
							if wpnActiveState == 0: # Shields have been deactivated:
								instanceDict["SOTI Inexistance Active"] = 0

								oSOTIInexistance.ActivateDefense(pShip, pInstance, 0)

							else: # Shields have been activated

								instanceDict["SOTI Inexistance Active"] = 1

								oSOTIInexistance.ActivateDefense(pShip, pInstance, 1)

								#print "Attempt successfull, instanceDict is ", instanceDict
					


	pObject.CallNextHandler(pEvent)
	return


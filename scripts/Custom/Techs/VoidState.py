# Phase Cloak v1.0
#
# By:
#	 MLeo Daalder
#
# Requirements:
#	Foundation Technologies (Version 20050510 or later)
#
# Installation:
#	Place this file in scripts\Custom\Techs
#
# dTechs configuration:
#   add:
#	"VoidState": TimePenalty
#   where TimePenalty is replaced by a number which is the amount
#   in seconds that the Cloak is disabled when it (if it's active).
#   If you don't want a penalty, replace it with 0
#   NOTE: if you add a Phase Cloak tech to the ship, add this one after the phase cloak, not before.
#
# Credits:
#	Apollo for his Phase Cloak (this mod is based on his implementation of the Phase Cloak)
#		So no flying through planets! I could have done that, but then your ship wouldn't be hit by anything
#		(so the penalty is useless) and besides, flying through planets is boring anyway...
#		I can tell.;)
#	Dasher for his Foundation and FoundationTech


import App
import FoundationTech

class VoidState(FoundationTech.TechDef):

	def OnDefense(self, pShip, pInstance, oYield, pEvent):
		if pInstance.__dict__['Void State'] <= 0:
			return
		
		pCloak = pShip.GetCloakingSubsystem()
		if not pCloak:
			return

		# Now, decloak for a sec or 2...
		#	Depends on the setting in the Void State tuple...
		pInstance.Disable(pShip, pCloak, pInstance.__dict__["Void State"])

	def Attach(self, pInstance):
		pInstance.lTechs.append(self)
		if pInstance.__dict__["Void State"] > 0:
			pInstance.lTorpDefense.append(self)
			pInstance.lPulseDefense.append(self)
			pInstance.lBeamDefense.append(self)

		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))

		pShip.SetCollisionsOn(0)
		pShip.SetHurtable(0)
		pShip.SetTargetable(0)

		pShip.AddPythonFuncHandlerForInstance(App.ET_CLOAK_COMPLETED, __name__ + ".CloakHandler")
		pShip.AddPythonFuncHandlerForInstance(App.ET_DECLOAK_COMPLETED, __name__ + ".CloakHandler")


	def Detach(self, pInstance):		
		pInstance.lTechs.remove(self)
		if pInstance.__dict__["Void State"] > 0:
			pInstance.lTorpDefense.remove(self)
			pInstance.lPulseDefense.remove(self)
			pInstance.lBeamDefense.remove(self)
		
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))

		pShip.SetCollisionsOn(1)
		pShip.SetHurtable(1)
		pShip.SetTargetable(1)

		pShip.RemoveHandlerForInstance(App.ET_CLOAK_COMPLETED, __name__ + ".CloakHandler")
		pShip.RemoveHandlerForInstance(App.ET_DECLOAK_COMPLETED, __name__ + ".CloakHandler")

	def OnBeamDefense(self, pShip, pInstance, oYield, pEvent):
		return self.OnDefense(pShip, pInstance, oYield, pEvent)

	def OnPulseDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		return self.OnDefense(pShip, pInstance, oYield, pEvent)

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		return self.OnDefense(pShip, pInstance, oYield, pEvent)

oVoidState = VoidState("Void State")		

def CloakHandler(pObject, pEvent): # Ensuring things like Phase cloak don't mess things up
	App.DamageableObject_Cast(pObject).SetCollisionsOn(0)	# ReSet collisions, hurting and targetable off, so simple !!!
	pShip = App.ShipClass_Cast(pObject)
	pShip.SetCollisionsOn(0)
	pShip.SetHurtable(0)
	pShip.SetTargetable(0)

	pObject.CallNextHandler(pEvent)


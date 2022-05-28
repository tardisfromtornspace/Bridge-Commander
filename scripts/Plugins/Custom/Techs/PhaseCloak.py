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
#	"Phase Cloak": TimePenalty
#   where TimePenalty is replaced by a number which is the ammount
#   in seconds that the Cloak is disabled when it (if it's active).
#   If you don't want a penalty, replace it with 0
#
# Credits:
#	Apollo for his Phase Cloak (this mod is based on his implementation of the Phase Cloak)
#		So no flying through planets! I could have done that, but then your ship wouldn't be hit by anything
#		(so the penalty is useless) and besides, flying through planets is boring anyway...
#		I can tell.;)
#	Dasher for his Foundation and FoundationTech


import App
import FoundationTech

class PhaseCloak(FoundationTech.TechDef):

	def OnDefense(self, pShip, pInstance, oYield, pEvent):
		if not pEvent.IsHullHit():
			return
		if pInstance.__dict__['Phase Cloak'] <= 0:
			return
		
		pCloak = pShip.GetCloakingSubsystem()
		if not pCloak:
			return

		if not (pCloak.IsCloaked() or pCloak.IsTryingToCloak() or pCloak.IsCloaking() or pCloak.IsDecloaking()):
			#print pShip.GetName(), "is not cloaked and is not trying to cloak and is not cloaking", pCloak
			return

		# Now, decloak for a sec or 2...
		#	Depends on the setting in the Phase Cloak tuple...
		pInstance.Disable(pShip, pCloak, pInstance.__dict__["Phase Cloak"])

	def Attach(self, pInstance):
		pInstance.lTechs.append(self)
		if pInstance.__dict__["Phase Cloak"] > 0:
			pInstance.lTorpDefense.append(self)
			pInstance.lPulseDefense.append(self)
			pInstance.lBeamDefense.append(self)

		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))

		# I can't deside between ET_CLOAK_BEGINNING and ET_CLOAK_COMPLETED
		#	Same for the decloaking part...
		pShip.AddPythonFuncHandlerForInstance(App.ET_CLOAK_BEGINNING, __name__ + ".CloakHandler")
		pShip.AddPythonFuncHandlerForInstance(App.ET_DECLOAK_BEGINNING, __name__ + ".DecloakHandler")


	def Detach(self, pInstance):		
		pInstance.lTechs.remove(self)
		if pInstance.__dict__["Phase Cloak"] > 0:
			pInstance.lTorpDefense.remove(self)
			pInstance.lPulseDefense.remove(self)
			pInstance.lBeamDefense.remove(self)
		
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		pShip.RemoveHandlerForInstance(App.ET_CLOAK_BEGINNING, __name__ + ".CloakHandler")
		pShip.RemoveHandlerForInstance(App.ET_DECLOAK_BEGINNING, __name__ + ".DecloakHandler")

	def OnBeamDefense(self, pShip, pInstance, oYield, pEvent):
		return self.OnDefense(pShip, pInstance, oYield, pEvent)

	def OnPulseDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		return self.OnDefense(pShip, pInstance, oYield, pEvent)

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		return self.OnDefense(pShip, pInstance, oYield, pEvent)

oPhaseCloak = PhaseCloak("Phase Cloak")		

def CloakHandler(pObject, pEvent):
	App.DamageableObject_Cast(pObject).SetCollisionsOn(0)	#Set collisions off, so simple !!!
	pSound = App.g_kSoundManager.GetSound("PhaseCloakOn")
	if pSound:
		pSound.AttachToNode(pObject.GetNode())
		pSound.Play()
	pObject.CallNextHandler(pEvent)

def DecloakHandler(pObject, pEvent):
	App.DamageableObject_Cast(pObject).SetCollisionsOn(1)	#Set collisions on, so simple !!!
	pSound = App.g_kSoundManager.GetSound("PhaseCloakOff")
	if pSound:
		pSound.AttachToNode(pObject.GetNode())
		pSound.Play()
	pObject.CallNextHandler(pEvent)

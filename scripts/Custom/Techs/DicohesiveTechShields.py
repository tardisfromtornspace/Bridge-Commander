#################################################################################################################
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
#         DampeningAOEDefensiveField.py by Alex SL Gato
#         Version 1.1
#         4th March 2025
#         Based on scripts\Custom\DS9FX\DS9FXPulsarFX\PulsarManager by USS Sovereign, Inversion Beam and Power Drain Beam 1.0 by MLeo Daalder, Apollo, and Dasher; and GraviticLance by Alex SL Gato, which was based on FiveSecsGodPhaser by USS Frontier, scripts/ftb/Tech/Shields by the FoundationTechnologies team, and scripts/ftb/Tech/FedAblativeArmour by the FoundationTechnologies team. Also based on PhaseCloak.py by MLeo, Apollo and Dasher.
#         Special Thanks to USS Sovereign for telling me better tips to remove the need of a hardpoint-wise made-up axis.
#                          
#################################################################################################################
# This tech basically makes the ship unhurtable until a shield is breached and a hit comes from there.
# Usage Example:  Add this (the lines under the triple ") to the dTechs attribute of your ShipDef, in the Ship plugin file (replace "Sovereign" with the proper abbrev).
'''
Foundation.ShipDef.Sovereign.dTechs = {
	"Dicohesive Tech Shields": {}
}
'''

import App
import FoundationTech

from bcdebug import debug
import traceback

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
            "Version": "0.45",
            "License": "LGPL",
            "Description": "Read the small title above for more info"
            }

# This should be the prime example of a special yield weapon defined
# according to Foundation Technologies.  The code is mostly based upon
# QuickBattleAddon.corboniteReflector() in Apollo's Advanced Technologies.

try:
	class DicohesiveTechVoidDef(FoundationTech.TechDef):

		#def __init__(self, name):
		#	FoundationTech.TechDef.__init__(self, name)
		#	self.pEventHandler = App.TGPythonInstanceWrapper()
		#	self.pEventHandler.SetPyWrapper(self)
		#	App.g_kEventManager.RemoveBroadcastHandler(App.ET_SHIELD_COLLISION, self.pEventHandler, "ShieldChange")
		#	App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_SHIELD_COLLISION, self.pEventHandler, "ShieldChange")
		#	print "Initialized Dicohesive Tech Shields"

		def OnDefense(self, pShip, pInstance, oYield, pEvent):
			debug(__name__ + ", OnDefense")

			if not pShip:
				return

			if not pInstance.DicohesiveTechShields.has_key("Systems"):
				pInstance.DicohesiveTechShields["Systems"] = {}

			# position of the impact
			kPoint = NiPoint3ToTGPoint3(pEvent.GetObjectHitPoint())
			fRadius = pEvent.GetRadius()
			fDamage = pEvent.GetDamage()

			pShields = pShip.GetShields()
			shieldHitBroken = 0
			if not pShields or pShields.IsDisabled() or not pShields.IsOn():
				shieldHitBroken = 1
				pShip.SetVisibleDamageRadiusModifier(1.0)
				pShip.SetVisibleDamageStrengthModifier(1.0)

				pHull=pShip.GetHull()
				didIDie = self.StoreHurt(pInstance, pHull, shieldHitBroken, fDamage, pShip, fRadius, kPoint, 1)
				if didIDie == 1:
					pShip.RunDeathScript()
					return

				pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
				pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
				while pSubsystem:
					didIDie = self.StoreHurt(pInstance, pSubsystem, shieldHitBroken, fDamage, pShip, fRadius, kPoint)
					if didIDie == 1:
						pShip.RunDeathScript()
						return
					pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

				pShip.EndGetSubsystemMatch(pIterator)
				return
			pShields.TurnOn()

			# get the nearest reference
			pReferenciado = None
			dMasCercano = 0
			bPlateDisabled = 0
			pointForward = App.TGPoint3_GetModelForward()
			pointBackward = App.TGPoint3_GetModelBackward()
			pointTop = App.TGPoint3_GetModelUp()
			pointBottom = App.TGPoint3_GetModelDown()
			pointRight = App.TGPoint3_GetModelRight()
			pointLeft = App.TGPoint3_GetModelLeft()
			lReferencias = [pointForward, pointBackward, pointTop, pointBottom, pointLeft, pointRight]

			for pPunto in lReferencias:
				#print lReferencias.index(pPunto)
				pPunto.Subtract(kPoint)
				#print pPunto.Length()
				if pReferenciado == None or pPunto.Length() < dMasCercano:
					dMasCercano = pPunto.Length()
					pReferenciado = pPunto

			if not pReferenciado: # Something went wrong, but it is better to keep recording the damage
				print "Something went wrong when finding references, ship will likely be immortal"
				pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
				pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
				while pSubsystem:
					self.StoreHurt(pInstance, pSubsystem, shieldHitBroken, fDamage, pShip, fRadius, kPoint)
					pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
				pShip.EndGetSubsystemMatch(pIterator)
				return

			shieldDir = lReferencias.index(pReferenciado)
			fCurr = pShields.GetCurShields(shieldDir)
			fMax = pShields.GetMaxShields(shieldDir)
			if fCurr < 0.10 * fMax:
				if fCurr < 0.05 * fMax:
					shieldHitBroken = 1
				nerf = fCurr - fDamage
				if nerf < 0:
					nerf = 0
				pShields.SetCurShields(shieldDir, nerf)

			#print "pEvent.IsHullHit() and shieldHitBroken for shieldir of name", pEvent.IsHullHit(), shieldHitBroken, shieldDir, pReferenciado
			if pEvent.IsHullHit() and shieldHitBroken == 1: #TO-DO and things
				#print "Hurt"
				pShip.SetVisibleDamageRadiusModifier(1.0)
				pShip.SetVisibleDamageStrengthModifier(1.0)

				pHull=pShip.GetHull()
				didIDie = self.StoreHurt(pInstance, pHull, shieldHitBroken, fDamage, pShip, fRadius, kPoint, 1)
				if didIDie == 1:
					pShip.RunDeathScript()
					return
				pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
				pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

				while pSubsystem:
					didIDie = self.StoreHurt(pInstance, pSubsystem, shieldHitBroken, fDamage, pShip, fRadius, kPoint)
					if didIDie == 1:
						pShip.EndGetSubsystemMatch(pIterator)
						pShip.RunDeathScript()
						return
					pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

				pShip.EndGetSubsystemMatch(pIterator)

			else:
				#print "Heal"
				pShip.SetInvincible(1)
				pShip.SetVisibleDamageRadiusModifier(0.0)
				pShip.SetVisibleDamageStrengthModifier(0.0)

				pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
				pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

				while pSubsystem:
					self.Heal(pInstance, pSubsystem)
					pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

				pShip.EndGetSubsystemMatch(pIterator)

		def Heal(self, pInstance, pSubsystem):
			if not pInstance.DicohesiveTechShields["Systems"].has_key(pSubsystem.GetName()):
				pInstance.DicohesiveTechShields["Systems"][pSubsystem.GetName()] = pSubsystem.GetMaxCondition()
			if pSubsystem.GetCondition() > pInstance.DicohesiveTechShields["Systems"][pSubsystem.GetName()]:
				pInstance.DicohesiveTechShields["Systems"][pSubsystem.GetName()] = pSubsystem.GetCondition()

			pSubsystem.SetCondition(pInstance.DicohesiveTechShields["Systems"][pSubsystem.GetName()])
			iChildren = pSubsystem.GetNumChildSubsystems()
			if iChildren > 0:
				for iIndex in range(iChildren):
					pChild = pSubsystem.GetChildSubsystem(iIndex)
					self.Heal(pInstance, pChild)

		def StoreHurt(self, pInstance, pSubsystem, shieldHitBroken, fDamage, pShip, fRadius, kPoint, force=0):
			pInstance.DicohesiveTechShields["Systems"][pSubsystem.GetName()] = pSubsystem.GetCondition()
			if shieldHitBroken == 1 and pSubsystem.IsCritical() and pSubsystem.GetCondition() < fDamage:
				iamarmoredunderneath = pInstance.__dict__.has_key('Adv Armor Tech')
				vDifference = NiPoint3ToTGPoint3(pSubsystem.GetPosition())
				vDifference.Subtract(kPoint)
				if not iamarmoredunderneath and (force == 1 or vDifference.Length() < fRadius + pSubsystem.GetRadius()) :
					pShip.SetInvincible(0)
					pShip.DestroySystem(pSubsystem)
					return 1
			iChildren = pSubsystem.GetNumChildSubsystems()
			if iChildren > 0 and force == 0:
				for iIndex in range(iChildren):
					pChild = pSubsystem.GetChildSubsystem(iIndex)
					didIDie = self.StoreHurt(pInstance, pChild, shieldHitBroken, fDamage, pShip, fRadius, kPoint, force)
					if didIDie == 1:
						return didIDie
			return 0

		def OnBeamDefense(self, pShip, pInstance, oYield, pEvent):
			debug(__name__ + ", OnBeamDefense")
			return self.OnDefense(pShip, pInstance, oYield, pEvent)

		def OnPulseDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
			debug(__name__ + ", OnPulseDefense")
			return self.OnDefense(pShip, pInstance, oYield, pEvent)

		def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
			debug(__name__ + ", OnTorpDefense")
			return self.OnDefense(pShip, pInstance, oYield, pEvent)


		# TODO:  Make this an activated technology

		def Attach(self, pInstance):
			debug(__name__ + ", Attach")
			pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
			if pShip != None:

				#pGame = App.Game_GetCurrentGame()
				#pEpisode = pGame.GetCurrentEpisode()
				#pMission = pEpisode.GetCurrentMission()

				#print "script of the ship is ", pShip.GetScript()
				#pPropertySet = pShip.GetPropertySet()
				#mod = __import__('Custom.Techs.DicohesiveShieldsReference')
				#mod.LoadPropertySet(pPropertySet)

				#pShip.SetupProperties()
				#mod = __import__('Custom.Techs.DicohesiveShieldsReference')
				#pShip.Update() # TO-DO comprueba que esto funciona
				#pShip.UpdateNodeOnly()
				#if pShip.GetName() == pGame.GetPlayer().GetName():
				#	pShip = pGame.GetPlayer()
				#	pGame.SetPlayer(pShip)


				pInstance.DicohesiveTechShields = {}

				pShip.SetInvincible(1)
				pHull=pShip.GetHull()
				hull_max=pHull.GetMaxCondition()
				pHull.SetCondition(hull_max)
				pCloak = pShip.GetCloakingSubsystem()
				if pCloak:
					pShip.AddPythonFuncHandlerForInstance(App.ET_CLOAK_COMPLETED, __name__ + ".CloakHandler")
					pShip.AddPythonFuncHandlerForInstance(App.ET_CLOAK_BEGINNING, __name__ + ".CloakHandler")
					pShip.AddPythonFuncHandlerForInstance(App.ET_DECLOAK_BEGINNING, __name__ + ".DecloakHandler")
			pInstance.lTechs.append(self)
			pInstance.lTorpDefense.insert(0, self)		# Important to put shield-type weapons in the front
			pInstance.lPulseDefense.insert(0, self)
			pInstance.lBeamDefense.insert(0, self)
			# print 'Attaching Dicohesive Shields to', pInstance, pInstance.__dict__

		def Detach(self, pInstance):		
			pInstance.lTechs.remove(self)
			pInstance.lTorpDefense.remove(self)
			pInstance.lPulseDefense.remove(self)
			pInstance.lBeamDefense.remove(self)
		
			pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
			if pShip:
				pCloak = pShip.GetCloakingSubsystem()
				if pCloak:
					pShip.RemoveHandlerForInstance(App.ET_CLOAK_COMPLETED, __name__ + ".CloakHandler")
					pShip.RemoveHandlerForInstance(App.ET_CLOAK_BEGINNING, __name__ + ".CloakHandler")
					pShip.RemoveHandlerForInstance(App.ET_DECLOAK_BEGINNING, __name__ + ".DecloakHandler")

			if hasattr(pInstance, "DicohesiveTechShields"):
				del pInstance.DicohesiveTechShields

		# def Activate(self):
		# 	FoundationTech.oWeaponHit.Start()
		# def Deactivate(self):
		# 	FoundationTech.oWeaponHit.Stop()

		#def ShieldChange(self, pEvent):
		#	pTarget = App.ShipClass_Cast(pEvent.GetDestination())
		#	if pTarget == None:
		#		#print "Dicohesive Tech Shields: cancelling, no target"
		#		return
		#      # This is a stub, not wholly necessary yet	

	oDicohesiveTechVoid = DicohesiveTechVoidDef('Dicohesive Tech Shields')
    
	def NiPoint3ToTGPoint3(p):
		debug(__name__ + ", NiPoint3ToTGPoint3")
		kPoint = App.TGPoint3()
		kPoint.SetXYZ(p.x, p.y, p.z)
		return kPoint
    
	def CloakHandler(pObject, pEvent):
		App.DamageableObject_Cast(pObject).SetCollisionsOn(0)	#Set collisions off, so simple !!!
		pSound = App.g_kSoundManager.GetSound("PhaseCloakOn")
		if pSound:
			pSound.AttachToNode(pObject.GetNode())
			pSound.Play()
		pShip = App.ShipClass_Cast(pObject)
		if pShip:
			pShields = pShip.GetShields()
			if pShields:
				pShields.TurnOn()
		pObject.CallNextHandler(pEvent)

	def DecloakHandler(pObject, pEvent):
		App.DamageableObject_Cast(pObject).SetCollisionsOn(1)	#Set collisions on, so simple !!!
		pSound = App.g_kSoundManager.GetSound("PhaseCloakOff")
		if pSound:
			pSound.AttachToNode(pObject.GetNode())
			pSound.Play()
		pShip = App.ShipClass_Cast(pObject)
		if pShip:
			pShields = pShip.GetShields()
			if pShields:
				pShields.TurnOn()
		pObject.CallNextHandler(pEvent)
except:
	print "Something went wrong wih Dicohesive Tech Shields technology"
	traceback.print_exc()
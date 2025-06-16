#################################################################################################################
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
#         B5Defences.py by Alex SL Gato
#         Version 1.10
#         16th June 2025
#         Based strongly on Shields.py by the FoundationTechnologies team, and ATPFunctions by Apollo.
#         From version 1.10 onwards, also has a dependency with USS Sovereign's DS9FX "Handle Shields" functions, which must be installed separately as a pre-requisite - used for the 'no bleedthrough Shields' tech, eminently used for those vessels whose "no dmg through shields" option from DS9FX should remain active the most to be better canon-compliant
#################################################################################################################

from bcdebug import debug

import App
import FoundationTech

# This should be the prime example of a special yield weapon defined
# according to Foundation Technologies.  The code is mostly based upon
# QuickBattleAddon.corboniteReflector() in Apollo's Advanced Technologies.


from ftb.Tech.ATPFunctions import *

ds9fxThere = 0
try:
	from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig
	from Custom.DS9FX.DS9FXLifeSupport import HandleShields
	ds9fxThere = 1
except:
	ds9fxThere = 0

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
            "Version": "1.10",
            "License": "LGPL",
            "Description": "Read the small title above for more info"
            }

torpsNetTypeThatCanPhase = None
try:
	import Multiplayer.SpeciesToTorp
	torpsNetTypeThatCanPhase = Multiplayer.SpeciesToTorp.PHASEDPLASMA # For the "torpedoes-going-through" issue
except:
	torpsNetTypeThatCanPhase = None
	print("Attention, you are missing Multiplayer.SpeciesToTorp, or your version lacks the stock PHASEDPLASMA type")

NonSerializedObjects = (
"oGridDefense",
"oCentauriGravimetric",
"oShadowEffect",
"oVorlonShields",
"oThirdspaceShields",
)

class GridDef(FoundationTech.TechDef):

	def OnPulseDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnPulseDefense")
		if pEvent.IsHullHit():
			return

		if oYield:
		 	if oYield.IsPhaseYield() or oYield.IsDrainYield():
		 		return

		if App.g_kSystemWrapper.GetRandomNumber(100) > 75.0 or (pInstance.__dict__[self.name] < pEvent.GetDamage()):
			return
		if pTorp and hasattr(pTorp, "SetLifetime"):
			pTorp.SetLifetime(0.0)
		fDamage = pEvent.GetDamage() #The power to reflect the weapon causes damage, 10% of the original damage
		ShieldDistributePos(pShip,fDamage)

		return 1	# Meaning no more defense functions are necessary.


	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnTorpDefense")
		if pEvent.IsHullHit():
			return

		if oYield:
		 	if oYield.IsPhaseYield() or oYield.IsDrainYield():
		 		return

		if App.g_kSystemWrapper.GetRandomNumber(100) > 50.0 or (pInstance.__dict__[self.name] < pEvent.GetDamage()):
			return

		#GridReflector(pShip, pInstance, pTorp, oYield, pEvent)
		if pTorp and hasattr(pTorp, "SetLifetime"):
			pTorp.SetLifetime(0.0)
		fDamage = pEvent.GetDamage() #The power to reflect the weapon causes damage, 10% of the original damage
		ShieldDistributePos(pShip,fDamage)

		return 1	# Meaning no more defense functions are necessary. 


	# TODO:  Make this an activated technology
	def Attach(self, pInstance):
		debug(__name__ + ", Attach")
		pInstance.lTechs.append(self)
		pInstance.lTorpDefense.insert(0, self)		# Important to put shield-type weapons in the front
		pInstance.lPulseDefense.insert(0, self)
		#print 'Attaching Defense Grid to', pInstance, pInstance.__dict__

	# def Activate(self):
	# 	FoundationTech.oWeaponHit.Start()
	# def Deactivate(self):
	# 	FoundationTech.oWeaponHit.Stop()
    
oGridDefense = GridDef('Defense Grid')

class CentauriDef(FoundationTech.TechDef):

	def OnPulseDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnPulseDefense")
		if pEvent.IsHullHit():
			return

		if oYield:
		 	if oYield.IsPhaseYield() or oYield.IsDrainYield():
		 		return

		if App.g_kSystemWrapper.GetRandomNumber(100) > 55.0 or (pInstance.__dict__[self.name] < pEvent.GetDamage()):
			return
		GridReflector(pShip, pInstance, pTorp, oYield, pEvent)

		return 1	# Meaning no more defense functions are necessary.


	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnTorpDefense")
		if pEvent.IsHullHit():
			return

		if oYield:
		 	if oYield.IsPhaseYield() or oYield.IsDrainYield():
		 		return

		if App.g_kSystemWrapper.GetRandomNumber(100) > 85.0 or (pInstance.__dict__[self.name] < pEvent.GetDamage()):
			return

		DirectReflector2(pShip, pInstance, pTorp, oYield, pEvent)

		return 1	# Meaning no more defense functions are necessary. 


	# TODO:  Make this an activated technology
	def Attach(self, pInstance):
		debug(__name__ + ", Attach")
		pInstance.lTechs.append(self)
		pInstance.lTorpDefense.insert(0, self)		# Important to put shield-type weapons in the front
		pInstance.lPulseDefense.insert(0, self)
		#print 'Attaching Defense Grid to', pInstance, pInstance.__dict__

	# def Activate(self):
	# 	FoundationTech.oWeaponHit.Start()
	# def Deactivate(self):
	# 	FoundationTech.oWeaponHit.Stop()
    
oCentauriGravimetric = CentauriDef('Gravimetric Defense')

class BabFiveShadowDef(FoundationTech.TechDef):

	def OnDefense(self, pShip, pInstance, oYield, pEvent):
		debug(__name__ + ", OnDefense")
		if (pShip != None):
			pShip.SetImpulse(0, pShip.GetWorldForwardTG(), App.PhysicsObjectClass.DIRECTION_WORLD_SPACE)

		if pEvent.IsHullHit():
			return

		if (pShip != None): # yes, repetition is intentional
			pShip.SetImpulse(0, pShip.GetWorldForwardTG(), App.PhysicsObjectClass.DIRECTION_WORLD_SPACE)

		if oYield:
		 	if oYield.IsPhaseYield() or oYield.IsDrainYield():
		 		return

		if (pShip != None):
			pShip.SetImpulse(0, pShip.GetWorldForwardTG(), App.PhysicsObjectClass.DIRECTION_WORLD_SPACE)

		pShields = pShip.GetShields()

		if pShields:
			# Thanks, MLeoDaalder, for the tip!  -Dasher42
			pShields.RedistributeShields()
			
		# if pShields:
		# 	pShieldTotal = 0.0
		# 	for shieldDir in range(App.ShieldClass.NUM_SHIELDS):			#Calculate the total shieldpower
		# 		pShieldTotal = pShieldTotal+pShields.GetCurShields(shieldDir)
		# 	for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
		# 		pShields.SetCurShields(shieldDir,pShieldTotal/6.0)  		#Redistribute shields equally


	def OnBeamDefense(self, pShip, pInstance, oYield, pEvent):
		debug(__name__ + ", OnBeamDefense")
		if (pShip != None):
			pShip.SetImpulse(0, pShip.GetWorldForwardTG(), App.PhysicsObjectClass.DIRECTION_WORLD_SPACE)
		if App.g_kSystemWrapper.GetRandomNumber(100) <= pInstance.__dict__[self.name]:
			return self.OnDefense(pShip, pInstance, oYield, pEvent)

	# TODO:  Make this an activated technology
	def Attach(self, pInstance):
		debug(__name__ + ", Attach")
		pInstance.lTechs.append(self)
		pInstance.lBeamDefense.insert(0, self)		# Important to put shield-type weapons in the front
		# print 'Attaching Shadow Dispersive Hull to', pInstance, pInstance.__dict__

	# def Activate(self):
	# 	FoundationTech.oWeaponHit.Start()
	# def Deactivate(self):
	# 	FoundationTech.oWeaponHit.Stop()

oShadowEffect = BabFiveShadowDef('Shadow Dispersive Hull')

class BabFiveVreeDef(FoundationTech.TechDef):

	def OnDefense(self, pShip, pInstance, oYield, pEvent):
		debug(__name__ + ", OnDefense")
		if oYield:
		 	if oYield.IsPhaseYield() or oYield.IsDrainYield():
		 		return

		if pEvent.IsHullHit():
			return

		pShields = pShip.GetShields()

		if pShields:
			# Thanks, MLeoDaalder, for the tip!  -Dasher42
			# ShieldDistributeNeg(pShip, pEvent.GetDamage())
			pShieldTotal = 0.0
			# pShieldTotal = -pEvent.GetDamage()
			for shieldDir in range(App.ShieldClass.NUM_SHIELDS):			#Calculate the total shieldpower
				pShieldTotal = pShieldTotal+pShields.GetCurShields(shieldDir)
			for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
				pShields.SetCurShields(shieldDir,pShieldTotal/6.0)  		#Redistribute shields equally


	def OnBeamDefense(self, pShip, pInstance, oYield, pEvent):
		debug(__name__ + ", OnBeamDefense")
		if App.g_kSystemWrapper.GetRandomNumber(100) <= pInstance.__dict__['Vree Shields']:
			return self.OnDefense(pShip, pInstance, oYield, pEvent)

	def OnPulseDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnPulseDefense")
		if App.g_kSystemWrapper.GetRandomNumber(100) <= pInstance.__dict__['Vree Shields']:
			return self.OnDefense(pShip, pInstance, oYield, pEvent)

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnTorpDefense")
		if App.g_kSystemWrapper.GetRandomNumber(100) <= pInstance.__dict__['Vree Shields']:
			return self.OnDefense(pShip, pInstance, oYield, pEvent)


	# TODO:  Make this an activated technology
	def Attach(self, pInstance):
		debug(__name__ + ", Attach")
		pInstance.lTechs.append(self)
		pInstance.lTorpDefense.insert(0, self)		# Important to put shield-type weapons in the front
		pInstance.lPulseDefense.insert(0, self)
		pInstance.lBeamDefense.insert(0, self)
		# print 'Attaching Vree Shields to', pInstance, pInstance.__dict__

	# def Activate(self):
	# 	FoundationTech.oWeaponHit.Start()
	# def Deactivate(self):
	# 	FoundationTech.oWeaponHit.Stop()

oVorlonShields = BabFiveVreeDef('Vree Shields')

class ForceNoDmgThoughShieldsDef(FoundationTech.TechDef):

	def OnDefense(self, pShip, pInstance, oYield, pEvent, pTorp=None):
		debug(__name__ + ", OnDefense")
		if pEvent.IsHullHit() and not oYield and not ((hasattr(oYield, "IsPhaseYield") and oYield.IsPhaseYield()) or (hasattr(oYield, "IsDrainYield") and oYield.IsDrainYield()) or (hasattr(oYield, "IsTransphasicYield") and oYield.IsTransphasicYield())) and pShip:
			pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
			if pShip and (not pTorp or not (torpsNetTypeThatCanPhase != None and pTorp.GetNetType() == torpsNetTypeThatCanPhase)):
					whatIsNeeded = self.CheckDS9FXNoDmgActive()
					if whatIsNeeded == 0:
						HandleShields.WeaponHit(pShip, pEvent)

	def OnBeamDefense(self, pShip, pInstance, oYield, pEvent):
		debug(__name__ + ", OnBeamDefense")
		if App.g_kSystemWrapper.GetRandomNumber(100) <= pInstance.__dict__['No bleedthrough Shields']:
			return self.OnDefense(pShip, pInstance, oYield, pEvent, None)

	def OnPulseDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnPulseDefense")
		if App.g_kSystemWrapper.GetRandomNumber(100) <= pInstance.__dict__['No bleedthrough Shields']:
			return self.OnDefense(pShip, pInstance, oYield, pEvent, pTorp)

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnTorpDefense")
		if App.g_kSystemWrapper.GetRandomNumber(100) <= pInstance.__dict__['No bleedthrough Shields']:
			return self.OnDefense(pShip, pInstance, oYield, pEvent, pTorp)


	# TODO:  Make this an activated technology
	def Attach(self, pInstance):
		debug(__name__ + ", Attach")
		if pInstance != None:
			pInstance.lTechs.append(self)
			pInstance.lTorpDefense.insert(0, self)		# Important to put shield-type weapons in the front
			pInstance.lPulseDefense.insert(0, self)
			pInstance.lBeamDefense.insert(0, self)

			whatIsNeeded = self.CheckDS9FXNoDmgActive()
			if whatIsNeeded == 0:
				pObjectID = pInstance.pShipID
				if pObjectID != None and pObjectID != App.NULL_ID:
					pObject = App.ShipClass_GetObjectByID(None, pObjectID)
					if pObject != None:
						pEvent = App.TGEvent_Create()
						pEvent.SetDestination(pObject)
						HandleShields.ShipCreated(pObject, pEvent)

		# print 'Attaching no bleedthrough shields to', pInstance, pInstance.__dict__

	def CheckDS9FXNoDmgActive(self):
		ds9checks = 0
		try:
			if ds9fxThere == 1:
				reload (DS9FXSavedConfig)

				if DS9FXSavedConfig.NoDamageThroughShields == 1:
					ds9checks = 1
			else:
				ds9checks = 2
		except:
			print "Error while trying to import DS9FXSavedConfig"
			ds9checks = 2
			traceback.print_exc()

		return ds9checks
		
	# def Activate(self):
	# 	FoundationTech.oWeaponHit.Start()
	# def Deactivate(self):
	# 	FoundationTech.oWeaponHit.Stop()

oThirdspaceShields = ForceNoDmgThoughShieldsDef('No bleedthrough Shields')


# print 'B5 Defences loaded'

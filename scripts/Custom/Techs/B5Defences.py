#################################################################################################################
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
#         B5Defences.py by Alex SL Gato
#         Version 1.01
#         17th April 2024
#         Based strongly on Shields.py by the FoundationTechnologies team, and ATPFunctions by Apollo.
#################################################################################################################

from bcdebug import debug

import App
import FoundationTech

# This should be the prime example of a special yield weapon defined
# according to Foundation Technologies.  The code is mostly based upon
# QuickBattleAddon.corboniteReflector() in Apollo's Advanced Technologies.


from ftb.Tech.ATPFunctions import *

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
            "Version": "1.01",
            "License": "LGPL",
            "Description": "Read the small title above for more info"
            }

NonSerializedObjects = (
"oGridDefense",
"oCentauriGravimetric",
"oShadowEffect",
"oVorlonShields",
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

                if (pShip != None):
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
			
		# if pShields:
		# 	pShieldTotal = 0.0
		# 	for shieldDir in range(App.ShieldClass.NUM_SHIELDS):			#Calculate the total shieldpower
		# 		pShieldTotal = pShieldTotal+pShields.GetCurShields(shieldDir)
		# 	for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
		# 		pShields.SetCurShields(shieldDir,pShieldTotal/6.0)  		#Redistribute shields equally


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
		# print 'Attaching Multivectral to', pInstance, pInstance.__dict__

	# def Activate(self):
	# 	FoundationTech.oWeaponHit.Start()
	# def Deactivate(self):
	# 	FoundationTech.oWeaponHit.Stop()

oVorlonShields = BabFiveVreeDef('Vree Shields')
# print 'Multivectral Shields loaded'

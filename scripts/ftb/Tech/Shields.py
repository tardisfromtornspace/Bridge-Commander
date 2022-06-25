from bcdebug import debug

import App
import FoundationTech

# This should be the prime example of a special yield weapon defined
# according to Foundation Technologies.  The code is mostly based upon
# QuickBattleAddon.corboniteReflector() in Apollo's Advanced Technologies.


from ATPFunctions import *

NonSerializedObjects = (
"oMultivect",
"oRegenerative",
"oReflector",
"oReflector2",
"oGridDefense",
"oCentauriGravimetric",
"oShadowEffect",
"oVorlonShields",
)

class MultivectDef(FoundationTech.TechDef):

	def OnDefense(self, pShip, pInstance, oYield, pEvent):
		debug(__name__ + ", OnDefense")
		if pEvent.IsHullHit():
			return

		if oYield:
		 	if oYield.IsPhaseYield() or oYield.IsDrainYield():
		 		return

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
		if App.g_kSystemWrapper.GetRandomNumber(100) <= pInstance.__dict__['Multivectral Shields']:
			return self.OnDefense(pShip, pInstance, oYield, pEvent)

	def OnPulseDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnPulseDefense")
		if App.g_kSystemWrapper.GetRandomNumber(100) <= pInstance.__dict__['Multivectral Shields']:
			return self.OnDefense(pShip, pInstance, oYield, pEvent)

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnTorpDefense")
		if App.g_kSystemWrapper.GetRandomNumber(100) <= pInstance.__dict__['Multivectral Shields']:
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

oMultivect = MultivectDef('Multivectral Shields')


class RegenerativeDef(MultivectDef):
	def OnDefense(self, pShip, pInstance, oYield, pEvent):
		debug(__name__ + ", OnDefense")
		if pEvent.IsHullHit():
			return

		if oYield:
		 	if oYield.IsPhaseYield() or oYield.IsDrainYield():
		 		return

		fDamage = pEvent.GetDamage() / pInstance.__dict__['Regenerative Shields']

		# print 'Regenerate', fDamage

		pShields = pShip.GetShields()
		if pShields:
			for shieldDir in range(App.ShieldClass.NUM_SHIELDS):			#Calculate the total shieldpower
				fCurr = pShields.GetCurShields(shieldDir)
				fMax = pShields.GetMaxShields(shieldDir)
				fCurr = fCurr + fDamage
				if fCurr > fMax:
					fCurr = fMax
				pShields.SetCurShields(shieldDir, fCurr)

	def OnBeamDefense(self, pShip, pInstance, oYield, pEvent):
		debug(__name__ + ", OnBeamDefense")
		return self.OnDefense(pShip, pInstance, oYield, pEvent)

	def OnPulseDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnPulseDefense")
		return self.OnDefense(pShip, pInstance, oYield, pEvent)

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnTorpDefense")
		return self.OnDefense(pShip, pInstance, oYield, pEvent)


oRegenerative = RegenerativeDef('Regenerative Shields')


class ReflectorDef(FoundationTech.TechDef):

	def OnPulseDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnPulseDefense")
		if pEvent.IsHullHit():
			return

		if oYield:
		 	if oYield.IsPhaseYield() or oYield.IsDrainYield():
		 		return

		if App.g_kSystemWrapper.GetRandomNumber(100) > pInstance.__dict__[self.name]:
			return

		RandomReflector(pShip, pInstance, pTorp, oYield, pEvent)

		return 1	# Meaning no more defense functions are necessary.


	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnTorpDefense")
		if pEvent.IsHullHit():
			return

		if oYield:
		 	if oYield.IsPhaseYield() or oYield.IsDrainYield():
		 		return

		if App.g_kSystemWrapper.GetRandomNumber(100) > pInstance.__dict__[self.name]:
			return

	# if iAff >= 5:
	# 	if not HasSufficientSpecialPower(pShip,80.0):
	# 		return
	# else:
	# 	if not pShip.GetObjID() == MissionLib.GetPlayer().GetObjID():
	# 		if HasSufficientSpecialPower(pShip,400.0):
	# 			SetCorboniteOn(pShip)
	# 		else:
	# 			return
	# 	else:
	# 		return

		DirectReflector(pShip, pInstance, pTorp, oYield, pEvent)

		return 1	# Meaning no more defense functions are necessary.


	# TODO:  Make this an activated technology
	def Attach(self, pInstance):
		debug(__name__ + ", Attach")
		pInstance.lTechs.append(self)
		pInstance.lTorpDefense.insert(0, self)		# Important to put shield-type weapons in the front
		pInstance.lPulseDefense.insert(0, self)
		#print 'Attaching Reflector to', pInstance, pInstance.__dict__

	# def Activate(self):
	# 	FoundationTech.oWeaponHit.Start()
	# def Deactivate(self):
	# 	FoundationTech.oWeaponHit.Stop()


oReflector = ReflectorDef('Reflector')
oReflector2= ReflectorDef('Reflector Shields') # Request by DarkThunder, it does help the consistancy in name calling


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
		GridReflector(pShip, pInstance, pTorp, oYield, pEvent)

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

		GridReflector(pShip, pInstance, pTorp, oYield, pEvent)

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

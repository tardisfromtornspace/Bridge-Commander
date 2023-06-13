from bcdebug import debug

import App
import FoundationTech

# This should be the prime example of a special yield weapon defined
# according to Foundation Technologies.  The code is mostly based upon
# QuickBattleAddon.corboniteReflector() in Apollo's Advanced Technologies.

class AlteranZPMDef(FoundationTech.TechDef):
	def OnDefense(self, pShip, pInstance, oYield, pEvent):
		debug(__name__ + ", OnDefense")

		if oYield:
		 	if oYield.IsPhaseYield() or oYield.IsDrainYield():
		 		return

		fDamage = pEvent.GetDamage()
		ZPM_ratio = 1.0
		try:
			pInstance.__dict__['Alteran ZPM Shields']
		except:
			ZPM_ratio = 1.0
		# print 'Regenerate', fDamage

		pShields = pShip.GetShields()
		if pShields:
			if pEvent.IsHullHit():
				pShip.SetInvincible(0)
				return
			pPower=pShip.GetPowerSubsystem()
			if (pPower==None):
				pShip.SetInvincible(0)
				return
			pHull=pShip.GetHull()
			if (pHull==None):
				pShip.SetInvincible(0)
				return

			batt_chg=pPower.GetMainBatteryPower()
			batt_limit=pPower.GetMainBatteryLimit()
			if (batt_chg<=(batt_limit*.03)):
				pShip.SetInvincible(0)
				return
			else:
				pShip.SetInvincible(1)

			ZPM_shield_pwr=batt_chg*ZPM_ratio
			 
			if (ZPM_shield_pwr>=fDamage):
				ZPM_shield_pwr=ZPM_shield_pwr-fDamage
				for shieldDir in range(App.ShieldClass.NUM_SHIELDS):			#Calculate the total shieldpower
					fCurr = pShields.GetCurShields(shieldDir)
					fMax = pShields.GetMaxShields(shieldDir)
					fCurr = fCurr + fDamage
					if fCurr > fMax:
						fCurr = fMax
					elif fCurr < 0.75 * fMax:
						fCurr = 0.75 * fMax
					
					pShields.SetCurShields(shieldDir, fCurr)
			else:
				pShip.SetInvincible(0)
				ZPM_shield_pwr=0				

			pPower.SetMainBatteryPower(ZPM_shield_pwr/ZPM_ratio)
			return
		else:
			pShip.SetInvincible(0)

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
		pInstance.lTechs.append(self)
		pInstance.lTorpDefense.insert(0, self)		# Important to put shield-type weapons in the front
		pInstance.lPulseDefense.insert(0, self)
		pInstance.lBeamDefense.insert(0, self)
		# print 'Attaching Multivectral to', pInstance, pInstance.__dict__

	# def Activate(self):
	# 	FoundationTech.oWeaponHit.Start()
	# def Deactivate(self):
	# 	FoundationTech.oWeaponHit.Stop()


oAlteranZPM = AlteranZPMDef('Alteran ZPM Shields')

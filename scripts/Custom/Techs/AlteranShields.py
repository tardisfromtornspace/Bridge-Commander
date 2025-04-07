# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL

# This should be the prime example of a special yield weapon/shield defined
# according to Foundation Technologies.  The code is mostly based upon
# QuickBattleAddon.corboniteReflector() in Apollo's Advanced Technologies.
#
#############################################
# Usage Example:  Add this to the dTechs attribute of your ShipDef, in the Ship plugin file
# but modify the values accordingly
# Strength: it is a key value that help on reducing the damage done by acting as a multiplier, so i.e. a value of 2 will make the game consider you have twice the energy levels.  Values equal or lesser than 0 will be ignored.
"""
Foundation.ShipDef.Atlantis.dTechs = {
	'Alteran ZPM Shields': { "Strength": 1 }
}
"""
#################################################################################################################
#
MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "1.01",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }
#
#################################################################################################################
#
from bcdebug import debug

import App
import FoundationTech

try:
	class AlteranZPMDef(FoundationTech.TechDef):

		ZPMpowered = 1
		def OnDefense(self, pShip, pInstance, oYield, pEvent):
			debug(__name__ + ", OnDefense")

			fDamage = pEvent.GetDamage()
			ZPM_ratio = 1.0
			try:
				if pInstance and pInstance.__dict__.has_key('Alteran ZPM Shields') and pInstance.__dict__['Alteran ZPM Shields'].has_key('Strength') and pInstance.__dict__['Alteran ZPM Shields']['Strength'] > 0:
					ZPM_ratio = pInstance.__dict__['Alteran ZPM Shields']['Strength']
			except:
				ZPM_ratio = 1.0
			# print 'Regenerate', fDamage

			pShields = pShip.GetShields()
	
			if pShields and not pShields.IsDisabled() and pShields.IsOn() and pShields.GetPowerPercentageWanted() > 0.0:
				pHull=pShip.GetHull()
				if (pHull==None):
					pShip.SetInvincible(0)
					return

				#if pEvent.IsHullHit():
				#	pShip.SetInvincible(0)
					#self.AlteranHullProtectionRegis(pShip, pInstance, oYield, pEvent, pHull, fDamage, 0 == 1)

				pPower=pShip.GetPowerSubsystem()
				if (pPower==None):
					pShip.SetInvincible(0)
					self.AlteranHullProtectionRegis(pShip, pInstance, oYield, pEvent, pHull, fDamage, 0 == 1)
					return

				batt_chg=pPower.GetMainBatteryPower()
				batt_limit=pPower.GetMainBatteryLimit()
				if (batt_chg<=(batt_limit*.06)):
					pShip.SetInvincible(0)
					if (self.ZPMpowered == 1):
						ZPM_shield_pwr=0
						self.ZPMpowered = 0
						pPower.SetMainBatteryPower(ZPM_shield_pwr/ZPM_ratio)
					self.AlteranHullProtectionRegis(pShip, pInstance, oYield, pEvent, pHull, fDamage, 0 == 1)
					return
				else:
					self.ZPMpowered = 1
					if not pEvent.IsHullHit():
						pShip.SetInvincible(1)
					else:
						pShip.SetInvincible(0)

				ZPM_shield_pwr=batt_chg*ZPM_ratio
			 
				if (ZPM_shield_pwr>=fDamage):
					ZPM_shield_pwr=ZPM_shield_pwr-fDamage
					for shieldDir in range(App.ShieldClass.NUM_SHIELDS):			#Calculate the total shieldpower
						fCurr = pShields.GetCurShields(shieldDir)
						fMax = pShields.GetMaxShields(shieldDir)
						#fCurr = fMax
						fCurr = fCurr + fDamage
						if fCurr > fMax:
							fCurr = fMax
						elif fCurr < 0.75 * fMax:
							fCurr = 0.75 * fMax
					
						pShields.SetCurShields(shieldDir, fCurr)

					shieldHull = ( not oYield or not ((hasattr(oYield, "IsPhaseYield") and oYield.IsPhaseYield()) or (hasattr(oYield, "IsTransphasicYield") and oYield.IsTransphasicYield()) or (hasattr(oYield, "IsChronTorpYield") and oYield.IsChronTorpYield())) )
					self.AlteranHullProtectionRegis(pShip, pInstance, oYield, pEvent, pHull, fDamage, shieldHull)
					
				else:
					pShip.SetInvincible(0)
					ZPM_shield_pwr=0
					self.ZPMpowered = 0
					self.AlteranHullProtectionRegis(pShip, pInstance, oYield, pEvent, pHull, fDamage, 0 == 1)				

				pPower.SetMainBatteryPower(ZPM_shield_pwr/ZPM_ratio)

				return

			else:
				pShip.SetInvincible(0)
				pHull=pShip.GetHull()
				if (pHull==None):
					return
				self.AlteranHullProtectionRegis(pShip, pInstance, oYield, pEvent, pHull, fDamage, 0 == 1)
	
		def AlteranHullProtectionRegis(self, pShip, pInstance, oYield, pEvent, pHull, fDamage, activeFlag):

			if not pInstance.__dict__['Alteran ZPM Shields'].has_key("Ships"):
				pInstance.__dict__['Alteran ZPM Shields']["Ships"] = {}

			if not pInstance.__dict__['Alteran ZPM Shields']["Ships"].has_key(pShip.GetObjID()):
				pInstance.__dict__['Alteran ZPM Shields']["Ships"][pShip.GetObjID()] = {}

			dOldConditions = pInstance.__dict__['Alteran ZPM Shields']["Ships"][pShip.GetObjID()]
			#dOldConditions[pHull.GetName()] = pHull.GetConditionPercentage()

			if not dOldConditions.has_key(pHull.GetName()):
				dOldConditions[pHull.GetName()] = 1.0
				#dOldConditions[pHull.GetName()] = pHull.GetConditionPercentage()

			fOldCondition = dOldConditions[pHull.GetName()]

			if activeFlag:
				# Ensures the hull is not damaged
				myHullPercentage = pHull.GetConditionPercentage()	
				if myHullPercentage <= fOldCondition:
					fNewCondition = fOldCondition
				else:
					fNewCondition = myHullPercentage

				pHull.SetConditionPercentage(fNewCondition)
			else:
				#fDiff = 1 - fOldCondition + fDamage / pHull.GetMaxCondition()
				#fNewCondition = fOldCondition - fDiff
				fNewCondition = pHull.GetConditionPercentage()

			#pHull.SetConditionPercentage(fNewCondition)
			dOldConditions[pHull.GetName()] = fNewCondition
		

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
			# print 'Attaching Alteran ZPM Shields to', pInstance, pInstance.__dict__

		# def Activate(self):
		# 	FoundationTech.oWeaponHit.Start()
		# def Deactivate(self):
		# 	FoundationTech.oWeaponHit.Stop()


	oAlteranZPM = AlteranZPMDef('Alteran ZPM Shields')
except:
	print "FoundationTech, or the FTB mod, or both are not installed, \nAlteran Shields are there but NOT enabled in your current BC installation"

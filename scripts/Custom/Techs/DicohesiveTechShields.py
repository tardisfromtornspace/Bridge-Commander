from bcdebug import debug

import App
import FoundationTech

# This should be the prime example of a special yield weapon defined
# according to Foundation Technologies.  The code is mostly based upon
# QuickBattleAddon.corboniteReflector() in Apollo's Advanced Technologies.

class DicohesiveTechVoidDef(FoundationTech.TechDef):

	def OnDefense(self, pShip, pInstance, oYield, pEvent):
		debug(__name__ + ", OnDefense")
		if pEvent.IsHullHit():
			pShip.SetInvincible(0)
			pShip.SetVisibleDamageRadiusModifier(1.0)
			pShip.SetVisibleDamageStrengthModifier(1.0)
		else:
			pShip.SetInvincible(1)
			pHull=pShip.GetHull()
			hull_max=pHull.GetMaxCondition()
			pHull.SetCondition(hull_max)
			pShip.SetVisibleDamageRadiusModifier(0.0)
			pShip.SetVisibleDamageStrengthModifier(0.0)


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
		# print 'Attaching Dicohesive Shields to', pInstance, pInstance.__dict__

	# def Activate(self):
	# 	FoundationTech.oWeaponHit.Start()
	# def Deactivate(self):
	# 	FoundationTech.oWeaponHit.Stop()

oDicohesiveTechVoid = DicohesiveTechVoidDef('Dicohesive Tech Shields')
from bcdebug import debug
import App

import FoundationTech
import MissionLib

# This should be the prime example of a special yield weapon defined
# according to Foundation Technologies.  The code is mostly based upon
# QuickBattleAddon.drainerWeapon() in Apollo's Advanced Technologies.

from DisablerYields import *

NonSerializedObjects = (
"oDrainerWeapon",
"oDrainerImmune",
)

# from ATP by Defiant
def IonSubSystem(pSubSystem):
	#print "Ionizing Subsystem: ",pSubSystem.GetName()
	debug(__name__ + ", IonSubSystem")
	if not pSubSystem:
		return

	ID=pSubSystem.GetObjID()
	pSubSystemProp=pSubSystem.GetProperty()
        pSubSystem.SetCondition(0.999*pSubSystem.GetCondition())
        fDisabledAt=pSubSystemProp.GetDisabledPercentage()
        fRepairComplex=pSubSystemProp.GetRepairComplexity()
        pSubSystemProp.SetDisabledPercentage(1.0)
        pSubSystemProp.SetRepairComplexity(10000000)


class BreenDrainerWeaponDef(MultipleDisableDef):

	def IsDrainYield(self):
		debug(__name__ + ", IsDrainYield")
		return 1

	def OnYield(self, pShip, pInstance, pEvent, pTorp):
		debug(__name__ + ", OnYield")
		if FoundationTech.EffectsLib:
			FoundationTech.EffectsLib.CreateSpecialFXSeq(pShip, pEvent, 'Damper')

		pShipID = pShip.GetObjID()

		pPower = pShip.GetPowerSubsystem()
		if pPower:
                        IonSubSystem(pPower)
	                pProp = pPower.GetProperty()
	                pProp.SetPowerOutput(0.0)
                        pProp.SetMainConduitCapacity(0.000001)
                        pProp.SetBackupConduitCapacity(0.000001)

		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))
		if not pShip:
			return

		pShields = pShip.GetShields()
		if pShields:
                        IonSubSystem(pShields)

		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))
		if not pShip:
			return

		pCloak = pShip.GetCloakingSubsystem()
		if pCloak:
                        IonSubSystem(pCloak)

		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))
		if not pShip:
			return

		pPlayer = MissionLib.GetPlayer()
		if pPlayer.GetObjID() == pShip.GetObjID():
			pSound = App.g_kSoundManager.GetSound("PowerDisabled")
			if pSound:
			        pSound.Play()

			if FoundationTech.BridgeFX:
				FoundationTech.BridgeFX.CreateDrainEffect()


class _BreenDrainerWeaponDef(MultipleDisableDef):

	def IsDrainYield(self):
		debug(__name__ + ", IsDrainYield")
		return 1

	def OnYield(self, pShip, pInstance, pEvent, pTorp):
		debug(__name__ + ", OnYield")
		if FoundationTech.EffectsLib:
			FoundationTech.EffectsLib.CreateSpecialFXSeq(pShip, pEvent, 'Damper')

		pPlayer = MissionLib.GetPlayer()
		if pPlayer.GetObjID() == pShip.GetObjID():
			pSound = App.g_kSoundManager.GetSound("PowerDisabled")
			if pSound:
				pSound.Play()

			if FoundationTech.BridgeFX:
				FoundationTech.BridgeFX.CreateDrainEffect()

		pPower = pShip.GetPowerSubsystem()
		if pPower:
			pInstance.AdjustMainBattery(pShip, pPower, 0.0)
			pInstance.AdjustBackupBattery(pShip, pPower, 0.0)

		MultipleDisableDef.OnYield(self, pShip, pInstance, pEvent, pTorp)

oDrainerWeapon = BreenDrainerWeaponDef('Damper Weapon', {})


class DrainerImmuneDef(FoundationTech.TechDef):

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnTorpDefense")
		if oYield and oYield.IsDrainYield():
			return 1

	def Attach(self, pInstance):
		debug(__name__ + ", Attach")
		pInstance.lTorpDefense.append(self)


oDrainerImmune = DrainerImmuneDef('Drainer Immune')


# print 'Damper Weapon loaded'

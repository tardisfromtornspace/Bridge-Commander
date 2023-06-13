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


# from ATP
def IonSubSystem(pSubSystem):
	#print "Ionizing Subsystem: ",pSubSystem.GetName()
	debug(__name__ + ", IonSubSystem")
	if not pSubSystem:
		return

	pSubSystemProp=pSubSystem.GetProperty()
        
        if pSubSystem.GetCondition() > 0.1:
                pSubSystem.SetCondition(0.001)
        if not App.g_kUtopiaModule.IsMultiplayer():
                pSubSystemProp.SetRepairComplexity(10000000)
        #pSubSystem.SetCondition(0.999*pSubSystem.GetCondition())
        #fDisabledAt=pSubSystemProp.GetDisabledPercentage()
        #fRepairComplex=pSubSystemProp.GetRepairComplexity()
        #pSubSystemProp.SetDisabledPercentage(1.0)
        #pSubSystemProp.SetRepairComplexity(10000000)


class BreenDrainerWeaponDef(MultipleDisableDef):

	def IsDrainYield(self):
		debug(__name__ + ", IsDrainYield")
		return 1

	def OnYield(self, pShip, pInstance, pEvent, pTorp):
		debug(__name__ + ", OnYield")
		if FoundationTech.EffectsLib:
			FoundationTech.EffectsLib.CreateSpecialFXSeq(pShip, pEvent, 'Damper')

		pShipID = pShip.GetObjID()
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))
		
		# useless against stations
		if not pShip or pShip.GetShipProperty().IsStationary():
			return

		pPlayer = MissionLib.GetPlayer()
		if pPlayer.GetObjID() == pShip.GetObjID():
			pVoice = App.g_kSoundManager.GetSound("PowerDisabled")
			if pVoice:
			        pVoice.Play()

                        pSound = App.g_kSoundManager.GetSound("BreenDraining")
                        if not pSound:
                                pSound = App.TGSound_Create("sfx/BreenDraining.wav", "BreenDraining", 0)
                        if pSound:
                                pSound.Play()

			if FoundationTech.BridgeFX:
				FoundationTech.BridgeFX.CreateDrainEffect()
                        
                        # disable glow on ship
			if not pShip.IsDead(): # possible crash work around
                        	pShip.DisableGlowAlphaMaps()

                # clients shouldn't do anything here
                if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
                        return

		pPower = pShip.GetPowerSubsystem()
		if pPower:
                        IonSubSystem(pPower)
	                #pProp = pPower.GetProperty()
	                #pProp.SetPowerOutput(0.0)
                        #pProp.SetMainConduitCapacity(0.000001)
                        #pProp.SetBackupConduitCapacity(0.000001)

		pShields = pShip.GetShields()
		if pShields:
                        IonSubSystem(pShields)

		pCloak = pShip.GetCloakingSubsystem()
		if pCloak:
                        IonSubSystem(pCloak)

                pImpulse = pShip.GetImpulseEngineSubsystem()
                if pImpulse:
                        IonSubSystem(pImpulse)

                pWarp = pShip.GetWarpEngineSubsystem()
                if pWarp:
                        IonSubSystem(pWarp)

	        pWeaponSys = pShip.GetTorpedoSystem()
	        if pWeaponSys:
		        IonSubSystem(pWeaponSys)
	        pWeaponSys = pShip.GetPhaserSystem()
	        if pWeaponSys:
		        IonSubSystem(pWeaponSys)
	        pWeaponSys = pShip.GetPulseWeaponSystem()
	        if pWeaponSys:
		        IonSubSystem(pWeaponSys)


oDrainerWeapon = BreenDrainerWeaponDef('Breen Drainer Weapon', {})


class DrainerImmuneDef(FoundationTech.TechDef):

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnTorpDefense")
		if oYield and hasattr(oYield, "IsDrainYield") and oYield.IsDrainYield():
			return 1

	def Attach(self, pInstance):
		debug(__name__ + ", Attach")
		pInstance.lTorpDefense.append(self)


oDrainerImmune = DrainerImmuneDef('Breen Drainer Immune')


# print 'Damper Weapon loaded'

#################################################################################################################
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
#         UpgradedBreenDrainer by Alex SL Gato
#         Version 1.0
#         28 June 2023
#         Based on FiveSecsGodPhaser by USS Frontier, scripts/ftb/Tech/BreenDrainer by the FoundationTechnologies team, scripts/ftb/Tech/DisablerYields by the FoundationTechnologies team, and some advice from the BreenDrain by Dasher42
#                          
#################################################################################################################
# TODO: 1. Create Read Me
#	2. Create a clear guide on how to add this...
#
# Start on 2:
# At the bottom of your torpedo projectile file add this (Between the """ and """):
"""
try:
	sYieldName = 'Upgraded Breen Drainer Weapon'
	sFireName = None

	import FoundationTech
	import Custom.Techs.UpgradedBreenDrainer

	oFire = Custom.Techs.UpgradedBreenDrainer.oUpgradedDrainerWeapon
	FoundationTech.dOnFires[__name__] = oFire

	oYield = FoundationTech.oTechs[sYieldName]
	FoundationTech.dYields[__name__] = oYield
except:
	print "Upgraded Breen Drainer Weapon not installed, or missing FoundationTech"
"""
# You can also add your ship to an immunity list, in order to keep the files unaltered... just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"Upgraded Breen Drainer Immune": 1
}
"""
# You can also add your ship to a normal breen drainer resistance list, in order to keep the files unaltered... just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"Breen Drainer Resistance": 1
}
"""
#################################################################################################################
from bcdebug import debug
import App

import FoundationTech
import MissionLib

# This should be the prime example of a special yield weapon defined
# according to Foundation Technologies.  The code is mostly based upon
# QuickBattleAddon.drainerWeapon() in Apollo's Advanced Technologies.

from ftb.Tech.DisablerYields import *

timeDrained = 300

NonSerializedObjects = (
"oUpgradedDrainerWeapon",
"oUpgradedDrainerImmune",
"oDrainerResistant",
)

def OnTorpPartialDefense(self, pShip, pInstance, pEvent):
	pPlayer = MissionLib.GetPlayer()
	if pPlayer.GetObjID() == pShip.GetObjID():
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

	pShields = pShip.GetShields()
	if pShields:
		pShieldDamage = 250 * pEvent.GetDamage()
		for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
			shieldAfter = pShields.GetCurShields(shieldDir)-pShieldDamage
			if shieldAfter < 0:
				shieldAfter = 0
			pShields.SetCurShields(shieldDir, shieldAfter)

	pImpulse = pShip.GetImpulseEngineSubsystem()

	if pImpulse and not pImpulse.IsDisabled():
		pInstance.DisableSubSys(pShip, pImpulse, timeDrained)
		#IonSubSystem(pImpulse)

	pWarp = pShip.GetWarpEngineSubsystem()
	if pWarp and not pWarp.IsDisabled():
		pInstance.DisableSubSys(pShip, pWarp, timeDrained)
		#IonSubSystem(pWarp)

	return 1


class UpgradedBreenDrainerWeaponDef(MultipleDisableDef):

	def IsDrainYield(self):
		debug(__name__ + ", IsDrainYield")
		return 0

	def IsPhaseYield(self):
		debug(__name__ + ", IsDrainYield")
		return 0

	def IsUpgradedDrainYield(self):
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

		if pInstance.__dict__['Breen Drainer Immune'] or pInstance.__dict__['Breen Drainer Resistance']:
			OnTorpPartialDefense(self, pShip, pInstance, pEvent)
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
			pInstance.DisableSubSys(pShip, pPower, 120000)

		pShields = pShip.GetShields()
		if pShields:
			pInstance.DisableSubSys(pShip, pShields, 120000)

		pCloak = pShip.GetCloakingSubsystem()
		if pCloak:
			pInstance.DisableSubSys(pShip, pCloak, 120000)

		pImpulse = pShip.GetImpulseEngineSubsystem()
		if pImpulse:
			pInstance.DisableSubSys(pShip, pImpulse, 120000)

		pWarp = pShip.GetWarpEngineSubsystem()
		if pWarp:
			pInstance.DisableSubSys(pShip, pWarp, 120000)

		pWeaponSys = pShip.GetTorpedoSystem()
		if pWeaponSys:
			pInstance.DisableSubSys(pShip, pWeaponSys, 120000)

		pWeaponSys = pShip.GetPhaserSystem()
		if pWeaponSys:
			pInstance.DisableSubSys(pShip, pWeaponSys, 120000)

		pWeaponSys = pShip.GetPulseWeaponSystem()
		if pWeaponSys:
			pInstance.DisableSubSys(pShip, pWeaponSys, 120000)


oUpgradedDrainerWeapon = UpgradedBreenDrainerWeaponDef('Upgraded Breen Drainer Weapon', {})


class UpgradedDrainerImmuneDef(FoundationTech.TechDef):

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnTorpDefense")
		if oYield and ((hasattr(oYield, "IsUpgradedDrainYield") and oYield.IsUpgradedDrainYield()) or (hasattr(oYield, "IsDrainYield") and oYield.IsDrainYield())):
			return 1

	def Attach(self, pInstance):
		debug(__name__ + ", Attach")
		pInstance.lTorpDefense.append(self)


oUpgradedDrainerImmune = UpgradedDrainerImmuneDef('Upgraded Breen Drainer Immune')


class DrainerImmuneResistanceDef(FoundationTech.TechDef):

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnTorpDefense")
		if oYield and hasattr(oYield, "IsDrainYield") and oYield.IsDrainYield():
			OnTorpPartialDefense(self, pShip, pInstance, pEvent)
			return 1

	def Attach(self, pInstance):
		debug(__name__ + ", Attach")
		pInstance.lTorpDefense.append(self)


oDrainerResistant = DrainerImmuneResistanceDef('Breen Drainer Resistance')


# print 'Upgraded Breen Weapon loaded'

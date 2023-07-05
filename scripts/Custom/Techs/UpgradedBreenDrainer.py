#################################################################################################################
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
#         UpgradedBreenDrainer by Alex SL Gato
#         Version 1.1
#         5th July 2023
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

# This should be the prime example of a special yield weapon defined according to Foundation Technologies.
# The code was mostly based upon QuickBattleAddon.drainerWeapon() in Apollo's Advanced Technologies.

from ftb.Tech.DisablerYields import *

import string

timeDrained = 300

NonSerializedObjects = (
"oUpgradedDrainerWeapon",
"oUpgradedDrainerImmune",
"oDrainerResistant",
)

global lImmuneAdvBreenDrainerShips # Some ships immune to this blow
lImmuneAdvBreenDrainerShips = (
                "Aeon",
                "AncientCity",
                "Atlantis",
                "B5LordShip",
                "B5TriadTriumvironº",
                "Battlecrab",
                "BattleTardis",
                "BattleTardisChamaleon",
                "CorsairTardis",
                "DalekVoidShip",
                "DanielJackson",
                "EAShadow_Hybrid",
                "EnterpriseJ",
                "janeway",
                "JLSAeon",
                "joke31stOberth",
                "Jubayr",
                "kirk",
                "mars",
                "MindridersThoughtforce",
                "OdysseyRefit",
                "saturn",
                "SigmaWalkerScienceLab",
                "SuperHiveShip",
                "Tardis",
                "TardisType89",
                "TardisType89Chamaleon",
                "Thant",
                "ThirdspaceCapitalShip",
                "TorvalusDarkKnife",
                "vger",
                "VulcanXRT55D",
                "VOR_Cruiser",
                "VOR_Planetkiller",
                "WCDoomMachine",
                "Wells",
                "Windrunner",
                "32C_crossfield",
                )

pVoices = [App.g_kSoundManager.GetSound("ImpulseDisabled"), App.g_kSoundManager.GetSound("WarpDisabled"), App.g_kSoundManager.GetSound("MultipleShieldsOffline")]
pBreenSound = App.g_kSoundManager.GetSound("BreenDraining")

pBrexMShieldFail = App.TGSound_Create("sfx\Bridge\Crew\Engineering\BrexNothingToAdd8.mp3", "BrexNothingToAdd8", 0)
pBrexMShieldFail.SetSFX(0) 
pBrexMShieldFail.SetInterface(1)

pBrexImpulseFail = App.TGSound_Create("sfx\Bridge\Crew\Engineering\ImpulseDisabled.mp3", "Impulse Disabled", 0)
pBrexImpulseFail.SetSFX(0) 
pBrexImpulseFail.SetInterface(1)

pBrexWarpFail = App.TGSound_Create("sfx\Bridge\Crew\Engineering\WarpDisabled.mp3", "Warp Disabled", 0)
pBrexWarpFail.SetSFX(0) 
pBrexWarpFail.SetInterface(1)

pKiskaWarpFunctional = App.TGSound_Create("sfx\Bridge\Crew\Helm\WarpFunctional.mp3", "Warp Functional", 0)
pKiskaWarpFunctional.SetSFX(0) 
pKiskaWarpFunctional.SetInterface(1)

pKiskaImpulseFunctional = App.TGSound_Create("sfx\Bridge\Crew\Helm\ImpulseFunctional.mp3", "Impulse Functional", 0)
pKiskaImpulseFunctional.SetSFX(0) 
pKiskaImpulseFunctional.SetInterface(1)

def engineerSounds(pAction, name, pSubsystem=None):
	if name != "Dummy":
		if not (pSubsystem and pSubsystem.IsDisabled()):
			App.g_kSoundManager.PlaySound(name)
	return 0

def OnTorpPartialDefense(self, pShip, pInstance, pEvent):
	initialReport = "Dummy"
	midReport = "Dummy"
	finalReport = "Dummy"
	recovery1Report = "Dummy"
	recovery2Report = "Dummy"

	# disable glow on ship
	if not pShip.IsDead(): # possible crash work around
		pShip.DisableGlowAlphaMaps()

	# clients shouldn't do anything here
	if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
		return

	pShields = pShip.GetShields()
	if pShields:
		countForMessage = 3
		pShieldDamage = 450 * pEvent.GetDamage()
		for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
			shieldAfter = pShields.GetCurShields(shieldDir)-pShieldDamage
			if shieldAfter < 0:
				shieldAfter = 0
			if shieldAfter/pShields.GetMaxShields(shieldDir) <= 0.10:
				countForMessage = countForMessage - 1
			pShields.SetCurShields(shieldDir, shieldAfter)
		if countForMessage <= 0 and App.g_kSystemWrapper.GetRandomNumber(100) < 9.0:
			finalReport = "BrexNothingToAdd8"

	#pShip.SetImpulse(0, pShip.GetWorldForwardTG(), App.PhysicsObjectClass.DIRECTION_WORLD_SPACE)
	pImpulse = pShip.GetImpulseEngineSubsystem()

	if pImpulse:
		if not pImpulse.IsDisabled():
			pInstance.DisableSubSys(pShip, pImpulse, timeDrained)
			initialReport = "Impulse Disabled"
			recovery1Report = "Impulse Functional"
		#else:
		#	pInstance.DisableSubSys(pShip, pImpulse, 1)

	pWarp = pShip.GetWarpEngineSubsystem()
	if pWarp:
		if not pWarp.IsDisabled():
			pInstance.DisableSubSys(pShip, pWarp, timeDrained)
			midReport = "Warp Disabled"
			recovery2Report = "Warp Functional"
		#else:
		#	pInstance.DisableSubSys(pShip, pWarp, 1) # Fix for some potential issues

	pPlayer = MissionLib.GetPlayer()
	if pPlayer.GetObjID() == pShip.GetObjID():
		if FoundationTech.BridgeFX:
			FoundationTech.BridgeFX.CreateDrainEffect()

		global pBreenSound
		if not pBreenSound:
			pBreenSound = App.TGSound_Create("sfx/BreenDraining.wav", "BreenDraining", 0)
		if pBreenSound:
			pBreenSound.Play()

		finalSound = "Dummy"
		if pShields and countForMessage <= 0:
			finalSound = "BrexMultipleShieldsFailed"
		pSequence = App.TGSequence_Create()
		pAction = App.TGScriptAction_Create(__name__, "engineerSounds", initialReport)
		pSequence.AddAction(pAction, None, 1.0)
		pAction = App.TGScriptAction_Create(__name__, "engineerSounds", midReport)
		pSequence.AddAction(pAction, None, 3.0)
		pAction = App.TGScriptAction_Create(__name__, "engineerSounds", finalReport)
		pSequence.AddAction(pAction, None, 5.5)
		pAction = App.TGScriptAction_Create(__name__, "engineerSounds", recovery1Report, pImpulse)
		pSequence.AddAction(pAction, None, timeDrained)
		pAction = App.TGScriptAction_Create(__name__, "engineerSounds", recovery2Report, pWarp)
		pSequence.AddAction(pAction, None, timeDrained + 3.0)
		pSequence.Play()

		#if pSound:
		#	pSound.Play()
		#pVoiceTwo = App.g_kSoundManager.GetSound("WarpDisabled")
		#if pVoiceTwo:
		#	pVoiceTwo.Play()


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

		global lImmuneAdvBreenDrainerShips
		sScript     = pShip.GetScript()
		sShipScript = string.split(sScript, ".")[-1]
		if sShipScript in lImmuneAdvBreenDrainerShips:
			return

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

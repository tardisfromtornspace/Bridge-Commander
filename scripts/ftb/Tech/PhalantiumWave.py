from bcdebug import debug
#########################################################################################################################
###	PhalantiumWave:													#
###		0 - Not active												#
###		1 - The effect designed by DreamYard, modified to work with NanoFX aswell				#											#
###	Phalantium Wave and NanoFX are now compatible ;-)								#
#########################################################################################################################

import App

import FoundationTech
import MissionLib

# This should be the prime example of a special yield weapon defined
# according to Foundation Technologies.  The code is mostly based upon
# QuickBattleAddon.drainerWeapon() in Apollo's Advanced Technologies.


class PhalantiumWaveDef(FoundationTech.TechDef):

	def OnYield(self, pShip, pInstance, pEvent, pTorp):
		# hull
		debug(__name__ + ", OnYield")
		iHDamageMax = pShip.GetHull().GetCondition()
		iHDamage = App.g_kSystemWrapper.GetRandomNumber(iHDamageMax * 0.4)
		# minimal 50% hull damage, ~70% mean, 90% maximal damage to remaining integrity
		pShip.DamageSystem(pShip.GetHull(), (iHDamageMax * 0.5) + iHDamage)

		# shields
		pShields = pShip.GetShields()
		if pShields:
			iShDamageMax = pShip.GetShields().GetCondition()
			if iShDamageMax > 1:
				# ~20% chance that this launch will completely destroy the shield system
				iShDamage = 0
				if iShDamageMax > 0:
					iShDamage = App.g_kSystemWrapper.GetRandomNumber(iShDamageMax * 0.25)
				# minimal 80% shield damage, ~90% mean damage to remaining integrity
				pShip.DamageSystem(pShields, (iShDamageMax * 0.8) + iShDamage)

		# sensors
		pSensors = pShip.GetSensorSubsystem()
		if pSensors:
			iSeDamageMax = pSensors.GetCondition()
			if iSeDamageMax > 1:
				# ~10% chance that this launch will completely destroy the shield system
				iSeDamage = App.g_kSystemWrapper.GetRandomNumber(iSeDamageMax * 0.45)
				# minimal 60% sensor damage, ~80% mean damage to remaining integrity
				pShip.DamageSystem(pSensors, (iSeDamageMax * 0.6) + iSeDamage)

		# many ways of querying subsystems; this is just one of them

		#torpedo tubes
		pTorpSys = pShip.GetTorpedoSystem()

		if pTorpSys:
			# iterate through torpedo launchers
			iNumTubes = pTorpSys.GetNumChildSubsystems()
			for jTube in range(iNumTubes):
				pTorpChild = pTorpSys.GetChildSubsystem(jTube)
				if pTorpChild:
					fToDamageMax = pTorpChild.GetConditionPercentage()
					if fToDamageMax > 0.0:
						# ~30% chance that this launch will completely destroy the launcher system
						fToDamage = App.g_kSystemWrapper.GetRandomNumber(fToDamageMax * 60.0)

						# not sure if method clamps, so just to be safe
						if (fToDamage > 40.0):
							fToDamage = 40.0

						# minimal 60% torpedo tube damage, ~90% mean damage to remaining integrity
						pTorpChild.SetConditionPercentage((fToDamageMax * 0.4) - (fToDamage * 0.01))

		# impulse drive
		pImpSys = pShip.GetImpulseEngineSubsystem()

		if pImpSys:
			# iterate through impulse drive units
			iNumImp = pImpSys.GetNumChildSubsystems()
			for iEng in range(iNumImp):
				pImpChild = pImpSys.GetChildSubsystem(iEng)
				if pImpChild:
					fImDamageMax = pImpChild.GetConditionPercentage()
					if fImDamageMax > 0.0:
						# ~17% chance that this launch will completely destroy the engine
						fImDamage = App.g_kSystemWrapper.GetRandomNumber(fImDamageMax * 70.0)

						# not sure if method clamps, so just to be safe
						if (fImDamage > 50.0):
							fImDamage = 50.0

						# minimal 50% impulse powerplant damage, ~80% mean damage to remaining integrity
						pImpChild.SetConditionPercentage ((fImDamageMax * 0.5) - (fImDamage * 0.01))

		# Spin our new hulk
		fRot = App.g_kSystemWrapper.GetRandomNumber(70)
		#SetLBRandRotation(pShip, (fRot + 1.0))

		if FoundationTech.EffectsLib:
			FoundationTech.EffectsLib.CreateSpecialFXSeq(pShip,pEvent,"Phalantium")

	# def Activate(self):
	# 	FoundationTech.oWeaponHit.Start()
	# def Deactivate(self):
	# 	FoundationTech.oWeaponHit.Stop()


oPhalantiumWave = PhalantiumWaveDef('Phalantium Wave')

# print 'Phalantium Wave loaded'

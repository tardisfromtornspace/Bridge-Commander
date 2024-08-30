import App
import Foundation
import string
import traceback

from bcdebug import debug

TRUE = 1
FALSE = 0

# If disabled, replace TRUE with FALSE
bEnabled = FALSE
try:
	from Custom.NanoFXv2.ExplosionFX import ExpFX
	import Custom.NanoFXv2.ExplosionFX.ExpSfx
	import Custom.NanoFXv2.NanoFX_ScriptActions
	import Custom.NanoFXv2.NanoFX_Lib
	import Custom.NanoFXv2.NanoFX_Config
	import Multiplayer.MissionShared

	if not ExpFX:
		print "you don't have NanoFXv2 installed"
		bEnabled = FALSE
	else:
		if not hasattr(ExpFX, "version") or ExpFX.version < 20240829:
			bEnabled = TRUE
except:
	print "NanoFX v2 beta is not installed, or an error happened:"
	bEnabled = FALSE
	traceback.print_exc()

if bEnabled:
	print "Tweaking NanoFX v2 explosions (version 20240829)"
	ExpFX.version = 20240829
	oldFunction = ExpFX.CreateNanoWeaponExpSeq
	
	def NewCreateNanoWeaponExpSeq(pEvent, sType):
		debug(__name__ + ", CreateNanoWeaponExpSeq")
		kTiming = App.TGProfilingInfo("ExpFX, CreateNanoWeaponExpSeq")
		### Create Sequence Object ###
		pSequence = App.TGSequence_Create()
	
		### Setup ###
		pShip = App.ShipClass_Cast(pEvent.GetTargetObject())
		if not pShip:
			return pSequence

		pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
		if not pShip:
			return pSequence

		### Create Nano's Small Explosion Sound ###
		if sType == "TorpShieldHit":
			pSound = ExpFX.CreateNanoSoundSeq(pShip, "ExpShieldSfx")
			pSequence.AddAction(pSound)
		else:
			pSound = ExpFX.CreateNanoSoundSeq(pShip, "ExpSmallSfx")
			pSequence.AddAction(pSound)
		###

		# little Defiant fix:
		if pShip.GetRadius() < 0.1 or (pShip.GetHull() and pShip.GetHull().GetCondition() < 100): # or else with small objects the game will crash without any warning
			return pSequence

		pSet = pShip.GetContainingSet()
		if not pSet:
			return pSequence
			
		pAttachTo = pShip.GetNode()
		pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())
		vEmitPos = pEvent.GetObjectHitPoint()
		vEmitDir = pEvent.GetObjectHitNormal()
		fSize  = pEvent.GetDamage() * (App.g_kSystemWrapper.GetRandomNumber(10) + 30) * 0.000035

		# MLeo Flying debris Edit 2
		vSpeed = pShip.GetVelocityTG()
		vEmitDir.x = vSpeed.GetX() * vEmitDir.x
		vEmitDir.y = vSpeed.GetY() * vEmitDir.y
		vEmitDir.z = vSpeed.GetZ() * vEmitDir.z

		if sType == "TorpShieldHit":
			# 0.13 is the stock photon torpedo damage radius
			auxRad = 1.0
			if pEvent.GetRadius() <= 0.0001: # Small-enough projectiles are not meant to deal knockback
				auxRad = pEvent.GetRadius() / 0.13
				fSize = (fSize / 2.0) * auxRad
				if fSize <= 0.1:
					return pSequence

				if fSize <= 1.0:
					fSize = 1.0
			elif pEvent.GetRadius() > 1.0:
				auxRad = 1.0
			else:
				fSize = (fSize / 2.0)

			if fSize < 0.00025:
				fSize = 0.00025

			pAttachTo = pSet.GetEffectRoot()
		if sType == "PhaserHullHit":
			fSize = fSize * 2.0
		###
		if sType == "TorpHullHit":
			knockback = pEvent.GetDamage()
				
			auxRad = 1.0
			if pEvent.GetRadius() <= 0.0001: # Small-enough projectiles are not meant to deal that much knockback
				auxRad = pEvent.GetRadius() / 0.13
				knockback = knockback * auxRad
				fSize = fSize * auxRad
				if fSize <= 1.0:
					fSize = 1.0

			if knockback <= 0.1:
				knockback = 0.1

			if (pEvent.GetDamage() >= 500 and sType == "TorpHullHit") and pAttachTo != None and vEmitPos != None and vEmitDir != None and pEmitFrom != None:
				pSparks = ExpFX.CreateExpSparkSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir)
				pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.4)
				pDebris = ExpFX.CreateNanoDebrisSeq(fSize * 1.25, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir)
				pSequence.AddAction(pDebris, App.TGAction_CreateNull(), 0.4)
				if (App.g_kSystemWrapper.GetRandomNumber(100) < 25):
					pSparks = ExpFX.CreateDamageSparkSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir)
					pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.4)
				pSound = ExpFX.CreateNanoSoundSeq(pShip, "ExpMedSfx")
				pSequence.AddAction(pSound, App.TGAction_CreateNull(), 0.4)
	
			### Add Rotational Spin to Ship From Torp Explosion 25% Chance##
			if (App.g_kSystemWrapper.GetRandomNumber(100) < 25):
				if (pEvent.GetDamage() >= 200): # TO-DO ADD SOMETHING HERE ABOUT NOT DOING THESE THINGS IF PSHIP-ISDEAD OR PSHIP.ISDYING???
					if (Custom.NanoFXv2.NanoFX_Config.eFX_RotationFX == "On") and (auxRad >= 1.0):
						anAction = Custom.NanoFXv2.NanoFX_Lib.CreateRotationSeq(pShip, knockback)
						if anAction:
							pSequence.AddAction(anAction, App.TGAction_CreateNull(), 0.4)
					if (Custom.NanoFXv2.NanoFX_Config.eFX_LightFlickerFX == "On"):
						anotherAction = Custom.NanoFXv2.NanoFX_Lib.CreateFlickerSeq(pShip, 1.5)
						if anotherAction:
							pSequence.AddAction(anotherAction, App.TGAction_CreateNull(), 0.4)
				else:
					###
					if (Custom.NanoFXv2.NanoFX_Config.eFX_LightFlickerFX == "On"):
						if (App.g_kSystemWrapper.GetRandomNumber(100) < 10):
							pSequence.AddAction(Custom.NanoFXv2.NanoFX_Lib.CreateFlickerSeq(pShip, 0.6))
					###
			if (Custom.NanoFXv2.NanoFX_Config.sFX_PlasmaFX == "On"):
				pPlasma = Custom.NanoFXv2.NanoFX_Lib.CreateSpecialFXSeq(pShip, pEvent, "PlasmaFX")
				if pPlasma != None:
					pSequence.AddAction(pPlasma)

		### Create Nano's Large Explosion ###
		debug(__name__ + ", CreateNanoWeaponExpSeq, the large explosion")
		if pAttachTo == None or vEmitPos == None or vEmitDir == None or pEmitFrom == None:
			return pSequence

		sFile = ExpFX.GetNanoGfxFile("ExplosionGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")
		pExplosion = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, fBrightness = 0.6)
		pSequence.AddAction(pExplosion)
		sFile = ExpFX.GetNanoGfxFile("ExpFlashGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/ExpFlash/")
		pFlash = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, iTiming = 8.0, fBrightness = 0.6)
		pSequence.AddAction(pFlash)

		iNumPlume = 3
		for iPoint in range( iNumPlume ):
			debug(__name__ + ", CreateNanoWeaponExpSeq, the iPoint explosion")
			sFile = ExpFX.GetNanoGfxFile("ExplosionGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")
			pExplosion = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize * 0.50, vEmitPos, vEmitDir, fVariance = 150.0, iTiming = 20, sType = "Plume")
			pSequence.AddAction(pExplosion)
			sFile = ExpFX.GetNanoGfxFile("ExpFlashGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/ExpFlash/")
			pFlash = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, iTiming = 4.0, fBrightness = 0.6)
			pSequence.AddAction(pFlash)
		###
		return pSequence

	ExpFX.CreateNanoWeaponExpSeq = NewCreateNanoWeaponExpSeq

	#oldDeathSeq = ExpFX.NanoDeathSeq # At the moment not adding this, still needs some tweaks

	def NewNanoDeathSeq(pShip):
		### Holds the Entire Death Sequence ###
		debug(__name__ + ", NanoDeathSeq")
		pFullSequence = App.TGSequence_Create()
		###
		### Setup Sequence Timing ###
		fTotalSequenceTime = 14
		fExplosionShift = -8.0
		###
		### Set up Exploding Ship Properties ###
		pExplodingShip = App.ShipClass_Cast(pShip)
		if not pExplodingShip:
			return

		pExplodingShip = App.ShipClass_GetObjectByID(None, pExplodingShip.GetObjID())
		if not pExplodingShip:
			return

		pExplodingShip.SetMass(50000)
		pExplodingShip.SetRotationalInertia(11000)
		fRadius = 0.0

		if (pExplodingShip.GetName() == "Player") or (pExplodingShip.GetName() == "player"):
			pExplodingShip.SetLifeTime (fTotalSequenceTime)
			pWarpPower = pExplodingShip.GetPowerSubsystem()
			if pWarpPower and pWarpPower.GetPowerOutput() > 0:
				pWarpPower = pExplodingShip.GetRadius() * 15
			else:
				pWarpPower = 15
			fRadius = pWarpPower
		else:
			pExplodingShip.SetLifeTime (fTotalSequenceTime / 2 + 1)
			pWarpPower = pExplodingShip.GetPowerSubsystem()
			if pWarpPower:
				pWarpPower = (pWarpPower.GetAvailablePower() * 0.025) + (pWarpPower.GetPowerOutput() * 0.075)
				pWarpPower = pWarpPower * Custom.NanoFXv2.NanoFX_Config.eFX_SplashRadius
				fRadius = pWarpPower / 50.0
				if pWarpPower:
					pExplodingShip.SetSplashDamage(pWarpPower, fRadius)
					print("Setting splash damage for %s to (%f, %f)" % (pExplodingShip.GetName(), pExplodingShip.GetSplashDamage(), pExplodingShip.GetSplashDamageRadius()))
					debug(__name__ + ", NanoDeathSeq Setting splash damage for %s to (%f, %f)" % (pExplodingShip.GetName(), pExplodingShip.GetSplashDamage(), pExplodingShip.GetSplashDamageRadius()))
		###
		### Begin Death Sequence ###
		############################
		###
		### Flicker some lights ###
		if (Custom.NanoFXv2.NanoFX_Config.eFX_LightFlickerFX == "On"):
			pFullSequence.AddAction(Custom.NanoFXv2.NanoFX_Lib.CreateFlickerSeq(pExplodingShip, 3.0, sStatus = "Off"), App.TGAction_CreateNull(), 1.0)
		###
		### Create Nano's Initial Large explosions ###
		pFullSequence.AddAction(ExpFX.CreateNanoExpSmallSeq(pExplodingShip, 0.01), App.TGAction_CreateNull(), 0.2)
		pFullSequence.AddAction(ExpFX.CreateNanoExpLargeSeq(pExplodingShip, 2), App.TGAction_CreateNull(), fTotalSequenceTime - 3.2 + fExplosionShift)
		pFullSequence.AddAction(ExpFX.CreateNanoExpLargeSeq(pExplodingShip, 2), App.TGAction_CreateNull(), fTotalSequenceTime - 3.05 + fExplosionShift)
		pFullSequence.AddAction(ExpFX.CreateNanoExpLargeSeq(pExplodingShip, 2), App.TGAction_CreateNull(), fTotalSequenceTime - 2.85 + fExplosionShift)
		###
		### Destroy Model into Debris Parts ###
		pFullSequence.AddAction(ExpFX.CreateNanoExpSmallSeq(pExplodingShip, 2.0), App.TGAction_CreateNull(), fTotalSequenceTime - 1.7 + fExplosionShift)
		###
		### Add Random Spin to Model ###
		if (Custom.NanoFXv2.NanoFX_Config.eFX_RotationFX == "On"):
			pFullSequence.AddAction(Custom.NanoFXv2.NanoFX_Lib.CreateRotationSeq(pExplodingShip, 700), App.TGAction_CreateNull(), 0.3)
			pFullSequence.AddAction(Custom.NanoFXv2.NanoFX_Lib.CreateRotationSeq(pExplodingShip, 1000, 0.5), App.TGAction_CreateNull(), fTotalSequenceTime - 1.6 + fExplosionShift)
		###
		### Create Nano's Warp Core Explosion ###
		if fRadius and fRadius > 0.0:
			pFullSequence.AddAction(ExpFX.CreateNanoExpNovaSeq(pExplodingShip, fRadius / 15), App.TGAction_CreateNull(), fTotalSequenceTime - 1.7 + fExplosionShift)
			#pFullSequence.AddAction(ExpFX.ShakeSequence(1.5), App.TGAction_CreateNull(), fTotalSequenceTime - 1.3 + fExplosionShift)
		###
		### Create Nano's Final Explosions ###
		pFullSequence.AddAction(ExpFX.CreateNanoExpLargeSeq(pExplodingShip, 2), App.TGAction_CreateNull(), fTotalSequenceTime - 1.95 + fExplosionShift)
		pFullSequence.AddAction(ExpFX.CreateNanoExpLargeSeq(pExplodingShip, 2), App.TGAction_CreateNull(), fTotalSequenceTime - 1.85 + fExplosionShift)
		pFullSequence.AddAction(ExpFX.CreateNanoExpLargeSeq(pExplodingShip, 2), App.TGAction_CreateNull(), fTotalSequenceTime - 1.65 + fExplosionShift)
		###
		#pFullSequence.SetUseRealTime(1)
		pFullSequence.AppendAction(App.TGScriptAction_Create("Custom.NanoFXv2.ExplosionFX.ExpFX", "DoPostExplosionStuff", pExplodingShip.GetObjID()), fTotalSequenceTime)
		#pFullSequence.AppendAction(App.TGScriptAction_Create("Custom.NanoFXv2.NanoFX_ScriptActions", "DestroyTGSequence", pFullSequence), fTotalSequenceTime)
		pFullSequence.Play()
		###
		bFound = 0
		for sName in Custom.NanoFXv2.NanoFX_Lib.g_LightsOff:
			if pShip.GetName() == sName:
				bFound = 1
			if bFound == 1:
				Custom.NanoFXv2.NanoFX_Lib.g_LightsOff.remove(pShip.GetName())

	#ExpFX.NanoDeathSeq = NewNanoDeathSeq
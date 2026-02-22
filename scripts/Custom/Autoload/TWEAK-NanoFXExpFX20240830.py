# VERSION 1.1.1
# 22nd February 2026

import App
import Foundation
import string
import traceback

from bcdebug import debug

TRUE = 1
FALSE = 0

versionPatch = 20260222 # Our version of the patch
# If disabled, replace TRUE with FALSE
bEnabled = FALSE

def ASequenceDummy(pAction):
	return 0

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
		if not hasattr(ExpFX, "version") or ExpFX.version < versionPatch:
			bEnabled = TRUE
except:
	print "NanoFX v2 beta is not installed, or an error happened:"
	bEnabled = FALSE
	traceback.print_exc()

if bEnabled:
	print "Tweaking NanoFX v2 explosions (version ", versionPatch, ")"
	#ExpFX.version = versionPatch

	oldCreateNanoWeaponExpSeq = ExpFX.CreateNanoWeaponExpSeq

	oldCreateNanoExpNovaSeq = ExpFX.CreateNanoExpNovaSeq
	oldCreateNanoExpLargeSeq = ExpFX.CreateNanoExpLargeSeq
	oldCreateNanoExpSmallSeq = ExpFX.CreateNanoExpSmallSeq
	oldNanoCollisionEffect = ExpFX.NanoCollisionEffect

	oldNanoDeathSeq = ExpFX.NanoDeathSeq # At the moment not adding this, still needs some tweaks

	# PATCH FOR: CreateNanoWeaponExpSeq
	def NewCreateNanoWeaponExpSeq(pEvent, sType):
		debug(__name__ + ", NewCreateNanoWeaponExpSeq")
		kTiming = App.TGProfilingInfo("ExpFX, CreateNanoWeaponExpSeq")
		### Create Sequence Object ###
		actionsAdded = 0
		pSequence = App.TGSequence_Create()
		### Setup ###
		pShip = App.ShipClass_Cast(pEvent.GetTargetObject())
		if not pShip or not hasattr(pShip, "GetObjID"):
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		iShipID = pShip.GetObjID()

		pShip = App.ShipClass_GetObjectByID(None, iShipID)
		if not pShip:
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		# little Defiant fix:
		if pShip.GetRadius() < 0.1: # or else with small objects the game will crash without any warning
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		myHull = pShip.GetHull()
		if not myHull or myHull.GetCondition() < 100: # or else with small objects the game will crash without any warning
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence		

		pSet = pShip.GetContainingSet()
		if not pSet:
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		### Create Nano's Small Explosion Sound ###
		if sType == "TorpShieldHit":
			pSound = ExpFX.CreateNanoSoundSeq(pShip, "ExpShieldSfx")
			if pSound:
				actionsAdded = actionsAdded + 1
				pSequence.AddAction(pSound)
		else:
			pSound = ExpFX.CreateNanoSoundSeq(pShip, "ExpSmallSfx")
			if pSound:
				actionsAdded = actionsAdded + 1
				pSequence.AddAction(pSound)
		###
			
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
					if actionsAdded <= 0:
						pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
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
				if pSparks:
					pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.4)
					actionsAdded = actionsAdded + 1
				pDebris = ExpFX.CreateNanoDebrisSeq(fSize * 1.25, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir)
				if pDebris:
					pSequence.AddAction(pDebris, App.TGAction_CreateNull(), 0.4)
					actionsAdded = actionsAdded + 1
				if (App.g_kSystemWrapper.GetRandomNumber(100) < 25):
					pSparks = ExpFX.CreateDamageSparkSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir)
					if pSparks:
						pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.4)
						actionsAdded = actionsAdded + 1

				pSound = ExpFX.CreateNanoSoundSeq(pShip, "ExpMedSfx")
				if pSound:
					pSequence.AddAction(pSound, App.TGAction_CreateNull(), 0.4)
					actionsAdded = actionsAdded + 1
	
			### Add Rotational Spin to Ship From Torp Explosion 25% Chance##
			if (App.g_kSystemWrapper.GetRandomNumber(100) < 25) and not (pShip.IsDead() or pShip.IsDying()):
				if (pEvent.GetDamage() >= 200):
					if (Custom.NanoFXv2.NanoFX_Config.eFX_RotationFX == "On") and (auxRad >= 1.0):
						anAction = Custom.NanoFXv2.NanoFX_Lib.CreateRotationSeq(pShip, knockback)
						if anAction:
							pSequence.AddAction(anAction, App.TGAction_CreateNull(), 0.4)
							actionsAdded = actionsAdded + 1
					if (Custom.NanoFXv2.NanoFX_Config.eFX_LightFlickerFX == "On"):
						anotherAction = Custom.NanoFXv2.NanoFX_Lib.CreateFlickerSeq(pShip, 1.5)
						if anotherAction:
							pSequence.AddAction(anotherAction, App.TGAction_CreateNull(), 0.4)
							actionsAdded = actionsAdded + 1
				else:
					###
					if (Custom.NanoFXv2.NanoFX_Config.eFX_LightFlickerFX == "On"):
						if (App.g_kSystemWrapper.GetRandomNumber(100) < 10):
							anotherOtherAction = Custom.NanoFXv2.NanoFX_Lib.CreateFlickerSeq(pShip, 0.6)
							if anotherOtherAction:
								pSequence.AddAction(anotherOtherAction)
								actionsAdded = actionsAdded + 1
					###
			if (Custom.NanoFXv2.NanoFX_Config.sFX_PlasmaFX == "On") and not (pShip.IsDead() or pShip.IsDying()):
				pPlasma = Custom.NanoFXv2.NanoFX_Lib.CreateSpecialFXSeq(pShip, pEvent, "PlasmaFX")
				if pPlasma != None:
					pSequence.AddAction(pPlasma)
					actionsAdded = actionsAdded + 1

		### Create Nano's Large Explosion ###
		debug(__name__ + ", CreateNanoWeaponExpSeq, the large explosion")
		if pAttachTo == None or vEmitPos == None or vEmitDir == None or pEmitFrom == None or fSize <= 0.0:
			if actionsAdded <= 0:
				pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		sFile = ExpFX.GetNanoGfxFile("ExplosionGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")
		pExplosion = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, fBrightness = 0.6)
		if pExplosion:
			pSequence.AddAction(pExplosion)
			actionsAdded = actionsAdded + 1
		sFile = ExpFX.GetNanoGfxFile("ExpFlashGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/ExpFlash/")
		pFlash = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, iTiming = 8.0, fBrightness = 0.6)
		if pFlash:
			pSequence.AddAction(pFlash)
			actionsAdded = actionsAdded + 1
		iNumPlume = 3
		for iPoint in range( iNumPlume ):
			debug(__name__ + ", CreateNanoWeaponExpSeq, the iPoint explosion")
			sFile = ExpFX.GetNanoGfxFile("ExplosionGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")
			pExplosion = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize * 0.50, vEmitPos, vEmitDir, fVariance = 150.0, iTiming = 20, sType = "Plume")
			if pExplosion:
				pSequence.AddAction(pExplosion)
				actionsAdded = actionsAdded + 1
			sFile = ExpFX.GetNanoGfxFile("ExpFlashGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/ExpFlash/")
			pFlash = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, iTiming = 4.0, fBrightness = 0.6)
			if pFlash:
				pSequence.AddAction(pFlash)
				actionsAdded = actionsAdded + 1
		###
		if actionsAdded == 0:
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 

		return pSequence

	ExpFX.CreateNanoWeaponExpSeq = NewCreateNanoWeaponExpSeq

	# PATCH FOR: CreateNanoExpNovaSeq
	def NewCreateNanoExpNovaSeq(pShip, fSize):
		debug(__name__ + ", NewCreateNanoExpNovaSeq")

		kTiming = App.TGProfilingInfo("ExpFX, CreateNanoExpNovaSeq")
		### Create Sequence Object ###
		actionsAdded = 0
		pSequence = App.TGSequence_Create()

		if not pShip or not hasattr(pShip, "GetObjID"):
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		iShipID = pShip.GetObjID()

		pShip = App.ShipClass_GetObjectByID(None, iShipID)
		if not pShip:
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		pSet = pShip.GetContainingSet()
		if not pSet:
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		###
		### Setup for Effect ###
		pAttachTo 	 = pSet.GetEffectRoot()
		pEmitFrom 	 = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())

		pWarpcore 	 = pShip.GetPowerSubsystem()
		pWarpcoreEmitPos = App.NiPoint3(0, 0, 0)
		if pWarpcore and hasattr(pWarpcore, "GetPosition"):
			pWarpcoreEmitPos = pWarpcore.GetPosition()
		else:
		#if not pWarpcore or not hasattr(pWarpcore, "GetPosition"):
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence
		
		vEmitDir = App.NiPoint3((App.g_kSystemWrapper.GetRandomNumber(200) - 100) * 0.01, (App.g_kSystemWrapper.GetRandomNumber(200) - 100) * 0.01, (App.g_kSystemWrapper.GetRandomNumber(200) - 100) * 0.01)
		fFlashColor   = Custom.NanoFXv2.NanoFX_Lib.GetOverrideColor(pShip, "ExpFX")
		iShow = 0.0
		if pShip.GetName() == "Player" or pShip.GetName() == "player":
			iShow = 2.0

		if (fFlashColor == None):
			sRace 			= Custom.NanoFXv2.NanoFX_Lib.GetSpeciesName(pShip)
			fFlashColor 	= Custom.NanoFXv2.NanoFX_Lib.GetRaceTextureColor(sRace)

		###
		if fSize != 1:
			sFile = ExpFX.GetNanoGfxFile("NovaRingGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/NovaRing/")
			pExplosion = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize * (5.0 + iShow), pWarpcoreEmitPos, iTiming = 64, fRed = fFlashColor[0], fGreen = fFlashColor[1], fBlue = fFlashColor[2], fBrightness = 0.5)
			if pExplosion:
				pSequence.AddAction(pExplosion, App.TGAction_CreateNull(), 0.4)
				actionsAdded = actionsAdded + 1
			sFile = ExpFX.GetNanoGfxFile("NovaSphereGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/NovaSphere/")
			pExplosion = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize * (3.0 + iShow), pWarpcoreEmitPos, iTiming = 28)
			if pExplosion:
				pSequence.AddAction(pExplosion, App.TGAction_CreateNull(), 0.5)
				actionsAdded = actionsAdded + 1
			sFile = ExpFX.GetNanoGfxFile("NovaFlashGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/NovaFlash/")
			pExplosion = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize * (3.0 + iShow), pWarpcoreEmitPos, iTiming = 20)
			if pExplosion:
				pSequence.AddAction(pExplosion)
				actionsAdded = actionsAdded + 1
			### Create Nano's Nova Explosion Sound ###
			pSound = ExpFX.CreateNanoSoundSeq(pShip, "ExpNovaSfx")
			if pSound:
				pSequence.AddAction(pSound)
				actionsAdded = actionsAdded + 1
			###
			### Damage the model with Warp Core Explosion ###
			aDmgAction = App.TGScriptAction_Create("Custom.NanoFXv2.NanoFX_ScriptActions", "NanoDamageShip", pShip, pEmitFrom, pShip.GetRadius(), 600.0)
			if aDmgAction:
				pSequence.AddAction(aDmgAction, App.TGAction_CreateNull(), 0.7)
				actionsAdded = actionsAdded + 1
		else:
			fSize = pShip.GetRadius() / 1.2
			### Create Nano's Nova Explosion Sound ###
			pSound = ExpFX.CreateNanoSoundSeq(pShip, "ExpLargeSfx")
			if pSound:
				pSequence.AddAction(pSound)
				actionsAdded = actionsAdded + 1
			###
		iNovaSparks = Custom.NanoFXv2.NanoFX_Config.eFX_ExpSparkFXLevel * 7.0
		for iPoint in range( iNovaSparks ):
			fRand = App.g_kSystemWrapper.GetRandomNumber(100) *  0.01
			pSparks = ExpFX.CreateExpSparkSeq(fSize * (0.8 + fRand), pEmitFrom, pAttachTo, pWarpcoreEmitPos, vEmitDir)
			if pSparks:
				pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.50)
				actionsAdded = actionsAdded + 1
		###

		if actionsAdded == 0:
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 

		return pSequence

	ExpFX.CreateNanoExpNovaSeq = NewCreateNanoExpNovaSeq

	# PATCH FOR: CreateNanoExpLargeSeq
	def NewCreateNanoExpLargeSeq(pShip, iNumPlume):
		debug(__name__ + ", NewCreateNanoExpLargeSeq")
		kTiming = App.TGProfilingInfo("ExpFX, CreateNanoExpLargeSeq")
		### Create Sequence Object ###
		actionsAdded = 0
		pSequence = App.TGSequence_Create()

		if not pShip or not hasattr(pShip, "GetObjID"):
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		iShipID = pShip.GetObjID()

		pShip = App.ShipClass_GetObjectByID(None, iShipID)
		if not pShip:
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		# prevent GetRandomPointOnModel() from crashing the game on dying/dead ships
		if pShip.IsDead() or pShip.IsDying():
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		pSet = pShip.GetContainingSet()
		if not pSet:
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		###
		### Setup for Effect ###
		pEmitFrom = pShip.GetRandomPointOnModel()
		pAttachTo = pShip.GetNode()
		vEmitPos = App.NiPoint3(0, 0, 0)
		vEmitDir = App.NiPoint3(1, 1, 1)
		fSize     = pShip.GetRadius() * 0.50
		sFile     = ExpFX.GetNanoGfxFile("ExplosionGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")
		###
		pSound = ExpFX.CreateNanoSoundSeq(pShip, "ExpMedSfx")
		if pSound:
			actionsAdded = actionsAdded + 1
			pSequence.AddAction(pSound)

		# little Defiant fix: just don't crash with small objects, please.
		myHull = pShip.GetHull()
		if not myHull or myHull.GetCondition() <= 0: # or else with small objects the game will crash without any warning
			if actionsAdded <= 0:
				pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		if pShip.GetRadius() < 0.1 or (myHull.GetCondition() < 100):
			if actionsAdded <= 0:
				pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		if not pEmitFrom:
			if actionsAdded <= 0:
				pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		pExplosion = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize)
		if pExplosion:
			pSequence.AddAction(pExplosion)
			actionsAdded = actionsAdded + 1
		pSparks = ExpFX.CreateExpSparkSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir)
		if pSparks:
			pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.5)
			actionsAdded = actionsAdded + 1

		pDebris = ExpFX.CreateNanoDebrisSeq(fSize, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir)
		if pDebris:
			pSequence.AddAction(pDebris, App.TGAction_CreateNull(), 0.5)
			actionsAdded = actionsAdded + 1

		for iPoint in range( iNumPlume ):
			sFile = ExpFX.GetNanoGfxFile("ExplosionGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")
			pExplosion = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize / 3.0,  fVariance = 120.0, iTiming = 20, sType = "Plume", fBrightness = 0.3)
			if pExplosion:
				pSequence.AddAction(pExplosion)
				actionsAdded = actionsAdded + 1
			pSparks = ExpFX.CreateExpSparkSeq(fSize, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir)
			if pSparks:
				pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.5)
				actionsAdded = actionsAdded + 1
			pDebris = ExpFX.CreateNanoDebrisSeq(fSize, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir)
			if pDebris:
				pSequence.AddAction(pDebris, App.TGAction_CreateNull(), 0.5)
				actionsAdded = actionsAdded + 1
		###
		if actionsAdded == 0:
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 

		return pSequence

	ExpFX.CreateNanoExpLargeSeq = NewCreateNanoExpLargeSeq

	# PATCH FOR: CreateNanoExpSmallSeq

	def NewCreateNanoExpSmallSeq(pShip, fTime):
		debug(__name__ + ", NewCreateNanoExpSmallSeq")
		kTiming = App.TGProfilingInfo("ExpFX, CreateNanoExpSmallSeq")
		### Create Sequence Object ###
		actionsAdded = 0
		pSequence = App.TGSequence_Create()
		###
		### Setup for Effect ###

		if not pShip or not hasattr(pShip, "GetObjID"):
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		iShipID = pShip.GetObjID()

		pShip = App.ShipClass_GetObjectByID(None, iShipID)
		if not pShip:
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		pSet = pShip.GetContainingSet()
		if not pSet:
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		iNumPlume = 1
		pAttachTo = pShip.GetNode()
		vEmitPos = App.NiPoint3(0, 0, 0)
		vEmitDir = App.NiPoint3(1, 1, 1)
		###
		### Create Nano's Explosion Sound ###
		pSound = ExpFX.CreateNanoSoundSeq(pShip, "ExpLargeSfx")
		pSequence.AddAction(pSound)
		fExplosionTime = 0.0
		# little Defiant fix: just don't crash with small objects, please.
		# and prevent GetRandomPointOnModel() from crashing the game on dying/dead ships
		# check: maybe the small object problem is linked to the randompoint one.
		#if pShip.GetRadius() < 0.1 or (pShip.GetHull() and pShip.GetHull().GetCondition() < 100) or pShip.IsDead() or pShip.IsDying():

		myHull = pShip.GetHull()
		if not myHull: # or else with small objects the game will crash without any warning
			if actionsAdded <= 0:
				pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		## prevent GetRandomPointOnModel() from crashing the game on dying/dead ships
		if pShip.IsDead(): # or pShip.IsDying():
			if actionsAdded <= 0:
				pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		if pShip.GetRadius() < 0.1:
			if actionsAdded <= 0:
				pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		shipRadius = pShip.GetRadius()

		while (fExplosionTime < fTime):
			###
			### Create Nano's Visual Smaller Explosions ###
			# prevent GetRandomPointOnModel() from crashing the game on dying/dead ships
			#if pShip.IsDead() or pShip.IsDying() or not pShip.GetHull() or pShip.GetHull().GetConditionPercentage() == 0:
			if pShip.IsDead():
				if actionsAdded <= 0:
					pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
				return pSequence

			pEmitFrom = pShip.GetRandomPointOnModel()
			if not pEmitFrom:
				if actionsAdded <= 0:
					pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
				return pSequence
			fSize  = shipRadius * (App.g_kSystemWrapper.GetRandomNumber(40) + 20) * 0.01
			sFile = ExpFX.GetNanoGfxFile("ExplosionGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")
			pExplosion = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize)
			if pExplosion:
				pSequence.AddAction(pExplosion)
				actionsAdded = actionsAdded + 1
			pSparks = ExpFX.CreateExpSparkSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir)
			if pSparks:
				pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.5)
				actionsAdded = actionsAdded + 1
			pDebris = ExpFX.CreateNanoDebrisSeq(fSize, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir)
			if pDebris:
				pSequence.AddAction(pDebris, App.TGAction_CreateNull(), 0.5)
				actionsAdded = actionsAdded + 1
			for iPoint in range( iNumPlume ):
				sFile = ExpFX.GetNanoGfxFile("ExplosionGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")
				pExplosion = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize / 3.0,  fVariance = 120.0, iTiming = 20, sType = "Plume")
				if pExplosion:
					pSequence.AddAction(pExplosion)
					actionsAdded = actionsAdded + 1
				pSparks = ExpFX.CreateExpSparkSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir)
				if pSparks:
					pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.5)
					actionsAdded = actionsAdded + 1
				pDebris = ExpFX.CreateNanoDebrisSeq(fSize, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir)
				if pDebris:
					pSequence.AddAction(pDebris, App.TGAction_CreateNull(), 0.5)
					actionsAdded = actionsAdded + 1
			###
			### Damage the model with these explosions ###
			dmgModelAction = App.TGScriptAction_Create("Custom.NanoFXv2.NanoFX_ScriptActions", "NanoDamageShip", pShip, pEmitFrom, shipRadius / 2.0, 1200.0)
			if dmgModelAction:
				pSequence.AddAction(dmgModelAction, App.TGAction_CreateNull(), 0.3)
				actionsAdded = actionsAdded + 1

			fExtraDamage = 0.1
			while (fExtraDamage < fTime):
				# prevent GetRandomPointOnModel() from crashing the game on dying/dead ships
				#if pShip.IsDead() or pShip.IsDying() or not pShip.GetHull() or pShip.GetHull().GetConditionPercentage() == 0:
				if pShip.IsDead():
					if actionsAdded <= 0:
						pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
					return pSequence
				pEmitFrom = pShip.GetRandomPointOnModel()
				if not pEmitFrom:
					if actionsAdded <= 0:
						pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
					return pSequence
				anotherDmgAction = App.TGScriptAction_Create("Custom.NanoFXv2.NanoFX_ScriptActions", "NanoDamageShip", pShip, pEmitFrom, shipRadius / 3.0, 1200.0)
				if anotherDmgAction:
					pSequence.AddAction(anotherDmgAction, App.TGAction_CreateNull(), 0.3)
					actionsAdded = actionsAdded + 1
				fExtraDamage = fExtraDamage + 0.04
			###
			fExplosionTime = fExplosionTime + 0.5

		if actionsAdded == 0:
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 

		return pSequence

	ExpFX.CreateNanoExpSmallSeq = NewCreateNanoExpSmallSeq

	# PATCH FOR: NanoDeathSeq

	def NewNanoDeathSeq(pShip):
		### Holds the Entire Death Sequence ###
		debug(__name__ + ", NewNanoDeathSeq")
		pFullSequence = App.TGSequence_Create()
		actionsAdded = 0
		###
		### Setup Sequence Timing ###
		fTotalSequenceTime = 14
		fExplosionShift = -8.0
		###
		### Set up Exploding Ship Properties ###
		pExplodingShip = App.ShipClass_Cast(pShip)
		if not pExplodingShip or not hasattr(pExplodingShip, "GetObjID"):
			pFullSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			pFullSequence.Play()
			return

		iShipID = pExplodingShip.GetObjID()

		pExplodingShip = App.ShipClass_GetObjectByID(None, iShipID)
		if not pExplodingShip:
			pFullSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			pFullSequence.Play()
			return

		pExplodingShip.SetMass(50000)
		pExplodingShip.SetRotationalInertia(11000)

		fRadius = 0.0
		shipName = pExplodingShip.GetName()
		fExplodingShipRadius = pExplodingShip.GetRadius()
		pWarpSubsys = pExplodingShip.GetPowerSubsystem()
		if (pExplodingShip.GetName() == "Player") or (pExplodingShip.GetName() == "player"):
			pExplodingShip.SetLifeTime (fTotalSequenceTime)
			pWarpPower = 15
			if pWarpSubsys and pWarpSubsys.GetPowerOutput() > 0 and fExplodingShipRadius > 0:
				pWarpPower = pWarpPower * fExplodingShipRadius
			fRadius = pWarpPower
		else:
			pExplodingShip.SetLifeTime (fTotalSequenceTime / 2 + 1)
			if pWarpSubsys:
				pWarpPower = (pWarpSubsys.GetAvailablePower() * 0.025) + (pWarpSubsys.GetPowerOutput() * 0.075)
				pWarpPower = pWarpPower * Custom.NanoFXv2.NanoFX_Config.eFX_SplashRadius
				fRadius = pWarpPower / 50.0
				if pWarpPower:
					pExplodingShip.SetSplashDamage(pWarpPower, fRadius)
					print("Setting splash damage for %s to (%f, %f)" % (pExplodingShip.GetName(), pExplodingShip.GetSplashDamage(), pExplodingShip.GetSplashDamageRadius()))
					debug(__name__ + ", NewNanoDeathSeq Setting splash damage for %s to (%f, %f)" % (pExplodingShip.GetName(), pExplodingShip.GetSplashDamage(), pExplodingShip.GetSplashDamageRadius()))
		###
		### Begin Death Sequence ###
		############################
		###
		### Flicker some lights ###
		if (Custom.NanoFXv2.NanoFX_Config.eFX_LightFlickerFX == "On"):
			pFlickerAction1 = Custom.NanoFXv2.NanoFX_Lib.CreateFlickerSeq(pExplodingShip, 3.0, sStatus = "Off")
			if pFlickerAction1:
				pFullSequence.AddAction(pFlickerAction1, App.TGAction_CreateNull(), 1.0)
				actionsAdded = actionsAdded + 1
		###
		### Create Nano's Initial Large explosions ###
		pSmallExpSeq1 = ExpFX.CreateNanoExpSmallSeq(pExplodingShip, 0.01)
		if pSmallExpSeq1:
			pFullSequence.AddAction(pSmallExpSeq1, App.TGAction_CreateNull(), 0.2)
			actionsAdded = actionsAdded + 1
		pLargeExpSeq1 = ExpFX.CreateNanoExpLargeSeq(pExplodingShip, 2)
		if pLargeExpSeq1:
			pFullSequence.AddAction(pLargeExpSeq1, App.TGAction_CreateNull(), fTotalSequenceTime - 3.2 + fExplosionShift)
			actionsAdded = actionsAdded + 1

		pLargeExpSeq2 = ExpFX.CreateNanoExpLargeSeq(pExplodingShip, 2)
		if pLargeExpSeq2:
			pFullSequence.AddAction(pLargeExpSeq2, App.TGAction_CreateNull(), fTotalSequenceTime - 3.05 + fExplosionShift)
			actionsAdded = actionsAdded + 1

		pLargeExpSeq3 = ExpFX.CreateNanoExpLargeSeq(pExplodingShip, 2)
		if pLargeExpSeq3:
			pFullSequence.AddAction(pLargeExpSeq3, App.TGAction_CreateNull(), fTotalSequenceTime - 2.85 + fExplosionShift)
			actionsAdded = actionsAdded + 1
		###
		### Destroy Model into Debris Parts ###
		pSmallExpSeq2 = ExpFX.CreateNanoExpSmallSeq(pExplodingShip, 2.0)
		if pSmallExpSeq2:
			pFullSequence.AddAction(pSmallExpSeq2, App.TGAction_CreateNull(), fTotalSequenceTime - 1.7 + fExplosionShift)
			actionsAdded = actionsAdded + 1
		###
		### Add Random Spin to Model ###
		if (Custom.NanoFXv2.NanoFX_Config.eFX_RotationFX == "On"):
			pRotAction1 = Custom.NanoFXv2.NanoFX_Lib.CreateRotationSeq(pExplodingShip, 700)
			if pRotAction1:
				pFullSequence.AddAction(pRotAction1, App.TGAction_CreateNull(), 0.3)
				actionsAdded = actionsAdded + 1
			pRotAction2 = Custom.NanoFXv2.NanoFX_Lib.CreateRotationSeq(pExplodingShip, 1000, 0.5)
			if pRotAction2:
				pFullSequence.AddAction(pRotAction2, App.TGAction_CreateNull(), fTotalSequenceTime - 1.6 + fExplosionShift)
				actionsAdded = actionsAdded + 1
		###
		### Create Nano's Warp Core Explosion ###
		if fRadius and fRadius > 0.0:
			pNovaExpAction1 = ExpFX.CreateNanoExpNovaSeq(pExplodingShip, fRadius / 15)
			if pNovaExpAction1:
				pFullSequence.AddAction(pNovaExpAction1, App.TGAction_CreateNull(), fTotalSequenceTime - 1.7 + fExplosionShift)
				actionsAdded = actionsAdded + 1
			#pShakeSequuence = ExpFX.ShakeSequence(1.5) # This Sequence does not exist in modern NanoFX
			#if pShakeSequuence:
			#	pFullSequence.AddAction(pShakeSequuence, App.TGAction_CreateNull(), fTotalSequenceTime - 1.3 + fExplosionShift)
			#	actionsAdded = actionsAdded + 1
		###
		### Create Nano's Final Explosions ###
		pFinalExpAction1 = ExpFX.CreateNanoExpLargeSeq(pExplodingShip, 2)
		if pFinalExpAction1:
			pFullSequence.AddAction(pFinalExpAction1, App.TGAction_CreateNull(), fTotalSequenceTime - 1.95 + fExplosionShift)
			actionsAdded = actionsAdded + 1

		pFinalExpAction2 = ExpFX.CreateNanoExpLargeSeq(pExplodingShip, 2)
		if pFinalExpAction2:
			pFullSequence.AddAction(pFinalExpAction2, App.TGAction_CreateNull(), fTotalSequenceTime - 1.85 + fExplosionShift)
			actionsAdded = actionsAdded + 1

		pFinalExpAction3 = ExpFX.CreateNanoExpLargeSeq(pExplodingShip, 2)
		if pFinalExpAction3:
			pFullSequence.AddAction(pFinalExpAction3, App.TGAction_CreateNull(), fTotalSequenceTime - 1.65 + fExplosionShift)
			actionsAdded = actionsAdded + 1
		###
		#pFullSequence.SetUseRealTime(1)
		pPostExplosionStuffAction = App.TGScriptAction_Create("Custom.NanoFXv2.ExplosionFX.ExpFX", "DoPostExplosionStuff", iShipID)
		if pPostExplosionStuffAction:
			pFullSequence.AppendAction(pPostExplosionStuffAction, fTotalSequenceTime)
			actionsAdded = actionsAdded + 1

		if actionsAdded == 0:
			pFullSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 

		#pDestroyTGSequenceAction = App.TGScriptAction_Create("Custom.NanoFXv2.NanoFX_ScriptActions", "DestroyTGSequence", pFullSequence) # This sequence exists but was commented on newer NanoFX, so I'll leave it commented
		#if pDestroyTGSequenceAction:
		#	pFullSequence.AppendAction(pDestroyTGSequenceAction, fTotalSequenceTime)
		pFullSequence.Play()
		###
		bFound = 0
		listToDelete = []
		try:
			for sName in Custom.NanoFXv2.NanoFX_Lib.g_LightsOff: # You cannot use a for loop to traverse lists to then delete items on that, not this way - internally C just makes it skip one, which is not good!
				if shipName == sName:
					bFound = 1
				if bFound == 1:
					listToDelete.append(sName)
		except:
			traceback.print_exc()

		try:
			for sName in listToDelete: # Weird cases where you have multiple of the same name.
				Custom.NanoFXv2.NanoFX_Lib.g_LightsOff.remove(sName)
		except:
			traceback.print_exc()

	ExpFX.NanoDeathSeq = NewNanoDeathSeq

	# PATCH FOR: NanoCollisionEffect

	def NewNanoCollisionEffect(pShip, pEvent):
		### Setup ###
		debug(__name__ + ", NanoCollisionEffect")

		if not pShip or not hasattr(pShip, "GetObjID"):
			return

		iShipID = pShip.GetObjID()

		pShip = App.ShipClass_GetObjectByID(None, iShipID)
		if not pShip: # or pShip.IsDead():
			return

		pSet = pShip.GetContainingSet()
		if not pSet:
			return
		actionsAdded = 0
		fSize     = pShip.GetRadius()
		pAttachTo = pSet.GetEffectRoot()
		pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())
		pSequence = App.TGSequence_Create()
		###
		### Get the collision points ###
		for iPoint in range( pEvent.GetNumPoints() ):
			vEmitPos = pEvent.GetPoint(iPoint)
			vEmitDir = App.TGPoint3_GetRandomUnitVector()

			### Add an explosion at this point ###
			sFile = ExpFX.GetNanoGfxFile("ExplosionGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")
			pCollision = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, None, pAttachTo, fSize, vEmitPos, vEmitDir)
			if pCollision:
				pSequence.AddAction(pCollision)
				actionsAdded = actionsAdded + 1
			pSound = ExpFX.CreateNanoSoundSeq(pShip, "ExpCollisionSfx")
			if pSound:
				pSequence.AddAction(pSound)
				actionsAdded = actionsAdded + 1
		###

		if actionsAdded == 0:
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
		pSequence.Play()
		###
		pShip.CallNextHandler(pEvent)

	ExpFX.NanoCollisionEffect = NewNanoCollisionEffect
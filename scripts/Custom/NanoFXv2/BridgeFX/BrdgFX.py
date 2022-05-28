from bcdebug import debug
###############################################################################
##	Filename:	BrdgFX.py
##	
##	Nano's Bridge Effects Enhancements Version 0.1 (No real Changes, just Optimized Game Performance)
##	
##	Created:	03/14/2003 - NanoByte a.k.a Michael T. Braams
###############################################################################
import App
import Foundation
import Custom.NanoFXv2.NanoFX_Lib
import Custom.NanoFXv2.NanoFX_Config
import Custom.NanoFXv2.NanoFX_ScriptActions

g_GfxSet		= { "DebrisGfx"  : Foundation.GetFileNames("scripts/Custom/NanoFXv2/ExplosionFX/Gfx/Debris", 'tga'),
					"ExpFlashGfx" : Foundation.GetFileNames("scripts/Custom/NanoFXv2/ExplosionFX/Gfx/ExpFlash", 'tga'),
				    "ExplosionGfx" : Foundation.GetFileNames("scripts/Custom/NanoFXv2/BridgeFX/Gfx/Explosions", 'tga'),
					"ParticleGfx"  : Foundation.GetFileNames("scripts/Custom/NanoFXv2/ExplosionFX/Gfx/Particles", 'tga')
				  }

g_ParticleControl = 0
CONST_MAXPARTICLES = Custom.NanoFXv2.NanoFX_Config.bFX_ParticleControl

###############################################################################
## Get Explosion File,  Random pick of Explosions
###############################################################################
def GetNanoGfxFile(sGfxSet, sFolderPath):
	
	debug(__name__ + ", GetNanoGfxFile")
	if len(g_GfxSet[sGfxSet]) > 0:
		iRandom = App.g_kSystemWrapper.GetRandomNumber(len(g_GfxSet[sGfxSet]))

		strFile = sFolderPath + g_GfxSet[sGfxSet][iRandom]
	
		return strFile
	
###############################################################################
## Control the Number of Particles being displayed at once so BC doesn't get
## bogged down or even CRASH!
###############################################################################	
def ControlParticles(pAction, iNum):
	
	debug(__name__ + ", ControlParticles")
	global g_ParticleControl
	g_ParticleControl = g_ParticleControl + iNum
	#print g_ParticleControl
		
	return 0
	
###############################################################################
## ExpSpark Sequence (Produce Effect Level based on NanoFX_Config)
###############################################################################
def CreateExpSparkSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir, fSpeed = 1, vGravity = None):

	### Create Sequence Object ###
	debug(__name__ + ", CreateExpSparkSeq")
	pSequence = App.TGSequence_Create()
	###
	for iNum in range(Custom.NanoFXv2.NanoFX_Config.bFX_ExpSparkFXLevel):
		if g_ParticleControl < CONST_MAXPARTICLES:
			sFile = GetNanoGfxFile("ParticleGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/Particles/")
			if not sFile:
				return pSequence
			fRandomSize = App.g_kSystemWrapper.GetRandomNumber(10)
			fVelocity = 1.0 + App.g_kSystemWrapper.GetRandomNumber(fSize * 100 + fRandomSize) * 0.01 - 0.2
			fVelocity = fVelocity * fSpeed
			pSparks = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, fEmitVel = fVelocity, fVariance = 150.0, fDamping = 0.4, vGravity = vGravity, sType = "ExpSparks")
			pSequence.AddAction(pSparks)
			ControlParticles(None, 1)
			pSequence.AddAction(App.TGScriptAction_Create(__name__, "ControlParticles", -1), App.TGAction_CreateNull(), 4.0)			
	###
	return pSequence
	
###############################################################################
## DamageSpark Sequence (Produce Effect Level based on NanoFX_Config)
###############################################################################
def CreateDamageSparkSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir, fSpeed = 1, vGravity = None):

	### Create Sequence Object ###
	debug(__name__ + ", CreateDamageSparkSeq")
	pSequence = App.TGSequence_Create()
	fDuration = Custom.NanoFXv2.NanoFX_Config.bFX_DamageSparkFXDuration
	###
	for iNum in range(Custom.NanoFXv2.NanoFX_Config.bFX_DamageSparkFXLevel):
		if g_ParticleControl < CONST_MAXPARTICLES:
			sFile = GetNanoGfxFile("ParticleGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/Particles/")
			fVelocity = (App.g_kSystemWrapper.GetRandomNumber(5) + 1) * 0.1
			fVelocity = fVelocity * fSpeed
			pSparks = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, fLifeTime = fDuration, fEmitVel = fVelocity, fVariance = 150.0, fDamping = 1.5, vGravity = vGravity, sType = "DamageSparks")
			pSequence.AddAction(pSparks)
			ControlParticles(None, 1)
			pSequence.AddAction(App.TGScriptAction_Create(__name__, "ControlParticles", -1), App.TGAction_CreateNull(), fDuration)			
	###
	return pSequence
	
###############################################################################
## Debris Sequence (Produce Effect Level based on NanoFX_Config)
###############################################################################
def CreateNanoDebrisSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir, fSpeed = 1, vGravity = None):

	### Create Sequence Object ###
	debug(__name__ + ", CreateNanoDebrisSeq")
	pSequence = App.TGSequence_Create()
	fDuration = 3.0
	###
	for iNum in range(Custom.NanoFXv2.NanoFX_Config.eFX_DebrisFXLevel):
		if g_ParticleControl < CONST_MAXPARTICLES:
			sFile = GetNanoGfxFile("DebrisGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/Debris/")
			fRandomSize = App.g_kSystemWrapper.GetRandomNumber(5) + 5
			fVelocity = 1.0 + App.g_kSystemWrapper.GetRandomNumber(fSize * 100 + fRandomSize) * 0.01
			fVelocity = fVelocity * fSpeed
			pDebris = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, bInheritVel = 1, fLifeTime = fDuration, fEmitVel = fVelocity, fVariance = 150.0, fDamping = 0.1, vGravity = vGravity, sType = "Debris")
			pSequence.AddAction(pDebris)
			ControlParticles(None, 1)
			pSequence.AddAction(App.TGScriptAction_Create(__name__, "ControlParticles", -1), App.TGAction_CreateNull(), fDuration)
	###
	return pSequence


def CreateSmoke (fDuration):
	# create smoke
	debug(__name__ + ", CreateSmoke")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridgeObject = App.BridgeObjectClass_GetObject (pSet, "bridge")
	if (pBridgeObject):
		pSequence = App.TGSequence_Create()
		pAction = App.BridgeEffectAction_CreateSmoke (fDuration, 1.5, 0.01, pBridgeObject, None, "data/sphere.tga")
		pController = pAction.GetController ()

		# Setup some default values for velocity, colors and alpha
		# Time zero.
		pController.AddColorKey (0.0, 0.8, 0.8, 0.8)
		pController.AddAlphaKey (0.0, 0.75)
		pController.AddSizeKey (0.0, 2.5)

		# End of life.
		pController.AddAlphaKey (1.0, 0.0)
		pController.AddSizeKey (1.0, 20.0)
		pController.SetEmitVelocity (40)
		pController.SetAngleVariance (60)
		
		pcHardpointName = pAction.GetHardpointName ()

		pBridgeObject.DoCrewReactions (pcHardpointName)
		pBridgeObject.FlickerLCARs(1.0)

		###

		pSequence.AddAction(pAction)
		#pSequence.Play()

def CreateSpark (fDuration):
	# create spark
	debug(__name__ + ", CreateSpark")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridgeObject = App.BridgeObjectClass_GetObject (pSet, "bridge")

	if (pBridgeObject):
		pSequence = App.TGSequence_Create()
		pAction = App.BridgeEffectAction_CreateSparks (fDuration, fDuration - 0.005 * 40, 0.005, pBridgeObject, None, "data/spark.tga")
		pController = pAction.GetSparkController ()

		# Setup some default values for velocity, colors and alpha
		pController.AddColorKey (0.0, 1.0, 1.0, 1.0)
		pController.AddColorKey (0.5, 1.0, 1.0, 0.6)
		pController.AddColorKey (1.0, 1.0, 0.7, 0.7)
		
		pController.AddAlphaKey (0.0, 1.0)
		pController.AddAlphaKey (0.5, 1.0)
		pController.AddAlphaKey (1.0, 0.0)

		pController.AddSizeKey (0.0, 0.35)

		pController.SetEmitVelocity (150.0)
		pController.SetGravity (0.0, 0.0, -150.0)
		pController.SetTailLength (10.0)

		###

		pSequence.AddAction(pAction)
		pSequence.AppendAction(App.TGScriptAction_Create("Custom.NanoFXv2.NanoFX_ScriptActions", "DestroyTGSequence", pSequence))
		pSequence.SetUseRealTime(1)
		pSequence.Play()
		
		pcHardpointName = pAction.GetHardpointName ()

		pBridgeObject.DoCrewReactions (pcHardpointName)
		pBridgeObject.FlickerLCARs(1.0)

	return

def CreateExplosion (fDuration):
	# Create explosion
	debug(__name__ + ", CreateExplosion")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridgeObject = App.BridgeObjectClass_GetObject (pSet, "bridge")
	
	if (pBridgeObject):
		# Create sequence
		pAttachTo = pBridgeObject.GetNode()
		vEmitPos = App.NiPoint3(0, 0, 0)
		vEmitDir = App.NiPoint3(0, 0, 150)
		vGravity = App.TGPoint3()
		vGravity.SetXYZ(0, 0, -150)
		fSize     = pBridgeObject.GetRadius() * 0.05

		pSequence = App.TGSequence_Create()
		
		# disabled in KM -> too many crashes
		iFun = 0 # 3
		for iPoint in range( iFun ):
			debug(__name__ + ", CreateExplosion loop %d" % iPoint)
			pEmitFrom = pBridgeObject.GetRandomPointOnModel()
			
			fSpeed = 5.0
			pSparks = CreateExpSparkSeq(fSize * 2.0, pEmitFrom, pAttachTo, vEmitPos, vEmitDir, fSpeed, vGravity)
			pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.5)
			
			fSpeed = 100.0
			pSparks = CreateDamageSparkSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir, fSpeed, vGravity)
			pSequence.AddAction(pSparks)
			
			fSpeed = 10.0
			pDebris = CreateNanoDebrisSeq(fSize * 1.25, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir, fSpeed, vGravity)
			pSequence.AddAction(pDebris, App.TGAction_CreateNull(), 0.5)
			
			#pSequence.AddAction(App.TGScriptAction_Create("Custom.NanoFXv2.NanoFX_ScriptActions", "NanoDamageShip", pBridgeObject, pEmitFrom, fSize / 3.0, 1200.0), App.TGAction_CreateNull(), 0.3)
			
			sFile = GetNanoGfxFile("ExplosionGfx", "scripts/Custom/NanoFXv2/BridgeFX/Gfx/Explosions/")
			pExplosion = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, iTiming = 24.0, fBrightness = 0.6)
			pSequence.AddAction(pExplosion)
			
			sFile = GetNanoGfxFile("ExpFlashGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/ExpFlash/")
			pFlash = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, iTiming = 8.0, fBrightness = 0.6)
			pSequence.AddAction(pFlash)
			
			iNumPlume = 3
			for iPoint in range( iNumPlume ):
				sFile = GetNanoGfxFile("ExplosionGfx", "scripts/Custom/NanoFXv2/BridgeFX/Gfx/Explosions/")
				pExplosion = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize * 0.50, vEmitPos, vEmitDir, fVariance = 150.0, iTiming = 16.0, sType = "Plume")
				pSequence.AddAction(pExplosion)
				sFile = GetNanoGfxFile("ExpFlashGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/ExpFlash/")
				pFlash = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, iTiming = 4.0, fBrightness = 0.6)
				pSequence.AddAction(pFlash)
				fSpeed = 5.0
				pSparks = CreateExpSparkSeq(fSize * 2.0, pEmitFrom, pAttachTo, vEmitPos, vEmitDir, fSpeed, vGravity)
				pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.5)
				fSpeed = 100.0
				pSparks = CreateDamageSparkSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir, fSpeed, vGravity)
				pSequence.AddAction(pSparks)
				fSpeed = 10.0
				pDebris = CreateNanoDebrisSeq(fSize * 1.25, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir, fSpeed, vGravity)
				pSequence.AddAction(pDebris, App.TGAction_CreateNull(), 0.5)
			
			###	
	
		#pSequence.SetUseRealTime(1)
		pSequence.AppendAction(App.TGScriptAction_Create("Custom.NanoFXv2.NanoFX_ScriptActions", "DestroyTGSequence", pSequence), 1.0)
		pSequence.Play ()
	debug(__name__ + ", CreateExplosion End")

LOCK_NanoBridgeHit = 0
def NanoBridgeHit (fCurHullPercent):
	
	debug(__name__ + ", NanoBridgeHit")
	global LOCK_NanoBridgeHit
	LOCK_NanoBridgeHit = 1
	if Custom.NanoFXv2.NanoFX_Config.bFX_Enabled == 0:
		return
		
	pSet = App.g_kSetManager.GetSet ("bridge")
	if not pSet:
		return

	pCamera = App.ZoomCameraObjectClass_GetObject (pSet, "maincamera")
	if not pCamera:
		return
		
	if (fCurHullPercent > 0.85):
		# Light damage.  Do sparks most of the time, occasionally steam
		r = App.g_kSystemWrapper.GetRandomNumber (100)
		#if (r < 20):
			#CreateSmoke (5)		# 5 seconds of smoke
		#else:
	#CreateSpark (1.0)
		CreateExplosion (15)
		SparkSound()
		# Shake the camera also.
		pCamera.SetShake (1.0, 1.0)
	elif (fCurHullPercent > 0.70):
		# Moderate damage
		#r = App.g_kSystemWrapper.GetRandomNumber (100)
#		if (r < 50):
#			CreateSmoke (10)

		# always create sparks
		#CreateSpark (1.5)
		CreateExplosion (15)
		SparkSound()

		# Shake the camera also.
		pCamera.SetShake (2.0, 1.0)
	else:
		# Heavy damage
		# Do explosions, steam, and sparks.
		#CreateSmoke (10)
		#CreateSpark (2.00)
		CreateExplosion (15)
		SparkSound()

		# Shake the camera also.
		pCamera.SetShake (3.0, 3.0)

	###
	LOCK_NanoBridgeHit = 0
	debug(__name__ + ", NanoBridgeHit End")

def SparkSound():
	# Don't do anything if the rendered set isn't the bridge.
	debug(__name__ + ", SparkSound")
	try:
		if App.g_kSetManager.GetRenderedSet().GetName() != "bridge":
			debug(__name__ + ", SparkSound Return 1")
			return
	except AttributeError:
		debug(__name__ + ", SparkSound Return 2")
		return

	# How long has it been since the last spark sound?  These sounds
	# are very distinctive, and we don't want them constantly playing
	# whenever the bridge shows damage.
	global g_fNextSpark
	fCurrentTime = App.g_kUtopiaModule.GetRealTime()
	try:
		if g_fNextSpark > fCurrentTime:
			debug(__name__ + ", SparkSound Return 3")
			return
	except NameError:
		pass

	g_fNextSpark = fCurrentTime + (App.g_kSystemWrapper.GetRandomNumber(2000) / 1000.0)

	import LoadTacticalSounds
	sSound = LoadTacticalSounds.GetRandomSound(g_lsSparks)
	pSound = App.g_kSoundManager.GetSound(sSound)
	if pSound:
		pSound.Play()
	debug(__name__ + ", SparkSound End")
	###

g_lsSparks = ( "ConsoleExplosion1", "ConsoleExplosion2",
			   "ConsoleExplosion3", "ConsoleExplosion4",
			   "ConsoleExplosion5", "ConsoleExplosion6",
			   "ConsoleExplosion7", "ConsoleExplosion8" )

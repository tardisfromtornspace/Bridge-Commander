from bcdebug import debug
###############################################################################
##	Filename:	NanoFX_ScriptActions.py
##
##	NanoFX Scripting Actions version 2.0
##
##	Created:	10/29/2003 - NanoByte a.k.a Michael T. Braams
###############################################################################
import App
import Custom.NanoFXv2.NanoFX_Config

###############################################################################
## Help BC clean up after itself by Deleting a TGSequence that has been Played
###############################################################################
def DestroyTGSequence(pAction, pSequence):
	return 0	
	debug(__name__ + ", DestroyTGSequence")
	if pSequence:
		pSequence.Destroy()
	debug(__name__ + ", DestroyTGSequence END")
	return 0

###############################################################################
## Set Game Speed...... useful for doing Slow Mo Effects or to Speed up game
###############################################################################
def SetGameSpeed(pAction, fSpeed):
	
	debug(__name__ + ", SetGameSpeed")
	import SimpleAPI
	SimpleAPI.Speed(fSpeed)
	
	return 0

###############################################################################
## Turn Off Lights
###############################################################################
def TurnOffLights(pAction, pObject):

	### Turn off Glows ###
	debug(__name__ + ", TurnOffLights")
	debug(__name__ + ", TurnOffLights Status: %d %d" % (pObject.IsDying(), pObject.IsDead()))
	if not pObject.IsDead():
		pObject.DisableGlowAlphaMaps()
	debug(__name__ + ", TurnOffLights DONE")
	###
	return 0
	###

###############################################################################
## Turn On Lights
###############################################################################
def TurnOnLights(pAction):

	### Quickly Turn off Game Glow Maps then Back on ###
	debug(__name__ + ", TurnOnLights")
	if Custom.NanoFXv2.NanoFX_Config.eFX_FixBrightGlows == "On":
		if (App.g_kLODModelManager.AreSpecularMapsEnabled() == 1):
			App.g_kLODModelManager.SetSpecularMapsEnabled(0)
	if (App.g_kLODModelManager.AreGlowMapsEnabled() == 1):
		App.g_kLODModelManager.SetGlowMapsEnabled(0)
		if App.g_kLODModelManager.GetDropLODLevel() == 0: # else the game will crash on not high graphics
			App.g_kLODModelManager.SetGlowMapsEnabled(1)
	###
	debug(__name__ + ", TurnOnLights Done")
	return 0
	###

###############################################################################
## Damage the Model
###############################################################################
def NanoDamageShip(pAction, pObject, vEmitPos, fRadius, fDamage):

	### Put Holes in our Model ###
	debug(__name__ + ", NanoDamageShip")
	pObject = App.DamageableObject_GetObjectByID(None, pObject.GetObjID())
	if pObject:
		pObject.AddDamage(vEmitPos, fRadius * 0.4, fDamage)
	debug(__name__ + ", NanoDamageShip Done")
	###
	return 0
	###

###############################################################################
## Random Rotation & Speed...
###############################################################################
def SetNanoRotation(pAction, pShip, fRotation, fSpeed):

	### Create some vectors ###
	debug(__name__ + ", SetNanoRotation")
	vNewVelocity = App.TGPoint3()
	
	pShip = App.DamageableObject_GetObjectByID(None, pShip.GetObjID())
	if not pShip:
		debug(__name__ + ", SetNanoRotation Return")
		return 0
	###
	### Set Speed ###
	if (fSpeed):
		vNewVelocity.SetX(fSpeed)
		vNewVelocity.SetY(fSpeed)
		vNewVelocity.SetZ(fSpeed)
		pShip.SetVelocity(vNewVelocity)
	###
	### Set it to a random spin direction... ###
	if (fRotation):
		vNewVelocity.SetX((App.g_kSystemWrapper.GetRandomNumber(20001) - 10000) / 10000.0)
		vNewVelocity.SetY((App.g_kSystemWrapper.GetRandomNumber(20001) - 10000) / 10000.0)
		vNewVelocity.SetZ((App.g_kSystemWrapper.GetRandomNumber(20001) - 10000) / 10000.0)
		###
		### Add New Velocity to Current Velocity ###
		vCurVelocity = pShip.GetAngularVelocityTG()
		vCurVelocity.Add(vNewVelocity)
		###
		### Set the length to the specified speed ###
		vCurVelocity.Unitize()
		vCurVelocity.Scale( fRotation * App.HALF_PI / 180.0 )
		pShip.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_WORLD_SPACE)
		###
	###
	debug(__name__ + ", SetNanoRotation Done")
	return 0
	###
	
###############################################################################
## NanoFX Effect Controller
###############################################################################
def CreateControllerFX( sFile, 
						pEmitFrom, 
						pAttachTo,
						fSize       = 1.0,
						vEmitPos    = App.NiPoint3(0, 0, 0),
						vEmitDir    = App.NiPoint3(0, 0, 0),
						bInheritVel = 0, 
						bDetach     = 0,
						fFrequency  = 0.2,   
						fLifeTime   = 0.1,
						fEmitVel    = None,
						fVariance   = None,
						fDamping    = None,
						vGravity    = None,
						iTiming     = 32,
						sType	    = "Normal",
						fRed	    = 255.0,
						fGreen      = 255.0,
						fBlue       = 255.0,
						fBrightness = 0.6):

	### Setup Controller Type ###
	debug(__name__ + ", CreateControllerFX")
	pController = SetupController(sType, fSize, fLifeTime, fRed, fGreen, fBlue, fBrightness)
	
	###
	### Setup Animation ###
	fSpeed = iTiming / 15.0
	
	if sType != "ExpSparks" and sType != "DamageSparks" and sType != "Debris":
		pController.SetEmitLife(fSpeed)
		pController.SetEmitFrequency(fFrequency)
		pController.SetEffectLifeTime(fSpeed + fLifeTime)
	###
	debug(__name__ + ", CreateControllerFX file %s" % sFile)
	pController.CreateTarget(sFile)
	###
	### Setup Properties ###
	
	if fEmitVel:
		pController.SetEmitVelocity(fEmitVel)
	if fVariance:
		pController.SetAngleVariance(fVariance)
		pController.SetEmitRadius(fSize / 4.0)
	if fDamping:
		pController.SetDamping(fDamping)
	if vGravity:
		pController.SetGravity(vGravity.GetX(), vGravity.GetY(), vGravity.GetZ())
	if sType != "Plume" and sType != "ExpSparks" and sType != "DamageSparks" and sType != "Debris":
		if sType == "Blinker" or sType == "StaticBlinker" or sType == "Plasma" or sType == "Normal":
			pController.SetTargetAlphaBlendModes(0, 0)
		else:
			pController.SetTargetAlphaBlendModes(0, 7)
	if pEmitFrom:
		pController.SetEmitFromObject(pEmitFrom)
	pController.SetEmitPositionAndDirection(vEmitPos, vEmitDir)
	pController.SetInheritsVelocity(bInheritVel)
	pController.SetDetachEmitObject(bDetach)
	pController.AttachEffect(pAttachTo)
	###
	debug(__name__ + ", CreateControllerFX Done")
	return App.EffectAction_Create(pController)
	###

###############################################################################
## Setup Controller Type
###############################################################################
def SetupController(sType, fSize, fLifeTime, fRed, fGreen, fBlue, fBrightness):
	
	### Create Controller based on Type ###
	debug(__name__ + ", SetupController")
	if (sType == "Normal" or sType == "Plasma"):
		pController = App.AnimTSParticleController_Create()
		###
		### Setup Alpha Colors ###
		pController.AddColorKey(0.1, 1.0, 1.0, 1.0)
		pController.AddColorKey(fBrightness, fRed / 255, fGreen / 255, fBlue / 255)
		pController.AddColorKey(1.0, 0.0, 0.0, 0.0)
		###
		pController.AddAlphaKey(0.0, 1.0)
		pController.AddAlphaKey(0.7, 0.5)
		pController.AddAlphaKey(1.0, 0.0)
		###
		### Setup Sizes ###
		fRandSize = App.g_kSystemWrapper.GetRandomNumber(10) * 0.01
		pController.AddSizeKey(0.0, 1.0 * fSize + fRandSize)
		pController.AddSizeKey(1.0, 1.0 * fSize + fRandSize)
	###
	if (sType == "Plume"):
		pController = App.ExplosionPlumeController_Create()
		###
		### Setup Alpha Colors ###
		### Setup Plume Effect ###
		pController.AddColorKey(0.0, fRed / 255, fGreen / 255, fBlue / 255)
		pController.AddColorKey(1.0, 0.0, 0.0, 0.0)
		###
		pController.AddAlphaKey(0.0, 1.0)
		pController.AddAlphaKey(0.7, 0.5)
		pController.AddAlphaKey(1.0, 0.0)
		### Setup Sizes ###
		fRandSize = App.g_kSystemWrapper.GetRandomNumber(20) * 0.01
		pController.AddSizeKey(0.0, 1.0 * fSize + fRandSize)
		pController.AddSizeKey(1.0, 1.0 * fSize + fRandSize)
	###
	if (sType == "Blinker"):
		pController = App.AnimTSParticleController_Create()
		###
		### Setup Alpha Colors ###
		### Setup Plume Effect ###
		pController.AddColorKey(0.0, fRed / 255, fGreen / 255, fBlue / 255)
		pController.AddColorKey(1.0, 0.0, 0.0, 0.0)
		###
		pController.AddAlphaKey(0.0, 1.0)
		pController.AddAlphaKey(1.0, 1.0)
		### Setup Sizes ###
		pController.AddSizeKey(0.0, fSize)
		pController.AddSizeKey(1.0, fSize)
	###
	if (sType == "StaticBlinker"):
		pController = App.AnimTSParticleController_Create()
		###
		### Setup Alpha Colors ###
		### Setup Plume Effect ###
		pController.AddColorKey(0.0, fRed / 255, fGreen / 255, fBlue / 255)
		pController.AddColorKey(1.0, fRed / 255, fGreen / 255, fBlue / 255)
		###
		pController.AddAlphaKey(0.0, 1.0)
		pController.AddAlphaKey(1.0, 1.0)
		### Setup Sizes ###
		pController.AddSizeKey(0.0, fSize)
		pController.AddSizeKey(1.0, fSize)
	###
	if (sType == "Debris"):
		### Create Controller ###
		fEmitRate = 0.005
		fDuration = fLifeTime
		pController = App.DebrisParticleController_Create(fDuration * (1.1295 - fDuration * 0.00003) + (App.g_kSystemWrapper.GetRandomNumber(10) * 0.001), fDuration, fEmitRate)
		pController.SetEmitLifeVariance(fDuration / 4.0)
		###
		# Setup some default values for velocity, colors and alpha
		pController.AddColorKey(0.0, 1.0, 1.0, 1.0)
		pController.AddColorKey(1.0, 0.0, 0.0, 0.0)
		###
		pController.AddAlphaKey(0.0, 0.8 + App.g_kSystemWrapper.GetRandomNumber(3) * 0.1)
		pController.AddAlphaKey(1.0, 0.0)
		###
		fRandomSize = App.g_kSystemWrapper.GetRandomNumber(5) + 5
		pController.AddSizeKey(0.0, 0.01)
		pController.AddSizeKey(0.2, fRandomSize * fSize * 0.01)
		pController.AddSizeKey(0.7, fRandomSize * fSize * 0.01)
		pController.AddSizeKey(1.0, 0.01)
		###
	if (sType == "ExpSparks") or (sType == "DamageSparks"):	
		### Create Controller ###
		if sType == "ExpSparks":
			fEmitRate = 0.005
			fDuration = 3.0 + App.g_kSystemWrapper.GetRandomNumber(100) * 0.01
			pController = App.SparkParticleController_Create(fDuration * 1.1345 + (App.g_kSystemWrapper.GetRandomNumber(25) * 0.001), fDuration, fEmitRate)
			pController.SetTailLength(0.05 * (App.g_kSystemWrapper.GetRandomNumber(2) + 1))
		else:
			fEmitRate = 0.5
			fDuration = fLifeTime
			pController = App.SparkParticleController_Create(fDuration, 1.0, fEmitRate)
			pController.SetTailLength(0.02)
		###
		# Setup some default values for velocity, colors and alpha
		pController.SetEmitLifeVariance(fDuration / 4.0)
		pController.AddColorKey(0.0, 1.0, 1.0, 0.9)
		pController.AddColorKey(0.6, 1.0, 0.8, 0.5)
		pController.AddColorKey(1.0, 0.5, 0.2, 0.0)
		###
		pController.AddAlphaKey(0.0, 1.0)
		pController.AddAlphaKey(0.6, 0.5)
		pController.AddAlphaKey(1.0, 0.0)
		###
		fRandomSize = App.g_kSystemWrapper.GetRandomNumber(10)
		pController.AddSizeKey(0.0, 0.01)
		pController.AddSizeKey(0.2, 0.03 * fSize * 0.75)
		pController.AddSizeKey(0.8, 0.05 * fSize * 0.75)
		pController.AddSizeKey(1.0, 0.01)
		###
	if (sType == "Atmosphere"):
		pController = App.AnimTSParticleController_Create()
		###
		### Setup Alpha Colors ###
		pController.AddColorKey(0.0, fRed / 255, fGreen / 255, fBlue / 255)
		pController.AddColorKey(1.0, 0.0, 0.0, 0.0)
		pController.AddAlphaKey(0.0, 1.0)
		pController.AddAlphaKey(1.0, 1.0)
		###
		### Setup Sizes ###
		pController.AddSizeKey(0.0, 2.0 * fSize)
		pController.AddSizeKey(1.0, 2.0 * fSize)
		###
	###
	debug(__name__ + ", SetupController Done")
	return pController
	###

###############################################################################
## End of NanoFX Script Actions
###############################################################################
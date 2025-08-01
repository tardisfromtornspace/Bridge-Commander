# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# OriBeam.py
# I wanted to create a trail script like Lost_Jedi's but allowing more customization from the projectile's side while still being compatible with the syntax Lost_Jedi used so people could use it on one projectile or another without needing to change projectile inner trail-call syntax, thus the same names and needing some similar stuff including global variables names in case someone ever used them on a script.
# 1st August 2025
#################################################################################################################
#
MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "1.01",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }
#
#################################################################################################################
#

# Imports and global variables
import App

# Lost_Jedi's version had these globals so, yeah, in case somebody used them on a script, so at least this script is compatible with those.
__author__      = MODINFO["Author"]
__copyright__   = ""
__license__     = MODINFO["License"]
__version__     = MODINFO["Version"]
__notes__       = MODINFO["Description"]

# Some extra defaults, these are new:
g_sTexture = "scripts/Custom/NanoFXv2/SpecialFX/Gfx/Plasma/Plasma.tga"
g_fFrequency = 0.001
g_fVelocity = 0.01
g_sAngleVariance = 60.0
g_sEmitLife = 4.0
g_sEffectLifetime = 12.0
g_sDrawOldToNew = 0
g_sTargetAb1 = 0
g_sTargetAb2 = 0
g_dCenter = App.NiPoint3(0, 0, 0)

# Another global variable with same name as LJ's to keep backwards compatibility
global lLoadedTexturesCache
lLoadedTexturesCache = [g_sTexture]

# Load function - picked from other LoadGFX scripts, renamed to fit with Lost_Jedi's function name, and then added cache support like LJ's
def LoadTexture(sTexturePath = None, iNumXFrames = 1, iNumYFrames = 1):
	global lLoadedTexturesCache
	if (sTexturePath in lLoadedTexturesCache):
		return sTexturePath
	fX = 0.0
	fY = 0.0
	if sTexturePath:
		pContainer = App.g_kTextureAnimManager.AddContainer(sTexturePath)
		if pContainer:
			pTrack = pContainer.AddTextureTrack(iNumXFrames * iNumYFrames)
			for index in range(iNumXFrames * iNumYFrames):
				pTrack.SetFrame(index, fX, fY + (1.0 / iNumYFrames), fX + (1.0 / iNumXFrames), fY)
				fX = fX + (1.0 / iNumXFrames)
				if (fX == 1.0):
					fX = 0.0
					fY = fY + (1.0 / iNumYFrames)
	lLoadedTexturesCache.append(sTexturePath)
	return sTexturePath


# Aux functions - for getting the NiAVNode, EffectRoot and EffectSequence without bugging
def GetNIAVNode(pObject):
	leNode = None
	if pObject and hasattr(pObject, "GetNode"):
		leNode = pObject.GetNode()
	return App.TGModelUtils_CastNodeToAVObject(leNode)

def GetSetEffectRoot(pObject):
	myEfRoot = None
	if pObject != None and hasattr(pObject, "GetContainingSet"):
		pSet = pObject.GetContainingSet()
		if pSet != None and hasattr(pSet, "GetEffectRoot"):
			myEfRoot = pSet.GetEffectRoot()
	return myEfRoot

def CreateEffectSequence(pEffect):
	# Creates and adds to a sequence, preventing some sequence issues
	pSequence = None
	if pEffect:
		pSequence = App.TGSequence_Create()
		pSequence.AddAction(pEffect)
	return pSequence

# Event-related functions
def AddInstanceHandler(pObject, sFunction, iEventType):
	if pObject != None:
		pObject.AddPythonFuncHandlerForInstance(iEventType, sFunction)

def AddCreationHandler(pObject, sFunction):
	AddInstanceHandler(pObject, sFunction, App.ET_TORPEDO_ENTERED_SET)

def AddHitHandler(pObject, sFunction):
	AddInstanceHandler(pObject, sFunction, App.ET_WEAPON_HIT)            
       

# Effects
# This function below is there so people can customize it from their own files
def DefaultColorKeyFunc(pEffect, fSize):
	pEffect.AddColorKey(0.1, 1.0, 0.8, 0.1)
	pEffect.AddColorKey(1.0, 0.996863, 0.904510, 0.137255)
	pEffect.AddColorKey(1.0, 0.0, 0.0, 0.0)

	pEffect.AddAlphaKey(0.0, 1.0)
	pEffect.AddAlphaKey(0.7, 0.5)
	pEffect.AddAlphaKey(1.0, 0.0)

	pEffect.AddSizeKey(0.0, 0.016 * fSize)
	pEffect.AddSizeKey(0.1, 0.23 * fSize)
	pEffect.AddSizeKey(1.0, 0.16 * fSize)

def CreateSmokeHigh(sTexture, fFrequency, fVelocity, fSize, pEmitFrom, kEmitPos, kEmitDir, pAttachTo, sAngleVariance = 60.0, sEmitLife = 4.0, sEffectLifetime = 12.0, sDrawOldToNew = 0, sTargetAb1 = 0, sTargetAb2 = 0, pFunc = DefaultColorKeyFunc):
	pEffectD = None
	try:
		pEffect = App.AnimTSParticleController_Create()

		## Setup colour and alpha

		pFunc(pEffect, fSize)

		## Setup properties
		pEffect.SetEmitVelocity(fVelocity)
		pEffect.SetAngleVariance(sAngleVariance)
		pEffect.SetEmitLife(sEmitLife)
		pEffect.SetEmitFrequency(fFrequency)
		pEffect.SetEffectLifeTime(sEffectLifetime)
		pEffect.SetDrawOldToNew(sDrawOldToNew)
		pEffect.CreateTarget(sTexture)
		pEffect.SetTargetAlphaBlendModes(sTargetAb1, sTargetAb2)
		pEffect.SetEmitFromObject(pEmitFrom)
		pEffect.SetEmitPositionAndDirection(kEmitPos, kEmitDir)	
		pEffect.AttachEffect(pAttachTo)
		pEffectD = App.EffectAction_Create(pEffect)

	except:
		print "OriBeam trail: error while calling CreateSmokeHigh:"
		traceback.print_exc()
		pEffectD = None

	return pEffectD

# Something like what LJ dubbed "Common" function to call, but more customizable.
def SetupSmokeTrail(pTorpedo, sTexture = g_sTexture, fFrequency = g_fFrequency, fVelocity = g_fVelocity, fSize = None, kEmitPos = g_dCenter, kEmitDir = g_dCenter, sAngleVariance = g_sAngleVariance, sEmitLife = g_sEmitLife, sEffectLifetime = g_sEffectLifetime, sDrawOldToNew = g_sDrawOldToNew, sTargetAb1 = g_sTargetAb1, sTargetAb2 = g_sTargetAb2, pFunction = DefaultColorKeyFunc):

	pEffectRoot = GetSetEffectRoot(pTorpedo)
	if pEffectRoot:
		pEmitFrom   = GetNIAVNode(pTorpedo)
		if pEmitFrom:
			efSize = 1.0
			if fSize != None:
				efSize = fSize
			elif pTorpedo and hasattr(pTorpedo, "GetRadius"):
				efSize = pTorpedo.GetRadius() * 3

			pAction = None
			try:
				pAction = CreateSmokeHigh(sTexture, fFrequency, fVelocity, efSize, pEmitFrom, kEmitPos, kEmitDir, pEffectRoot, sAngleVariance, sEmitLife, sEffectLifetime, sDrawOldToNew, sTargetAb1, sTargetAb2, pFunction)
			except:
				print "OriBeam trail: error while calling SetupSmokeTrail:"
				traceback.print_exc()
				pAction = None
			if pAction:
				pSequence = App.TGSequence_Create()
				pSequence.AddAction(pAction)
				pSequence.Play()
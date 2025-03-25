# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# ImpactTexture.py
# Modified from Effects.py (by the STBC team originally, and some modified versions by other authors like VonFrank) and SporeDrive.py by Alex SL Gato.
# 25th March 2025
#################################################################################################################
# This file contains "ShipElectricField" which will create random texture animations from a certain file around the ship, and "DriveEnterFlash" which will create detached effects on the same point with slight random sizes; alongside certain auxiliar functions to perform the deed individually and to obtain the effect root and AVNode from various sources (on GetSetEffectRoot, it expects an input Object class which has a "GetContainingSet" function, like a ship or a torpedo, but it also admits a Set, or a NiNodePtr or NiNode; while the "GetNIAVNode" expects an Object with a "GetNode" method, or an actual Ni Node).
# 
#################################################################################################################
#
MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "0.1",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }
#
#################################################################################################################
#

import App

from bcdebug import debug

import math
import string
import traceback

import LoadTextures

defaultColorKey = [100.0 / 255, 1.0 / 255, 255.0 / 255]

#Original by LJ, modified by Alex Sl Gato
def GetSetEffectRoot(pObject):
	if pObject:
		if hasattr(pObject, "GetContainingSet"):
			pSet = pObject.GetContainingSet()
			if pSet and hasattr(pSet, "GetEffectRoot"):
				return pSet.GetEffectRoot()
		elif hasattr(pObject, "GetEffectRoot"):
			return pObject.GetEffectRoot()
		elif hasattr(pObject, "__class__") and pObject.__class__ == App.NiNode:
			return pObject
	return None

#Original by LJ, modified by Alex Sl Gato
def GetNIAVNode(pObject):
	if pObject:
		if hasattr(pObject, "GetNode"):
			return App.TGModelUtils_CastNodeToAVObject(pObject.GetNode())
		else:
			try:
				valTu = App.TGModelUtils_CastNodeToAVObject(pObject)
				return valTu
			except:
				valTu = None
			return valTu
	return None

# Aux. function grabbed from VonFrank's Remastered Effects.py
def CreateElectricExplosion(fSize, fLife, pEmitFrom, bOwnsEmitFrom, pEffectRoot, fRed, fGreen, fBlue, fFrequency = 1.0, fEmitLife=1, fSpeed=2.0, sFile = 'data/Textures/Effects/ExplosionA.tga'):
	
	pExplosion = App.AnimTSParticleController_Create()

	pExplosion.AddColorKey(0.0, fRed, fGreen, fBlue)
	pExplosion.AddColorKey(0.5, fRed, fGreen, fBlue)
	pExplosion.AddColorKey(1.0, 1.0 / 255, 1.0 / 255, 1.0 / 255)

	pExplosion.AddAlphaKey(0.4, 1.0)
	pExplosion.AddAlphaKey(1.0, 1.0)

	pExplosion.AddSizeKey(0.0, 1.0 * fSize)
	pExplosion.AddSizeKey(0.2, 1.0 * fSize)
	pExplosion.AddSizeKey(0.6, 1.0 * fSize)
	pExplosion.AddSizeKey(0.9, 1.0 * fSize)

	pExplosion.SetEmitLife(fEmitLife)
	pExplosion.SetEmitFrequency(fFrequency)
	pExplosion.SetEffectLifeTime(fSpeed + fLife)
	pExplosion.CreateTarget(sFile)
	pExplosion.SetTargetAlphaBlendModes(0, 7)

	pExplosion.AttachEffect(pEffectRoot)

	pExplosion.SetEmitFromObject(pEmitFrom)
	pExplosion.SetDetachEmitObject(bOwnsEmitFrom)

	return pExplosion

# Aux function
def ShipElectricField(pAction, pShipID, sType, amount=5, sparkSize=0.05, delay=2.0, sFile = 'data/Textures/Effects/ExplosionA.tga', sFileFrameW = 8, sFileFrameH = 1, colorKey=None, rShip=None, pShipNode=None, fLife=1.0, bOwnsEmitFrom=0):
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShipID)
	if not pShip:
		return 0
	if pShip == None:
		return 0

	try:
		if colorKey == None:
			import Custom.NanoFXv2.NanoFX_Lib
			colorKey = Custom.NanoFXv2.NanoFX_Lib.GetOverrideColor(pShip, sType)
			if colorKey == None:
				colorKey = defaultColorKey
	except:
		colorKey = defaultColorKey

	iCycleCount = 1
	if amount > 0 and sparkSize > 0:
		pElectricShockSequence = App.TGSequence_Create()

		if pShipNode == None:		
			pShipNode = pShip.GetNode()
		if rShip == None:
			rShip = pShip.GetRadius()

		LoadTextures.LoadGFX(sFileFrameW, sFileFrameH, sFile)

		while (iCycleCount < amount):
			try:
				pEmitPos = pShip.GetRandomPointOnModel()
				pExplosion = CreateElectricExplosion(rShip * sparkSize, fLife, pEmitPos, bOwnsEmitFrom, pShipNode, colorKey[0], colorKey[1], colorKey[2], fFrequency = 0.09, fEmitLife=1.5, fSpeed=delay)
				pAExplosion = None
				if pExplosion != None:
					pAExplosion = App.EffectAction_Create(pExplosion)
				if pAExplosion != None:
					pElectricShockSequence.AddAction(pAExplosion, App.TGAction_CreateNull(), iCycleCount * 0.005)
			except:
				print __name__, ": error while calling ShipElectricField:"
				traceback.print_exc()
			iCycleCount = iCycleCount + 1

		pElectricShockSequence.Play()

	return 0

# Aux function
def CreateDetachedElectricExplosion(fRed, fGreen, fBlue, fSize, fLifeTime, sFile, pEmitFrom, pAttachTo, fFrequency=1,fEmitLife=1,fSpeed=1.0):
	pEffect = None
	try:     
		pEffect = App.AnimTSParticleController_Create()

		pEffect.AddColorKey(0.0, fRed, fGreen, fBlue)
		pEffect.AddColorKey(0.5, fRed, fGreen, fBlue)
		pEffect.AddColorKey(1.0, 1.0 / 255, 1.0 / 255, 1.0 / 255)

		pEffect.AddAlphaKey(0.0, 0.0)
		pEffect.AddAlphaKey(1.0, 0.0)

		pEffect.AddSizeKey(0.0, 0.8 * fSize)
		pEffect.AddSizeKey(0.2, 1.0 * fSize)
		pEffect.AddSizeKey(0.6, 1.0 * fSize)
		pEffect.AddSizeKey(0.8, 0.7 * fSize)
		pEffect.AddSizeKey(1.0, 0.1 * fSize)

		pEffect.SetEmitLife(fEmitLife)
		pEffect.SetEmitFrequency(fFrequency)
		pEffect.SetEffectLifeTime(fSpeed + fLifeTime)
		pEffect.SetInheritsVelocity(0)
		pEffect.SetDetachEmitObject(0) # If set to 1 it makes the main ship invisible LOL
		pEffect.CreateTarget(sFile)
		pEffect.SetTargetAlphaBlendModes(0, 7)

		pEffect.SetEmitFromObject(pEmitFrom)
		pEffect.AttachEffect(pAttachTo)         

		return pEffect
	except:
		print "SporeDrive TravellingMethod: error while calling CreateDetachedElectricExplosion:"
		traceback.print_exc()
		pEffect = None

	return pEffect

# Aux function. Create flash effect on a ship.
def DriveEnterFlash(pAction, pShipID, sType, amount=3, sparkSize=5, sFile = 'data/Textures/Effects/SporeDriveElectricExplosion.tga', sFileFrameW = 8, sFileFrameH = 1, colorKey=None, pAttachTo = None, pEmitFrom = None, fSize = None, fFrequency=0.09,fEmitLife=0.75,fSpeed=0.0, fLife=0.75):
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShipID)

	if (not pShip or pShip == None) and pAttachTo == None:
		return 0

	fEffectList = []
	try:
		iCycleCount = 0
		if amount > 0 and sparkSize > 0:

			try:
				if colorKey == None:
					import Custom.NanoFXv2.NanoFX_Lib
					colorKey = Custom.NanoFXv2.NanoFX_Lib.GetOverrideColor(pShip, sType)
					if colorKey == None:
						colorKey = defaultColorKey
			except:
				colorKey = defaultColorKey

			LoadTextures.LoadGFX(sFileFrameW, sFileFrameH, sFile)

			if pAttachTo == None:
				pAttachTo = GetSetEffectRoot(pShip) #pShip.GetContainingSet().GetEffectRoot()
			else:
				pAttachTo = GetSetEffectRoot(pAttachTo)
			if fSize == None:
				if pShip:
					fSize = pShip.GetRadius() * sparkSize
				else:
					fSize = sparkSize

			if pEmitFrom == None:
				pEmitFrom = GetNIAVNode(pShip)
			else:
				pEmitFrom = GetNIAVNode(pEmitFrom)

			while (iCycleCount < amount):
				try:
					rdm = (App.g_kSystemWrapper.GetRandomNumber(10) + 90) / 100.0
					pEffect = CreateDetachedElectricExplosion(colorKey[0], colorKey[1], colorKey[2], fSize * rdm, fLife, sFile, pEmitFrom, pAttachTo, fFrequency=0.09,fEmitLife=0.75,fSpeed=0.0)
					if pEffect:
						fEffect = App.EffectAction_Create(pEffect)
						if fEffect:
							fEffectList.append(fEffect)
				except:
					print __name__, ": error while calling DriveEnterFlash:"
					traceback.print_exc()

				iCycleCount = iCycleCount + 1

	except:
		print "SporeDrive TravellingMethod: error while calling SporeDriveEnterFlash:"
		traceback.print_exc()
		fEffect = None

	lenef = len(fEffectList)
	if lenef > 0:
		pSequence = App.TGSequence_Create()
		for fEffect in fEffectList:
			pSequence.AddAction(fEffect, None)
		pSequence.Play()
                
	return 0
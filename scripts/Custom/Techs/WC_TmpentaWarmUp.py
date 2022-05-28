#############################################
##					   ##
## Adonis TMP Warp Startup "Technology"    ##
## By MLeo Daalder, commissioned by Adonis ##
##					   ##
#############################################

"""
Adonis TMP Warp Startup script

Usage (mostly by example this time, sorry, had to cut it a bit due to school pressure):
Foundation.ShipDef.AdLuxor.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"grilleb_glow": {
				0.0: "data/Models/Ships/WCtmpenta/grilleb_glow.tga", 
				1.0: "data/Models/Ships/WCtmpenta/grilleb2_glow.tga",
			},

		}
	}
"""

import App
import Foundation
import FoundationTech
import string


class ListCompare:
	def __init__(self, list):
		self.list = list

	def __cmp__(self, other):# Not entirely according to convention, but it does the trick
		return not other in self.list

##################################################
##						##
## Right, this acts like a module replacement,	##
## since global variables need to be "imported"	##
## using the global keyword while globals from	##
## a module don't. Using static variables from	##
## a class give the same effect while loosing	##
## the dependance of the module.		##
##						##
##################################################
class types:
	DictionaryType = type({})
	ListType = type([])
	TupleType= type(())
	StringType = type("")
	ArrayType    = ListCompare([ListType, TupleType])
	SequenceType = ListCompare([StringType, ArrayType])
	ContainerType= ListCompare([DictionaryType, SequenceType])

types.InstanceType = type(types())

class AdonisTMPWarpStartUpDef(FoundationTech.TechDef):
	def AttachShip(self, pShip, pInstance):
		#pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		if pShip and getattr(pInstance, self.name, None):
			if not hasattr(pInstance, "TextureRegistration"):
				pInstance.TextureRegistration = {}
			if hasattr(pInstance, "NormalTextures"):
				PreProcessTextureRegistration(pInstance)
			if not getattr(pInstance, "bAddedAdonisTMPWarpHandlers", 0):
				pShip.AddPythonFuncHandlerForInstance(App.ET_START_WARP, __name__ + ".StartingWarp")
				pShip.AddPythonFuncHandlerForInstance(App.ET_START_WARP_NOTIFY, __name__ + ".StartingWarp")
				pShip.AddPythonFuncHandlerForInstance(App.ET_EXITED_SET, __name__ + ".ExitSet")
				pInstance.bAddedAdonisTMPWarpHandlers = 1

	def DetachShip(self, pShipID, pInstance):
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		if pShip and getattr(pInstance, "bAddedAdonisTMPWarpHandlers", 0):
			pShip.RemoveHandlerForInstance(App.ET_START_WARP, __name__ + ".StartingWarp")
			pShip.RemoveHandlerForInstance(App.ET_START_WARP_NOTIFY, __name__ + ".StartingWarp")
			pShip.RemoveHandlerForInstance(App.ET_EXITED_SET, __name__ + ".ExitSet")
			pInstance.bAddedAdonisTMPWarpHandlers = 0


oAdonisTMPWarpStartUp = AdonisTMPWarpStartUpDef("AdonisTMPWarpStartUp")

def StartingWarp(pObject, pEvent):
	pObject.CallNextHandler(pEvent)

	pShip = App.ShipClass_Cast(pObject)
	pInstance = FoundationTech.dShips[pShip.GetName()]
	# Check to see if this is a valid ship
	if not getattr(pInstance, "bAddedAdonisTMPWarpHandlers", 0):
		return	# Ok, not a valid ship, bye bye!
	dConfig = getattr(pInstance, "AdonisTMPWarpStartUp")
	if not dConfig:
		return
	if dConfig.has_key("startTrack"):
		dConfig = dConfig["startTrack"]
	else:
		dConfig = dConfig.get("track", {})
	RollTextures(pInstance, pShip, dConfig)

def ExitSet(pObject, pEvent):
	pObject.CallNextHandler(pEvent)

	pShip = App.ShipClass_Cast(pEvent.GetDestination())
        sSetName = pEvent.GetCString()
	# if the system we come from is the warp system, then we exitwarp, right?
        if sSetName != "warp":
		#print "I thought we were exiting warp?", sSetName, pShip.GetName()
		return
	pInstance = FoundationTech.dShips.get(pShip.GetName())
	if not pInstance:
		return
	# Check to see if this is a valid ship
	if not getattr(pInstance, "bAddedAdonisTMPWarpHandlers", 0):
		return	# Ok, not a valid ship, bye bye!
	dConfig = getattr(pInstance, "AdonisTMPWarpStartUp")
	if not dConfig:
		return
	bReverse = 0
	if dConfig.has_key("stopTrack"):
		dConfig = dConfig["stopTrack"]
	else:
		dConfig = dConfig.get("track", {})
		bReverse = 1
	RollTextures(pInstance, pShip, dConfig, bReverse)

def RollTextures(pInstance, pShip, dTextures, bReverse=0):
	for name, textures in dTextures.items():
		lTextures = textures.items()
		lTextures.sort()
		if bReverse:
			# The first and the last textures are at the same moments!
			lTimes = textures.keys()
			lTimes.sort()
			fFirst = lTimes[0]
			fLast  = lTimes[-1]
			lTimes.reverse()
			lNew = [fFirst]
			for i in range(1, len(lTimes)):
				time = lTimes[i]
				prev = lTimes[i-1]
				lNew.append((prev-time) + lNew[i-1])
			# Reintegrate changes
			lNewTextures = []
			for i in range(len(lTextures)):
				lNewTextures.append((lNew[i], lTextures[i][1]))
			lTextures = lNewTextures
		pTextureMap = pInstance.TextureRegistration.get(name, None)
		if not pTextureMap:
			pTextureMap = TextureMap(name)
			pInstance.TextureRegistration[name] = pTextureMap
		pTextureMap.SwitchMap(pShip, lTextures)

class TextureMap:
	def __init__(self, textureName, currentMap=None):
		self.textureName = textureName
		if not currentMap: currentMap = textureName[:]
		self.currentMap = currentMap[:]
		self.pSequence = None
		self.bInSequence = 0

	def SwitchMap(self, pShip, sNew):
		self.StopAnimation()
		if type(sNew) == types.StringType:
			# Wee... Simple texture replacement
			self.InternalSwitchMap(pShip, self.currentMap, sNew)
		else:
			# Animation, we assume for easyness that this is a "flat" dict type (so ((key, value), (key....
			# And that we will only play it once
			self.pSequence = App.TGSequence_Create()
			fTiming = 0.0
			for index, texture in sNew:
				self.pSequence.AppendAction(ImmersionMethodScriptAction_Create(self, "InternalSwitchMap", pShip, texture), index-fTiming)
				fTiming = index
			self.pSequence.AppendAction(ImmersionMethodScriptAction_Create(self, "FinalSequenceAction"))
			self.pSequence.Play()
	def StopAnimation(self):
		if self.bInSequence:
			self.bInSequence = 0
			if self.pSequence and self.pSequence.IsPlaying():
				self.pSequence.Abort()
			self.pSequence = None
			return 1
		return 0
	def InternalSwitchMap(self, pShip, sNew):
		if self.currentMap == sNew:
			return
		pShip.ReplaceTexture(sNew, self.currentMap)
		pShip.RefreshReplacedTextures()
		self.currentMap = DistillNewMapName(sNew)
	def FinalSequenceAction(self):
		self.bInSequence = 0
		self.pSequence = None

def DistillNewMapName(sPath):
	return string.split(string.split(sPath, "\\")[-1], "/")[-1][:-4]

def PreProcessTextureRegistration(pInstance):
	dTextureRegistration = pInstance.NormalTextures
	if not pInstance.pShipID:
		return
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), self.pShipID)
	if not pShip:
		return
	if not hasattr(pInstance, "TextureRegistration"):
		pInstance.TextureRegistration = {}
	for texture, path in dTextureRegistration.items():
		if type(info) != types.InstanceType:
			pTextureMap = pInstance.TextureRegistration.get(texture, None)
			if not pTextureMap:
				pTextureMap = TextureMap(texture)
				pInstance.TextureRegistration[texture] = pTextureMap

			pTextureMap.SwitchMap(pShip, path)
			pTextureMap.SwitchMap(pShip, path)# Extra in case a modder meant "currently swapped texture" (for example, with SDT)
		else:
			continue# Already a proper texture registration, atleast, we hope it sounds, looks and smells like a duck, eh, texture registration
	return

# The next 2 functions are from Immersion, with thanks from LJ.
# They are used to call methods on objects from TGSequences.
# Slightly modified to recieve variable number of arguments by MLeo
#
# Currently taken from BPCore -MLeo

def ImmersionMethodScriptAction_Create(oObject, sMethod, *args):
	return apply(App.TGScriptAction_Create, (__name__, "RedirectClassAction", oObject, sMethod,) + args)

def RedirectClassAction(pAction, oObject, sMethod, *args):
	if oObject:
		pyAttr = getattr(oObject, sMethod)
		if pyAttr:
			apply(pyAttr, args)
	return 0



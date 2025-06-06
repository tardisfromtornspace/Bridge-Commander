# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# GC is ALL Rights Reserved by USS Frontier, but since GC supports Plugins it is fair to release a new TravellingMethod or patch old ones as long as the files remain unmodified.
# SGStargateNetwork.py
# Based on the prototype custom travelling method plugin script, by USS Frontier (Enhanced Warp.py, original, template), and then modified by Alex SL Gato for B5Stargate.
# 16th April 2025
#################################################################################################################
##########	MANUAL
#################################################################################################################
# NOTE: all functions/methods and attributes defined here (in this prototype example plugin, SGStargateNetwork) are required to be in the plugin, with the exception of:
# -Auxiliar attributes "myDependingTravelModule" and "myDependingTravelModulePath", since ***this TravellingMethod depends on Hyperdrive TravellingMethod and all its dependencies to work, else it will not perform***.
# -Auxiliar functions: "AlternateFTLActionEnteringWarp", "AlternateFTLActionExitWarp", "BringMeStargateFromShipSet", "CalculateDistanceBetweenObejcts", "ConditionalAlignmentPlace", "CreateDetachedElectricExplosion", "ExitSetFTLAlternateSubModel", "findShipInstance", "GetShipType", "GetWellShipFromID", "KindOfMove", "LoadGFX", "MatrixMult", "myNiPoint3ToTGPoint3", "myTGPoint3ToNiPoint3", "StargatePoolFlash" and "StartingFTLAlternateSubModel".
# If you want to make a ship a Stargate, you need to add the following to the scripts/Custom/Ships/ file:
# Note, the value of it denotes what to do:
# 0 = stargate unavailable for use from realspace.
# values different from 0 = stargate available.
#  * 1 = Type I Stargate gate - can connect to all gates from a type 1 to any other type.
#  * -1 = Type I Stargate gate - can only connect to gates from 1 and -1.
#  * 2 = Type II Milky Way Gate - can connect to all gates from a type 2 to any other type.
#  * -2 = Type II Milky Way Gate - can only connect to gates from 2 and -2.
#  * 3 = Type III Pegasus Milky Way Gate - can connect all gates from a type 3 to any other type.
#  * -3 = Type III Pegasus Milky Way Gate - can connect to all gates.
#... and so on 
# There's also another parameter "SGWorkingStargateRad", useful for when ship size does not match gate size. Use it to cap the radius according to a certain size (a closed jumper is around 0.16 - 0.17). If it is not added, it will just consider ship and gate radius.
# Finally, "SGWorkingStargateFlashRad" is to modify the flash radius to a set size.
"""
#Sample Setup: replace "ActiveSupergate" for the appropiate abbrev.
Foundation.ShipDef.ActiveSupergate.IsSGWorkingStargate = 1
Foundation.ShipDef.ActiveSupergate.SGWorkingStargateRad = 1
Foundation.ShipDef.ActiveSupergate.SGWorkingStargateFlashRad = 1
"""
#
#################################################################################################################
##########	END OF MANUAL
#################################################################################################################
#################################################################################################################
#
MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "0.12",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }
#
#################################################################################################################
#
from bcdebug import debug

#######################################
#######################################
###     GENERAL ATTRIBUTES
#######################################
#######################################
########
# name of this travelling method 
########
sName = "Stargate Network"

########
# if this travelling method is ship based. Warp for example is ship based, that means that any ship equipped with it can
# engage it anytime she wants. 
# Some travelling methods, like wormholes, are not ship based, that means ships need to enter the wormhole to travel.
########
bIsShipBased = 1

########################################
########################################
###     TRAVELER ATTRIBUTES
########################################
########################################
########
# if this travelling method can be used to tow ships.
########
bCanTowShips = 1

########
# path and file name to engine degradation sound alert
########
sDegradationSoundFile = "scripts\\Custom\\GalaxyCharts\\Sounds\\DegradationAlert.wav"

########
# if this travelling method should show starstreaks while travelling
# (starstreaks options setup in Galaxy Charts UMM Configuration menu)
########
bUseStarstreaks = 0

########
# if a ship can drop out of travel, while travelling.
########
bCanDropOut = 0

########
# if a ship can change its destination while travelling.
########
bCanChangeCourse = 0

########
# if a ship can change its speed while travelling.
########
bCanChangeSpeed = 1

########
# Phrase to show when ship is engaging this travelling method, the destination name is automatically added to the end
# so, like in warp, for example, it'll be "Warping to Kronos..."
########
sGoingTo = "Entering Stargate to go to"

########
# Phrase to show when the ship drops out of travel (while travelling)
########
sDropOut = "Exiting Stargate..."

########
# if this travelling method can trigger RDFs when a ship exits travel.
########
bCanTriggerRDF = 1

########
# The following 2 floats define the range of values that can be set as the travelling speed of a ship using this travelling method.
# For warp, for example, it's from 1 to 9.99
# It's an arbitrary scale/range. The actual conversion to a exact speed unit (km/h) is done in the method ConvertSpeedAmount located below.
########
fMinimumSpeed = 1.0
fMaximumSpeed = 1.0

########
# A float, representing the radius (in kilometers) from a launch coordinate which a ship can be able to activate this non-ship-based travelling method
########
fLaunchRadius = 15.0

########
# This attribute specifies the travelling restrictions for this travelling method. Systems can be set to be restricted to this and/or other travelling
# methods in its system plugin (region plugin part)
# The value of this attribute must be a integer, one of the ones contained in the following enum (fyi, 'RS' is abbreviation of 'restricted system'):
# 0 = No restriction
# 1 = can only be used between RSs  (when in a RS to travel to another RS)
# 2 = travel from anywhere to a RS, but can only return to the system where ship came from
# 3 = travel from anywhere to a RS, and can return to any system
########
iRestrictionFlag = 0


###########################################
###########################################
####       TRAVELER METHODS
###########################################
###########################################
import App
import Custom.GravityFX.GravityFXlib
import Foundation
import FoundationTech
import MissionLib
import math
import string
import traceback

#######################################
####   ALTERNATESUBMODELFTL METHODS
#######################################

myDependingTravelModule = None # The module we load.
myDependingTravelModulePath = "Custom.TravellingMethods.Hyperdrive" # From where we load the module.
try:
	myDependingTravelModuleAux = __import__(myDependingTravelModulePath)
	if hasattr(myDependingTravelModuleAux, "sName"):
		theNewName = myDependingTravelModuleAux.sName
		if theNewName != None and theNewName == "Hyperdrive" and hasattr(myDependingTravelModuleAux, "IsShipEquipped") and hasattr(myDependingTravelModuleAux, "SetupSequence") and hasattr(myDependingTravelModuleAux, "GetStartTravelEvents") and hasattr(myDependingTravelModuleAux, "GetExitedTravelEvents") and hasattr(myDependingTravelModuleAux, "GetTravelSetToUse") and hasattr(myDependingTravelModuleAux, "ConvertSpeedAmount"):
			myDependingTravelModule = myDependingTravelModuleAux
except:
	traceback.print_exc()

#ENGAGING_ALTERNATEFTLSUBMODEL = App.UtopiaModule_GetNextEventType() # For when we are immediately about to fly with this FTL method
#DISENGAGING_ALTERNATEFTLSUBMODEL = App.UtopiaModule_GetNextEventType() # For when we are immediately about to stop flying with this FTL method
# Due to AlternateSubModelFTL implementation, only 1 function can cover 1 event, no multiple functions can cover the same event directly. While on regular implementation of these SubModel FTL method that limits nothing, if you want multiple functions to respond, you must create a parent function of sorts that calls all the other functions you want, or create some sort of alternate listener inside some function.

# Because we could end on an endless loop, the imports must be done inside the functions, else the game will not recognize any attribute or function beyond that
# Reason I'm doing this function pass beyond just passing input parameters to the common function is to allow other TravellingMethod modders more flexibility
# from Custom.Techs.AlternateSubModelFTL import StartingProtoWarp, ExitSetProto

def KindOfMove(): 
	return "Stargate Network" # Modify this with the name you are gonna use for the AlternateSubModelFTL - on this case it is identical to Stargate Network, so we are gonna use that

def StartingFTLAlternateSubModel(pObject, pEvent, techP, move): # What actions does AlternateSubModelFTL need to do when entering this FTL method
	if move == None:
		move = KindOfMove()

	from Custom.Techs.AlternateSubModelFTL import StartingProtoWarp
	StartingProtoWarp(pObject, pEvent, techP, move)

def AlternateFTLActionEnteringWarp(): # Linking eType with the function - since we are depending on another travel method to work for us, we add an "Error" one which the AlternateSubModelFTL Tech will catch
	if myDependingTravelModule != None:
		return myDependingTravelModule.AlternateFTLActionEnteringWarp()
	else:
		return None, None, "Error"

def ExitSetFTLAlternateSubModel(pObject, pEvent, techP, move): # What actions does AlternateSubModelFTL need to do when exiting this FTL method
	if move == None:
		move = KindOfMove()

	from Custom.Techs.AlternateSubModelFTL import ExitSetProto
	ExitSetProto(pObject, pEvent, techP, move)

def AlternateFTLActionExitWarp(): # Linking eType with the function
	if myDependingTravelModule != None:
		return myDependingTravelModule.AlternateFTLActionExitWarp()
	else:
		return None, None, "Error"


########
# Method to check if the ship is equipped with this travelling method.
# Must return 1 if it has it, 0 if it does not.
# NOTE: this function is not used as a method of the Travel class as are the other functions here.
#       this is actually used just like a helper for the Travel Manager.
########
# An aux. function
def findShipInstance(pShip):
	debug(__name__ + ", findShipInstance")
	pInstance = None
	try:
		if not pShip:
			return pInstance
		if FoundationTech.dShips.has_key(pShip.GetName()):
			pInstance = FoundationTech.dShips[pShip.GetName()]
	except:
		pass
	return pInstance

def IsShipEquipped(pShip):
	return 1 # I mean, ALL ships can use it...

########
# Method to check if the ship can travel.
# Must return 1 if it can, otherwise return a string(reason why the ship couldn't travel)
########

# An aux. function.
def GetWellShipFromID(pShipID):
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShipID)
	if not pShip or pShip.IsDead() or pShip.IsDying():
		return None
	return pShip

# An aux. function.
def GetShipType(pShip):
        debug(__name__ + ", GetShipType")
        if pShip and pShip.GetScript():
                return string.split(pShip.GetScript(), '.')[-1]
        return None

# An aux. function.
def IsWorkingStargate(pShip):

	typeOfGate = None
	radLimit = None
	flashLimit = None
	sShipType = GetShipType(pShip)
	if not sShipType:
		return typeOfGate, radLimit#, flashLimit

	if Foundation.shipList.has_key(sShipType):
		pFoundationShip = Foundation.shipList[sShipType]
		if pFoundationShip:
			if hasattr(pFoundationShip, "IsSGWorkingStargate"):
				typeOfGate = pFoundationShip.IsSGWorkingStargate
			if hasattr(pFoundationShip, "SGWorkingStargateRad"):
				radLimit = pFoundationShip.SGWorkingStargateRad
			if hasattr(pFoundationShip, "SGWorkingStargateFlashRad"):
				flashLimit = pFoundationShip.SGWorkingStargateFlashRad
	return typeOfGate, radLimit, flashLimit

# An aux. function.
def CalculateDistanceBetweenObejcts(pTarget, pShip, pShipLoc=None):
	distanceBetween = -1
	if pShipLoc == None and pShip != None:
		pShipLoc = pShip.GetWorldLocation()
	if pTarget != None and pShipLoc != None:
		targetplacement = pTarget.GetWorldLocation()
		if targetplacement != None:
			targetplacement.Subtract(pShipLoc)
			distanceBetween = targetplacement.Length()

	return distanceBetween

def CanTravel(self):
	if myDependingTravelModule == None:
		return "Impossible to travel through a Stargate if the technology does not exist!"
	pShip = self.GetShip()
	pPlayer = App.Game_GetCurrentPlayer()
	bIsPlayer = 0
	pShipID = pShip.GetObjID()
	if pPlayer and pShipID == pPlayer.GetObjID():
		bIsPlayer = 1
	pHelm = App.CharacterClass_GetObject(App.g_kSetManager.GetSet("bridge"), "Helm")

	pSet = pShip.GetContainingSet()
	if not pSet:
		return "We are in No Set"

	pProx = pSet.GetProximityManager()
	if not pProx:
		return "This Set is unstable"	

	lshipsToAssess = []

	ticksPerKilometer = 225/40 # 225 is approximately 40 km, so 225/40 is the number of ticks per kilometer
	kIter = pProx.GetNearObjects(pShip.GetWorldLocation(), fLaunchRadius * ticksPerKilometer, 1) 
	while 1:
		pObject = pProx.GetNextObject(kIter)
		if not pObject:
			break

		if pObject.IsTypeOf(App.CT_SHIP):
			if hasattr(pObject, "GetObjID"):
				paTargetID = pObject.GetObjID()
				paTarget = GetWellShipFromID(paTargetID)
				if paTarget and paTargetID != pShipID:
					lshipsToAssess.append(paTarget)
	
	pProx.EndObjectIteration(kIter)

	validFound = 0
	pShipLoc = pShip.GetWorldLocation()
	shipRad = pShip.GetRadius()
	gateType = 0
	gateRad = 0
	if pShipLoc != None:
		for pTarget in lshipsToAssess:
			try:
				works, radiusLimit, _ = IsWorkingStargate(pTarget)
				if works != None and works != 0:
					try:
						distanceBetween = CalculateDistanceBetweenObejcts(pTarget, pShip, pShipLoc)
						targetRad = pTarget.GetRadius()
						if targetRad != None and targetRad <= distanceBetween:
							if radiusLimit != None:
								if radiusLimit >= shipRad:
									validFound = 1
									gateType = works
									gateRad = radiusLimit
							elif targetRad >= shipRad:
								validFound = 1
								gateType = works
								gateRad = targetRad
					except:
						validFound = 0
						print "Error on", __name__, ".CanTravel:"
						traceback.print_exc()
			except:
				print "Error on", __name__, ".CanTravel:"
				traceback.print_exc()

			if validFound == 1:
				break

	if validFound == 0:
		return "We need to be inside a suitable stargate range of proper size."

	pImpulseEngines = pShip.GetImpulseEngineSubsystem()
	if not pImpulseEngines:
		return "No Impulse Engines"

	if (pImpulseEngines.GetPowerPercentageWanted() == 0.0):
		# Ship is trying to warp with their engines off.
		if bIsPlayer == 1:
			pXO = App.CharacterClass_GetObject(App.g_kSetManager.GetSet("bridge"), "XO")
			if pXO:
				MissionLib.QueueActionToPlay(App.CharacterAction_Create(pXO, App.CharacterAction.AT_SAY_LINE, "EngineeringNeedPowerToEngines", None, 1))
		return "Impulse Engines offline"

	works = 0
	myDestSet = self.DestSet
	validGate = None
	if myDestSet != None and hasattr(myDestSet, "GetProximityManager"):
		pProx2 = myDestSet.GetProximityManager()
		if not pProx2:
			return "Destination Set is unstable"
		

		for aObject in myDestSet.GetClassObjectList(App.CT_SHIP):
			if aObject != None and hasattr(aObject, "GetObjID"):
				aShipID = aObject.GetObjID()
				if aShipID != pShipID:
					pFutureShip = GetWellShipFromID(aShipID)
					if pFutureShip:
						destGateType, destGateRad, _ = IsWorkingStargate(pFutureShip)
						pFutureShipRad = pFutureShip.GetRadius()
						if destGateType != None and destGateType != 0 and ((gateType > 0 and destGateType > 0) or (gateType < 0 and gateType == -destGateType)):
							if (destGateRad != None and shipRad <= destGateRad) or (shipRad <= pFutureShipRad):
								works = destGateType
								break
		if works == 0:
			return "No stargates found on destination"

	return 1
					

########
# Method to check if the ship can continue travelling (she's travelling, yeah)
# must return 1 if she can, 0 if she can't travel anymore (thus will forcibly drop out).
########
def CanContinueTravelling(self):
	pShip = self.GetShip()
	pPlayer = App.Game_GetCurrentPlayer()
	bIsPlayer = 0
	if pPlayer and pShip.GetObjID() == pPlayer.GetObjID():
		bIsPlayer = 1

	pImpulseEngines = pShip.GetImpulseEngineSubsystem()
	bStatus = 1
	if pImpulseEngines != None:
		if pImpulseEngines.IsDisabled() == 1:
			if bIsPlayer == 1:
				pSequence = App.TGSequence_Create ()
				pSubtitleAction = App.SubtitleAction_CreateC("Brex: Impulse engines are disabled sir, I'm getting us out before we are lost to unknown eddies.")
				pSubtitleAction.SetDuration(3.0)
				pSequence.AddAction(pSubtitleAction)
				pSequence.Play()
			bStatus = 0
	else:
		bStatus = 0
	return bStatus

########
# Method to get the direction to turn the ship towards for her to travel. 
# return can be:
# None -> ship will travel blindly. That is, without turning to face a particular direction (possibly dodging potential obstacles)
# TGPoint3  -> the direction vector to turn towards.
# [TGPoint3, TGPoint3]  -> a list of direction vectors ( [forward, up] )  to turn and align towards.
########
def GetEngageDirection(self):
	# We go on blindly
	return None

########
# Method to do travelling method specific stuff before the ship engages travel. At this point, ship is already due to engage travel, that is,
# passed the checks to see if she can travel and is starting the travelling procedures.
# return value is not important.
########
def PreEngageStuff(self):
	return

########
# Method to do travelling method specific stuff before the ship exits travel. This happens right before the ship changes set to enter the its destination.
# return value is not important.
########
def PreExitStuff(self):
	return

########
# Method to setup the GFX effect sequences, and return them in the order:
# 1� entering travel sequence
# 2� during travel sequence
# 3� exiting travel sequence
########

# An aux. function.
def BringMeStargateFromShipSet(pShipID, chooseClosest=0, gateType=None):

	returningType = None
	flashLimit = None
	pShip = GetWellShipFromID(pShipID)
	if pShip:
		myDestSet = pShip.GetContainingSet()
		if myDestSet:
			pProx2 = myDestSet.GetProximityManager()
			if pProx2 != None:
				pShipLoc = pShip.GetWorldLocation()
				works = -1
				pStargate = None
				pDistance = None
				for aObject in myDestSet.GetClassObjectList(App.CT_SHIP):
					if aObject != None and hasattr(aObject, "GetObjID"):
						aShipID = aObject.GetObjID()
						pFutureShip = GetWellShipFromID(aShipID)
						if pFutureShip:
							works, radLimit, iFlash = IsWorkingStargate(pFutureShip)
							if works != None and works != 0 and (gateType == None or ((gateType > 0 and works > 0) or (gateType < 0 and gateType == -works)) ):
								if pStargate == None:
									pStargate = pFutureShip
									returningType = works
									flashLimit = iFlash
								if chooseClosest == 0:
									break
								distanceBetween = CalculateDistanceBetweenObejcts(pFutureShip, pShip, pShipLoc)
								if distanceBetween > -1:
									if pDistance == None:
										pDistance = distanceBetween
									elif pDistance > distanceBetween:
										pDistance = distanceBetween
										pStargate = pFutureShip
										returningType = works
										flashLimit = iFlash
				return pStargate, returningType, flashLimit

	return None, returningType, flashLimit

# An aux. function, based on the FedAblativeArmour.py script's one, a fragment probably imported from ATP Functions by Apollo
def myNiPoint3ToTGPoint3(p, factor=1.0):
	kPoint = App.TGPoint3()
	kPoint.SetXYZ(p.x * factor, p.y * factor, p.z * factor)
	return kPoint

# An aux. function.
def myTGPoint3ToNiPoint3(p, factor=1.0):
	kPoint = App.NiPoint3(p.x * factor, p.y * factor, p.z * factor)
	return kPoint

# An aux. function.
def MatrixMult(kFwd, kNewUp):
    debug(__name__ + ", MatrixMult")
    vAuxVx = kFwd.y * kNewUp.z - kNewUp.y * kFwd.z
    vAuxVy = kNewUp.x * kFwd.z - kFwd.x * kNewUp.z
    vAuxVz = kFwd.x * kNewUp.y - kNewUp.x * kFwd.y
    return vAuxVx, vAuxVy, vAuxVz

# Aux. function
def LoadGFX(iNumXFrames, iNumYFrames, sFile):
                fX = 0.0
                fY = 0.0

                pContainer = App.g_kTextureAnimManager.AddContainer(sFile)   
                pTrack = pContainer.AddTextureTrack(iNumXFrames * iNumYFrames)
                for index in range(iNumXFrames * iNumYFrames):
                        pTrack.SetFrame(index, fX, fY + (1.0 / iNumYFrames), fX + (1.0 / iNumXFrames), fY)
                        fX = fX + (1.0 / iNumXFrames)

                        if (fX >= 1.0):
                            fX = 0.0
                            fY = fY + (1.0 / iNumYFrames)

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
		print "SGStargateNetwork TravellingMethod: error while calling CreateDetachedElectricExplosion:"
		traceback.print_exc()
		pEffect = None

	return pEffect

# Aux function. Create flash effect on a ship.
def StargatePoolFlash(pAction, pShipID, sType, sRace, sparkSize=5, sFile = 'scripts/Custom/TravellingMethods/GFX/JumpspaceFlashAlternate.tga'):
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShipID)
	if not pShip:
		return 0
	if pShip == None:
		return 0

	fEffectList = []
	try:
		sFile = "scripts/Custom/TravellingMethods/GFX/StargateVooshFlash.tga"

		if sparkSize > 0:
			colorKey = [245.0 / 255, 245.0 / 255, 255.0 / 255]

			LoadGFX(4, 4, sFile)

			pAttachTo = pShip.GetContainingSet().GetEffectRoot()
			fSize = pShip.GetRadius() * sparkSize
			pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())

			try:
				pEffect = CreateDetachedElectricExplosion(colorKey[0], colorKey[1], colorKey[2], fSize, 1, sFile, pEmitFrom, pAttachTo, fFrequency=1,fEmitLife=1,fSpeed=1)
				if pEffect:
					fEffect = App.EffectAction_Create(pEffect)
					if fEffect:
						fEffectList.append(fEffect)
			except:
				print "SGStargateNetwork TravellingMethod: error while calling StargatePoolFlash:"
				traceback.print_exc()

	except:
		print "SGStargateNetwork TravellingMethod: error while calling StargatePoolEnterFlash:"
		traceback.print_exc()
		fEffect = None

	lenef = len(fEffectList)
	if lenef > 0:
		pSequence = App.TGSequence_Create()
		for fEffect in fEffectList:
			pSequence.AddAction(fEffect, None)
		pSequence.Play()
                
	return 0

# An aux. function.
def ConditionalAlignmentPlace(pAction, pShipID, chooseClosest=0, method="Entry", radiusAdder = 0, rRadius = None, sRace = None, fTimeToFlash = None, pStargateID = None, pStargateType = None):
	pShip = GetWellShipFromID(pShipID)
	if pShip:
		myCommand = "Enter Warp"
		if method != "Entry" and method != myCommand:
			myCommand = "Exit Warp"

		radLimit = None
		flashLimit = None
		if pStargateID == None:
			pStargate, radLimit, flashLimit = BringMeStargateFromShipSet(pShipID, chooseClosest, pStargateType)
		else:
			pStargate = GetWellShipFromID(pStargateID)
			_ , radLimit, flashLimit = IsWorkingStargate(pShip)

		if pStargate:
			# Get the forward from that ship
			kNewUpReal = pStargate.GetWorldUpTG() #App.TGPoint3_GetModelUp()
			pointForwardLoc = App.TGPoint3_GetModelForward()
			pointForwardDir = App.TGPoint3_GetModelForward()
			if method == "Entry":
				#pointForwardLoc = App.TGPoint3_GetModelBackward()
				pointForwardDir = App.TGPoint3_GetModelBackward()

			if pointForwardLoc != None:
				try:
					#isUsingPhys = pShip.IsUsingPhysics()
					#pShip.SetUsePhysics(0)
					vVelocity = App.TGPoint3()
					vVelocity.SetXYZ(0,0,0)
					pShip.SetAcceleration(vVelocity)
					pShip.SetAngularAcceleration(vVelocity)
					pShip.SetVelocity(vVelocity)
					pShip.SetAngularVelocity(vVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)				
					#pShip.SetUsePhysics(isUsingPhys)
				except:
					traceback.print_exc()	
				try:
					pShipNode = pShip.GetNiObject()
					pStargateNode = pStargate.GetNiObject()
					if pStargateNode != None:
						# While we are far from everyone, alignment.
						
						pGVectorFwd = App.TGModelUtils_LocalToWorldVector(pStargateNode, pointForwardDir)

						kFwd = myNiPoint3ToTGPoint3(pGVectorFwd)
						kFwd.Unitize()

						kNewUp = App.TGPoint3()
						kNewUp.SetXYZ(kNewUpReal.x, kNewUpReal.y, kNewUpReal.z)

						kPerp = kFwd.Perpendicular()
						kPerp2 = App.TGPoint3()
						kPerp2.SetXYZ(kPerp.x, kPerp.y, kPerp.z)

						# Align Step 1: a x b, with a and b being the kFwd and the kNewUp

						vAuxVx, vAuxVy, vAuxVz = MatrixMult(kFwd, kNewUp)

						if vAuxVx == 0.0 and vAuxVy == 0.0 and vAuxVz == 0.0: # No other option, we share the same rect
							pShip.AlignToVectors(kFwd, kPerp2) # Aims correctly but gives a weird clockwise or counterclockwise turn if the ship rotates
						else:
							kVect1 = App.TGPoint3()
							kVect1.SetXYZ(vAuxVx, vAuxVy, vAuxVz)

							#Now that we got a x b, we want to get (a x b) x a = kVect1 x a, to get the perpendicular we really want
							vAuxVx, vAuxVy, vAuxVz = MatrixMult(kVect1, kFwd)


							kVect2 = App.TGPoint3()
							kVect2.SetXYZ(vAuxVx, vAuxVy, vAuxVz)
							kVect2.Unitize()

							pShip.AlignToVectors(kFwd, kVect2)

						# Second, translation: scale the forward by both ship's radius, adjusting the conversion from local to world (1 world = 100 local)

						radCal = 1.0

						intoCalc= 1.0
						starRad = pStargate.GetRadius()
						shipRad = pShip.GetRadius()

						if flashLimit != None:
							radCal = flashLimit / (starRad + 0.001)

						pointForwardLoc.Scale(100*((intoCalc*starRad)+shipRad) + radiusAdder)

						pGPoint = App.TGModelUtils_LocalToWorldPoint(pStargateNode, pointForwardLoc)

						pShip.SetTranslate(myNiPoint3ToTGPoint3(pGPoint))
						pShip.UpdateNodeOnly()

						if fTimeToFlash != None:
							try:
								# Create the flash.
								# Potential TO-DO maybe add a disable collisions check?
								pFlashAction1 = App.TGScriptAction_Create(__name__, "StargatePoolFlash", pStargate.GetObjID(), myCommand, sRace, radCal)
								if pFlashAction1:
									pEngageWarpSeq = App.TGSequence_Create()
									pEngageWarpSeq.AddAction(pFlashAction1, None, fTimeToFlash)
									pEngageWarpSeq.Play()
							except:
								traceback.print_exc()


				except:
					traceback.print_exc()
		else:
			if fTimeToFlash != None:
				try:
					# Create the flash.
					pFlashAction1 = App.TGScriptAction_Create(__name__, "StargatePoolFlash", pShipID, myCommand, sRace, rRadius)
					if pFlashAction1:
						pEngageWarpSeq = App.TGSequence_Create()
						pEngageWarpSeq.AddAction(pFlashAction1, None, fTimeToFlash)
						pEngageWarpSeq.Play()
				except:
					traceback.print_exc()
					
	return 0			


def SetupSequence(self):
	# you can use this function as an example on how to create your own '.SetupSequence(self)' method for your
	# custom travelling method.
	
	# note that the only REQUIRED part is what the function return and the single parameter 'pTravel', so go to the end of the function
	# for more info

	################################################################################
	# from here below it is just the custom code to create the custom sequences
	# NOT-REQUIRED  STUFF
	# modify accordingly for your sequences
	#########
	# NOTE:  ALL tractor related actions that are used here for the engaging and for the exiting
	#        warp sequences ARE REQUIRED if you want to be able to succesfully (and beautifully)
	#	   tractor ships thru your travel. (in this example, thru Starspace)
	################################################################################

	debug(__name__ + ", SetupSequence")
	pWS = self.TravelerSequence	
	
	sCustomActionsScript = "Custom.GalaxyCharts.WarpSequence_Override"
	
	try:
		from Custom.QBautostart.Libs.LibWarp import GetEntryDelayTime
		fEntryDelayTime = GetEntryDelayTime()
	except:
		fEntryDelayTime = 2.0
	pShip = pWS.GetShip()
	pPlayer = App.Game_GetCurrentPlayer()

	if (pShip == None):
		return

	pShipID = pShip.GetObjID()

	# Get the destination set name from the module name, if applicable.
	pcDest = None
	pcDestModule = pWS.GetDestination()
	if (pcDestModule != None):
		pcDest = pcDestModule[string.rfind(pcDestModule, ".") + 1:]
		if (pcDest == None):
			pcDest = pcDestModule

	pWarpSet = pWS.Travel.GetTravelSetToUse()

	pEngageWarpSeq = App.TGSequence_Create()

	pExitWarpSeq = App.TGSequence_Create()

	# Keep track of which action is the final action in the warp sequence,
	# so we can attach the m_pPostWarp sequence to the end.  By default,
	# pMoveAction2 is the final action...
	pFinalAction = None
	pWarpSoundAction1 = None

	try:
		import Custom.NanoFXv2.NanoFX_Lib
		sRace = Custom.NanoFXv2.NanoFX_Lib.GetSpeciesName(pShip)
		pWS.Logger.LogString("Got species of ship from NanoFXv2")
	except:
		sRace = ""

	# EXTRA ADDED
	pGateShip, iGateType, _ = BringMeStargateFromShipSet(pShipID, 1, None)

	myBoosting = 15.0

	rRadius = 5 
	pSRad = pShip.GetRadius()
	if pSRad < 5:
		rRadius = 2/(pSRad+0.0001) * 5

	iVelRel = 2.0 * 100 * myBoosting/(fEntryDelayTime+0.1)

	if (pPlayer != None) and (pShipID == pPlayer.GetObjID()):
		fEntryDelayTime = fEntryDelayTime + 0.1

		pDisallowInput = App.TGScriptAction_Create("MissionLib", "RemoveControl")
		pEngageWarpSeq.AddAction(pDisallowInput, None)

	fTimeToFlash = fEntryDelayTime*0.5
	
	pProperAlignment1 = App.TGScriptAction_Create(__name__, "ConditionalAlignmentPlace", pShipID, 1, "Entry", iVelRel, rRadius, sRace, fEntryDelayTime * 0.6 + 0.2 + 0.7 + fTimeToFlash * 0.6, pGateShip.GetObjID(), None)
	pEngageWarpSeq.AddAction(pProperAlignment1, None)

	if (pPlayer != None) and (pShipID == pPlayer.GetObjID()):
		fEntryDelayTime = fEntryDelayTime + 0.1

		# Force a noninteractive cinematic view in space..
		pCinematicStart = App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0)
		pEngageWarpSeq.AddAction(pCinematicStart, pProperAlignment1)

		pDisallowInput = App.TGScriptAction_Create("MissionLib", "RemoveControl")
		pEngageWarpSeq.AddAction(pDisallowInput, pCinematicStart)

		# Maybe for other FTL methods it could be unecessary but having the camera constantly swapping and then having the warp flash at 2 cm from your face is not good!
		pcOrig = None
		pcOrigModule = pWS.GetDestination()
		if (pcOrigModule != None):
			pcOrig = pcOrigModule[string.rfind(pcOrigModule, ".") + 1:]
			if (pcOrig == None):
				pcOrig = pcOrigModule
		if pcOrig != None:
			pWatchShipLeave = App.TGScriptAction_Create(__name__, "WatchPlayerShipLeave", pcOrig, pShip.GetName())
			if pWatchShipLeave != None:
				pEngageWarpSeq.AddAction(pWatchShipLeave, pCinematicStart)

	if myDependingTravelModule != None:
		pWarpSoundAction1 = App.TGScriptAction_Create(myDependingTravelModulePath, "PlayHyperdriveSounds", pShipID, "Enter Warp", sRace)
		pEngageWarpSeq.AddAction(pWarpSoundAction1, pProperAlignment1, fEntryDelayTime + 0.2)
	
	pBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShipID, 1, myBoosting)
	pEngageWarpSeq.AddAction(pBoostAction, pProperAlignment1, fEntryDelayTime + 0.2 + 0.7)

	#fTimeToFlash = fEntryDelayTime*0.5
	if pWS.Travel.bTractorStat == 1:
		fCount = 0.0
		while fCount < fTimeToFlash:
			pMaintainTowingAction = App.TGScriptAction_Create(sCustomActionsScript, "MaintainTowingAction", pWS)
			pEngageWarpSeq.AddAction(pMaintainTowingAction, None, fCount)
			fCount = fCount + 0.01
			if fCount >= fTimeToFlash:
				break

	# Create the warp flash.
	#if myDependingTravelModule != None:
	#	pFlashAction1 = App.TGScriptAction_Create(myDependingTravelModulePath, "B5StarspaceFlash", pShipID, "Enter Warp", sRace, rRadius)
	#	pEngageWarpSeq.AddAction(pFlashAction1, pBoostAction, fTimeToFlash * 0.8)

	# Hide the ship.
	pHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShipID, 1)
	pEngageWarpSeq.AddAction(pHideShip, pBoostAction, fTimeToFlash * 1.0)

	pUnBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShipID, 0, 1.0)
	pEngageWarpSeq.AddAction(pUnBoostAction, pHideShip)
	
	pCheckTowing = App.TGScriptAction_Create(sCustomActionsScript, "EngageSeqTractorCheck", pWS)
	pEngageWarpSeq.AddAction(pCheckTowing, pUnBoostAction, 0.25)

	if myDependingTravelModule != None and (pPlayer != None) and (pShipID == pPlayer.GetObjID()):
		pWarpSoundActionMid = App.TGScriptAction_Create(myDependingTravelModulePath, "defineTravelSpaceNoise", 1)
		pEngageWarpSeq.AddAction(pWarpSoundActionMid, pUnBoostAction, 2.5)	

	pEnWarpSeqEND = App.TGScriptAction_Create(sCustomActionsScript, "NoAction")
	pEngageWarpSeq.AddAction(pEnWarpSeqEND, pUnBoostAction, 2.5)

	############### exiting begins ########

	# Add the actions for exiting warp only if the destination set exists.
	if(pWS.GetDestinationSet() != None):
		pProperAlignment2 = App.TGScriptAction_Create(__name__, "ConditionalAlignmentPlace", pShipID, 0, "Exit", 0, rRadius, sRace, 0.6, None, iGateType)
		pExitWarpSeq.AddAction(pProperAlignment2, None)

		if (pPlayer != None) and (pShipID == pPlayer.GetObjID()):
			# Force a noninteractive cinematic view in space..
			pCinematicStart = App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0)
			pExitWarpSeq.AddAction(pCinematicStart, pProperAlignment2)
			if myDependingTravelModule != None:
				pWarpSoundActionMidFinal = App.TGScriptAction_Create(myDependingTravelModulePath, "defineTravelSpaceNoise", 0)
				pExitWarpSeq.AddAction(pWarpSoundActionMidFinal, None)

			pDisallowInput = App.TGScriptAction_Create("MissionLib", "RemoveControl")
			pExitWarpSeq.AddAction(pDisallowInput, pCinematicStart)

			# Add actions to move the camera in the destination set to watch the placement,
			# so we can watch the ship come in.
			# Initial position is reverse chasing the placement the ship arrives at.
			pCameraAction4 = App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", pcDest, pPlayer.GetName())
			pExitWarpSeq.AddAction(pCameraAction4, pDisallowInput)
	
		# Hide the ship.
		pHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShipID, 1)
		pExitWarpSeq.AddAction(pHideShip, pProperAlignment2)

		# Check for towee
		if pWS.Travel.bTractorStat == 1:
			pHideTowee = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pWS.Travel.Towee.GetObjID(), 1)
			pExitWarpSeq.AddAction(pHideTowee, pHideShip)

		# Create the warp flash.
		#if myDependingTravelModule != None:
		#	pFlashAction2 = App.TGScriptAction_Create(myDependingTravelModulePath, "B5StarspaceFlash", pShipID, "Exit Warp", sRace, rRadius)
		#	pExitWarpSeq.AddAction(pFlashAction2, pHideShip, 0.7)

		# Un-Hide the ship
		pUnHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShipID, 0)
		pExitWarpSeq.AddAction(pUnHideShip, pHideShip, 1.7)

		# Un-hide the Towee, plus if it exists, also set up the maintain chain
		## REMEMBER: any changes in the time of this sequence will also require a re-check of this part, to make sure
		##           we're making the right amount of MaintainTowing actions.
		if pWS.Travel.bTractorStat == 1:
			pUnHideTowee = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pWS.Travel.Towee.GetObjID(), 0)
			pExitWarpSeq.AddAction(pUnHideTowee, pUnHideShip)

			fCount = 0.0
			while fCount < 3.6:
				pMaintainTowingAction = App.TGScriptAction_Create(sCustomActionsScript, "MaintainTowingAction", pWS)
				pExitWarpSeq.AddAction(pMaintainTowingAction, pUnHideTowee, fCount)
				fCount = fCount + 0.01
				if fCount >= 3.6:
					break

		# Give it a little boost
		pBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShipID, 1, myBoosting)
		pExitWarpSeq.AddAction(pBoostAction, pUnHideShip, 0.1)

		# Play the vushhhhh of exiting warp
		if myDependingTravelModule != None:
			pWarpSoundAction2 = App.TGScriptAction_Create(myDependingTravelModulePath, "PlayHyperdriveSounds", pShipID, "Exit Warp", sRace)
			pExitWarpSeq.AddAction(pWarpSoundAction2, pBoostAction)
	
		# Make the ship return to normal speed.
		pUnBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShipID, 0, 1.0)
		pExitWarpSeq.AddAction(pUnBoostAction, pBoostAction, 2.0)

		# And finally finish the exit sequence
		# actually, just put up a empty action, the Traveler system automatically puts his exit sequence action at the
		# end of the sequence, and his exit action is necessary. However I want it to trigger at the right time, and doing
		# this, i'll achieve that.
		pExitWarpSeqEND = App.TGScriptAction_Create(sCustomActionsScript, "NoAction")
		pExitWarpSeq.AddAction(pExitWarpSeqEND, pUnBoostAction, 1.5)

	###########################################################################################
	# end of the not-required stuff that sets up my sequences
	###########################################################################################

	# Now the following part, the return statement is VERY important.
	# it must return a list of 3 values, from beggining to end, they must be:
	# 1�: the engaging travel sequence  (plays once, when the ship enters the travel)
	# 2�: the during travel sequence    (plays repeatedly, while the ship is travelling)
	# 3�: the exiting travel sequence   (plays once, when the ship exits travel)

	# Note that each one of them can be None, if you don't want to have that sequence in your travel method.

	return [pEngageWarpSeq, None, pExitWarpSeq]


########
# Method to return "starting travel" events, much like those START_WARP events.
# must return a list with the events, possibly none (empty list)
########
def GetStartTravelEvents(self):
	if myDependingTravelModule != None:
		return myDependingTravelModule.GetStartTravelEvents(self)
	pEvent = App.TGEvent_Create()
	sOriAdress = pEvent.this
	sOriAdress = sOriAdress[0:len(sOriAdress)-7]
	sAdress = sOriAdress+"WarpEvent"
	pSWNEvent = App.WarpEvent(sAdress)
	pSWNEvent.SetEventType(App.ET_START_WARP_NOTIFY )
	pSWNEvent.SetDestination(self.Ship)
	return [ pSWNEvent ]

########
# Method to return "exiting travel" events, much like those EXITED_SET or EXITED_WARP events.
# must return a list with the events, possibly none (empty list)
########
def GetExitedTravelEvents(self):
	if myDependingTravelModule != None:
		return myDependingTravelModule.GetExitedTravelEvents(self)
	pEvent = App.TGStringEvent_Create()
	pEvent.SetEventType(App.ET_EXITED_SET)
	pEvent.SetDestination(self.Ship)
	pEvent.SetString("warp")
	return [ pEvent ]

########
# Method to return the travel set to use.
# must return a App.SetClass instance, it can't be None.
# NOTE: for the moment, this is probably the best way to make if ships can, or can not, be chased while warping.
########
def GetTravelSetToUse(self):
	if myDependingTravelModule != None:
		return myDependingTravelModule.GetTravelSetToUse(self)
	try:
		import Custom.GalaxyCharts.Traveler
		pSet = None
		if self.IsPlayer == 1:
			pSet = Custom.GalaxyCharts.Traveler.Travel.pTravelSet
		elif self.IsPlayer == 0 and self.IsAIinPlayerRoute == 1:
			pSet = Custom.GalaxyCharts.Traveler.Travel.pTravelSet
		elif self.IsPlayer == 0 and self.IsAIinPlayerRoute == 0:
			pSet = Custom.GalaxyCharts.Traveler.Travel.pAITravelSet
		return pSet
	except:
		self._LogError("GetTravelSetToUse")

########
# Method to convert the speed this ship is travelling at to Cs ("c" is the physical constant that is equal to the speed of light, in km/h. So,
# in other words, this method should convert the "speed" of the ship, which is relative to this travelling method, to how many times is the ship
# travelling faster than the speed of light.
# must return a float  (like 1.0)
########
def ConvertSpeedAmount(fSpeed):
	if myDependingTravelModule != None:
		return myDependingTravelModule.ConvertSpeedAmount(12.0)
	if fSpeed >= 9.999:
		fFacA = 2.88                ##### Do Not Change These Values #####
		fFacB = 8.312               ##### Do Not Change These Values #####
	elif fSpeed > 9.99:
		fFacA = 2.88                ##### Do Not Change These Values #####
		fFacB = 7.512               ##### Do Not Change These Values #####
	elif fSpeed > 9.6:
		fFacA = 2.8700              ##### Do Not Change These Values #####
		fFacB = 5.9645              ##### Do Not Change These Values #####
	elif fSpeed <= 9.6:
		fFacA = 3.0                 ##### Do Not Change These Values #####
		fFacB = 3.0                 ##### Do Not Change These Values #####

	speed = (math.pow(fSpeed, (10.0/fFacA)) + math.pow((10.0-fSpeed), (-11.0/fFacB)))
	return speed

########
# Method to return the normal max speed of this travelling method that this travel instance (ship) can achieve.
# For "normal", I mean, on normal circunstances, like for example, engines at 100% power.
# must return a float  (like 1.0)
########
def GetMaxSpeed(self):
	return self.Ship.GetMaxWarpSpeed()

########
# Method to return the normal cruise speed of this travelling method that this travel instance (ship) can achieve.
# For "normal", I mean, on normal circunstances, like for example, engines at 100% power.
# must return a float  (like 1.0)
########
def GetCruiseSpeed(self):
	return self.Ship.GetCruiseWarpSpeed()

########
# Method to return the actual max speed of this travelling method that this travel instance (ship) can achieve.
# By "actual", I mean, in the current circunstances, like for example: in warp, engine power affects max speed. So the actual max speed
# that the ship can achieve will be different than the normal max speed if engine power is not at 100%.
# must return a float  (like 1.0)
########
def GetActualMaxSpeed(self):
	pWarpEngines = self.Ship.GetWarpEngineSubsystem()
	if pWarpEngines == None:
		return 5.0
	fRealMaxSpeed = self.GetMaxSpeed()
	if self.IsPlayer == 1:
		fPower = pWarpEngines.GetPowerPercentageWanted()
	else:
		fPower = self.AIwarpPower
	fAMWS = (fRealMaxSpeed * fPower) - (fPower - 1.0)
	if fAMWS > 9.99:
		fAMWS = 9.99
	return fAMWS

########
# Method to return the actual cruise speed of this travelling method that this travel instance (ship) can achieve.
# By "actual", I mean, in the current circunstances, like for example: in warp, engine power affects cruise speed. So the actual cruise speed
# that the ship can achieve will be different than the normal cruise speed if engine power is not at 100%.
# must return a float  (like 1.0)
########
def GetActualCruiseSpeed(self):
	pWarpEngines = self.Ship.GetWarpEngineSubsystem()
	if pWarpEngines == None:
		return 5.0
	fRealCruiseSpeed = self.GetCruiseSpeed()
	if self.IsPlayer == 1:
		fPower = pWarpEngines.GetPowerPercentageWanted()
	else:
		fPower = self.AIwarpPower
	fACWS = (fRealCruiseSpeed * fPower) - (fPower - 1.0)
	if fACWS > 9.99:
		fACWS = 9.99
	return fACWS

########
# Method to return the list of systems that can be damaged by degradation of the travel (which happens when a ship travels faster than her 
# actual cruise speed).  In warp, for example, the systems that are damaged by degradation is the warp engines.
# must return a list  (like [])
########
def GetDegradationSystems(self):
	pWarpEngines = self.Ship.GetWarpEngineSubsystem()
	return [ pWarpEngines ]

########
# Method to return the list of coordinates (points in space) in this set which the ship can activate this travelling method from.
# must return a list  (like [])
########
def GetLaunchCoordinatesList(pSet):
	return []
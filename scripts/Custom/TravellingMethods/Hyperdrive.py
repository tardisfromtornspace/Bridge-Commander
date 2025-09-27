# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# Hyperdrive.py
# GC is ALL Rights Reserved by USS Frontier, but since GC supports Plugins it is fair to release a new TravellingMethod or patch old ones as long as the files remain unmodified.
# Based on the prototype custom travelling method plugin script, by USS Frontier (Normal Warp.py, original, template), original incomplete version made by BCXtreme (https://www.gamefront.com/games/bridge-commander/file/slipstream-for-galaxy-charts) for slipstream and finished by Alex SL Gato. Then modified for Hyperdrive.
# This plugin was originally released without a license, which means it defaults to All Rights Reserved. While the original readme includes the line "As far as I am concerned, anyone can take this and finish it if they want to," that grants permission to continue development — but not to relicense or attach a license such as LGPL. The absence of an explicit license means the work cannot be treated as open source.
# Slipstream Module and Hyperdrive Module remain ALL RIGHTS RESERVED, by USS Sovereign.
# Please note that this file requires:
# - USS Sovereign's Hyperdrive Module, as the purpose of the original mod was to provide exactly that.
# The original Slipstream version requires all assets from the incomplete original from https://www.gamefront.com/games/bridge-commander/file/slipstream-for-galaxy-charts, except scripts/Custom/TravellingMethods/Slipstream.py.new (so, basically the files at scripts/Custom/GalaxyCharts), but since this file needs to create its own for Hyperdrive, it does not require them.
# 27th September 2025
#################################################################################################################
##########	MANUAL
#################################################################################################################
# This mod provides Hyperdrive functionality for GalaxyCharts for ships that could use HyperdriveModule, finishing the work done by BCXtreme so sounds and flashes work properly, AI-only Hyperdrive set is different from player-and-AI set, made some code check more efficient, and speeds are adjusted so AI vessels can use Hyperdrive with different speeds since Sovereign's Hyperdrive has been used for SW and SG ships, amongst others. Unlike the Slipstream version, Stargate Hyperdrive lacks player ISI functions, so we also modify this TravellingMethod further to support AlternateSubModelFTL ISI (AlternateSubModelFTL ISI functions were provided with permission from Sovereign as well and those sections remain All Rights Reserved). Also, Hyperdrive Module lacks a hyperspace sounds, so we are not adding one.
#
# To make a ship use Hyperdrive, follow USS Sovereign's instructions on how to add his own Hyperdrive, which basically consists on adding any hardpoint called "Hyperdrive " followed by a number from 1 to 20. As a GalaxyCharts quirk and to cover the multi-fandom statement above, speeds have been set on a 1.0-10.0 warp range. 1.0-2.0 here are roughly the same as warp 1.0 to 9.99 of GC's Normal Warp, while 3.0, 4.0,... would be a rough equivalent of if GC allowed to introduce fSppeds of warp 8 * 20.0 , 8 * 30.0,... and so on. It gets very, very fast on the higher numbers. This is done as a way to provide stuff like local, galactic and intergalactic hyperdrives.
# NOTE: all functions/methods and attributes defined here (in this prototype example plugin, Hyperdrive) are required to be in the plugin, with the exception of:
# -Auxiliar attributes: "myDependingTravelModule", "myDependingTravelModuleLib", "myDependingTravelModuleLibPath", "myDependingTravelModulePath", "myGlobalAISet" and "myGlobalpSet"
# -Auxiliar functions: "AuxProtoElementNames", "findShipInstance", "GetEngageDirectionC", "GetWellShipFromID", "HyperdriveDisabledCalculations", "HyperdriveFlash", "PlayHyperdriveSounds", "ProperTunnelTexture" and "WatchPlayerShipLeave".
# -Auxiliar classes: 
# -Auxiliar functions for intra-system intercept (ISI) support, which as a result of being a common-made function between default GalaxyCharts functions/methods, regular AlternateSubModelFTL and ISI, while not required to be on the plugin, some of their contents are actually required if they are not there: "awayNavPointDistanceCalc", "CanTravelShip", "EngageSeqTractorCheckI", "GetEngageDirectionISI", "GetExitedTravelEventsI", "GetStartTravelEventsI", "GetEngageDirectionC", "InSystemIntercept", "MaintainTowingActionI", "PlayB5TransDimensionalDriveSoundI", "removeTractorISITowInfo", "SetupSequenceISI" and "SetupTowingI".
# Additionally, "GetTravelSetToUse" was modified slightly from the template's original, so as to provide a way for possible extra scripts (i.e. some Hyperdrive Hub jump network, if that is possible) to work easier.
#
#################################################################################################################
##########	END OF MANUAL
#################################################################################################################
#################################################################################################################
#
MODINFO = { "Author": "\"BCXtreme\" (original), \"Alex SL Gato\" andromedavirgoa@gmail.com (fixes), \"USS Sovereign\" (Hyperdrive Module)",
	    "Version": "0.34",
	    "License": "All Rights Reserved, by BCXtreme",
	    "Description": "Read the small title above for more info"
	    }
#
#################################################################################################################


# prototype custom travelling method plugin script, by USS Frontier

# NOTE: all functions/methods and attributes defined here (in this prototype example plugin, NormalWarp) are required to be in the plugin.

#######################################
#######################################
###     GENERAL ATTRIBUTES
#######################################
#######################################
########
# name of this travelling method 
########
sName = "Hyperdrive"

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
bCanDropOut = 1

########
# if a ship can change it's destination while travelling.
########
bCanChangeCourse = 1

########
# if a ship can change it's speed while travelling.
########
bCanChangeSpeed = 1

########
# Phrase to show when ship is engaging this travelling method, the destination name is automatically added to the end
# so, like in warp, for example, it'll be "Warping to Kronos..."
########
sGoingTo = "Opening Hyperdrive Tunnel to"

########
# Phrase to show when the ship drops out of travel (while travelling)
########
sDropOut = "Dropped out of Hyperdrive Tunnel..."

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
fMaximumSpeed = 10.0

########
# A float, representing the radius (in kilometers) from a launch coordinate which a ship can be able to activate this non-ship-based travelling method
########
fLaunchRadius = 0.0

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
from bcdebug import debug
import App
import Camera
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
myDependingTravelModulePath = "Custom.Hyperdrive.HyperdriveModule" # From where we load the module.
try:
	myDependingTravelModuleAux = __import__(myDependingTravelModulePath)
	if myDependingTravelModuleAux != None and hasattr(myDependingTravelModuleAux, "VERSION") and hasattr(myDependingTravelModuleAux, "sHyperdriveList") and hasattr(myDependingTravelModuleAux, "EnteringFlash") and hasattr(myDependingTravelModuleAux, "ExitingFlash"):
		myDependingTravelModule = myDependingTravelModuleAux
except:
	traceback.print_exc()

myDependingTravelModuleLib = None # The module we load.
myDependingTravelModuleLibPath = "Custom.Hyperdrive.Libs.LoadFlash" # From where we load the module.
try:
	myDependingTravelModuleLibAux = __import__(myDependingTravelModuleLibPath)
	if myDependingTravelModuleLibAux != None and hasattr(myDependingTravelModuleLibAux, "StartGFX") and hasattr(myDependingTravelModuleLibAux, "CreateGFX"):
		myDependingTravelModuleLib = myDependingTravelModuleLibAux
except:
	traceback.print_exc()

ENGAGING_ALTERNATEFTLSUBMODEL = App.UtopiaModule_GetNextEventType() # For when we are immediately about to fly with this FTL method
DISENGAGING_ALTERNATEFTLSUBMODEL = App.UtopiaModule_GetNextEventType() # For when we are immediately about to stop flying with this FTL method
# Due to AlternateSubModelFTL implementation, only 1 function can cover 1 event, no multiple functions can cover the same event directly. While on regular implementation of these SubModel FTL method that limits nothing, if you want multiple functions to respond, you must create a parent function of sorts that calls all the other functions you want, or create some sort of alternate listener inside some function.

# Because we could end on an endless loop, the imports must be done inside the functions, else the game will not recognize any attribute or function beyond that
# Reason I'm doing this function pass beyond just passing input parameters to the common function is to allow other TravellingMethod modders more flexibility
# from Custom.Techs.AlternateSubModelFTL import StartingProtoWarp, ExitSetProto

def KindOfMove(): 
	return "Hyperdrive" # Modify this with the name you are gonna use for the AlternateSubModelFTL

def StartingFTLAlternateSubModel(pObject, pEvent, techP, move): # What actions does AlternateSubModelFTL need to do when entering this FTL method
	if move == None:
		move = KindOfMove()

	from Custom.Techs.AlternateSubModelFTL import StartingProtoWarp
	StartingProtoWarp(pObject, pEvent, techP, move)

def AlternateFTLActionEnteringWarp(): # Linking eType with the function - since we are depending on another travel method to work for us, we add an "Error" one which the AlternateSubModelFTL Tech will catch
	if myDependingTravelModule != None:
		return ENGAGING_ALTERNATEFTLSUBMODEL, StartingFTLAlternateSubModel
	else:
		return None, None, "Error"

def ExitSetFTLAlternateSubModel(pObject, pEvent, techP, move): # What actions does AlternateSubModelFTL need to do when exiting this FTL method
	if move == None:
		move = KindOfMove()

	from Custom.Techs.AlternateSubModelFTL import ExitSetProto
	ExitSetProto(pObject, pEvent, techP, move)

def AlternateFTLActionExitWarp(): # Linking eType with the function
	if myDependingTravelModule != None:
		return DISENGAGING_ALTERNATEFTLSUBMODEL, ExitSetFTLAlternateSubModel
	else:
		return None, None, "Error"

def InSystemIntercept():
	if myDependingTravelModule != None:
		propulsionType = sName # The name for its subMenu option
		eEntryEvent = GetStartTravelEventsI
		eExitEvent = GetExitedTravelEventsI
		eSequenceFunction = SetupSequenceISI # Important NOTE - This sequence is gonna be a modification of the normal sequences for changing systems. Since intra-system does not call pre-engage nor post-engage functions on its own (only the entry and exit events), if you have an actual pre-engage and post-engage function that is not just a mere "return", you may want to adjust your sequence to call them instead at the appropiate time.
		isEquipped = IsShipEquipped
		eCanTravel = CanTravelShip
		awayNavPointDistance = awayNavPointDistanceCalc # This is a custom multiplier value, used for checking when a ship is too close to a planet or ship. A lower value means that it will allow closer ISI, while a higher value will make that ISI inner proximity limit be further. Negative values are set to 0.
		engageDirection = GetEngageDirectionISI

		return propulsionType, eEntryEvent, eExitEvent, eSequenceFunction, isEquipped, eCanTravel, awayNavPointDistance, engageDirection

	else:
		return "ERROR"

def awayNavPointDistanceCalc(pShipID=None):
	return 0.9


########
# Method to check if the ship is equipped with this travelling method.
# Must return 1 if it has it, 0 if it does not.
# NOTE: this function is not used as a method of the Travel class as are the other functions here.
#       this is actually used just like a helper for the Travel Manager.
########
# An aux function.
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

	specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist = AuxProtoElementNames()
        totalHyperdriveEngines, onlineHyperdriveEngines = HyperdriveDisabledCalculations("Core", None, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, None, pShip, 1)
	return (totalHyperdriveEngines > 0)

	return 0


########
# Method to check if the ship can travel.
# Must return 1 if it can, otherwise return a string(reason why the ship couldn't travel)
########
# This is just an auxiliar function I made for this
def AuxProtoElementNames(*args):
	# Returns hardpoint property name fragments that indicate are part of the B5Jumpspace system, and blacklists
	coolNames = None
	if myDependingTravelModule != None:
		coolNames = myDependingTravelModule.sHyperdriveList
	return coolNames, ["hyperdrive"], ["not a hyperdrive", " not hyperdrive"]

# This is just another auxiliar function I (Alex SL Gato) made for more efficient system lookup.
# The original was like the OLD CODE example below, which follows Hyperdrive Module style in a way, looking for 20 particular names. However, there is an issue with that - it needs to do a pass on a ship's hardpoint for each subsystem name, out of 20. That means that on a best-case scenario it needs to perform part of a pass, while on a worst-case scenario, it needs to perform 20 passes to state that the ship lacks Hyperdrive. When it's only the player ship, it is acceptable. However, when it applies to ALL the potential ships on the galaxy and some of them have huge hardpoints, it LAGs a lot. The new method just needs to perform part of a pass on a best-case scenario, and 1 hardpoint pass on a worst-case one, and it will tell you how many Hyperdrive drives are if you allow it to perform a full pass.
# OLD CODE:
# for i in range(20): # Slisptream Drive uses something like this. This is compeltely feasible when there's only 1 player
#		number = i + 1
#		pDrive = MissionLib.GetSubsystemByName(pShip, "Hyperdrive "+str(number) )
#		if pDrive != None:
#			return 1

def HyperdriveDisabledCalculations(type, specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, pSubsystem, pShip, justFindOne=0):
	totalHyperdriveEngines = 0
	onlineHyperdriveEngines = 0
	if type == "Nacelle":
		if pSubsystem != None:
			for i in range(pSubsystem.GetNumChildSubsystems()):
				pChild = pSubsystem.GetChildSubsystem(i)
				if pChild:
					if hasattr(pChild, "GetName") and pChild.GetName() != None:
						pChildName = pChild.GetName()
						found = 0
						blacklisted = 0
						if specificNacelleHPList == None:				
							pchildnamelower = string.lower(pChildName)
							for item in hardpointProtoNames:
								foundThis = string.find(pchildnamelower, item) + 1
								if foundThis > 0:
									found = 1
									break
							for item in hardpointProtoBlacklist:
								foundThis = string.find(pchildnamelower, item) + 1
								if foundThis > 0:
									blacklisted = 1
									break
						else:
							found = (pChildName in specificNacelleHPList)

						if found and not blacklisted:
							totalHyperdriveEngines = totalHyperdriveEngines + 1
							if pChild.GetCondition() > 0.0 and not pChild.IsDisabled():
								onlineHyperdriveEngines = onlineHyperdriveEngines + 1
								if justFindOne == 1:
									break
	elif type == "Core":
		pShipSet = pShip.GetPropertySet()
		pShipList = pShipSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
		iNumItems = pShipList.TGGetNumItems()

		pShipList.TGBeginIteration()
		for i in range(iNumItems):
			pShipProperty = App.SubsystemProperty_Cast(pShipList.TGGetNext().GetProperty())
			if pShipProperty:
				pSubsystema = pShip.GetSubsystemByProperty(pShipProperty)
				if pSubsystema and pSubsystema != None:
					if hasattr(pSubsystema, "GetName") and pSubsystema.GetName() != None:
						pSubsystemName = pSubsystema.GetName()

						found = 0
						blacklisted = 0
						if specificCoreHPList == None:				
							pSubsystemNamelower = string.lower(pSubsystemName)
							for item in hardpointProtoNames:
								foundThis = string.find(pSubsystemNamelower, item) + 1
								if foundThis > 0:
									found = 1
									break
							for item in hardpointProtoBlacklist:
								foundThis = string.find(pSubsystemNamelower, item) + 1
								if foundThis > 0:
									blacklisted = 1
									break
						else:
							found = (pSubsystemName in specificCoreHPList)

						if found and not blacklisted:
							totalHyperdriveEngines = totalHyperdriveEngines + 1
							if pSubsystema.GetCondition() > 0.0 and not pSubsystema.IsDisabled() and (not hasattr(pSubsystema, "IsOn") or pSubsystema.IsOn()):
								onlineHyperdriveEngines = onlineHyperdriveEngines + 1
								if justFindOne == 1:
									break

		pShipList.TGDoneIterating()
		pShipList.TGDestroy()

	return totalHyperdriveEngines, onlineHyperdriveEngines

def CanTravel(self): # NOTE: Requires CanTravelShip
	debug(__name__ + ", CanTravel")
	return CanTravelShip(self.GetShip())

# Auxiliar ISI function
def CanTravelShip(pShip):
	if myDependingTravelModule == None:
		return "Impossible to travel to Hyperdrive if Hyperdrive does not exist!"
	pPlayer = App.Game_GetCurrentPlayer()
	bIsPlayer = 0
	if pPlayer and pShip.GetObjID() == pPlayer.GetObjID():
		bIsPlayer = 1
	pHelm = App.CharacterClass_GetObject(App.g_kSetManager.GetSet("bridge"), "Helm")
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


	specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist = AuxProtoElementNames()
        totalHyperdriveEngines, onlineHyperdriveEngines = HyperdriveDisabledCalculations("Core", None, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, None, pShip, 1)
	if totalHyperdriveEngines <= 0:
		return "Unequipped with Hyperdrive Drive"
	if onlineHyperdriveEngines <= 0:
		return "Hyperdrive Drive disabled or offline"

	pSet = pShip.GetContainingSet()

	pStarbase12Set = App.g_kSetManager.GetSet("Starbase12")
	if pStarbase12Set:
		if pShip.GetContainingSet():
			if pStarbase12Set.GetObjID() == pShip.GetContainingSet().GetObjID():
				pStarbase12 = App.ShipClass_GetObject(pStarbase12Set, "Starbase 12")
				if pStarbase12:
					import AI.Compound.DockWithStarbase
					if AI.Compound.DockWithStarbase.IsInViewOfInsidePoints(pShip, pStarbase12):
						if bIsPlayer == 1:
							if pHelm:
								App.CharacterAction_Create(pHelm, App.CharacterAction.AT_SAY_LINE, "CantWarp3", None, 1).Play()
							else:
								# No character, display subtitle only.
								pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Crew General.tgl")
								if pDatabase:
									pSequence = App.TGSequence_Create()
									pSubtitleAction = App.SubtitleAction_Create(pDatabase, "CantWarp3")
									pSubtitleAction.SetDuration(3.0)
									pSequence.AddAction(pSubtitleAction)
									pSequence.Play()
									App.g_kLocalizationManager.Unload(pDatabase)
						return "Inside Starbase12"
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
	bStatus = 1

	specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist = AuxProtoElementNames()
        totalHyperdriveEngines, onlineHyperdriveEngines = HyperdriveDisabledCalculations("Core", None, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, None, pShip, 1)
	if totalHyperdriveEngines <= 0 or onlineHyperdriveEngines <= 0:
		if bIsPlayer == 1:
			pSequence = App.TGSequence_Create ()
			pSubtitleAction = App.SubtitleAction_CreateC("Brex: Hyperdrive Drive is disabled or offline, sir, the Hyperdrive tunnel is collapsing.")
			pSubtitleAction.SetDuration(3.0)
			pSequence.AddAction(pSubtitleAction)
			pSequence.Play()
		bStatus = 0

	return bStatus

########
# Method to get the direction to turn the ship towards for her to travel. 
# return can be:
# None -> ship will travel blindly. That is, without turning to face a particular direction (possibly dodging potential obstacles)
# TGPoint3  -> the direction vector to turn towards.
# [TGPoint3, TGPoint3]  -> a list of direction vectors ( [forward, up] )  to turn and align towards.
########
def GetEngageDirection(self): # NOTE: Requires GetEngageDirectionC
	debug(__name__ + ", GetEngageDirection")
	return GetEngageDirectionC(self, None)

# Aux. ISI function.
def GetEngageDirectionISI(pPlayerID): # NOTE: Requires GetEngageDirectionC
	debug(__name__ + ", GetEngageDirectionISI")
	return GetEngageDirectionC(None, pPlayerID)

# Aux. ISI function.
def GetEngageDirectionC(mySelf, pPlayerID = None):
	# Get all the objects along the line that we'll
	# be warping through.
	debug(__name__ + ", GetEngageDirectionC")
	fRayLength = 4000.0

	vOrigin = None
	vEnd = None

	pPlayer = None
	if mySelf != None:
		vOrigin = mySelf.Ship.GetWorldLocation()
		vEnd = mySelf.Ship.GetWorldForwardTG() # REMEMBER, this forward and stuff needs to be changed to other directions if your drive moves that way!
	elif pPlayerID != None:
		pPlayer = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pPlayerID)
		if pPlayer:
			vOrigin = pPlayer.GetWorldLocation()
			vEnd = pPlayer.GetWorldForwardTG() # REMEMBER, this forward and stuff needs to be changed to other directions if your drive moves that way!
		else:
			return None
	else:
		return None

	vEnd.Scale(fRayLength)
	vEnd.Add(vOrigin)
	
	lsObstacles = None
	if pPlayer == None:
		lsObstacles = mySelf.GetWarpObstacles(vOrigin, vEnd)
	else:
		lsObstacles = MissionLib.GrabWarpObstaclesFromSet(vOrigin, vEnd, pPlayer.GetContainingSet(), pPlayer.GetRadius(), 1, pPlayer.GetObjID())

	# If we have no obstacles in the way, we're good.
	if len(lsObstacles) == 0:
		vZero = App.TGPoint3()
		vZero.SetXYZ(0, 0, 0)
		if mySelf != None:
			mySelf.Ship.SetTargetAngularVelocityDirect(vZero)
		else:
			pPlayer.SetTargetAngularVelocityDirect(vZero)
		return None

	vBetterDirection = None
	# We've got obstacles in the way.
	if not vBetterDirection:
		# Cast a few rays
		# and try to find a good direction to go.  If we don't
		# find a good direction, that's bad...
		for iRayCount in range(50):
			vRay = App.TGPoint3_GetRandomUnitVector()

			# Bias it toward our Forward direction.
			vRay.Scale(1.5)
			myForward = None
			if pPlayer == None:
				myForward = mySelf.Ship.GetWorldForwardTG() # REMEMBER, this forward and stuff needs to be changed to other directions if your drive moves that way!
			else:
				myForward = pPlayer.GetWorldForwardTG() # REMEMBER, this forward and stuff needs to be changed to other directions if your drive moves that way!

			vRay.Add(myForward)
			vRay.Unitize()

			vEnd = App.TGPoint3()
			vEnd.Set(vRay)
			vEnd.Scale(fRayLength)

			vEnd.Add(vOrigin)

			lsObstacles = None
			if mySelf != None:
				lsObstacles = mySelf.GetWarpObstacles(vOrigin, vEnd)
			else:
				lsObstacles = MissionLib.GrabWarpObstaclesFromSet(vOrigin, vEnd, pPlayer.GetContainingSet(), pPlayer.GetRadius(), 1, pPlayer.GetObjID())

			if not lsObstacles:
				# Found a good direction.
				vBetterDirection = vRay
				break

	if vBetterDirection:
		# Return the better direction to turn to, the Travel will take care of the rest.
		return vBetterDirection
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
# 1º entering travel sequence
# 2º during travel sequence
# 3º exiting travel sequence
########
# Aux. ISI function
def removeTractorISITowInfo(pShipID, pInstance=None):
	debug(__name__ + ", removeTractorISITowInfo")
	if pInstance == None:
		pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShipID)
		if not pShip:
			return 0

		pInstance = findShipInstance(pShip)
		
	if pInstance:
		try:
			if hasattr(pInstance, "HyperdriveTractorISIvTowPosition"):
				del pInstance.HyperdriveTractorISIvTowPosition
		except:
			print "Hyperdrive: Error while calling removeTractorISITowInfo"
			traceback.print_exc()
		try:
			if hasattr(pInstance, "HyperdriveTractorISITowee"):
				del pInstance.HyperdriveTractorISITowee
		except:
			print "Hyperdrive: Error while calling removeTractorISITowInfo"
			traceback.print_exc()
		try:
			if hasattr(pInstance, "HyperdriveTractorISIbTractorStat"):
				del pInstance.HyperdriveTractorISIbTractorStat
		except:
			print "Hyperdrive: Error while calling removeTractorISITowInfo"
			traceback.print_exc()

	return 0

# Aux. ISI function
def SetupTowingI(ShipID):
	debug(__name__ + ", SetupTowingI")
	try:
		if bCanTowShips != 1:
			return 0

		pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), ShipID)
		if not pShip:
			return 0

		pInstance = findShipInstance(pShip)
		if not pInstance:
			return 0

		# Figure out if we're towing a ship right now.
		pTractor = pShip.GetTractorBeamSystem()
		if (not pTractor)  or  (not pTractor.IsOn())  or  (pTractor.IsDisabled()):
			return 0

		# Tractor beam mode needs to be set to Tow, and must be firing.
		if (pTractor.GetMode() != App.TractorBeamSystem.TBS_TOW)  or  (not pTractor.IsFiring()):
			return 0

		# ***FIXME: We're assuming that, just because we're firing, we're
		# hitting the right target.
		# I didn't found this "GetTargetList" method on App, but somehow it works...
		try:
			pTarget = pTractor.GetTargetList()[0]
			if not pTarget:
				return 0
		except IndexError:
			# probably for some reason the tractor didn't had a target, return
			return 0

		if pTarget.GetWorldLocation() == None:
			return 0

		pInstance.HyperdriveTractorISIvTowPosition = pTarget.GetWorldLocation()
		pInstance.HyperdriveTractorISIvTowPosition.Subtract( pShip.GetWorldLocation() )
		pInstance.HyperdriveTractorISIvTowPosition.MultMatrixLeft( pShip.GetWorldRotation().Transpose() )

		pInstance.HyperdriveTractorISITowee = pTarget.GetObjID()

		pInstance.HyperdriveTractorISIbTractorStat = 1

	except:
		print "Hyperdrive: Error while calling SetupTowingI"
		traceback.print_exc()

	return 0

# Aux. ISI function
def MaintainTowingActionI(pAction, pShipID):
	debug(__name__ + ", MaintainTowingActionI")
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShipID)
	if not pShip:
		return 0

	pInstance = findShipInstance(pShip)
	if not pInstance:
		return 0
	try:
		if hasattr(pInstance, "HyperdriveTractorISIbTractorStat") and pInstance.HyperdriveTractorISIbTractorStat == 1:
			pTractor = pShip.GetTractorBeamSystem()
			if pTractor == None:
				# ship has no tractor beam... what in the blazes?!?
				return 0
			elif pTractor.IsDisabled() == 1:
				### self tractors are disabled... for now, better bail out...
				return 0
			if pTractor.IsOn() == 0:
				pTractor.TurnOn()
				if pTractor.IsOn() == 0:
					### couldn't set the tractors on for some reason... for now, better bail out...
					return 0
			if pTractor.GetMode() != App.TractorBeamSystem.TBS_TOW:
				# the tractor beam system mode was changed, so set it back to tow to make sure that
				# no problems will occur, and the process of towing a ship thru travel goes smoothly
				pTractor.SetMode(App.TractorBeamSystem.TBS_TOW)

			if not hasattr(pInstance, "HyperdriveTractorISITowee"):
				return 0

			targetID = pInstance.HyperdriveTractorISITowee
			pTempTargetAux = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), targetID)
			if not pTempTargetAux:
				return 0

			# Update/Maintain the towee's position and speed with the tower.
			vPosition = App.TGPoint3()
			vPosition.Set( pInstance.HyperdriveTractorISIvTowPosition )
			vPosition.MultMatrixLeft( pShip.GetWorldRotation() )
			vPosition.Add( pShip.GetWorldLocation() )
			pTempTargetAux.SetTranslate(vPosition)
			# Set it to match velocities.
			pTempTargetAux.SetVelocity( pShip.GetVelocityTG() )
			pTempTargetAux.UpdateNodeOnly()

			vOffset = App.TGPoint3()
			vOffset.SetXYZ(0, 0, 0)
			if pTractor.IsFiring():
				try:
					pTarget = pTractor.GetTargetList()[0]
				except IndexError:
					return 0

				if pTarget == None:
					# self is tractoring target None, so resume tractoring on the Towee
					pTractor.StartFiring(pTempTargetAux, vOffset)
				else:
					if pTarget.GetObjID() != targetID:
						# self is tractoring another ship...
						### for now, it's better to resume towing the Towee, we'll think what we can do
						### when this happens later.
						pTractor.StartFiring(pTempTargetAux, vOffset)
			else:
				# self isn't tractoring anymore, so resume tractoring on the Towee
				pTractor.StartFiring(pTempTargetAux, vOffset)
	except:
		print "Hyperdrive: Error while calling MaintainTowingActionI"
		traceback.print_exc()

	return 0

# Aux. ISI function
def EngageSeqTractorCheckI(pAction, pShipID):
	debug(__name__ + ", EngageSeqTractorCheckI")

	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShipID)
	if not pShip:
		return 0

	pInstance = findShipInstance(pShip)
	if not pInstance:
		return 0

	if hasattr(pInstance, "HyperdriveTractorISIbTractorStat") and pInstance.HyperdriveTractorISIbTractorStat == 1 and hasattr(pInstance, "HyperdriveTractorISITowee") and pInstance.HyperdriveTractorISITowee != None:
		# hide the towee

		pToweeShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pInstance.HyperdriveTractorISITowee)
		if pToweeShip:
			pToweeShip.SetHidden(1)

		# and then shut down the tractors. you don't wanna see a tractor beam going out of nowhere grabbing a ship
		pTractors = pShip.GetTractorBeamSystem()
		# I know that for this part to happen the ship that is travelling has to have an tractor beam system. Still, knowing STBC like we do, it's best to do this check again, to be sure and prevent any problems.
		if pTractors != None:
			pTractors.StopFiring()

		if pToweeShip:
			vZero = App.TGPoint3()
			vZero.SetXYZ(0,0,0)
			pToweeShip.SetVelocity(vZero)
			pToweeShip.SetAcceleration(vZero)
			pToweeShip.UpdateNodeOnly()
	return 0


# Some auxiliar global variables to allow set change and better sounds
myGlobalpSet = None
myGlobalAISet = None

# An aux. function.
def GetWellShipFromID(pShipID):
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShipID)
	if not pShip or pShip.IsDead() or pShip.IsDying():
		return None
	return pShip

# An aux. function.
def PlayHyperdriveSounds(pAction, pShipID, sAction = "Enter Warp", sRace = None):
	try:
		pShip = GetWellShipFromID(pShipID)
		if pShip:
			if myDependingTravelModule != None:
				if myDependingTravelModuleLib != None:
					if sAction == "Enter Warp":
						myDependingTravelModule.EnteringFlash(pAction, pShipID)
					else:
						myDependingTravelModule.ExitingFlash(pAction, pShipID)
				else:
					print "Your Hyperdrive module is missing a key library: ", myDependingTravelModuleLibPath
			else:
				print "There's no Hyperdrive module on ", myDependingTravelModuleLibPath
	except:
			traceback.print_exc()
	return 0

# An aux. function. original by BCXtreme, modified by Alex SL Gato.
def HyperdriveFlash(pFlashAction1, pShipID):
	pShip = GetWellShipFromID(pShipID)
	if pShip:
		try:
			if myDependingTravelModule != None:
				if myDependingTravelModuleLib != None:
					myDependingTravelModuleLib.StartGFX(pShipID)
					myDependingTravelModuleLib.CreateGFX(pShip)
				else:
					print "Your Hyperdrive module is missing a key library: ", myDependingTravelModuleLibPath
			else:
				print "There's no Hyperdrive module on ", myDependingTravelModuleLibPath
		except:
			traceback.print_exc()
	else:
		print "ship not found or dying or dead"
	return 0

# Aux. for a better camera
# A modified Actions.CameraScriptActions function.
def WatchPlayerShipLeave(pAction, sSet, sObjectName):
	debug(__name__ + ", WatchPlayerShipLeave")
	pSet = App.g_kSetManager.GetSet(sSet)

	if not pSet:
		return 0

	pCamera = Camera.GetPlayerCamera()

	if not pCamera:
		return 0

	pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", sSet, sObjectName, 1, 0)
	pAction.Play()

	pMode = pCamera.GetCurrentCameraMode()
	if not pMode:
		return 0

	pMode.SetAttrFloat("AwayDistance", -1.0)
	pMode.SetAttrFloat("ForwardOffset", -7.0)
	pMode.SetAttrFloat("SideOffset", -7.0)
	pMode.SetAttrFloat("RangeAngle1", -360.0)
	pMode.SetAttrFloat("RangeAngle2", 360.0)
	pMode.SetAttrFloat("RangeAngle3", -360.0)
	pMode.SetAttrFloat("RangeAngle4", 360.0)
	pMode.SetAttrFloat("AwayDistance", 100000.0)
	pMode.Update()

	return 0
# ISI function
def SetupSequenceISI(pShip=None): # TO-DO UPDATE
	# you can use this function as an example on how to create your own 'SetupSequenceISI(self)' method for AlternateSubModelFTL
	# While it has to basically mirror the '.SetupSequence(self)' method below (albeit you could create totally different sequences if you want), it needs to remove any unecessary code that references to self or changing systems.
	# Also this intraSystem intercept does not automatically call PreEngage nor PostEngage functions, if you really need to call those, you would need to call them by yourself, and adapted to also not include references to self.
	# something of the style of "DoPreEngageStuffISI()" or something.
	debug(__name__ + ", SetupSequenceISI")
	sCustomActionsScript = "Custom.GalaxyCharts.WarpSequence_Override"
	#AAAA
	try:
		from Custom.QBautostart.Libs.LibWarp import GetEntryDelayTime
		fEntryDelayTime = GetEntryDelayTime()
	except:
		fEntryDelayTime = 2.0

	pPlayer = App.Game_GetCurrentPlayer()

	if (pShip == None):
		pShip = pPlayer

	if (pShip == None):
		return

	pShipID = pShip.GetObjID()

	SetupTowingI(pShipID)

	pInstance = findShipInstance(pShip)

	hasTractorReady = pInstance != None and hasattr(pInstance, "BSTransDimensionalDriveISIbTractorStat") and (pInstance.BSTransDimensionalDriveISIbTractorStat == 1)

	# Get the destination set name from the module name, if applicable.
	pPlayerSet = pShip.GetContainingSet()
	sSet = ""
	if pPlayerSet != None:
		sSet = pPlayerSet.GetName()

	# Get the destination set name from the module name, if applicable.
	pcDest = None
	pcDestModule = pPlayerSet.GetRegionModule()
	if (pcDestModule != None):
		pcDest = pcDestModule[string.rfind(pcDestModule, ".") + 1:]
		if (pcDest == None):
			pcDest = pcDestModule

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
	except:
		sRace = ""

	try:
		import Custom.NanoFXv2.NanoFX_Lib
		sRace = Custom.NanoFXv2.NanoFX_Lib.GetSpeciesName(pShip)
	except:
		sRace = ""
	
	if (pPlayer != None) and (pShipID == pPlayer.GetObjID()):
		fEntryDelayTime = fEntryDelayTime + 1.0

		# Force a noninteractive cinematic view in space..
		pCinematicStart = App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0)
		pEngageWarpSeq.AddAction(pCinematicStart, None)

		pDisallowInput = App.TGScriptAction_Create("MissionLib", "RemoveControl")
		pEngageWarpSeq.AddAction(pDisallowInput, pCinematicStart)

		# Maybe for other FTL methods it could be unecessary but having the camera constantly swapping and then having the warp flash at 2 cm from your face is not good!
		#pcOrig = None
		#pcOrigModule = pcDestModule
		#if (pcOrigModule != None):
		#	pcOrig = pcOrigModule[string.rfind(pcOrigModule, ".") + 1:]
		#	if (pcOrig == None):
		#		pcOrig = pcOrigModule
		#if pcOrig != None:
		#	pWatchShipLeave = App.TGScriptAction_Create(__name__, "WatchPlayerShipLeave", pcOrig, pShip.GetName())
		#	if pWatchShipLeave != None:
		#		pEngageWarpSeq.AddAction(pWatchShipLeave, pCinematicStart)

	pWarpSoundAction1 = App.TGScriptAction_Create(__name__, "PlayHyperdriveSounds", pShipID, "Enter Warp", sRace)
	pEngageWarpSeq.AddAction(pWarpSoundAction1, None, fEntryDelayTime + 0.2)
	
	pBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShipID, 1, 100.0)
	pEngageWarpSeq.AddAction(pBoostAction, pWarpSoundAction1, 0.7)

	try:
		import Custom.NanoFXv2.WarpFX.WarpFX
		pNacelleFlash = Custom.NanoFXv2.WarpFX.WarpFX.CreateNacelleFlashSeq(pShip, pShip.GetRadius())
		pEngageWarpSeq.AddAction(pNacelleFlash, pWarpSoundAction1)
	except:
		pass

	fTimeToFlash = 3.5 + fEntryDelayTime -1.3
	if hasTractorReady == 1:
		while fCount < fTimeToFlash:
			pMaintainTowingAction = App.TGScriptAction_Create(__name__, "MaintainTowingActionI", pShipID)
			pEngageWarpSeq.AddAction(pMaintainTowingAction, None, fCount)

			fCount = fCount + 0.01

	## Create the warp flash.
	pFlashAction1 = App.TGScriptAction_Create(__name__, "HyperdriveFlash", pShipID)
	pEngageWarpSeq.AddAction(pFlashAction1, None, fTimeToFlash)

	# Hide the ship.
	pHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShipID, 1)
	pEngageWarpSeq.AddAction(pHideShip, pFlashAction1, 1.6)

	pUnBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShipID, 0, 1.0)
	pEngageWarpSeq.AddAction(pUnBoostAction, pHideShip)
	
	pCheckTowing = App.TGScriptAction_Create(__name__, "EngageSeqTractorCheckI", pShipID)
	pEngageWarpSeq.AddAction(pCheckTowing, pUnBoostAction)	

	pEnWarpSeqEND = App.TGScriptAction_Create(sCustomActionsScript, "NoAction")
	pEngageWarpSeq.AddAction(pEnWarpSeqEND, pUnBoostAction, 2.5)

	############### exiting begins ########

	if (pPlayer != None) and (pShipID == pPlayer.GetObjID()):
		# Force a noninteractive cinematic view in space..
		pCinematicStart = App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0)
		pExitWarpSeq.AddAction(pCinematicStart, None)

		pDisallowInput = App.TGScriptAction_Create("MissionLib", "RemoveControl")
		pExitWarpSeq.AddAction(pDisallowInput, pCinematicStart)

		# Add actions to move the camera in the destination set to watch the placement,
		# so we can watch the ship come in.
		# Initial position is reverse chasing the placement the ship arrives at.
		pCameraAction4 = App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", pcDest, pPlayer.GetName())
		pExitWarpSeq.AddAction(pCameraAction4, pDisallowInput)
	
	# Hide the ship.
	pHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShipID, 1)
	pExitWarpSeq.AddAction(pHideShip, None)

	# Check for towee
	if hasTractorReady == 1:
		pHideTowee = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pInstance.BSTransDimensionalDriveISITowee, 1)
		pExitWarpSeq.AddAction(pHideTowee, pHideShip)

	## Create the warp flash.
	pFlashAction2 = App.TGScriptAction_Create(__name__, "HyperdriveFlash", pShipID)
	pExitWarpSeq.AddAction(pFlashAction2, pHideShip, 0.7)

	# Un-Hide the ship
	pUnHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShipID, 0)
	pExitWarpSeq.AddAction(pUnHideShip, pFlashAction2, 1.5)

	# Un-hide the Towee, plus if it exists, also set up the maintain chain
	## REMEMBER: any changes in the time of this sequence will also require a re-check of this part, to make sure
	##	   we're making the right amount of MaintainTowing actions.
	if hasTractorReady == 1:
		pUnHideTowee = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pInstance.BSTransDimensionalDriveISITowee, 0)
		pExitWarpSeq.AddAction(pUnHideTowee, pUnHideShip)
		fCount = 0.0
		while fCount < 3.6:
			pMaintainTowingAction = App.TGScriptAction_Create(__name__, "MaintainTowingActionI", pShip.GetObjID())
			pExitWarpSeq.AddAction(pMaintainTowingAction, pUnHideTowee, fCount)
			fCount = fCount + 0.01
			if fCount >= 3.6:
				break
		pEMaintainTowingAction = App.TGScriptAction_Create(__name__, "removeTractorISITowInfo", pShip.GetObjID())
		pExitWarpSeq.AddAction(pEMaintainTowingAction, pUnHideTowee, fCount + 0.3)

	# Give it a little boost
	pBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShipID, 1, 10.0)
	pExitWarpSeq.AddAction(pBoostAction, pUnHideShip, 0.1)

	# Play the vushhhhh of exiting warp
	pWarpSoundAction2 = App.TGScriptAction_Create(__name__, "PlayHyperdriveSounds", pShipID, "Exit Warp", sRace)
	pExitWarpSeq.AddAction(pWarpSoundAction2, pBoostAction)
	
	# Make the ship return to normal speed.
	pUnBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShipID, 0, 1.0)
	pExitWarpSeq.AddAction(pUnBoostAction, pWarpSoundAction2, 2.0)

	# IMPORTANT: These three actions below are an extra added for intra-system intercept since we need to ensure the cutscene really ends and control is returned to the player.
	# This could be handled on the main AlternateSubModelFTL script but I'm leaving it here to allow better customization

	if (pPlayer != None) and (pShipID == pPlayer.GetObjID()):
		pActionCSE0 = App.TGScriptAction_Create("MissionLib", "ReturnControl")
		pExitWarpSeq.AddAction(pActionCSE0, pUnBoostAction, 0.5)
		pActionCSE1 = App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", sSet)
		pExitWarpSeq.AddAction(pActionCSE1, pUnBoostAction, 0.1)
		pActionCSE2 = App.TGScriptAction_Create("MissionLib", "EndCutscene")
		pExitWarpSeq.AddAction(pActionCSE2, pUnBoostAction, 0.1)

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
	# 1º: the engaging travel sequence  (plays once, when the ship enters the travel)
	# 2º: the during travel sequence    (plays repeatedly, while the ship is travelling)
	# 3º: the exiting travel sequence   (plays once, when the ship exits travel)

	# Note that each one of them can be None, if you don't want to have that sequence in your travel method.

	return [pEngageWarpSeq, fTimeToFlash + 2.5, pExitWarpSeq]

# An aux function I used
def ProperTunnelTexture(pShip):
	# Custom tunnel textures?
	fTunnel = MissionLib.GetShip("Hyperdrive Outer", myGlobalpSet)
	fTunnel2 = MissionLib.GetShip("Hyperdrive Inner", myGlobalpSet)
	pModule = __import__(pShip.GetScript())

	GFX = "scripts/Custom/Hyperdrive/GFX/Hyperspace2.tga"
	# Is there a customization for this ship available?
	if hasattr(pModule, "HyperdriveCustomizations"):
		pCustomization = pModule.HyperdriveCustomizations()
            
		# Customization exists, but does the tunnel texture entry exist?!
		if pCustomization.has_key('TunnelTexture'):
			# Bingo, replace textures for both tunnels then
			GFX = "scripts/Custom/Hyperdrive/GFX/" + pCustomization['TunnelTexture']


	fTunnel.ReplaceTexture(GFX, "outer_glow")
	fTunnel2.ReplaceTexture(GFX, "outer_glow")

	fTunnel.RefreshReplacedTextures()
	fTunnel2.RefreshReplacedTextures()

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
	#	warp sequences ARE REQUIRED if you want to be able to succesfully (and beautifully)
	#	   tractor ships thru your travel. (in this example, thru warp)
	################################################################################

	pWS = self.TravelerSequence	
	
	sCustomActionsScript = "Custom.GalaxyCharts.WarpSequence_Override"
	
	try:
		from Custom.QBautostart.Libs.LibWarp import GetEntryDelayTime
		fEntryDelayTime = GetEntryDelayTime()
	except:
		fEntryDelayTime = 1.0
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

	## disable during warp seq because for now WARP gfx effect doesn't have the need of any during warp seq fx
	## and then, if it is None, the Travel won't try to use it
	#if pWS.DuringWarpSeq == None:
	#	pWS.DuringWarpSeq = App.TGSequence_Create()
	#pDuringWarpSeq = App.TGSequence_Create()

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
	
	if (pPlayer != None) and (pShipID == pPlayer.GetObjID()):
		fEntryDelayTime = fEntryDelayTime + 1.0

		# Force a noninteractive cinematic view in space..
		pCinematicStart = App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0)
		pEngageWarpSeq.AddAction(pCinematicStart, None)
		try:
			ProperTunnelTexture(pShip)
		except:
			traceback.print_exc()

		pDisallowInput = App.TGScriptAction_Create("MissionLib", "RemoveControl")
		pEngageWarpSeq.AddAction(pDisallowInput, pCinematicStart)

		# Ensure we have customizations set:

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

	pWarpSoundAction1 = App.TGScriptAction_Create(__name__, "PlayHyperdriveSounds", pShipID, "Enter Warp", sRace)
	pEngageWarpSeq.AddAction(pWarpSoundAction1, None, fEntryDelayTime + 0.2)
	
	pBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShipID, 1, 100.0)
	pEngageWarpSeq.AddAction(pBoostAction, pWarpSoundAction1, 0.7)

	try:
		import Custom.NanoFXv2.WarpFX.WarpFX
		pNacelleFlash = Custom.NanoFXv2.WarpFX.WarpFX.CreateNacelleFlashSeq(pShip, pShip.GetRadius())
		pEngageWarpSeq.AddAction(pNacelleFlash, pWarpSoundAction1)
		pWS.Logger.LogString("Using Nacelle Flash Sequence from NanoFXv2")
	except:
		pass

	fTimeToFlash = 3.5 + fEntryDelayTime -1.3
	if pWS.Travel.bTractorStat == 1:
		fCount = 0.0
		while fCount < fTimeToFlash:
			pMaintainTowingAction = App.TGScriptAction_Create(sCustomActionsScript, "MaintainTowingAction", pWS)
			pEngageWarpSeq.AddAction(pMaintainTowingAction, None, fCount)
			fCount = fCount + 0.01
			if fCount >= fTimeToFlash:
				break

	## Create the warp flash.
	pFlashAction1 = App.TGScriptAction_Create(__name__, "HyperdriveFlash", pShipID) #pFlashAction1 = App.TGScriptAction_Create("Actions.EffectScriptActions", "WarpFlash", pShip)
	pEngageWarpSeq.AddAction(pFlashAction1, None, fTimeToFlash)

	# Hide the ship.
	pHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShipID, 1)
	pEngageWarpSeq.AddAction(pHideShip, pFlashAction1, 1.6)

	pUnBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShipID, 0, 1.0)
	pEngageWarpSeq.AddAction(pUnBoostAction, pHideShip)
	
	pCheckTowing = App.TGScriptAction_Create(sCustomActionsScript, "EngageSeqTractorCheck", pWS)
	pEngageWarpSeq.AddAction(pCheckTowing, pHideShip)	

	pEnWarpSeqEND = App.TGScriptAction_Create(sCustomActionsScript, "NoAction")
	pEngageWarpSeq.AddAction(pEnWarpSeqEND, pUnBoostAction, 2.5)

	############### exiting begins ########

	# Add the actions for exiting warp only if the destination set exists.
	if(pWS.GetDestinationSet() != None):
		if (pPlayer != None) and (pShipID == pPlayer.GetObjID()):
			# Force a noninteractive cinematic view in space..
			pCinematicStart = App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0)
			pExitWarpSeq.AddAction(pCinematicStart, None)

			pDisallowInput = App.TGScriptAction_Create("MissionLib", "RemoveControl")
			pExitWarpSeq.AddAction(pDisallowInput, pCinematicStart)

			# Add actions to move the camera in the destination set to watch the placement,
			# so we can watch the ship come in.
			# Initial position is reverse chasing the placement the ship arrives at.
			pCameraAction4 = App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", pcDest, pPlayer.GetName())
			pExitWarpSeq.AddAction(pCameraAction4, pDisallowInput)
	
		# Hide the ship.
		pHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShipID, 1)
		pExitWarpSeq.AddAction(pHideShip, None)

		# Check for towee
		if pWS.Travel.bTractorStat == 1:
			pHideTowee = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pWS.Travel.Towee.GetObjID(), 1)
			pExitWarpSeq.AddAction(pHideTowee, pHideShip)

		## Create the warp flash.
		pFlashAction2 = App.TGScriptAction_Create(__name__, "HyperdriveFlash", pShipID)  #pFlashAction2 = App.TGScriptAction_Create("Actions.EffectScriptActions", "WarpFlash", pShip)
		pExitWarpSeq.AddAction(pFlashAction2, pHideShip, 0.7)

		# Un-Hide the ship
		pUnHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShipID, 0)
		pExitWarpSeq.AddAction(pUnHideShip, pFlashAction2, 1.5)

		# Un-hide the Towee, plus if it exists, also set up the maintain chain
		## REMEMBER: any changes in the time of this sequence will also require a re-check of this part, to make sure
		##	   we're making the right amount of MaintainTowing actions.
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
		pBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShipID, 1, 100.0)
		pExitWarpSeq.AddAction(pBoostAction, pUnHideShip, 0.1)

		# Play the vushhhhh of exiting warp
		pWarpSoundAction2 = App.TGScriptAction_Create(__name__, "PlayHyperdriveSounds", pShipID, "Exit Warp", sRace)
		pExitWarpSeq.AddAction(pWarpSoundAction2, pBoostAction)
	
		# Make the ship return to normal speed.
		pUnBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShipID, 0, 1.0)
		pExitWarpSeq.AddAction(pUnBoostAction, pWarpSoundAction2, 2.0)

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
	# 1º: the engaging travel sequence  (plays once, when the ship enters the travel)
	# 2º: the during travel sequence    (plays repeatedly, while the ship is travelling)
	# 3º: the exiting travel sequence   (plays once, when the ship exits travel)

	# Note that each one of them can be None, if you don't want to have that sequence in your travel method.

	return [pEngageWarpSeq, None, pExitWarpSeq]


########
# Method to return "starting travel" events, much like those START_WARP events.
# must return a list with the events, possibly none (empty list)
########
def GetStartTravelEvents(self):
	debug(__name__ + ", GetStartTravelEvents")
	return GetStartTravelEventsI(self.Ship)

# Aux. ISI function
def GetStartTravelEventsI(pShip):
	debug(__name__ + ", GetStartTravelEventsI")

	pEvent = App.TGEvent_Create()
	sOriAdress = pEvent.this
	sOriAdress = sOriAdress[0:len(sOriAdress)-7]
	sAdress = sOriAdress+"WarpEvent"
	pSWNEvent = App.WarpEvent(sAdress)
	pSWNEvent.SetEventType(ENGAGING_ALTERNATEFTLSUBMODEL)
	pSWNEvent.SetDestination(pShip)

	# You need to perform these for each event you want, else you get ctd (crash-to-desktop)
	pEvent2e = App.TGEvent_Create()
	sOriAdress2e = pEvent2e.this
	sOriAdress2e = sOriAdress2e[0:len(sOriAdress2e)-7]
	sAdress2e = sOriAdress2e+"WarpEvent"

	pSWNEvent2 = App.WarpEvent(sAdress2e)
	pSWNEvent2.SetEventType(App.ET_START_WARP_NOTIFY)
	pSWNEvent2.SetDestination(pShip)

	return [ pSWNEvent, pSWNEvent2 ]

########
# Method to return "exiting travel" events, much like those EXITED_SET or EXITED_WARP events.
# must return a list with the events, possibly none (empty list)
########
def GetExitedTravelEvents(self):
	debug(__name__ + ", GetExitedTravelEvents")
	return GetExitedTravelEventsI(self.Ship)

# Aux. ISI function
def GetExitedTravelEventsI(pShip):
	debug(__name__ + ", GetExitedTravelEventsI")
	pEvent = App.TGStringEvent_Create()
	pEvent.SetEventType(App.ET_EXITED_SET)
	pEvent.SetDestination(pShip)
	pEvent.SetString("warp")

	pEvent2 = App.TGStringEvent_Create()
	pEvent2.SetEventType(DISENGAGING_ALTERNATEFTLSUBMODEL)
	pEvent2.SetDestination(pShip)
	pEvent2.SetString("warp")

	return [ pEvent, pEvent2 ]

########
# Method to return the travel set to use.
# must return a App.SetClass instance, it can't be None.
# NOTE: for the moment, this is probably the best way to make if ships can, or can not, be chased while warping.
########
def GetTravelSetToUse(self, manual = 0):
	global myGlobalpSet, myGlobalAISet
	try:
		import Custom.GalaxyCharts.Traveler
		import Custom.GalaxyCharts.TravelerSystems.HyperdriveTravel
		import Custom.GalaxyCharts.TravelerSystems.AIHyperdriveTravel
		pSet = None
		if manual != 0:
			if manual == 1:
				if myGlobalpSet == None:
					myGlobalpSet = Custom.GalaxyCharts.TravelerSystems.HyperdriveTravel.Initialize()
				return myGlobalpSet
			else:
				if myGlobalAISet == None:
					myGlobalAISet = Custom.GalaxyCharts.TravelerSystems.AIHyperdriveTravel.Initialize()
				return myGlobalAISet
		if self.IsPlayer == 1:
			if myGlobalpSet == None:
				myGlobalpSet = Custom.GalaxyCharts.TravelerSystems.HyperdriveTravel.Initialize()
			pSet = myGlobalpSet
		elif self.IsPlayer == 0 and self.IsAIinPlayerRoute == 1:
			if myGlobalpSet == None:
				myGlobalpSet = Custom.GalaxyCharts.TravelerSystems.HyperdriveTravel.Initialize()
			pSet = myGlobalpSet
		elif self.IsPlayer == 0 and self.IsAIinPlayerRoute == 0:
			if myGlobalAISet == None:
				myGlobalAISet = Custom.GalaxyCharts.TravelerSystems.HyperdriveTravel.Initialize()
			pSet = myGlobalAISet
		return pSet
	except:
		print "Error on ", __name__, "GetTravelSetToUse. Please read the in-file documentation for possible ways to fix it."
		traceback.print_exc()
		self._LogError("GetTravelSetToUse")

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
	return None

########
# Method to convert the speed this ship is travelling at to Cs ("c" is the physical constant that is equal to the speed of light, in km/h. So,
# in other words, this method should convert the "speed" of the ship, which is relative to this travelling method, to how many times is the ship
# travelling faster than the speed of light.
# must return a float  (like 1.0)
########
def ConvertSpeedAmount(fSpeed):
	if fSpeed >= 1.999:
		fFacA = 2.88		##### Do Not Change These Values #####
		fFacB = 8.312	       ##### Do Not Change These Values #####
	elif fSpeed > 1.99:
		fFacA = 2.88		##### Do Not Change These Values #####
		fFacB = 7.512	       ##### Do Not Change These Values #####
	elif fSpeed > 1.6:
		fFacA = 2.8700	      ##### Do Not Change These Values #####
		fFacB = 5.9645	      ##### Do Not Change These Values #####
	elif fSpeed <= 1.6:
		fFacA = 3.0		 ##### Do Not Change These Values #####
		fFacB = 3.0		 ##### Do Not Change These Values #####

	speed = 1.0
	if fSpeed <= 1.0:
		speed = (math.pow(fSpeed, (10.0/3.0)) + math.pow((10.0-fSpeed), (-11.0/3.0)))
	else:
		iSpeed = 1.0 # 
		if fSpeed <= 2.0:
			iSpeed = (fSpeed - 1.0) * 10.0
		else:
			iSpeed = fSpeed * 80.0 - 150
		
		speed = (math.pow(iSpeed, (10.0/fFacA)))

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
	debug(__name__ + ", GetActualMaxSpeed")
	pWarpEngines = self.Ship.GetWarpEngineSubsystem()
	fPower = 1.0
	fRealMaxSpeed = self.GetMaxSpeed()
	if pWarpEngines != None:
		if self.IsPlayer == 1:
			fPower = pWarpEngines.GetPowerPercentageWanted()
		else:
			fPower = self.AIwarpPower
	else:
		if fRealMaxSpeed != 0:
			mySpeed = self.GetSpeed()
			if mySpeed is None or mySpeed > fMaximumSpeed or mySpeed > fRealMaxSpeed:
				mySpeed = fRealMaxSpeed
			elif mySpeed < fMinimumSpeed:
				mySpeed = fRealMaxSpeed
			fPower = mySpeed/fRealMaxSpeed
		else:
			fPower = 1.0

	fAMWS = (fRealMaxSpeed * fPower) - (fPower - 1.0)
	if fAMWS > fMaximumSpeed:
		fAMWS = fMaximumSpeed
	return fAMWS

########
# Method to return the actual cruise speed of this travelling method that this travel instance (ship) can achieve.
# By "actual", I mean, in the current circunstances, like for example: in warp, engine power affects cruise speed. So the actual cruise speed
# that the ship can achieve will be different than the normal cruise speed if engine power is not at 100%.
# must return a float  (like 1.0)
########
def GetActualCruiseSpeed(self):
	debug(__name__ + ", GetActualCruiseSpeed")

	fPower = 1.0
	pWarpEngines = self.Ship.GetWarpEngineSubsystem()
	fRealCruiseSpeed = self.GetCruiseSpeed()
	if pWarpEngines != None:
		if self.IsPlayer == 1:
			fPower = pWarpEngines.GetPowerPercentageWanted()
		else:
			fPower = self.AIwarpPower
	else:
		if fRealCruiseSpeed != 0:
			mySpeed = self.GetSpeed()
			if mySpeed is None or mySpeed > fMaximumSpeed or mySpeed > fRealCruiseSpeed:
				mySpeed = fRealCruiseSpeed
			elif mySpeed < fMinimumSpeed:
				mySpeed = fRealCruiseSpeed

			fPower = mySpeed/fRealCruiseSpeed
		else:
			fPower = 1.0

	fACWS = (fRealCruiseSpeed * fPower) - (fPower - 1.0)
	if fACWS > fMaximumSpeed:
		fACWS = fMaximumSpeed
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

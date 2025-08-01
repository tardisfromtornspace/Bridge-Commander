# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# GC is ALL Rights Reserved by USS Frontier, but since GC supports Plugins it is fair to release a new TravellingMethod or patch old ones as long as the files remain unmodified.
# SporeDrive.py
# prototype custom travelling method plugin script, by USS Frontier (Enhanced Warp, original) and then modified by Alex SL Gato for Spore Drive
# 14th April 2025
#################################################################################################################
##########	MANUAL
#################################################################################################################
# NOTE: all functions/methods and attributes defined here (in this prototype example plugin, SporeDrive) are required to be in the plugin, with the exclusion of:
# ------ MODINFO, which is there just to verify versioning.
# ------ ALTERNATESUBMODELFTL METHODS subsection, which are exclusively used for alternate SubModels for FTL which is a separate but linked mod, or to import needed modules.
# ------ Auxiliar functions: "AuxProtoElementNames", "CreateDetachedElectricExplosion", "CreateElectricExplosion", "CustomBoostShipSpeed", "findShipInstance", "LoadGFX", "MainPartRotation", "PlacementOffsetOrbitWatch", "PlaySporeDriveSound", "SporeDriveBasicConfigInfo", "SporeDriveDisabledCalculations", "SporeDriveEnterFlash" and "SporeElectricField".
# ------ Auxiliar variables: "myGlobalAISet" and "myGlobalpSet" used for keeping tabs on our alternate pSets.
# ------ Auxiliar functions for intra-system intercept (ISI) support, which as a result of being a common-made function between default GalaxyCharts functions/methods, regular AlternateSubModelFTL and ISI, while not required to be on the plugin, some of their contents are actually required if they are not there: "CanTravelShip", "EngageSeqTractorCheckI", "GetEngageDirectionC", "GetEngageDirectionISI", "GetExitedTravelEventsI", "GetStartTravelEventsI", "MainPartRotationI", "PlaySporeDriveSoundI", "MaintainTowingActionI", "removeTractorISITowInfo", "SetupSequenceISI", "SetupTowingI".
# NOTE 2: This version of SporeDrive also has Intra-System Intercept functions, meaning a SubMenu appears on the Helm menu to allow for a slipstream-like intercept. For more info on this, see the Manual for AlternateSubModelFTL and the comments on this file.
# === How-To-Add ===
# This Travelling Method is Ship-based, on this case it needs of Foundation and FoundationTech to verify if the ship is equipped with it.
# This FTL method check is stored inside an "Alternate-Warp-FTL" dictionary, which is a script that should be located at scripts/Custom/Techs/AlternateSubModelFTL.py. While this sub-tech can work totally fine without such module installed, it is recommended to have it.
# On this case, due to that, only the lines marked with "# (#)" are needed for Spore-Drive to work, but the final parent technology may require more:
# "Spore-Drive": is the name of the key. This is the bare minimum for the technology to work
# "Nacelles": is the name of a key whose value indicates a list of which warp engine property children (nacelles) are part of the Spore-Drive system. If all are disabled/destroyed, Spore-Drive will not engage. If this field does not exist, it will check all warp hardpoints containing "SporeDrive", "spore drive" or "spore-drive" (case-insensitive). Leave as "Nacelles": [] to make it skip this disabled check.
# "Core": is the name of a key whose value indicates a list of which hardpoint properties (not nacelles) are part of the Spore-Drive system. If all are disabled/destroyed, Spore-Drive will not engage either. If this field does not exist or "Core": [] this check will be skipped.
# "NormalRotation", "EndRotation" and "Time": Indicates in what way the main body rotates while performing the FTL Spore Drive Action, from the "normal" rotation position, to the "end" rotation position, in "Time" centiseconds. Leave them blank to use a default [0, 0, 0] and [0, 4.19, 0] in 2 seconds. In both rotation cases, the fields are the X, Y and Z axis. Please note that "Time" will also affect how soon the final entry flash happens.
# "ExitDirection": when the ship drops out of this FTL method, in what direction it moves. Do not include to call default "Down".
# "CamDistance": when the ship enters Spore Drive, how far is the camera from the vessel. Default is 25.
# "UncloakDistance": when the ship ends an ISI, radius around it where cloaked ships can be decloaked, in kilometers. Negative values are ignored. Default is 25 km.
# "UncloakChance": when the ship ends an ISI, chance that a ship inside the cloak disruption AOE actually decloaks, with the value being in percentage. Default is 25, that is 25% chance of being uncloaked.
# "I Sparks Chance": Sometimes when performing a jump, some extra sparks appear before the jump. This keys holds the value which indicates that chance, on a 0-100 effective range. Default is 0.
# "O Sparks Chance": Sometimes when performing a jump, some extra sparks appear after the jump. This keys holds the value which indicates that chance, on a 0-100 effective range. Default is 0.
# "Enter Sparks Density": when sparks happen before the jump, this value indicates how many. Default is 0.
# "Exit Sparks Density": when sparks happen before the jump, this value indicates how many. Default is 0.
# "Sparks Size": when sparks happen, this value indicates relative size with respect to the ship. Default is 0.05 (5% of the ship's size).
"""
#Sample Setup: replace "USSProtostar" for the appropiate abbrev. Also remove "# (#)"
Foundation.ShipDef.USSProtostar.dTechs = { # (#)
	"Alternate-Warp-FTL": { # (#)
		"Setup": { # (#)
			"Spore-Drive": {	"Nacelles": ["Proto Warp Nacelle"], "Core": ["Proto-Core"], "NormalRotation": [0, 0, 0], "EndRotation" : [0, 4.19, 0], "Time": 200, "ExitDirection": "Down", "CamDistance": 25, "UncloakDistance": 25, "UncloakChance": 25, "I Sparks Chance": 30, "O Sparks Chance": 30, "Enter Sparks Density": 3, "Exit Sparks Density": 3, "Sparks Size": 0.05,}, # (#)
			"Body": "VasKholhr_Body",
			"NormalModel":          shipFile,
			"WarpModel":          "VasKholhr_WingUp",
			"Spore-DriveModel":          "VasKholhr_WingUp",
			"AttackModel":          "VasKholhr_WingDown",
			"BodySetScale": 1.0,
			"NormalSetScale": 1.0,
			"WarpSetScale": 1.0,
			"Spore-DriveSetScale": 1.0,
			"AttackSetScale": 1.0,
			"Hardpoints":       {
				"Proto Warp Nacelle":  [0.000000, 0.000000, 0.075000],
			},

			"AttackHardpoints":       {
				"Proto Warp Nacelle":  [0.000000, -0.250000, 2.075000],
			},
			"WarpHardpoints":       {
				"Proto Warp Nacelle":  [0.000000, -0.250000, -2.075000],
			},
			"Spore-DriveHardpoints":       {
				"Proto Warp Nacelle":  [0.000000, -1.000000, -2.075000],
			},
		}, # (#)

		"Port Wing":     ["VasKholhr_Portwing", {
			"SetScale": 1.0
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0], # normal Rotation used if not Red Alert and if not Warp
			"AttackRotation":         [0, -0.6, 0],
			"AttackDuration":         200.0, # Value is 1/100 of a second
			"AttackPosition":         [0, 0, 0.03],
			"WarpRotation":       [0, 0.349, 0],
			"WarpPosition":       [0, 0, 0.02],
			"WarpDuration":       150.0,
			"Spore-DriveRotation":       [0, 0.749, 0],
			"Spore-DrivePosition":       [0, 0, 0.05],
			"Spore-DriveDuration":       150.0,
			},
		],
        
		"Starboard Wing":     ["VasKholhr_Starboardwing", {
			"SetScale": 1.0
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0],
			"AttackRotation":         [0, 0.6, 0],
			"AttackDuration":         200.0, # Value is 1/100 of a second
			"AttackPosition":         [0, 0, 0.03],
			"WarpRotation":       [0, -0.349, 0],
			"WarpPosition":       [0, 0, 0.02],
			"WarpDuration":       150.0,
			"Spore-DriveRotation":       [0, -0.749, 0],
			"Spore-DrivePosition":       [0, 0, 0.05],
			"Spore-DriveDuration":       150.0,
			},
		],
	}, # (#)
} # (#)
"""
#
#################################################################################################################
##########	END OF MANUAL
#################################################################################################################
#################################################################################################################
#
MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "0.52",
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
sName = "Spore-Drive"

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
# if a ship can change its destination while travelling.
########
bCanChangeCourse = 1

########
# if a ship can change its speed while travelling.
########
bCanChangeSpeed = 1

########
# Phrase to show when ship is engaging this travelling method, the destination name is automatically added to the end
# so, like in warp, for example, it'll be "Warping to Kronos..."
########
sGoingTo = "Using Spore-Drive to travel to"

########
# Phrase to show when the ship drops out of travel (while travelling)
########
sDropOut = "Dropped out of Spore-Drive..."

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
# NOTE: on this file several of the imports have been moved above for better understanding

ENGAGING_ALTERNATEFTLSUBMODEL = App.UtopiaModule_GetNextEventType() # For when we are immediately about to fly with this FTL method
DISENGAGING_ALTERNATEFTLSUBMODEL = App.UtopiaModule_GetNextEventType() # For when we are immediately about to stop flying with this FTL method
# Due to AlternateSubModelFTL implementation, only 1 function can cover 1 event, no multiple functions can cover the same event directly. While on regular implementation of these SubModel FTL method that limits nothing, if you want multiple functions to respond, you must create a parent function of sorts that calls all the other functions you want, or create some sort of alternate listener inside some function.

# Because we could end on an endless loop, the imports must be done inside the functions, else the game will not recognize any attribute or function beyond that
# Reason I'm doing this function pass beyond just passing input parameters to the common function is to allow other TravellingMethod modders more flexibility
# from Custom.Techs.AlternateSubModelFTL import StartingSporeDrive, ExitSetProto

def KindOfMove(): 
	return "Spore-Drive" # Modify this with the name you are gonna use for the AlternateSubModelFTL

def StartingFTLAlternateSubModel(pObject, pEvent, techP, move): # What actions does AlternateSubModelFTL need to do when entering this FTL method
	if move == None:
		move = KindOfMove()

	from Custom.Techs.AlternateSubModelFTL import StartingProtoWarp
	StartingProtoWarp(pObject, pEvent, techP, move)

def AlternateFTLActionEnteringWarp(): # Linking eType with the function
	return ENGAGING_ALTERNATEFTLSUBMODEL, StartingFTLAlternateSubModel

def ExitSetFTLAlternateSubModel(pObject, pEvent, techP, move): # What actions does AlternateSubModelFTL need to do when exiting this FTL method
	if move == None:
		move = KindOfMove()

	from Custom.Techs.AlternateSubModelFTL import ExitSetProto
	ExitSetProto(pObject, pEvent, techP, move)

def AlternateFTLActionExitWarp(): # Linking eType with the function
	return DISENGAGING_ALTERNATEFTLSUBMODEL, ExitSetFTLAlternateSubModel

def InSystemIntercept():
	propulsionType = sName # The name for its subMenu option
	eEntryEvent = GetStartTravelEventsI
	eExitEvent = GetExitedTravelEventsI
	eSequenceFunction = SetupSequenceISI # Important NOTE - This sequence is gonna be a modification of the normal sequences for changing systems. Since intra-system does not call pre-engage nor post-engage functions on its own (only the entry and exit events), if you have an actual pre-engage and post-engage function that is not just a mere "return", you may want to adjust your sequence to call them instead at the appropiate time.
	isEquipped = IsShipEquipped
	eCanTravel = CanTravelShip
	awayNavPointDistance = awayNavPointDistanceCalc # This is a custom multiplier value, used for checking when a ship is too close to a planet or ship. A lower value means that it will allow closer ISI, while a higher value will make that ISI inner proximity limit be further. Negative values are set to 0.
	engageDirection = GetEngageDirectionISI

	return propulsionType, eEntryEvent, eExitEvent, eSequenceFunction, isEquipped, eCanTravel, awayNavPointDistance, engageDirection

def awayNavPointDistanceCalc(pShipID=None):
	return 0.2

#######################################
# "IsShipEquipped" Method to check if the ship is equipped with this travelling method.
# Must return 1 if it has it, 0 if it does not.
# NOTE: this function is not used as a method of the Travel class as are the other functions here.
#       this is actually used just like a helper for the Travel Manager.
########
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
	debug(__name__ + ", IsShipEquipped")
	pWarpEngines = pShip.GetWarpEngineSubsystem()
	if pWarpEngines:
		pInstance = findShipInstance(pShip)
		if not pInstance:
			return 0

		pInstanceDict = pInstance.__dict__
		if pInstanceDict.has_key("Alternate-Warp-FTL") and pInstanceDict["Alternate-Warp-FTL"].has_key("Setup") and pInstanceDict["Alternate-Warp-FTL"]["Setup"].has_key("Spore-Drive"): # You need to add a foundation technology to this vessel "AlternateSubModelFTL"
			return 1
		else:
			return 0
	else:
		return 0


########
# "CanTravel" Method to check if the ship can travel.
# Must return 1 if it can, otherwise return a string(reason why the ship couldn't travel)
########
# This is just an auxiliar function I made for this
def AuxProtoElementNames(*args):
	# Returns hardpoint property name fragments that indicate are part of the Spore-Drive system, and blacklists
	return ["sporedrive", "proto warp", "spore-drive"], ["not a sporedrive", "not a spore drive", "not a spore-drive", " not sporedrive", " not spore drive", " not spore-drive"]

# This is just another auxiliar function I made for this
def SporeDriveBasicConfigInfo(pShip):
	pInstance = findShipInstance(pShip) # On this case, IsShipEquipped(pShip) already checked this for us - HOWEVER do not forget to check if you modify the script
	pInstancedict = None
	specificNacelleHPList = None 
	specificCoreHPList = None
	normalRot = None
	endRot = None
	exitDir = None
	myTime = 200.0
	myDistance = 25
	enterDensity = 0
	sparksChanceI = 0
	exitDensity = 0
	sparksChanceO = 0
	sparkSize = 0.05
	if pInstance:
		pInstancedict = pInstance.__dict__ 
		if pInstancedict.has_key("Alternate-Warp-FTL") and pInstancedict["Alternate-Warp-FTL"].has_key("Setup") and pInstancedict["Alternate-Warp-FTL"]["Setup"].has_key("Spore-Drive"):
			if pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"].has_key("Nacelles"): # Use: if the tech has this field, use it. Must be a list. "[]" would mean that this field is skipped during checks.
				specificNacelleHPList = pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"]["Nacelles"]
			if pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"].has_key("Core"): # Use: if the tech has this field, use it. Must be a list. "[]" would mean that this field is skipped during checks.
				specificCoreHPList = pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"]["Core"]

			if pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"].has_key("NormalRotation"):
				normalRot = pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"]["NormalRotation"]
			if pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"].has_key("EndRotation"):
				endRot = pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"]["EndRotation"]
			if pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"].has_key("ExitDirection"):
				exitDir = pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"]["ExitDirection"]
			if pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"].has_key("Time"):
				myTime = pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"]["Time"]
			if pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"].has_key("CamDistance"): # Use: if the tech has this field, use it. Must be a list. "[]" would mean that this field is skipped during checks.
				myDistance = pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"]["CamDistance"]

			if pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"].has_key("Enter Sparks Density"):
				enterDensity = pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"]["Enter Sparks Density"]
			if pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"].has_key("Exit Sparks Density"):
				exitDensity = pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"]["Exit Sparks Density"]
			if pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"].has_key("I Sparks Chance"):
				sparksChanceI = pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"]["I Sparks Chance"]
			if pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"].has_key("O Sparks Chance"):
				sparksChanceO = pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"]["O Sparks Chance"]
			if pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"].has_key("Sparks Size") and pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"]["Sparks Size"] >= 0:
				sparkSize = pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"]["Sparks Size"]

	hardpointProtoNames, hardpointProtoBlacklist = AuxProtoElementNames()

	return pInstance, pInstancedict, specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, normalRot, endRot, exitDir, myTime, myDistance, enterDensity,	sparksChanceI, exitDensity, sparksChanceO, sparkSize

# This is just another auxiliar function I made for this
def SporeDriveDisabledCalculations(type, specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, pSubsystem, pShip):
	totalSporeDriveEngines = 0
	onlineSporeDriveEngines = 0
	if type == "Nacelle":	
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
						totalSporeDriveEngines = totalSporeDriveEngines + 1
						if pChild.GetCondition() > 0.0 and not pChild.IsDisabled():
							onlineSporeDriveEngines = onlineSporeDriveEngines + 1
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
						found = (pSubsystemName in specificCoreHPList)

						if found:
							totalSporeDriveEngines = totalSporeDriveEngines + 1
							if pSubsystema.GetCondition() > 0.0 and not pSubsystema.IsDisabled():
								onlineSporeDriveEngines = onlineSporeDriveEngines + 1

		pShipList.TGDoneIterating()
		pShipList.TGDestroy()

	return totalSporeDriveEngines, onlineSporeDriveEngines

def CanTravel(self): # NOTE: Requires CanTravelShip
	debug(__name__ + ", CanTravel")
	return CanTravelShip(self.GetShip())

# Auxiliar ISI function
def CanTravelShip(pShip):
	debug(__name__ + ", CanTravelShip")
	pPlayer = App.Game_GetCurrentPlayer()
	bIsPlayer = 0
	if pPlayer and pShip.GetObjID() == pPlayer.GetObjID():
		bIsPlayer = 1
	pHelm = App.CharacterClass_GetObject(App.g_kSetManager.GetSet("bridge"), "Helm")

	isEquipped = IsShipEquipped(pShip)
	if not isEquipped:
		if bIsPlayer == 1:
			if pHelm:
				App.CharacterAction_Create(pHelm, App.CharacterAction.AT_SAY_LINE, "BrexNothingToAdd7", None, 1).Play() # Brex speaking through Kiska, ventriloquism
			else:
				# No character, display subtitle only.
				pDatabase = App.g_kLocalizationManager.Load ("data/TGL/Bridge Crew General.tgl")
				if pDatabase:
					pSequence = App.TGSequence_Create ()
					pSubtitleAction = App.SubtitleAction_Create (pDatabase, "BrexNothingToAdd7") #CantWarp5
					pSubtitleAction.SetDuration (3.0)
					pSequence.AddAction (pSubtitleAction)
					pSequence.Play ()
					App.g_kLocalizationManager.Unload (pDatabase)
		return "This ship is not equipped with Spore-Drive"

	#pImpulseEngines = pShip.GetImpulseEngineSubsystem()
	#if not pImpulseEngines:
	#	return "No Impulse Engines"

	#if (pImpulseEngines.GetPowerPercentageWanted() == 0.0):
	#	# Ship is trying to warp with their engines off.
	#	if bIsPlayer == 1:
	#		pXO = App.CharacterClass_GetObject(App.g_kSetManager.GetSet("bridge"), "XO")
	#		if pXO:
	#			MissionLib.QueueActionToPlay(App.CharacterAction_Create(pXO, App.CharacterAction.AT_SAY_LINE, "EngineeringNeedPowerToEngines", None, 1))
	#	return "Impulse Engines offline"

	pInstance, pInstancedict, specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, _ , _ , _ , _ , _ , _ , _ , _ , _ , _ = SporeDriveBasicConfigInfo(pShip)

	pWarpEngines = pShip.GetWarpEngineSubsystem()
	if specificNacelleHPList == None or (specificNacelleHPList != None and len(specificNacelleHPList) > 0):
		if pWarpEngines:
			totalSporeDriveEngines, onlineSporeDriveEngines = SporeDriveDisabledCalculations("Nacelle", specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, pWarpEngines, pShip)

			if totalSporeDriveEngines <= 0 or onlineSporeDriveEngines <= 0:
				if bIsPlayer == 1:
					if pHelm:
						App.CharacterAction_Create(pHelm, App.CharacterAction.AT_SAY_LINE, "CantWarp1", None, 1).Play()
					else:
						# No character, display subtitle only.
						pDatabase = App.g_kLocalizationManager.Load ("data/TGL/Bridge Crew General.tgl")
						if pDatabase:
							pSequence = App.TGSequence_Create ()
							pSubtitleAction = App.SubtitleAction_Create (pDatabase, "CantWarp1")
							pSubtitleAction.SetDuration (3.0)
							pSequence.AddAction (pSubtitleAction)
							pSequence.Play ()
							App.g_kLocalizationManager.Unload (pDatabase)

				return "Spore-Drive Engines disabled"
		
			if not pWarpEngines.IsOn():
				if bIsPlayer == 1:
					if pHelm:
						App.CharacterAction_Create(pHelm, App.CharacterAction.AT_SAY_LINE, "CantWarp5", None, 1).Play()
					else:
						# No character, display subtitle only.
						pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Crew General.tgl")
						if pDatabase:
							pSequence = App.TGSequence_Create()
							pSubtitleAction = App.SubtitleAction_Create(pDatabase, "CantWarp5")
							pSubtitleAction.SetDuration(3.0)
							pSequence.AddAction(pSubtitleAction)
							pSequence.Play()
							App.g_kLocalizationManager.Unload(pDatabase)
				return "Spore-Drive Engines offline"
		else:
			return "Spore-Drive Engines non-existant"

	if specificCoreHPList != None and len(specificCoreHPList) > 0:
		totalSporeDriveCores, onlineSporeDriveCores = SporeDriveDisabledCalculations("Core", specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, pWarpEngines, pShip)

		if totalSporeDriveCores <= 0 or onlineSporeDriveCores <= 0:
			if bIsPlayer == 1:
				if pHelm:
					App.CharacterAction_Create(pHelm, App.CharacterAction.AT_SAY_LINE, "CantWarp1", None, 1).Play()
				else:
					# No character, display subtitle only.
					pDatabase = App.g_kLocalizationManager.Load ("data/TGL/Bridge Crew General.tgl")
					if pDatabase:
						pSequence = App.TGSequence_Create ()
						pSubtitleAction = App.SubtitleAction_Create (pDatabase, "CantWarp1")
						pSubtitleAction.SetDuration (3.0)
						pSequence.AddAction (pSubtitleAction)
						pSequence.Play ()
						App.g_kLocalizationManager.Unload (pDatabase)
			return "All proto-cores are disabled"

	pSet = pShip.GetContainingSet()
	#pNebula = pSet.GetNebula()
	#if pNebula:
	#	if pNebula.IsObjectInNebula(pShip):
	#		if bIsPlayer == 1:
	#			if pHelm:
	#				App.CharacterAction_Create(pHelm, App.CharacterAction.AT_SAY_LINE, "CantWarp2", None, 1).Play()
	#			else:
	#				# No character, display subtitle only.
	#				pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Crew General.tgl")
	#				if pDatabase:
	#					pSequence = App.TGSequence_Create()
	#					pSubtitleAction = App.SubtitleAction_Create(pDatabase, "CantWarp2")
	#					pSubtitleAction.SetDuration(3.0)
	#					pSequence.AddAction(pSubtitleAction)
	#					pSequence.Play()
	#					App.g_kLocalizationManager.Unload(pDatabase)
	#		return "Inside Nebula"

	# See if we are in an asteroid field
	#AsteroidFields = pSet.GetClassObjectList(App.CT_ASTEROID_FIELD)
	#for i in AsteroidFields:
	#	pField = App.AsteroidField_Cast(i)
	#	if pField:
	#		if pField.IsShipInside(pShip):
	#			if bIsPlayer == 1:
	#				if pHelm:
	#					App.CharacterAction_Create(pHelm, App.CharacterAction.AT_SAY_LINE, "CantWarp4", None, 1).Play()
	#				else:
	#					# No character, display subtitle only.
	#					pDatabase = App.g_kLocalizationManager.Load ("data/TGL/Bridge Crew General.tgl")
	#					if pDatabase:
	#						pSequence = App.TGSequence_Create ()
	#						pSubtitleAction = App.SubtitleAction_Create (pDatabase, "CantWarp4")
	#						pSubtitleAction.SetDuration (3.0)
	#						pSequence.AddAction (pSubtitleAction)
	#						pSequence.Play ()
	#						App.g_kLocalizationManager.Unload (pDatabase)
	#			return "Inside Asteroid Field"
					
	#pStarbase12Set = App.g_kSetManager.GetSet("Starbase12")
	#if pStarbase12Set:
	#	if pShip.GetContainingSet():
	#		if pStarbase12Set.GetObjID() == pShip.GetContainingSet().GetObjID():
	#			pStarbase12 = App.ShipClass_GetObject(pStarbase12Set, "Starbase 12")
	#			if pStarbase12:
	#				import AI.Compound.DockWithStarbase
	#				if AI.Compound.DockWithStarbase.IsInViewOfInsidePoints(pShip, pStarbase12):
	#					if bIsPlayer == 1:
	#						if pHelm:
	#							App.CharacterAction_Create(pHelm, App.CharacterAction.AT_SAY_LINE, "CantWarp3", None, 1).Play()
	#						else:
	#							# No character, display subtitle only.
	#							pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Crew General.tgl")
	#							if pDatabase:
	#								pSequence = App.TGSequence_Create()
	#								pSubtitleAction = App.SubtitleAction_Create(pDatabase, "CantWarp3")
	#								pSubtitleAction.SetDuration(3.0)
	#								pSequence.AddAction(pSubtitleAction)
	#								pSequence.Play()
	#								App.g_kLocalizationManager.Unload(pDatabase)
	#					return "Inside Starbase12"
	return 1

########
# Method to check if the ship can continue travelling (she's travelling, yeah)
# must return 1 if she can, 0 if she can't travel anymore (thus will forcibly drop out).
########
def CanContinueTravelling(self):
	debug(__name__ + ", CanContinueTravelling")
	pShip = self.GetShip()
	pPlayer = App.Game_GetCurrentPlayer()
	bIsPlayer = 0
	if pPlayer and pShip.GetObjID() == pPlayer.GetObjID():
		bIsPlayer = 1
	pWarpEngines = pShip.GetWarpEngineSubsystem()
	bStatus = 1

	isEquipped = IsShipEquipped(pShip)
	if not isEquipped:
		if bIsPlayer == 1:
			pSequence = App.TGSequence_Create ()
			pSubtitleAction = App.SubtitleAction_CreateC("Brex: We don't have Spore-Drive sir, we are dropping out of it.")
			pSubtitleAction.SetDuration(3.0)
			pSequence.AddAction(pSubtitleAction)
			pSequence.Play()
		bStatus = 0
	else:
		pInstance, pInstancedict, specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, _ , _ , _ , _ , _ , _ , _ , _ , _ , _ = SporeDriveBasicConfigInfo(pShip)
		if pInstance and pInstancedict:
			totalSporeDriveCores, onlineSporeDriveCores = SporeDriveDisabledCalculations("Core", specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, pWarpEngines, pShip)
			if totalSporeDriveCores > 0 and onlineSporeDriveCores <= 0:
				if bIsPlayer == 1:
					pSequence = App.TGSequence_Create ()
					pSubtitleAction = App.SubtitleAction_CreateC("Brex: All Spore-Drive cores are offline or disabled sir, we are dropping out of Spore-Drive.")
					pSubtitleAction.SetDuration(3.0)
					pSequence.AddAction(pSubtitleAction)
					pSequence.Play()
				bStatus = 0
			elif (specificNacelleHPList == None or (specificNacelleHPList != None and len(specificNacelleHPList) > 0)):
				totalSporeDriveEngines = 0
				onlineSporeDriveEngines = 0
				if pWarpEngines != None:
					totalSporeDriveEngines, onlineSporeDriveEngines = SporeDriveDisabledCalculations("Nacelle", specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, pWarpEngines, pShip)
				if pWarpEngines == None or (totalSporeDriveEngines > 0 and onlineSporeDriveEngines <= 0):
					if bIsPlayer == 1:
						pSequence = App.TGSequence_Create ()
						pSubtitleAction = App.SubtitleAction_CreateC("Brex: All Spore-Drive nacelles are offline or disabled sir, we are dropping out of Spore-Drive.")
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
def GetEngageDirection(self): # NOTE: Requires GetEngageDirectionC
	debug(__name__ + ", GetEngageDirection")
	return GetEngageDirectionC(self, None)

# Aux. ISI function.
def GetEngageDirectionISI(pPlayerID): # NOTE: Requires GetEngageDirectionC
	debug(__name__ + ", GetEngageDirectionISI")
	return GetEngageDirectionC(None, pPlayerID)

def GetEngageDirectionC(mySelf, pPlayerID = None):
	"""
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
	"""
	return None

########
# Method to do travelling method specific stuff before the ship engages travel. At this point, ship is already due to engage travel, that is,
# passed the checks to see if she can travel and is starting the travelling procedures.
# return value is not important.
########
def PreEngageStuff(self):
	debug(__name__ + ", PreEngageStuff")

	return

########
# Method to do travelling method specific stuff before the ship exits travel. This happens right before the ship changes set to enter the its destination.
# return value is not important.
########
def PreExitStuff(self):
	debug(__name__ + ", PreExitStuff")
	
	return

########
# Method to setup the GFX effect sequences, and return them in the order:
# 1� entering travel sequence
# 2� during travel sequence
# 3� exiting travel sequence
########
# Another aux function I made
def PlaySporeDriveSound(pAction, pWS, sType, sRace):
	debug(__name__ + ", PlaySporeDriveSound")

	pShip = pWS.GetShip()
	return PlaySporeDriveSoundI(pAction, pShip, sType, sRace)

# Aux. ISI function
def PlaySporeDriveSoundI(pAction, pShip, sType, sRace):
	debug(__name__ + ", PlaySporeDriveSoundI")

	pPlayer = App.Game_GetCurrentPlayer()
	if pShip == None or pPlayer == None:
		return 0					

	pSet = pShip.GetContainingSet()
	pPlaSet = pPlayer.GetContainingSet()
	if pSet == None or pPlaSet == None:
		return 0

	if pSet.GetRegionModule() == pPlaSet.GetRegionModule():
		try:
			import Custom.NanoFXv2.WarpFX.WarpFX
			siType = ""
			if sRace == "":
				sRace = "Default"
			if sType == "Enter Warp":
				siType = "EnterSporeDrive"
			elif sType == "Exit Warp":
				siType = "ExitSporeDrive"
			else:
				siType = ""
			if siType != "":
				sFile = "sfx\\SporeDrive\\"+sRace+"\\"+sRace+siType+".wav"
				Custom.GravityFX.GravityFXlib.PlaySound(sFile, sRace+" "+siType+" Sound")
		except:
			try:
				sRace = "Default"
				siType = ""
				if sType == "Enter Warp":
					siType = "EnterSporeDrive"
				elif sType == "Exit Warp":
					siType = "ExitSporeDrive"
				else:
					siType = ""
				if siType != "":
					sFile = "sfx\\SporeDrive\\"+sRace+"\\"+sRace+siType+".wav"
					Custom.GravityFX.GravityFXlib.PlaySound(sFile, sRace+" "+siType+" Sound")
			except:
				print "SporeDrive TravellingMethod: error while calling PlaySporeDriveSound:"
				traceback.print_exc()
	return 0

# Another aux function I made
def MainPartRotation(pAction, pWS, sRace, back):
	debug(__name__ + ", MainPartRotation")	
	pShip = pWS.GetShip()
	return MainPartRotationI(pAction, pShip, sRace, back)

# Aux. ISI function
def MainPartRotationI(pAction, pShip, sRace, back):
	debug(__name__ + ", MainPartRotationI")
	if pShip:
		pInstance = findShipInstance(pShip) # On this case, IsShipEquipped(pShip) already checked this for us - HOWEVER do not forget to check if you modify the script
		pInstancedict = None
		if pInstance:
			pInstancedict = pInstance.__dict__ 
			if pInstancedict.has_key("Alternate-Warp-FTL") and pInstancedict["Alternate-Warp-FTL"].has_key("Setup") and pInstancedict["Alternate-Warp-FTL"]["Setup"].has_key("Spore-Drive"):
				if not pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"].has_key("NormalRotation"):
					pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"]["NormalRotation"] = [0, 0, 0]
				specificBeginningRotation = pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"]["NormalRotation"]
				if not pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"].has_key("EndRotation"):
					pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"]["EndRotation"] = [0, 4.19, 0]
				specificEndRotation = pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"]["EndRotation"]
				if not pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"].has_key("Time"):
					pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"]["Time"] = 200 # in centi-seconds
				myTime = pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"]["Time"]
				
				dOptionsList = { "Experimental": 1}

				iRotStepX =  0
				iRotStepY =  0
				iRotStepY =  0

				if myTime != 0:
					iRotStepX =  (specificEndRotation[0] - specificBeginningRotation[0])/(myTime)
					iRotStepY =  (specificEndRotation[1] - specificBeginningRotation[1])/(myTime)
					iRotStepZ =  (specificEndRotation[2] - specificBeginningRotation[2])/(myTime)
				if back != 0:
					iRotStepX = - iRotStepX
					iRotStepY = - iRotStepY
					iRotStepZ = - iRotStepZ

				from Custom.Techs.AlternateSubModelFTL import performRotationAndScaleAdjust
				performRotationAndScaleAdjust(pShip, pShip, dOptionsList, 0, 0, 0, iRotStepX, iRotStepY, iRotStepZ, 0)
	return 0

# Another aux function I made
def CustomBoostShipSpeed(pAction, sCustomActionsScript, ShipID, bBoost, fBoostScale, vDir):

	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), ShipID)
	if pShip:
		vDirec = None
		if vDir != None and vDir != "Fwd" and vDir != "Forward":
			if vDir == "Back":
				vDirec = pShip.GetWorldBackwardTG()
			elif vDir == "Up":
				vDirec = pShip.GetWorldUpTG()
			elif vDir == "Down":
				vDirec = pShip.GetWorldDownTG()
			elif vDir == "Right":
				vDirec = pShip.GetWorldRightTG()
			elif vDir == "Left":
				vDirec = pShip.GetWorldLeftTG()

		if sCustomActionsScript != None:
			try:
				banana = __import__(sCustomActionsScript, globals(), locals(), ["BoostShipSpeed"])
			except:
				banana = __import__(sCustomActionsScript, globals(), locals())

			if banana and hasattr(banana, "BoostShipSpeed"):
				banana.BoostShipSpeed(pAction, ShipID, bBoost, fBoostScale, vDirec)

	return 0

# Another aux function I made
def PlacementOffsetOrbitWatch(pAction, pCamera, distance, sMode = "FreeOrbit"):
	debug(__name__ + ", PlacementOffsetOrbitWatch")
	if pCamera:
		Camera.NewMode(pCamera, sMode, 0, 1, [("MinimumDistance", distance * 0.5), ("Distance", distance), ("MaximumDistance", distance * 1.5)], 1) # From CameraModes.py
		pCamera.Update(App.g_kUtopiaModule.GetGameTime())

	return 0

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
			if hasattr(pInstance, "SporeDriveISIvTowPosition"):
				del pInstance.SporeDriveISIvTowPosition
		except:
			print "SporeDrive: Error while calling removeTractorISITowInfo"
			traceback.print_exc()
		try:
			if hasattr(pInstance, "SporeDriveISITowee"):
				del pInstance.SporeDriveISITowee
		except:
			print "SporeDrive: Error while calling removeTractorISITowInfo"
			traceback.print_exc()
		try:
			if hasattr(pInstance, "SporeDriveISIbTractorStat"):
				del pInstance.SporeDriveISIbTractorStat
		except:
			print "SporeDrive: Error while calling removeTractorISITowInfo"
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

		pInstance.SporeDriveISIvTowPosition = pTarget.GetWorldLocation()
		pInstance.SporeDriveISIvTowPosition.Subtract( pShip.GetWorldLocation() )
		pInstance.SporeDriveISIvTowPosition.MultMatrixLeft( pShip.GetWorldRotation().Transpose() )

		pInstance.SporeDriveISITowee = pTarget.GetObjID()

		pInstance.SporeDriveISIbTractorStat = 1

	except:
		print "SporeDrive: Error while calling SetupTowingI"
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
		if hasattr(pInstance, "SporeDriveISIbTractorStat") and pInstance.SporeDriveISIbTractorStat == 1:
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

			if not hasattr(pInstance, "SporeDriveISITowee"):
				return 0

			targetID = pInstance.SporeDriveISITowee
			pTempTargetAux = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), targetID)
			if not pTempTargetAux:
				return 0

			# Update/Maintain the towee's position and speed with the tower.
			vPosition = App.TGPoint3()
			vPosition.Set( pInstance.SporeDriveISIvTowPosition )
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
		print "SporeDrive: Error while calling MaintainTowingActionI"
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

	if hasattr(pInstance, "SporeDriveISIbTractorStat") and pInstance.SporeDriveISIbTractorStat == 1 and hasattr(pInstance, "SporeDriveISITowee") and pInstance.SporeDriveISITowee != None:
		# hide the towee

		pToweeShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pInstance.SporeDriveISITowee)
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

# An auxiliar function
def checkISINearbyRecloaking(pAction, pShipID):
	if pShipID != None:
		pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShipID)
		if pShip:
			pSet = pShip.GetContainingSet()
			if not pSet:
				return 0

			pInstance = findShipInstance(pShip)
			if not pInstance:
				return 0

			pProx = pSet.GetProximityManager()
			if not pProx:
				return 0

			iRange = 25
			iChance = 25
			ticksPerKilometer = 225/40.0 # 225 is approximately 40 km, so 225/40 is the number of ticks per kilometer

			pInstancedict = pInstance.__dict__
			if pInstancedict.has_key("Alternate-Warp-FTL") and pInstancedict["Alternate-Warp-FTL"].has_key("Setup") and pInstancedict["Alternate-Warp-FTL"]["Setup"].has_key("Spore-Drive"):
				if pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"].has_key("UncloakDistance") and pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"]["UncloakDistance"] >= 0:
					iRange = pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"]["UncloakDistance"]
				if pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"].has_key("UncloakChance"):
					iChance = pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"]["UncloakChance"]

			kIter = pProx.GetNearObjects(pShip.GetWorldLocation(), iRange * ticksPerKilometer, 1) 
			while 1:
				pObject = pProx.GetNextObject(kIter)
				if not pObject:
					break

				vibechecker = 0
				if not pObject.GetName() == pShip.GetName():
					if pObject.IsTypeOf(App.CT_SHIP):
						pkShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pObject.GetObjID())
						if pkShip and (App.g_kSystemWrapper.GetRandomNumber(100) <= iChance):
							pCloak = pkShip.GetCloakingSubsystem()
							if pCloak:
								pkInstance = findShipInstance(pkShip)
								if not pkInstance:
									pCloak.InstantDecloak()
								else:
									pkInstanceDict = pkInstance.__dict__
									if not (pkInstanceDict.has_key("Phase Cloak") or pkInstanceDict.has_key("Phased Cloak")):
										pCloak.InstantDecloak()
			pProx.EndObjectIteration(kIter)
	return 0

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

# Aux. function grabebd from VonFrank's Remastered Effects.py
def CreateElectricExplosion(fSize, fLife, pEmitFrom, bOwnsEmitFrom, pEffectRoot, fRed, fGreen, fBlue, fFrequency = 1.0, fEmitLife=1, fSpeed=2.0, sFile = 'data/Textures/Effects/RegularElectricExplosion.tga'):
	
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
def SporeElectricField(pAction, pShipID, sType, sRace, amount=5, sparkSize=0.05, delay=2.0, sFile = 'data/Textures/Effects/RegularElectricExplosion.tga'):
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShipID)
	if not pShip:
		return 0
	if pShip == None:
		return 0

	colorKey = [100.0 / 255, 1.0 / 255, 255.0 / 255]
	try:
		import Custom.NanoFXv2.NanoFX_Lib
		colorKey = Custom.NanoFXv2.NanoFX_Lib.GetOverrideColor(pShip, sType)
		if colorKey == None:
			colorKey = [100.0 / 255, 255.0 / 255, 255.0 / 255]
	except:
		colorKey = [100.0 / 255, 255.0 / 255, 1.0 / 255]

	iCycleCount = 1
	if amount > 0 and sparkSize > 0:
		pElectricShockSequence = App.TGSequence_Create()

		pShipNode = pShip.GetNode()
		rShip = pShip.GetRadius()

		LoadGFX(8, 1, sFile)

		while (iCycleCount < amount):
			try:
				pEmitPos = pShip.GetRandomPointOnModel()
				pExplosion = CreateElectricExplosion(rShip * sparkSize, 1.0, pEmitPos, 0, pShipNode, colorKey[0], colorKey[1], colorKey[2], fFrequency = 0.09, fEmitLife=1.5, fSpeed=delay)
				pAExplosion = None
				if pExplosion != None:
					pAExplosion = App.EffectAction_Create(pExplosion)
				if pAExplosion != None:
					pElectricShockSequence.AddAction(pAExplosion, App.TGAction_CreateNull(), iCycleCount * 0.005)
			except:
				print "SporeDrive TravellingMethod: error while calling SporeElectricField:"
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

# Aux function. Create flash effect on a ship. Texture is a mix between VonFrank's Remastered electrical efect and Discovery Mycelial effect.
def SporeDriveEnterFlash(pAction, pShipID, sType, sRace, amount=3, sparkSize=5, sFile = 'data/Textures/Effects/SporeDriveElectricExplosion.tga'):
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShipID)
	if not pShip:
		return 0
	if pShip == None:
		return 0

	fEffectList = []
	try:
		iCycleCount = 0
		if amount > 0 and sparkSize > 0:
			colorKey = [100.0, 255.0 / 255, 255.0 / 255]
			try:
				import Custom.NanoFXv2.NanoFX_Lib
				colorKey = Custom.NanoFXv2.NanoFX_Lib.GetOverrideColor(pShip, sType)
				if colorKey == None:
					colorKey = [100.0 / 255, 255.0 / 255, 255.0 / 255]
			except:
				colorKey = [100.0 / 255, 255.0 / 255, 255.0 / 255]

			LoadGFX(8, 1, sFile)

			pAttachTo = pShip.GetContainingSet().GetEffectRoot()
			fSize = pShip.GetRadius() * sparkSize
			pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())

			while (iCycleCount < amount):
				try:
					rdm = (App.g_kSystemWrapper.GetRandomNumber(80) + 20) / 100.0
					#pEffect = CreateDetachedElectricExplosion(colorKey[0], colorKey[1], colorKey[2], fSize * rdm, 1.5, sFile, pEmitFrom, pAttachTo, fFrequency=0.09,fEmitLife=1.5,fSpeed=0.0)
					pEffect = CreateDetachedElectricExplosion(colorKey[0], colorKey[1], colorKey[2], fSize * rdm, 0.75, sFile, pEmitFrom, pAttachTo, fFrequency=0.09,fEmitLife=0.75,fSpeed=0.0)
					if pEffect:
						fEffect = App.EffectAction_Create(pEffect)
						if fEffect:
							fEffectList.append(fEffect)
				except:
					print "SporeDrive TravellingMethod: error while calling SporeDriveEnterFlash:"
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

# Some auxiliar global variables to allow set change and better sounds
myGlobalpSet = None
myGlobalAISet = None

# ISI function
def SetupSequenceISI(pShip=None):
	# you can use this function as an example on how to create your own 'SetupSequenceISI(self)' method for AlternateSubModelFTL
	# While it has to basically mirror the '.SetupSequence(self)' method below (albeit you could create totally different sequences if you want), it needs to remove any unecessary code that references to self or changing systems.
	# Also this intraSystem intercept does not automatically call PreEngage nor PostEngage functions, if you really need to call those, you would need to call them by yourself, and adapted to also not include references to self.
	# something of the style of "DoPreEngageStuffISI()" or something.
	debug(__name__ + ", SetupSequence")
	
	sCustomActionsScript = "Custom.GalaxyCharts.WarpSequence_Override"
	
	try:
		from Custom.QBautostart.Libs.LibWarp import GetEntryDelayTime
		fEntryDelayTime = GetEntryDelayTime()
	except:
		fEntryDelayTime = 1.0

	pPlayer = App.Game_GetCurrentPlayer()

	if (pShip == None):
		pShip = pPlayer

	if (pShip == None):
		return

	pShipID = pShip.GetObjID()
	SetupTowingI(pShipID)

	pInstance = findShipInstance(pShip)
	_, _, _, _, _, _, _ , _ , myExitDirection, myTime, myDistance, inDensity, inChance, exDensity, exChance, sparkSize = SporeDriveBasicConfigInfo(pShip)

	if myExitDirection == None or myExitDirection == "":
		myExitDirection = "Down"

	hasTractorReady = hasattr(pInstance, "SporeDriveISIbTractorStat") and (pInstance.SporeDriveISIbTractorStat == 1)

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
	#pDuringWarpSeq = App.TGSequence_Create() ## This is unused
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

	extraSoundTime = 0.0


	if (pPlayer != None) and (pShip.GetObjID() == pPlayer.GetObjID()):
		fEntryDelayTime = fEntryDelayTime + 1.0
		extraSoundTime = 0.01
		
		myCamera = Camera.GetPlayerCamera()

		# Force a noninteractive cinematic view in space..
		pCinematicStart = App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0)
		pEngageWarpSeq.AddAction(pCinematicStart, None)

		pDisallowInput = App.TGScriptAction_Create("MissionLib", "RemoveControl")
		#pEngageWarpSeq.AddAction(pDisallowInput, None)
		pEngageWarpSeq.AddAction(pDisallowInput, pCinematicStart)

		pCameraAction0 = App.TGScriptAction_Create(__name__, "PlacementOffsetOrbitWatch", myCamera, myDistance, "FreeOrbit")
		pEngageWarpSeq.AddAction(pCameraAction0, pDisallowInput)


	pWarpSoundAction1 = App.TGScriptAction_Create(__name__, "PlaySporeDriveSoundI", pShip, "Enter Warp", sRace)
	pEngageWarpSeq.AddAction(pWarpSoundAction1, None, extraSoundTime)

	# Extra added for more likeness
	rdmI = App.g_kSystemWrapper.GetRandomNumber(100)
	if rdmI < inChance:
		pWarpRegularEEffectAction1 = App.TGScriptAction_Create(__name__, "SporeElectricField", pShip.GetObjID(), "PlasmaFX", sRace, inDensity, sparkSize, 0)
		pEngageWarpSeq.AddAction(pWarpRegularEEffectAction1, None)
	
	pBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShip.GetObjID(), 1, 1.0)
	pEngageWarpSeq.AddAction(pBoostAction, pWarpSoundAction1, 0.01)

	#try:
	#	import Custom.NanoFXv2.WarpFX.WarpFX
	#	pNacelleFlash = Custom.NanoFXv2.WarpFX.WarpFX.CreateNacelleFlashSeq(pShip, pShip.GetRadius())
	#	pEngageWarpSeq.AddAction(pNacelleFlash, pWarpSoundAction1)
	#except:
	#	pass

	fTimeToFlash = (fEntryDelayTime) + (2*(App.WarpEngineSubsystem_GetWarpEffectTime()/2.0))

	fCount = 0.0
	while fCount < fTimeToFlash and (fCount * 100) <= myTime:
		if (fCount * 100) <= myTime:
			pRotateVessel = App.TGScriptAction_Create(__name__, "MainPartRotationI", pShip, sRace, 0)
			if pRotateVessel:
				pEngageWarpSeq.AddAction(pRotateVessel, None, fCount)
		if hasTractorReady == 1:
			pMaintainTowingAction = App.TGScriptAction_Create(__name__, "MaintainTowingActionI", pShip.GetObjID())
			pEngageWarpSeq.AddAction(pMaintainTowingAction, None, fCount)

		fCount = fCount + 0.01
		if fCount >= fTimeToFlash:
			break

	if fCount != fTimeToFlash:
		fTimeToFlash = fCount + 0.25

	# TO-DO Maybe create two ship clone copies?
	# Create the warp flash.
	#pFlashAction1 = App.TGScriptAction_Create("Actions.EffectScriptActions", "WarpFlash", pShip.GetObjID())
	pFlashAction1 = App.TGScriptAction_Create(__name__, "SporeDriveEnterFlash", pShip.GetObjID(), "WarpFX", sRace, 5, 5)
	pEngageWarpSeq.AddAction(pFlashAction1, None, fTimeToFlash)

	# Hide the ship.
	pHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShip.GetObjID(), 1)
	pEngageWarpSeq.AddAction(pHideShip, pFlashAction1)

	pUnBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShip.GetObjID(), 0, 0.0)
	pEngageWarpSeq.AddAction(pUnBoostAction, pHideShip)
	
	pCheckTowing = App.TGScriptAction_Create(__name__, "EngageSeqTractorCheckI", pShip.GetObjID())
	pEngageWarpSeq.AddAction(pCheckTowing, pHideShip)	

	pEnWarpSeqEND = App.TGScriptAction_Create(sCustomActionsScript, "NoAction")
	pEngageWarpSeq.AddAction(pEnWarpSeqEND, pUnBoostAction, 2.5)

	############### exiting begins ########

	if (pPlayer != None) and (pShip.GetObjID() == pPlayer.GetObjID()):
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
	pHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShip.GetObjID(), 1)
	pExitWarpSeq.AddAction(pHideShip, None)

	# Give it a little reverse boost (to avoid collisions)
	pBoostAAction = App.TGScriptAction_Create(__name__, "CustomBoostShipSpeed", sCustomActionsScript, pShip.GetObjID(), 1, -300.0, myExitDirection)
	pExitWarpSeq.AddAction(pBoostAAction, pHideShip)

	# Make the ship return to normal speed.
	pUnBoostAAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShip.GetObjID(), -1, 1.0)
	pExitWarpSeq.AddAction(pUnBoostAAction, pBoostAAction, 1.2)

	# Check for towee
	if hasTractorReady == 1:
		pHideTowee = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pInstance.SporeDriveISITowee, 1)
		pExitWarpSeq.AddAction(pHideTowee, pHideShip)

	# Create the warp flash.
	pFlashAction2 = App.TGScriptAction_Create("Actions.EffectScriptActions", "WarpFlash", pShip.GetObjID())
	pExitWarpSeq.AddAction(pFlashAction2, pUnBoostAAction)
	#pExitWarpSeq.AddAction(pFlashAction2, pHideShip, 1.2) #0.7

	# Un-Hide the ship
	pUnHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShip.GetObjID(), 0)
	pExitWarpSeq.AddAction(pUnHideShip, pFlashAction2, 0.01)

	# Extra added for more likeness
	rdmO = App.g_kSystemWrapper.GetRandomNumber(100)
	if rdmO < exChance:
		pWarpRegularEEffectAction2 = App.TGScriptAction_Create(__name__, "SporeElectricField", pShip.GetObjID(), "PlasmaFX", sRace, exDensity, sparkSize)
		pExitWarpSeq.AddAction(pWarpRegularEEffectAction2, pUnHideShip, 0.0)

	# Un-hide the Towee, plus if it exists, also set up the maintain chain
	## REMEMBER: any changes in the time of this sequence will also require a re-check of this part, to make sure
	##           we're making the right amount of MaintainTowing actions.
	if hasTractorReady == 1:
		pUnHideTowee = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pInstance.SporeDriveISITowee, 0)
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
	pBoostAction = App.TGScriptAction_Create(__name__, "CustomBoostShipSpeed", sCustomActionsScript, pShip.GetObjID(), 1, 300.0, myExitDirection)
	pExitWarpSeq.AddAction(pBoostAction, pUnHideShip)

	# Play the vushhhhh of exiting warp
	pWarpSoundAction2 = App.TGScriptAction_Create(__name__, "PlaySporeDriveSoundI", pShip, "Exit Warp", sRace)
	pExitWarpSeq.AddAction(pWarpSoundAction2, pBoostAction)
	
	# Make the ship return to normal speed.
	pUnBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShip.GetObjID(), -1, 1.0)
	pExitWarpSeq.AddAction(pUnBoostAction, pWarpSoundAction2, 1.2)

	# IMPORTANT: These three actions below are an extra added for intra-system intercept since we need to ensure the cutscene really ends and control is returned to the player.
	# This could be handled on the main AlternateSubModelFTL script but I'm leaving it here to allow better customization
	if (pPlayer != None) and (pShipID == pPlayer.GetObjID()):
		pActionCSE0 = App.TGScriptAction_Create("MissionLib", "ReturnControl")
		pExitWarpSeq.AddAction(pActionCSE0, pUnBoostAction, 0.5)
		pActionCSE1 = App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", sSet)
		pExitWarpSeq.AddAction(pActionCSE1, pUnBoostAction, 0.1)
		pActionCSE2 = App.TGScriptAction_Create("MissionLib", "EndCutscene")
		pExitWarpSeq.AddAction(pActionCSE2, pUnBoostAction, 0.1)

	# This is just a tiny extra, this vessel can uncloak nerby vessels which don't use a phased cloak

	pActionCSE3 = App.TGScriptAction_Create(__name__, "checkISINearbyRecloaking", pShip.GetObjID())
	pExitWarpSeq.AddAction(pActionCSE3, pUnBoostAction, 0.2)


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
	# 2�: the time between engaging and exiting sequences
	# 3�: the exiting travel sequence   (plays once, when the ship exits travel)

	# Note that each one of them can be None, if you don't want to have that sequence in your travel method.

	return [pEngageWarpSeq, fTimeToFlash + 2.5, pExitWarpSeq]


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
	#	   tractor ships thru your travel. (in this example, thru warp)
	################################################################################

	debug(__name__ + ", SetupSequence")
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

	pInstance = findShipInstance(pShip)
	
	_, _, _, _, _, _, _ , _ , myExitDirection, myTime, myDistance, inDensity, inChance, exDensity, exChance, sparkSize = SporeDriveBasicConfigInfo(pShip)
	if myExitDirection == None or myExitDirection == "":
		myExitDirection = "Down"

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

	extraSoundTime = 0.01
	if (pPlayer != None) and (pShip.GetObjID() == pPlayer.GetObjID()):
		fEntryDelayTime = fEntryDelayTime + 1.0
		extraSoundTime = 0.25
		pPlayerSet = pShip.GetContainingSet()
		myCamera = Camera.GetPlayerCamera()

		#myCamera = pSet.GetActiveCamera()
		#pMode = pCamera.GetNamedCameraMode("FreeOrbit")

		# Force a noninteractive cinematic view in space..
		pCinematicStart = App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0)
		pEngageWarpSeq.AddAction(pCinematicStart, None)

		pDisallowInput = App.TGScriptAction_Create("MissionLib", "RemoveControl")
		#pEngageWarpSeq.AddAction(pDisallowInput, None)
		pEngageWarpSeq.AddAction(pDisallowInput, pCinematicStart)

		pCameraAction0 = App.TGScriptAction_Create(__name__, "PlacementOffsetOrbitWatch", myCamera, myDistance, "FreeOrbit")
		pEngageWarpSeq.AddAction(pCameraAction0, pDisallowInput)


	pWarpSoundAction1 = App.TGScriptAction_Create(__name__, "PlaySporeDriveSound", pWS, "Enter Warp", sRace)
	pEngageWarpSeq.AddAction(pWarpSoundAction1, None, extraSoundTime)
	
	# Extra added for more likeness
	rdmI = App.g_kSystemWrapper.GetRandomNumber(100)
	if rdmI < inChance:
		pWarpRegularEEffectAction1 = App.TGScriptAction_Create(__name__, "SporeElectricField", pShip.GetObjID(), "PlasmaFX", sRace, inDensity, sparkSize, 0)
		pEngageWarpSeq.AddAction(pWarpRegularEEffectAction1, None)

	pBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShip.GetObjID(), 1, 1.0)
	pEngageWarpSeq.AddAction(pBoostAction, pWarpSoundAction1, 0.01)

	#try:
	#	import Custom.NanoFXv2.WarpFX.WarpFX
	#	pNacelleFlash = Custom.NanoFXv2.WarpFX.WarpFX.CreateNacelleFlashSeq(pShip, pShip.GetRadius())
	#	pEngageWarpSeq.AddAction(pNacelleFlash, pWarpSoundAction1)
	#	pWS.Logger.LogString("Using Nacelle Flash Sequence from NanoFXv2")
	#except:
	#	pass

	fTimeToFlash = (fEntryDelayTime) + (2*(App.WarpEngineSubsystem_GetWarpEffectTime()/2.0))

	fCount = 0.0
	while fCount < fTimeToFlash and (fCount * 100) <= myTime:
		if (fCount * 100) <= myTime:
			pRotateVessel = App.TGScriptAction_Create(__name__, "MainPartRotation", pWS, sRace, 0)
			if pRotateVessel:
				pEngageWarpSeq.AddAction(pRotateVessel, None, fCount)
		if pWS.Travel.bTractorStat == 1:
			pMaintainTowingAction = App.TGScriptAction_Create(sCustomActionsScript, "MaintainTowingAction", pWS)
			pEngageWarpSeq.AddAction(pMaintainTowingAction, None, fCount)

		fCount = fCount + 0.01
		if fCount >= fTimeToFlash:
			break

	if fCount != fTimeToFlash:
		fTimeToFlash = fCount + 0.25

	# TO-DO Maybe create two ship clone copies?
	# Create the warp flash.
	#pFlashAction1 = App.TGScriptAction_Create("Actions.EffectScriptActions", "WarpFlash", pShip.GetObjID())
	pFlashAction1 = App.TGScriptAction_Create(__name__, "SporeDriveEnterFlash", pShip.GetObjID(), "WarpFX", sRace, 5, 5)
	pEngageWarpSeq.AddAction(pFlashAction1, None, fTimeToFlash)

	# Hide the ship.
	pHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShip.GetObjID(), 1)
	pEngageWarpSeq.AddAction(pHideShip, pFlashAction1)

	pUnBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShip.GetObjID(), 0, 0.0)
	pEngageWarpSeq.AddAction(pUnBoostAction, pHideShip)
	
	pCheckTowing = App.TGScriptAction_Create(sCustomActionsScript, "EngageSeqTractorCheck", pWS)
	pEngageWarpSeq.AddAction(pCheckTowing, pHideShip)	

	pEnWarpSeqEND = App.TGScriptAction_Create(sCustomActionsScript, "NoAction")
	pEngageWarpSeq.AddAction(pEnWarpSeqEND, pUnBoostAction, 2.5)

	############### exiting begins ########

	# Add the actions for exiting warp only if the destination set exists.
	if(pWS.GetDestinationSet() != None):
		if (pPlayer != None) and (pShip.GetObjID() == pPlayer.GetObjID()):
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
		pHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShip.GetObjID(), 1)
		pExitWarpSeq.AddAction(pHideShip, None)

		# Check for towee
		if pWS.Travel.bTractorStat == 1:
			pHideTowee = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pWS.Travel.Towee.GetObjID(), 1)
			pExitWarpSeq.AddAction(pHideTowee, pHideShip)

		# Create the warp flash.
		pFlashAction2 = App.TGScriptAction_Create("Actions.EffectScriptActions", "WarpFlash", pShip.GetObjID())
		pExitWarpSeq.AddAction(pFlashAction2, pHideShip, 0.7)

		# Un-Hide the ship
		pUnHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShip.GetObjID(), 0)
		pExitWarpSeq.AddAction(pUnHideShip, pFlashAction2, 0.01)

		# Extra added for more likeness
		rdmO = App.g_kSystemWrapper.GetRandomNumber(100)
		if rdmO < exChance:
			pWarpRegularEEffectAction2 = App.TGScriptAction_Create(__name__, "SporeElectricField", pShip.GetObjID(), "PlasmaFX", sRace, exDensity, sparkSize)
			pExitWarpSeq.AddAction(pWarpRegularEEffectAction2, pUnHideShip, 0.0)

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
		pBoostAction = App.TGScriptAction_Create(__name__, "CustomBoostShipSpeed", sCustomActionsScript, pShip.GetObjID(), 1, 300.0, myExitDirection)
		pExitWarpSeq.AddAction(pBoostAction, pUnHideShip)

		# Play the vushhhhh of exiting warp
		pWarpSoundAction2 = App.TGScriptAction_Create(__name__, "PlaySporeDriveSound", pWS, "Exit Warp", sRace)
		pExitWarpSeq.AddAction(pWarpSoundAction2, pBoostAction)
	
		# Make the ship return to normal speed.
		pUnBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShip.GetObjID(), -1, 1.0)
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
def GetTravelSetToUse(self, manual=0):
	debug(__name__ + ", GetTravelSetToUse")
	global myGlobalpSet, myGlobalAISet
	try:
		import Custom.GalaxyCharts.Traveler
		import Custom.GalaxyCharts.TravelerSystems.MycelialNetworkTravelSet
		import Custom.GalaxyCharts.TravelerSystems.AIMycelialNetworkTravelSet
		pSet = None
		if manual == 1:
			if myGlobalpSet == None:
				myGlobalpSet = Custom.GalaxyCharts.TravelerSystems.MycelialNetworkTravelSet.Initialize()
			if myGlobalAISet == None:
				myGlobalAISet = Custom.GalaxyCharts.TravelerSystems.AIMycelialNetworkTravelSet.Initialize()	
		if self.IsPlayer == 1:
			if myGlobalpSet == None:
				try:
					myGlobalpSet = Custom.GalaxyCharts.TravelerSystems.MycelialNetworkTravelSet.Initialize()
					self.Logger.LogString(" -Initialized Mycelial Network Travel Set")
				except:
					print "ERROR on GetTravelSetToUse: "
					traceback.print_exc()
			pSet = myGlobalpSet
		elif self.IsPlayer == 0 and self.IsAIinPlayerRoute == 1:
			if myGlobalpSet == None:
				try:
					myGlobalpSet = Custom.GalaxyCharts.TravelerSystems.MycelialNetworkTravelSet.Initialize()
					self.Logger.LogString(" -Initialized Mycelial Network Travel Set")
				except:
					print "ERROR on GetTravelSetToUse: "
					traceback.print_exc()
			pSet = myGlobalpSet
		elif self.IsPlayer == 0 and self.IsAIinPlayerRoute == 0:
			if myGlobalAISet == None:
				try:
					myGlobalAISet = Custom.GalaxyCharts.TravelerSystems.AIMycelialNetworkTravelSet.Initialize()
					self.Logger.LogString(" -Initialized AI Mycelial Network Travel Set")
				except:
					print "ERROR on GetTravelSetToUse: "
					traceback.print_exc()
			pSet = myGlobalAISet
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
	debug(__name__ + ", ConvertSpeedAmount")

	if fSpeed <= 1.01:
		return 0.0001

	if fSpeed >= 9.999:
		fFacA = 2.88                ##### Do Not Change These Values #####
		fFacB = 8.312               ##### Do Not Change These Values #####
	elif fSpeed > 9.99:
		fFacA = 2.88                ##### Do Not Change These Values #####
		fFacB = 7.512               ##### Do Not Change These Values #####
	elif fSpeed > 9.6:
		fFacA = 2.8700              ##### Do Not Change These Values #####
		fFacB = 5.9645              ##### Do Not Change These Values #####
	elif fSpeed >= 5.0: # This was fSpeed <= 9.6
		fFacA = 3.0                 ##### Do Not Change These Values #####
		fFacB = 3.0                 ##### Do Not Change These Values #####
		fSpeed = 9.6 # I modified this, so Spore Drive can go far without those, and only if you want to go slow on purpose, you go slow
	elif fSpeed < 5.0:
		fFacA = 3.0                 ##### Do Not Change These Values #####
		fFacB = 3.0                 ##### Do Not Change These Values #####	

	speed = (math.pow(fSpeed, (10.0/fFacA)) + math.pow((10.0-fSpeed), (-11.0/fFacB)))
	return speed *420480*420480

########
# Method to return the normal max speed of this travelling method that this travel instance (ship) can achieve.
# For "normal", I mean, on normal circunstances, like for example, engines at 100% power.
# must return a float  (like 1.0)
########
def GetMaxSpeed(self):
	debug(__name__ + ", GetMaxSpeed")
	return self.Ship.GetMaxWarpSpeed()

########
# Method to return the normal cruise speed of this travelling method that this travel instance (ship) can achieve.
# For "normal", I mean, on normal circunstances, like for example, engines at 100% power.
# must return a float  (like 1.0)
########
def GetCruiseSpeed(self):
	debug(__name__ + ", GetCruiseSpeed")
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
	debug(__name__ + ", GetActualCruiseSpeed")
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
	debug(__name__ + ", GetDegradationSystems")
	pWarpEngines = self.Ship.GetWarpEngineSubsystem()
	return [ pWarpEngines ]

########
# Method to return the list of coordinates (points in space) in this set which the ship can activate this travelling method from.
# must return a list  (like [])
########
def GetLaunchCoordinatesList(pSet):
	debug(__name__ + ", GetLaunchCoordinatesList")
	return []
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# SporeDrive.py
# prototype custom travelling method plugin script, by USS Frontier (Enhanced Warp, original) and then modified by Alex SL Gato for Proto-Warp
# 19th November 2024
#################################################################################################################
##########	MANUAL
#################################################################################################################
# NOTE: all functions/methods and attributes defined here (in this prototype example plugin, SporeDrive) are required to be in the plugin, with the exclusion of:
# ------ MODINFO, which is there just to verify versioning.
# ------ ALTERNATESUBMODELFTL METHODS subsection, which are exclusively used for alternate SubModels for FTL which is a separate but linked mod, or to import needed modules.
# ------ Auxiliar functions: "AuxProtoElementNames", "findShipInstance", "PlaySporeDriveSound", "SporeDriveBasicConfigInfo" and "SporeDriveDisabledCalculations".
# === How-To-Add ===
# This Travelling Method is Ship-based, on this case it needs of Foundation and FoundationTech to verify if the ship is equipped with it.
# This FTL method check is stored inside an "Alternate-Warp-FTL" dictionary, which is a script that should be located at scripts/Custom/Techs/AlternateSubModelFTL.py. While this sub-tech can work totally fine without such module installed, it is recommended to have it.
# On this case, due to that, only the lines marked with "# (#)" are needed for Spore-Drive to work, but the final parent technology may require more:
# "Spore-Drive": is the name of the key. This is the bare minimum for the technology to work
# "Nacelles": is the name of a key whose value indicates a list of which warp engine property children (nacelles) are part of the Spore-Drive system. If all are disabled/destroyed, Spore-Drive will not engage. If this field does not exist, it will check all warp hardpoints containing "SporeDrive", "spore drive" or "spore-drive" (case-insensitive). Leave as "Nacelles": [] to make it skip this disabled check.
# "Core": is the name of a key whose value indicates a list of which hardpoint properties (not nacelles) are part of the Spore-Drive system. If all are disabled/destroyed, Spore-Drive will not engage either. If this field does not exist or "Core": [] this check will be skipped.
"""
#Sample Setup: replace "USSProtostar" for the appropiate abbrev. Also remove "# (#)"
Foundation.ShipDef.USSProtostar.dTechs = { # (#)
	"Alternate-Warp-FTL": { # (#)
		"Setup": { # (#)
			"Spore-Drive": {	"Nacelles": ["Proto Warp Nacelle"], "Core": ["Proto-Core"], }, # (#)
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
	    "Version": "0.1",
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
bCanTowShips = 0

########
# path and file name to engine degradation sound alert
########
sDegradationSoundFile = "scripts\\Custom\\GalaxyCharts\\Sounds\\DegradationAlert.wav"

########
# if this travelling method should show starstreaks while travelling
# (starstreaks options setup in Galaxy Charts UMM Configuration menu)
########
bUseStarstreaks = 1

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
	if pInstance:
		pInstancedict = pInstance.__dict__ 
		if pInstancedict.has_key("Alternate-Warp-FTL") and pInstancedict["Alternate-Warp-FTL"].has_key("Setup") and pInstancedict["Alternate-Warp-FTL"]["Setup"].has_key("Spore-Drive"):
			if pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"].has_key("Nacelles"): # Use: if the tech has this field, use it. Must be a list. "[]" would mean that this field is skipped during checks.
				specificNacelleHPList = pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"]["Nacelles"]
			if pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"].has_key("Core"): # Use: if the tech has this field, use it. Must be a list. "[]" would mean that this field is skipped during checks.
				specificCoreHPList = pInstancedict["Alternate-Warp-FTL"]["Setup"]["Spore-Drive"]["Core"]

	hardpointProtoNames, hardpointProtoBlacklist = AuxProtoElementNames()

	return pInstance, pInstancedict, specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist

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

def CanTravel(self):
	debug(__name__ + ", CanTravel")
	pShip = self.GetShip()
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

	pInstance, pInstancedict, specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist = SporeDriveBasicConfigInfo(pShip)

	pWarpEngines = pShip.GetWarpEngineSubsystem()
	if pWarpEngines:
		if pWarpEngines.IsDisabled():
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
			return "Warp Engines disabled"
		if specificNacelleHPList == None or (specificNacelleHPList != None and len(specificNacelleHPList) > 0):
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
			return "Warp or Spore-Drive Engines offline"
	else:
		return "No Warp Engines"

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
	AsteroidFields = pSet.GetClassObjectList(App.CT_ASTEROID_FIELD)
	for i in AsteroidFields:
		pField = App.AsteroidField_Cast(i)
		if pField:
			if pField.IsShipInside(pShip):
				if bIsPlayer == 1:
					if pHelm:
						App.CharacterAction_Create(pHelm, App.CharacterAction.AT_SAY_LINE, "CantWarp4", None, 1).Play()
					else:
						# No character, display subtitle only.
						pDatabase = App.g_kLocalizationManager.Load ("data/TGL/Bridge Crew General.tgl")
						if pDatabase:
							pSequence = App.TGSequence_Create ()
							pSubtitleAction = App.SubtitleAction_Create (pDatabase, "CantWarp4")
							pSubtitleAction.SetDuration (3.0)
							pSequence.AddAction (pSubtitleAction)
							pSequence.Play ()
							App.g_kLocalizationManager.Unload (pDatabase)
				return "Inside Asteroid Field"
					
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
	debug(__name__ + ", CanContinueTravelling")
	pShip = self.GetShip()
	pPlayer = App.Game_GetCurrentPlayer()
	bIsPlayer = 0
	if pPlayer and pShip.GetObjID() == pPlayer.GetObjID():
		bIsPlayer = 1
	pWarpEngines = pShip.GetWarpEngineSubsystem()
	bStatus = 1
	if pWarpEngines != None:
		if pWarpEngines.IsDisabled() == 1:
			if bIsPlayer == 1:
				pSequence = App.TGSequence_Create ()
				pSubtitleAction = App.SubtitleAction_CreateC("Brex: Warp engines are disabled sir, we are dropping out of warp.")
				pSubtitleAction.SetDuration(3.0)
				pSequence.AddAction(pSubtitleAction)
				pSequence.Play()
			bStatus = 0

		elif pWarpEngines.IsOn() == 0:
			if bIsPlayer == 1:
				pSequence = App.TGSequence_Create ()
				pSubtitleAction = App.SubtitleAction_CreateC("Brex: Warp engines are offline sir, we are dropping out of warp.")
				pSubtitleAction.SetDuration(3.0)
				pSequence.AddAction(pSubtitleAction)
				pSequence.Play()
			bStatus = 0

		if bStatus > 0:
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
				pInstance, pInstancedict, specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist = SporeDriveBasicConfigInfo(pShip)
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
						totalSporeDriveEngines, onlineSporeDriveEngines = SporeDriveDisabledCalculations("Nacelle", specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, pWarpEngines, pShip)
						if totalSporeDriveEngines > 0 and onlineSporeDriveEngines <= 0:
							if bIsPlayer == 1:
								pSequence = App.TGSequence_Create ()
								pSubtitleAction = App.SubtitleAction_CreateC("Brex: All Spore-Drive nacelles are offline or disabled sir, we are dropping out of Spore-Drive.")
								pSubtitleAction.SetDuration(3.0)
								pSequence.AddAction(pSubtitleAction)
								pSequence.Play()
							bStatus = 0
				else:
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
	# Get all the objects along the line that we'll
	# be warping through.
	debug(__name__ + ", GetEngageDirection")
	fRayLength = 4000.0
	vOrigin = self.Ship.GetWorldLocation()
	vEnd = self.Ship.GetWorldForwardTG()
	vEnd.Scale(fRayLength)
	vEnd.Add(vOrigin)
	
	lsObstacles = self.GetWarpObstacles(vOrigin, vEnd)
	# If we have no obstacles in the way, we're good.
	if len(lsObstacles) == 0:
		vZero = App.TGPoint3()
		vZero.SetXYZ(0, 0, 0)
		self.Ship.SetTargetAngularVelocityDirect(vZero)
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
			vRay.Add(self.Ship.GetWorldForwardTG())
			vRay.Unitize()

			vEnd = App.TGPoint3()
			vEnd.Set(vRay)
			vEnd.Scale(fRayLength)

			vEnd.Add(vOrigin)
			lsObstacles = self.GetWarpObstacles(vOrigin, vEnd)
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
# 1º entering travel sequence
# 2º during travel sequence
# 3º exiting travel sequence
########
# Anther aux function I made
def PlaySporeDriveSound(pAction, pWS, sType, sRace):
	debug(__name__ + ", PlayWarpSound")
	pShip = pWS.GetShip()
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
			if sRace == "":
				sRace = "Default"
			if sType == "Enter Warp":
				sType = "EnterSporeDrive"
			#elif sType == "Exit Warp":
			#	sType = "ExitSporeDrive"
			else:
				sType = ""
			if sType != "":
				sFile = "sfx\\SporeDrive\\"+sRace+"\\"+sRace+sType+".wav"
				Custom.GravityFX.GravityFXlib.PlaySound(sFile, sRace+" "+sType+" Sound")
		except:
			try:
				sRace = "Default"
				if sType == "Enter Warp":
					sFile = "sfx\\SporeDrive\\"+sRace+"\\"+sRace+sType+".wav"
					Custom.GravityFX.GravityFXlib.PlaySound(sFile, sRace+" "+sType+" Sound")
			except:
				print "SporeDrive TravellingMethod: error while calling PlaySporeDriveSound:"
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
	
	if (pPlayer != None) and (pShip.GetObjID() == pPlayer.GetObjID()):
		fEntryDelayTime = fEntryDelayTime + 1.0

		# Force a noninteractive cinematic view in space..
		pCinematicStart = App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0)
		pEngageWarpSeq.AddAction(pCinematicStart, None)

		#pWarpSoundAction0 = App.TGScriptAction_Create(__name__, "PlayProtoWarpSound", pWS, "Enter Warp", sRace)
		#pEngageWarpSeq.AddAction(pWarpSoundAction0, None, 0)

		pDisallowInput = App.TGScriptAction_Create("MissionLib", "RemoveControl")
		pEngageWarpSeq.AddAction(pDisallowInput, pCinematicStart)

	pWarpSoundAction1 = App.TGScriptAction_Create(sCustomActionsScript, "PlayWarpSound", pWS, "Enter Warp", sRace)
	pEngageWarpSeq.AddAction(pWarpSoundAction1, None, fEntryDelayTime + 0.2)
	
	pBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShip.GetObjID(), 1, 1.0)
	pEngageWarpSeq.AddAction(pBoostAction, pWarpSoundAction1, 0.7)

	try:
		import Custom.NanoFXv2.WarpFX.WarpFX
		pNacelleFlash = Custom.NanoFXv2.WarpFX.WarpFX.CreateNacelleFlashSeq(pShip, pShip.GetRadius())
		pEngageWarpSeq.AddAction(pNacelleFlash, pWarpSoundAction1)
		pWS.Logger.LogString("Using Nacelle Flash Sequence from NanoFXv2")
	except:
		pass

	fTimeToFlash = (fEntryDelayTime*2) + (2*(App.WarpEngineSubsystem_GetWarpEffectTime()/2.0))
	if pWS.Travel.bTractorStat == 1:
		fCount = 0.0
		while fCount < fTimeToFlash:
			pMaintainTowingAction = App.TGScriptAction_Create(sCustomActionsScript, "MaintainTowingAction", pWS)
			pEngageWarpSeq.AddAction(pMaintainTowingAction, None, fCount)
			fCount = fCount + 0.01
			if fCount >= fTimeToFlash:
				break

	# TO-DO Create also a USS Sovereign Slipstream drive based on this, using this sequence and extracting the engage and disengage events
	# TO-DO Maybe create two ship clone copies?
	# TO-DO Create flash sound
	#pWarpSoundAction0 = App.TGScriptAction_Create(__name__, "PlaySporeDriveSound", pWS, "Enter Warp", sRace)
	#pEngageWarpSeq.AddAction(pWarpSoundAction0, None, 0)
	# Create the warp flash.
	# TO-DO Replace with a spore-drive flash
	pFlashAction1 = App.TGScriptAction_Create("Actions.EffectScriptActions", "WarpFlash", pShip.GetObjID())
	pEngageWarpSeq.AddAction(pFlashAction1, None, fTimeToFlash)

	# Hide the ship.
	pHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShip.GetObjID(), 1)
	pEngageWarpSeq.AddAction(pHideShip, pFlashAction1)

	pUnBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShip.GetObjID(), 0, 1.0)
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
		pExitWarpSeq.AddAction(pFlashAction2, pHideShip, 0.1)

		# Un-Hide the ship
		pUnHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShip.GetObjID(), 0)
		pExitWarpSeq.AddAction(pUnHideShip, pFlashAction2, 0.1)

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
		pBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShip.GetObjID(), 1, 1.0)
		pExitWarpSeq.AddAction(pBoostAction, pUnHideShip, 0.01)

		# TO-DO Replace with a spore-drive flash and sound
		# Play the vushhhhh of exiting warp
		pWarpSoundAction2 = App.TGScriptAction_Create(sCustomActionsScript, "PlayWarpSound", pWS, "Exit Warp", sRace)
		pExitWarpSeq.AddAction(pWarpSoundAction2, pBoostAction)
	
		# Make the ship return to normal speed.
		pUnBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShip.GetObjID(), 0, 1.0)
		pExitWarpSeq.AddAction(pUnBoostAction, pWarpSoundAction2, 0.01)

		# And finally finish the exit sequence
		# actually, just put up a empty action, the Traveler system automatically puts his exit sequence action at the
		# end of the sequence, and his exit action is necessary. However I want it to trigger at the right time, and doing
		# this, i'll achieve that.
		pExitWarpSeqEND = App.TGScriptAction_Create(sCustomActionsScript, "NoAction")
		pExitWarpSeq.AddAction(pExitWarpSeqEND, pUnBoostAction, 0.01)

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

	pEvent = App.TGEvent_Create()
	sOriAdress = pEvent.this
	sOriAdress = sOriAdress[0:len(sOriAdress)-7]
	sAdress = sOriAdress+"WarpEvent"
	pSWNEvent = App.WarpEvent(sAdress)
	pSWNEvent.SetEventType(ENGAGING_ALTERNATEFTLSUBMODEL)
	pSWNEvent.SetDestination(self.Ship)

	# You need to perform these for each event you want, else you get ctd (crash-to-desktop)
	pEvent2e = App.TGEvent_Create()
	sOriAdress2e = pEvent2e.this
	sOriAdress2e = sOriAdress2e[0:len(sOriAdress2e)-7]
	sAdress2e = sOriAdress2e+"WarpEvent"

	pSWNEvent2 = App.WarpEvent(sAdress2e)
	pSWNEvent2.SetEventType(App.ET_START_WARP_NOTIFY)
	pSWNEvent2.SetDestination(self.Ship)

	return [ pSWNEvent, pSWNEvent2 ]

########
# Method to return "exiting travel" events, much like those EXITED_SET or EXITED_WARP events.
# must return a list with the events, possibly none (empty list)
########
def GetExitedTravelEvents(self):
	debug(__name__ + ", GetExitedTravelEvents")
	pEvent = App.TGStringEvent_Create()
	pEvent.SetEventType(App.ET_EXITED_SET)
	pEvent.SetDestination(self.Ship)
	pEvent.SetString("warp")

	pEvent2 = App.TGStringEvent_Create()
	pEvent2.SetEventType(DISENGAGING_ALTERNATEFTLSUBMODEL)
	pEvent2.SetDestination(self.Ship)
	pEvent2.SetString("warp")

	return [ pEvent, pEvent2 ]

########
# Method to return the travel set to use.
# must return a App.SetClass instance, it can't be None.
# NOTE: for the moment, this is probably the best way to make if ships can, or can not, be chased while warping.
########
def GetTravelSetToUse(self):
	debug(__name__ + ", GetTravelSetToUse")
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
	debug(__name__ + ", ConvertSpeedAmount")
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
	return speed*420480*420480

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
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# GC is ALL Rights Reserved by USS Frontier, but since GC supports Plugins it is fair to release a new TravellingMethod or patch old ones as long as the files remain unmodified.
# BSG1978UltraLightDrive.py
# prototype custom travelling method plugin script, by USS Frontier (Enhanced Warp, original) and then modified by Alex SL Gato for BSG 1978 Ultra-Light Drive.
# 22nd September 2025
#################################################################################################################
##########	MANUAL
#################################################################################################################
# NOTE: all functions/methods and attributes defined here (in this prototype example plugin, BSG1978UltraLightDrive) are required to be in the plugin, with the exclusion of:
# ------ MODINFO, which is there just to verify versioning.
# ------ import Camera
# ------ "subTechName", just to make our life easier
# ------ ALTERNATESUBMODELFTL METHODS subsection, which are exclusively used for alternate SubModels for FTL which is a separate but linked mod, or to import needed modules.
# ------ Auxiliar functions: "AuxProtoElementNames", "CreateElectricExplosion", "EezoEnterExitFlash", "EezoField", "findShipInstance", "LoadGFX", "PlayBSG1978UltraLightDriveSound", "BSG1978UltraLightDriveBasicConfigInfo", "BSG1978UltraLightDriveDisabledCalculations" and "WatchPlayerShipLeave". 
# === How-To-Add ===
# This Travelling Method is Ship-based, on this case it needs of Foundation and FoundationTech to verify if the ship is equipped with it.
# This FTL method check is stored inside an "Alternate-Warp-FTL" dictionary, which is a script that should be located at scripts/Custom/Techs/AlternateSubModelFTL.py. While this sub-tech can work totally fine without such module installed, it is recommended to have it.
# On this case, due to that, only the lines marked with "# (#)" are needed for BSG 1978 Ultra-Light-Drive to work, but the final parent technology may require more:
# "BSG 1978 Ultra-Light-Drive": is the name of the key. This is the bare minimum for the technology to work
# "WNacelles": is the name of a key whose value indicates a list of which warp engine property children (nacelles) are part of the BSG 1978 Ultra-Light-Drive system. If all are disabled/destroyed, BSG 1978 Ultra-Light-Drive will not engage. If this field does not exist or "WNacelles": [] it skips this disabled check.
# "Nacelles": is the name of a key whose value indicates a list of which hardpoint properties (nacelles) are part of the BSG 1978 Ultra-Light-Drive system. If all are disabled/destroyed, BSG 1978 Ultra-Light-Drive will not engage. If this field does not exist or "Nacelles": [] it skips this disabled check. Only use this field if your hardpoint does not allow you to have a primary warp control subsystem, else use WNacelles as it is more efficient.
# "Core": is the name of a key whose value indicates a list of which hardpoint properties (not nacelles) are part of the BSG 1978 Ultra-Light-Drive system. If all are disabled/destroyed, BSG 1978 Ultra-Light-Drive will not engage either. If this field does not exist or "Core": [] this check will be skipped.
# "Enter FTL Density": is the name of a key whose value indicates how many Eezo "sparks" happen when entering FTL. Default is 50. Eezo sparks adopt the tint of the Race's PlasmaFX color.
# "Mid FTL Density": is the name of a key whose value indicates how many Eezo "sparks" happen when mid FTL. Default is 50. At the moment this Mid value does nothing because during-FTL sequences seem to crash the game.
# "Exit FTL Density": is the name of a key whose value indicates how many Eezo "sparks" happen when exiting FTL. Default is 50.
# "Spark Size": A value per 1 which stats how big are the sparks. Default is 0.05 (5% ship's radius).
"""
#Sample Setup: replace "USSProtostar" for the appropiate abbrev. Also remove "# (#)"
Foundation.ShipDef.USSProtostar.dTechs = { # (#)
	"Alternate-Warp-FTL": { # (#)
		"Setup": { # (#)
			"BSG 1978 Ultra-Light-Drive": {	"WNacelles": [], "Nacelles": ["Gravitic Initiator"], "Core": ["Tylium Energizer"], "Enter FTL Density": 50, "Mid FTL Density": 50, "Exit FTL Density": 50, "Spark Size": 0.05,}, # (#)
			"Body": "VasKholhr_Body",
			"NormalModel":          shipFile,
			"WarpModel":          "VasKholhr_WingUp",
			"BSG 1978 Ultra-Light-DriveModel":          "VasKholhr_WingUp",
			"AttackModel":          "VasKholhr_WingDown",
			"BodySetScale": 1.0,
			"NormalSetScale": 1.0,
			"WarpSetScale": 1.0,
			"BSG 1978 Ultra-Light-DriveSetScale": 1.0,
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
			"BSG 1978 Ultra-Light-DriveHardpoints":       {
				"Proto Warp Nacelle":  [0.000000, -1.000000, -2.075000],
			},
		}, # (#)

		"Port Wing":     ["VasKholhr_Portwing", {
			"SetScale": 1.0,
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0], # normal Rotation used if not Red Alert and if not Warp
			"AttackRotation":         [0, -0.6, 0],
			"AttackDuration":         200.0, # Value is 1/100 of a second
			"AttackPosition":         [0, 0, 0.03],
			"WarpRotation":       [0, 0.349, 0],
			"WarpPosition":       [0, 0, 0.02],
			"WarpDuration":       150.0,
			"BSG 1978 Ultra-Light-DriveRotation":       [0, 0.749, 0],
			"BSG 1978 Ultra-Light-DrivePosition":       [0, 0, 0.05],
			"BSG 1978 Ultra-Light-DriveDuration":       150.0,
			},
		],
        
		"Starboard Wing":     ["VasKholhr_Starboardwing", {
			"SetScale": 1.0,
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0],
			"AttackRotation":         [0, 0.6, 0],
			"AttackDuration":         200.0, # Value is 1/100 of a second
			"AttackPosition":         [0, 0, 0.03],
			"WarpRotation":       [0, -0.349, 0],
			"WarpPosition":       [0, 0, 0.02],
			"WarpDuration":       150.0,
			"BSG 1978 Ultra-Light-DriveRotation":       [0, -0.749, 0],
			"BSG 1978 Ultra-Light-DrivePosition":       [0, 0, 0.05],
			"BSG 1978 Ultra-Light-DriveDuration":       150.0,
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
	    "Version": "0.33",
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
sName = "Colonial Ultra-Light-Drive"

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
sGoingTo = "Ultra-Light-Driving to"

########
# Phrase to show when the ship drops out of travel (while travelling)
########
sDropOut = "Dropped out of superluminic speeds..."

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


ENGAGING_ALTERNATEFTLSUBMODEL = App.UtopiaModule_GetNextEventType() # For when we are immediately about to fly with this FTL method
DISENGAGING_ALTERNATEFTLSUBMODEL = App.UtopiaModule_GetNextEventType() # For when we are immediately about to stop flying with this FTL method
# Due to AlternateSubModelFTL implementation, only 1 function can cover 1 event, no multiple functions can cover the same event directly. While on regular implementation of these SubModel FTL method that limits nothing, if you want multiple functions to respond, you must create a parent function of sorts that calls all the other functions you want, or create some sort of alternate listener inside some function.

# Because we could end on an endless loop, the imports must be done inside the functions, else the game will not recognize any attribute or function beyond that
# Reason I'm doing this function pass beyond just passing input parameters to the common function is to allow other TravellingMethod modders more flexibility
# from Custom.Techs.AlternateSubModelFTL import StartingProtoWarp, ExitSetProto

subTechFTLName = "BSG 1978 Ultra-Light-Drive"
def KindOfMove(): 
	return subTechFTLName # Modify this with the name you are gonna use for the AlternateSubModelFTL

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
	pInstance = findShipInstance(pShip)
	if not pInstance:
		return 0

	pInstanceDict = pInstance.__dict__
	if pInstanceDict.has_key("Alternate-Warp-FTL") and pInstanceDict["Alternate-Warp-FTL"].has_key("Setup") and pInstanceDict["Alternate-Warp-FTL"]["Setup"].has_key(subTechFTLName): # You need to add a foundation technology to this vessel "AlternateSubModelFTL"
		return 1
	else:
		return 0
	return 0


########
# "CanTravel" Method to check if the ship can travel.
# Must return 1 if it can, otherwise return a string(reason why the ship couldn't travel)
########
# This is just an auxiliar function I made for this
def AuxProtoElementNames(*args):
	# Returns hardpoint property name fragments that indicate are part of the BSG 1978 Ultra-Light-Drive system, and blacklists
	return ["ultra-light-drive engine"], ["not an ultra-light-drive engine", "not a ultra-light-drive engine", " not ultra-light-drive engine"]

# This is just another auxiliar function I made for this
def BSG1978UltraLightDriveBasicConfigInfo(pShip):
	pInstance = findShipInstance(pShip) # On this case, IsShipEquipped(pShip) already checked this for us - HOWEVER do not forget to check if you modify the script
	pInstancedict = None
	specificNacelleHPList = None
	specificNacelleWHPList = [] 
	specificCoreHPList = None
	enterDensity = 200
	midDensity = 200
	exitDensity = 200
	sparkSize = 0.05
	if pInstance:
		pInstancedict = pInstance.__dict__ 
		if pInstancedict.has_key("Alternate-Warp-FTL") and pInstancedict["Alternate-Warp-FTL"].has_key("Setup") and pInstancedict["Alternate-Warp-FTL"]["Setup"].has_key(subTechFTLName):
			if pInstancedict["Alternate-Warp-FTL"]["Setup"][subTechFTLName].has_key("Nacelles"): # Use: if the tech has this field, use it. Must be a list. "[]" would mean that this field is skipped during checks.
				specificNacelleHPList = pInstancedict["Alternate-Warp-FTL"]["Setup"][subTechFTLName]["Nacelles"]
			if pInstancedict["Alternate-Warp-FTL"]["Setup"][subTechFTLName].has_key("WNacelles"): # Use: if the tech has this field, use it. Must be a list. "[]" would mean that this field is skipped during checks.
				specificNacelleWHPList = pInstancedict["Alternate-Warp-FTL"]["Setup"][subTechFTLName]["WNacelles"]
			if pInstancedict["Alternate-Warp-FTL"]["Setup"][subTechFTLName].has_key("Core"): # Use: if the tech has this field, use it. Must be a list. "[]" would mean that this field is skipped during checks.
				specificCoreHPList = pInstancedict["Alternate-Warp-FTL"]["Setup"][subTechFTLName]["Core"]
			if pInstancedict["Alternate-Warp-FTL"]["Setup"][subTechFTLName].has_key("Enter FTL Density"):
				enterDensity = pInstancedict["Alternate-Warp-FTL"]["Setup"][subTechFTLName]["Enter FTL Density"]
			if pInstancedict["Alternate-Warp-FTL"]["Setup"][subTechFTLName].has_key("Mid FTL Density"):
				midDensity = pInstancedict["Alternate-Warp-FTL"]["Setup"][subTechFTLName]["Mid FTL Density"]
			if pInstancedict["Alternate-Warp-FTL"]["Setup"][subTechFTLName].has_key("Exit FTL Density"):
				exitDensity = pInstancedict["Alternate-Warp-FTL"]["Setup"][subTechFTLName]["Exit FTL Density"]
			if pInstancedict["Alternate-Warp-FTL"]["Setup"][subTechFTLName].has_key("Spark Size"):
				sparkSize = pInstancedict["Alternate-Warp-FTL"]["Setup"][subTechFTLName]["Spark Size"]

	hardpointProtoNames, hardpointProtoBlacklist = AuxProtoElementNames()

	return pInstance, pInstancedict, specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, enterDensity, midDensity, exitDensity, sparkSize, specificNacelleWHPList

# This is just another auxiliar function I made for this
def BSG1978UltraLightDriveDisabledCalculations(type, specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, pSubsystem, pShip, justFindOne=0):
	totalBSG1978UltraLightDriveEngines = 0
	onlineBSG1978UltraLightDriveEngines = 0
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
						totalBSG1978UltraLightDriveEngines = totalBSG1978UltraLightDriveEngines + 1
						if pChild.GetCondition() > 0.0 and not pChild.IsDisabled():
							onlineBSG1978UltraLightDriveEngines = onlineBSG1978UltraLightDriveEngines + 1
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
						found = (pSubsystemName in specificCoreHPList)

						if found:
							totalBSG1978UltraLightDriveEngines = totalBSG1978UltraLightDriveEngines + 1
							if pSubsystema.GetCondition() > 0.0 and not pSubsystema.IsDisabled():
								onlineBSG1978UltraLightDriveEngines = onlineBSG1978UltraLightDriveEngines + 1
								if justFindOne == 1:
									break

		pShipList.TGDoneIterating()
		pShipList.TGDestroy()

	return totalBSG1978UltraLightDriveEngines, onlineBSG1978UltraLightDriveEngines

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
		return "This ship is not equipped with BSG 1978 Ultra-Light-Drive"

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

	try:
		pInstance, pInstancedict, specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, _, _, _, _, specificNacelleWHPList = BSG1978UltraLightDriveBasicConfigInfo(pShip)

		pWarpEngines = pShip.GetWarpEngineSubsystem()
		if (specificNacelleWHPList != None and len(specificNacelleWHPList) > 0):
			totalBSG1978UltraLightDriveEngines, onlineBSG1978UltraLightDriveEngines = BSG1978UltraLightDriveDisabledCalculations("Nacelle", specificNacelleWHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, pWarpEngines, pShip, 1)

			if totalBSG1978UltraLightDriveEngines <= 0 or onlineBSG1978UltraLightDriveEngines <= 0:
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

				return "BSG 1978 Ultra-Light-Drive Engines disabled"

		if (specificNacelleHPList != None and len(specificNacelleHPList) > 0):
			totalBSG1978UltraLightDriveCores, onlineBSG1978UltraLightDriveCores = BSG1978UltraLightDriveDisabledCalculations("Core", specificNacelleHPList, specificNacelleHPList, hardpointProtoNames, hardpointProtoBlacklist, pWarpEngines, pShip, 1)

			if totalBSG1978UltraLightDriveCores <= 0 or onlineBSG1978UltraLightDriveCores <= 0:
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
							pSequence.Play()
							App.g_kLocalizationManager.Unload (pDatabase)

				return "BSG 1978 Ultra-Light-Drive Engines disabled"
	
		if specificCoreHPList != None and len(specificCoreHPList) > 0:
			totalBSG1978UltraLightDriveCores, onlineBSG1978UltraLightDriveCores = BSG1978UltraLightDriveDisabledCalculations("Core", specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, pWarpEngines, pShip)

			if totalBSG1978UltraLightDriveCores <= 0 or onlineBSG1978UltraLightDriveCores <= 0:
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
							pSequence.Play()
							App.g_kLocalizationManager.Unload (pDatabase)
				return "All Mass Effect cores are disabled"

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
	except:
		traceback.print_exc()
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
	if bStatus > 0:
		isEquipped = IsShipEquipped(pShip)
		if not isEquipped:
			if bIsPlayer == 1:
				pSequence = App.TGSequence_Create ()
				pSubtitleAction = App.SubtitleAction_CreateC("Brex: We don't have BSG 1978 Ultra-Light-Drive sir, we are dropping out of it.")
				pSubtitleAction.SetDuration(3.0)
				pSequence.AddAction(pSubtitleAction)
				pSequence.Play()
			bStatus = 0
		else:
			pInstance, pInstancedict, specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, _, _, _, _, specificNacelleWHPList = BSG1978UltraLightDriveBasicConfigInfo(pShip)
			if pInstance and pInstancedict:
				if (specificNacelleWHPList != None and len(specificNacelleWHPList) > 0):
					totalBSG1978UltraLightDriveEngines, onlineBSG1978UltraLightDriveEngines = BSG1978UltraLightDriveDisabledCalculations("Nacelle", specificNacelleWHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, pWarpEngines, pShip, 1)

					if totalBSG1978UltraLightDriveEngines <= 0 or onlineBSG1978UltraLightDriveEngines <= 0:
						if bIsPlayer == 1:
							pSequence = App.TGSequence_Create ()
							pSubtitleAction = App.SubtitleAction_CreateC("Brex: All Ultra-Light-Drive engines are offline or disabled sir, we are dropping out of superluminic speeds.")
							pSubtitleAction.SetDuration(3.0)
							pSequence.AddAction(pSubtitleAction)
							pSequence.Play()
						bStatus = 0

				if bStatus > 0 and (specificNacelleHPList != None and len(specificNacelleHPList) > 0):
					totalBSG1978UltraLightDriveCores, onlineBSG1978UltraLightDriveCores = BSG1978UltraLightDriveDisabledCalculations("Core", specificNacelleHPList, specificNacelleHPList, hardpointProtoNames, hardpointProtoBlacklist, pWarpEngines, pShip, 1)

					if totalBSG1978UltraLightDriveCores <= 0 or onlineBSG1978UltraLightDriveCores <= 0:
						if bIsPlayer == 1:
							pSequence = App.TGSequence_Create ()
							pSubtitleAction = App.SubtitleAction_CreateC("Brex: All Ultra-Light-Drive engines are offline or disabled sir, we are dropping out of superluminic speeds.")
							pSubtitleAction.SetDuration(3.0)
							pSequence.AddAction(pSubtitleAction)
							pSequence.Play()
						bStatus = 0

				if bStatus > 0 and specificCoreHPList != None and len(specificCoreHPList) > 0:
					totalBSG1978UltraLightDriveCores, onlineBSG1978UltraLightDriveCores = BSG1978UltraLightDriveDisabledCalculations("Core", specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, pWarpEngines, pShip)

					if totalBSG1978UltraLightDriveCores <= 0 or onlineBSG1978UltraLightDriveCores <= 0:
						if bIsPlayer == 1:
							pSequence = App.TGSequence_Create ()
							pSubtitleAction = App.SubtitleAction_CreateC("Brex: All Ultra-Light-Drive cores are offline or disabled sir, we are dropping out of superluminic speeds.")
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
def PlayBSG1978UltraLightDriveSound(pAction, pWS, sType, sRace):
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

			sFile = None

			if sType == "Enter Warp":
				sFile = "scripts/Custom/TravellingMethods/SFX/enterBSG1978FTL.wav"
			elif sType == "Entering Warp":
				sFile = "scripts/Custom/TravellingMethods/SFX/vooshBSG1978FTL.wav"
			else:
				sFile = "scripts/Custom/TravellingMethods/SFX/exitBSG1978FTL.wav"

			if sFile != None:
				pEnterSound = App.TGSound_Create(sFile, sType, 0)
				pEnterSound.SetSFX(0) 
				pEnterSound.SetInterface(1)

				App.g_kSoundManager.PlaySound(sType)
				#Custom.GravityFX.GravityFXlib.PlaySound(sFile, sRace+" "+sType+" B5 Sound")
		except:
			try:
				if sType == "Enter Warp":
					sFile = "scripts/Custom/TravellingMethods/SFX/enterBSG1978FTL.wav"
				else:
					sFile = "scripts/Custom/TravellingMethods/SFX/exitBSG1978FTL.wav"

				if sFile != None:
					Custom.GravityFX.GravityFXlib.PlaySound(sFile, sRace+" "+sType+" B5 Sound")
			except:
				print "BSG1978UltraLightDrive TravellingMethod: error while calling PlaynBSGDimensionalJumpSoundC:"
				traceback.print_exc()
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

                        if (fX == 1.0):
                            fX = 0.0
                            fY = fY + (1.0 / iNumYFrames)

# Aux. function grabebd from VonFrank's Remastered Effects.py
def CreateElectricExplosion(fSize, fLife, pEmitFrom, bOwnsEmitFrom, pEffectRoot, colorKey, colorKey2, fFrequency = 1.0, fEL = 1.0):
	
	pExplosion = App.AnimTSParticleController_Create()

	pExplosion.AddColorKey(0.1, colorKey[0]/ 255.0, colorKey[1]/ 255.0, colorKey[2]/ 255.0)
	pExplosion.AddColorKey(0.5, colorKey2[0]/ 255.0, colorKey2[1]/ 255.0, colorKey2[2]/ 255.0)
	pExplosion.AddColorKey(1.0, colorKey2[0]/ 255.0, colorKey2[1]/ 255.0, colorKey2[2]/ 255.0)

	pExplosion.AddAlphaKey(0.0, 1.0)
	pExplosion.AddAlphaKey(0.8, 0.8)
	pExplosion.AddAlphaKey(1.0, 0.1)

	pExplosion.AddSizeKey(0.0, 1.0 * fSize)
	pExplosion.AddSizeKey(0.2, 1.0 * fSize)
	pExplosion.AddSizeKey(0.6, 1.0 * fSize)
	pExplosion.AddSizeKey(0.9, 1.0 * fSize)

	
	pExplosion.SetEmitLife(fEL)
	pExplosion.SetEmitFrequency(fFrequency)
	pExplosion.SetEffectLifeTime(fLife + 2.0)
	pExplosion.CreateTarget('data/Textures/Effects/EezoElectricExplosion.tga')
	pExplosion.SetTargetAlphaBlendModes(0, 7)

	pExplosion.AttachEffect(pEffectRoot)

	pExplosion.SetEmitFromObject(pEmitFrom)
	pExplosion.SetDetachEmitObject(bOwnsEmitFrom)

	return pExplosion

# An aux function
def EezoField(pAction, pWS, sType, sRace, amount=50, sparkSize=0.05, type="Enter Warp"):
	pShip = pWS.GetShip()
	if pShip == None:
		return 0

	colorKey = [255.0, 255.0, 255.0]
	colorKey2 = [255.0, 255.0, 255.0]
	try:
		import Custom.NanoFXv2.NanoFX_Lib
		colorKey = Custom.NanoFXv2.NanoFX_Lib.GetOverrideColor(pShip, sType)
		if colorKey == None:
			colorKey = [255.0, 255.0, 255.0]
	except:
		colorKey = [255.0, 255.0, 255.0]

	if type == "Enter Warp":
		colorKey2[1] = colorKey2[1] * 0.5
		colorKey2[2] = colorKey2[2] * 0.1
	elif type == "Exit Warp":
		colorKey[0] = colorKey[0] * 0.1
		colorKey[1] = colorKey[1] * 0.5

	iCycleCount = 1
	if amount > 0 and sparkSize > 0:
		pElectricShockSequence = None
		pShipNode = pShip.GetNode()
		pSet =	pShip.GetContainingSet()
		pSetERoot = None
		if pSet != None:
			pSetERoot = pSet.GetEffectRoot() 
		rShip = pShip.GetRadius()

		LoadGFX(8, 1, 'data/Textures/Effects/EezoElectricExplosion.tga')
		try:
			while (iCycleCount <= amount):
				pEmitPos = pShip.GetRandomPointOnModel()
				pExplosion = CreateElectricExplosion(rShip * sparkSize, 1.0, pEmitPos, 0, pShipNode, colorKey, colorKey2, fFrequency = 1.0, fEL = 1.0)
				pAExplosion = None
				if pExplosion != None:
					pAExplosion = App.EffectAction_Create(pExplosion)
				if pAExplosion != None:
					if pElectricShockSequence == None:
						pElectricShockSequence = App.TGSequence_Create()
					pElectricShockSequence.AddAction(pAExplosion, App.TGAction_CreateNull(), iCycleCount * 0.005)

				if pSetERoot != None:
					pEmitPos2 = pShip.GetRandomPointOnModel()
					pExplosion2 = CreateElectricExplosion(rShip * sparkSize, 1.0, pEmitPos2, 0, pSetERoot, colorKey, colorKey2, fFrequency = 1.0, fEL = 3.0)
					pAExplosion2 = None
					if pExplosion2 != None:
						pAExplosion2 = App.EffectAction_Create(pExplosion)
					if pAExplosion2 != None:
						pElectricShockSequence.AddAction(pAExplosion2, App.TGAction_CreateNull(), iCycleCount * 0.005)

				iCycleCount = iCycleCount + 1
		except:
			traceback.print_exc()
		if pElectricShockSequence != None:
			pElectricShockSequence.Play()

	return 0

# Create flash effect on a ship
def EezoEnterExitFlash(pAction, pWS):
	pShip = pWS.GetShip()
	if pShip == None:
		return 0

	sFile = 'scripts/Custom/TravellingMethods/GFX/HyperdriveFlashPurple.tga'
	fEffect = None
	try:
		LoadGFX(4, 4, 'scripts/Custom/TravellingMethods/GFX/HyperdriveFlashPurple.tga') # I am unsure as to how this file was here - that is, I heavily suspect it is from a Stargate pack, but the one I have does not have methods that alter the TravellingMethods...

		pAttachTo = pShip.GetContainingSet().GetEffectRoot() #pShip.GetNode()
		fSize = pShip.GetRadius() * 5
		pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())

		fLifeTime = 1
		fRed = 255.0
		fGreen = 255.0
		fBlue = 255.0
		fBrightness = 0.8
		fSpeed = 0.5
       
		pEffect = App.AnimTSParticleController_Create()
		pEffect.AddColorKey(0.0, fRed / 255, fGreen / 255, fBlue / 255)
		pEffect.AddColorKey(1.0, fRed / 255, fGreen / 255, fBlue / 255)
		pEffect.AddAlphaKey(0.0, 1.0)
		pEffect.AddAlphaKey(1.0, 1.0)
		pEffect.AddSizeKey(0.0, fSize)
		pEffect.AddSizeKey(1.0, fSize)

		pEffect.SetEmitLife(0.5)
		pEffect.SetEmitFrequency(1)
		pEffect.SetEffectLifeTime(fSpeed + fLifeTime)
		pEffect.SetInheritsVelocity(0)
		pEffect.SetDetachEmitObject(0) # If set to 1 it makes the main ship invisible LOL
		pEffect.CreateTarget(sFile)
		pEffect.SetTargetAlphaBlendModes(0, 7)

		pEffect.SetEmitFromObject(pEmitFrom)
		pEffect.AttachEffect(pAttachTo)                
		fEffect = App.EffectAction_Create(pEffect)

	except:
		print "BSG1978UltraLightDrive TravellingMethod: error while calling EezoEnterExitFlash:"
		traceback.print_exc()
		fEffect = None

	if fEffect != None:
		pSequence = App.TGSequence_Create()
		pSequence.AddAction(fEffect)
		pSequence.Play ()
                
	return 0

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

	_, _, _, _, _, _, eDensity, mDensity, exDensity, sparkSize, _ = BSG1978UltraLightDriveBasicConfigInfo(pShip)

	pEngageWarpSeq = App.TGSequence_Create()

	## disable during warp seq because for now WARP gfx effect doesn't have the need of any during warp seq fx
	## and then, if it is None, the Travel won't try to use it
	#if pWS.DuringWarpSeq == None:
	#	pWS.DuringWarpSeq = App.TGSequence_Create()
	# Extra added for Mass Effect
	#pDuringWarpSeq = App.TGSequence_Create()
	pDuringWarpSeq = None
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

		pDisallowInput = App.TGScriptAction_Create("MissionLib", "RemoveControl")
		pEngageWarpSeq.AddAction(pDisallowInput, pCinematicStart)

		# AN EXTRA I HAD TO ADD BECAUSE REALLY WHY WAS THIS NOT ADDED?
		# Maybe for other FTL methods it could be unecessary but for warp having the camera constantly swapping and then having the warp flash at 2 cm from your face is not good!
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
		# END OF THE EXTRA

	pWarpSoundAction1 = App.TGScriptAction_Create(__name__, "PlayBSG1978UltraLightDriveSound", pWS, "Enter Warp", sRace)
	pEngageWarpSeq.AddAction(pWarpSoundAction1, None, fEntryDelayTime + 0.2)

	# Extra added for Ultra-Light-Drive
	pWarpEezoEffectAction1 = App.TGScriptAction_Create(__name__, "EezoField", pWS, "PlasmaFX", sRace, eDensity, sparkSize, "Enter Warp")
	pEngageWarpSeq.AddAction(pWarpEezoEffectAction1, None, fEntryDelayTime * 0.5)

	pBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShip.GetObjID(), 1, 10000.0)
	pEngageWarpSeq.AddAction(pBoostAction, pWarpSoundAction1, 0.7)

	pWarpSoundAction1v = App.TGScriptAction_Create(__name__, "PlayBSG1978UltraLightDriveSound", pWS, "Entering Warp", sRace)
	pEngageWarpSeq.AddAction(pWarpSoundAction1v, pBoostAction)

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

	# Create the warp flash.
	#pFlashAction1 = App.TGScriptAction_Create("Actions.EffectScriptActions", "WarpFlash", pShip.GetObjID())
	#pFlashAction1 = App.TGScriptAction_Create(__name__, "EezoEnterExitFlash", pWS)
	#pEngageWarpSeq.AddAction(pFlashAction1, None, fTimeToFlash)

	# Hide the ship... wait, we don't need to for this method!
	#pHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShip.GetObjID(), 1)
	#pEngageWarpSeq.AddAction(pHideShip, pBoostAction, fTimeToFlash)

	pUnBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShip.GetObjID(), 0, 1.0)
	pEngageWarpSeq.AddAction(pUnBoostAction, pBoostAction, fTimeToFlash)
	
	pCheckTowing = App.TGScriptAction_Create(sCustomActionsScript, "EngageSeqTractorCheck", pWS)
	pEngageWarpSeq.AddAction(pCheckTowing, pUnBoostAction)	

	pEnWarpSeqEND = App.TGScriptAction_Create(sCustomActionsScript, "NoAction")
	pEngageWarpSeq.AddAction(pEnWarpSeqEND, pUnBoostAction, 0.5)

	############### mid sequence begins ########
	# Extra added for Ultra-Light-Drive
	#pWarpEezoEffectAction2 = App.TGScriptAction_Create(__name__, "EezoField", pWS, "PlasmaFX", sRace, mDensity, sparkSize)
	#pDuringWarpSeq.AddAction(pWarpEezoEffectAction2, None, 1.0)
	#pMidWarpSeqEND = App.TGScriptAction_Create(sCustomActionsScript, "NoAction")
	#pDuringWarpSeq.AddAction(pMidWarpSeqEND, pWarpEezoEffectAction2, 1.0)
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
	
		# Hide the ship... wait we don't need to for this one
		#pHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShip.GetObjID(), 1)
		#pExitWarpSeq.AddAction(pHideShip, None)

		# Check for towee
		if pWS.Travel.bTractorStat == 1:
			pHideTowee = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pWS.Travel.Towee.GetObjID(), 1)
			pExitWarpSeq.AddAction(pHideTowee, pHideShip)

		# Create the warp flash.
		#pFlashAction2 = App.TGScriptAction_Create("Actions.EffectScriptActions", "WarpFlash", pShip.GetObjID())
		#pFlashAction2 = App.TGScriptAction_Create(__name__, "EezoEnterExitFlash", pWS)
		#pExitWarpSeq.AddAction(pFlashAction2, pHideShip, 0.7)
		#pExitWarpSeq.AddAction(pFlashAction2, pHideShip, 0)

		# Un-Hide the ship
		pUnHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShip.GetObjID(), 0)
		pExitWarpSeq.AddAction(pUnHideShip, None)

		# Extra added for Ultra-Light-Drive
		pWarpEezoEffectAction3 = App.TGScriptAction_Create(__name__, "EezoField", pWS, "PlasmaFX", sRace, exDensity, sparkSize, "Exit Warp")
		pExitWarpSeq.AddAction(pWarpEezoEffectAction3, pUnHideShip)

		# Un-hide the Towee, plus if it exists, also set up the maintain chain
		## REMEMBER: any changes in the time of this sequence will also require a re-check of this part, to make sure
		##           we're making the right amount of MaintainTowing actions.
		if pWS.Travel.bTractorStat == 1:
			pUnHideTowee = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pWS.Travel.Towee.GetObjID(), 0)
			pExitWarpSeq.AddAction(pUnHideTowee, pUnHideShip)

			fCount = 0.0
			while fCount < (fTimeToFlash * 0.5):
				pMaintainTowingAction = App.TGScriptAction_Create(sCustomActionsScript, "MaintainTowingAction", pWS)
				pExitWarpSeq.AddAction(pMaintainTowingAction, pUnHideTowee, fCount)
				fCount = fCount + 0.01
				if fCount >= (fTimeToFlash * 0.5):
					break

		# Give it a little boost
		pBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShip.GetObjID(), 1, 10000.0)
		pExitWarpSeq.AddAction(pBoostAction, pWarpEezoEffectAction3)

		# Play the vushhhhh of exiting warp
		pWarpSoundAction2 = App.TGScriptAction_Create(__name__, "PlayBSG1978UltraLightDriveSound", pWS, "Exit Warp", sRace)
		pExitWarpSeq.AddAction(pWarpSoundAction2, pBoostAction)
	
		# Make the ship return to normal speed.
		pUnBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShip.GetObjID(), 0, 1.0)
		pExitWarpSeq.AddAction(pUnBoostAction, pUnHideShip, fTimeToFlash * 0.5)

		# And finally finish the exit sequence
		# actually, just put up a empty action, the Traveler system automatically puts his exit sequence action at the
		# end of the sequence, and his exit action is necessary. However I want it to trigger at the right time, and doing
		# this, i'll achieve that.
		pExitWarpSeqEND = App.TGScriptAction_Create(sCustomActionsScript, "NoAction")
		pExitWarpSeq.AddAction(pExitWarpSeqEND, pUnBoostAction, 0.5)

	###########################################################################################
	# end of the not-required stuff that sets up my sequences
	###########################################################################################

	# Now the following part, the return statement is VERY important.
	# it must return a list of 3 values, from beggining to end, they must be:
	# 1º: the engaging travel sequence  (plays once, when the ship enters the travel)
	# 2º: the during travel sequence    (plays repeatedly, while the ship is travelling)
	# 3º: the exiting travel sequence   (plays once, when the ship exits travel)

	# Note that each one of them can be None, if you don't want to have that sequence in your travel method.

	return [pEngageWarpSeq, pDuringWarpSeq, pExitWarpSeq]

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
		fFacA = 2.88 / 6.0              ##### Do Not Change These Values #####
		fFacB = 8.312            ##### Do Not Change These Values #####
	elif fSpeed > 9.99:
		fFacA = 2.88 / 5.0              ##### Do Not Change These Values #####
		fFacB = 7.512            ##### Do Not Change These Values #####
	elif fSpeed > 9.6:
		fFacA = 2.8700 / 4.0             ##### Do Not Change These Values #####
		fFacB = 5.9645             ##### Do Not Change These Values #####
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
	fPower = 1.0
	fRealMaxSpeed = self.GetMaxSpeed()
	if pWarpEngines != None:
		if self.IsPlayer == 1:
			fPower = pWarpEngines.GetPowerPercentageWanted()
		else:
			fPower = self.AIwarpPower
	else:
		if fRealMaxSpeed != 0:
			fPower = self.GetSpeed()/fRealMaxSpeed
		else:
			fPower = 1.0

	fAMWS = (fRealMaxSpeed * fPower) - (fPower - 1.0)
	if fAMWS > 10.0:
		fAMWS = 10.0
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
	fRealCruiseSpeed = self.GetCruiseSpeed()
	if pWarpEngines != None:
		if self.IsPlayer == 1:
			fPower = pWarpEngines.GetPowerPercentageWanted()
		else:
			fPower = self.AIwarpPower
	else:
		if fRealCruiseSpeed != 0:
			fPower = self.GetSpeed()/fRealCruiseSpeed
		else:
			fPower = 1.0

	fACWS = (fRealCruiseSpeed * fPower) - (fPower - 1.0)
	if fACWS > 10.0:
		fACWS = 10.0
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
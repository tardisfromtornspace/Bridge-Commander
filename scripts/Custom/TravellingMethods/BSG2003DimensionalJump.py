# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# GC is ALL Rights Reserved by USS Frontier, but since GC supports Plugins it is fair to release a new TravellingMethod or patch old ones as long as the files remain unmodified.
# BSG2003DimensionalJump.py
# Based on the prototype custom travelling method plugin script, by USS Frontier (Enhanced Warp.py, original, template), and then modified by Alex SL Gato for nBSGDimensionalJump.
# This ship is a legal replacement to the illegal JumpspaceModule - use BSG2003DimensionalJump instead.
# 8th September 2025
#################################################################################################################
##########	MANUAL
#################################################################################################################
#TO-DO UPDATE THIS MANUAL
# TO-DO THE LIGHT JUMPS FROM FRONT TO BACK
# TO-DO MAKE IT SO WHILE ON THE SYSTEM THE JUMP AUTOMATICALLY FAILS SO YOU NEED MULTIPLE JUMPS TO REACH YOUR DESTINATION
# TO-DO MAKE IT SO THE CYLONS REQUIRE 10x JUMPS FOR A THING AND THEN GALACTICA 200x
# TO-DO LOOK A WAY TO MAKE THE JUMP ENGINES WORK EVERY 33 MINUTES - ACTUALLY 15 MINUTES
# TO-DO When popping in and out the vessel the flash should move backwards (enter) forwards (exit) -use gravity?.
# TO-DO Noise from https://www.youtube.com/watch?v=sGCfC4NvQaY minute 1:04
# TO-DO when disappearing all ships nearby may suffer from some damage that passes through shields. The close to the source the worse the damage would be (but not affecting ships that are dead or dying already, to prevent issues).

# NOTE: all functions/methods and attributes defined here (in this prototype example plugin, nBSGDimensionalJump) are required to be in the plugin, with the exclusion of:
# ------ MODINFO, which is there just to verify versioning.
# ------ ALTERNATESUBMODELFTL METHODS subsection, which are exclusively used for alternate SubModels for FTL which is a separate but linked mod, or to import needed modules.
# ------ Auxiliar functions: "AuxProtoElementNames", "nBSGDimensionalJumpFlash", "CreateDetachedElectricExplosion", "findShipInstance", "HasPhasednBSGDimensionalJumpDrive", "HasCloakedJumpSystem", "LoadGFX", "PlaynBSGDimensionalJumpSound", "PlaynBSGDimensionalJumpSoundC", "nBSGDimensionalJumpBasicConfigInfo" and "nBSGDimensionalJumpDisabledCalculations".
# ------ Auxiliar variables: and , used for keeping tabs on our alternate pSets and the sound that plays while on jumpspace.
# ------ Auxiliar class  and its instance 
# ------ Auxiliar functions for intra-system intercept (ISI) support, which as a result of being a common-made function between default GalaxyCharts functions/methods, regular AlternateSubModelFTL and ISI, while not required to be on the plugin, some of their contents are actually required if they are not there: "awayNavPointDistanceCalc", "CanTravelShip", "ConditionalCloak", "ConditionalDecloak", "EngageSeqTractorCheckI", "GetEngageDirectionISI", "GetExitedTravelEventsI", "GetStartTravelEventsI", "GetEngageDirectionC", "InSystemIntercept", "MaintainTowingActionI", "PlaynBSGDimensionalJumpSoundI", "removeTractorISITowInfo", "SetupSequenceISI" and "SetupTowingI".
# Please note that "GetTravelSetToUse" has been modified to allow a different Travel Set.
# === How-To-Add ===
# This Travelling Method is Ship-based, on this case it may need of Foundation and FoundationTech to verify if the ship is equipped with it.
# This main FTL method check is stored inside an "Alternate-Warp-FTL" dictionary, which is a script that should be located at scripts/Custom/Techs/AlternateSubModelFTL.py. While this sub-tech can work totally fine without such module installed, or even just act on hardpoint properties alone (including a ship subsystem that contains "jumpspace drive" or "jump-space drive", case insensitive, and another called "TransDimensional Drive" case-sensitive, on the hardpoint will suffice), it is recommended to have it.
# On this case, due to that, only the lines marked with "# (#)" are needed for nBSGDimensionalJump to work, but the final parent technology may require more:
# "nBSGDimensionalJump": is the name of the key. This is the bare minimum for the technology to work
# "Nacelles": is the name of a key whose value indicates a list of which warp engine property children (nacelles) are part of the nBSGDimensionalJump system. If all are disabled/destroyed, nBSGDimensionalJump will not engage. If this field does not exist or "Nacelles": [] it skips this disabled check.
# "Core": is the name of a key whose value indicates a list of which hardpoint properties (not nacelles) are part of the nBSGDimensionalJump system. If all are disabled/destroyed, nBSGDimensionalJumpDrive will not engage either. If this field does not exist, it wil check for all subsystems with "quantum jumpspace drive" or "quantum jump-space drive", case insensitive. Use "Core": [] to skip this check.
# Subsystems note: when editing the hardpoint, you can also add another hardpoint property called "TransDimensional Drive" to change this FTL effects and behaviour slightly (instead of a vortex-like animation at great speeds, it's a big silent rotund flash with barely any movement). Same with "Hyperspace Cloak" (will not use any flashes and will actually try to make the ship cloak and decloak and will use shadow sounds).
# TO-DO CHANGE THIS --> Also, important note, this mod uses additional systems for GalaxyCharts, "Custom.GalaxyCharts.TravelerSystems.nBSGDimensionalJumpDriveTunnelTravelSet" and "Custom.GalaxyCharts.TravelerSystems.AInBSGDimensionalJumpDriveTunnelTravelSet", with "Custom.GalaxyCharts.TravelerSystems.nBSGDimensionalJumpDriveTunnelTravelSet_S" being optional but highly recommended to have.
# "Cooldown Time": time in seconds between jumps on a type of ship, in seconds. Default is 15 * 60 seconds (I was told 33 minutes was just during the 33 minutes arc and it was more like the times they needed to jump when the Cylons found them).
"""
#Sample Setup: replace "EAOmega" for the appropiate abbrev. Also remove "# (#)"
Foundation.ShipDef.EAOmega.dTechs = { # (#)
	"Alternate-Warp-FTL": { # (#)
		"Setup": { # (#)
			"nBSGDimensionalJump": {	"Nacelles": ["Dimensional Jump Engine"], "Core": ["Tylium Core"], "Cooldown Time": 33 * 60}, # (#)
			"Body": "VasKholhr_Body",
			"NormalModel":          shipFile,
			"WarpModel":          "VasKholhr_WingUp",
			"nBSGDimensionalJumpModel":          "VasKholhr_WingUp",
			"AttackModel":          "VasKholhr_WingDown",
			"BodySetScale": 1.0,
			"NormalSetScale": 1.0,
			"WarpSetScale": 1.0,
			"nBSGDimensionalJumpSetScale": 1.0,
			"AttackSetScale": 1.0,
			"Hardpoints":       {
				"Port Hanger":  [-5.500000, 1.000000, 0.000000, {"Disabled Percentage" : 0.5}],
				"Star Hanger":  [5.500000, 1.000000, 0.000000, {"Disabled Percentage" : 0.5}],
				"Launch Tube P1":  [-6.900000, 2.900000, -0.620000, {"Disabled Percentage" : 0.5}],
				"Launch Tube P2":  [-6.950000, 2.150000, -0.620000, {"Disabled Percentage" : 0.5}],
				"Launch Tube P3":  [-7.000000, 1.020000, -0.620000, {"Disabled Percentage" : 0.5}],
				"Launch Tube P4":  [-7.020000, 0.300000, -0.620000, {"Disabled Percentage" : 0.5}],
				"Launch Tube P5":  [-7.020000, -0.800000, -0.620000, {"Disabled Percentage" : 0.5}],
				"Launch Tube P6":  [-7.020000, -1.550000, -0.620000, {"Disabled Percentage" : 0.5}],
				"Launch Tube P7":  [-7.020000, -2.675000, -0.620000, {"Disabled Percentage" : 0.5}],
				"Launch Tube P8":  [-7.020000, -3.400000, -0.620000, {"Disabled Percentage" : 0.5}],
				"Launch Tube P9":  [-6.930000, -4.500000, -0.620000, {"Disabled Percentage" : 0.5}],
				"Launch Tube P10":  [-6.850000, -5.275000, -0.620000, {"Disabled Percentage" : 0.5}],
				"Launch Tube P1 OEP":  [-6.900000, 2.900000, -0.620000 ],
				"Launch Tube P2 OEP":  [-6.950000, 2.150000, -0.620000 ],
				"Launch Tube P3 OEP":  [-7.000000, 1.020000, -0.620000 ],
				"Launch Tube P4 OEP":  [-7.020000, 0.300000, -0.620000 ],
				"Launch Tube P5 OEP":  [-7.020000, -0.800000, -0.620000 ],
				"Launch Tube P6 OEP":  [-7.020000, -1.550000, -0.620000 ],
				"Launch Tube P7 OEP":  [-7.020000, -2.675000, -0.620000 ],
				"Launch Tube P8 OEP":  [-7.020000, -3.400000, -0.620000 ],
				"Launch Tube P9 OEP":  [-6.930000, -4.500000, -0.620000 ],
				"Launch Tube P10 OEP":  [-6.850000, -5.275000, -0.620000 ],
			},

			"nBSGDimensionalJumpHardpoints":       {
				"Port Hanger":  [-5.500000, 1.000000, 0.000000, {"Disabled Percentage" : 1.5}],
				"Star Hanger":  [5.500000, 1.000000, 0.000000, {"Disabled Percentage" : 1.5}],
				"Launch Tube P1":  [-6.900000, 2.900000, -0.620000, {"Disabled Percentage" : 1.5}],
				"Launch Tube P2":  [-6.950000, 2.150000, -0.620000, {"Disabled Percentage" : 1.5}],
				"Launch Tube P3":  [-7.000000, 1.020000, -0.620000, {"Disabled Percentage" : 1.5}],
				"Launch Tube P4":  [-7.020000, 0.300000, -0.620000, {"Disabled Percentage" : 1.5}],
				"Launch Tube P5":  [-7.020000, -0.800000, -0.620000, {"Disabled Percentage" : 1.5}],
				"Launch Tube P6":  [-7.020000, -1.550000, -0.620000, {"Disabled Percentage" : 1.5}],
				"Launch Tube P7":  [-7.020000, -2.675000, -0.620000, {"Disabled Percentage" : 1.5}],
				"Launch Tube P8":  [-7.020000, -3.400000, -0.620000, {"Disabled Percentage" : 1.5}],
				"Launch Tube P9":  [-6.930000, -4.500000, -0.620000, {"Disabled Percentage" : 1.5}],
				"Launch Tube P10":  [-6.850000, -5.275000, -0.620000, {"Disabled Percentage" : 1.5}],
				"Launch Tube P1 OEP":  [-6.900000, 2.900000, -0.620000 ],
				"Launch Tube P2 OEP":  [-6.950000, 2.150000, -0.620000 ],
				"Launch Tube P3 OEP":  [-7.000000, 1.020000, -0.620000 ],
				"Launch Tube P4 OEP":  [-7.020000, 0.300000, -0.620000 ],
				"Launch Tube P5 OEP":  [-7.020000, -0.800000, -0.620000 ],
				"Launch Tube P6 OEP":  [-7.020000, -1.550000, -0.620000 ],
				"Launch Tube P7 OEP":  [-7.020000, -2.675000, -0.620000 ],
				"Launch Tube P8 OEP":  [-7.020000, -3.400000, -0.620000 ],
				"Launch Tube P9 OEP":  [-6.930000, -4.500000, -0.620000 ],
				"Launch Tube P10 OEP":  [-6.850000, -5.275000, -0.620000 ],
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
			"nBSGDimensionalJumpRotation":       [0, 0.749, 0],
			"nBSGDimensionalJumpPosition":       [0, 0, 0.05],
			"nBSGDimensionalJumpDuration":       150.0,
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
			"nBSGDimensionalJumpRotation":       [0, -0.749, 0],
			"nBSGDimensionalJumpPosition":       [0, 0, 0.05],
			"nBSGDimensionalJumpDuration":       150.0,
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
	    "Version": "0.25",
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
sName = "Kobollian Dimensional Jump"

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
sGoingTo = "10, 9, 8, 7, 6, 5, 4, 3, 2, 1... Jumping towards" # TO-DO ADD 10 SEC JUMP COUNTDOWN

########
# Phrase to show when the ship drops out of travel (while travelling)
########
sDropOut = "00:00:00 Jump executed..."

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
fLaunchRadius = 20.0

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
# from Custom.Techs.AlternateSubModelFTL import StartingProtoWarp, ExitSetProto

def KindOfMove(): 
	return "nBSGDimensionalJump" # Modify this with the name you are gonna use for the AlternateSubModelFTL

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
	return 0.6


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

	pInstance, pInstanceDict, specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, delay = nBSGDimensionalJumpBasicConfigInfo(pShip)
	pInstance = findShipInstance(pShip)
	if pInstance:
		if pInstanceDict.has_key("Alternate-Warp-FTL") and pInstanceDict["Alternate-Warp-FTL"].has_key("Setup") and pInstanceDict["Alternate-Warp-FTL"]["Setup"].has_key("nBSGDimensionalJump"): # You need to add a foundation technology to this vessel "AlternateSubModelFTL"
			return 1
	return 0

# An aux function, checks if this ship can do phased nBSGDimensionalJumpDrive. In order for ships that used another version can still use this, it follows similar functionality.
def HasPhasednBSGDimensionalJumpDrive(pShip, myStr = "Better Jump"):
	found = 0
        pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
	pSystem = pShip.GetNextSubsystemMatch(pIterator)

	# Add the stats of each engine into the list
        while (pSystem != None):
		if hasattr(pSystem, "GetName") and pSystem.GetName() == myStr:
                   pCurrStats = pSystem.GetConditionPercentage()
                   pDisabled = pSystem.GetDisabledPercentage()
                   if pCurrStats > pDisabled:
                       found = 1
                       break                
		pSystem = pShip.GetNextSubsystemMatch(pIterator)

        pShip.EndGetSubsystemMatch(pIterator)
	return found

# An aux function, checks if this ship can do Sigma Walkers Dimensional Drive. In order for ships that used another version can still use this, it follows similar functionality.
def HasCloakedJumpSystem(pShip):
	return HasPhasednBSGDimensionalJumpDrive(pShip, myStr = "Jump Cloak")

########
# "CanTravel" Method to check if the ship can travel.
# Must return 1 if it can, otherwise return a string(reason why the ship couldn't travel)
########
# This is just an auxiliar function I made for this
def AuxProtoElementNames(*args):
	# Returns hardpoint property name fragments that indicate are part of the nBSGDimensionalJump system, and blacklists
	return ["ftl dimensional jump drive", "ftl dimensional drive"], ["not a ftl dimensional jump drive", "not a ftl dimensional drive", " not ftl dimensional jump drive", " not ftl dimensional drive"]

# This is just another auxiliar function I made for this
def nBSGDimensionalJumpBasicConfigInfo(pShip):
	pInstance = findShipInstance(pShip) # On this case, IsShipEquipped(pShip) already checked this for us - HOWEVER do not forget to check if you modify the script
	pInstancedict = None
	specificNacelleHPList = None
	specificCoreHPList = None
	delay = 15 * 60
	if pInstance:
		pInstancedict = pInstance.__dict__ 
		if pInstancedict.has_key("Alternate-Warp-FTL") and pInstancedict["Alternate-Warp-FTL"].has_key("Setup") and pInstancedict["Alternate-Warp-FTL"]["Setup"].has_key("nBSGDimensionalJump"):
			if pInstancedict["Alternate-Warp-FTL"]["Setup"]["nBSGDimensionalJump"].has_key("Nacelles"): # Use: if the tech has this field, use it. Must be a list. "[]" would mean that this field is skipped during checks.
				specificNacelleHPList = pInstancedict["Alternate-Warp-FTL"]["Setup"]["nBSGDimensionalJump"]["Nacelles"]
			if pInstancedict["Alternate-Warp-FTL"]["Setup"]["nBSGDimensionalJump"].has_key("Core"): # Use: if the tech has this field, use it. Must be a list. "[]" would mean that this field is skipped during checks.
				specificCoreHPList = pInstancedict["Alternate-Warp-FTL"]["Setup"]["nBSGDimensionalJump"]["Core"]
			if pInstancedict["Alternate-Warp-FTL"]["Setup"]["nBSGDimensionalJump"].has_key("Cooldown Time"): # Use: if the tech has this field, use it. Must be a number.
				delay = pInstancedict["Alternate-Warp-FTL"]["Setup"]["nBSGDimensionalJump"]["Cooldown Time"]

	hardpointProtoNames, hardpointProtoBlacklist = AuxProtoElementNames()

	return pInstance, pInstancedict, specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, delay

# This is just another auxiliar function I made for this
def nBSGDimensionalJumpDisabledCalculations(type, specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, pSubsystem, pShip, justFindOne=0):
	totalnBSGDimensionalJumpEngines = 0
	onlinenBSGDimensionalJumpEngines = 0
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
							totalnBSGDimensionalJumpEngines = totalnBSGDimensionalJumpEngines + 1
							if pChild.GetCondition() > 0.0 and not pChild.IsDisabled():
								onlinenBSGDimensionalJumpEngines = onlinenBSGDimensionalJumpEngines + 1
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
							totalnBSGDimensionalJumpEngines = totalnBSGDimensionalJumpEngines + 1
							if pSubsystema.GetCondition() > 0.0 and not pSubsystema.IsDisabled():
								onlinenBSGDimensionalJumpEngines = onlinenBSGDimensionalJumpEngines + 1
								if justFindOne == 1:
									break

		pShipList.TGDoneIterating()
		pShipList.TGDestroy()

	return totalnBSGDimensionalJumpEngines, onlinenBSGDimensionalJumpEngines

# Auxiliar function TO-DO ADD TO DOC
def AreWeOnFTLCooldown(pInstance):
	timeRemaining = 0
	if pInstance:
		if hasattr(pInstance, "nBSGJumpCooldown"): # TO-DO ADD THIS AS A SEPARATE FUNCTION?
			coolDown = pInstance.nBSGJumpCooldown
			currentTime = App.g_kUtopiaModule.GetGameTime()
			if coolDown is not None and currentTime is not None and type(coolDown) == type(currentTime) and coolDown > currentTime:
				timeRemaining = coolDown - currentTime
	else:
		timeRemaining = None
	return timeRemaining

# Auxiliar function TO-DO ADD TO DOC
def AreWeOnFTLStretch(pInstance):
	timeRemaining = 0
	if pInstance:
		if pInstance and hasattr(pInstance, "nBSGJumpStretch"): # TO-DO ADD THIS AS A SEPARATE FUNCTION?
			coolDown = pInstance.nBSGJumpStretch
			currentTime = App.g_kUtopiaModule.GetGameTime()
			if coolDown is not None and currentTime is not None and type(coolDown) == type(currentTime) and coolDown > currentTime:
				timeRemaining = coolDown  - currentTime
	else:
		timeRemaining = None
	return timeRemaining

# Auxiliar function TO-DO ADD TO DOC
def InstateFTLCooldown(pInstance, delay): # TO-DO add a method to get the delays also TO-DO cleanup
	if pInstance:
		#if not hasattr(pInstance, "nBSGJumpCooldown"):
		currentTime = App.g_kUtopiaModule.GetGameTime()
		pInstance.nBSGJumpCooldown = currentTime + delay
	else:
		print __name__, "InstateFTLCooldown could not find a pInstance..."

# Auxiliar function TO-DO ADD TO DOC
def InstateFTLStrCooldown(pInstance, delay=0.2, remove=0): # TO-DO add a method to get the delays also TO-DO cleanup
	if pInstance:
		if remove == 1:
			if hasattr(pInstance, "nBSGJumpStretch"):
				pInstance.nBSGJumpStretch = None	
		elif remove == 0 or (not hasattr(pInstance, "nBSGJumpStretch") or pInstance.nBSGJumpStretch == None):
			currentTime = App.g_kUtopiaModule.GetGameTime()
			pInstance.nBSGJumpStretch = currentTime + delay
	else:
		print __name__, "InstateFTLStrCooldown could not find a pInstance..."

# Auxiliar function TO-DO ADD TO DOC
def afterGlowFTLact(pAction, pWS):
	debug(__name__ + ", afterGlowFTLact")

	pShip = pWS.GetShip()
	if pShip != None:
		afterGlowFTLC(pShip)
	return 0

# Auxiliar function TO-DO ADD TO DOC
def afterGlowFTLactISI(pAction, pShipID):
	debug(__name__ + ", afterGlowFTLactI")

	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShipID)
	if pShip != None:
		afterGlowFTLC(pShip)
	return 0

# Auxiliar function TO-DO ADD TO DOC
def afterGlowFTLC(pShip):
	debug(__name__ + ", afterGlowFTL")
	try:
		if pShip != None:
			pInstance, pInstancedict, specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, delay = nBSGDimensionalJumpBasicConfigInfo(pShip)
			if pInstance != None:
				InstateFTLStrCooldown(pInstance, remove=1) # No longer stretching
				#TO-DO UNCOMMENT THIS InstateFTLCooldown(pInstance, delay)
	except:
		traceback.print_exc()

def CanTravel(self): # NOTE: Requires CanTravelShip
	debug(__name__ + ", CanTravel")
	return CanTravelShip(self.GetShip())

# Auxiliar ISI function
def CanTravelShip(pShip):
	debug(__name__ + ", CanTravel")

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
		return "This ship is not equipped with Kobollian FTL Jump Drive"

	pInstance, pInstancedict, specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, delay = nBSGDimensionalJumpBasicConfigInfo(pShip)

	pWarpEngines = pShip.GetWarpEngineSubsystem()
	if (specificNacelleHPList != None and len(specificNacelleHPList) > 0):
		totalnBSGDimensionalJumpEngines, onlinenBSGDimensionalJumpEngines = nBSGDimensionalJumpDisabledCalculations("Nacelle", specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, pWarpEngines, pShip, 1)

		if totalnBSGDimensionalJumpEngines <= 0 or onlinenBSGDimensionalJumpEngines <= 0:
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

			return "Kobollian FTL Drive Engines disabled"

	if specificCoreHPList == None or (specificCoreHPList != None and len(specificCoreHPList) > 0):
		totalnBSGDimensionalJumpCores, onlinenBSGDimensionalJumpCores = nBSGDimensionalJumpDisabledCalculations("Core", specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, pWarpEngines, pShip, 1)

		if totalnBSGDimensionalJumpCores <= 0 or onlinenBSGDimensionalJumpCores <= 0:
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
			return "Kobollian FTL Drive or power are disabled"

	timeRemaining = AreWeOnFTLCooldown(pInstance)
	if timeRemaining == None:
		return "Some kind of error must have happened with pInstances"
	if timeRemaining > 0:
		return "Drive is still spooling for another "+ str(timeRemaining) +" seconds"

	return 1


########
# Method to check if the ship can continue travelling (she's travelling, yeah)
# must return 1 if she can, 0 if she can't travel anymore (thus will forcibly drop out).
########
def CanContinueTravelling(self): # TO-DO UPDATE
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
		bStatus = 0
	else:
		pInstance, pInstancedict, specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, delay = nBSGDimensionalJumpBasicConfigInfo(pShip)
		try:
			InstateFTLStrCooldown(pInstance, remove=-1)
			timeR = AreWeOnFTLStretch(pInstance)
			if timeR == None or timeR <= 0.0:
				InstateFTLStrCooldown(pInstance, remove=1)
				bStatus = 0
		except:
			traceback.print_exc()
		
	if bStatus == 0 and bIsPlayer == 1:
		pSubtitleAction = App.SubtitleAction_CreateC("Brex: Jump!")
		if pSubtitleAction:
			pSubtitleAction.SetDuration(3.0)
			pSequence = App.TGSequence_Create ()
			pSequence.AddAction(pSubtitleAction)
			pSequence.Play()
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
# 1º entering travel sequence
# 2º during travel sequence
# 3º exiting travel sequence
########
# Another aux function I made
def PlaynBSGDimensionalJumpSound(pAction, pWS, sType, sRace):
	debug(__name__ + ", PlaynBSGDimensionalJumpSound")

	pShip = pWS.GetShip()
	return PlaynBSGDimensionalJumpSoundC(pAction, pShip, sType, sRace)

# Aux. ISI function
def PlaynBSGDimensionalJumpSoundI(pAction, pShipID, sType, sRace):
	debug(__name__ + ", PlaynBSGDimensionalJumpSoundI")
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShipID)
	if pShip != None:
		PlaynBSGDimensionalJumpSoundC(pAction, pShip, sType, sRace)
	return 0

# Aux. ISI function
def PlaynBSGDimensionalJumpSoundC(pAction, pShip, sType, sRace): #TO-DO Update with the sound from https://www.youtube.com/watch?v=sGCfC4NvQaY at 1:04
	debug(__name__ + ", PlaynBSGDimensionalJumpSoundC")

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

			if HasCloakedJumpSystem(pShip):
				if sType == "Enter Warp":
					sFile = "scripts/Custom/TravellingMethods/SFX/SigmaB5DriveSounds.wav" 
				else:
					sFile = "scripts/Custom/TravellingMethods/SFX/SigmaB5DriveSoundsExit.wav"

			elif HasPhasednBSGDimensionalJumpDrive(pShip):
				if sType == "Enter Warp":
					sFile = "scripts/Custom/TravellingMethods/SFX/shadowPhasedFScream.wav"
				else:
					sFile = "scripts/Custom/TravellingMethods/SFX/shadowPhasedFScream.wav"
			else:
				if sType == "Enter Warp":
					sFile = "scripts/Custom/TravellingMethods/SFX/enterjumpspace.wav"
				else:
					sFile = "scripts/Custom/TravellingMethods/SFX/exitjumpspace.wav"

			if sFile != None:
				pEnterSound = App.TGSound_Create(sFile, sType, 0)
				pEnterSound.SetSFX(0) 
				pEnterSound.SetInterface(1)

				App.g_kSoundManager.PlaySound(sType)
				#Custom.GravityFX.GravityFXlib.PlaySound(sFile, sRace+" "+sType+" B5 Sound")
		except:
			try:
				if sType == "Enter Warp":
					sFile = "scripts/Custom/TravellingMethods/SFX/enterjumpspace.wav"
				else:
					sFile = "scripts/Custom/TravellingMethods/SFX/exitjumpspace.wav"

				if sFile != None:
					Custom.GravityFX.GravityFXlib.PlaySound(sFile, sRace+" "+sType+" B5 Sound")
			except:
				print "nBSGDimensionalJump TravellingMethod: error while calling PlaynBSGDimensionalJumpSoundC:"
				traceback.print_exc()
	return 0

#Aux function.
def ConditionalDecloak(pAction, pShipID, instant = 0):
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShipID)
	if not pShip:
		return 0

	if HasPhasednBSGDimensionalJumpDrive(pShip):
		if pShip.IsCloaked():
			pCloak = pShip.GetCloakingSubsystem()
			if pCloak:
				if instant == 1:
					pCloak.InstantDecloak()
				else:
					pCloak.StopCloaking()
	return 0

# Aux. function
def ConditionalCloak(pAction, pShipID, instant = 0):
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShipID)
	if not pShip:
		return 0

	if HasPhasednBSGDimensionalJumpDrive(pShip):
		if not pShip.IsCloaked():
			pCloak = pShip.GetCloakingSubsystem()
			if pCloak:
				if instant == 1:
					pCloak.InstantCloak()
				else:
					pCloak.StartCloaking()
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

# Aux function TO-DO REMOVE UNECESSARY STUFF
def CreateDetachedElectricExplosion(fRed, fGreen, fBlue, fSize, fLifeTime, sFile, pEmitFrom, pAttachTo, fFrequency=1,fEmitLife=1,fSpeed=1.0, fBrightness= 0.7, vEmitPos=App.NiPoint3(0, 0, 0), vEmitDir=App.NiPoint3(0, 0, 0)):
	pEffect = None
	try:     
		pEffect = App.AnimTSParticleController_Create()

		pEffect.AddColorKey(0.1, 1.0, 1.0, 1.0)
		pEffect.AddColorKey(fBrightness, fRed / 255, fGreen / 255, fBlue / 255)
		pEffect.AddColorKey(1.0, 0.0, 0.0, 0.0)

		pEffect.AddAlphaKey(0.0, 1.0)
		pEffect.AddAlphaKey(0.7, 0.5)
		pEffect.AddAlphaKey(1.0, 0.0)


		pEffect.AddAlphaKey(0.0, 1.0)
		pEffect.AddAlphaKey(1.0, 1.0)

		pEffect.AddSizeKey(0.0, 0.8 * fSize)
		pEffect.AddSizeKey(0.2, 1.0 * fSize)
		pEffect.AddSizeKey(0.6, 1.0 * fSize)
		pEffect.AddSizeKey(0.8, 0.5 * fSize)
		pEffect.AddSizeKey(1.0, 0.1 * fSize)

		pEffect.SetEmitLife(fEmitLife)
		pEffect.SetEmitFrequency(fFrequency)
		pEffect.SetEffectLifeTime(fSpeed + fLifeTime)
		pEffect.SetInheritsVelocity(0)
		pEffect.SetDetachEmitObject(0) # If set to 1 it makes the main ship invisible LOL
		pEffect.CreateTarget(sFile)
		pEffect.SetTargetAlphaBlendModes(0, 7)
		pEffect.SetGravity(0, -5, 0)

		pEffect.SetDrawOldToNew(0) # TO-DO test line 1 makes it like normal, but 0?

		pEffect.SetEmitFromObject(pEmitFrom)

		pEffect.SetEmitPositionAndDirection(vEmitPos, vEmitDir)
		pEffect.AttachEffect(pAttachTo)         

		return pEffect
	except:
		print "nBSGDimensionalJump TravellingMethod: error while calling CreateDetachedElectricExplosion:"
		traceback.print_exc()
		pEffect = None

	return pEffect

# Aux function. TO-DO UPDATE AND ADD TO DOC
def NiPoint3ToTGPoint3(p, factor = 1.0):
		debug(__name__ + ", NiPoint3ToTGPoint3")
		kPoint = App.TGPoint3()
		kPoint.SetXYZ(p.x * factor, p.y * factor, p.z * factor)
		return kPoint

# Aux function. TO-DO UPDATE AND ADD TO DOC
def TGPoint3ToNiPoint3(p, factor=1.0):
	debug(__name__ + ", TGPoint3ToNiPoint3")
	kPoint = App.NiPoint3(p.x * factor, p.y * factor, p.z * factor)
	return kPoint

# Aux function. Create flash effect on a ship. TO-DO UPDATE AND ADD THAT IT NEEDS NANOFXV2 TO WORK
def nBSGDimensionalJumpFlash(pAction, pShipID, sType, sRace, sparkSize=5, sFile = 'scripts/Custom/TravellingMethods/GFX/nBSGDimensionalJumpFlashAlternate.tga'):
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShipID)
	if not pShip:
		return 0
	if pShip == None:
		return 0

	fEffectList = []
	try:
		if HasPhasednBSGDimensionalJumpDrive(pShip):
			return 0

		elif HasCloakedJumpSystem(pShip): # TO-DO ADJUST THIS
			if sType == "Enter Warp":
				sFile = "scripts/Custom/TravellingMethods/GFX/SigmaJumpspaceFlash.tga"
			else:
				sFile = "scripts/Custom/TravellingMethods/GFX/SigmaJumpspaceFlash.tga"

		else:
			if sType == "Enter Warp":
				sFile = "scripts/Custom/TravellingMethods/GFX/SigmaJumpspaceFlash.tga"
			else:
				sFile = "scripts/Custom/TravellingMethods/GFX/SigmaJumpspaceFlash.tga"

		if sparkSize > 0:
			colorKey = [255.0, 155.0, 55.0]

			LoadGFX(4, 4, sFile)

			pAttachTo = pShip.GetContainingSet().GetEffectRoot()
			shipR = pShip.GetRadius()
			fiSize = shipR * sparkSize # TO-DO WE MAY NEED TO TWEAK THIS FOR EACH SHIP AS A CASE-BY-CASE BASIS
			shipNode = pShip.GetNode() # NiPoint3
			frontDir = App.TGPoint3_GetModelForward() #TGPoint3
			shipFwd = TGPoint3ToNiPoint3(frontDir, shipR) # NiPoint3
			pEmitFrom = App.TGModelUtils_CastNodeToAVObject(shipNode) # TO-DO ADD pS

			try:
				pEffect = CreateDetachedElectricExplosion(colorKey[0], colorKey[1], colorKey[2], fiSize, 1, sFile, pEmitFrom, pAttachTo, fFrequency=1,fEmitLife=1,fSpeed=1, fBrightness=0.7, vEmitPos = shipFwd, vEmitDir    = App.NiPoint3(0, -1, 0)) # TO-DO ADD OTHER STUFF

				#import Custom.NanoFXv2.NanoFX_ScriptActions
				#pEffect = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile,
				#									pEmitFrom, 
				#									pAttachTo, 
				#									fSize = fiSize, 
				#									vEmitPos    = shipFwd, 
				#									vEmitDir    = App.NiPoint3(0, -1, 0),
				#									bInheritVel = 1,
				#									bDetach     = 0,
				#									fFrequency = 1,
				#									fLifeTime = 1,
				#									fEmitVel = None,
				#									fVariance = 150.0,
				#									fDamping    = None,
				#									vGravity    = None,
				#									iTiming = 72,
				#									sType = "Plasma",
				#									fRed = colorKey[0], 
				#									fGreen = colorKey[1], 
				#									fBlue = colorKey[2],
				#									fBrightness = 0.90) 
				
				if pEffect:
					fEffect = App.EffectAction_Create(pEffect)
					if fEffect:
						fEffectList.append(fEffect)
					#fEffectList.append(pEffect)
			except:
				print "nBSGDimensionalJump TravellingMethod: error while calling nBSGDimensionalJumpEnterFlash:"
				traceback.print_exc()

	except:
		print "nBSGDimensionalJump TravellingMethod: error while calling nBSGDimensionalJumpEnterFlash:"
		traceback.print_exc()
		fEffect = None

	lenef = len(fEffectList)
	if lenef > 0:
		pSequence = App.TGSequence_Create()
		for fEffect in fEffectList:
			pSequence.AddAction(fEffect, None)
		pSequence.Play()
                
	return 0

#######
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
			if hasattr(pInstance, "nBSGDimensionalJumpDriveISIvTowPosition"):
				del pInstance.nBSGDimensionalJumpDriveISIvTowPosition
		except:
			print "nBSGDimensionalJumpDrive: Error while calling removeTractorISITowInfo"
			traceback.print_exc()
		try:
			if hasattr(pInstance, "nBSGDimensionalJumpDriveISITowee"):
				del pInstance.nBSGDimensionalJumpDriveISITowee
		except:
			print "nBSGDimensionalJumpDrive: Error while calling removeTractorISITowInfo"
			traceback.print_exc()
		try:
			if hasattr(pInstance, "nBSGDimensionalJumpDriveISIbTractorStat"):
				del pInstance.nBSGDimensionalJumpDriveISIbTractorStat
		except:
			print "nBSGDimensionalJumpDrive: Error while calling removeTractorISITowInfo"
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

		pInstance.nBSGDimensionalJumpDriveISIvTowPosition = pTarget.GetWorldLocation()
		pInstance.nBSGDimensionalJumpDriveISIvTowPosition.Subtract( pShip.GetWorldLocation() )
		pInstance.nBSGDimensionalJumpDriveISIvTowPosition.MultMatrixLeft( pShip.GetWorldRotation().Transpose() )

		pInstance.nBSGDimensionalJumpDriveISITowee = pTarget.GetObjID()

		pInstance.nBSGDimensionalJumpDriveISIbTractorStat = 1

	except:
		print "nBSGDimensionalJumpDrive: Error while calling SetupTowingI"
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
		if hasattr(pInstance, "nBSGDimensionalJumpDriveISIbTractorStat") and pInstance.nBSGDimensionalJumpDriveISIbTractorStat == 1:
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

			if not hasattr(pInstance, "nBSGDimensionalJumpDriveISITowee"):
				return 0

			targetID = pInstance.nBSGDimensionalJumpDriveISITowee
			pTempTargetAux = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), targetID)
			if not pTempTargetAux:
				return 0

			# Update/Maintain the towee's position and speed with the tower.
			vPosition = App.TGPoint3()
			vPosition.Set( pInstance.nBSGDimensionalJumpDriveISIvTowPosition )
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
		print "nBSGDimensionalJumpDrive: Error while calling MaintainTowingActionI"
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

	if hasattr(pInstance, "nBSGDimensionalJumpDriveISIbTractorStat") and pInstance.nBSGDimensionalJumpDriveISIbTractorStat == 1 and hasattr(pInstance, "nBSGDimensionalJumpDriveISITowee") and pInstance.nBSGDimensionalJumpDriveISITowee != None:
		# hide the towee

		pToweeShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pInstance.nBSGDimensionalJumpDriveISITowee)
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

# ISI function TO-DO UPDATE
def SetupSequenceISI(pShip=None):
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

	hasTractorReady = pInstance != None and hasattr(pInstance, "nBSGDimensionalJumpDriveISIbTractorStat") and (pInstance.nBSGDimensionalJumpDriveISIbTractorStat == 1)

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

	myBoosting = 0.0
	if HasPhasednBSGDimensionalJumpDrive(pShip):
		myBoosting = 50.0
	elif HasCloakedJumpSystem(pShip):
		myBoosting = 0.0
		
	if (pPlayer != None) and (pShipID == pPlayer.GetObjID()):
		fEntryDelayTime = fEntryDelayTime + 0.1

		# Force a noninteractive cinematic view in space..
		pCinematicStart = App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0)
		pEngageWarpSeq.AddAction(pCinematicStart, None)

		pDisallowInput = App.TGScriptAction_Create("MissionLib", "RemoveControl")
		pEngageWarpSeq.AddAction(pDisallowInput, pCinematicStart)

	# An extra for checks
	pWarpAction0 = App.TGScriptAction_Create(__name__, "ConditionalCloak", pShipID, 0)
	pEngageWarpSeq.AddAction(pWarpAction0, None, fEntryDelayTime + 0.2)

	pWarpSoundAction1 = App.TGScriptAction_Create(__name__, "PlaynBSGDimensionalJumpSoundI", pShipID, "Enter Warp", sRace)
	pEngageWarpSeq.AddAction(pWarpSoundAction1, None, fEntryDelayTime + 0.2)
	
	pBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShipID, 1, myBoosting)
	pEngageWarpSeq.AddAction(pBoostAction, pWarpSoundAction1, 0.7)

	#try:
	#	import Custom.NanoFXv2.WarpFX.WarpFX
	#	pNacelleFlash = Custom.NanoFXv2.WarpFX.WarpFX.CreateNacelleFlashSeq(pShip, pShip.GetRadius())
	#	pEngageWarpSeq.AddAction(pNacelleFlash, pWarpSoundAction1)
	#except:
	#	pass

	fTimeToFlash = (fEntryDelayTime*2) + (1*(App.WarpEngineSubsystem_GetWarpEffectTime()/2.0))
	fCount = 0.0
	if hasTractorReady == 1:
		while fCount < fTimeToFlash:
			pMaintainTowingAction = App.TGScriptAction_Create(__name__, "MaintainTowingActionI", pShipID)
			pEngageWarpSeq.AddAction(pMaintainTowingAction, None, fCount)

			fCount = fCount + 0.01

	if fCount != fTimeToFlash:
		fTimeToFlash = fCount + 0.25

	# Create the warp flash.
	pFlashAction1 = App.TGScriptAction_Create(__name__, "nBSGDimensionalJumpFlash", pShipID, "Enter Warp", sRace)
	pEngageWarpSeq.AddAction(pFlashAction1, None, fTimeToFlash * 0.8)

	# Hide the ship.
	pHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShipID, 1)
	pEngageWarpSeq.AddAction(pHideShip, pFlashAction1, fTimeToFlash * 0.2)

	pUnBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShipID, 0, 1.0)
	pEngageWarpSeq.AddAction(pUnBoostAction, pHideShip)
	
	pCheckTowing = App.TGScriptAction_Create(__name__, "EngageSeqTractorCheckI", pShipID)
	pEngageWarpSeq.AddAction(pCheckTowing, pUnBoostAction)

	# An extra for checks
	pWarpActionN = App.TGScriptAction_Create(__name__, "ConditionalDecloak", pShipID, 1)
	pEngageWarpSeq.AddAction(pWarpActionN, None)	

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

	# An extra, ensures cooldown works
	pFlagShip = App.TGScriptAction_Create(__name__, "afterGlowFTLactISI", pShipID)
	pExitWarpSeq.AddAction(pFlagShip, None)

	# Extra added
	pWarpActionR0 = App.TGScriptAction_Create(__name__, "ConditionalCloak", pShipID, 1)
	pExitWarpSeq.AddAction(pWarpActionR0, None)

	# Check for towee
	if hasTractorReady == 1:
		pHideTowee = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pInstance.nBSGDimensionalJumpDriveISITowee, 1)
		pExitWarpSeq.AddAction(pHideTowee, pHideShip)

	# Create the warp flash.
	pFlashAction2 = App.TGScriptAction_Create(__name__, "nBSGDimensionalJumpFlash", pShipID, "Exit Warp", sRace)
	pExitWarpSeq.AddAction(pFlashAction2, pHideShip, 0.65)

	# Un-Hide the ship
	pUnHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShipID, 0)
	pExitWarpSeq.AddAction(pUnHideShip, pFlashAction2, 1.0)

	# Extra added
	pWarpActionRN = App.TGScriptAction_Create(__name__, "ConditionalDecloak", pShipID, 1)
	pExitWarpSeq.AddAction(pWarpActionRN, pUnHideShip, 0.01)

	# Un-hide the Towee, plus if it exists, also set up the maintain chain
	## REMEMBER: any changes in the time of this sequence will also require a re-check of this part, to make sure
	##           we're making the right amount of MaintainTowing actions.
	if hasTractorReady == 1:
		pUnHideTowee = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pInstance.nBSGDimensionalJumpDriveISITowee, 0)
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
	pBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShipID, 1, myBoosting)
	pExitWarpSeq.AddAction(pBoostAction, pUnHideShip, 0.1)

	# Play the vushhhhh of exiting warp
	pWarpSoundAction2 = App.TGScriptAction_Create(__name__, "PlaynBSGDimensionalJumpSoundI", pShipID, "Exit Warp", sRace)
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
	#	   tractor ships thru your travel. (in this example, thru nBSGDimensionalJumpDrive)
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

	myBoosting = 0.0
	if HasPhasednBSGDimensionalJumpDrive(pShip):
		myBoosting = 50.0
	elif HasCloakedJumpSystem(pShip):
		myBoosting = 0.0
	#TO-DO ADD SIZE REDUCTION AND RE-ESCALE
	#TO-DO ADD THE COOLDOWN THING
	#TO-DO CREATEA A FUNCTION THAT CHECKS SHIPS AROUND AND DAMAGES THEM SLIGHTLY
		
	if (pPlayer != None) and (pShipID == pPlayer.GetObjID()):
		fEntryDelayTime = fEntryDelayTime + 0.1

		# Force a noninteractive cinematic view in space..
		pCinematicStart = App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0)
		pEngageWarpSeq.AddAction(pCinematicStart, None)

		pWarpSoundAction0 = App.TGScriptAction_Create(__name__, "PlaynBSGDimensionalJumpSoundI", pShipID, "Enter Warp", sRace)
		pEngageWarpSeq.AddAction(pWarpSoundAction0, None, 0)

		pDisallowInput = App.TGScriptAction_Create("MissionLib", "RemoveControl")
		pEngageWarpSeq.AddAction(pDisallowInput, pCinematicStart)

	# An extra for checks
	pWarpAction0 = App.TGScriptAction_Create(__name__, "ConditionalCloak", pShipID, 0)
	pEngageWarpSeq.AddAction(pWarpAction0, None, fEntryDelayTime + 0.2)

	pWarpSoundAction1 = App.TGScriptAction_Create(__name__, "PlaynBSGDimensionalJumpSoundI", pShipID, "Enter Warp", sRace)
	pEngageWarpSeq.AddAction(pWarpSoundAction1, None, fEntryDelayTime + 0.2)
	
	pBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShipID, 1, myBoosting)
	pEngageWarpSeq.AddAction(pBoostAction, pWarpSoundAction1, 0.7)

	#try:
	#	import Custom.NanoFXv2.WarpFX.WarpFX
	#	pNacelleFlash = Custom.NanoFXv2.WarpFX.WarpFX.CreateNacelleFlashSeq(pShip, pShip.GetRadius())
	#	pEngageWarpSeq.AddAction(pNacelleFlash, pWarpSoundAction1)
	#	pWS.Logger.LogString("Using Nacelle Flash Sequence from NanoFXv2")
	#except:
	#	pass

	fTimeToFlash = (fEntryDelayTime*2) + (1*(App.WarpEngineSubsystem_GetWarpEffectTime()/2.0))
	if pWS.Travel.bTractorStat == 1:
		fCount = 0.0
		while fCount < fTimeToFlash:
			pMaintainTowingAction = App.TGScriptAction_Create(sCustomActionsScript, "MaintainTowingAction", pWS)
			pEngageWarpSeq.AddAction(pMaintainTowingAction, None, fCount)
			fCount = fCount + 0.01
			if fCount >= fTimeToFlash:
				break

	# Create the warp flash.
	pFlashAction1 = App.TGScriptAction_Create(__name__, "nBSGDimensionalJumpFlash", pShipID, "Enter Warp", sRace)
	pEngageWarpSeq.AddAction(pFlashAction1, None, fTimeToFlash * 0.8)

	# Hide the ship.
	pHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShipID, 1)
	pEngageWarpSeq.AddAction(pHideShip, pFlashAction1, fTimeToFlash * 0.2)

	pUnBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShipID, 0, 1.0)
	pEngageWarpSeq.AddAction(pUnBoostAction, pHideShip, 2.4)
	
	pCheckTowing = App.TGScriptAction_Create(sCustomActionsScript, "EngageSeqTractorCheck", pWS)
	pEngageWarpSeq.AddAction(pCheckTowing, pUnBoostAction, 0.25)

	# An extra for checks
	pWarpActionN = App.TGScriptAction_Create(__name__, "ConditionalDecloak", pShipID, 1)
	pEngageWarpSeq.AddAction(pWarpActionN, pHideShip)	

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

		# An extra, ensures cooldown works
		pFlagShip = App.TGScriptAction_Create(__name__, "afterGlowFTLact", pWS)
		pExitWarpSeq.AddAction(pFlagShip, None)
		
		# Extra added
		pWarpActionR0 = App.TGScriptAction_Create(__name__, "ConditionalCloak", pShipID, 1)
		pExitWarpSeq.AddAction(pWarpActionR0, None)

		# Check for towee
		if pWS.Travel.bTractorStat == 1:
			pHideTowee = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pWS.Travel.Towee.GetObjID(), 1)
			pExitWarpSeq.AddAction(pHideTowee, pHideShip)

		# Create the warp flash. # TO-DO ADD SOMETHING HERE THAT ADDS COOLDOWN AND REMOVES FTL STRETCH
		pFlashAction2 = App.TGScriptAction_Create(__name__, "nBSGDimensionalJumpFlash", pShipID, "Exit Warp", sRace)
		pExitWarpSeq.AddAction(pFlashAction2, pHideShip, 0.7)

		# Un-Hide the ship
		pUnHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShipID, 0)
		pExitWarpSeq.AddAction(pUnHideShip, pFlashAction2, 1.0)

		# Extra added
		pWarpActionRN = App.TGScriptAction_Create(__name__, "ConditionalDecloak", pShipID, 1)
		pExitWarpSeq.AddAction(pWarpActionRN, pUnHideShip, 0.01)

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
		pWarpSoundAction2 = App.TGScriptAction_Create(__name__, "PlaynBSGDimensionalJumpSoundI", pShipID, "Exit Warp", sRace)
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
def GetTravelSetToUse(self, manual=0):
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

	return None

########
# Method to convert the speed this ship is travelling at to Cs ("c" is the physical constant that is equal to the speed of light, in km/h. So,
# in other words, this method should convert the "speed" of the ship, which is relative to this travelling method, to how many times is the ship
# travelling faster than the speed of light.
# must return a float  (like 1.0)
########
def ConvertSpeedAmount(fSpeed):
	debug(__name__ + ", ConvertSpeedAmount")

	baseSpeed = 32 * 5 * 80.0
	mediumSpeed = 5.0
	AfactIs = 1.0
	speed = baseSpeed * math.pow((fSpeed/mediumSpeed), 4) * math.pow(20, (fSpeed - mediumSpeed) * AfactIs) # Ok so the Cylons required 10 jumps to go from Galactica to Caprica - while Battlestar Galactica required 200 - that's 20 times faster. I jsut have to make their warp factors so the Cylons are 1 step further from the Colonials

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
	if pWarpEngines == None:
		return 5.0
	fRealMaxSpeed = self.GetMaxSpeed()
	if self.IsPlayer == 1:
		fPower = pWarpEngines.GetPowerPercentageWanted()
	else:
		fPower = self.AIwarpPower
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
	if pWarpEngines == None:
		return 5.0
	fRealCruiseSpeed = self.GetCruiseSpeed()
	if self.IsPlayer == 1:
		fPower = pWarpEngines.GetPowerPercentageWanted()
	else:
		fPower = self.AIwarpPower
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
	pHull = self.Ship.GetHull()
	pPower = self.Ship.GetPowerSubsystem()
	return [ pWarpEngines, pHull, pPower]

########
# Method to return the list of coordinates (points in space) in this set which the ship can activate this travelling method from.
# must return a list  (like [])
########
def GetLaunchCoordinatesList(pSet):
	debug(__name__ + ", GetLaunchCoordinatesList")
	return []
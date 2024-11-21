# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# AlternateSubModelFTL.py
# 20th September 2024, by Alex SL Gato (CharaToLoki)
#         Based on Defiant's SubModels script (from which it inherits the classes, so in fact SubModels is a dependency) and BorgAdaptation.py by Alex SL Gato, which were based on the Foundation import function by Dasher
#         Also based on ATPFunctions by Apollo and slightly on DS9FXPulsarManager by USS Sovereign.
#################################################################################################################
# A modification of a modification, last modification by Alex SL Gato (CharaToLoki)
##################################################################################################################################################################################################################################
##################################################################################################################################################################################################################################
##########	MANUAL
##################################################################################################################################################################################################################################
##################################################################################################################################################################################################################################
# === INTRODUCTION ===
# The purpose of this plugin is to provide extended globalized actions for alternate TravellingMethods, providing them with the option to modify the model, like SubModels, but a bit less "broken"; as well as supporting SubModels Warp and Attack support.
# NOTE: This will not affect pre-existing TravellingMethods, a ship could have those and not use this tech at all.
# ATTENTION: This script has two classes "ProtoWarp" and "MovingEventUpdated" which inherit from Defiant's SubModels "SubModel" and "MovingEvent" classes, and also uses certain functions from that script - as such, it depends on it and that script being on scripts/Custom/Techs folder.
# WARNING: Also because they inherit from that class and use the same individual subList parameter, it is NOT RECOMMENDED to call SubModels and this technology on the same ship.
# ATTENTION: The script is also dependant on scripts/Custom/TravellingMethods and on GalaxyCharts to verify sub-technology and FTL availability. With those options turned off, the usefulness of this script is reduced to a cleaner customizable SubModels.
# === HOW-TO-USE a pre-existing FTL TravellingMethods that supports this tech ===
# Below there's a sample setup. Those familiarized with SubModels script will notice the script is basically identical, but with a twist, presenting extra elements related with the TravellingMethods files that support this file.
#
# On this case, we have a TravellingMethods file called ProtoWarp which is called inside as "Proto-Warp" (explanaton on how to add these are mentioned after the Sample Setup).
#
# For clarity, we will use the symbols:
# - "(*)"                - to determine something which is arbitrary to the TravellingMethods FTL sub-tech.
# - "(-)"                - to something that is optional but necessary to perform the function they indicate, or not globally necessary but still needed for a set of functions.
# - "(0)"                - to something that is optional but does nothing else that add a nice touch, since no other functions would be affected if they were skipped, for the most part.
# - "(#)"                - something that is always needed, or may always be needed if you need any figment of functionality outside of calling a literal empty version of the function.
# - "<insert_name_here>" - basically a generalization example for any other TravellingMethod. On this case in particular, <insert_name_here> = "Proto-Warp". Unless told otherwise, this generalization implies you can have as many of that field as you want, as long as <insert_name_here> is different for each one, allowing multiple TravellingMethods subModels support.
# - "c.s."               - "case-sensitive". That is, it will notice it is different if you type like this, LIKE THIS, LiKe ThIs and so on.
# - "<s-s>"              - "It uses the name of the ship File located at scripts/ships". Having a dummy ship with the smallest hardpoint possible should be the best. Also if the model is not a 300k vert creation. Please, for the sake of slow computers, try to follow this recommendation.
# - "<k:v>"              - key - value format. On python, key: value. Unless key or value are variables (or value is not an integer), you need to ensure they are between "" to indicate they are strings. Also it's c.s. "key like this" : "value like that", "unless the value for the key is a number like": 10 
#
# (#) On the "Setup" section, people will notice:
# -- (*) A ""Proto-Warp": {"Nacelles": ["Proto Warp Nacelle"], "Core": ["Proto-Core"], }," line, This can vary wildly between TravellingMethods, some may not even require a similar line, so check each one's readme (if they have it) to get more information on its SubTech. However for those modders that use this tech to validate if the ship is equipped or not, please do so somewhere inside the "Setup" field. On this case in particular, this line is simply arbitrarily defined here so the ProtoWarp TravellingMethods script, which uses this tech to verify the ship is equipped with it, can determine the ship has or does not have this tech. 
# -- (#) "Body" is a key whose value stores the model used during transformations. <s-s> <k:v> c.s.
# -- (#) "NormalModel" is a key whose value stores the model used when no red alert nor special warp or FTL method with this tech support happen. <s-s> <k:v> c.s.
# -- (-) "WarpModel" is a key whose value stores the model used when the ship uses warp, and no other FTL SubModel Warp Events are called. <s-s> <k:v> c.s.
# --------- Please note that while being (-), it pretty much is (#) if you added certain attack-related fields which are outside of "Setup".
# -- (-) "AttackModel" is a key whose value stores the model used when the ship is at red alert. <s-s> <k:v> c.s.
# --------- Please note that while being (-), it pretty much is (#) if you added certain warp-related fields which are outside of "Setup".
# -- (-) "<insert_name_here>Model" is a key whose value stores the model used when the ship uses <insert_name_here>, and will supersede the warp-related options. <k:v> <s-s> c.s.
# --------- Please note that while being (-), it pretty much is (#) if you added certain <insert_name_here>-related fields which are outside of "Setup".
# -- (0) "BodySetScale": indicates the model size multiplier during a transformation. Do not include to have default 1.0 (regular scale). <k:v>
# -- (0) "NormalSetScale": indicates the model size multiplier during normal conditions. Do not include to have default 1.0 (regular scale). <k:v>
# -- (0) "AttackSetScale": indicates the model size multiplier during red alert. Do not include to have default 1.0 (regular scale). <k:v>
# -- (0) "<insert_name_here>SetScale": indicates the model size multiplier during <insert_name_here> (f.ex. during Warp, during Proto-Warp). Do not include to have default 1.0 (regular scale). <k:v>
# -- (0) "Hardpoints": a dictionary which stores inside all subsystem property names in <k:v> format which would move after a transformation, regarding normal positions (including yellow alert).
# --------- On this case, each dictionary entry would be "Subsystem name" : [x, y, z]
# -- (0) "AttackHardpoints": a dictionary which stores inside all subsystem property names in <k:v> format which would move after a transformation, regarding red alert positions.
# --------- On this case, each dictionary entry would be "Subsystem name" : [x, y, z]
# -- (0) "WarpHardpoints": a dictionary which stores inside all subsystem property names in <k:v> format which would move after a transformation, regarding normal warp positions.
# --------- On this case, each dictionary entry would be "Subsystem name" : [x, y, z]
# -- (0) "<insert_name_here>Hardpoints": a dictionary which stores inside all subsystem property names in <k:v> format which would move after a transformation, regarding <insert_name_here> positions.
# --------- On this case, each dictionary entry would be "Subsystem name" : [x, y, z]
# (-) After that, there's a section for each non-main-body piece, in <k:v> format, with "k" being the inner name the piece will receive, and v a list of structure: ["A", D]
# --------- (#) "A" is the first value of the list, it is the ship model used for that particular piece during any transformation. <s-s> c.s.
# --------- (-) "D" is a dictionary containing positions and rotations for each situation. c.s.
# ---------------- (0) "<insert_name_here>Position": a dictionary entry which stores inside the movement in <k:v> format which the piece would move to during an <insert_name_here> transformation. On this example, "<insert_name_here>" could be nothing (thus "Position", for default), "Attack" (for red alert), "Warp" (for regular warp) or "Proto-Warp" (for Proto-Warp).
# ----------------------- Movement value is on [x, y, z]
# ---------------- (0) "<insert_name_here>Rotation": a dictionary entry which stores inside the rotation in <k:v> format which the piece would move to during an <insert_name_here> transformation. On this example, "<insert_name_here>" could be nothing (thus "Rotation", for default), "Attack" (for red alert), "Warp" (for regular warp) or "Proto-Warp" (for Proto-Warp).
# ----------------------- Rotation value is on [x, y, z] axis of rotation
# ---------------- (0) "SetScale": indicates the model size of a subpart. Do not include to have same behaviour as SubModels (regular scale but if the part has a too-extreme rotation (like, at least 90 degrees) it will suffer an asintotic process where it suddenly becomes small and then extremely big and inverted). <k:v>
# ---------------- (0) "Experimental": a dictionary entry which establishes if the ship uses experimental rotation or not. "Experimental": 0 or entry not added implies it uses the legacy submodels style of rotation.
# ------------------------ Legacy rotations are better for backwards-compatibility and may have less drifting issues, but only work for a particular quadrant of rotation ( -90, 90 ) degrees and are best for ( -45 degrees, 45 degrees) amplitude. They share the same issues SubModels rotations have.
# ------------------------ Experimental rotations are best suited if the ship requires to rotate more than that quadrant, but may also have their own range of issues.
#
# NOTE: In order to prevent some in-game engine shenanigans, it is recommended that ALL positions for each situation used are different, even if slightly, to prevent some cases of parts just floating if the beginning and end position were the same.
"""
#Sample Setup: replace "USSProtostar" for the appropiate abbrev
Foundation.ShipDef.USSProtostar.dTechs = {
	"Alternate-Warp-FTL": {
		"Setup": {
			"Proto-Warp": {	"Nacelles": ["Proto Warp Nacelle"], "Core": ["Proto-Core"], },
			"Body": "VasKholhr_Body",
			"NormalModel":          shipFile,
			"WarpModel":          "VasKholhr_WingUp",
			"Proto-WarpModel":          "VasKholhr_WingUp",
			"AttackModel":          "VasKholhr_WingDown",
			"BodySetScale": 1.0,
			"NormalSetScale": 1.0,
			"WarpSetScale": 1.0,
			"Proto-WarpSetScale": 1.0,
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
			"Proto-WarpHardpoints":       {
				"Proto Warp Nacelle":  [0.000000, -1.000000, -2.075000],
			},
		},

		"Port Wing":     ["VasKholhr_Portwing", {
			"Experimental": 0,
			"SetScale": 1.0,
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0], # normal Rotation used if not Red Alert and if not Warp
			"AttackRotation":         [0, -0.6, 0],
			"AttackDuration":         200.0, # Value is 1/100 of a second
			"AttackPosition":         [0, 0, 0.03],
			"WarpRotation":       [0, 0.349, 0],
			"WarpPosition":       [0, 0, 0.02],
			"WarpDuration":       150.0,
			"Proto-WarpRotation":       [0, 0.749, 0],
			"Proto-WarpPosition":       [0, 0, 0.05],
			"Proto-WarpDuration":       150.0,
			},
		],
        
		"Starboard Wing":     ["VasKholhr_Starboardwing", {
			"Experimental": 0,
			"SetScale": 1.0,
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0],
			"AttackRotation":         [0, 0.6, 0],
			"AttackDuration":         200.0, # Value is 1/100 of a second
			"AttackPosition":         [0, 0, 0.03],
			"WarpRotation":       [0, -0.349, 0],
			"WarpPosition":       [0, 0, 0.02],
			"WarpDuration":       150.0,
			"Proto-WarpRotation":       [0, -0.749, 0],
			"Proto-WarpPosition":       [0, 0, 0.05],
			"Proto-WarpDuration":       150.0,
			},
		],
	},
}
"""
#
# === HOW TO CREATE a compatible FTL TravellingMethods that supports this tech ===
# On this, we lean on GalaxyCharts since the file was originally meant to be for that.
# STEP 1. Create a proper GalaxyCharts TravellingMethod file, or modify a pre-existing one for your needs.
# STEP 2. The bare minimum to add would be the following:
"""
####### NOTE: From here to the next "NOTE" goes after the import statements of TRAVELER METHODS: #######
# These four lines should be uncommented only if they are missing. Please note that "from bcdebug import debug" may already be present at the very beginning of the file
#import App
#from bcdebug import debug
#import math
#import MissionLib
#import string

# These lines below are only used if needed (f.ex. because an auxiliar method uses them). Feel free to add more if needed for custom plugins.
import Foundation
import FoundationTech
#import traceback
 
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
	return "Proto-Warp" # Modify this with the name you are gonna use for the AlternateSubModelFTL

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

####### NOTE: From here to the next "NOTE" would replace the original "GetStartTravelEvents" and "GetExitedTravelEvents". On this case, we have left it so both our custom event and the warp-related events are called, to prove it is easy to add multiple events #######
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



"""
# STEP 3. Once we added that, we make sure we have a manual of sorts at the beginning of the file and we add those peculiarities, since certain quirks may make it need special things to be activated. Any other quirk we add to make the tech behave more like we want, would probably need to be mentioned in some way so any future user could have an easier way adding it.
# -- On our example, on the case of Proto-Warp, derived from Enhanced Warp, we wanted the tech to be only equipped on a certain FoundationTech dictionary, so we added/modified the following:
"""
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
		if pInstanceDict.has_key("Alternate-Warp-FTL") and pInstanceDict["Alternate-Warp-FTL"].has_key("Setup") and pInstanceDict["Alternate-Warp-FTL"]["Setup"].has_key("Proto-Warp"): # You need to add a foundation technology to this vessel "AlternateSubModelFTL"
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
	# Returns hardpoint property name fragments that indicate are part of the proto-warp system, and blacklists
	return ["protowarp", "proto warp", "proto-warp"], ["not a protowarp", "not a proto warp", "not a proto-warp", " not protowarp", " not proto warp", " not proto-warp"]

# This is just another auxiliar function I made for this
def ProtoWarpBasicConfigInfo(pShip):
	pInstance = findShipInstance(pShip) # On this case, IsShipEquipped(pShip) already checked this for us - HOWEVER do not forget to check if you modify the script
	pInstancedict = None
	specificNacelleHPList = None 
	specificCoreHPList = None
	if pInstance:
		pInstancedict = pInstance.__dict__ 
		if pInstanceDict.has_key("Alternate-Warp-FTL") and pInstanceDict["Alternate-Warp-FTL"].has_key("Setup") and pInstanceDict["Alternate-Warp-FTL"]["Setup"].has_key("Proto-Warp"):
			if pInstancedict["Alternate-Warp-FTL"]["Setup"]["Proto-Warp"].has_key("Nacelles"): # Use: if the tech has this field, use it. Must be a list. "[]" would mean that this field is skipped during checks.
				specificNacelleHPList = pInstancedict["Alternate-Warp-FTL"]["Setup"]["Proto-Warp"]["Nacelles"]
			if pInstancedict["Alternate-Warp-FTL"]["Setup"]["Proto-Warp"].has_key("Core"): # Use: if the tech has this field, use it. Must be a list. "[]" would mean that this field is skipped during checks.
				specificCoreHPList = pInstancedict["Alternate-Warp-FTL"]["Setup"]["Proto-Warp"]["Core"]

	hardpointProtoNames, hardpointProtoBlacklist = AuxProtoElementNames()

	return pInstance, pInstancedict, specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist

# This is just another auxiliar function I made for this
def ProtoWarpDisabledCalculations(type, specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, pSubsystem, pShip):
	totalProtoWarpEngines = 0
	onlineProtoWarpEngines = 0
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
						totalProtoWarpEngines = totalProtoWarpEngines + 1
						if pChild.GetCondition() > 0.0 and not pChild.IsDisabled():
							onlineProtoWarpEngines = onlineProtoWarpEngines + 1
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
							totalProtoWarpEngines = totalProtoWarpEngines + 1
							if pSubsystema.GetCondition() > 0.0 and not pSubsystema.IsDisabled():
								onlineProtoWarpEngines = onlineProtoWarpEngines + 1

		pShipList.TGDoneIterating()
		pShipList.TGDestroy()

	return totalProtoWarpEngines, onlineProtoWarpEngines

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
		return "This ship is not equipped with Proto-Warp"

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

	pInstance, pInstancedict, specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist = ProtoWarpBasicConfigInfo(pShip)

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
		elif specificNacelleHPList == None or (specificNacelleHPList != None and len(specificNacelleHPList) > 0):
			totalProtoWarpEngines, onlineProtoWarpEngines = ProtoWarpDisabledCalculations("Nacelle", specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, pWarpEngines, pShip)

			if totalProtoWarpEngines <= 0 or onlineProtoWarpEngines <= 0:
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

				return "Proto-Warp Engines disabled"
		
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
			return "Warp or Proto-Warp Engines offline"
	else:
		return "No Warp Engines"

	if specificCoreHPList != None and len(specificCoreHPList) > 0:
		totalProtoWarpCores, onlineProtoWarpCores = ProtoWarpDisabledCalculations("Core", specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, pWarpEngines, pShip)

		if totalProtoWarpCores <= 0 or onlineProtoWarpCores <= 0:
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
					pSubtitleAction = App.SubtitleAction_CreateC("Brex: We don't have proto-warp sir, we are dropping out of it.")
					pSubtitleAction.SetDuration(3.0)
					pSequence.AddAction(pSubtitleAction)
					pSequence.Play()
				bStatus = 0
			else:
				pInstance, pInstancedict, specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist = ProtoWarpBasicConfigInfo(pShip)
				if pInstance and pInstancedict:
					totalProtoWarpCores, onlineProtoWarpCores = ProtoWarpDisabledCalculations("Core", specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, pWarpEngines, pShip)
					if totalProtoWarpCores > 0 and onlineProtoWarpCores <= 0:
						if bIsPlayer == 1:
							pSequence = App.TGSequence_Create ()
							pSubtitleAction = App.SubtitleAction_CreateC("Brex: All Proto-Warp cores are offline or disabled sir, we are dropping out of proto-warp.")
							pSubtitleAction.SetDuration(3.0)
							pSequence.AddAction(pSubtitleAction)
							pSequence.Play()
						bStatus = 0
					elif (specificNacelleHPList == None or (specificNacelleHPList != None and len(specificNacelleHPList) > 0)):
						totalProtoWarpEngines, onlineProtoWarpEngines = ProtoWarpDisabledCalculations("Nacelle", specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, pWarpEngines, pShip)
						if totalProtoWarpEngines > 0 and onlineProtoWarpEngines <= 0:
							if bIsPlayer == 1:
								pSequence = App.TGSequence_Create ()
								pSubtitleAction = App.SubtitleAction_CreateC("Brex: All Proto-Warp nacelles are offline or disabled sir, we are dropping out of proto-warp.")
								pSubtitleAction.SetDuration(3.0)
								pSequence.AddAction(pSubtitleAction)
								pSequence.Play()
							bStatus = 0
				else:
					bStatus = 0
	else:
		bStatus = 0
	return bStatus
"""
# ------ Thus, the manual for Proto-Warp should look more or less like the following and before the from bcdebug import debug line:

# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# ProtoWarp.py
# prototype custom travelling method plugin script, by USS Frontier (Enhanced Warp, original) and then modified by Alex SL Gato for Proto-Warp
# 19th November 2024
#################################################################################################################
##########	MANUAL
#################################################################################################################
# NOTE: all functions/methods and attributes defined here (in this prototype example plugin, ProtoWarp) are required to be in the plugin, with the exclusion of:
# ------ MODINFO, which is there just to verify versioning.
# ------ ALTERNATESUBMODELFTL METHODS subsection, which are exclusively used for alternate SubModels for FTL which is a separate but linked mod, or to import needed modules.
# ------ Auxiliar functions: "AuxProtoElementNames", "findShipInstance", "ProtoWarpBasicConfigInfo" and "ProtoWarpDisabledCalculations".
# === How-To-Add ===
# This Travelling Method is Ship-based, on this case it needs of Foundation and FoundationTech to verify if the ship is equipped with it.
# This FTL method check is stored inside an "Alternate-Warp-FTL" dictionary, which is a script that should be located at scripts/Custom/Techs/AlternateSubModelFTL.py. While this sub-tech can work totally fine without such module installed, it is recommended to have it.
# On this case, due to that, only the lines marked with "# (#)" are needed for Proto-Warp to work, but the final parent technology may require more:
# "Proto-Warp": is the name of the key. This is the bare minimum for the technology to work
# "Nacelles": is the name of a key whose value indicates a list of which warp engine property children (nacelles) are part of the Proto-Warp system. If all are disabled/destroyed, Proto-Warp will not engage. If this field does not exist, it will check all warp hardpoints containing "protowarp", "proto warp" or "proto-warp" (case-insensitive). Leave as "Nacelles": [] to make it skip this disabled check.
# "Core": is the name of a key whose value indicates a list of which hardpoint properties (not nacelles) are part of the Proto-Warp system. If all are disabled/destroyed, Proto-Warp will not engage either. If this field does not exist or "Core": [] this check will be skipped.
"""
#Sample Setup: replace "USSProtostar" for the appropiate abbrev. Also remove "# (#)"
Foundation.ShipDef.USSProtostar.dTechs = { # (#)
	"Alternate-Warp-FTL": { # (#)
		"Setup": { # (#)
			"Proto-Warp": {	"Nacelles": ["Proto Warp Nacelle"], "Core": ["Proto-Core"], }, # (#)
			"Body": "VasKholhr_Body",
			"NormalModel":          shipFile,
			"WarpModel":          "VasKholhr_WingUp",
			"Proto-WarpModel":          "VasKholhr_WingUp",
			"AttackModel":          "VasKholhr_WingDown",
			"BodySetScale": 1.0,
			"NormalSetScale": 1.0,
			"WarpSetScale": 1.0,
			"Proto-WarpSetScale": 1.0,
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
			"Proto-WarpHardpoints":       {
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
			"Proto-WarpRotation":       [0, 0.749, 0],
			"Proto-WarpPosition":       [0, 0, 0.05],
			"Proto-WarpDuration":       150.0,
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
			"Proto-WarpRotation":       [0, -0.749, 0],
			"Proto-WarpPosition":       [0, 0, 0.05],
			"Proto-WarpDuration":       150.0,
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

##################################################################################################################################################################################################################################
##################################################################################################################################################################################################################################
##########	END OF MANUAL
##################################################################################################################################################################################################################################
##################################################################################################################################################################################################################################
#
#################################################################################################################
#
MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "0.4",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }
#
#################################################################################################################
#

import App
from bcdebug import debug
import FoundationTech
import loadspacehelper
import math
import MissionLib
import nt
import string
from SubModels import *
import traceback

REMOVE_POINTER_FROM_SET = 190
NO_COLLISION_MESSAGE = 192
REPLACE_MODEL_MSG = 208
SET_TARGETABLE_MSG = 209

# Because SubModels is ridiculously hard to make children without having to re-do all the functions, I've made this, so now you can just follow

eTypeDict = {}

_g_dExcludeSomePlugins = {
	# Some random plugins that I don't want to risk people attempting to load using this tech
	"000-Fixes20030217": 1,
	"000-Fixes20030221": 1,
	"000-Fixes20030305-FoundationTriggers": 1,
	"000-Fixes20030402-FoundationRedirect": 1,
	"000-Fixes20040627-ShipSubListV3Foundation": 1,
	"000-Fixes20040715": 1,
	"000-Fixes20230424-ShipSubListV4_7Foundation": 1,
	"000-Utilities-Debug-20040328": 1,
	"000-Utilities-FoundationMusic-20030410": 1,
	"000-Utilities-GetFileNames-20030402": 1,
	"000-Utilities-GetFolderNames-20040326": 1,
}

	# based on the FedAblativeArmour.py script, a fragment probably imported from ATP Functions by Apollo
def NiPoint3ToTGPoint3(p, factor = 1.0):
	debug(__name__ + ", NiPoint3ToTGPoint3")
	kPoint = App.TGPoint3()
	kPoint.SetXYZ(p.x * factor, p.y * factor, p.z * factor)
	return kPoint

def TGPoint3ToNiPoint3(p, factor=1.0):
	debug(__name__ + ", TGPoint3ToNiPoint3")
	kPoint = App.NiPoint3(p.x * factor, p.y * factor, p.z * factor)
	return kPoint

def findShipInstance(pShip):
	pInstance = None
	try:
		pInstance = FoundationTech.dShips[pShip.GetName()]
		if pInstance == None:
			print "After looking, no tech pInstance for ship:", pShip.GetName(), "How odd..."
		
	except:
		pass

	return pInstance

def findscriptsShipsField(pShip, thingToFind):
	thingFound = None
	pShipModule=__import__(pShip.GetScript())
	information = pShipModule.GetShipStats()
	if information != None and information.has_key(thingToFind):
		thingFound = information[thingToFind]
	return thingFound

# Set the parts for ProtoWarp state 
def StartingProtoWarp(pObject, pEvent, techP, move):
	debug(__name__ + ", StartingProtoWarp")
	StartingWarpCommon(pObject, pEvent, techP, move)

def ExitSetProto(pObject, pEvent, techType, move):
	debug(__name__ + ", ExitSet")
	pShip   = App.ShipClass_Cast(pEvent.GetDestination())
	sSetName = pEvent.GetCString()
	# if the system we come from is the warp system, then we exitwarp, right?
	if sSetName == "warp":
		# call ExitingProtoWarp in a few seconds
		pSeq = App.TGSequence_Create()
		pSeq.AppendAction(App.TGScriptAction_Create(__name__, "ExitingProtoWarp", pShip, techType, move), 4.0)
		pSeq.Play()
		
	pObject.CallNextHandler(pEvent)
	return 0

# Based on LoadExtraPlugins by Dasher42, but heavily modified so it only imports a few things
def LoadExtraLimitedPlugins(dExcludePlugins=_g_dExcludeSomePlugins):
	import string
	global vulnerableProjToSGShields, vulnerableBeamsToSGShields, defaultDummyNothing

	dir="scripts\\Custom\\TravellingMethods" # I want to limit any vulnerability as much as I can while keeping functionality
	try:
		list = nt.listdir(dir)
		if not list:
			print "ERROR: Missing scripts/Custom/TravellingMethods folder for AlternateSubModelFTL technology"
			return
	except:
		print "ERROR: Missing scripts/Custom/TravellingMethods folder for AlternateSubModelFTL technology, or other error:"
		traceback.print_exc()
		return		

	list.sort()

	dotPrefix = string.join(string.split(dir, "\\")[1:], ".") + "."

	filesChecked = {} 
	for plugin in list:
		s = string.split(plugin, ".")
		if len(s) <= 1:
			continue
	
		# Indexing by -1 lets us be sure we're grabbing the extension. -Dasher42
		extension = s[-1]
		fileName = string.join(s[:-1], ".")

		# We don't want to accidentally load wrong things
		if (extension == "py") and not fileName == "__init__": # I am not allowing people to just use the .pyc directly, I don't want people to not include source scripts - Alex SL Gato
			#print "AlternateSubModelFTL  script is reviewing " + fileName + " of dir " + dir
			if dExcludePlugins.has_key(fileName):
				debug(__name__ + ": Ignoring plugin" + fileName)
				continue

			try:
				if not filesChecked.has_key(fileName):
					filesChecked[fileName] = 1
					myGoodPlugin = dotPrefix + fileName

					try:
						banana = __import__(myGoodPlugin, globals(), locals(), ["AlternateFTLActionEnteringWarp", "AlternateFTLActionExitWarp"])
					except:
						banana = __import__(myGoodPlugin, globals(), locals())

					global eTypeDict
					if hasattr(banana, "AlternateFTLActionEnteringWarp"):

						eType, functionEnteringWarp = banana.AlternateFTLActionEnteringWarp() # Must be a regular function that only returns a type and function
						#print eType, functionEnteringWarp
						if eType and not eTypeDict.has_key(eType):
							eTypeDict[eType] = functionEnteringWarp

					if hasattr(banana, "AlternateFTLActionExitWarp"):
						eType2, functionExitWarp = banana.AlternateFTLActionExitWarp() # Must be a regular function that only returns a type and function
						if eType2 and not eTypeDict.has_key(eType2):
							eTypeDict[eType2] = functionExitWarp
			except:
				print "someone attempted to add more than they should to the SG Shields script"
				traceback.print_exc()

LoadExtraLimitedPlugins()

# This class controls the attach and detach of the Models
class ProtoWarp(SubModels):
	def __init__(self, name):
		debug(__name__ + ", Initiated")
		FoundationTech.TechDef.__init__(self, name)
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)
		# DO NOT ADD GLOBAL BROADCASTS FOR REGULAR WARP DRIVE-RELATED CALLS, USE LOCAL SHIP HANDLERS
		global eTypeDict
		for eType in eTypeDict.keys():
			App.g_kEventManager.RemoveBroadcastHandler(eType, self.pEventHandler, "FTLFunctionHandler")
			App.g_kEventManager.AddBroadcastPythonMethodHandler(eType, self.pEventHandler, "FTLFunctionHandler")

	def FTLFunctionHandler(self, pEvent):
		if not pEvent or pEvent == None:
			return 0
		eType = pEvent.GetEventType()
		if eType:
			pShip = pEvent.GetDestination()
			if pShip:
				pShip = App.ShipClass_Cast(pEvent.GetDestination())
				if pShip:
					iShipID = pShip.GetObjID()
					if iShipID and iShipID != App.NULL_ID:
						pShip = App.ShipClass_GetObjectByID(None, iShipID)
						if pShip:
							global eTypeDict
							try:
								eTypeDict[eType](pShip, pEvent, self, None)
							except:
								print "Error while performing custom FTL Warp:"
								traceback.print_exc()

	def MySystemPointer(self): # Name of the tech, for the dictionary
		return self.name

	def MySubPositionPointer(self): # Name of the sublists, for the tech's sub-dictionaries which may not be happy with the tech name for one reason or another
		return self.name

	def DoesItHaveTheTechnology(self, pShip):
		hasTheTech = 0
		pInstance = findShipInstance(pShip)
		pInstanceDict = None
		if pInstance:
			pInstanceDict = pInstance.__dict__
			if pInstanceDict.has_key(self.MySystemPointer()):
				hasTheTech = 1
		return hasTheTech, pInstanceDict

	# called by FoundationTech when a ship is created
	# Prepares the ship for moving its sub parts
	def AttachShip(self, pShip, pInstance):
		debug(__name__ + ", AttachShip")
		print "Ship %s with Alternative Warp FTL SubModel support added" % pShip.GetName()

		pShipID = pShip.GetObjID()
		sNamePrefix = str(pShipID) + "_"
		pInstanceDict = pInstance.__dict__
		pInstanceDict["OptionsList"] = [] # save options to this list, so we can access them later

		self.AddbAddedFTLSituationListener()

		ModelList = pInstanceDict[self.MySystemPointer()]
		AlertListener = 0
		
		if not ModelList.has_key("Setup"):
			print "Error: Cannot find Setup for Moving Parts and warp control"
			return

		pInstanceDict["Warp Overriden"] = 0 # Small trick to control regular Warp
		
		# Interate over every item
		for sNameSuffix in ModelList.keys():
			# if this is the setup, do the thinks for the whole ship 
			#we have to remember, like alert state
			if sNameSuffix == "Setup":
				dOptions = ModelList[sNameSuffix]

				dOptions1 = {}

				dOptions["AlertLevel"] = 0
				dOptions["GenMoveID"] = 0

                                for key in dOptions.keys():
                                    dOptions1[key] = dOptions[key]

				pInstance.OptionsList.append("Setup", dOptions1)
				continue # nothing more to do here

			#
			# the following stuff is only for the objects that move
			
			if len(ModelList[sNameSuffix]) > 1:
				dOptions = ModelList[sNameSuffix][1]
			sFile = ModelList[sNameSuffix][0]
			loadspacehelper.PreloadShip(sFile, 1)
			

			# save the shipfile for later use
			dofShip = [None, None]
			dofShip[0] = sNameSuffix
                        
			# save the shipfile for later use, this would be on "item[1]"
			dOptions2 = {}
			dOptions2["sShipFile"] = sFile
                        
			# set current rotation/position values
			if not dOptions.has_key("Position"):
				dOptions["Position"] = [0, 0, 0]
			dOptions2["currentPosition"] = dOptions["Position"]

			if not dOptions.has_key("Rotation"):
				dOptions["Rotation"] = [0, 0, 0]
			dOptions2["currentRotation"] = dOptions["Rotation"]

			dOptions2["curMovID"] = 0

			for key in dOptions.keys():
				dOptions2[key] = dOptions[key]

			dofShip[1] = dOptions2
			pInstance.OptionsList.append(dofShip)

			# event listener
			AlertListener = self.Add_FTLAndSituationMethods(dOptions, pShip, pInstanceDict, AlertListener)

		self.PerformPostAttachLoopActions(pShip, AlertListener)

	def AddbAddedFTLSituationListener(self):
		self.bAddedWarpListener = {} # these variables will make sure we add our event handlers only once
		self.bAddedAlertListener = {}

	def Add_FTLAndSituationMethods(self, dOptions, pShip, pInstanceDict, AlertListener):
		self.Add_CloakMethods(pShip)
		self.Add_WarpMethods(pShip, dOptions)
		AlertListener = self.Add_AttackMethods(pShip, dOptions, AlertListener, pInstanceDict)
		return AlertListener

	def Remove_FTLAndSituationMethods(self, pShip):
		self.Remove_CloakMethods(pShip)
		self.Remove_WarpMethods(pShip)
		self.Remove_AttackMethods(pShip)

	def Add_CloakMethods(self, pShip):
		self.Remove_CloakMethods(pShip)
		pShip.AddPythonFuncHandlerForInstance(App.ET_CLOAK_BEGINNING, __name__ + ".CloakHandler")
		pShip.AddPythonFuncHandlerForInstance(App.ET_DECLOAK_BEGINNING, __name__ + ".DecloakHandler")

	def Remove_CloakMethods(self, pShip):
		pShip.RemoveHandlerForInstance(App.ET_CLOAK_BEGINNING, __name__ + ".CloakHandler")
		pShip.RemoveHandlerForInstance(App.ET_DECLOAK_BEGINNING, __name__ + ".DecloakHandler")	

	def Add_AttackMethods(self, pShip, dOptions, AlertListener, pInstanceDict):
		if not self.bAddedAlertListener.has_key(pShip.GetObjID()) and (dOptions.has_key("AttackRotation") or dOptions.has_key("AttackPosition")):
			pShip.AddPythonFuncHandlerForInstance(App.ET_SET_ALERT_LEVEL, __name__ + ".AlertProtoStateChanged")
			# Alert change handler doesn't work for AI ships, so use subsystem changed instead
			pShip.AddPythonFuncHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateProtoChanged")
			self.bAddedAlertListener[pShip.GetObjID()] = 1 
			AlertListener = 1
		return AlertListener
	def Remove_AttackMethods(self, pShip):
		if self.bAddedAlertListener.has_key(pShip.GetObjID()):
			pShip.RemoveHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateProtoChanged")
			pShip.RemoveHandlerForInstance(App.ET_SET_ALERT_LEVEL, __name__ + ".AlertProtoStateChanged")
			try:
				del self.bAddedAlertListener[pShip.GetObjID()]
			except:
				pass

	def Add_WarpMethods(self, pShip, dOptions):
		if not self.bAddedWarpListener.has_key(pShip.GetObjID()) and (dOptions.has_key("WarpRotation") or dOptions.has_key("WarpPosition")):
			pShip.AddPythonFuncHandlerForInstance(App.ET_START_WARP, __name__ + ".StartingWarpE")
			pShip.AddPythonFuncHandlerForInstance(App.ET_START_WARP_NOTIFY, __name__ + ".StartingWarpE")
			# ET_EXITED_WARP handler doesn't seem to work, so use ET_EXITED_SET instead
			pShip.AddPythonFuncHandlerForInstance(App.ET_EXITED_SET, __name__ + ".ExitSetWarp")
			self.bAddedWarpListener[pShip.GetObjID()] = 1
	def Remove_WarpMethods(self, pShip):
		if self.bAddedWarpListener.has_key(pShip.GetObjID()):
			pShip.RemoveHandlerForInstance(App.ET_START_WARP, __name__ + ".StartingWarpE")
			pShip.RemoveHandlerForInstance(App.ET_START_WARP_NOTIFY, __name__ + ".StartingWarpE")
			pShip.RemoveHandlerForInstance(App.ET_EXITED_SET, __name__ + ".ExitSetWarp")
			try:
				del self.bAddedWarpListener[pShip.GetObjID()]
			except:
				pass

	def PerformPostAttachLoopActions(self, pShip, AlertListener):
		# Make sure the Ship is correctly set because we don't get the first ET_SUBSYSTEM_STATE_CHANGED event for Ai ships
		if AlertListener:
			PartsForWeaponProtoState(pShip, self)

	# Called by FoundationTech when a Ship is removed from set (eg destruction)
	def DetachShip(self, iShipID, pInstance):
		# get our Ship
		debug(__name__ + ", DetachShip")
		pShip = App.ShipClass_GetObjectByID(None, iShipID)
		if pShip:
			# remove the listeners
			self.Remove_FTLAndSituationMethods(pShip)
			
			if hasattr(pInstance, "OptionsList"):
				for item in pInstance.OptionsList:
					if item[0] == "Setup":
						if item[1].has_key("AlertLevel"):
							del item[1]["AlertLevel"]
						if item[1].has_key("GenMoveID"):
							del item[1]["GenMoveID"]
					else:
						if item[1].has_key("currentPosition"):
							del item[1]["currentPosition"]
						if item[1].has_key("currentRotation"):
							del item[1]["currentRotation"]
						if item[1].has_key("curMovID"):
							del item[1]["curMovID"]

			pInstanceDict = pInstance.__dict__
			if pInstanceDict and pInstanceDict.has_key("Warp Overriden"):
				try:
					pInstanceDict["Warp Overriden"] = None
				except:
					pass
				
		if hasattr(pInstance, "SubModelList"):
			for pSubShip in pInstance.SubModelList:
				try:
					pSubShip = App.ShipClass_GetObjectByID(None, pSubShip.GetObjID())
					if pSubShip:
						pSet = pSubShip.GetContainingSet()
						pSubName = pSubShip.GetName()
						if pSet and pSubName != None:
							DeleteObjectFromSet(pSet, pSubName)
				except:
					print "Error while calling AlternateSubModelFTL DetachShip SubModelList"
					traceback.print_exc()

			del pInstance.SubModelList

	# Attaches the SubParts to the Body Model
	# Detach is inherited from SubModels
	def AttachParts(self, pShip, pInstance):
		debug(__name__ + ", AttachParts")
		pSet = pShip.GetContainingSet()
		pInstance.__dict__["SubModelList"] = []
		ModelList = pInstance.__dict__[self.MySystemPointer()]

		pShipID = pShip.GetObjID()
		sNamePrefix = str(pShipID) + "_"
		SubModelList = pInstance.SubModelList

                pCloak = pShip.GetCloakingSubsystem()
                shipIsCloaking = 0
                shipIsDecloaking = 0
		if pCloak:
			shipIsCloaking = pCloak.IsCloaking() or pCloak.IsCloaked() 
			shipIsDecloaking = pCloak.IsDecloaking() or not pCloak.IsCloaked()

		# iteeeerate over every SubModel
		for sNameSuffix in ModelList.keys():
			if sNameSuffix == "Setup":
				continue

			sFile = ModelList[sNameSuffix][0]
			sShipName = sNamePrefix + sNameSuffix
			
			# check if the ship does exist first, before create it
			pSubShip = MissionLib.GetShip(sShipName)
			if not pSubShip:
				pSubShip = loadspacehelper.CreateShip(sFile, pSet, sShipName, "", 0, 1)
			SubModelList.append(pSubShip)

			# save the options list
			iSaveDone = 0

			dOptions = {} 
			# this is here to check if we already have the entry
			for lList in pInstance.OptionsList:
				if lList[0] != "Setup":
					proceed = 0
					if lList[0] == sNameSuffix:
						proceed = 1
					else:
						if (lList[0] != None):
							if hasattr(lList[0], "GetObjID") and (lList[0].GetName() == pSubShip.GetName()):
								proceed = 1

					if proceed > 0 and lList[1]["sShipFile"] == sFile:
						lList[0] = pSubShip
						iSaveDone = 1
						dOptions = lList[1]
						break
					

			#print iSaveDone, dOptions
			
			if not iSaveDone:
				print "AlternateSubModelFTL: rebuilding options"
     				if len(ModelList[sNameSuffix]) > 1:
     					dOptionsSingle = ModelList[sNameSuffix][1]

				loadspacehelper.PreloadShip(sFile, 1)

				# save the shipfile for later use, this would be on "item[1]"
				dOptions2 = {}
				dOptions2["sShipFile"] = sFile
                        
				# set current rotation/position values
				if not dOptionsSingle.has_key("Position"):
					dOptionsSingle["Position"] = [0, 0, 0]
				dOptions2["currentPosition"] = dOptionsSingle["Position"]

				if not dOptionsSingle.has_key("Rotation"):
					dOptionsSingle["Rotation"] = [0, 0, 0]
				dOptions2["currentRotation"] = dOptionsSingle["Rotation"]

				dOptions2["curMovID"] = 0

				for key in dOptionsSingle.keys():
					dOptions2[key] = dOptionsSingle[key]

				pInstance.OptionsList.append([pSubShip, dOptions2])
				dOptions = dOptions2


			# set current positions
			pSubShip.SetTranslateXYZ(dOptions["currentPosition"][0],dOptions["currentPosition"][1],dOptions["currentPosition"][2])

			scaleFactor = 1.0
			if dOptions.has_key("SetScale") and dOptions["SetScale"] != 0.0:
				scaleFactor = dOptions["SetScale"]

			if not (dOptions.has_key("Experimental") and dOptions["Experimental"] != 0.0):
				pSubShip.SetAngleAxisRotation(1.0, dOptions["currentRotation"][0], dOptions["currentRotation"][1], dOptions["currentRotation"][2])
				iNorm = math.sqrt(dOptions["currentRotation"][0] ** 2 + dOptions["currentRotation"][1] ** 2 + dOptions["currentRotation"][2] ** 2)
				pSubShip.SetScale((-iNorm + 1.85) * scaleFactor)
			else:
				# Since attempting to make the non-legacy version have the proper initial rotation when added just causes the experimental rotation system to get very wonky rotations no matter the type of fixes I do, we are going to temporarily let the experimental rotation handle that while we hide the ship.
				pSubShip.SetScale(scaleFactor)
				pSubShip.SetHidden(1)

			pSubShip.UpdateNodeOnly()


			
			pSubShip.SetUsePhysics(0)
			pSubShip.SetTargetable(0)
			mp_send_settargetable(pSubShip.GetObjID(), 0)
			pSubShip.SetInvincible(1)
			pSubShip.SetHurtable(0)
			#pSubShip.GetShipProperty().SetMass(1.0e+25)
			#pSubShip.GetShipProperty().SetRotationalInertia(1.0e+25)
			#pSubShip.GetShipProperty().SetStationary(1)
			pSubShip.SetHailable(0)
			if pSubShip.GetShields():
				pSubShip.GetShields().TurnOff()
	    
			pShip.EnableCollisionsWith(pSubShip, 0)
			pSubShip.EnableCollisionsWith(pShip, 0)
			MultiPlayerEnableCollisionWith(pShip, pSubShip, 0)
			for pSubShip2 in SubModelList:
				if pSubShip.GetObjID() != pSubShip2.GetObjID():
					pSubShip.EnableCollisionsWith(pSubShip2, 0)
					pSubShip2.EnableCollisionsWith(pSubShip, 0)
					MultiPlayerEnableCollisionWith(pSubShip, pSubShip2, 0)
			
			pShip.AttachObject(pSubShip)

			if pCloak:
				pSubShipID = pSubShip.GetObjID()
				if shipIsCloaking:
					CloakShip(pSubShipID, -1)
				elif shipIsDecloaking:
					CloakShip(pSubShipID, 1)

	# check if parts are attached
	def ArePartsAttached(self, pShip, pInstance):
		debug(__name__ + ", ArePartsAttached")
		if hasattr(pInstance, "SubModelList"):
			return 1
		return 0

	# Detaches the parts
	def DetachParts(self, pShip, pInstance):
		debug(__name__ + ", DetachParts")
		if hasattr(pInstance, "SubModelList"):
			for pSubShip in pInstance.SubModelList:
				pSet = pSubShip.GetContainingSet()
				pShip.DetachObject(pSubShip)
				DeleteObjectFromSet(pSet, pSubShip.GetName())
			del pInstance.SubModelList

oProtoWarp = ProtoWarp("Alternate-Warp-FTL")

# The class does the moving of the parts
# with every move the part continues to move
class MovingEventUpdated(MovingEvent):
        # prepare fore move...
        def __init__(self, pShip, item, fDuration, lStartingRotation, lStoppingRotation, lStartingTranslation, lStoppingTranslation, dHardpoints):
                debug(__name__ + ", __init__")

                self.iNacelleID = item[0].GetObjID()
		self.iShipID = pShip.GetObjID()
                self.iThisMovID = item[1]["curMovID"]
                self.dOptionsList = item[1]
                self.pShip = pShip
			
		self.fDurationMul = 0.94 # make us a little bit faster to avoid bad timing
	
                # rotation values
                self.iCurRotX = lStartingRotation[0]
                self.iCurRotY = lStartingRotation[1]
                self.iCurRotZ = lStartingRotation[2]
		if fDuration > 0:
			self.iRotStepX = (lStoppingRotation[0] - lStartingRotation[0]) / (fDuration * self.fDurationMul)
			self.iRotStepY = (lStoppingRotation[1] - lStartingRotation[1]) / (fDuration * self.fDurationMul)
			self.iRotStepZ = (lStoppingRotation[2] - lStartingRotation[2]) / (fDuration * self.fDurationMul)
		else:
			self.iRotStepX = (lStoppingRotation[0] - lStartingRotation[0])
			self.iRotStepY = (lStoppingRotation[1] - lStartingRotation[1])
			self.iRotStepZ = (lStoppingRotation[2] - lStartingRotation[2])
                
                # translation values
                self.iCurTransX = lStartingTranslation[0]
                self.iCurTransY = lStartingTranslation[1]
                self.iCurTransZ = lStartingTranslation[2]
		if fDuration > 0:
			self.iTransStepX = (lStoppingTranslation[0] - lStartingTranslation[0]) / (fDuration * self.fDurationMul)
			self.iTransStepY = (lStoppingTranslation[1] - lStartingTranslation[1]) / (fDuration * self.fDurationMul)
			self.iTransStepZ = (lStoppingTranslation[2] - lStartingTranslation[2]) / (fDuration * self.fDurationMul)
		else:
			self.iTransStepX = (lStoppingTranslation[0] - lStartingTranslation[0])
			self.iTransStepY = (lStoppingTranslation[1] - lStartingTranslation[1])
			self.iTransStepZ = (lStoppingTranslation[2] - lStartingTranslation[2])
		
		self.dStopHardpoints = dHardpoints
		self.dStartHardpoints = {}
		self.dCurHPs = {}
		for sHP in self.dStopHardpoints.keys():
			lPos = None
			pHP = MissionLib.GetSubsystemByName(pShip, sHP)
			pPOP = GetPositionOrientationPropertyByName(pShip, sHP)
			if pHP:
				NiPoint3 = pHP.GetPosition()
				lPos = [NiPoint3.x, NiPoint3.y, NiPoint3.z]
			elif pPOP:
				TGPoint3 = pPOP.GetPosition()
				lPos = [TGPoint3.x, TGPoint3.y, TGPoint3.z]
			else:
				print "Submodel Error: Unable to find Hardpoint %s" % sHP
			if lPos:
				self.dStartHardpoints[sHP] = lPos
				self.dCurHPs[sHP] = lPos

		self.dHPSteps = {}
		for sHP in self.dStartHardpoints.keys():
			self.dHPSteps[sHP] = [0, 0, 0]
			
			if fDuration > 0:
				self.dHPSteps[sHP][0] = (self.dStopHardpoints[sHP][0] - self.dStartHardpoints[sHP][0]) / (fDuration * self.fDurationMul)
				self.dHPSteps[sHP][1] = (self.dStopHardpoints[sHP][1] - self.dStartHardpoints[sHP][1]) / (fDuration * self.fDurationMul)
				self.dHPSteps[sHP][2] = (self.dStopHardpoints[sHP][2] - self.dStartHardpoints[sHP][2]) / (fDuration * self.fDurationMul)
			else:
				self.dHPSteps[sHP][0] = (self.dStopHardpoints[sHP][0] - self.dStartHardpoints[sHP][0])
				self.dHPSteps[sHP][1] = (self.dStopHardpoints[sHP][1] - self.dStartHardpoints[sHP][1])
				self.dHPSteps[sHP][2] = (self.dStopHardpoints[sHP][2] - self.dStartHardpoints[sHP][2])

		self.firstTime = 1
		if self.dOptionsList.has_key("Experimental") and self.dOptionsList["Experimental"] != 0.0:
			# Since the thing below causes the system to get wonky rotations, I'm gonna do a move called hiding the ship until it's properly moved.
			item[0].SetHidden(1)
			"""
			pNacelle = App.ShipClass_GetObjectByID(None, self.iNacelleID)
			if pNacelle:
				# Future TO-DO: CHECK WHY WHEN USED ON CALL, NO ISSUES HAPPEN, BUT WHEN IT'S USED ON HERE OR ATTACHPARTS, ISSUES HAPPEN
				# set new Rotation values
				self.iCurRotX = self.iCurRotX + self.iRotStepX
				self.iCurRotY = self.iCurRotY + self.iRotStepY
				self.iCurRotZ = self.iCurRotZ + self.iRotStepZ

				# set new Translation values
				self.iCurTransX = self.iCurTransX + self.iTransStepX
				self.iCurTransY = self.iCurTransY + self.iTransStepY
				self.iCurTransZ = self.iCurTransZ + self.iTransStepZ
				# set Translation
				pNacelle.SetTranslateXYZ(self.iCurTransX, self.iCurTransY, self.iCurTransZ)

				# set Experimental rotation and re-scaling
				self.firstTime = performRotationAndScaleAdjust(pShip, pNacelle, self.dOptionsList, self.iCurRotX, self.iCurRotY, self.iCurRotZ, self.iCurRotX, self.iCurRotY, self.iCurRotZ, self.firstTime)
			"""

		self.wentWrong = 0

	# move!
	def __call__(self):
		# if the move ID doesn't match then this move is outdated
		debug(__name__ + ", __call__")
		# this makes sure the game does not crash when trying to access a deleted element

                pShip = App.ShipClass_GetObjectByID(None, self.iShipID)
                if not pShip:
                        #print "Moving Error: Lost MAIN part"
                        return 0

                if not hasattr(self, "iNacelleID"):
                        return 0

		pNacelle = App.ShipClass_GetObjectByID(None, self.iNacelleID)
		if not pNacelle:
			#print "Moving Error: Lost part"
			return 0
		
                if (not self.dOptionsList.has_key("curMovID")) or self.iThisMovID != self.dOptionsList["curMovID"]:
                        print "Moving Error: Move no longer active"
                        return 1

		# set new Rotation values
		self.iCurRotX = self.iCurRotX + self.iRotStepX
		self.iCurRotY = self.iCurRotY + self.iRotStepY
		self.iCurRotZ = self.iCurRotZ + self.iRotStepZ
		# set Rotation
		self.firstTime = performRotationAndScaleAdjust(pShip, pNacelle, self.dOptionsList, self.iCurRotX, self.iCurRotY, self.iCurRotZ, self.iRotStepX, self.iRotStepY, self.iRotStepZ, self.firstTime)

		# set new Translation values
		self.iCurTransX = self.iCurTransX + self.iTransStepX
		self.iCurTransY = self.iCurTransY + self.iTransStepY
		self.iCurTransZ = self.iCurTransZ + self.iTransStepZ
		# set Translation
		pNacelle.SetTranslateXYZ(self.iCurTransX, self.iCurTransY, self.iCurTransZ)


		
		self.dOptionsList["currentRotation"] = [self.iCurRotX, self.iCurRotY, self.iCurRotZ]
		self.dOptionsList["currentPosition"] = [self.iCurTransX, self.iCurTransY, self.iCurTransZ]
		
		# Hardpoints
		if self.dCurHPs != None:
			for sHP in self.dCurHPs.keys():
				self.dCurHPs[sHP][0] = self.dCurHPs[sHP][0] + self.dHPSteps[sHP][0]
				self.dCurHPs[sHP][1] = self.dCurHPs[sHP][1] + self.dHPSteps[sHP][1]
				self.dCurHPs[sHP][2] = self.dCurHPs[sHP][2] + self.dHPSteps[sHP][2]
				UpdateHardpointPositionsTo(self.pShip, sHP, self.dCurHPs[sHP])
		
		pNacelle.UpdateNodeOnly()
		return 0


def performRotationAndScaleAdjust(pShip, pNacelle, dOptionsList, iCurRotX, iCurRotY, iCurRotZ, iRotStepX, iRotStepY, iRotStepZ, firstTime, iWait = 2.0): # iWait is to compensate steps

	scaleFactor = 1.0
	if dOptionsList.has_key("SetScale") and dOptionsList["SetScale"] != 0.0:
		scaleFactor = dOptionsList["SetScale"]

	if dOptionsList.has_key("Experimental") and dOptionsList["Experimental"] != 0.0:

		# Since we have issues with "pNacelle.SetAngleAxisRotation(1.0, iCurRotX, iCurRotY, iCurRotZ)" only working for one quadrant, and with "pNacelle.SetMatrixRotation(rotationMatrix)" suffering the same problem, we need to find another way.
		# On this case, "pNacelle.Rotate(rotationMatrix)" is an ideal option, but for that to work we need to perform some calculations.
		# First, we need to know the rotation per-tick, fortunately we already know, it's the iStepRot!
		# Alongside knowing this, we can use that to simplify our calculus, just using infinitesimal rotation matrixes, which have several advantages, among them that are mostly commutative with each other.
		"""
			    (    1            -iRotStepZ       iRotStepY )
			A = ( iRotStepZ           1           -iRotStepX )
			    (-iRotStepY        iRotStepX           1     )

		"""
		# BUT WAIT, in-game Rotation considers matrixes with global World coordinates, not pShip individual coordinates - we need to transform these parameters to global World ones.
		# We know that the Y axis angle is iRotStepY... but how is that in global? We need to know the general rotation we are interested in - since these nacelles are attached to the ship, it's the parent's ship rotation!

		parentShipRotation = pShip.GetWorldRotation()

		baseXrotationAngle = App.TGPoint3()
		baseXrotationAngle.SetXYZ(iRotStepX * iWait, 0.0, 0.0)

		vGlobalDirX = App.TGPoint3()
		vGlobalDirX.Set(baseXrotationAngle)
		vGlobalDirX.MultMatrixLeft(parentShipRotation)

		if firstTime > 0:
			iRotStepX = iCurRotX + iRotStepX
			iRotStepY = iCurRotY + iRotStepY
			iRotStepZ = iCurRotZ + iRotStepZ

		baseYrotationAngle = App.TGPoint3()
		baseYrotationAngle.SetXYZ(0.0, iRotStepY * iWait, 0.0)

		vGlobalDirY = App.TGPoint3()
		vGlobalDirY.Set(baseYrotationAngle)
		vGlobalDirY.MultMatrixLeft(parentShipRotation)

		baseZrotationAngle = App.TGPoint3()
		baseZrotationAngle.SetXYZ(0.0, 0.0, iRotStepZ * iWait)

		vGlobalDirZ = App.TGPoint3()
		vGlobalDirZ.Set(baseZrotationAngle)
		vGlobalDirZ.MultMatrixLeft(parentShipRotation)

		vGlobalFinalAngles = App.TGPoint3()
		vGlobalFinalAngles.SetXYZ(vGlobalDirX.x + vGlobalDirY.x + vGlobalDirZ.x , vGlobalDirX.y + vGlobalDirY.y + vGlobalDirZ.y, vGlobalDirX.z + vGlobalDirY.z + vGlobalDirZ.z)

		firstCol = App.TGPoint3()
		firstCol.SetXYZ(1.0 , -vGlobalFinalAngles.z, vGlobalFinalAngles.y)
		secondCol = App.TGPoint3()
		secondCol.SetXYZ(vGlobalFinalAngles.z , 1.0, -vGlobalFinalAngles.x)
		thirdCol = App.TGPoint3()
		thirdCol.SetXYZ(-vGlobalFinalAngles.y , vGlobalFinalAngles.x, 1.0)

		kRot = App.TGMatrix3()
		kRot.SetCol(0, firstCol)
		kRot.SetCol(1, secondCol)
		kRot.SetCol(2, thirdCol)

		pNacelle.Rotate(kRot)
		pNacelle.SetScale(scaleFactor)

		if firstTime > 0:
			pNacelle.SetHidden(0)

	else:
		pNacelle.SetAngleAxisRotation(1.0, iCurRotX, iCurRotY, iCurRotZ)
		iNorm = math.sqrt(iCurRotX ** 2 + iCurRotY ** 2 + iCurRotZ ** 2)
		pNacelle.SetScale((-iNorm + 1.85) * scaleFactor)


	return 0


def MatrixMult(kFwd, kNewUp):
	debug(__name__ + ", MatrixMult")
	vAuxVx = kFwd.y * kNewUp.z - kNewUp.y * kFwd.z
	vAuxVy = kNewUp.x * kFwd.z - kFwd.x * kNewUp.z
	vAuxVz = kFwd.x * kNewUp.y - kNewUp.x * kFwd.y
	return vAuxVx, vAuxVy, vAuxVz

def MatrixDet(matrix):
	debug(__name__ + ", MatrixDet")
	secondRow = {"x": matrix[3], "y": matrix[4], "z": matrix[5]}
	ThirdRow = {"x": matrix[3], "y": matrix[4], "z": matrix[5]}
	vAuxVx, vAuxVy, vAuxVz = MatrixMult(secondRow, ThirdRow)
	return vAuxVx * matrix[0] + vAuxVy * matrix[1] + vAuxVz * matrix[2]


def IncCurrentMoveIDUpdated(pShip, pInstance):
	debug(__name__ + ", IncCurrentMoveIDUpdated")
	if hasattr(pInstance, "OptionsList"):
		for item in pInstance.OptionsList:
			if item[0] == "Setup":
				item[1]["GenMoveID"] = item[1]["GenMoveID"] + 1


def GetCurrentMoveIDUpdated(pShip, pInstance):
	debug(__name__ + ", GetCurrentMoveIDUpdated")
	iGenMoveID = 0
	if hasattr(pInstance, "OptionsList"):	
		for item in pInstance.OptionsList:
			if item[0] == "Setup":
				iGenMoveID = item[1]["GenMoveID"]
	return iGenMoveID
			

def MoveFinishMatchIDUpdated(pShip, pInstance, iThisMovID):
	debug(__name__ + ", MoveFinishMatchIDUpdated")
	try:
		if GetCurrentMoveIDUpdated(pShip, pInstance) == iThisMovID:
			return 1
	except:
		return 0
	return 0

def CloakShip(pNacelleID, decloak=0):
    debug(__name__ + ", CloakShip")
    pNacelle = App.ShipClass_GetObjectByID(None, pNacelleID)
    if not pNacelle:
        #print "Moving Error: Lost part"
        return 0

    pCloak = pNacelle.GetCloakingSubsystem()
    if pCloak:
        if decloak == 0:
            pCloak.StartCloaking()
        elif decloak == 1:
            pCloak.InstantDecloak()
        elif decloak == -1:
            pCloak.InstantCloak()


def CloakHandler(pObject, pEvent):
        debug(__name__ + ", CloakHandler")
        pInstance = findShipInstance(pObject)

        pShip = App.ShipClass_GetObjectByID(None, pInstance.pShipID)

        iType = pShip.GetAlertLevel()
        iLongestTime = 0.0
        dHardpoints = {}
        
        # check if ship still exits
        pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
        if not pShip:
                return

        # iterate over every Turret
        pCloak = pShip.GetCloakingSubsystem()
        if pCloak and hasattr(pInstance, "SubModelList"):
            shipIsCloaking = pCloak.IsCloaking()
            shipIsDecloaking = pCloak.IsDecloaking()
            for pSubShip in pInstance.TurretList:
                        pSubShipID = pSubShip.GetObjID()
                        if shipIsCloaking:
                            CloakShip(pSubShipID, 0)
                        elif shipIsDecloaking:
                            CloakShip(pSubShipID, 1)

        pObject.CallNextHandler(pEvent)

def DecloakHandler(pObject, pEvent):
        debug(__name__ + ", DecloakHandler")
        pInstance = findShipInstance(pObject)

        pShip = App.ShipClass_GetObjectByID(None, pInstance.pShipID)

        iType = pShip.GetAlertLevel()
        iLongestTime = 0.0
        dHardpoints = {}
        
        # check if ship still exits
        pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
        if not pShip:
                return

        # iterate over every Turret
        pCloak = pShip.GetCloakingSubsystem()
        if pCloak and hasattr(pInstance, "SubModelList"):
            shipIsCloaking = pCloak.IsCloaking()
            shipIsDecloaking = pCloak.IsDecloaking()
            for pSubShip in pInstance.TurretList:
                        pSubShipID = pSubShip.GetObjID()
                        if shipIsCloaking:
                            CloakShip(pSubShipID, 0)
                        elif shipIsDecloaking:
                            CloakShip(pSubShipID, 1)

        pObject.CallNextHandler(pEvent)


# calls the MovingEventUpdated class and returns its return value
def MovingActionUpdated(pAction, oMovingEventUpdated):
	debug(__name__ + ", MovingActionUpdated")
	return oMovingEventUpdated()

def AlertProtoStateChanged(pObject, pEvent, techP = oProtoWarp):
	debug(__name__ + ", AlertProtoStateChanged")
	pObject.CallNextHandler(pEvent)
	pShip = App.ShipClass_Cast(pObject)
	if pShip:
		pShipID = pShip.GetObjID()
		if pShipID:
			pShip = App.ShipClass_GetObjectByID(None, pShipID)
			if pShip:
				pSeq = App.TGSequence_Create()
				pSeq.AppendAction(App.TGScriptAction_Create(__name__, "AlertProtoStateChangedAction", pShip, techP), 0.1)
				pSeq.Play()
	return 0


def AlertProtoStateChangedAction(pAction, pShip, techP = oProtoWarp):
	debug(__name__ + ", AlertProtoStateChangedAction")
	PartsForWeaponProtoState(pShip, techP)
	return 0

# called when a ship changes Power of one of its subsystems
# cause this is possible also an alert event
def SubsystemStateProtoChanged(pObject, pEvent, techP = oProtoWarp):
	debug(__name__ + ", SubsystemStateProtoChanged")
	pShip = App.ShipClass_Cast(pObject)
	pSubsystem = pEvent.GetSource()

	# if the subsystem that changes its power is a weapon
	if pSubsystem.IsTypeOf(App.CT_WEAPON_SYSTEM):
		# set wings for this alert state
		PartsForWeaponProtoState(pShip, techP)
		
	pObject.CallNextHandler(pEvent)
	return 0      

# Prepares a ship to move: Replaces the current Model with the move Model and attaches its sub Models
def PrepareShipForProtoMove(pShip, pInstance, techType=oProtoWarp):
	debug(__name__ + ", PrepareShipForProtoMove")
	if not techType.ArePartsAttached(pShip, pInstance):
		techName = techType.MySystemPointer()
		ReplaceModel(pShip, pInstance.__dict__[techName]["Setup"]["Body"])
		techType.AttachParts(pShip, pInstance)
		scaleFactor = 1.0
		if pInstance.__dict__[techName]["Setup"].has_key("BodySetScale") and pInstance.__dict__[techName]["Setup"]["BodySetScale"] != 0.0:
			scaleFactor = pInstance.__dict__[techName]["Setup"]["BodySetScale"]
		pShip.SetScale(scaleFactor)

	checkingReCloak(pShip)
	return 0

def checkingReCloak(pShip):
	try:
		pShipID = pShip.GetObjID()
		if pShipID:
			pShip = App.ShipClass_GetObjectByID(None, pShipID)
		if pShip:
			pCloak = pShip.GetCloakingSubsystem()
			if pCloak:
				shipIsCloaking = pCloak.IsCloaking() or pCloak.IsCloaked() 
				shipIsDecloaking = pCloak.IsDecloaking() or not pCloak.IsCloaked()
				if shipIsCloaking:
					CloakShip(pShipID, -1)
				#elif shipIsDecloaking:
				#	CloakShip(pShipID, 1)

	except:
		traceback.print_exc()

	return 0


# called after the Alert move action
# Remove the attached parts and use the attack or normal model now
def AlertMoveFinishProtoAction(pAction, pShip, pInstance, iThisMovID, techType = oProtoWarp):
	
	# Don't switch Models back when the ID does not match
	debug(__name__ + ", AlertMoveFinishProtoAction")
	if not MoveFinishMatchIDUpdated(pShip, pInstance, iThisMovID):
		return 0
	try:
		techType.DetachParts(pShip, pInstance)
	except:
		pass

	techName = techType.MySystemPointer()
	scaleFactor = 1.0
	if pShip.GetAlertLevel() == 2:
		sNewShipScript = pInstance.__dict__[techName]["Setup"]["AttackModel"]
		if pInstance.__dict__[techName]["Setup"].has_key("AttackSetScale") and pInstance.__dict__[techName]["Setup"]["AttackSetScale"] != 0.0:
			scaleFactor = pInstance.__dict__[techName]["Setup"]["AttackSetScale"]
	else:
		sNewShipScript = pInstance.__dict__[techName]["Setup"]["NormalModel"]
		if pInstance.__dict__[techName]["Setup"].has_key("NormalSetScale") and pInstance.__dict__[techName]["Setup"]["NormalSetScale"] != 0.0:
			scaleFactor = pInstance.__dict__[techName]["Setup"]["NormalSetScale"]
	ReplaceModel(pShip, sNewShipScript)
	pShip.SetScale(scaleFactor)
	checkingReCloak(pShip)

	return 0

### Up to here were the things for Attack - warp is better.

# called when a ship exits a Set. Replacement for WARP_END Handler.
def ExitSetWarp(pObject, pEvent, techType = oProtoWarp, move="Warp"):
	if not pEvent:
		return 0

	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	if not pShip:
		return 0

	pShipID = pShip.GetObjID()
	if not pShipID:
		return 0

	pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
	if not pShip:
		return 0
	
	pInstance = findShipInstance(pShip)
	if not pInstance:
		if pObject:
			pObject.CallNextHandler(pEvent)
		return 0
	pInstanceDict = pInstance.__dict__
	if pInstanceDict and pInstanceDict.has_key("Warp Overriden"):
		if move == "Warp":
			if pInstanceDict["Warp Overriden"] > 0:
				if pObject:
					pObject.CallNextHandler(pEvent)
				return 0

	ExitSetProto(pObject, pEvent, techType, move)
	return 0

def ExitSetProto(pObject, pEvent, techType, move):
	debug(__name__ + ", ExitSet")
	pShip   = App.ShipClass_Cast(pEvent.GetDestination())
	sSetName = pEvent.GetCString() # It is a TGStringEvent

	# if the system we come from is the warp system, then we exitwarp, right?
	if sSetName == "warp":
		# call ExitingProtoWarp in a few seconds
		pSeq = App.TGSequence_Create()
		pSeq.AppendAction(App.TGScriptAction_Create(__name__, "ExitingProtoWarp", pShip, techType, move), 4.0)
		pSeq.Play()
		
	pObject.CallNextHandler(pEvent)
	return 0

# called after the warp-start move action
# Remove the attached parts and use the warp model now
def ProtoWarpStartMoveFinishAction(pAction, pShip, pInstance, iThisMovID, techP=oProtoWarp, move=oProtoWarp.MySubPositionPointer()):
	# Don't switch Models back when the ID does not match
	debug(__name__ + ", ProtoWarpStartMoveFinishAction")
	if not MoveFinishMatchIDUpdated(pShip, pInstance, iThisMovID):
		return 0
		
	techP.DetachParts(pShip, pInstance)
	techName = techP.MySystemPointer()
	sNewShipScript = pInstance.__dict__[techName]["Setup"][str(move) + "Model"]
	scaleFactor = 1.0
	if pInstance.__dict__[techName]["Setup"].has_key(str(move) + "SetScale") and pInstance.__dict__[techName]["Setup"][str(move) + "SetScale"] != 0.0:
		scaleFactor = pInstance.__dict__[techName]["Setup"][str(move) + "SetScale"]
	ReplaceModel(pShip, sNewShipScript)
	pShip.SetScale(scaleFactor)

	checkingReCloak(pShip)
	return 0


# called after the warp-exit move action
# Remove the attached parts and use the attack or normal model now
def ProtoWarpExitMoveFinishAction(pAction, pShip, pInstance, iThisMovID, techP=oProtoWarp, move=oProtoWarp.MySubPositionPointer()):
	# Don't switch Models back when the ID does not match
	debug(__name__ + ", ProtoWarpExitMoveFinishAction")
	if not MoveFinishMatchIDUpdated(pShip, pInstance, iThisMovID):
		if move != "Warp":
			RestoreWarpOverriden(pShip, pInstance)
		return 0
		
	techP.DetachParts(pShip, pInstance)
	techName = techP.MySystemPointer()
	if pInstance.__dict__[techName]["Setup"].has_key("AttackModel") and pShip.GetAlertLevel() == 2:
		sNewShipScript = pInstance.__dict__[techName]["Setup"]["AttackModel"]
		if pInstance.__dict__[techName]["Setup"].has_key("AttackSetScale") and pInstance.__dict__[techName]["Setup"]["AttackSetScale"] != 0.0:
			scaleFactor = pInstance.__dict__[techName]["Setup"]["AttackSetScale"]
	else:
		sNewShipScript = pInstance.__dict__[techName]["Setup"]["NormalModel"]
		if pInstance.__dict__[techName]["Setup"].has_key("NormalSetScale") and pInstance.__dict__[techName]["Setup"]["NormalSetScale"] != 0.0:
			scaleFactor = pInstance.__dict__[techName]["Setup"]["NormalSetScale"]

	ReplaceModel(pShip, sNewShipScript)
	pShip.SetScale(scaleFactor)
	checkingReCloak(pShip)

	if move != "Warp":
		RestoreWarpOverriden(pShip, pInstance)

	return 0

def RestoreWarpOverriden(pShip, pInstance):
	if not pShip:
		return 0

	pShipID = pShip.GetObjID()
	if not pShipID:
		return 0

	pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
	if not pShip:
		return 0
	
	if not pInstance:
		pInstance = findShipInstance(pShip)

	if not pInstance:
		pObject.CallNextHandler(pEvent)
		return 0
	pInstanceDict = pInstance.__dict__
	if pInstanceDict and pInstanceDict.has_key("Warp Overriden"):
		if pInstanceDict["Warp Overriden"] > 0:
			pInstanceDict["Warp Overriden"] = 0
	return 0

# called after a move, sets the current Rotation/Translation values to the final ones
def UpdateStateProto(pAction, pShip, item, lStoppingRotation, lStoppingTranslation):
        debug(__name__ + ", UpdateStateProto")
        item[1]["currentRotation"] = lStoppingRotation
        item[1]["currentPosition"] = lStoppingTranslation
        item[1]["curMovID"] = 0
        return 0

def UpdateHardpointPositionsE(pAction, pShip, dHardpoints, iThisMovID):
        debug(__name__ + ", UpdateHardpointPositionsE")

	pInstance = findShipInstance(pShip)
	if not pInstance or not MoveFinishMatchIDUpdated(pShip, pInstance, iThisMovID):
		return 0

	for sHP in dHardpoints.keys():
		UpdateHardpointPositionsTo(pShip, sHP, dHardpoints[sHP])
	return 0


# Set the parts to the correct alert state
def PartsForWeaponProtoState(pShip, techP):	
	debug(__name__ + ", PartsForWeaponProtoState")
	
	if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
		return 0
	
	pInstance = findShipInstance(pShip)
	iType = pShip.GetAlertLevel()
	iLongestTime = 0.0
	dHardpoints = {}
	
	# check if ship still exits
	pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
	if not pShip:
		return 0
	
	# try to get the last alert level
	for item in pInstance.OptionsList:
		if item[0] == "Setup":
			dGenShipDict = item[1]
			break
	
	# check if the alert state has really chanced since the last time
	if dGenShipDict["AlertLevel"] == iType:
		return 0
	# update alert state
	dGenShipDict["AlertLevel"] = iType
	IncCurrentMoveIDUpdated(pShip, pInstance)
	
	# start with replacing the Models
	PrepareShipForProtoMove(pShip, pInstance, techP)
	
	# iterate over every submodel
	for item in pInstance.OptionsList:
		if item[0] == "Setup":
			# attack or cruise modus?
			dHardpoints = {}
			if iType == 2 and item[1].has_key("AttackHardpoints"):
				dHardpoints = item[1]["AttackHardpoints"]
			elif iType != 2 and item[1].has_key("Hardpoints"):
				dHardpoints = item[1]["Hardpoints"]
			
			# setup is not a submodel
			continue
	
		# set the id for this move
		iThisMovID = item[1]["curMovID"] + 1
		item[1]["curMovID"] = iThisMovID
	
		fDuration = 200.0
		if item[1].has_key("AttackDuration"):
			fDuration = item[1]["AttackDuration"]
		    
		# Rotation
		lStartingRotation = item[1]["currentRotation"]
		lStoppingRotation = lStartingRotation
		if item[1].has_key("AttackRotation") and iType == 2:
			lStoppingRotation = item[1]["AttackRotation"]
		else:
			lStoppingRotation = item[1]["Rotation"]
		
		# Translation
		lStartingTranslation = item[1]["currentPosition"]
		lStoppingTranslation = lStartingTranslation
		if item[1].has_key("AttackPosition") and iType == 2:
			lStoppingTranslation = item[1]["AttackPosition"]
		else:
			lStoppingTranslation = item[1]["Position"]
	
		iTime = 0.0
		iTimeNeededTotal = 0.0
		oMovingEventUpdated = MovingEventUpdated(pShip, item, fDuration, lStartingRotation, lStoppingRotation, lStartingTranslation, lStoppingTranslation, dHardpoints)
		#if not hasattr(oMovingEventUpdated, "wentWrong") or oMovingEventUpdated.wentWrong == 2:
		#	# Something went wrong, better do not add a sequence for this
		#	continue

		pSeq = App.TGSequence_Create()
		
		# do the move
		while(iTime < fDuration):
			if iTime == 0.0:
				iWait = 0.1 # we wait for the first run
			else:
				iWait = 0.01 # normal step
			pSeq.AppendAction(App.TGScriptAction_Create(__name__, "MovingActionUpdated", oMovingEventUpdated), iWait)
			iTimeNeededTotal = iTimeNeededTotal + iWait
			iTime = iTime + 1
		pSeq.AppendAction(App.TGScriptAction_Create(__name__, "UpdateStateProto", pShip, item, lStoppingRotation, lStoppingTranslation))
		pSeq.Play()
		
		# iLongestTime is for the part that needs the longest time...
		if iTimeNeededTotal > iLongestTime:
			iLongestTime = iTimeNeededTotal
		
	# finally detach
	thisMoveCurrentID = GetCurrentMoveIDUpdated(pShip, pInstance)

	pSeq = App.TGSequence_Create()
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "UpdateHardpointPositionsE", pShip, dHardpoints, thisMoveCurrentID), iLongestTime)
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "AlertMoveFinishProtoAction", pShip, pInstance, thisMoveCurrentID, techP), 2.0)
	pSeq.Play()


# Set the parts for Warp state
def StartingWarpE(pObject, pEvent, techP = oProtoWarp, move="Warp"):
	debug(__name__ + ", StartingWarpE")
	# Slight delay, as it is likely the special FTL methods have not yet managed to alter things to prevent entering warp
	pSeq = App.TGSequence_Create()
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "StartingWarpCommonNoDelay", pObject, pEvent, techP, move), 0.3)
	pSeq.Play()
	return 0

def StartingWarpCommonNoDelay(pAction, pObject, pEvent, techP, move):
	StartingWarpCommon(pObject, pEvent, techP, move)
	return 0

# Set the parts for ProtoWarp state 
def StartingProtoWarp(pObject, pEvent, techP, move):
	debug(__name__ + ", StartingProtoWarp")
	StartingWarpCommon(pObject, pEvent, techP, move)
	return 0

def StartingWarpCommon(pObject, pEvent, techP, subPosition="Warp"):
	debug(__name__ + ", StartingWarpCommon")
	if not pObject or not pEvent:
		return 0

	pShip = App.ShipClass_Cast(pObject)
	if not pShip:
		return 0

	pShipID = pShip.GetObjID()
	if not pShipID:
		return 0

	pShip = App.ShipClass_GetObjectByID(None, pShipID)
	if not pShip:
		return 0

	if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
		#pObject.CallNextHandler(pEvent)
		return 0

	pInstance = findShipInstance(pShip)
	if not pInstance:
		#pObject.CallNextHandler(pEvent)
		return 0

	pInstanceDict = pInstance.__dict__
	if pInstanceDict and pInstanceDict.has_key("Warp Overriden"):
		if subPosition == "Warp":
			if pInstanceDict["Warp Overriden"] > 0:
				#pObject.CallNextHandler(pEvent)
				return 0	
		else: # Any other FTL method, we have priority!!!
			if pInstanceDict["Warp Overriden"] <= 0:
				pInstanceDict["Warp Overriden"] = 1	

	iLongestTime = 0.0
	IncCurrentMoveIDUpdated(pShip, pInstance)
	dHardpoints = {}

	# first replace the Models
	PrepareShipForProtoMove(pShip, pInstance, techP)
	subPositionHardpoints = str(subPosition) + "Hardpoints"
	subPositionDuration = str(subPosition) + "Duration"
	subPositionRotation = str(subPosition) + "Rotation"
	subPositionPosition = str(subPosition) + "Position"
	for item in pInstance.OptionsList:
		# setup is not a submodel
		if item[0] == "Setup":
			if item[1].has_key(subPositionHardpoints):
				dHardpoints = item[1][subPositionHardpoints]
			continue
	
		# set the id for this move
		iThisMovID = item[1]["curMovID"] + 1
		item[1]["curMovID"] = iThisMovID
	
		fDuration = 200.0
		
		if item[1].has_key(subPositionDuration):
			fDuration = item[1][subPositionDuration]
		    
		# Rotation
		lStartingRotation = item[1]["currentRotation"]
		lStoppingRotation = lStartingRotation
		if item[1].has_key(subPositionRotation):
			lStoppingRotation = item[1][subPositionRotation]
		
		# Translation
		lStartingTranslation = item[1]["currentPosition"]
		lStoppingTranslation = lStartingTranslation
		if item[1].has_key(subPositionPosition):
			lStoppingTranslation = item[1][subPositionPosition]
	
		iTime = 0.0
		iTimeNeededTotal = 0.0
		oMovingEventUpdated = MovingEventUpdated(pShip, item, fDuration, lStartingRotation, lStoppingRotation, lStartingTranslation, lStoppingTranslation, {})
		if not hasattr(oMovingEventUpdated, "wentWrong") or oMovingEventUpdated.wentWrong == 2:
			# Something went wrong, better do not add a sequence for this
			continue
		pSeq = App.TGSequence_Create()
		
		# do the move
		while(iTime < fDuration):
			if iTime == 0.0:
				iWait = 0.1 # we wait for the first run
			else:
				iWait = 0.01 # normal step
			pSeq.AppendAction(App.TGScriptAction_Create(__name__, "MovingActionUpdated", oMovingEventUpdated), iWait)
			iTimeNeededTotal = iTimeNeededTotal + iWait
			iTime = iTime + 1
		pSeq.AppendAction(App.TGScriptAction_Create(__name__, "UpdateStateProto", pShip, item, lStoppingRotation, lStoppingTranslation))
		pSeq.Play()
		
		# iLongestTime is for the part that needs the longest time...
		if iTimeNeededTotal > iLongestTime:
			iLongestTime = iTimeNeededTotal
		
	# finally detach
	thisMoveCurrentID = GetCurrentMoveIDUpdated(pShip, pInstance)

	pSeq = App.TGSequence_Create()
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "UpdateHardpointPositionsE", pShip, dHardpoints, thisMoveCurrentID), iLongestTime)
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "ProtoWarpStartMoveFinishAction", pShip, pInstance, thisMoveCurrentID, techP, subPosition), 2.0)
	pSeq.Play()

	return 0

def ExitingProtoWarp(pAction, pShip, techP, subPosition):
	debug(__name__ + ", ExitingProtoWarp")
	
	if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
		debug(__name__ + ", ExitingProtoWarp Return not host")
		return 0
	
	pInstance = findShipInstance(pShip)
	iLongestTime = 0.0
	IncCurrentMoveIDUpdated(pShip, pInstance)
	dHardpoints = {}
	
	# first replace the Models
	PrepareShipForProtoMove(pShip, pInstance, techP)
	
	for item in pInstance.OptionsList:
		# setup is not a submodel
		if item[0] == "Setup":
			dHardpoints = {}
			if item[1].has_key(str(subPosition) + "Hardpoints"):
				dHardpoints = item[1][str(subPosition) + "Hardpoints"]
			continue
	
		# set the id for this move
		iThisMovID = item[1]["curMovID"] + 1
		item[1]["curMovID"] = iThisMovID
	
		fDuration = 200.0
		if item[1].has_key(str(subPosition) + "Duration"):
			fDuration = item[1][str(subPosition) + "Duration"]
		    
		# Rotation
		lStartingRotation = item[1]["currentRotation"]
		lStoppingRotation = lStartingRotation
		if item[1].has_key("AttackRotation") and pShip.GetAlertLevel() == 2:
				lStoppingRotation = item[1]["AttackRotation"]
		else:
			lStoppingRotation = item[1]["Rotation"]
		
		# Translation
		lStartingTranslation = item[1]["currentPosition"]
		lStoppingTranslation = lStartingTranslation
		if item[1].has_key("AttackPosition") and pShip.GetAlertLevel() == 2:
				lStoppingTranslation = item[1]["AttackPosition"]
		else:
			lStoppingTranslation = item[1]["Position"]
	
		iTime = 0.0
		iTimeNeededTotal = 0.0
		oMovingEventUpdated = MovingEventUpdated(pShip, item, fDuration, lStartingRotation, lStoppingRotation, lStartingTranslation, lStoppingTranslation, dHardpoints)
		if not hasattr(oMovingEventUpdated, "wentWrong") or oMovingEventUpdated.wentWrong == 2:
			# Something went wrong, better do not add a sequence for this
			continue
		pSeq = App.TGSequence_Create()
		
		# do the move
		while(iTime < fDuration):
			if iTime == 0.0:
				iWait = 0.1 # we wait for the first run
			else:
				iWait = 0.01 # normal step
			pSeq.AppendAction(App.TGScriptAction_Create(__name__, "MovingActionUpdated", oMovingEventUpdated), iWait)
			iTimeNeededTotal = iTimeNeededTotal + iWait
			iTime = iTime + 1
		pSeq.AppendAction(App.TGScriptAction_Create(__name__, "UpdateStateProto", pShip, item, lStoppingRotation, lStoppingTranslation))
		pSeq.Play()
		
		# iLongestTime is for the part that needs the longest time...
		if iTimeNeededTotal > iLongestTime:
			iLongestTime = iTimeNeededTotal
		
	# finally detach
	thisMoveCurrentID = GetCurrentMoveIDUpdated(pShip, pInstance)
	pSeq = App.TGSequence_Create()
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "UpdateHardpointPositionsE", pShip, dHardpoints, thisMoveCurrentID), iLongestTime)
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "ProtoWarpExitMoveFinishAction", pShip, pInstance, thisMoveCurrentID, techP, subPosition), 2.0)
	pSeq.Play()
	
	return 0
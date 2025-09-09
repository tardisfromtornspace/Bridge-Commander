# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL, FOR THOSE SECTIONS THAT DO NOT FALL UNDER ANY OTHER LICENSE (See explanation below)
# AlternateSubModelFTL.py
# 9th September 2025, by Alex SL Gato (CharaToLoki)
#         Based on Defiant's SubModels script logic and BorgAdaptation.py by Alex SL Gato, which were based on the Foundation import function by Dasher
#         Also based slightly on ATPFunctions (by Apollo) and DS9FXPulsarManager style (by USS Sovereign).
#         Also some sections based and copied from the Slipstream module by Mario aka USS Sovereign, modified by Alex SL Gato with Mario's permission to adapt part of his code to this script ONLY as long as it is meant for KM, and that he can and will take action otherwise (see Documentation/USSSovereignStanceAboutModifyingorRepackagingSlipstream.PNG).
# IMPORTANT NOTE:
#  - All sections based on USS Sovereign's Slipstream module fall under the All Rights Reserved section, by USS Sovereign. Those sections are left clear with two text banners, from "BEGINNING OF USS SOVEREIGN'S LIMITED PERMISSION AREA" to "END OF USS SOVEREIGN'S LIMITED PERMISSION AREA". Do not modify or repackage those sections of the mod without extreme permission from the authors:
#  ---- USS Sovereign condition: that this mod is intended to be released for KM and not for REP, RE nor REM-related mods (see Documentation/USSSovereignStanceAboutModifyingorRepackagingSlipstream.PNG).
#  ---- Alex SL Gato condition: does not mind as long as USS Sovereign and he are being credited and both Mario and himself's conditions are covered (which means that if Mario's conditions are not met, neither are his).
#################################################################################################################
# A modification of a modification, last modification by Alex SL Gato (CharaToLoki)
##################################################################################################################################################################################################################################
##################################################################################################################################################################################################################################
##########	MANUAL
##################################################################################################################################################################################################################################
##################################################################################################################################################################################################################################
# === INTRODUCTION ===
# The purpose of this plugin is to provide extended globalized actions for alternate TravellingMethods, providing them with the option to modify the model, like SubModels, but a bit less "broken"; as well as supporting SubModels Warp and Attack support, and a limited intra-system-intercept for each of those methods.
# NOTE: This will not affect pre-existing TravellingMethods, a ship could have those and not use this tech at all.
# INFO: While originally this script had two classes "ProtoWarp" and "MovingEventUpdated" which inherited from Defiant's SubModels "SubModel" and "MovingEvent" classes, and also used certain functions from that script, current version doesn't, so no issues should arise from combining both on the same ship. However, due to this script's mechanisms, it is suggested to just use AlternateSubmodelFTL instead. Please note that due to one of this script's roles being to also cover SubModel's functionality without modders needing to also change the scripts/Custom/Ships fine-tuned positions and rotations, some functionalities present similarities with SubModel ones.
# ATTENTION: The script is dependant on scripts/Custom/TravellingMethods and on GalaxyCharts to verify sub-technology and FTL availability. With those options turned off, the usefulness of this script is reduced to a cleaner customizable SubModels.
# ATTENTION: The script is also dependant on ftb.Tech.ATPFunctions
# === HOW-TO-USE a pre-existing FTL TravellingMethods that supports this tech ===
# Below there's a sample setup. Those familiarized with SubModels script will notice the how-to is basically identical, but with a twist, presenting extra elements related with more rotations and the TravellingMethods files that support this file.
#
# On this case, we have a TravellingMethods file called ProtoWarp which is called inside as "Proto-Warp" (explanaton on how to add these are mentioned after the Sample Setup).
#
# For clarity, we will use the symbols:
# - "(*)"                - to determine something which is arbitrary to the TravellingMethods FTL sub-tech.
# - "(-)"                - to something that is optional but necessary to perform the function they indicate, or not globally necessary but still needed for a set of functions.
# - "(0)"                - to something that is optional but does nothing else that adds a nice touch, since no other functions would be affected if they were skipped, for the most part.
# - "(#)"                - something that is always needed, or may always be needed if you need any figment of functionality outside of calling a literal empty version of the function.
# - "<insert_name_here>" - basically a generalization example for any other TravellingMethod. On this case in particular, <insert_name_here> = "Proto-Warp". Unless told otherwise, this generalization implies you can have as many of that field as you want, as long as <insert_name_here> is different for each one, allowing multiple TravellingMethods subModels support.
# - "c.s."               - "case-sensitive". That is, it will notice it is different if you type like this, LIKE THIS, LiKe ThIs and so on.
# - "<s-s>"              - "It uses the name of the ship File located at scripts/ships". Having a dummy ship with the smallest hardpoint possible should be the best. Also if the model is not a 300k vert creation. Please, for the sake of slow computers, try to follow this recommendation.
# - "<k:v>"              - key - value format. On python, key: value. Unless key or value are variables (or value is not an integer), you need to ensure they are between "" to indicate they are strings. Also it's c.s. "key like this" : "value like that", "unless the value for the key is a number like": 10
# - "~r.c~"              - rapid-change between status or situations, most often before all the pieces have managed to move/rotate fully and the transformation was ongoing f.ex. a ship with normal position and attack position constantly switching from red alert to green alert every second.
#
# (#) On the "Setup" section, people will notice:
# -- (*) A ""Proto-Warp": {"Nacelles": ["Proto Warp Nacelle"], "Core": ["Proto-Core"], }," line, This can vary wildly between TravellingMethods, some may not even require a similar line, so check each one's readme (if they have it) to get more information on its SubTech. However for those modders that use this tech to validate if the ship is equipped or not, please do so somewhere inside the "Setup" field. On this case in particular, this line is simply arbitrarily defined here so the ProtoWarp TravellingMethods script, which uses this tech to verify the ship is equipped with it, can determine the ship has or does not have this tech. This kind of line is what can also be used for indentifying if a ship has Intra-System Intercept.
# -- (#) "Body" is a key whose value stores the model used during transformations. <s-s> <k:v> c.s.
# -- (#) "NormalModel" is a key whose value stores the model used when no red alert nor special warp or FTL method with this tech support happen. <s-s> <k:v> c.s.
# -- (-) "WarpModel" is a key whose value stores the model used when the ship uses warp, and no other FTL SubModel Warp Events are called. <s-s> <k:v> c.s.
# --------- Please note that while being (-), it pretty much is (#) if you added certain attack-related fields which are outside of "Setup".
# -- (-) "AttackModel" is a key whose value stores the model used when the ship is at red alert. <s-s> <k:v> c.s.
# --------- Please note that while being (-), it pretty much is (#) if you added certain warp-related fields which are outside of "Setup".
# -- (-) "<insert_name_here>Model" is a key whose value stores the model used when the ship uses <insert_name_here>, and will supersede the warp-related options. <k:v> <s-s> c.s.
# --------- Please note that while being (-), it pretty much is (#) if you added certain <insert_name_here>-related fields which are outside of "Setup".
# -- (0) "BodySetScale": indicates the model size multiplier during a transformation. Affects ALL attached part scales as well. Do not include to have default 1.0 (regular scale). <k:v>
# -- (0) "NormalSetScale": indicates the model size multiplier during normal conditions. Affects ALL attached part scales as well. Do not include to have default 1.0 (regular scale). <k:v>
# -- (0) "AttackSetScale": indicates the model size multiplier during red alert. Affects ALL attached part scales as well. Do not include to have default 1.0 (regular scale). <k:v>
# -- (0) "<insert_name_here>SetScale": indicates the model size multiplier during <insert_name_here> (f.ex. during Warp, during Proto-Warp). Affects ALL attached part scales as well. Do not include to have default 1.0 (regular scale). <k:v>
# -- (0) "Hardpoints": a dictionary which stores inside all subsystem property names in <k:v> format which would move after a transformation, regarding normal positions (including yellow alert).
# --------- On this case, each dictionary entry would be "Subsystem name" : [x, y, z], or alternatively "Subsystem name" : [x, y, z, S], with "S" being a dictionary of structure {<k:v>} that provides extra features to apply during or after a subModel transformation:
# ------------- (0) "Disabled Percentage": a dictionary entry which stores the disabled percentage for a subsystem when ending a transfomation for the requested "<insert_name_here>Hardpoints" dictionary (for example, after switching from red alert to normal alert, it would follow the disabled percentages of "Hardpoints"). On this case this value is skipped if the dictionary entry for a subsystem lacks this parameter, allowing for a limited selective system disabling/enabling according only to alert levels, the FTL being used, or both. <s-s> c.s.
# -- (0) "AttackHardpoints": a dictionary which stores inside all subsystem property names in <k:v> format which would move after a transformation, regarding red alert positions.
# --------- On this case, each dictionary entry would be "Subsystem name" : [x, y, z], or [x, y, z, S] (see above)
# -- (0) "WarpHardpoints": a dictionary which stores inside all subsystem property names in <k:v> format which would move after a transformation, regarding normal warp positions.
# --------- On this case, each dictionary entry would be "Subsystem name" : [x, y, z], or [x, y, z, S] (see above)
# -- (0) "<insert_name_here>Hardpoints": a dictionary which stores inside all subsystem property names in <k:v> format which would move after a transformation, regarding <insert_name_here> positions.
# --------- On this case, each dictionary entry would be "Subsystem name" : [x, y, z], or [x, y, z, S] (see above)
# -- (0) "<insert_name_here>IgnoreCall": a dictionary entry which stores inside a value that determines if a ship complies (0) or ignores (1 or greater) certain event calls for when a ship uses <insert_name_here>.
# --------- The objective of this parameter is to help cover strange cases, where an FTL TravellingMethod with AlternateSubModels support not constrained by the template (and excluding regular Warp) is used by a vessel which can perform such travelling method, but you don't want that vessel to even swap between models nor attach/detach non-main-body-pieces.
# --------- If <insert_name_here> = "Attack" or "<insert_name_here>" = "", it will apply for Attack and Normal states when switching between alerts, albeit that is not the objective of this parameter and for that case it would be better to just not add attack rotation nor attack positions to non-main body pieces.
# (-) After that, there's a section for each non-main-body piece, in <k:v> format, with "k" being the inner name the piece will receive, and v a list of structure: ["A", D]
# --------- (#) "A" is the first value of the list, it is the ship model used for that particular piece during any transformation. <s-s> c.s.
# --------- (-) "D" is a dictionary containing positions, rotations and miscelllaneous information for each situation. c.s.
# ---------------- (0) "<insert_name_here>Position": a dictionary entry which stores inside the movement in <k:v> format which the piece would move to during an <insert_name_here> transformation. On this example, "<insert_name_here>" could be nothing (thus "Position", for default), "Attack" (for red alert), "Warp" (for regular warp) or "Proto-Warp" (for Proto-Warp).
# ----------------------- Movement value is on [x, y, z].
# ---------------- (0) "<insert_name_here>Rotation": a dictionary entry which stores inside the rotation in <k:v> format which the piece would move to during an <insert_name_here> transformation. On this example, "<insert_name_here>" could be nothing (thus "Rotation", for default), "Attack" (for red alert), "Warp" (for regular warp) or "Proto-Warp" (for Proto-Warp).
# ----------------------- Rotation value is on [x, y, z] axis of rotation.
# ---------------- (0) "<insert_name_here>Duration": a dictionary entry which stores inside the time, in <k:v> format and in centiseconds, that a <insert_name_here> transformation lasts. On this example, "<insert_name_here>" should not be empty, so "Attack" for red alert, "Warp" for regular warp or "Proto-Warp" for Proto-Warp.
# ---------------- (0) "<insert_name_here>DelayEntry": a dictionary entry which stores inside the time, in <k:v> format and in seconds, that a <insert_name_here> beginning transformation (f.ex. from normal to attack) waits before actually moving or rotating. Default and minimum is 0, which is added to the default 0.1 normal wait. On this example, "<insert_name_here>" should not be empty, so "Attack" for red alert, "Warp" for regular warp or "Proto-Warp" for Proto-Warp.
# ---------------- (0) "<insert_name_here>DelayExit": a dictionary entry which stores inside the time, in <k:v> format and in seconds, that a <insert_name_here> exit transformation (f.ex. from attack to normal) waits before actually moving or rotating. Default and minimum value is 0, which is added to the default 0.1 normal wait. On this example, "<insert_name_here>" should not be empty, so "Attack" for red alert, "Warp" for regular warp or "Proto-Warp" for Proto-Warp.
# ---------------- (0) "SetScale": indicates the model size of a subpart. Do not include to have same behaviour as SubModels (regular scale but if the part has a too-extreme rotation (like, at least 90 degrees) it will suffer an asintotic process where it suddenly becomes small and then extremely big and inverted). <k:v>
# ---------------- (0) "Experimental": a dictionary entry which establishes if the ship uses experimental rotation or not. "Experimental": 0 or entry not added implies it uses the legacy submodels style of rotation.
# ------------------------ Legacy rotations are better for backwards-compatibility and have little to none drifting issues, but only work for a particular quadrant of rotation ( -90, 90 ) degrees and are best for ( -45 degrees, 45 degrees) amplitude. They share most of the issues SubModels rotations have (including that beyond the optimal movement range the subparts will suffer an unwanted size change, more prominent the more we approach to the quadrant limit), except that they are more optimized and thus will not suffer accidental drifting nor will cause memory issues.
# ------------------------ Experimental rotations are best suited if the ship requires to rotate beyond the amplitude legacy provides, but require to use a tiny bit more of memory and suffer from an extremely slight ~r.c~ rotation drift due to float number innacuracies. Experimental rotation degrees are aproximately 1:1 with legacy rotations of the same quadrant, but some slight differences may arise due to slight implementation differences and the legacy quadrant limit. Please notice that because this script was made with backwards compatibility with SubModels, some of the quirks related with SubModels regarding time needed to rotate and angles covered still affect legacy and experimental angles.
# ---------------- (0) "ResetToPrevious": a dictionary entry whose only purpose is to indicate, when value 1, that a nacelle's position should always return to the pre-FTL position after performing the FTL entry transformation, or the supposed initial FTL positions after exiting FTL - only recommended to be used for asymmetric movement methods, where only the startup or end movement sequences happen (f.ex. Spore Displacement Drive, where the only movement done is at the beginning).
# ---------------- (0) "Ignore<insert_name_here>Entry": if this value is set to 1, that piece will not rotate nor move when the FTL Entry event for <insert_name_here> happens. Useful for when a ship has some pieces that require to do only a part of the action while others need both entry and exit.
# ---------------- (0) "Ignore<insert_name_here>Exit": if this value is set to 1, that piece will not rotate nor move when the FTL Exit event for <insert_name_here> happens. Useful for when a ship has some pieces that require to do only a part of the action while others need both entry and exit (f.ex. a 32nd Century Crossfield may need to have the main body parts ignore the exit revert sequence, but still needs to have two of its nacelles re-attach and float when engaging and disengaging Spore Drive - this could be alternatively done in other ways too but this option brings more flexibility).
# 
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
				"Proto Warp Nacelle":  [0.000000, 0.000000, 0.075000, {"Disabled Percentage" : 1.1}],
			},

			"AttackHardpoints":       {
				"Proto Warp Nacelle":  [0.000000, -0.250000, 2.075000, {"Disabled Percentage" : 0.5}],
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
			"ResetToPrevious": 0,
			"IgnoreProto-WarpEntry": 0,
			"IgnoreProto-WarpExit": 0,
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
			"Proto-WarpDelayEntry":       0.15,
			},
		],
        
		"Starboard Wing":     ["VasKholhr_Starboardwing", {
			"Experimental": 0,
			"SetScale": 1.0,
			"ResetToPrevious": 0,
			"IgnoreProto-WarpEntry": 0,
			"IgnoreProto-WarpExit": 0,
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
			"Proto-WarpDelayExit":       0.15,
			},
		],
	},
}
"""
#
# === HOW-TO-USE a pre-existing FTL TravellingMethods Intra-System Intercept ===
#
# When a ship is equipped with at least 1 type of alternate FTL that has the required InSystemIntercept() (ISI) function, if the player plays as that ship, a new entry called "Alt. intrasystem Intercept" (or whatever name the "MainHelmMenuName" variable has stored) will appear on top of the "Helm" ("Kiska" on stock bridges) Menu. When the player ship is no longer equipped with the drive, this sub-menu will disappear.
# Structure of the Menu:
# o "Alt. intrasystem Intercept"
# oooo "Intercept Methods": this entry is actually a bullet-list subMenu, indicating which FTL Methods that support ISI are equipped on this ship. Upon clicking on one of its subMenu options, it will attempt to move the ship to the desired intercept location, which is the ship, planet or navpoint the player has selected at the moment. This may not always succeed, as each button is linked to a set of filters.
# ooooooo "Method1": actually it is the name the InSystemIntercept() the TravellingMethod provides.
# ooooooo "Method2": more than 1 method to intercept can be selected.
# ooooooo "MethodN": please notice that due to implementation, two or more buttons could have the same name, but this is not recommended.
# oooo "Initiate Navpoint Mode"/"Stop Navpoint Mode": a common toggleable button, it will spawn a "navpoint" ship for interception when the player does not want to use other ships, planets or nav-points as objectives to intercept. Click again to remove the navpoint.
# The filters that each Intercept Method button has are the following:
# - No-target filter: if the intercept location is not a ship or a planet, the respective button name will temporarily change name to "NO TARGET".
# - Safety distance feature: if the intercept target is too close to the ship, the respective button name will temporarily change name to "TOO CLOSE".
# - Local FTL restrictions: before engaging, this plugin also checks the CanTravel equivalent function provided by InSystemIntercept() function. If it does not meet the requirements, it will not engage and the button will temporarily change to "CANNOT DO". Additionally, the local function may drop certain subtitles and phrases to hint at what is preventing the ship from using ISI at the moment.
# - Local FTL 'GoodAim' functions: once we know we can engage, the plugin will look for a good position to perform the intercept, according to the function provided by InSystemIntercept() function. Once we have reached this stage the ISI will happen, but will be delayed the time needed to aim for a good position.
#
# === HOW TO CREATE a compatible FTL TravellingMethods that supports this tech ===
#
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
#
# === HOW TO CREATE a compatible FTL TravellingMethods that supports ISI ===
# ISI (Intra-System-Intercept) is a feature that extends the point above one step further. As such, you need to follow the steps above, but adding the following (alongside an explanation on the user manual about how that TravellingMethod supports ISI and the extra auxiliar functions that are not needed for GalaxyCharts):
"""

####### Inside the ALTERNATESUBMODELFTL METHODS section: #######
def InSystemIntercept():
	propulsionType = sName # The name for its subMenu option - could be the same as the one on TravellingMethod, could be different... or it could even clash with another name - albeit that is not recommended.
	eEntryEvent = GetStartTravelEventsI # The events called during the beginning of the ISI sequence. Events like App.ET_START_WARP_NOTIFY are ignored.
	eExitEvent = GetExitedTravelEventsI # The events called after the diplacement of the ISI sequence. Events like App.ET_EXITED_SET are ignored.
	eSequenceFunction = SetupSequenceISI # This should return three values, the before-displacement sequence, the time in-between, and the post-displacement sequence. The sequences are a modification of the normal sequences for changing systems.
	# Important NOTE: Since intra-system does not call pre-engage nor post-engage functions on its own (only the entry and exit events), if you have an actual pre-engage and post-engage function that is not just a mere "return", you may want to adjust your sequence to call them instead at the appropiate time.
	isEquipped = IsShipEquipped # Function for knowing if the ship is equipped with ISI for this TravellingMethod.
	eCanTravel = CanTravelShip # Function for knowing if the ship equipped with ISI for this TravellingMethod, can actually use it for ISI.
	awayNavPointDistance = awayNavPointDistanceCal # This is a custom multiplier value, used for checking when a ship is too close to a planet or ship. A lower value means that it will allow closer ISI, while a higher value will make that ISI inner proximity limit be further. Negative values are set to 0.
	engageDirection = GetEngageDirectionISI # The function used for knowing if the ship is aiming at a good position before engaging. If it returns none it means the ship is correctly aimed, else the function provided should give a better course. AlternateSubModelFTL would orient the ship to that direction.

	return propulsionType, eEntryEvent, eExitEvent, eSequenceFunction, isEquipped, eCanTravel, awayNavPointDistance, engageDirection

"""
# As you may have noticed, the function above calls to some functions/attributes not mentioned before. This is because these functions/attributes are indeed custom and could be unique to each TravellingMethod, with the only common feature that, unlike the equivalents for normalFTL travel, they must get rid of any call to "self" and accept, if necessary, a pShip. Example from these is below, done in another script for Spore Drive, where:
# - propulsionType = sName # sName being the sName = "Spore Drive" atribute.
# - eEntryEvent = GetStartTravelEventsI # With GetStartTravelEventsI being a modified function from GetStartTravelEvents, with both being modified below to use less space and make changes easier:
"""
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
"""
# - eExitEvent = GetExitedTravelEventsI # With GetExitedTravelEventsI being a modified function from GetExitedTravelEvents, with both being modified below to use less space and make changes easier:
"""
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
"""
# - eSequenceFunction = SetupSequenceISI # With SetupSequenceISI being a totally separate SetupSequence (extra additional functions from this custom one are not shown, with the exception of some useful handlers to support ISI dragging another ship with a tractor beam):
"""
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
	debug(__name__ + ", SetupTowing")
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

	SetupTowingI(pShip.GetObjID())

	pInstance = findShipInstance(pShip)
	_, _, _, _, _, _, _ , _ , myExitDirection, myTime, myDistance = SporeDriveBasicConfigInfo(pShip)

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

	extraSoundTime = 0.01


	if (pPlayer != None) and (pShip.GetObjID() == pPlayer.GetObjID()):
		fEntryDelayTime = fEntryDelayTime + 1.0
		extraSoundTime = 0.25
		
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

	# Create the warp flash.
	pFlashAction1 = App.TGScriptAction_Create("Actions.EffectScriptActions", "WarpFlash", pShip.GetObjID())
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

	# Check for towee
	if hasTractorReady == 1:
		pHideTowee = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pInstance.SporeDriveISITowee, 1)
		pExitWarpSeq.AddAction(pHideTowee, pHideShip)

	# Create the warp flash.
	pFlashAction2 = App.TGScriptAction_Create("Actions.EffectScriptActions", "WarpFlash", pShip.GetObjID())
	pExitWarpSeq.AddAction(pFlashAction2, pHideShip, 0.7)

	# Un-Hide the ship
	pUnHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShip.GetObjID(), 0)
	pExitWarpSeq.AddAction(pUnHideShip, pFlashAction2, 0.01)

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
	pExitWarpSeq.AddAction(pUnBoostAction, pWarpSoundAction2, 2.0)

	# IMPORTANT: These three actions below are an extra added for intra-system intercept since we need to ensure the cutscene really ends and control is returned to the player.
	# This could be handled on the main AlternateSubModelFTL script but I'm leaving it here to allow better customization

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
	# 2º: the time between engaging and exiting sequences
	# 3º: the exiting travel sequence   (plays once, when the ship exits travel)

	# Note that each one of them can be None, if you don't want to have that sequence in your travel method.

	return [pEngageWarpSeq, fTimeToFlash + 2.5, pExitWarpSeq]
"""
# - isEquipped = IsShipEquipped # With IsShipEquipped being the exact same auxiliar IsShipEquipped the TravellingMethod had and which did not require extra modifications.
# - eCanTravel = CanTravelShip # CanTravelShip being a modified CanTravel to support the lack of "self", with both being modified below to use less space and make changes easier:
"""
def CanTravel(self):
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

	pInstance, pInstancedict, specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, _ , _ , _ , _ , _ = SporeDriveBasicConfigInfo(pShip)

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

"""
# - awayNavPointDistance = awayNavPointDistanceCal # With awayNavPointDistanceCal being a simple function located immediately below InSystemIntercept that may accept a pShipID as a parameter and returns 1.0 multiplier:
"""
def awayNavPointDistanceCalc(pShipID=None):
	return 1.0
"""
# - engageDirection = GetEngageDirectionISI # With GetEngageDirectionISI being a modified GetEngageDirection, with both being modified below to use less space and make changes easier (with a hypothethical that we needed a modified course, something which Spore Drive actually does not, just returning None on 'GetEngageDirectionC'): 
"""
def GetEngageDirection(self): # NOTE: Requires GetEngageDirectionC
	debug(__name__ + ", GetEngageDirection")
	return GetEngageDirectionC(self, None)

# Aux. ISI function.
def GetEngageDirectionISI(pPlayerID): # NOTE: Requires GetEngageDirectionC
	debug(__name__ + ", GetEngageDirectionISI")
	return GetEngageDirectionC(None, pPlayerID)

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
"""
# 
##################################################################################################################################################################################################################################
##################################################################################################################################################################################################################################
##########	END OF MANUAL
##################################################################################################################################################################################################################################
##################################################################################################################################################################################################################################
#
#################################################################################################################
#
MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "0.87",
	    "License": "All Rights Reserved (USS Sovereign sections), LGPL (everywhere else)",
	    "Description": "Read the small title above for more info"
	    }
#
#################################################################################################################
#

import App
from bcdebug import debug
import Foundation
import FoundationTech
import loadspacehelper
import math
import MissionLib
import nt
import string
#from SubModels import *
from threading import Semaphore
import traceback

REMOVE_POINTER_FROM_SET = 190
NO_COLLISION_MESSAGE = 192
REPLACE_MODEL_MSG = 208
SET_TARGETABLE_MSG = 209

navDist = 1500 # Default distance for in-system intercept navpoints

# Because SubModels is ridiculously hard to make children without having to re-do all the functions, I've made this, so now you can just follow
eTypeDict = {}

# For in-system intercept
eInSystemIntercept = {}
eEquippedInSystemIntercept = {}

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

# Replaces the Model of pShip
def ReplaceModel(pShip, sNewShipScript):
	debug(__name__ + ", ReplaceModel")
	
	pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
	if not pShip:
		return
	
	ShipScript = __import__('ships.' + sNewShipScript)
	ShipScript.LoadModel()
	kStats = ShipScript.GetShipStats()
	pShip.SetupModel(kStats['Name'])
	if App.g_kUtopiaModule.IsMultiplayer():
		MPSentReplaceModelMessage(pShip, sNewShipScript)

def ReplaceModelBlackLightsFix(pShip):
	# Because hiding and unhiding the ship does not seem to do the job of fixing the weird lack of lights, but something like this dumb thing below does :/
	from ftb.Tech.ATPFunctions import *

	point = pShip.GetWorldLocation()
	pHitPoint = App.TGPoint3()
	pHitPoint.SetXYZ(point.x, point.y, point.z)

	pVec = pShip.GetVelocityTG()
	pVec.Scale(0.001)
	pHitPoint.Add(pVec)

	mod = "Tactical.Projectiles.AutomaticSystemRepairDummy" 
	try:
		pTempTorp = FireTorpFromPointWithVector(pHitPoint, pVec, mod, pShip.GetObjID(), pShip.GetObjID(), __import__(mod).GetLaunchSpeed())
		if pTempTorp:
			pTempTorp.SetHidden(1)
			pTempTorp.SetLifetime(0.0)
	except:
		print "You are missing 'Tactical.Projectiles.AutomaticSystemRepairDummy' torpedo on your install, without that a weird black-texture-until-firing-or-fired bug may happen"
		traceback.print_exc()

def DeleteObjectFromSet(pSet, sObjectName):
	if not MissionLib.GetShip(sObjectName, None, bAnySet = 1):
		return
	pSet.DeleteObjectFromSet(sObjectName)
	
	# send clients to remove this object
	if App.g_kUtopiaModule.IsMultiplayer():
		# Now send a message to everybody else that the score was updated.
		# allocate the message.
		pMessage = App.TGMessage_Create()
		pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet
			
		# Setup the stream.
		kStream = App.TGBufferStream()		# Allocate a local buffer stream.
		kStream.OpenBuffer(256)				# Open the buffer stream with a 256 byte buffer.
	
		# Write relevant data to the stream.
		# First write message type.
		kStream.WriteChar(chr(REMOVE_POINTER_FROM_SET))

		# Write the name of killed ship
		for i in range(len(sObjectName)):
			kStream.WriteChar(sObjectName[i])
		# set the last char:
		kStream.WriteChar('\0')

		# Okay, now set the data from the buffer stream to the message
		pMessage.SetDataFromStream(kStream)

		# Send the message to everybody but me.  Use the NoMe group, which
		# is set up by the multiplayer game.
		pNetwork = App.g_kUtopiaModule.GetNetwork()
		if not App.IsNull(pNetwork):
			if App.g_kUtopiaModule.IsHost():
				pNetwork.SendTGMessageToGroup("NoMe", pMessage)
			else:
				pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)

		# We're done.  Close the buffer.
		kStream.CloseBuffer()
	return 0


def MultiPlayerEnableCollisionWith(pObject1, pObject2, CollisionOnOff):
	# Setup the stream.
	# Allocate a local buffer stream.
	debug(__name__ + ", MultiPlayerEnableCollisionWith")
	kStream = App.TGBufferStream()
	# Open the buffer stream with a 256 byte buffer.
	kStream.OpenBuffer(256)
	# Write relevant data to the stream.
	# First write message type.
	kStream.WriteChar(chr(NO_COLLISION_MESSAGE))
	
	# send Message
	kStream.WriteInt(pObject1.GetObjID())
	kStream.WriteInt(pObject2.GetObjID())
	kStream.WriteInt(CollisionOnOff)

	pMessage = App.TGMessage_Create()
	# Yes, this is a guaranteed packet
	pMessage.SetGuaranteed(1)
	# Okay, now set the data from the buffer stream to the message
	pMessage.SetDataFromStream(kStream)
	# Send the message to everybody but me.  Use the NoMe group, which
	# is set up by the multiplayer game.
	# TODO: Send it to asking client only
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	if not App.IsNull(pNetwork):
		if App.g_kUtopiaModule.IsHost():
			pNetwork.SendTGMessageToGroup("NoMe", pMessage)
		else:
			pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
	# We're done.  Close the buffer.
	kStream.CloseBuffer()


def MPSentReplaceModelMessage(pShip, sNewShipScript):
	# Setup the stream.
	# Allocate a local buffer stream.
	debug(__name__ + ", MPSentReplaceModelMessage")
	kStream = App.TGBufferStream()
	# Open the buffer stream with a 256 byte buffer.
	kStream.OpenBuffer(256)
	# Write relevant data to the stream.
	# First write message type.
	kStream.WriteChar(chr(REPLACE_MODEL_MSG))

	try:
		from Multiplayer.Episode.Mission4.Mission4 import dReplaceModel
		dReplaceModel[pShip.GetObjID()] = sNewShipScript
	except ImportError:
		pass

	# send Message
	kStream.WriteInt(pShip.GetObjID())
	iLen = len(sNewShipScript)
	kStream.WriteShort(iLen)
	kStream.Write(sNewShipScript, iLen)

	pMessage = App.TGMessage_Create()
	# Yes, this is a guaranteed packet
	pMessage.SetGuaranteed(1)
	# Okay, now set the data from the buffer stream to the message
	pMessage.SetDataFromStream(kStream)
	# Send the message to everybody but me.  Use the NoMe group, which
	# is set up by the multiplayer game.
	# TODO: Send it to asking client only
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	if not App.IsNull(pNetwork):
		if App.g_kUtopiaModule.IsHost():
			pNetwork.SendTGMessageToGroup("NoMe", pMessage)
		else:
			pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
	# We're done.  Close the buffer.
	kStream.CloseBuffer()


def mp_send_settargetable(iShipID, iMode):
	# Setup the stream.
	# Allocate a local buffer stream.
	debug(__name__ + ", mp_send_settargetable")
	kStream = App.TGBufferStream()
	# Open the buffer stream with a 256 byte buffer.
	kStream.OpenBuffer(256)
	# Write relevant data to the stream.
	# First write message type.
	kStream.WriteChar(chr(SET_TARGETABLE_MSG))

	# send Message
	kStream.WriteInt(iShipID)
	kStream.WriteInt(iMode)

	pMessage = App.TGMessage_Create()
	# Yes, this is a guaranteed packet
	pMessage.SetGuaranteed(1)
	# Okay, now set the data from the buffer stream to the message
	pMessage.SetDataFromStream(kStream)
	# Send the message to everybody but me.  Use the NoMe group, which
	# is set up by the multiplayer game.
	# TODO: Send it to asking client only
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	if not App.IsNull(pNetwork):
		if App.g_kUtopiaModule.IsHost():
			pNetwork.SendTGMessageToGroup("NoMe", pMessage)
		else:
			pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
	# We're done.  Close the buffer.
	kStream.CloseBuffer()

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

					if hasattr(banana, "InSystemIntercept"):
						propulsionType, eEntryEvent, eExitEvent, eSequenceFunction, isEquipped, eCanTravel, awayNavPointDistance, engageDirection = banana.InSystemIntercept()
						if propulsionType and not eInSystemIntercept.has_key(myGoodPlugin):
							eInSystemIntercept[myGoodPlugin] = {}
							eInSystemIntercept[myGoodPlugin]["PropulsionType"] = propulsionType # Name used for the menu
							eInSystemIntercept[myGoodPlugin]["EntryEvent"] = eEntryEvent
							eInSystemIntercept[myGoodPlugin]["ExitEvent"] = eExitEvent
							eInSystemIntercept[myGoodPlugin]["Sequences"] = eSequenceFunction
							eInSystemIntercept[myGoodPlugin]["IsEquipped"] = isEquipped
							eInSystemIntercept[myGoodPlugin]["CanTravel"] = eCanTravel
							eInSystemIntercept[myGoodPlugin]["EngageDirectionF"] = engageDirection
							eInSystemIntercept[myGoodPlugin]["AwayNavPointDistance"] = awayNavPointDistance

			except:
				print "someone attempted to add more than they should to the AlternateSubModelFTL script"
				traceback.print_exc()

LoadExtraLimitedPlugins()

#### BEGINNING OF USS SOVEREIGN'S LIMITED PERMISSION AREA ####
# Button properties

#bButton = None
bMenu = None
bNavPointButton = None
bInterceptMenu = None
pButtonCondition = 1

pPane = None
pPaneID = None
pWasCloaked = 0

MainHelmMenuName = "Alt. intrasystem Intercept"
HelmButtonIniNavP = "Initiate Navpoint Mode"
HelmSubMName = "Intercept Methods"

fDirectionTimeThreshold = 0.2

NormalColor = App.TGColorA() 
NormalColor.SetRGBA(0.8, 0.6, 0.8, 1.0)
HighlightedColor = App.TGColorA() 
HighlightedColor.SetRGBA(0.92, 0.76, 0.92, 1.0)
NormalColor2 = App.TGColorA() 
NormalColor2.SetRGBA(0.5, 0.5, 1.0, 1.0)
HighlightedColor2 = App.TGColorA() 
HighlightedColor2.SetRGBA(0.61, 0.61, 1.0, 1.0)
DisabledColor = App.TGColorA() 
DisabledColor.SetRGBA(0.25, 0.25, 0.25, 1.0)

NavPName = "Alternate FTL intrasystem Nav"

# From ATP_GUIUtils -- From The Notes Of USS SOVEREIGN: Very useful.
def GetBridgeMenu(menuName):
	pTactCtrlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	if(pDatabase is None):
		return
	App.g_kLocalizationManager.Unload(pDatabase)
	return pTactCtrlWindow.FindMenu(pDatabase.GetString(menuName))

# From one of the released DS9FXMenuLib, or at least, the one on slipstream, since for some reason the one there had different functions than the one on DS9FX or TravellingMethods and some of those functions were not there.
# Makes a submenu for a given bridge menu, modified to add support for InsertChild()
def CreateMenu(sNewMenuName, sBridgeMenuName, bAdditional = 0, bPosition = 0):
	pMenu = GetBridgeMenu(sBridgeMenuName)
	pNewMenu = App.STMenu_Create(sNewMenuName)
       	
	if bAdditional == 1:
		pMenu.AddChild(pNewMenu)
	elif bAdditional == 2:
		pMenu.InsertChild(bPosition, pNewMenu)     
	else:
		pMenu.PrependChild(pNewMenu)

	return pNewMenu

# Removes a menu button
def RemoveMenu(name=MainHelmMenuName):
	#global bButton
	pBridge = App.g_kSetManager.GetSet("bridge")
	pHelm = App.CharacterClass_GetObject(pBridge, "Helm")
	pMenu = pHelm.GetMenu()
	if (pMenu != None):
		pButton = pMenu.GetSubmenu(name)
		if (pButton != None):
			pMenu.DeleteChild(pButton)
			#bButton = None
	return 0

def initRemoveInSystemNavpoint(pPlayer=None, pSet=None):
	if pPlayer == None:
		pPlayer = MissionLib.GetPlayer()
	if pPlayer:
		if pSet == None:
			pSet = pPlayer.GetContainingSet()
		if pSet:
			# Navpoint exists?
			try:
				pSet.DeleteObjectFromSet(NavPName)
			except:
				pass
			return pPlayer, pSet
		else:
			return pPlayer, None
	else:
		return None, None

# Mostly from Defiant's LibEngineering, but modified to work with a string event.
def CreateBridgeMenuButton(sButtonName, sMenuName, Function, bToButton = None, EventStr = ""):
	pMenu = GetBridgeMenu(sMenuName)
	
	ET_EVENT = App.Mission_GetNextEventType()

	pMenu.AddPythonFuncHandlerForInstance(ET_EVENT, Function)

	pEvent = App.TGStringEvent_Create()
	pEvent.SetEventType(ET_EVENT)
	pEvent.SetDestination(pMenu)
	pEvent.SetString(str(EventStr))
	pButton = App.STButton_CreateW(App.TGString(sButtonName), pEvent)
    
	if not bToButton:
		pMenu.PrependChild(pButton)
	else:
		bToButton.PrependChild(pButton)

	return pButton

# Mostly from Defiant's LibEngineering, but modified so it works with standalone buttons.
def CreateButton(sButtonName, sMenuName, Function, sToButton = None, EventInt = 0):        
        pMenu = GetBridgeMenu(sMenuName)

        if sToButton:
                sToButton = pMenu.GetSubmenu(sToButton)
        
        ET_EVENT = App.Mission_GetNextEventType()

        pMenu.AddPythonFuncHandlerForInstance(ET_EVENT, Function)

        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_EVENT)
        pEvent.SetDestination(pMenu)
        pEvent.SetInt(EventInt)
        pButton = App.STButton_CreateW(App.TGString(sButtonName), pEvent)
    
        if not sToButton:
                pMenu.PrependChild(pButton)
        else:
                sToButton.PrependChild(pButton)

        return pButton

def initAddMainMenuPart():
	bMenu = CreateMenu(MainHelmMenuName, "Helm", 2, 0)
	bNavPointButton = CreateButton(HelmButtonIniNavP, "Helm", __name__ + ".SlipstreamNavpoint", MainHelmMenuName)
	bInterceptMenu = App.STMenu_CreateW(App.TGString(HelmSubMName))
	bMenu.PrependChild(bInterceptMenu)
	#bNavPointButton = CreateBridgeMenuButton(HelmButtonIniNavP, "Helm", __name__ + ".SlipstreamNavpoint", bMenu)
	return bMenu, bNavPointButton, bInterceptMenu

def initAddMainMenuSubFTLPart(bInterceptMenu, name, dictName):
	bInterceptButton = None
	if name != None:
		bInterceptButton = CreateBridgeMenuButton(str(name), "Helm", __name__ + ".SlipstreamInterceptStats", bInterceptMenu, dictName)

	return bInterceptButton

def RemoveMouseHandler(pMission = None):
	if pMission == None:
		pGame = App.Game_GetCurrentGame()
		if pGame:
			pEpisode = pGame.GetCurrentEpisode()
			if pEpisode:
				pMission = pEpisode.GetCurrentMission()
	try:
		if pMission:
			App.g_kEventManager.RemoveBroadcastHandler(App.ET_MOUSE, pMission, __name__ + ".MoveNavpoint")
	except:
		print "Error while removing Mouse Handler:"
		traceback.print_exc()
	return 0

def AddMouseHandler(pMission = None):
	if pMission == None:
		pGame = App.Game_GetCurrentGame()
		if pGame:
			pEpisode = pGame.GetCurrentEpisode()
			if pEpisode:
				pMission = pEpisode.GetCurrentMission()

	try:
		if pMission:
			App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_MOUSE, pMission, __name__ + ".MoveNavpoint")
	except:
		print "Error while adding Mouse Handler:"
		traceback.print_exc()
	return 0

# Delete navpoint when exiting
def delnavpoint():
	global pButtonCondition, bNavPointButton
        
	#if not pSupported == 1:
	#    return 0
            
	# Navpoint deleted
	initRemoveInSystemNavpoint()
            
	# Handler deactivated
	RemoveMouseHandler()
            
	# No need to trigger this function more than necessary
	if not pButtonCondition == 1:
		# Change button stats and delete the navpoint
		pButtonCondition = 1
		if hasattr(bNavPointButton, 'SetName'):
			bNavPointButton.SetName(App.TGString("Initiate Navpoint Mode"))
	return 0

# Disable button
def disablebutton(bButton=None):
	delnavpoint()

	if bButton is None:
		return
	if hasattr(bButton, 'SetDisabled'):
		if bButton.IsEnabled():
			bButton.SetDisabled()

def quitting():
	global pPane
	RemoveMouseHandler()

	if not pPane == None:
		# Let's not cause any crashes
		pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
		try:
			# Just destroy the window, we don't need it anymore.
			App.g_kFocusManager.RemoveAllObjectsUnder(pPane)

			pTCW.DeleteChild(pPane)

			pPane = None
                    
		except:
			pass

	return 0

# Create a navpoint
def SlipstreamNavpoint(pObject, pEvent):
        global pButtonCondition, bNavPointButton, dist

        # Reset dist
        dist = navDist
        
        if pButtonCondition == 1:
            global NavPName
            # Button stats changed and name
            pButtonCondition = 0
            bNavPointButton.SetName(App.TGString("Stop Navpoint Mode"))
            
            # Create the navpoint
            pPlayer = MissionLib.GetPlayer()
            pSet = pPlayer.GetContainingSet()
            pLoc = pPlayer.GetWorldLocation()
            strNav = NavPName
            pNav = loadspacehelper.CreateShip("Distortion", pSet, strNav, None)

            fNav = MissionLib.GetShip(strNav, pSet) 
            fNav.SetTranslateXYZ(pLoc.GetX() + 150, pLoc.GetY() + 150, pLoc.GetZ())
            fNav.UpdateNodeOnly()
            fNav.SetHidden(1)
            fNav.SetInvincible(1)
            fNav.SetHurtable(0)

            # Remove the nav point from the proximity manager
            ProximityManager = pSet.GetProximityManager()
            ProximityManager.RemoveObject(fNav)
            
            # Setup a handler
            AddMouseHandler()

        else:
            # Change button stats and delete the navpoint
            pButtonCondition = 1
            bNavPointButton.SetName(App.TGString("Initiate Navpoint Mode"))
            
            # Navpoint deleted
            initRemoveInSystemNavpoint()
            
            # Handler deactivated
            RemoveMouseHandler()


# Move the navpoint by converting mouse xy to 3d xyz
def MoveNavpoint(pObject, pEvent):
	global dist

	# Has attr?
	if not hasattr(pEvent, 'GetButtonNum') and hasattr(pEvent, 'GetFlags'):
		return

	# Tactical mode?
	if not App.TopWindow_GetTopWindow().IsTacticalVisible():
		return

	# Grab mouse button number and flag
	eButton = pEvent.GetButtonNum()
	eFlag = pEvent.GetFlags()
	
	if eButton == 2048 and eFlag == 2816:
		pass

	elif eButton == 4096 and eFlag == 4864:
		dist = dist + 1000
		if dist > 11500:
			dist = 1500

	else:
		return

	# Admiral Ames was a very smart guy!
	eX = pEvent.GetX() * (dist) - (dist/2)
	eY = pEvent.GetY() * (-dist) + (dist/2)

	# Grab some values
	pPlayer = MissionLib.GetPlayer()
	pSet = pPlayer.GetContainingSet()
	pLoc = pPlayer.GetWorldLocation()
	pGame = App.Game_GetCurrentGame()
	pCamera = pGame.GetPlayerCamera()
	pFwdCam = pCamera.GetWorldForwardTG()
	pUpCam = pCamera.GetWorldUpTG()
	pRightCam = pCamera.GetWorldRightTG()

	# Calculate the xyz's
	cordX = dist * pFwdCam.GetX() + eX * pRightCam.GetX() + eY * pUpCam.GetX()
	cordY = dist * pFwdCam.GetY() + eX * pRightCam.GetY() + eY * pUpCam.GetY()
	cordZ = dist * pFwdCam.GetZ() + eX * pRightCam.GetZ() + eY * pUpCam.GetZ()

	# Translate the navpoint finally
	global NavPName
	fNav = MissionLib.GetShip(NavPName, pSet) 
	fNav.SetTranslateXYZ(pLoc.GetX() + cordX, pLoc.GetY() + cordY, pLoc.GetZ() + cordZ)
	fNav.UpdateNodeOnly()

def SlipstreamInterceptStats(pObject, pEvent):
	#Well this is different to how Mario's Slipstream operates, we just check the apporpiate functions

	if not pEvent or not hasattr(pEvent, "GetCString"):
		print "AlternateSubModelFTL: Warning, SlipstreamInterceptStats cannot find a string event"
		return

	myGoodPlugin = pEvent.GetCString()

	global eInSystemIntercept, eEquippedInSystemIntercept

	if eEquippedInSystemIntercept.has_key(myGoodPlugin):
		pPlayer =  MissionLib.GetPlayer()
		if pPlayer:
			iIsEquipped = eInSystemIntercept[myGoodPlugin]["IsEquipped"](pPlayer)
			if iIsEquipped > 0:
				canTravel = eEquippedInSystemIntercept[myGoodPlugin]["CanTravel"](pPlayer)
				if canTravel == 1:
					InterceptTargetCheck(myGoodPlugin)
				else:
					mybInterceptButton = None
					if eEquippedInSystemIntercept[myGoodPlugin].has_key("bInterceptButton"):
						mybInterceptButton = eEquippedInSystemIntercept[myGoodPlugin]["bInterceptButton"]

					if mybInterceptButton != None:
						mybInterceptButton.SetName(App.TGString("CANNOT DO"))
						pSequence = App.TGSequence_Create()
						pAction = App.TGScriptAction_Create(__name__, "ResetButtonString", mybInterceptButton, myGoodPlugin)
						pSequence.AddAction(pAction, None, 1)
						pSequence.Play()

					pSequence2 = App.TGSequence_Create ()
					pSubtitleAction = App.SubtitleAction_CreateC("Computer: " + str(canTravel))
					pSubtitleAction.SetDuration(3.0)
					pSequence2.AddAction(pSubtitleAction)
					pSequence2.Play()

					print canTravel
	else:
		print "AlternateSubModelFTL: Warning, SlipstreamInterceptStats cannot find the equipped plugin"
		return


# Are we targetting something?!
def InterceptTargetCheck(myGoodPlugin):
	global eEquippedInSystemIntercept

	mybInterceptButton = None
	if eEquippedInSystemIntercept.has_key(myGoodPlugin) and eEquippedInSystemIntercept[myGoodPlugin].has_key("bInterceptButton"):
		mybInterceptButton = eEquippedInSystemIntercept[myGoodPlugin]["bInterceptButton"]

	if mybInterceptButton != None:
		pPlayer = MissionLib.GetPlayer()
		pTargetShip = App.ShipClass_Cast(pPlayer.GetTarget())
		pTargetPlanet = App.Planet_Cast(pPlayer.GetTarget())

		customMult = 1.0
		if eInSystemIntercept[myGoodPlugin].has_key("AwayNavPointDistance"):
			customMult = eInSystemIntercept[myGoodPlugin]["AwayNavPointDistance"](pPlayer.GetObjID())

		if customMult < 0:
			customMult = 0.0

		if pTargetPlanet:
			if not DistanceCheck(pTargetPlanet) >= 400 * customMult:
				mybInterceptButton.SetName(App.TGString("TOO CLOSE"))
				pSequence = App.TGSequence_Create()
				pAction = App.TGScriptAction_Create(__name__, "ResetButtonString", mybInterceptButton, myGoodPlugin)
				pSequence.AddAction(pAction, None, 1)
				pSequence.Play()
				# print 'AlternateSubModelFTL ISI: Planet is too close...'
				return
            
			InterceptTarget(pTargetPlanet, 1, myGoodPlugin)

		elif pTargetShip:
			if not DistanceCheck(pTargetShip) >= 250 * customMult:
				mybInterceptButton.SetName(App.TGString("TOO CLOSE"))
				pSequence = App.TGSequence_Create()
				pAction = App.TGScriptAction_Create(__name__, "ResetButtonString", mybInterceptButton, myGoodPlugin)
				pSequence.AddAction(pAction, None, 1)
				pSequence.Play()
				# print 'AlternateSubModelFTL ISI: Ship is too close...'
				return
            
			InterceptTarget(pTargetShip, 0, myGoodPlugin)

		else:
			mybInterceptButton.SetName(App.TGString("NO TARGET"))
			pSequence = App.TGSequence_Create()
			pAction = App.TGScriptAction_Create(__name__, "ResetButtonString", mybInterceptButton, myGoodPlugin)
			pSequence.AddAction(pAction, None, 1)
			pSequence.Play()
			# print 'AlternateSubModelFTL ISI: No target...'
			return

	else:
		print "AlternateSubModelFTL: Error, InterceptTargetCheck cannot find the equipped button or plugin"

# Reset button string warning
def ResetButtonString(pAction, pButton, myGoodPlugin):
	try:
		if eEquippedInSystemIntercept.has_key(myGoodPlugin):
			myName = eEquippedInSystemIntercept[myGoodPlugin]["PropulsionType"]
			if myName == None:
				print "AlternateSubModelFTL: ERR.: missing PropulsionType Name for plugin: '", myGoodPlugin, "'"
				myName = myGoodPlugin
			pButton.SetName(App.TGString(myName))
		else:
			print "AlternateSubModelFTL: ERR.: missing plugin name: '", myGoodPlugin, "' in equipped dictionary"
	except:
		pass

	return 0

# Checks distance between the player and the given object
def DistanceCheck(pObject):
	pPlayer = App.Game_GetCurrentGame().GetPlayer()
	vDifference = pObject.GetWorldLocation()
	vDifference.Subtract(pPlayer.GetWorldLocation())

	return vDifference.Length()

def InterceptTarget(pTarget, IsPlanet, myGoodPlugin):
        global pWasCloaked
        
        # Grab values and start the prescripted sequence
        pPlayer = App.Game_GetCurrentPlayer()    
        pSequence = App.TGSequence_Create ()
        pSequence.AddAction(App.TGScriptAction_Create(__name__, "PositionPlayerIntercept", pTarget, IsPlanet, myGoodPlugin))
        pSequence.Play()

        # I have to grab the player over here and see if he's actually cloaked
        pWasCloaked = 0
        if pPlayer.IsCloaked():
            pWasCloaked = 1
            #pCloak = pPlayer.GetCloakingSubsystem()
            #if pCloak:
            #    pCloak.InstantDecloak()

# Redirect function
def PositionPlayerIntercept(pAction, pTarget, IsPlanet, myGoodPlugin):
        # Start the supplimentary function
        AdditionalPosAndCheckIntercept(None, pTarget, IsPlanet, myGoodPlugin)

        return 0

def callPlayerEventsForInSystem(pAction, myGoodPlugin, pPlayer=None, keyToLook="EntryEvent", eventsToOverlook=[App.ET_START_WARP_NOTIFY]):
	if not pPlayer:
		pPlayer = MissionLib.GetPlayer()

	if eInSystemIntercept.has_key(myGoodPlugin) and eInSystemIntercept[myGoodPlugin].has_key(keyToLook):
		try:
			for penEvent in eInSystemIntercept[myGoodPlugin][keyToLook](pPlayer):
				if hasattr(penEvent, "GetEventType") and not penEvent.GetEventType() in eventsToOverlook:
					App.g_kEventManager.AddEvent(penEvent)
		except:
			print "AlternateSubModelFTL: Error while calling local function callPlayerEventsForInSystem:"
			traceback.print_exc()
	return 0

def orderSeqPlay(pAction, mySequ):
	if mySequ != None:
		try:
			mySequ.Play()
		except:
			print "AlternateSubModelFTL: Error while playing a sequence in orderSeqPlay:"
			traceback.print_exc()
			
	return 0

# Returns a random number
def GetRandomRate(Max, Number):
	if Max <= 0:
		Max = 1
	return App.g_kSystemWrapper.GetRandomNumber(Max) + Number

# Reset navpoints after in system jump
def ResetNavpoints():
	global pButtonCondition, bNavPointButton
	
	# Change button stats and delete the navpoint
	pButtonCondition = 1
	if bNavPointButton != None and hasattr(bNavPointButton, "SetName"):
		bNavPointButton.SetName(App.TGString("Initiate Navpoint Mode"))

	# Navpoint deleted
	initRemoveInSystemNavpoint()
            
	# Handler deactivated
	RemoveMouseHandler()

	return 0

# Swap players position
def SwapPlayerPos(pAction, pTarget, IsPlanet):

	if not pTarget:
		return 0

	pPlayer = MissionLib.GetPlayer()
	if not pPlayer:
		return 0
	
	fRadius = 0
	pTargetX = 0
	pTargetY = 0
	pTargetZ = 0
	RateX = 0
	RateY = 0
	RateZ = 0
	
	# Target is planet
	if IsPlanet == 1:
		fRadius = pTarget.GetAtmosphereRadius() * 3

		pLocation = pTarget.GetWorldLocation()
		pTargetX = pLocation.GetX()
		pTargetY = pLocation.GetY()
		pTargetZ = pLocation.GetZ()

		# Take into account the atmosphere, given the fact that the planet was properly scripted...
		RateX = GetRandomRate(5, 200)
		RateY = GetRandomRate(5, 200)
		RateZ = GetRandomRate(5, 200)		

	# Target can only be a ship
	else:
		fRadius = pTarget.GetRadius() * 2

		pLocation = pTarget.GetWorldLocation()
		pTargetX = pLocation.GetX()   
		pTargetY = pLocation.GetY()
		pTargetZ = pLocation.GetZ()

		# Luckily ships don't have atmospheres
		RateX = GetRandomRate(5, 50)
		RateY = GetRandomRate(5, 50)
		RateZ = GetRandomRate(5, 50)

	pXCoord = pTargetX + RateX + fRadius
	pYCoord = pTargetY + RateY + fRadius
	pZCoord = pTargetZ + RateZ + fRadius

	pPlayer.SetTranslateXYZ(pXCoord, pYCoord, pZCoord)
	pPlayer.UpdateNodeOnly() 

	# Update proximity manager info for player
	pSet = pPlayer.GetContainingSet()
	if pSet:
		ProximityManager = pSet.GetProximityManager() 
		if (ProximityManager):
			try:
				ProximityManager.UpdateObject(pPlayer)
			except:
				print "AlternateSubModelFTL: SwapPlayerPos: Error while updating ProximityManager info for pPlayer:"
				traceback.print_exc()	

	# Kill the navpoint mode
	ResetNavpoints()
			
	return 0

def checkISIRecloaking():
	global pWasCloaked
	pPlayer = MissionLib.GetPlayer()
	if pWasCloaked == 1:
		pCloak = pPlayer.GetCloakingSubsystem()
		if pCloak:
			pCloak.InstantDecloak()
			pCloak.InstantCloak()
	return 0

def resetArrivingNone(myGoodPlugin):
	global eEquippedInSystemIntercept
	if myGoodPlugin != None and eEquippedInSystemIntercept != None and eEquippedInSystemIntercept.has_key(myGoodPlugin) and eEquippedInSystemIntercept[myGoodPlugin].has_key("ArrivingAt"):
		eEquippedInSystemIntercept[myGoodPlugin]["ArrivingAt"] = 0
	return 0

def BackToNormal(pAction, myGoodPlugin):
	global pDefault, pWasCloaked

	# Restore things back to normal
	pGame = App.Game_GetCurrentGame()
	pGame.SetGodMode(0)
	# Collision settings
	App.ProximityManager_SetPlayerCollisionsEnabled(pDefault)

	checkISIRecloaking()
	resetArrivingNone(myGoodPlugin)
        
        return 0

# Do the additional sweep to aid the position spin
def AdditionalPosAndCheckIntercept(pAction, pTarget, IsPlanet, myGoodPlugin):
	global pDefault
    
	# Positioning function

	sAim = None
	pPlayer = MissionLib.GetPlayer()

	if eEquippedInSystemIntercept.has_key(myGoodPlugin) and eInSystemIntercept[myGoodPlugin].has_key("EngageDirectionF"):
		try:
			sAim = eInSystemIntercept[myGoodPlugin]["EngageDirectionF"](pPlayer.GetObjID())
		except:
			print "AlternateSubModelFTL: Error while calling local function during AdditionalPosAndCheckIntercept:"
			traceback.print_exc()

		if sAim:
			fTime = pPlayer.TurnTowardDirection(sAim)
			# Not quite there yet?
			if fTime < fDirectionTimeThreshold:
				sAim = None
	# Good Aim
	if sAim == None:	       
		# Who the hell knows, something still might go wrong. Better be safe then sorry!
		pGame = App.Game_GetCurrentGame()
		pGame.SetGodMode(1)
		# Collision settings
		pDefault = App.ProximityManager_GetPlayerCollisionsEnabled()
		App.ProximityManager_SetPlayerCollisionsEnabled(0)

		# Grab player and set
		pSet = pPlayer.GetContainingSet()

		# Since there is a lot of customization, we need to make sure that things cannot go wrong if something on the customization went wrong.
		preEngSeq = None
		postEngSeq = None
		timeBetw = 1.0
		if eInSystemIntercept[myGoodPlugin].has_key("Sequences"):
			preEngSeq, timeBetw , postEngSeq = eInSystemIntercept[myGoodPlugin]["Sequences"](pPlayer)

		if preEngSeq == None:
			preEngSeq = App.TGSequence_Create()
			
		pSubAction = App.TGScriptAction_Create(__name__, "callPlayerEventsForInSystem", myGoodPlugin, pPlayer, "EntryEvent", [App.ET_START_WARP_NOTIFY])
		if pSubAction:
			preEngSeq.AddAction(pSubAction, None, 0)

		pActionChg = App.TGScriptAction_Create(__name__, "SwapPlayerPos", pTarget, IsPlanet)
		preEngSeq.AppendAction(pActionChg, timeBetw)

		pPostAction = App.TGScriptAction_Create(__name__, "callPlayerEventsForInSystem", myGoodPlugin, pPlayer, "ExitEvent", [App.ET_EXITED_SET])
		if pPostAction:
			preEngSeq.AddAction(pPostAction, pActionChg, 0.5)
		if postEngSeq != None:
			pClosureAction = App.TGScriptAction_Create(__name__, "orderSeqPlay", postEngSeq)
			if pClosureAction:
				preEngSeq.AppendAction(pClosureAction)

		pFinalAction = App.TGScriptAction_Create(__name__, "BackToNormal", myGoodPlugin)
		if pFinalAction != None:
			preEngSeq.AppendAction(pFinalAction)


		preEngSeq.Play()

	# Bad Aim, repeat process
	else:
		# Use sequence counter
		pSequence = App.TGSequence_Create()
		pAction = App.TGScriptAction_Create(__name__, "AdditionalPosAndCheckIntercept", pTarget, IsPlanet, myGoodPlugin)
		pSequence.AddAction(pAction, None, 1)
		pSequence.Play()

	return 0

#### END OF USS SOVEREIGN'S LIMITED PERMISSION AREA ####



# This class controls the attach and detach of the Models
#class ProtoWarp(SubModels):
class ProtoWarp(FoundationTech.TechDef):
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


	#### BEGINNING OF USS SOVEREIGN'S LIMITED PERMISSION AREA ####
		# the following listeners are part of an adapted Slipstream script by Mario aka USS Sovereign, and modified by Alex SL Gato with explicit permission from Mario, 
		# with the condition that this mod is intended to be released for KM. Do not modify them or this part of the mod without the conditions stated at the beginning of the file!

		# OK first we apply the .init() equivalents that zzzSlipstreamModule would have done
		App.g_kEventManager.RemoveBroadcastHandler(Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP, self.pEventHandler, "InSystemFTLFunctionHandler")

		App.g_kEventManager.AddBroadcastPythonMethodHandler(Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP, self.pEventHandler, "InSystemFTLFunctionHandler")
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_SET_PLAYER, self.pEventHandler, "InSystemFTLFunctionHandler") # For teleporting events
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_SET_PLAYER, self.pEventHandler, "InSystemFTLFunctionHandler")

		# This would be the equivalent to a pruned .handlers()
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_MISSION_START, self.pEventHandler, "InSystemFTLMissionStart")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_MISSION_START, self.pEventHandler, "InSystemFTLMissionStart")

		# This would be the equivalent to a pruned .disablebutton()
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, self.pEventHandler, "InSystemFTLDisableButton")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_ENTERED_SET, self.pEventHandler, "InSystemFTLDisableButton")

		# This would be the equivalent to a pruned .deletenavpoint()
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_EXITED_SET, self.pEventHandler, "InSystemFTLDelNavpoint")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_EXITED_SET, self.pEventHandler, "InSystemFTLDelNavpoint")

		# This would be the equivalent to a pruned .quitting()
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_QUIT, self.pEventHandler, "InSystemFTLQuitting")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_QUIT, self.pEventHandler, "InSystemFTLQuitting")
		
	def InSystemFTLQuitting(self, pEvent):
		debug(__name__ + ", InSystemFTLQuitting")
		# For all in-system-intercepts, clear everything
		quitting()
		return 0

	def InSystemFTLDelNavpoint(self, pEvent):
		debug(__name__ + ", InSystemFTLDelNavpoint")
		delnavpoint()
		return 0

	def InSystemFTLDisableButton(self, pEvent):
		debug(__name__ + ", InSystemFTLDisableButton")
		# Call the function(s) only if the player is the one triggering it
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		if pShip is None:
			return 0

		pShipID = pShip.GetObjID()
		if not pShipID:
			return 0

		pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShipID)
		if pShip is None:
			return 0
		
		pPlayer = MissionLib.GetPlayer()
		if pPlayer is None:
			return 0

		if pShip.GetObjID() == pPlayer.GetObjID():
			global eEquippedInSystemIntercept
			areWeIntercepting = 0

			RemoveMouseHandler()
			for method in eEquippedInSystemIntercept.keys():
				if areWeIntercepting == 0 and eEquippedInSystemIntercept[method].has_key("ArrivingAt") and eEquippedInSystemIntercept[method]["ArrivingAt"] == 1:
					areWeIntercepting = 1

			if areWeIntercepting == 1:
				try:
					import Bridge.HelmMenuHandlers
					Bridge.HelmMenuHandlers.g_bShowEnteringBanner = 0
				except:
					print "Error while calling InSystemFTLDisableButton"
					traceback.print_exc()
			disablebutton()
		else:
			return 0


		#eEquippedInSystemIntercept
		return 0	
	
	def InSystemFTLMissionStart(self, pEvent):
		debug(__name__ + ", InSystemFTLMissionStart")
		# On Mario's original version, this function also checked if the game was QB or a custom version of it or not and a course-set listener. On our case, we just need to initiate it as normal.
		self.InSystemFTLFunctionHandler(pEvent)
		return 0	

	def InSystemFTLFunctionHandler(self, pEvent):
		debug(__name__ + ", InSystemFTLFunctionHandler")
		global bMenu, bNavPointButton, bInterceptMenu, pButtonCondition

		RemoveMenu()
		RemoveMouseHandler()

		pPlayer, pSet = initRemoveInSystemNavpoint()
		if not pPlayer:
			return 0

		pButtonCondition = 1
		numEq = 0

		for myGoodPlugin in eInSystemIntercept.keys():
			iIsEquipped = eInSystemIntercept[myGoodPlugin]["IsEquipped"](pPlayer)
			if iIsEquipped:
				eEquippedInSystemIntercept[myGoodPlugin] = eInSystemIntercept[myGoodPlugin]
				eEquippedInSystemIntercept[myGoodPlugin]["ArrivingAt"] = 0
				numEq = numEq + 1
			else:
				try:
					if eEquippedInSystemIntercept.has_key(myGoodPlugin):
						del eEquippedInSystemIntercept[myGoodPlugin]
				except:
					print "AlternateSubModelFTL: Error while unequipping in InSystemFTLFunctionHandler:"
					traceback.print_exc()

		if numEq > 0:
			global NormalColor, HighlightedColor, NormalColor2, HighlightedColor2, DisabledColor

			bMenu, bNavPointButton, bInterceptMenu = initAddMainMenuPart()

			if bMenu != None and bNavPointButton != None and bInterceptMenu != None:
				bNavPointButton.SetUseUIHeight(0)
				bNavPointButton.SetNormalColor(NormalColor2)
				bNavPointButton.SetHighlightedColor(HighlightedColor2)
				bNavPointButton.SetSelectedColor(NormalColor2)
				bNavPointButton.SetDisabledColor(DisabledColor)
				bNavPointButton.SetColorBasedOnFlags()

				for myGoodPlugin in eEquippedInSystemIntercept.keys():
					myName = eEquippedInSystemIntercept[myGoodPlugin]["PropulsionType"]
					if myName == None:
						print "AlternateSubModelFTL: ERR.: missing PropulsionType Name for plugin: '", myGoodPlugin, "'"
						myName = myGoodPlugin
					bInterceptButton = initAddMainMenuSubFTLPart(bInterceptMenu, myName, myGoodPlugin)
					if bInterceptButton != None:
						bInterceptButton.SetUseUIHeight(0)
						bInterceptButton.SetNormalColor(NormalColor2)
						bInterceptButton.SetHighlightedColor(HighlightedColor2)
						bInterceptButton.SetSelectedColor(NormalColor2)
						bInterceptButton.SetDisabledColor(DisabledColor)
						bInterceptButton.SetColorBasedOnFlags()

					eEquippedInSystemIntercept[myGoodPlugin]["bInterceptButton"] = bInterceptButton			
		return 0

	#### END OF USS SOVEREIGN'S LIMITED PERMISSION AREA ####

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
		pInstanceDict["AlternateFTLSubModelOptionsList"] = [] # save options to this list, so we can access them later

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

				pInstance.AlternateFTLSubModelOptionsList.append("Setup", dOptions1)
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
			pInstance.AlternateFTLSubModelOptionsList.append(dofShip)

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
			AlertListener = AlertListener + 1
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
		if AlertListener > 0:
			PartsForWeaponProtoState(pShip, self)

	# Called by FoundationTech when a Ship is removed from set (eg destruction)
	def DetachShip(self, iShipID, pInstance):
		# get our Ship
		debug(__name__ + ", DetachShip")
		pShip = App.ShipClass_GetObjectByID(None, iShipID)
		if pShip:
			# remove the listeners
			self.Remove_FTLAndSituationMethods(pShip)
			
			if hasattr(pInstance, "AlternateFTLSubModelOptionsList"):
				for item in pInstance.AlternateFTLSubModelOptionsList:
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
						if item[1].has_key("MySemaphore"):
							del item[1]["MySemaphore"]
						if item[1].has_key("curMovID"):
							del item[1]["curMovID"]

		pInstanceDict = pInstance.__dict__
		if pInstanceDict:
			if pInstanceDict.has_key("Warp Overriden"):
				try:
					pInstanceDict["Warp Overriden"] = None
				except:
					pass
			
		if hasattr(pInstance, "HasExperimentalRotationParts"):
			del pInstance.HasExperimentalRotationParts
				
		if hasattr(pInstance, "SubModelFTLList"):
			for pSubShip in pInstance.SubModelFTLList:
				try:
					pSubShip = App.ShipClass_GetObjectByID(None, pSubShip.GetObjID())
					if pSubShip:
						pSet = pSubShip.GetContainingSet()
						pSubName = pSubShip.GetName()
						if pSet and pSubName != None:
							DeleteObjectFromSet(pSet, pSubName)
				except:
					print "Error while calling AlternateSubModelFTL DetachShip SubModelFTLList"
					traceback.print_exc()

			del pInstance.SubModelFTLList

		if hasattr(pInstance, "SubModelFTLListFirstTime"):
			del pInstance.SubModelFTLListFirstTime

	# Attaches the SubParts to the Body Model
	# Detach is inherited from SubModels
	def AttachParts(self, pShip, pInstance):
		debug(__name__ + ", AttachParts")

		pSet = pShip.GetContainingSet()
		if not pSet:
			print "AlternateSubModelFTL: Sorry, unable to add Attach Parts because there's no Containing Set."

		pInstanceDict = pInstance.__dict__
		if not pInstanceDict.has_key("SubModelFTLList"):
			pInstanceDict["SubModelFTLList"] = []

		ModelList = pInstanceDict[self.MySystemPointer()]

		pShipID = pShip.GetObjID()
		sNamePrefix = str(pShipID) + "_"
		SubModelFTLList = pInstance.SubModelFTLList

		myFirstTime = not hasattr(pInstance, "SubModelFTLListFirstTime") # Weird fix for parts dropping, interesting
		pCloak = pShip.GetCloakingSubsystem()
		shipIsCloaking = 0
		shipIsDecloaking = 0
		if pCloak:
			shipIsCloaking = pCloak.IsCloaking() or pCloak.IsCloaked() 
			shipIsDecloaking = pCloak.IsDecloaking() or not pCloak.IsCloaked()

		experimentalParts = 0
		# iteeeerate over every SubModel
		for sNameSuffix in ModelList.keys():
			if sNameSuffix == "Setup":
				continue

			sFile = ModelList[sNameSuffix][0]
			sShipName = sNamePrefix + sNameSuffix
			
			# check if the ship does exist first, before create it
			pSubShip = MissionLib.GetShip(sShipName, None, bAnySet = 1)


			# save the options list
			iSaveDone = 0

			dOptions = {} 
			# this is here to check if we already have the entry
			for lList in pInstance.AlternateFTLSubModelOptionsList:
				if lList[0] != "Setup":
					proceed = 0
					if lList[0] == sNameSuffix:
						proceed = 1
					else:
						if (lList[0] != None):
							if hasattr(lList[0], "GetObjID") and (lList[0].GetName() == sShipName):
								piNacelle = App.ShipClass_GetObjectByID(None, lList[0].GetObjID())
								if piNacelle:
									# The non-experimental performs an angleaxis rotation thatdoes not really affect a ship's position nor rotation when attached, it is best to keep it
									# The experimental suffers from drifts so it is best if we just use a fresh start
									if not pSubShip:
										if not (lList[1].has_key("Experimental") and lList[1]["Experimental"] != 0.0):
											pSubShip = piNacelle
										else:
											experimentalParts = experimentalParts + 1
											# FUTURE TO-DO check if you can just perform the same trick as with non-experimental, then re-orient things to fix issues
											# Apparently re-using the ship from above may cause a lights-out bug
											#pSubShip = piNacelle
											poSubSet = None
											poSubSet = piNacelle.GetContainingSet()
											if poSubSet:
												DeleteObjectFromSet(poSubSet, sShipName)
											piNacelle.SetDeleteMe(1)

								proceed = 1

					if proceed > 0 and lList[1]["sShipFile"] == sFile:
						if not pSubShip:
							pSubShip = None
							if lList[1].has_key("Experimental") and lList[1]["Experimental"] != 0.0:
								pSubShip = loadspacehelper.CreateShip(sFile, pSet, sShipName, "", 0, 1)
							else:
								pSubShip = loadspacehelper.CreateShip(sFile, pSet, sShipName, "", 0, 1)
							if not pSubShip:
								print "AlternateSubModelFTL: Sorry, unable to add ship of sFile = ", sFile, " . It is likely that such file with that exact name does not exist, and that will cause issues."

						lList[0] = pSubShip
						iSaveDone = 1
						dOptions = lList[1]
						break
					

			#print iSaveDone, dOptions
			
			if not iSaveDone:
				print "AlternateSubModelFTL: rebuilding options for ", sNameSuffix, ". This should not happen and it's only here if something went wrong..."
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

				pInstance.AlternateFTLSubModelOptionsList.append([pSubShip, dOptions2])
				dOptions = dOptions2

			if pSubShip == None:
				print "AlternateSubModelFTL: Error - missing SubShip during AttachParts "
				continue
			SubModelFTLList.append(pSubShip)

			# set current positions
			pSubShip.SetTranslateXYZ(dOptions["currentPosition"][0],dOptions["currentPosition"][1],dOptions["currentPosition"][2])

			scaleFactor = 1.0
			if dOptions.has_key("SetScale") and dOptions["SetScale"] != 0.0:
				scaleFactor = dOptions["SetScale"]

			pSubShip.SetUsePhysics(0)
			pSubShip.SetTargetable(0)
			mp_send_settargetable(pSubShip.GetObjID(), 0)
			pSubShip.SetInvincible(1)
			pSubShip.SetHurtable(0)
			#pSubShip.GetShipProperty().SetMass(1.0e+25)
			#pSubShip.GetShipProperty().SetRotationalInertia(1.0e+25)
			# Experimental-rotation nacelles cannot support the remove-from-set drifting-fix method without causing the main body vessel to become extremely dark, so we use the easier-to-implement but slightly less effective method of making that ship Stationary
			pSubShip.GetShipProperty().SetStationary(1)
			#if (dOptions.has_key("Experimental") and dOptions["Experimental"] != 0.0):
			#	pSubShip.GetShipProperty().SetStationary(1)
			pSubShip.SetHailable(0)
			if pSubShip.GetShields():
				pSubShip.GetShields().TurnOff()
	    
			pShip.EnableCollisionsWith(pSubShip, 0)
			pSubShip.EnableCollisionsWith(pShip, 0)
			MultiPlayerEnableCollisionWith(pShip, pSubShip, 0)
			for pSubShip2 in SubModelFTLList:
				if pSubShip.GetObjID() != pSubShip2.GetObjID():
					pSubShip.EnableCollisionsWith(pSubShip2, 0)
					pSubShip2.EnableCollisionsWith(pSubShip, 0)
					MultiPlayerEnableCollisionWith(pSubShip, pSubShip2, 0)

			if not (dOptions.has_key("Experimental") and dOptions["Experimental"] != 0.0):
				if myFirstTime: # If we don't do this the first time, we get inertia issues
					pMyMiniSet = pSubShip.GetContainingSet()
					pShip.DetachObject(pSubShip)
					if pMyMiniSet:
						DeleteObjectFromSet(pMyMiniSet, pSubShip.GetName())
					DeleteObjectFromSet(pSet, pSubShip.GetName())
				pSubShip.SetAngleAxisRotation(1.0, dOptions["currentRotation"][0], dOptions["currentRotation"][1], dOptions["currentRotation"][2])
				iNorm = math.sqrt(dOptions["currentRotation"][0] ** 2 + dOptions["currentRotation"][1] ** 2 + dOptions["currentRotation"][2] ** 2)
				pSubShip.SetScale((-iNorm + 1.85) * scaleFactor)
			#else:
			#	# Since attempting to make the non-legacy version have the proper initial rotation when added just causes the experimental rotation system to get very wonky rotations no matter the type of fixes I do, we are going to temporarily let the experimental rotation handle that while we hide the ship.
			#	pSubShip.SetScale(scaleFactor)
			#	pSubShip.SetHidden(1)

			# set current positions
			pSubShip.SetTranslateXYZ(dOptions["currentPosition"][0],dOptions["currentPosition"][1],dOptions["currentPosition"][2])

			pSubShip.UpdateNodeOnly()

			pShip.AttachObject(pSubShip)
			pShip.UpdateNodeOnly()

			if (dOptions.has_key("Experimental") and dOptions["Experimental"] != 0.0):
				performRotationAndScaleAdjust(pShip, pSubShip, dOptions, dOptions["currentRotation"][0], dOptions["currentRotation"][1], dOptions["currentRotation"][2], 0, 0, 0, 1)

			if pCloak:
				pSubShipID = pSubShip.GetObjID()
				if shipIsCloaking:
					CloakShip(pSubShipID, -1)
				elif shipIsDecloaking:
					CloakShip(pSubShipID, 1)

		if myFirstTime: # It's a dumb fix, but it works
			pInstance.SubModelFTLListFirstTime = 1
			pInstance.HasExperimentalRotationParts = experimentalParts

	# check if parts are attached
	def ArePartsAttached(self, pShip, pInstance):
		debug(__name__ + ", ArePartsAttached")
		if hasattr(pInstance, "SubModelFTLList"):
			return 1
		return 0

	# Detaches the parts
	def DetachParts(self, pShip, pInstance):
		debug(__name__ + ", DetachParts")
		if hasattr(pInstance, "SubModelFTLList"):
			for pSubShip in pInstance.SubModelFTLList:
				pSet = pSubShip.GetContainingSet()
				pShip.DetachObject(pSubShip)
				DeleteObjectFromSet(pSet, pSubShip.GetName())
			del pInstance.SubModelFTLList

oProtoWarp = ProtoWarp("Alternate-Warp-FTL")

# The class does the moving of the parts
# with every move the part continues to move
#class MovingEventUpdated(MovingEvent):
class MovingEventUpdated:
	# prepare fore move...
	def __init__(self, pShip, item, fDuration, lStartingRotation, lStoppingRotation, lStartingTranslation, lStoppingTranslation, dHardpoints):
		debug(__name__ + ", __init__")

		self.iNacelleID = item[0].GetObjID()
		self.iShipID = pShip.GetObjID()
		self.iThisMovID = item[1]["curMovID"]
		self.dAlternateFTLSubModelOptionsList = item[1]
		self.pShip = pShip
			
		self.fDurationMul = 1.0 #(1 - 0.03125) # 0.95 # make us a little bit faster to avoid bad timing
	
		# rotation values

		self.iSCurRotX = 0.0
		self.iSCurRotY = 0.0
		self.iSCurRotZ = 0.0

		self.experimentalFactor = 1.0

		if self.dAlternateFTLSubModelOptionsList.has_key("Experimental") and self.dAlternateFTLSubModelOptionsList["Experimental"] != 0.0:
			self.experimentalFactor = 1.5

			if not self.dAlternateFTLSubModelOptionsList.has_key("MySemaphore"): # We already have some drifts, better to ensure the sequences done are atomic just in case.
				self.dAlternateFTLSubModelOptionsList["MySemaphore"] = Semaphore()

		self.iCurRotX = lStartingRotation[0] + self.iSCurRotX
		self.iCurRotY = lStartingRotation[1] + self.iSCurRotY
		self.iCurRotZ = lStartingRotation[2] + self.iSCurRotZ

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
				print "AlternateSubModelFTL Error: Unable to find Hardpoint %s" % sHP
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

		self.firstTime = 0
		self.wentWrong = 0

	# move!
	def __call__(self):
		# if the move ID doesn't match then this move is outdated
		debug(__name__ + ", __call__")
		# this makes sure the game does not crash when trying to access a deleted element

		pShip = App.ShipClass_GetObjectByID(None, self.iShipID)
		if not pShip:
			print "AlternateSubModelFTL Moving Error: Lost MAIN part"
			return 0

		if not hasattr(self, "iNacelleID"):
			print "AlternateSubModelFTL Moving Error: Lost our own iNacelleID"
			return 0

		pNacelle = App.ShipClass_GetObjectByID(None, self.iNacelleID)
		if not pNacelle:
			print "AlternateSubModelFTL Moving Error: Lost part"
			return 0
		
		if (not self.dAlternateFTLSubModelOptionsList.has_key("curMovID")) or self.iThisMovID != self.dAlternateFTLSubModelOptionsList["curMovID"]:
			#print "AlternateSubModelFTL Move no longer active."
			return 1

		if self.dAlternateFTLSubModelOptionsList.has_key("MySemaphore"):
			self.dAlternateFTLSubModelOptionsList["MySemaphore"].acquire()

		# set new Translation values
		self.iCurTransX = self.iCurTransX + self.iTransStepX
		self.iCurTransY = self.iCurTransY + self.iTransStepY
		self.iCurTransZ = self.iCurTransZ + self.iTransStepZ
		# set Translation
		pNacelle.SetTranslateXYZ(self.iCurTransX, self.iCurTransY, self.iCurTransZ)
		pNacelle.UpdateNodeOnly()

		# set new Rotation values
		self.iCurRotX = self.iCurRotX + self.iRotStepX
		self.iCurRotY = self.iCurRotY + self.iRotStepY
		self.iCurRotZ = self.iCurRotZ + self.iRotStepZ
		# set Rotation

		aux = 0
		if hasattr(self, "firstTime"):
			aux = self.firstTime

		self.firstTime = performRotationAndScaleAdjust(pShip, pNacelle, self.dAlternateFTLSubModelOptionsList, self.iCurRotX, self.iCurRotY, self.iCurRotZ, self.iRotStepX, self.iRotStepY, self.iRotStepZ, aux)

		pNacelle.UpdateNodeOnly()

		if self.dAlternateFTLSubModelOptionsList.has_key("currentRotation"):
			self.dAlternateFTLSubModelOptionsList["currentRotation"] = [self.iCurRotX, self.iCurRotY, self.iCurRotZ]

		if self.dAlternateFTLSubModelOptionsList.has_key("currentPosition"):
			self.dAlternateFTLSubModelOptionsList["currentPosition"] = [self.iCurTransX, self.iCurTransY, self.iCurTransZ]
		
		# Hardpoints
		if self.dCurHPs != None:
			for sHP in self.dCurHPs.keys():
				self.dCurHPs[sHP][0] = self.dCurHPs[sHP][0] + self.dHPSteps[sHP][0]
				self.dCurHPs[sHP][1] = self.dCurHPs[sHP][1] + self.dHPSteps[sHP][1]
				self.dCurHPs[sHP][2] = self.dCurHPs[sHP][2] + self.dHPSteps[sHP][2]
				UpdateHardpointPositionsTo(self.pShip, sHP, self.dCurHPs[sHP])
		
		pNacelle.UpdateNodeOnly()

		if self.dAlternateFTLSubModelOptionsList.has_key("MySemaphore"):
			self.dAlternateFTLSubModelOptionsList["MySemaphore"].release()

		return 0
		

def performRotationAndScaleAdjust(pShip, pNacelle, dOptionsList, iCurRotX, iCurRotY, iCurRotZ, iRotStepX, iRotStepY, iRotStepZ, firstTime, iWait = 1.5): # iWait = 1.5 # iWait = 2.0 is to compensate steps

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

		if iRotStepX != 0.0 or iRotStepY != 0.0 or iRotStepZ != 0.0:
			vGlobalFinalAngles = App.TGPoint3()
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

		if firstTime != 0:
			pNacelle.SetHidden(0)

	else:
		pNacelle.SetAngleAxisRotation(1.0, iCurRotX, iCurRotY, iCurRotZ)
		iNorm = math.sqrt(iCurRotX ** 2 + iCurRotY ** 2 + iCurRotZ ** 2)
		pNacelle.SetScale((-iNorm + 1.85) * scaleFactor)


	return 0

def FloatNearlyEquals(n1, n2, tolerance=0.0078125):
	return (math.abs(n1 - n2) < tolerance)

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
	if hasattr(pInstance, "AlternateFTLSubModelOptionsList"):
		for item in pInstance.AlternateFTLSubModelOptionsList:
			if item[0] == "Setup":
				item[1]["GenMoveID"] = item[1]["GenMoveID"] + 1


def GetCurrentMoveIDUpdated(pShip, pInstance):
	debug(__name__ + ", GetCurrentMoveIDUpdated")
	iGenMoveID = 0
	if hasattr(pInstance, "AlternateFTLSubModelOptionsList"):	
		for item in pInstance.AlternateFTLSubModelOptionsList:
			if item[0] == "Setup":
				iGenMoveID = item[1]["GenMoveID"]
	return iGenMoveID
			

def MoveFinishMatchIDUpdated(pShip, pInstance, iThisMovID):
	debug(__name__ + ", MoveFinishMatchIDUpdated")
	try:
		if GetCurrentMoveIDUpdated(pShip, pInstance) == iThisMovID:
			return 1
		else:
			return 0
	except:
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
	if pCloak and hasattr(pInstance, "SubModelFTLList"): # Needs to be changed on other things
		shipIsCloaking = pCloak.IsCloaking()
		shipIsDecloaking = pCloak.IsDecloaking()
		for pSubShip in pInstance.SubModelFTLList:
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
	if pCloak and hasattr(pInstance, "SubModelFTLList"): # Needs to be changed on other things
		shipIsCloaking = pCloak.IsCloaking()
		shipIsDecloaking = pCloak.IsDecloaking()
		for pSubShip in pInstance.SubModelFTLList:
			pSubShipID = pSubShip.GetObjID()
			if shipIsCloaking:
				CloakShip(pSubShipID, 0)
			elif shipIsDecloaking:
				CloakShip(pSubShipID, 1)

	pObject.CallNextHandler(pEvent)


# calls the MovingEventUpdated class and returns its return value
def MovingActionUpdated(pAction, oMovingEventUpdated):
	debug(__name__ + ", MovingActionUpdated")
	value = 0
	try:
		oMovingEventUpdated()
	except:
		print "AlternateSubModelFTL: Something went wrong with MovingActionUpdated"
		value = 0
		traceback.print_exc()

	return value

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

	pShip = App.ShipClass_GetObjectByID(None, pObject.GetObjID())
	pSubsystem = pEvent.GetSource()

	# if the subsystem that changes its power is a weapon
	if not pSubsystem:
		pObject.CallNextHandler(pEvent)
		return 0

	if hasattr(pEvent, "GetBool"):
		wpnActiveState = pEvent.GetBool()

		if pSubsystem.IsTypeOf(App.CT_WEAPON_SYSTEM):
			# set turrets for this alert state
			PartsForWeaponProtoState(pShip, techP)
		"""
		else:
			try:
				pParent = pSubsystem.GetParentSubsystem()
				if pParent and (pParent.IsTypeOf(App.CT_WEAPON_SYSTEM) or pParent.IsTypeOf(App.CT_PHASER_SYSTEM) or pSubsystem.IsTypeOf(App.CT_PULSE_WEAPON_SYSTEM) or pSubsystem.IsTypeOf(App.CT_TORPEDO_SYSTEM)):
					PartsForWeaponProtoState(pShip, techP)
			except:
				pass
		"""

		pObject.CallNextHandler(pEvent)
		return
		
	pObject.CallNextHandler(pEvent)
	return 0 

# Prepares a ship to move: Replaces the current Model with the move Model and attaches its sub Models
def PrepareShipForProtoMove(pShip, pInstance, techType=oProtoWarp, move=oProtoWarp.MySubPositionPointer()):
	debug(__name__ + ", PrepareShipForProtoMove")
	pInstanceDict = None
	pIdictTech = None
	techName = techType.MySystemPointer()

	if pInstance != None:
		pInstanceDict = pInstance.__dict__
	else:
		return 1

	if pInstanceDict != None and pInstanceDict.has_key(techName):
		pIdictTech = pInstanceDict[techName]
	else:
		return 1

	sToIgnore = str(move) + "IgnoreCall"

	if pIdictTech == None or (pIdictTech["Setup"].has_key(sToIgnore) and pIdictTech["Setup"][sToIgnore] == 1):
		return 1

	if not techType.ArePartsAttached(pShip, pInstance):
		if pIdictTech["Setup"].has_key("Body"): 
			ReplaceModel(pShip, pIdictTech["Setup"]["Body"])
		if not hasattr(pInstance, "HasExperimentalRotationParts") or pInstance.HasExperimentalRotationParts <= 0:
			ReplaceModelBlackLightsFix(pShip)

		techType.AttachParts(pShip, pInstance)

		scaleFactor = 1.0
		if pIdictTech["Setup"].has_key("BodySetScale") and pIdictTech["Setup"]["BodySetScale"] != 0.0:
			scaleFactor = pIdictTech["Setup"]["BodySetScale"]
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
def JointAlertMoveFinishProtoAction(pAction, pShip, pInstance, dHardpoints, iThisMovID, techType = oProtoWarp):
	UpdateHardpointPositionsE(pAction, pShip, dHardpoints, iThisMovID)
	AlertMoveFinishProtoAction(pAction, pShip, pInstance, iThisMovID, techType)
	return 0


def AlertMoveFinishProtoAction(pAction, pShip, pInstance, iThisMovID, techType = oProtoWarp):
	
	# Don't switch Models back when the ID does not match
	debug(__name__ + ", AlertMoveFinishProtoAction")
	if not MoveFinishMatchIDUpdated(pShip, pInstance, iThisMovID):
		#print "AlternateSubModelFTL: AlertMoveFinishProtoAction: the IDs do not match"
		return 0
	try:
		techType.DetachParts(pShip, pInstance)
	except:
		traceback.print_exc()

	techName = techType.MySystemPointer()
	scaleFactor = 1.0
	sNewShipScript = None
	if pInstance.__dict__[techName]["Setup"].has_key("AttackModel") and pShip.GetAlertLevel() == 2:
		if pInstance.__dict__[techName]["Setup"].has_key("AttackModel"):
			sNewShipScript = pInstance.__dict__[techName]["Setup"]["AttackModel"]
		if pInstance.__dict__[techName]["Setup"].has_key("AttackSetScale") and pInstance.__dict__[techName]["Setup"]["AttackSetScale"] != 0.0:
			scaleFactor = pInstance.__dict__[techName]["Setup"]["AttackSetScale"]
	else:
		if pInstance.__dict__[techName]["Setup"].has_key("NormalModel"):
			sNewShipScript = pInstance.__dict__[techName]["Setup"]["NormalModel"]
		if pInstance.__dict__[techName]["Setup"].has_key("NormalSetScale") and pInstance.__dict__[techName]["Setup"]["NormalSetScale"] != 0.0:
			scaleFactor = pInstance.__dict__[techName]["Setup"]["NormalSetScale"]

	if sNewShipScript != None:
		ReplaceModel(pShip, sNewShipScript)
	if not hasattr(pInstance, "HasExperimentalRotationParts") or pInstance.HasExperimentalRotationParts <= 0:
		ReplaceModelBlackLightsFix(pShip)
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
		#print "AlternateSubModelFTL: ProtoWarpStartMoveFinishAction: the IDs do not match"
		return 0
		
	techP.DetachParts(pShip, pInstance)
	techName = techP.MySystemPointer()
	sNewShipScript = None
	if pInstance.__dict__[techName]["Setup"].has_key(str(move) + "Model"):
		sNewShipScript = pInstance.__dict__[techName]["Setup"][str(move) + "Model"]
	scaleFactor = 1.0
	if pInstance.__dict__[techName]["Setup"].has_key(str(move) + "SetScale") and pInstance.__dict__[techName]["Setup"][str(move) + "SetScale"] != 0.0:
		scaleFactor = pInstance.__dict__[techName]["Setup"][str(move) + "SetScale"]
	if sNewShipScript != None:
		ReplaceModel(pShip, sNewShipScript)
	if not hasattr(pInstance, "HasExperimentalRotationParts") or pInstance.HasExperimentalRotationParts <= 0:
		ReplaceModelBlackLightsFix(pShip)
	pShip.SetScale(scaleFactor)

	checkingReCloak(pShip)
	return 0


# called after the warp-exit move action
# Remove the attached parts and use the attack or normal model now
def ProtoWarpExitMoveFinishAction(pAction, pShip, pInstance, iThisMovID, techP=oProtoWarp, move=oProtoWarp.MySubPositionPointer()):
	# Don't switch Models back when the ID does not match
	debug(__name__ + ", ProtoWarpExitMoveFinishAction")
	if not MoveFinishMatchIDUpdated(pShip, pInstance, iThisMovID):
		#print "AlternateSubModelFTL: ProtoWarpExitMoveFinishAction: the IDs do not match"
		if move != "Warp":
			RestoreWarpOverriden(pShip, pInstance)
		return 0
		
	techP.DetachParts(pShip, pInstance)
	techName = techP.MySystemPointer()

	scaleFactor = 1.0
	sNewShipScript = None
	if pInstance.__dict__[techName]["Setup"].has_key("AttackModel") and pShip.GetAlertLevel() == 2:
		if pInstance.__dict__[techName]["Setup"].has_key("AttackModel"):
			sNewShipScript = pInstance.__dict__[techName]["Setup"]["AttackModel"]
		if pInstance.__dict__[techName]["Setup"].has_key("AttackSetScale") and pInstance.__dict__[techName]["Setup"]["AttackSetScale"] != 0.0:
			scaleFactor = pInstance.__dict__[techName]["Setup"]["AttackSetScale"]
	else:
		if pInstance.__dict__[techName]["Setup"].has_key("NormalModel"):
			sNewShipScript = pInstance.__dict__[techName]["Setup"]["NormalModel"]
		if pInstance.__dict__[techName]["Setup"].has_key("NormalSetScale") and pInstance.__dict__[techName]["Setup"]["NormalSetScale"] != 0.0:
			scaleFactor = pInstance.__dict__[techName]["Setup"]["NormalSetScale"]

	if sNewShipScript != None:
		ReplaceModel(pShip, sNewShipScript)

	if not hasattr(pInstance, "HasExperimentalRotationParts") or pInstance.HasExperimentalRotationParts <= 0:
		ReplaceModelBlackLightsFix(pShip)
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
def UpdateStateProto(pAction, pShip, item, lStoppingRotation, lStoppingTranslation, iThisMovID):
	debug(__name__ + ", UpdateStateProto")
	if item == None or not item or not item[1] or item[1] == None:
		print "AlternateSubModelFTL: no item return from UpdateStateProto"
		return 0

	pInstance = findShipInstance(pShip)
	if not pInstance or not MoveFinishMatchIDUpdated(pShip, pInstance, iThisMovID):
		#print "AlternateSubModelFTL: Called mismatching return from UpdateStateProto"
		return 0

	if item[1].has_key("currentRotation"):
		item[1]["currentRotation"] = lStoppingRotation
	if item[1].has_key("currentPosition"):
		item[1]["currentPosition"] = lStoppingTranslation
	if item[1].has_key("curMovID"):
		item[1]["curMovID"] = 0
	if item[1].has_key("MySemaphore"):
		del item[1]["MySemaphore"]

	return 0

def GetPositionOrientationPropertyByName(pShip, pcSubsystemName):
	debug(__name__ + ", GetPositionOrientationPropertyByName")
	pPropSet = pShip.GetPropertySet()
	pInstanceList = pPropSet.GetPropertiesByType(App.CT_POSITION_ORIENTATION_PROPERTY)

	pInstanceList.TGBeginIteration()
	iNumItems = pInstanceList.TGGetNumItems()

	for i in range(iNumItems):
		pInstance = pInstanceList.TGGetNext()
		pProperty = App.PositionOrientationProperty_Cast(pInstance.GetProperty())
		
		if pProperty.GetName().GetCString() == pcSubsystemName:
			return pProperty

	pInstanceList.TGDoneIterating()
	pInstanceList.TGDestroy()
	
	return None


def UpdateHardpointPositionsTo(pShip, sHP, lPos, extraCh = 0):
	debug(__name__ + ", UpdateHardpointPositionsTo")

	pHP = MissionLib.GetSubsystemByName(pShip, sHP)
	pPOP = GetPositionOrientationPropertyByName(pShip, sHP)
	if pHP:
		pHPprob = pHP.GetProperty()
		if pHPprob != None:
			pHPprob.SetPosition(lPos[0], lPos[1], lPos[2])
			if extraCh == 1:
				if lPos[3] != None and type(lPos[3]) == type({}):
					if lPos[3].has_key("Disabled Percentage"):
						pHPprob.SetDisabledPercentage(lPos[3]["Disabled Percentage"])
						#pHP.SetCondition(pHP.GetCondition())
	elif pPOP:
		pPosition = App.TGPoint3()
		pPosition.SetXYZ(lPos[0], lPos[1], lPos[2])
		pPOP.SetPosition(pPosition)
	else:
		print "AltSubmodel Error: Unable to find Hardpoint %s" % sHP
	pShip.UpdateNodeOnly()

def UpdateHardpointStatusTo(pShip, sHP, lPos):
	pSubsystemProperty = pSubsystem.GetProperty()
	if pSubsystemProperty:
		pSubsystemProperty.SetDisabledPercentage(pInstanceDict["Systems Changed With GC On"]["Hardpoints"][pSubsystem.GetName()])

def UpdateHardpointPositionsE(pAction, pShip, dHardpoints, iThisMovID):
	debug(__name__ + ", UpdateHardpointPositionsE")

	pInstance = findShipInstance(pShip)
	if not pInstance or not MoveFinishMatchIDUpdated(pShip, pInstance, iThisMovID):
		return 0

	for sHP in dHardpoints.keys():
		UpdateHardpointPositionsTo(pShip, sHP, dHardpoints[sHP], 1)
	return 0


# Set the parts to the correct alert state
def PartsForWeaponProtoState(pShip, techP):	
	debug(__name__ + ", PartsForWeaponProtoState")
	
	if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
		return 0
	
	pInstance = findShipInstance(pShip)
	if pInstance == None or not pInstance.__dict__.has_key(techP.MySystemPointer()):
		return 0

	iType = pShip.GetAlertLevel()
	iLongestTime = 0.0
	iGracePeriodTime = 2.0

	dHardpoints = {}
	
	# check if ship still exits
	pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
	if not pShip:
		return 0
	
	# try to get the last alert level
	for item in pInstance.AlternateFTLSubModelOptionsList:
		if item[0] == "Setup":
			dGenShipDict = item[1]
			break
	
	# check if the alert state has really changed since the last time
	if dGenShipDict["AlertLevel"] == iType:
		return 0
	# update alert state
	dGenShipDict["AlertLevel"] = iType


	# start with replacing the Models
	myTransStr = ""
	if iType == 2:
		myTransStr = "Attack"
	shouldStop = PrepareShipForProtoMove(pShip, pInstance, techP, myTransStr)
	if shouldStop == 1:
		return 0
	IncCurrentMoveIDUpdated(pShip, pInstance)
	thisMoveCurrentID = GetCurrentMoveIDUpdated(pShip, pInstance)
	
	# iterate over every submodel
	for item in pInstance.AlternateFTLSubModelOptionsList:
		if item[0] == "Setup":
			# attack or cruise modus?
			dHardpoints = {}
			if iType == 2 and item[1].has_key("AttackHardpoints"):
				dHardpoints = item[1]["AttackHardpoints"]
			elif iType != 2 and item[1].has_key("Hardpoints"):
				dHardpoints = item[1]["Hardpoints"]
			
			# setup is not a submodel
			continue

		if item[0] == None or not hasattr(item[0], "GetObjID"):
			print "AlternateSubModelFTL: nacelle ship missing. Aborting for this nacelle..."
			# The submodel is missing, for example because the ship file is missing.
			continue

		# set the id for this move
		iThisMovID = item[1]["curMovID"] + 1
		item[1]["curMovID"] = iThisMovID
	
		fDuration = 200.0 # In centiseconds (2 seconds)
		if item[1].has_key("AttackDuration"):
			fDuration = item[1]["AttackDuration"]

		initialWait = 0.1 # In seconds (so 10 centiseconds)
		if iType == 2 and item[1].has_key("AttackDelayEntry") and item[1]["AttackDelayEntry"] > 0:
			initialWait = initialWait + item[1]["AttackDelayEntry"]
		elif iType != 2 and item[1].has_key("AttackDelayExit") and item[1]["AttackDelayExit"] > 0:
			initialWait = initialWait + item[1]["AttackDelayExit"]
		
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
		if not hasattr(oMovingEventUpdated, "wentWrong") or oMovingEventUpdated.wentWrong != 0:
			print "AlternateSubModelFTL: oMovingEventUpdated found an issue while initializing - skipping"
			continue

		pSeq = None
		
		# do the move
		
		while(iTime * 100 <= (fDuration + (initialWait * 100))):
			if iTime == 0.0:
				iWait = initialWait # we wait for the first run
			else:
				iWait = 0.01 # normal step
			theScriptToPerform = App.TGScriptAction_Create(__name__, "MovingActionUpdated", oMovingEventUpdated)
			if theScriptToPerform != None:
				if pSeq == None:
					pSeq = App.TGSequence_Create()
				pSeq.AppendAction(theScriptToPerform, iWait)
			else:
				print "AlternateSubModelFTL: failed to create script action for PartsForWeaponProtoState ", iTimeNeededTotal, iTime, iWait
			iTimeNeededTotal = iTimeNeededTotal + iWait
			iTime = iTime + iWait

		finalLocalScriptAct = App.TGScriptAction_Create(__name__, "UpdateStateProto", pShip, item, lStoppingRotation, lStoppingTranslation, thisMoveCurrentID)
		if finalLocalScriptAct:
			if pSeq == None:
				pSeq = App.TGSequence_Create()
			pSeq.AppendAction(finalLocalScriptAct, 0.01)
			pSeq.Play()
		else:
			print "AlternateSubModelFTL: Error while trying to perform final local action"

		# iLongestTime is for the part that needs the longest time...
		if iTimeNeededTotal > iLongestTime:
			iLongestTime = round(iTimeNeededTotal, 2)

		## iLongestTime is for the part that needs the longest time...
		#if fDuration + initialWait > iLongestTime:
		#	iLongestTime = fDuration + initialWait #round(iTimeNeededTotal, 2)
		
	# finally detach
	#iLongestTime = iLongestTime/100.0

	pSeq = App.TGSequence_Create()
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "JointAlertMoveFinishProtoAction", pShip, pInstance, dHardpoints, thisMoveCurrentID), iLongestTime + iGracePeriodTime + 0.01)
	pSeq.Play()
	return 0


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
			techName = techP.MySystemPointer()
			if pInstanceDict["Warp Overriden"] <= 0 and not pInstanceDict.has_key(techName) and not pInstanceDict[techName].has_key(str(subPosition) + "IgnoreCall"):
				pInstanceDict["Warp Overriden"] = 1

	if not pInstanceDict or not pInstanceDict.has_key(techP.MySystemPointer()):
		return 0

	iLongestTime = 0.0
	iGracePeriodTime = 2.0

	dHardpoints = {}

	# start with replacing the Models
	shouldStop = PrepareShipForProtoMove(pShip, pInstance, techP, str(subPosition))
	if shouldStop == 1:
		return 0

	IncCurrentMoveIDUpdated(pShip, pInstance)
	thisMoveCurrentID = GetCurrentMoveIDUpdated(pShip, pInstance)

	subPositionHardpoints = str(subPosition) + "Hardpoints"
	subPositionDuration = str(subPosition) + "Duration"
	subPositionRotation = str(subPosition) + "Rotation"
	subPositionPosition = str(subPosition) + "Position"
	subPositionIg = "Ignore" + str(subPosition) + "Entry"
	subPositionDelay = str(subPosition) + "DelayEntry"
	for item in pInstance.AlternateFTLSubModelOptionsList:
		# setup is not a submodel
		if item[0] == "Setup":
			if item[1].has_key(subPositionHardpoints):
				dHardpoints = item[1][subPositionHardpoints]
			continue

		if item[0] == None or not hasattr(item[0], "GetObjID"):
			print "AlternateSubModelFTL: nacelle ship missing. Aborting for this type..."
			# The submodel is missing, for example because the ship file is missing.
			continue

		if item[1].has_key(subPositionIg) and item[1][subPositionIg] == 1:
			continue

		# set the id for this move
		iThisMovID = item[1]["curMovID"] + 1
		item[1]["curMovID"] = iThisMovID
	
		fDuration = 200.0
		
		if item[1].has_key(subPositionDuration):
			fDuration = item[1][subPositionDuration]

		initialWait = 0.1 # In seconds (so 10 centiseconds)
		if item[1].has_key(subPositionDelay) and item[1][subPositionDelay] > 0:
			initialWait = initialWait + item[1][subPositionDelay]
		    
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
		oMovingEventUpdated = MovingEventUpdated(pShip, item, fDuration, lStartingRotation, lStoppingRotation, lStartingTranslation, lStoppingTranslation, dHardpoints)
		if not hasattr(oMovingEventUpdated, "wentWrong") or oMovingEventUpdated.wentWrong != 0:
			print "AlternateSubModelFTL: oMovingEventUpdated found an issue while initializing - skipping"
			continue

		pSeq = App.TGSequence_Create()


		# do the move
		while(iTime * 100 <= (fDuration + (initialWait * 100))):
			if iTime == 0.0:
				iWait = initialWait # we wait for the first run
			else:
				iWait = 0.01 # normal step
			theScriptToPerform = App.TGScriptAction_Create(__name__, "MovingActionUpdated", oMovingEventUpdated)
			if theScriptToPerform != None:
				pSeq.AppendAction(theScriptToPerform, iWait)
			else:
				print "AlternateSubModelFTL: failed to create script action for PartsForWeaponProtoState ", iTimeNeededTotal, iTime, iWait
			iTimeNeededTotal = iTimeNeededTotal + iWait
			iTime = iTime + iWait

		finalLocalScriptAct = None

		if item[1].has_key("ResetToPrevious") and item[1]["ResetToPrevious"] == 1:
			finalLocalScriptAct = App.TGScriptAction_Create(__name__, "UpdateStateProto", pShip, item, lStartingRotation, lStartingTranslation, thisMoveCurrentID)
		else:
			finalLocalScriptAct = App.TGScriptAction_Create(__name__, "UpdateStateProto", pShip, item, lStoppingRotation, lStoppingTranslation, thisMoveCurrentID)

		if finalLocalScriptAct:
			pSeq.AppendAction(finalLocalScriptAct, 0.01)
			pSeq.Play()
		else:
			print "AlternateSubModelFTL: Error while trying to perform final local action"

		## iLongestTime is for the part that needs the longest time...
		if iTimeNeededTotal > iLongestTime:
			iLongestTime = round(iTimeNeededTotal, 2)
		#if fDuration + initialWait > iLongestTime:
		#	iLongestTime = fDuration + initialWait #round(iTimeNeededTotal, 2)
		
	# finally detach
	#iLongestTime = iLongestTime/100.0
	pSeq = App.TGSequence_Create()
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "UpdateHardpointPositionsE", pShip, dHardpoints, thisMoveCurrentID), iLongestTime + iGracePeriodTime + 0.01)
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "ProtoWarpStartMoveFinishAction", pShip, pInstance, thisMoveCurrentID, techP, subPosition), 2.0)
	pSeq.Play()

	return 0

def ExitingProtoWarp(pAction, pShip, techP, subPosition):
	debug(__name__ + ", ExitingProtoWarp")
	
	if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
		debug(__name__ + ", ExitingProtoWarp Return not host")
		return 0

	iType = pShip.GetAlertLevel()
	pInstance = findShipInstance(pShip)

	if not pInstance:
		#pObject.CallNextHandler(pEvent)
		return 0

	pInstanceDict = pInstance.__dict__

	if not pInstanceDict or not pInstanceDict.has_key(techP.MySystemPointer()): 
		return 0

	iLongestTime = 0.0
	iGracePeriodTime = 2.0

	dHardpoints = {}
	
	# first replace the Models
	shouldStop = PrepareShipForProtoMove(pShip, pInstance, techP, str(subPosition))
	if shouldStop == 1:
		return 0


	IncCurrentMoveIDUpdated(pShip, pInstance)
	thisMoveCurrentID = GetCurrentMoveIDUpdated(pShip, pInstance)

	subPositionHardpoints = str(subPosition) + "Hardpoints"
	subPositionDuration = str(subPosition) + "Duration"
	subPositionRotation = str(subPosition) + "Rotation"
	subPositionPosition = str(subPosition) + "Position"
	subPositionIg = "Ignore" + str(subPosition) + "Exit"
	subPositionDelay = str(subPosition) + "DelayExit"

	for item in pInstance.AlternateFTLSubModelOptionsList:
		# setup is not a submodel
		if item[0] == "Setup":
			dHardpoints = {}
			if iType == 2 and item[1].has_key("AttackHardpoints"):
				dHardpoints = item[1]["AttackHardpoints"]
			elif iType != 2 and item[1].has_key("Hardpoints"):
				dHardpoints = item[1]["Hardpoints"]
			continue

		if item[0] == None or not hasattr(item[0], "GetObjID"):
			print "AlternateSubModelFTL: nacelle ship missing. Aborting for this type..."
			# The submodel is missing, for example because the ship file is missing.
			continue

		if item[1].has_key(subPositionIg) and item[1][subPositionIg] == 1:
			continue

		# set the id for this move
		iThisMovID = item[1]["curMovID"] + 1
		item[1]["curMovID"] = iThisMovID
	
		fDuration = 200.0
		if item[1].has_key(subPositionDuration):
			fDuration = item[1][subPositionDuration]
		
		initialWait = 0.1 # In seconds (so 10 centiseconds)
		if item[1].has_key(subPositionDelay) and item[1][subPositionDelay] > 0:
			initialWait = initialWait + item[1][subPositionDelay]
    
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


		if item[1].has_key("ResetToPrevious") and item[1]["ResetToPrevious"] == 1:
			if item[1].has_key(subPositionRotation):
				lStartingRotation = item[1][subPositionRotation]
			if item[1].has_key(subPositionPosition):
				lStartingTranslation = item[1][subPositionPosition]
	
		iTime = 0.0
		iTimeNeededTotal = 0.0
		oMovingEventUpdated = MovingEventUpdated(pShip, item, fDuration, lStartingRotation, lStoppingRotation, lStartingTranslation, lStoppingTranslation, dHardpoints)
		if not hasattr(oMovingEventUpdated, "wentWrong") or oMovingEventUpdated.wentWrong != 0:
			print "AlternateSubModelFTL: oMovingEventUpdated found an issue while initializing - skipping"
			continue

		pSeq = App.TGSequence_Create()
		
		# do the move
		while(iTime * 100 <= (fDuration + (initialWait * 100))):
			if iTime == 0.0:
				iWait = initialWait # we wait for the first run
			else:
				iWait = 0.01 # normal step
			theScriptToPerform = App.TGScriptAction_Create(__name__, "MovingActionUpdated", oMovingEventUpdated)
			if theScriptToPerform != None:
				pSeq.AppendAction(theScriptToPerform, iWait)
			else:
				print "AlternateSubModelFTL: failed to create script action for PartsForWeaponProtoState ", iTimeNeededTotal, iTime, iWait
			iTimeNeededTotal = iTimeNeededTotal + iWait
			iTime = iTime + iWait

		finalLocalScriptAct = App.TGScriptAction_Create(__name__, "UpdateStateProto", pShip, item, lStoppingRotation, lStoppingTranslation, thisMoveCurrentID)

		if finalLocalScriptAct:
			pSeq.AppendAction(finalLocalScriptAct, 0.01)
			pSeq.Play()
		else:
			print "AlternateSubModelFTL: Error while trying to perform final local action"

		# iLongestTime is for the part that needs the longest time...
		if iTimeNeededTotal > iLongestTime:
			iLongestTime = round(iTimeNeededTotal, 2)
		
		## iLongestTime is for the part that needs the longest time...
		#if fDuration + initialWait > iLongestTime:
		#	iLongestTime = fDuration + initialWait #round(iTimeNeededTotal, 2)
		
	# finally detach
	#iLongestTime = iLongestTime/100.0
	pSeq = App.TGSequence_Create()
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "UpdateHardpointPositionsE", pShip, dHardpoints, thisMoveCurrentID), iLongestTime + iGracePeriodTime + 0.01)
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "ProtoWarpExitMoveFinishAction", pShip, pInstance, thisMoveCurrentID, techP, subPosition), 2.0)
	pSeq.Play()
	
	return 0
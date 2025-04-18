# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# Slipstream.py
# GC is ALL Rights Reserved by USS Frontier, but since GC supports Plugins it is fair to release a new TravellingMethod or patch old ones as long as the files remain unmodified.
# Based on the prototype custom travelling method plugin script, by USS Frontier (Normal Warp.py, original, template), original incomplete version made by BCXtreme (https://www.gamefront.com/games/bridge-commander/file/slipstream-for-galaxy-charts) and finished by Alex SL Gato.
# This plugin was originally released without a license, which means it defaults to All Rights Reserved. While the original readme includes the line "As far as I am concerned, anyone can take this and finish it if they want to," that grants permission to continue development — but not to relicense or attach a license such as LGPL. The absence of an explicit license means the work cannot be treated as open source.
# Slipstream Module remains ALL RIGHTS RESERVED, by USS Sovereign.
# Please note that this file requires:
# - USS Sovereign's Slipstream Module, as the purpose of the original mod was to provide exactly that.
# - All assets from the incomplete original from https://www.gamefront.com/games/bridge-commander/file/slipstream-for-galaxy-charts, except scripts/Custom/TravellingMethods/Slipstream.py.new (so, basically the files at scripts/Custom/GalaxyCharts)
# 18th April 2025
#################################################################################################################
##########	MANUAL
#################################################################################################################
# This mod provides Slipstream functionality for GalaxyCharts for ships that could use SlipstreamModule, finishing the work done by BCXtreme so sounds and flashes work properly, AI-only slipstream set is different from player-and-AI set, made some code check more efficient, and speeds are adjusted so AI vessels can use Slipstream.

# To make a ship use Slipstream, follow USS Sovereign's instructions on how to add his own Slipstream, which basically consists on adding any hardpoint called "Slipstream Drive " followed by a number from 1 to 20. Slipstream intercept is still handled by Sovereign's Slipstream Module, so do not expect a non-player to use it.
# NOTE: all functions/methods and attributes defined here (in this prototype example plugin, Slipstream) are required to be in the plugin, with the exception of:
# -Auxiliar attributes: "myDependingTravelModule", "myDependingTravelModuleLib", "myDependingTravelModuleLibPath", "myDependingTravelModulePath", "myGlobalAISet", "myGlobalpSet" and "pSlipstreamEngineSound"
# -Auxiliar functions: "AnObjectDying", "AuxProtoElementNames", "defineTravelSpaceNoise", "GetWellShipFromID", "PlaySlipstreamSounds", "SlipstreamDisabledCalculations", "SlipstreamFlash" and "WatchPlayerShipLeave".
# -Auxiliar classes: "WhyMissionLibGetsError" and its instance "basicListener"
# Additionally, "GetTravelSetToUse" was modified slightly from the template's original, so as to provide a way for possible extra scripts (i.e. some slipstream Hub jump network, if that is possible) to work easier.
#
#################################################################################################################
##########	END OF MANUAL
#################################################################################################################
#################################################################################################################
#
MODINFO = { "Author": "\"BCXtreme\" (original), \"Alex SL Gato\" andromedavirgoa@gmail.com (fixes), \"USS Sovereign\" (Slipstream Module)",
	    "Version": "0.16",
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
sName = "Slipstream"

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
sGoingTo = "Opening Slipstream Tunnel to"

########
# Phrase to show when the ship drops out of travel (while travelling)
########
sDropOut = "Dropped out of Slipstream Tunnel..."

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
myDependingTravelModulePath = "Custom.Slipstream.SlipstreamModule" # From where we load the module.
try:
	myDependingTravelModuleAux = __import__(myDependingTravelModulePath)
	if myDependingTravelModuleAux != None and hasattr(myDependingTravelModuleAux, "VERSION") and hasattr(myDependingTravelModuleAux, "sSlipstreamList") and hasattr(myDependingTravelModuleAux, "EnteringFlash") and hasattr(myDependingTravelModuleAux, "ExitingFlash"):
		myDependingTravelModule = myDependingTravelModuleAux
except:
	traceback.print_exc()

myDependingTravelModuleLib = None # The module we load.
myDependingTravelModuleLibPath = "Custom.Slipstream.Libs.LoadFlash" # From where we load the module.
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
	return "Slipstream" # Modify this with the name you are gonna use for the AlternateSubModelFTL

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


########
# Method to check if the ship is equipped with this travelling method.
# Must return 1 if it has it, 0 if it does not.
# NOTE: this function is not used as a method of the Travel class as are the other functions here.
#       this is actually used just like a helper for the Travel Manager.
########
def IsShipEquipped(pShip):

	hardpointProtoNames, hardpointProtoBlacklist = AuxProtoElementNames()
        totalSlipstreamEngines, onlineSlipstreamEngines = SlipstreamDisabledCalculations("Core", None, None, hardpointProtoNames, hardpointProtoBlacklist, None, pShip, 1)
	return (totalSlipstreamEngines > 0)

	return 0


########
# Method to check if the ship can travel.
# Must return 1 if it can, otherwise return a string(reason why the ship couldn't travel)
########
# This is just an auxiliar function I made for this
def AuxProtoElementNames(*args):
	# Returns hardpoint property name fragments that indicate are part of the B5Jumpspace system, and blacklists
	return ["slipstream drive"], ["not a slipstream drive", " not slipstream drive"]

# This is just another auxiliar function I (Alex SL Gato) made for more efficient system lookup.
# The original was like the OLD CODE example below, which follows Slipstream Module style in a way, looking for 20 particular names. However, there is an issue with that - it needs to do a pass on a ship's hardpoint for each subsystem name, out of 20. That means that on a best-case scenario it needs to perform part of a pass, while on a worst-case scenario, it needs to perform 20 passes to state that the ship lacks Slipstream. When it's only the player ship, it is acceptable. However, when it applies to ALL the potential ships on the galaxy and some of them have huge hardpoints, it LAGs a lot. The new method just needs to perform part of a pass on a best-case scenario, and 1 hardpoint pass on a worst-case one, and it will tell you how many slipstream drives are if you allow it to perform a full pass.
# OLD CODE:
# for i in range(20): # Slisptream Drive uses something like this. This is compeltely feasible when there's only 1 player
#		number = i + 1
#		pDrive = MissionLib.GetSubsystemByName(pShip, "Slipstream Drive "+str(number) )
#		if pDrive != None:
#			return 1

def SlipstreamDisabledCalculations(type, specificNacelleHPList, specificCoreHPList, hardpointProtoNames, hardpointProtoBlacklist, pSubsystem, pShip, justFindOne=0):
	totalSlipstreamEngines = 0
	onlineSlipstreamEngines = 0
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
							totalSlipstreamEngines = totalSlipstreamEngines + 1
							if pChild.GetCondition() > 0.0 and not pChild.IsDisabled():
								onlineSlipstreamEngines = onlineSlipstreamEngines + 1
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
							totalSlipstreamEngines = totalSlipstreamEngines + 1
							if pSubsystema.GetCondition() > 0.0 and not pSubsystema.IsDisabled() and (not hasattr(pSubsystema, "IsOn") or pSubsystema.IsOn()):
								onlineSlipstreamEngines = onlineSlipstreamEngines + 1
								if justFindOne == 1:
									break

		pShipList.TGDoneIterating()
		pShipList.TGDestroy()

	return totalSlipstreamEngines, onlineSlipstreamEngines

def CanTravel(self):
	if myDependingTravelModule == None:
		return "Impossible to travel to Slipstream if Slipstream does not exist!"
	pShip = self.GetShip()
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


	hardpointProtoNames, hardpointProtoBlacklist = AuxProtoElementNames()
        totalSlipstreamEngines, onlineSlipstreamEngines = SlipstreamDisabledCalculations("Core", None, None, hardpointProtoNames, hardpointProtoBlacklist, None, pShip, 0)
	if totalSlipstreamEngines <= 0:
		return "Unequipped with Slipstream Drive"
	if onlineSlipstreamEngines <= 0:
		return "Slipstream Drive disabled or offline"

	pSet = pShip.GetContainingSet()
	pNebula = pSet.GetNebula()
	if pNebula:
		if pNebula.IsObjectInNebula(pShip):
			if bIsPlayer == 1:
				pSequence = App.TGSequence_Create()
				pSubtitleAction = App.SubtitleAction_CreateC("LoMar: Captain, we can't open a slipstream tunnel inside a nebula.")
				pSubtitleAction.SetDuration(3.0)
				pSequence.AddAction(pSubtitleAction)
				pSequence.Play()
			return "Inside Nebula"

	# See if we are in an asteroid field
	AsteroidFields = pSet.GetClassObjectList(App.CT_ASTEROID_FIELD)
	for i in AsteroidFields:
		pField = App.AsteroidField_Cast(i)
		if pField:
			if pField.IsShipInside(pShip):
				if bIsPlayer == 1:
					pSequence = App.TGSequence_Create()
					pSubtitleAction = App.SubtitleAction_CreateC("LoMar: Captain, we can't open a slipstream tunnel inside an asteroid field.")
					pSubtitleAction.SetDuration(3.0)
					pSequence.AddAction(pSubtitleAction)
					pSequence.Play()
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
	pShip = self.GetShip()
	pPlayer = App.Game_GetCurrentPlayer()
	bIsPlayer = 0
	if pPlayer and pShip.GetObjID() == pPlayer.GetObjID():
		bIsPlayer = 1
	bStatus = 1

	hardpointProtoNames, hardpointProtoBlacklist = AuxProtoElementNames()
        totalSlipstreamEngines, onlineSlipstreamEngines = SlipstreamDisabledCalculations("Core", None, None, hardpointProtoNames, hardpointProtoBlacklist, None, pShip, 0)
	if totalSlipstreamEngines <= 0 or onlineSlipstreamEngines <= 0:
		if bIsPlayer == 1:
			pSequence = App.TGSequence_Create ()
			pSubtitleAction = App.SubtitleAction_CreateC("Brex: Slipstream Drive is disabled or offline, sir, the slipstream tunnel is collapsing.")
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
def GetEngageDirection(self):
	# Get all the objects along the line that we'll
	# be warping through.
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

# Some auxiliar global variables to allow set change and better sounds
myGlobalpSet = None
myGlobalAISet = None
pSlipstreamEngineSound = None

# An aux. function.
def GetWellShipFromID(pShipID):
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShipID)
	if not pShip or pShip.IsDead() or pShip.IsDying():
		return None
	return pShip

# An aux. function.
def PlaySlipstreamSounds(pAction, pShipID, sAction = "Enter Warp", sRace = None):
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
					print "Your slipstream module is missing a key library: ", myDependingTravelModuleLibPath
			else:
				print "There's no slipstream module on ", myDependingTravelModuleLibPath
	except:
			traceback.print_exc()
	return 0

# An aux. function. original by BCXtreme, modified by Alex SL Gato.
def SlipstreamFlash(pFlashAction1, pShipID):
	pShip = GetWellShipFromID(pShipID)
	if pShip:
		try:
			if myDependingTravelModule != None:
				if myDependingTravelModuleLib != None:
					myDependingTravelModuleLib.StartGFX(pShipID)
					myDependingTravelModuleLib.CreateGFX(pShip)
				else:
					print "Your slipstream module is missing a key library: ", myDependingTravelModuleLibPath
			else:
				print "There's no slipstream module on ", myDependingTravelModuleLibPath
		except:
			traceback.print_exc()
	else:
		print "ship not found or dying or dead"
	return 0

# An aux class and its instance.
class WhyMissionLibGetsError:
	def __init__(self, name):
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)

	def AnObjectDying(self, pEvent):
		try:
			AnObjectDying(self, pEvent)
		except:
			traceback.print_exc()
		return 0

	def BeginListening(self):
		self.StopListening()
		App.g_kEventManager.AddBroadcastPythonMethodHandler(Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP, self.pEventHandler, "AnObjectDying")
		#App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_OBJECT_EXPLODING, self.pEventHandler, "AnObjectDying")

	def StopListening(self):
		#App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, self.pEventHandler, "AnObjectDying")
		App.g_kEventManager.RemoveBroadcastHandler(Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP, self.pEventHandler, "AnObjectDying")

	def CallNextHandler(self, pEvent):
		return	

basicListener = WhyMissionLibGetsError("Lennier is listening")

# An aux function
def AnObjectDying(TGObject, pEvent):
	# Check and see if the mission is terminating
	debug(__name__ + ", ObjectDying")
		
	pShip	= App.ShipClass_Cast(pEvent.GetDestination())
	if (pShip == None):
		return 0

	pShipID = App.NULL_ID
	if hasattr(pShip, "GetObjID"):
		pShipID = pShip.GetObjID()

	if pShipID == None or pShipID == App.NULL_ID:
		return 0

	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShipID)
	if not pShip:
		return 0

	pPlayer = App.Game_GetCurrentPlayer()
	if pPlayer and hasattr(pPlayer, "GetObjID"):
		pPlayerID = pPlayer.GetObjID()
		if pPlayerID != None and pPlayerID != App.NULL_ID and pPlayerID == pShipID:
			try:
				defineTravelSpaceNoise(None, 0)
			except:
				print "Error while shutting up the global Slipstream noise:"
				traceback.print_exc()

	# All done, pass the event on
	TGObject.CallNextHandler(pEvent)
	return 0

# An aux function.
def defineTravelSpaceNoise(pAction, engage=1):
	debug(__name__ + ", defineTravelSpaceNoise")
	if myDependingTravelModule == None:
		return 0

	global pSlipstreamEngineSound
	if pSlipstreamEngineSound == None:
		pSlipstreamEngineSoundAux = None
		try:
			if hasattr(myDependingTravelModule, "pSlipstreamEngineSound"):
				pSlipstreamEngineSoundAux = myDependingTravelModule.pSlipstreamEngineSound
			else:
				pSlipstreamEngineSoundAux = App.TGSound_Create("scripts/Custom/Slipstream/SFX/slipstreamenginenoise.wav", "SlipstreamEngineSound", 0)
				pSlipstreamEngineSoundAux.SetSFX(0) 
				pSlipstreamEngineSoundAux.SetInterface(1)
				pSlipstreamEngineSoundAux.SetLooping(1)
		except:
			pSlipstreamEngineSoundAux = None
			print "Error on ", __name__, " defineTravelSpaceNoise:"
			traceback.print_exc()

		if pSlipstreamEngineSoundAux != None:
			pSlipstreamEngineSound = pSlipstreamEngineSoundAux

	if pSlipstreamEngineSound == None:
		return 0

	if engage == 0:
		try:
			App.g_kSoundManager.StopSound("SlipstreamEngineSound")

		except:
			print "Error on ", __name__, " defineTravelSpaceNoise:"
			traceback.print_exc()
	else:
		try:
			App.g_kSoundManager.PlaySound("SlipstreamEngineSound")

			try:
				basicListener.BeginListening()
			except:
				print "Error on ", __name__, " defineTravelSpaceNoise:"
				traceback.print_exc()

		except:
			print "Error on ", __name__, " defineTravelSpaceNoise:"
			traceback.print_exc()
		
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

	pWarpSoundAction1 = App.TGScriptAction_Create(__name__, "PlaySlipstreamSounds", pShipID, "Enter Warp", sRace)
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
	pFlashAction1 = App.TGScriptAction_Create(__name__, "SlipstreamFlash", pShipID) #pFlashAction1 = App.TGScriptAction_Create("Actions.EffectScriptActions", "WarpFlash", pShip)
	pEngageWarpSeq.AddAction(pFlashAction1, None, fTimeToFlash)

	# Hide the ship.
	pHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShipID, 1)
	pEngageWarpSeq.AddAction(pHideShip, pFlashAction1, 1.6)

	pUnBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShipID, 0, 1.0)
	pEngageWarpSeq.AddAction(pUnBoostAction, pHideShip)
	
	pCheckTowing = App.TGScriptAction_Create(sCustomActionsScript, "EngageSeqTractorCheck", pWS)
	pEngageWarpSeq.AddAction(pCheckTowing, pHideShip)

	if (pPlayer != None) and (pShipID == pPlayer.GetObjID()):
		pWarpSoundActionMid = App.TGScriptAction_Create(__name__, "defineTravelSpaceNoise", 1)
		pEngageWarpSeq.AddAction(pWarpSoundActionMid, pUnBoostAction, 2.5)	

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

			pWarpSoundActionMidFinal = App.TGScriptAction_Create(__name__, "defineTravelSpaceNoise", 0)
			pExitWarpSeq.AddAction(pWarpSoundActionMidFinal, None)

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
		pFlashAction2 = App.TGScriptAction_Create(__name__, "SlipstreamFlash", pShipID)  #pFlashAction2 = App.TGScriptAction_Create("Actions.EffectScriptActions", "WarpFlash", pShip)
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
		pWarpSoundAction2 = App.TGScriptAction_Create(__name__, "PlaySlipstreamSounds", pShipID, "Exit Warp", sRace)
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
def GetStartTravelEvents(self): # No need for ISI, Slipstream module takes care of that.
	debug(__name__ + ", GetStartTravelEventsI")

	pShip = self.Ship

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
def GetExitedTravelEvents(self): # No need for ISI, Slipstream module takes care of that.
	debug(__name__ + ", GetExitedTravelEventsI")

	pShip = self.Ship

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
		import Custom.GalaxyCharts.TravelerSystems.SlipstreamTravel
		import Custom.GalaxyCharts.TravelerSystems.AISlipstreamTravel
		pSet = None
		if manual != 0:
			if manual == 1:
				if myGlobalpSet == None:
					myGlobalpSet = Custom.GalaxyCharts.TravelerSystems.SlipstreamTravel.Initialize()
				return myGlobalpSet
			else:
				if myGlobalAISet == None:
					myGlobalAISet = Custom.GalaxyCharts.TravelerSystems.AISlipstreamTravel.Initialize()
				return myGlobalAISet
		if self.IsPlayer == 1:
			if myGlobalpSet == None:
				myGlobalpSet = Custom.GalaxyCharts.TravelerSystems.SlipstreamTravel.Initialize()
			pSet = myGlobalpSet
		elif self.IsPlayer == 0 and self.IsAIinPlayerRoute == 1:
			if myGlobalpSet == None:
				myGlobalpSet = Custom.GalaxyCharts.TravelerSystems.SlipstreamTravel.Initialize()
			pSet = myGlobalpSet
		elif self.IsPlayer == 0 and self.IsAIinPlayerRoute == 0:
			if myGlobalAISet == None:
				myGlobalAISet = Custom.GalaxyCharts.TravelerSystems.SlipstreamTravel.Initialize()
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
	if fSpeed >= 9.999:
		fFacA = 2.88		##### Do Not Change These Values #####
		fFacB = 8.312	       ##### Do Not Change These Values #####
	elif fSpeed > 9.99:
		fFacA = 2.88		##### Do Not Change These Values #####
		fFacB = 7.512	       ##### Do Not Change These Values #####
	elif fSpeed > 9.6:
		fFacA = 2.8700	      ##### Do Not Change These Values #####
		fFacB = 5.9645	      ##### Do Not Change These Values #####
	elif fSpeed <= 9.6:
		fFacA = 3.0		 ##### Do Not Change These Values #####
		fFacB = 3.0		 ##### Do Not Change These Values #####

	speed = (math.pow(fSpeed, (10.0/fFacA)) + math.pow((10.0-fSpeed), (-11.0/fFacB)))

	speed = (75000/3.0) * speed * (math.pow(4.0, (10.0/fFacA)) + math.pow((10.0-4.0), (-11.0/fFacB)))

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

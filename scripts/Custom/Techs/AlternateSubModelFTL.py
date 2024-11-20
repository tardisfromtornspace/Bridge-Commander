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

# This class inherits from Defiant's SubModels script - as such, it depends on it.
# TO-DO FIRST BEFORE PERFORMING THE THING BELOW, FIX THE BUGS THAT WERE NOT THERE BEFORE
# TO-DO TEMPORARILY MODIFY THE CRASHFIXER SO ECH FUNCTION THROWS WHAT TYPE OF CRASH WAS AVOIDED, TO KNOW BETTER WHAT WAS WRONG
#TO-DO UPDATE, ALSO UPDATE THE SAMPLE SETUP TO HAVE TABS AND BE MORE CLEAR
# TO-DO Try to make this work with broadcast handlers and then you just push them onto the __init__ - something similar to how you extend things with SGShields and such
#
#################################################################################################################
#
MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "0.2",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }
#
#################################################################################################################
#

# TO-DO It is NOT RECOMMENDED to combine the parent SubModels class with STProdigyProtoWarp class and possible children since sublists are shared.



"""

Sample Setup:
# TO-DO MODIFY THINGS SO IT CHECKS "Alternate-Warp-FTL" and from there "Proto-Warp" : {"Nacelles": [], "Core": []}
#
Foundation.ShipDef.VasKholhr.dTechs = { "Alternate-Warp-FTL": {
	"Setup":	{
		"Body":	"VasKholhr_Body",
		"NormalModel": shipFile,
		"WarpModel": "VasKholhr_WingUp",
		"ProtoWarpModel":	  "VasKholhr_WingUp",
		"AttackModel":	  "VasKholhr_WingDown",
		"Hardpoints":       {
			"Port Cannon":  [-0.677745, 0.514529, -0.229285],
			"Star Cannon":  [0.663027, 0.511252, -0.240265],
			"Port Cannon 1":  [-0.323324, 0.240263, -0.115398],
			"Star Cannon 1":  [0.319566, 0.242142, -0.11861],
		},
		"AttackHardpoints":       {
			"Port Cannon":  [-0.503543, 0.524792, -0.47761],
			"Star Cannon":  [0.486256, 0.527008, -0.483889],
			"Port Cannon 1":  [-0.244469, 0.228191, -0.19762],
			"Star Cannon 1":  [0.243789, 0.243208, -0.201933],
		},
	},
		
	"Port Wing":     ["VasKholhr_Portwing", {
		"Position":	     [0, 0, 0],
		"Rotation":	     [0, 0, 0], # normal Rotation used if not Red Alert and if not Warp
		"AttackRotation":	 [0, -0.6, 0],
		"AttackDuration":	 200.0, # Value is 1/100 of a second
		"AttackPosition":	 [0, 0, 0.03],
		"WarpRotation":       [0, 0.349, 0],
		"WarpPosition":       [0, 0, 0.02],
		"WarpDuration":       150.0,
		}
	],
	
	"Starboard Wing":     ["VasKholhr_Starboardwing", {
		"Position":	     [0, 0, 0],
		"Rotation":	     [0, 0, 0],
		"AttackRotation":	 [0, 0.6, 0],
		"AttackDuration":	 200.0, # Value is 1/100 of a second
		"AttackPosition":	 [0, 0, 0.03],
		"WarpRotation":       [0, -0.349, 0],
		"WarpPosition":       [0, 0, 0.02],
		"WarpDuration":       150.0,
		}
	],
}}



"""

REMOVE_POINTER_FROM_SET = 190
NO_COLLISION_MESSAGE = 192
REPLACE_MODEL_MSG = 208
SET_TARGETABLE_MSG = 209

# TO-DO Ok so idea would be, first we skim through all the TravellingMethods folder
# If we find certain functions (a function that would return a proper function and its eType), we store them
# StartingProtoWarp(pObject, pEvent, techP, move=oProtoWarp.MySubPositionPointer()):
# eTypeDict = {"eType": function}
## for eType in eTypeDict.keys():
## 	App.g_kEventManager.RemoveBroadcastHandler(eType, self.pEventHandler, "FTLFunctionHandler")
##	App.g_kEventManager.AddBroadcastPythonMethodHandler(eType, self.pEventHandler, "FTLFunctionHandler")
##
## def FTLFunctionHandler(self, pEvent, AND WHATEVER IS NEEDED HERE)
##	eType = pEvent.GetEventType()
##	pShip = pEvent.GetDestination() # stub, obviously fix it
##	eTypeDict[eType](self, pShip, pEvent, AND WHATEVER IS NEEDED HERE) # Best of this is that we would not need to check special techs or anything of the sort
##      # BTW self would be "techP"
## Do not worry about actual FTL speeds, that is what the other script works in

# Because SubModels is ridiculously hard to make children without having to re-do all the functions, I've made this, so now you can just re-do the attach/detach

eTypeDict = {} #"eType": function

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
						print eType, functionEnteringWarp
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

#TO-DO UPDATE FROM HERE

# This class controls the attach and detach of the Models
class ProtoWarp(SubModels):
	#className = "Proto-Warp"
	#classSub = "Proto-Warp"

	def __init__(self, name):
		debug(__name__ + ", Initiated")
		FoundationTech.TechDef.__init__(self, name)
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)
		# TO-DO ACTUALLY DO NOT ADD THIS FOR WARP DRIVE AND EXITSET, USE NORMAL ONES FOR THAT, AND FTL BROADCASTS FOR OTHERS :)
		# TO-DO ACTUALLY TEST THIS! Make it so they import the proper config!!!
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
							# TO-DO COMMENT THIS LINE
							print "And the ship still exists, calling function:"
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
		print "Ship %s with ProtoWarp support added" % pShip.GetName()

		sNamePrefix = pShip.GetName() + "_"
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
				# we start with green alert
				if not dOptions.has_key("AlertLevel"):
					dOptions["AlertLevel"] = {}
				if not dOptions.has_key("GenMoveID"):
					dOptions["GenMoveID"] = {}
				dOptions["AlertLevel"][pShip.GetName()] = 0
				dOptions["GenMoveID"][pShip.GetName()] = 0
				pInstance.OptionsList.append("Setup", dOptions)
				continue # nothing more todo here
			#
			# the following stuff is only for the objects that moves
			
			if len(ModelList[sNameSuffix]) > 1:
				dOptions = ModelList[sNameSuffix][1]
			sFile = ModelList[sNameSuffix][0]
			loadspacehelper.PreloadShip(sFile, 1)
			
			# save the shipfile for later use
			dOptions["sShipFile"] = sFile
			
			# set current rotation/position values
			if not dOptions.has_key("currentRotation"):
				dOptions["currentRotation"] = {}
			if not dOptions.has_key("currentPosition"):
				dOptions["currentPosition"] = {}
			if not dOptions.has_key("curMovID"):
				dOptions["curMovID"] = {}
			dOptions["currentRotation"][pShip.GetName()] = [0, 0, 0] # those two lists are updated with every move
			dOptions["currentPosition"][pShip.GetName()] = [0, 0, 0]
			dOptions["curMovID"][pShip.GetName()] = 0
			if not dOptions.has_key("Position"):
				dOptions["Position"] = [0, 0, 0]
			dOptions["currentPosition"][pShip.GetName()] = dOptions["Position"] # set current Position
			
			if not dOptions.has_key("Rotation"):
				dOptions["Rotation"] = [0, 0, 0]
			dOptions["currentRotation"][pShip.GetName()] = dOptions["Rotation"] # set current Rotation
			
			# event listener
			AlertListener = self.Add_FTLAndSituationMethods(dOptions, pShip, pInstanceDict, AlertListener)

		self.PerformPostAttachLoopActions(pShip, AlertListener)

	# TO-DO REMOVE DRIED LAVA
	def AddbAddedFTLSituationListener(self):
		self.bAddedWarpListener = {} # these variables will make sure we add our event handlers only once
		#self.bAddedProtoWarpListener = {}
		self.bAddedAlertListener = {}

	def Add_FTLAndSituationMethods(self, dOptions, pShip, pInstanceDict, AlertListener):
		#self.Add_ProtoWarpMethods(pShip, dOptions, pInstanceDict)
		self.Add_WarpMethods(pShip, dOptions)
		AlertListener = self.Add_AttackMethods(pShip, dOptions, AlertListener, pInstanceDict)
		return AlertListener

	def Remove_FTLAndSituationMethods(self, pShip):
		#self.Remove_ProtoWarpMethods(pShip)
		self.Remove_WarpMethods(pShip)
		self.Remove_AttackMethods(pShip)

	def Add_AttackMethods(self, pShip, dOptions, AlertListener, pInstanceDict):
		if not self.bAddedAlertListener.has_key(pShip.GetName()) and (dOptions.has_key("AttackRotation") or dOptions.has_key("AttackPosition")):
			pShip.AddPythonFuncHandlerForInstance(App.ET_SET_ALERT_LEVEL, __name__ + ".AlertProtoStateChanged")
			# Alert change handler doesn't work for AI ships, so use subsystem changed instead
			pShip.AddPythonFuncHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateProtoChanged")
			self.bAddedAlertListener[pShip.GetName()] = 1 
			AlertListener = 1
		return AlertListener
	def Remove_AttackMethods(self, pShip):
		if self.bAddedAlertListener.has_key(pShip.GetName()):
			pShip.RemoveHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateProtoChanged")
			pShip.RemoveHandlerForInstance(App.ET_SET_ALERT_LEVEL, __name__ + ".AlertProtoStateChanged")
			try:
				del self.bAddedAlertListener[pShip.GetName()]
			except:
				pass

	def Add_WarpMethods(self, pShip, dOptions):
		if not self.bAddedWarpListener.has_key(pShip.GetName()) and (dOptions.has_key("WarpRotation") or dOptions.has_key("WarpPosition")):
			pShip.AddPythonFuncHandlerForInstance(App.ET_START_WARP, __name__ + ".StartingWarpE")
			pShip.AddPythonFuncHandlerForInstance(App.ET_START_WARP_NOTIFY, __name__ + ".StartingWarpE")
			# ET_EXITED_WARP handler doesn't seem to work, so use ET_EXITED_SET instead
			pShip.AddPythonFuncHandlerForInstance(App.ET_EXITED_SET, __name__ + ".ExitSetWarp")
			self.bAddedWarpListener[pShip.GetName()] = 1
	def Remove_WarpMethods(self, pShip):
		if self.bAddedWarpListener.has_key(pShip.GetName()):
			pShip.RemoveHandlerForInstance(App.ET_START_WARP, __name__ + ".StartingWarpE") # TO-DO ADJUST TO ADD MISSING STARTING WARP AND ENDING WARP THINGS
			pShip.RemoveHandlerForInstance(App.ET_START_WARP_NOTIFY, __name__ + ".StartingWarpE")
			pShip.RemoveHandlerForInstance(App.ET_EXITED_SET, __name__ + ".ExitSetWarp")
			try:
				del self.bAddedWarpListener[pShip.GetName()]
			except:
				pass

	def Add_ProtoWarpMethods(self, pShip, dOptions, pInstanceDict):
		if not self.bAddedProtoWarpListener.has_key(pShip.GetName()) and (dOptions.has_key("ProtoWarpRotation") or dOptions.has_key("ProtoWarpPosition")):
			pShip.AddPythonFuncHandlerForInstance(ENGAGING_PROTO_WARP, __name__ + ".StartingProtoWarp")
			pShip.AddPythonFuncHandlerForInstance(DISENGAGING_PROTO_WARP, __name__ + ".ExitSetProto")
			self.bAddedProtoWarpListener[pShip.GetName()] = 1 # 1 = Not protowarping, 2 = protowarping - warp sequence verifies its own warp sequence is not suppressed.
	def Remove_ProtoWarpMethods(self, pShip, pInstanceDict):
		if self.bAddedProtoWarpListener.has_key(pShip.GetName()): # TO-DO UPDATE IF NECESSARY REMOVING THESE AND ONLY USING BROADCAST HANDLER?
			pShip.RemoveHandlerForInstance(ENGAGING_PROTO_WARP, __name__ + ".StartingProtoWarp")
			pShip.RemoveHandlerForInstance(DISENGAGING_PROTO_WARP, __name__ + ".ExitSetProto")
			try:
				del self.bAddedProtoWarpListener[pShip.GetName()]
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
			self.Remove_FTLAndSituationMethods(pShip) # TO-DO MAKE IT SO ONLY THE WARP LISTENERS ARE HERE
			
			if hasattr(pInstance, "OptionsList"):
				for item in pInstance.OptionsList:
					if item[0] == "Setup":
						del item[1]["AlertLevel"][pShip.GetName()]
					else:
						del item[1]["currentRotation"][pShip.GetName()]
						del item[1]["currentPosition"][pShip.GetName()]

			pInstanceDict = pInstance.__dict__
			if pInstanceDict and pInstanceDict.has_key("Warp Overriden"):
				try:
					pInstanceDict["Warp Overriden"] = None
				except:
					pass
				
		if hasattr(pInstance, "SubModelList"):
			del pInstance.SubModelList

	# Attaches the SubParts to the Body Model
	# Detach is inherited from SubModels
	def AttachParts(self, pShip, pInstance):
		debug(__name__ + ", AttachParts")
		pSet = pShip.GetContainingSet()
		pInstance.__dict__["SubModelList"] = []
		ModelList = pInstance.__dict__[self.MySystemPointer()]
		sNamePrefix = pShip.GetName() + "_"
		SubModelList = pInstance.SubModelList

		# iteeeerate over every SubModel
		for sNameSuffix in ModelList.keys():
			if sNameSuffix == "Setup":
				continue

			sFile = ModelList[sNameSuffix][0]
			sShipName = sNamePrefix + sNameSuffix
			
			# check if the ship does exist first, before create it
			pSubShip = MissionLib.GetShip(sShipName)
			if not pSubShip:
				pSubShip = loadspacehelper.CreateShip(sFile, pSet, sShipName, "")
			SubModelList.append(pSubShip)
			if len(ModelList[sNameSuffix]) > 1:
				dOptions = ModelList[sNameSuffix][1]

			# set current positions
			pSubShip.SetTranslateXYZ(dOptions["currentPosition"][pShip.GetName()][0],dOptions["currentPosition"][pShip.GetName()][1],dOptions["currentPosition"][pShip.GetName()][2])
			iNorm = math.sqrt(dOptions["currentRotation"][pShip.GetName()][0] ** 2 + dOptions["currentRotation"][pShip.GetName()][1] ** 2 + dOptions["currentRotation"][pShip.GetName()][2] ** 2)
			pSubShip.SetAngleAxisRotation(1.0,dOptions["currentRotation"][pShip.GetName()][0],dOptions["currentRotation"][pShip.GetName()][1],dOptions["currentRotation"][pShip.GetName()][2])
			pSubShip.SetScale(-iNorm + 1.85)
			pSubShip.UpdateNodeOnly()

			# save the options list
			iSaveDone = 0
			# this is here to check if we already have the entry
			for lList in pInstance.OptionsList:
				if lList[0] != "Setup":
					if lList[1]["sShipFile"] == sFile:
						lList[0] = pSubShip
						iSaveDone = 1
						break
			
			if not iSaveDone:
				pInstance.OptionsList.append([pSubShip, dOptions])
			
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

oProtoWarp = ProtoWarp("Proto-Warp")

# The class does the moving of the parts
# with every move the part continues to move
class MovingEventUpdated(MovingEvent):
	# move!
	def __call__(self):
		# if the move ID doesn't match then this move is outdated
		debug(__name__ + ", __call__")
		if self.iThisMovID != self.dOptionsList["curMovID"][self.pShip.GetName()]:
			print "Moving Error: Move no longer active"
			return 1
		
		# this makes sure the game does not crash when trying to access a deleted element
		pNacelle = App.ShipClass_GetObjectByID(None, self.iNacelleID)
		if not pNacelle:
			#print "Moving Error: Lost part"
			return 0
			
		# set new Rotation values
		self.iCurRotX = self.iCurRotX + self.iRotStepX
		self.iCurRotY = self.iCurRotY + self.iRotStepY
		self.iCurRotZ = self.iCurRotZ + self.iRotStepZ
		iNorm = math.sqrt(self.iCurRotX ** 2 + self.iCurRotY ** 2 + self.iCurRotZ ** 2)
		# set Rotation
		pNacelle.SetAngleAxisRotation(1.0, self.iCurRotX, self.iCurRotY, self.iCurRotZ)
		#pNacelle.SetScale(-iNorm + 1.85) # TO-DO CHECK IF THE SCALE DOES NOT GO BONKERS WITH THIS

		# set new Translation values
		self.iCurTransX = self.iCurTransX + self.iTransStepX
		self.iCurTransY = self.iCurTransY + self.iTransStepY
		self.iCurTransZ = self.iCurTransZ + self.iTransStepZ
		# set Translation
		pNacelle.SetTranslateXYZ(self.iCurTransX, self.iCurTransY, self.iCurTransZ)
		
		self.dOptionsList["currentRotation"][self.pShip.GetName()] = [self.iCurRotX, self.iCurRotY, self.iCurRotZ]
		self.dOptionsList["currentPosition"][self.pShip.GetName()] = [self.iCurTransX, self.iCurTransY, self.iCurTransZ]
		
		# Hardpoints
		for sHP in self.dCurHPs.keys():
			self.dCurHPs[sHP][0] = self.dCurHPs[sHP][0] + self.dHPSteps[sHP][0]
			self.dCurHPs[sHP][1] = self.dCurHPs[sHP][1] + self.dHPSteps[sHP][1]
			self.dCurHPs[sHP][2] = self.dCurHPs[sHP][2] + self.dHPSteps[sHP][2]
			UpdateHardpointPositionsTo(self.pShip, sHP, self.dCurHPs[sHP])
		
		pNacelle.UpdateNodeOnly()
		return 0

"""
#TO-DO DELETE... or improve to check things are not going awry, that is the question...
def IncCurrentMoveID(pShip, pInstance):
	debug(__name__ + ", IncCurrentMoveID")
	for item in pInstance.OptionsList:
		if item[0] == "Setup":
			item[1]["GenMoveID"][pShip.GetName()] = item[1]["GenMoveID"][pShip.GetName()] + 1


def GetCurrentMoveID(pShip, pInstance):
	debug(__name__ + ", GetCurrentMoveID")
	iGenMoveID = 0
	
	for item in pInstance.OptionsList:
		if item[0] == "Setup":
			iGenMoveID = item[1]["GenMoveID"][pShip.GetName()]
	return iGenMoveID
			

def MoveFinishMatchId(pShip, pInstance, iThisMovID):
	debug(__name__ + ", MoveFinishMatchId")
	if GetCurrentMoveID(pShip, pInstance) == iThisMovID:
		return 1
	return 0
	
"""	

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

# Prepares a ship to move: Replaces the current Model with the move Model and attaches its sub Models
def PrepareShipForProtoMove(pShip, pInstance, techType=oProtoWarp):
	debug(__name__ + ", PrepareShipForProtoMove")
	if not techType.ArePartsAttached(pShip, pInstance):
		techName = techType.MySystemPointer()
		ReplaceModel(pShip, pInstance.__dict__[techName]["Setup"]["Body"])
		techType.AttachParts(pShip, pInstance)


# called after the Alert move action
# Remove the attached parts and use the attack or normal model now
def AlertMoveFinishProtoAction(pAction, pShip, pInstance, iThisMovID, techType = oProtoWarp):
	
	# Don't switch Models back when the ID does not match
	debug(__name__ + ", AlertMoveFinishProtoAction")
	if not MoveFinishMatchId(pShip, pInstance, iThisMovID):
		return 1
	techType.DetachParts(pShip, pInstance)
	techName = techType.MySystemPointer()
	if pShip.GetAlertLevel() == 2:
		sNewShipScript = pInstance.__dict__[techName]["Setup"]["AttackModel"]
	else:
		sNewShipScript = pInstance.__dict__[techName]["Setup"]["NormalModel"]
	ReplaceModel(pShip, sNewShipScript)
	
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
	if not MoveFinishMatchId(pShip, pInstance, iThisMovID):
		return 1
		
	techP.DetachParts(pShip, pInstance)
	techName = techP.MySystemPointer()
	sNewShipScript = pInstance.__dict__[techName]["Setup"][str(move) + "Model"]
	ReplaceModel(pShip, sNewShipScript)
	return 0


# called after the warp-exit move action
# Remove the attached parts and use the attack or normal model now
def ProtoWarpExitMoveFinishAction(pAction, pShip, pInstance, iThisMovID, techP=oProtoWarp, move=oProtoWarp.MySubPositionPointer()):
	# Don't switch Models back when the ID does not match
	debug(__name__ + ", ProtoWarpExitMoveFinishAction")
	if not MoveFinishMatchId(pShip, pInstance, iThisMovID):
		if move != "Warp":
			RestoreWarpOverriden(pShip, pInstance)
		return 1
		
	techP.DetachParts(pShip, pInstance)
	techName = techP.MySystemPointer()
	if pInstance.__dict__[techName]["Setup"].has_key("AttackModel") and pShip.GetAlertLevel() == 2:
		sNewShipScript = pInstance.__dict__[techName]["Setup"]["AttackModel"]
	else:
		sNewShipScript = pInstance.__dict__[techName]["Setup"]["NormalModel"]
	ReplaceModel(pShip, sNewShipScript)

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

# Set the parts to the correct alert state
def PartsForWeaponProtoState(pShip, techP):	
	debug(__name__ + ", PartsForWeaponProtoState")
	
	if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
		return 0
	
	pInstance = FoundationTech.dShips[pShip.GetName()]
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
	if dGenShipDict["AlertLevel"][pShip.GetName()] == iType:
		return 0
	# update alert state
	dGenShipDict["AlertLevel"][pShip.GetName()] = iType
	IncCurrentMoveID(pShip, pInstance)
	
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
		iThisMovID = item[1]["curMovID"][pShip.GetName()] + 1
		item[1]["curMovID"][pShip.GetName()] = iThisMovID
	
		fDuration = 200.0
		if item[1].has_key("AttackDuration"):
			fDuration = item[1]["AttackDuration"]
		    
		# Rotation
		lStartingRotation = item[1]["currentRotation"][pShip.GetName()]
		lStoppingRotation = lStartingRotation
		if item[1].has_key("AttackRotation") and iType == 2:
			lStoppingRotation = item[1]["AttackRotation"]
		else:
			lStoppingRotation = item[1]["Rotation"]
		
		
		# Translation
		lStartingTranslation = item[1]["currentPosition"][pShip.GetName()]
		lStoppingTranslation = lStartingTranslation
		if item[1].has_key("AttackPosition") and iType == 2:
			lStoppingTranslation = item[1]["AttackPosition"]
		else:
			lStoppingTranslation = item[1]["Position"]
	
		iTime = 0.0
		iTimeNeededTotal = 0.0
		oMovingEventUpdated = MovingEventUpdated(pShip, item, fDuration, lStartingRotation, lStoppingRotation, lStartingTranslation, lStoppingTranslation, dHardpoints)
		pSeq = App.TGSequence_Create()
		
		# do the move
		while(iTime < fDuration):
			if iTime == 0.0:
				iWait = 0.5 # we wait for the first run
			else:
				iWait = 0.01 # normal step
			pSeq.AppendAction(App.TGScriptAction_Create(__name__, "MovingActionUpdated", oMovingEventUpdated), iWait)
			iTimeNeededTotal = iTimeNeededTotal + iWait
			iTime = iTime + 1
		pSeq.AppendAction(App.TGScriptAction_Create(__name__, "UpdateState", pShip, item, lStoppingRotation, lStoppingTranslation))
		pSeq.Play()
		
		# iLongestTime is for the part that needs the longest time...
		if iTimeNeededTotal > iLongestTime:
			iLongestTime = iTimeNeededTotal
		
	# finally detach
	pSeq = App.TGSequence_Create()
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "UpdateHardpointPositions", pShip, dHardpoints), iLongestTime)
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "AlertMoveFinishProtoAction", pShip, pInstance, GetCurrentMoveID(pShip, pInstance), techP), 2.0)
	pSeq.Play()


# Set the parts for Warp state
def StartingWarpE(pObject, pEvent, techP = oProtoWarp, move="Warp"):
	debug(__name__ + ", StartingWarpE")
	# Slight delay, as it is likely the special FTL methods have not yet managed to alter things to prevent entering warp
	pSeq = App.TGSequence_Create()
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "StartingWarpCommonNoDelay", pObject, pEvent, techP, move), 0.3)
	pSeq.Play()

def StartingWarpCommonNoDelay(pAction, pObject, pEvent, techP, move):
	StartingWarpCommon(pObject, pEvent, techP, move)
	return 0

# Set the parts for ProtoWarp state 
def StartingProtoWarp(pObject, pEvent, techP, move):
	debug(__name__ + ", StartingProtoWarp")
	StartingWarpCommon(pObject, pEvent, techP, move)

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
	IncCurrentMoveID(pShip, pInstance)
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
		iThisMovID = item[1]["curMovID"][pShip.GetName()] + 1
		item[1]["curMovID"][pShip.GetName()] = iThisMovID
	
		fDuration = 200.0
		
		if item[1].has_key(subPositionDuration):
			fDuration = item[1][subPositionDuration]
		    
		# Rotation
		lStartingRotation = item[1]["currentRotation"][pShip.GetName()]
		lStoppingRotation = lStartingRotation
		if item[1].has_key(subPositionRotation):
			lStoppingRotation = item[1][subPositionRotation]
		
		# Translation
		lStartingTranslation = item[1]["currentPosition"][pShip.GetName()]
		lStoppingTranslation = lStartingTranslation
		if item[1].has_key(subPositionPosition):
			lStoppingTranslation = item[1][subPositionPosition]
	
		iTime = 0.0
		iTimeNeededTotal = 0.0
		oMovingEventUpdated = MovingEventUpdated(pShip, item, fDuration, lStartingRotation, lStoppingRotation, lStartingTranslation, lStoppingTranslation, {})
		pSeq = App.TGSequence_Create()
		
		# do the move
		while(iTime < fDuration):
			if iTime == 0.0:
				iWait = 0.5 # we wait for the first run
			else:
				iWait = 0.01 # normal step
			pSeq.AppendAction(App.TGScriptAction_Create(__name__, "MovingActionUpdated", oMovingEventUpdated), iWait)
			iTimeNeededTotal = iTimeNeededTotal + iWait
			iTime = iTime + 1
		pSeq.AppendAction(App.TGScriptAction_Create(__name__, "UpdateState", pShip, item, lStoppingRotation, lStoppingTranslation))
		pSeq.Play()
		
		# iLongestTime is for the part that needs the longest time...
		if iTimeNeededTotal > iLongestTime:
			iLongestTime = iTimeNeededTotal
		
	# finally detach
	pSeq = App.TGSequence_Create()
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "UpdateHardpointPositions", pShip, dHardpoints), iLongestTime)
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "ProtoWarpStartMoveFinishAction", pShip, pInstance, GetCurrentMoveID(pShip, pInstance), techP, subPosition), 2.0)
	pSeq.Play()

	return 0

def ExitingProtoWarp(pAction, pShip, techP, subPosition):
	debug(__name__ + ", ExitingProtoWarp")
	
	if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
		debug(__name__ + ", ExitingProtoWarp Return not host")
		return 0
	
	pInstance = FoundationTech.dShips[pShip.GetName()]
	iLongestTime = 0.0
	IncCurrentMoveID(pShip, pInstance)
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
		iThisMovID = item[1]["curMovID"][pShip.GetName()] + 1
		item[1]["curMovID"][pShip.GetName()] = iThisMovID
	
		fDuration = 200.0
		if item[1].has_key(str(subPosition) + "Duration"):
			fDuration = item[1][str(subPosition) + "Duration"]
		    
		# Rotation
		lStartingRotation = item[1]["currentRotation"][pShip.GetName()]
		lStoppingRotation = lStartingRotation
		if item[1].has_key("AttackRotation") and pShip.GetAlertLevel() == 2:
				lStoppingRotation = item[1]["AttackRotation"]
		else:
			lStoppingRotation = item[1]["Rotation"]
		
		# Translation
		lStartingTranslation = item[1]["currentPosition"][pShip.GetName()]
		lStoppingTranslation = lStartingTranslation
		if item[1].has_key("AttackPosition") and pShip.GetAlertLevel() == 2:
				lStoppingTranslation = item[1]["AttackPosition"]
		else:
			lStoppingTranslation = item[1]["Position"]
	
		iTime = 0.0
		iTimeNeededTotal = 0.0
		oMovingEventUpdated = MovingEventUpdated(pShip, item, fDuration, lStartingRotation, lStoppingRotation, lStartingTranslation, lStoppingTranslation, dHardpoints)
		pSeq = App.TGSequence_Create()
		
		# do the move
		while(iTime < fDuration):
			if iTime == 0.0:
				iWait = 0.5 # we wait for the first run
			else:
				iWait = 0.01 # normal step
			pSeq.AppendAction(App.TGScriptAction_Create(__name__, "MovingActionUpdated", oMovingEventUpdated), iWait)
			iTimeNeededTotal = iTimeNeededTotal + iWait
			iTime = iTime + 1
		pSeq.AppendAction(App.TGScriptAction_Create(__name__, "UpdateState", pShip, item, lStoppingRotation, lStoppingTranslation))
		pSeq.Play()
		
		# iLongestTime is for the part that needs the longest time...
		if iTimeNeededTotal > iLongestTime:
			iLongestTime = iTimeNeededTotal
		
	# finally detach
	pSeq = App.TGSequence_Create()
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "UpdateHardpointPositions", pShip, dHardpoints), iLongestTime)
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "ProtoWarpExitMoveFinishAction", pShip, pInstance, GetCurrentMoveID(pShip, pInstance), techP, subPosition), 2.0)
	pSeq.Play()
	
	return 0
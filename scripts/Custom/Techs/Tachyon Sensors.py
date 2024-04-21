#################################################################################################################
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
#         Tachyon Sensors.py by Alex SL Gato
#         21st April 2024 TO-DO
#         Based on CloakCounterMeasures.py by Defiant. Since that file used BSD license, we need to include their license here. However, for some reason the license files are not present on the file, so we'll have to include them here:
"""
Copyright (c) 2005, Defiant All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
    * All advertising materials mentioning features or use of this software must display the following acknowledgement: This product includes software developed by the Defiant.
    * Neither the name of the Defiant nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY Defiant AS IS AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL Defiant BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. 
"""
#################################################################################################################
#
# TODO: 1. Create Read Me
#	2. Create a clear guide on how to add this...
#
# Start on 2:
# This tech is basically a help script to find and destroy cloaked ships, based on the original software developed by Defiant.
# Its purpose is to help imitate Babylon 5 sensors and communications, which are Tachyon-based and as such could have a chance to automatically detect regular cloaked vessels (with some exceptions, such as "Phase Cloak", "Torvalus Cloak", "Starcraft Cloak" or "Kyber Cloak").
# just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev.
# Please notice there's a number on the field, its purpose is to help mediate some interaction with Fool Targeting's sub-tech "Minbari Stealth", since Minbari Stealth is made to excel with Tachyon-based sensors, so regular STBC sensors 
# (multi-spectral and subspatial-based) would probably have less problems. The number is a multiplier to the sensor range required for a ship with this tech to penetrate the Minbari Stealth, and to represent some sensor quality, as for
# example Babylon 5 Station sensors may extend beyond the range of a regular Minbari Sharlin... but would they be capable of ignoring the Mibnari Cloak? Or the other way around, a ship with lower sensor range than a Sharlin, but a very
# advanced tech or targeting system that would mostly ignore it (f.ex. a Shadow Fighter Drone).
# IMPORTANT NOTE 2: This tech most likely requires of scripts/Custom/QBautostart/CloakCounterMeasures.py by Defiant for appropiate behaviour regardless (the "explosion-reveals-ship" part is already handled by that script).
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"Tachyon Sensors":  1.0
}
"""
# In order to count those "exceptions", you can add an addendum to this Tech in scripts/Custom/Techs/TachyonSensorsRebuff, creating a subScript which can regulate the chances.
#For example, let's imagine we do not want Phased Cloak vessels to be revealed by this technology... then we would add a script on that folder called "Phased Cloak". Below is such example.
"""
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 21st April 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used along with the Tachyon Sensors Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/TachyonSensorsRebuff
# As these are Sub-techs with some leeway, their manuals must be explained here.
# However, ALL of them have a thing in coommon - they must have a "chance" function and/or a "distance" multiplier function
# chance will give chances in the 0.0(impossible)-1.0(certain) range. If you don't want to affect rates, do not add this function, or return the pChance input value
# distance provides a range multiplier - If you don't want to affect distances, do not add this function, or return the pDistance input value
# In both cases, the "pSensorRange" input is the range of the ship which is scanning the others.
##################################
# SPECIFIC SUB-TECH MANUAL:
# This tech adds a modifier to the chances of being spotted by Tachyon Sensors tech while being cloaked. Specifically, it makes it impossible for a ship with
# Tachyon Sensors to spot the scanned ship.
# How-to-use:
# On this case, this is just to add something to a pre-existing tech, no special fields. However, for other technologies, it may be necessary.
####
# NOTE: Imports and additional functions may be necessary here as well, depending on how creative it becomes
import App
from bcdebug import debug
import traceback

# Some global variables could be used as well

def chance(pScannerShip, pScannedShip, pScannerInstanceDict, pScannedInstanceDict, pChance, pSensorRange):
	debug(__name__ + ", chance")
	# For Phase Cloak is simple, unconditionally undetectable by Tachyon Sensors
	return 0.0

def distance(pScannerShip, pScannedShip, pScannerInstanceDict, pScannedInstanceDict, pDistance, pSensorRange):
	debug(__name__ + ", distance")
	return pDistance
"""

MODINFO = { "Author": "\"Defiant\" erik@vontaene.de (original), \"Alex SL Gato\" andromedavirgoa@gmail.com (modified)",
	    "Version": "0.2",
	    "License": "LGPL & BSD",
	    "Description": "Read the small title above for more info"
	    }

import App

import Foundation
import FoundationTech
import loadspacehelper
import MissionLib

import nt
import math
import string

from bcdebug import debug
import traceback

dict_lockNoFirepoint = {}

ticksPerKilometer = 225/40 # 225 is approximately 40 km, so 225/40 is the number of ticks per kilometer
totalShips = 0 # We count how many ships we have with this technology.
globalCaution = 10 # 10% chance of scanning leaving a trace
variableNames = {} # Some techs may just return a number, others may return a number according to a function - this is in order to extend this tech functionality without needing to change the file

AUTO_TARGET_EXPLOSION_POINT = 1
FirePointName = "Unknown Explosion"
sFirePointScanDetectName = "Unknown Anomaly"
REMOVE_POINTER_FROM_SET = 190
NO_COLLISION_MESSAGE = 192
ET_CLIENT_SCAN = 197
dict_lockNoFirepoint = {}
FIREPOINT_LIFETIME = 10

_g_dExcludeBorgPlugins = {
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
def NiPoint3ToTGPoint3(p):
	kPoint = App.TGPoint3()
	kPoint.SetXYZ(p.x, p.y, p.z)
	return kPoint

def findShipInstance(pShip):
	pInstance = None
	try:
		pInstance = FoundationTech.dShips[pShip.GetName()]
		if pInstance == None:
			print "After looking, no pInstance for ship:", pShip.GetName(), "How odd..."
		
	except:
		#print "Error while looking for pInstance for Borg technology:"
		#traceback.print_exc()
		pass

		
	#finally:
	return pInstance

def findscriptsShipsField(pShip, thingToFind):
	thingFound = None
	pShipModule=__import__(pShip.GetScript())
	information = pShipModule.GetShipStats()
	if information != None and information.has_key(thingToFind):
		thingFound = information[thingToFind]
	return thingFound

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
	return 0

# Get the Distance between the Ship and pObject
def Distance(pShip, pObject):
	debug(__name__ + ", Distance")
	vDifference = pObject.GetWorldLocation()
	vDifference.Subtract(pShip.GetWorldLocation())

	return vDifference.Length()

def isFirepoint(pShip):
	debug(__name__ + ", isFirepoint")
	if pShip:
		return string.find(string.lower(pShip.GetName()), "firepoint")
	return -1

def DeleteFirePoint(pAction, myFirePointName):
	debug(__name__ + ", DeleteFirePoint")
	pFirepoint = MissionLib.GetShip(myFirePointName)
	if pFirepoint:
		pSet = pFirepoint.GetContainingSet()
		if pSet:
			pSet.RemoveObjectFromSet(myFirePointName)
                        
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
			for i in range(len(myFirePointName)):
				kStream.WriteChar(myFirePointName[i])
			# set the last char:
			kStream.WriteChar('\0')

			# Okay, now set the data from the buffer stream to the message
			pMessage.SetDataFromStream(kStream)

			# Send the message to everybody but me.  Use the NoMe group, which
			# is set up by the multiplayer game.
			pNetwork = App.g_kUtopiaModule.GetNetwork()
			if not App.IsNull(pNetwork):
				pNetwork.SendTGMessageToGroup("NoMe", pMessage)

			# We're done.  Close the buffer.
			kStream.CloseBuffer()
	return 0        

def DeleteFirePointAfterScan(pAction, myFirePointName):
	debug(__name__ + ", DeleteFirePointAfterScan")
	return DeleteFirePoint(pAction, myFirePointName)

def CreateScanFirepoint(pShip, pScannerShip):
	debug(__name__ + ", CreateScanFirepoint")
	pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
	pScanner = App.ShipClass_GetObjectByID(None, pShip.GetObjID())

	if not pScannerShip: # probably the player
		pScannerShip = MissionLib.GetPlayer()

	if not pScannerShip or not pShip:
		return

	pEnemies = MissionLib.GetEnemyGroup()
	pFriendlies = MissionLib.GetFriendlyGroup()
	pNeutrals = MissionLib.GetNeutralGroup()
	pTractors = MissionLib.GetTractorGroup()
        
	if pShip and pScannerShip:                
		# check group
		sameGroup = 0
		if pEnemies and pEnemies.IsNameInGroup(pShip.GetName()):
			myFirePointName = str(pScannerShip.GetObjID()) + sFirePointScanDetectName + " E" + str(pShip.GetObjID())
			group = "enemy"
			if pEnemies.IsNameInGroup(pScannerShip.GetName()):
				sameGroup = 1
				group = "tractor"
		elif pFriendlies and pFriendlies.IsNameInGroup(pShip.GetName()):
			myFirePointName = str(pScannerShip.GetObjID()) + sFirePointScanDetectName + " F" + str(pShip.GetObjID())
			group = "friendly"
			if pFriendlies.IsNameInGroup(pScannerShip.GetName()):
				sameGroup = 1
				group = "tractor"
		elif pNeutrals and pNeutrals.IsNameInGroup(pShip.GetName()):
			myFirePointName = str(pScannerShip.GetObjID()) + sFirePointScanDetectName + " N" + str(pShip.GetObjID())
			group = "neutral"
			if pNeutrals.IsNameInGroup(pScannerShip.GetName()):
				sameGroup = 1
				group = "tractor"
		else:
			myFirePointName = str(pScannerShip.GetObjID()) + sFirePointScanDetectName + " T" + str(pShip.GetObjID())
			group = "tractor"
			if pTractors and pTractors.IsNameInGroup(pScannerShip.GetName()):
				sameGroup = 1
                
		pFirePoint = MissionLib.GetShip(myFirePointName)
		FirePointCoord = None
                
		# if it does not exist we have to create it first
		if not pFirePoint:
			pFirePoint = loadspacehelper.CreateShip("Firepoint", pScannerShip.GetContainingSet(), myFirePointName, None)
			if group == "enemy" and not pEnemies.IsNameInGroup(myFirePointName):
				pEnemies.AddName(myFirePointName)
				pFriendlies.RemoveName(myFirePointName)
				pNeutrals.RemoveName(myFirePointName)
				pTractors.RemoveName(myFirePointName)
			elif group == "friendly" and not pFriendlies.IsNameInGroup(myFirePointName):
				pEnemies.RemoveName(myFirePointName)
				pFriendlies.AddName(myFirePointName)
				pNeutrals.RemoveName(myFirePointName)
				pTractors.RemoveName(myFirePointName)
			elif group == "neutral" and not pNeutrals.IsNameInGroup(myFirePointName):
				pEnemies.RemoveName(myFirePointName)
				pFriendlies.RemoveName(myFirePointName)
				pNeutrals.AddName(myFirePointName)
				pTractors.RemoveName(myFirePointName)
			elif group == "tractor" and not pTractors.IsNameInGroup(myFirePointName):
				pEnemies.RemoveName(myFirePointName)
				pFriendlies.RemoveName(myFirePointName)
				pNeutrals.RemoveName(myFirePointName)
				pTractors.AddName(myFirePointName)

			if sameGroup:
				pFirePoint.SetTargetable(0)
			else:
				pFirePoint.SetTargetable(1)

			pFirePoint.UpdateNodeOnly()

		pFirePoint = MissionLib.GetShip(myFirePointName)
                
		# reposition
		fRadius = pShip.GetHull().GetRadius() + 1
		x = 0
		y = 0
		z = 0
		if fRadius > 0:
			x = (App.g_kSystemWrapper.GetRandomNumber(fRadius) * -1**App.g_kSystemWrapper.GetRandomNumber(1))
			y = (App.g_kSystemWrapper.GetRandomNumber(fRadius) * -1**App.g_kSystemWrapper.GetRandomNumber(1))
			z = (App.g_kSystemWrapper.GetRandomNumber(fRadius) * -1**App.g_kSystemWrapper.GetRandomNumber(1))
		kLocation = App.TGPoint3()
		kLocation.SetXYZ(x, y, z)
                
		pFirePoint.SetHailable(0)
		pFirePoint.EnableCollisionsWith(pShip, 0)
		if App.g_kUtopiaModule.IsMultiplayer():
			MultiPlayerEnableCollisionWith(pFirePoint, pShip, 0)

		pFirePoint.SetCollisionsOn(0)
		pFirePoint.SetTranslate(kLocation)
		pFirePoint.UpdateNodeOnly()
		pShip.AttachObject(pFirePoint)

		if AUTO_TARGET_EXPLOSION_POINT and not pScannerShip.GetTarget() or isFirepoint(pScannerShip.GetTarget()) != -1:
			pScannerShip.SetTarget(pFirePoint.GetName())
                                
		pSeq = App.TGSequence_Create()
		pSeq.AppendAction(App.TGScriptAction_Create(__name__, "DeleteFirePointAfterScan", myFirePointName), FIREPOINT_LIFETIME)
		pSeq.Play()

def DetectCloakedShips(pAction, pShip):
	debug(__name__ + ", DetectCloakedShips")
	pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID()) # Here is the funny thing, a Tachyon Scan is intensive enough that unless the user has a tech to counter it, they will reveal themselves as well.
	if pShip:
		pSet = pShip.GetContainingSet()
		pInstance = findShipInstance(pShip)
		probability = 10
		if pInstance:
			pInsDict = pInstance.__dict__
			if pInsDict.has_key("Tachyon Sensors"):
				if pInsDict["Tachyon Sensors"] < 1.0:
					probability = 90 * ( 1.1 - pInsDict["Tachyon Sensors"])

				pSensor = pShip.GetSensorSubsystem()
				pSensorRange = 0
				distance = 0
				if pSensor and pSensor.GetSensorRange():
					pSensorRange = pSensor.GetSensorRange() * pSensor.GetConditionPercentage() * pSensor.GetPowerPercentageWanted()
					
					for paShip in pSet.GetClassObjectList(App.CT_SHIP):
						if paShip.IsCloaked():
							probabilityOne = probability
							distanceMult = 1.0
							pScannedInstance = findShipInstance(paShip)
							if pScannedInstance:
								pScannedInstanceDict = pScannedInstance.__dict__
								for techName in variableNames.keys():
									if pScannedInstanceDict.has_key(techName):
										if variableNames[techName].has_key("chance"):
											probabilityOne = variableNames[techName]["chance"](pShip, paShip, pInsDict, pScannedInstanceDict, probabilityOne, pSensorRange) # Things like custom distance will be taken care of here

										if variableNames[techName].has_key("distance"):
											distanceMult = variableNames[techName]["chance"](pShip, paShip, pInsDict, pScannedInstanceDict, distanceMult, pSensorRange) # Things like custom distance will be taken care of here

							if App.g_kSystemWrapper.GetRandomNumber(100) <= probability and pSensorRange > Distance(pShip, paShip) * distanceMult:
								CreateScanFirepoint(paShip, pShip)
	return 0

def ShipScan(pShip):
	debug(__name__ + ", ShipScan")
	pSeq = App.TGSequence_Create()
	for i in range(2):
		pSeq.AppendAction(App.TGScriptAction_Create(__name__, "DetectCloakedShips", pShip), 1)
	pSeq.Play()

def ScanInit(pObject, pEvent=None, pPlayer=None):
	debug(__name__ + ", ScanInit")
	#if pEvent and hasattr(pObject, "CallNextHandler"):
	#	pObject.CallNextHandler(pEvent)
        
	if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
		if not pPlayer:
			pPlayer = MissionLib.GetPlayer() # As far as I know, only the player can initite scans normally... if that is false, please contact Alex SL Gato.
		ShipScan(pPlayer)
	# we are client. Inform the Server that we are scanning
	else:
		if not pPlayer:
			pPlayer = MissionLib.GetPlayer()
		pMessage = App.TGMessage_Create()
		pMessage.SetGuaranteed(1)
		kStream = App.TGBufferStream()
		kStream.OpenBuffer(256)

		kStream.WriteChar(chr(ET_CLIENT_SCAN))

		# Write our ID
		kStream.WriteInt(pPlayer.GetObjID())
                
		pMessage.SetDataFromStream(kStream)
		pNetwork = App.g_kUtopiaModule.GetNetwork()
		if not App.IsNull(pNetwork):
			pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
		kStream.CloseBuffer()


# Based on LoadExtraPlugins by Dasher42, but heavily modified so it only imports a thing
def LoadExtraLimitedPlugins(dExcludePlugins=_g_dExcludeBorgPlugins):

	dir="scripts\\Custom\\Techs\\TachyonSensorsRebuff" # I want to limit any vulnerability as much as I can while keeping functionality
	import string

	list = nt.listdir(dir)
	list.sort()

	dotPrefix = string.join(string.split(dir, "\\")[1:], ".") + "."

	for plugin in list:
		s = string.split(plugin, ".")
		if len(s) <= 1:
			continue
		
		# Indexing by -1 lets us be sure we're grabbing the extension. -Dasher42
		extension = s[-1]
		fileName = string.join(s[:-1], ".")

		# We don't want to accidentally load wrong things
		if (extension == "py") and not fileName == "__init__": # I am not allowing people to just use the .pyc directly, I don't want people to not include source scripts - Alex SL Gato
			#print "Tachyon Sensors script is reviewing " + fileName + " of dir " + dir
			if dExcludePlugins.has_key(fileName):
				debug(__name__ + ": Ignoring plugin" + fileName)
				continue

			try:
				if not variableNames.has_key(fileName):
					myGoodPlugin = dotPrefix + fileName
					
					# I really wanted to make it so it only imports these two methods, but it is not letting me do it :(
					# The only other secure option I could think about is making random files with the name and those two values in the name and then splitting them up, but if there's an update you would end up with rubbish as well
					# banana = __import__(myGoodPlugin, fromlist=["defenseCounterRdm"])
					# banana = __import__(myGoodPlugin, fromlist=["defenseCounter"])

					try:
						banana = __import__(myGoodPlugin, globals(), locals(), ["chance", "distance"])
					except:
						try:
							banana = __import__(myGoodPlugin, globals(), locals(), ["chance"])
						except:
							banana = __import__(myGoodPlugin, globals(), locals(), ["distance"])

					if hasattr(banana, "chance"):
						variableNames[fileName] =  {}
						variableNames[fileName]["chance"] = banana.chance

					if hasattr(banana, "distance"):
						if not variableNames.has_key(fileName):
							variableNames[fileName] =  {}
						variableNames[fileName]["distance"] = banana.distance

					
					#print "Tachyon Sensor reviewing of this tech is a success"
			except:
				print "someone attempted to add more than they should to the Tachyon Sensor script"
				traceback.print_exc()

	


LoadExtraLimitedPlugins()
#print variableNames

tachyonShips = {} # ship IDs of ships with tachyon tech
class TachyonSensorsDef(FoundationTech.TechDef):
	def __init__(self, name):
		debug(__name__ + ", Initiated Reality Bomb counter")
		FoundationTech.TechDef.__init__(self, name)
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)

	def Attach(self, pInstance):
		pInstance.lTechs.append(self)
		#pInstance.lTorpDefense.insert(0, self)		# Important to put shield-type weapons in the front
		#pInstance.lPulseDefense.insert(0, self)
		#pInstance.lBeamDefense.insert(0, self)
		global totalShips, tachyonShips

		tachyonShips[pInstance.pShipID] = 1

		self.manualCleanup()

		if totalShips <= 0: # First time, we set it to 1 and do the InnacurateFire change
			totalShips = 1
			#App.g_kEventManager.RemoveBroadcastHandler(App.ET_WEAPON_HIT, self.pEventHandler, __name__+ ".WeaponHit") # Handled by CloakCounterMeasures.py already.
			App.g_kEventManager.RemoveBroadcastHandler(App.ET_CLOAK_BEGINNING, self.pEventHandler, "CloakStart") # Maybe we need to add ET_ENTERED_SET...
			App.g_kEventManager.RemoveBroadcastHandler(App.ET_CLOAK_COMPLETED, self.pEventHandler, "CloakDone")  # ...and ET_EXITED_SET as well
			App.g_kEventManager.RemoveBroadcastHandler(App.ET_SCAN, self.pEventHandler, "ScanInitA")

			#App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WEAPON_HIT, self.pEventHandler, __name__+ ".WeaponHit") # Handled by CloakCounterMeasures.py already.
			# adding the Firepoint in the cloaking phase seems to crash the game so avoid that
			App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_CLOAK_BEGINNING, self.pEventHandler, "CloakStart")
			App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_CLOAK_COMPLETED, self.pEventHandler, "CloakDone")
			App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_SCAN, self.pEventHandler, "ScanInitA")

		else:
			totalShips = totalShips + 1

	def Detach(self, pInstance):
		global totalShips, tachyonShips
		totalShips = totalShips - 1
		if tachyonShips.has_key(pInstance.pShipID):
			del tachyonShips[pInstance.pShipID]

		self.manualCleanup()

		if totalShips <= 0:
			#App.g_kEventManager.RemoveBroadcastHandler(App.ET_WEAPON_HIT, self.pEventHandler, __name__+ ".WeaponHit")
			App.g_kEventManager.RemoveBroadcastHandler(App.ET_CLOAK_BEGINNING, self.pEventHandler, "CloakStart") # Maybe we need to add ET_ENTERED_SET...
			App.g_kEventManager.RemoveBroadcastHandler(App.ET_CLOAK_COMPLETED, self.pEventHandler, "CloakDone")  # ...and ET_EXITED_SET as well
			App.g_kEventManager.RemoveBroadcastHandler(App.ET_SCAN, self.pEventHandler, "ScanInitA")
		pInstance.lTechs.remove(self)

	def CloakStart(self, pEvent):
		debug(__name__ + ", CloakStart")
		global dict_lockNoFirepoint
		# Get the ship that is cloaking
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
		if pShip:
			dict_lockNoFirepoint[pShip.GetObjID()] = 1
        	#pObject.CallNextHandler(pEvent)


	def CloakDone(self, pEvent):
		debug(__name__ + ", CloakDone")
		global dict_lockNoFirepoint
		# Get the ship that is cloaking
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
		if pShip and dict_lockNoFirepoint.has_key(pShip.GetObjID()):
			del dict_lockNoFirepoint[pShip.GetObjID()]
		#pObject.CallNextHandler(pEvent)
		self.CarefulScan()

	def CarefulScan(self):
		debug(__name__ + ", CarefulScan")
		global tachyonShips, globalCaution
			
		listToRemove = []
		for aShipID in tachyonShips.keys():
			aShip = App.ShipClass_GetObjectByID(None, aShipID)
			if not aShip or aShip.IsDead() or aShip.IsDying():
				listToRemove.append(aShipID)
			elif App.g_kSystemWrapper.GetRandomNumber(100) <= globalCaution: # this may be a bit expensive
				ScanInit(self, None, aShip)
			
		self.manualCleanup(listToRemove)

	def manualCleanup(self, list=None): # Just in case... this should normally clean up on its own
		debug(__name__ + ", manualCleanup")
		global tachyonShips
		listToRemove = []
		if list == None:
			for aShipID in tachyonShips.keys():
				aShip = App.ShipClass_GetObjectByID(None, aShipID)
				if not aShip or aShip.IsDead() or aShip.IsDying():
					listToRemove.append(aShipID)
		else:
			listToRemove = list

		for aShipID in listToRemove:
			try:
				del tachyonShips[aShipID]
			except:
				pass

	def ScanInitA(self, pEvent):
		ScanInit(self, pEvent, None)




oTachyonSensors = TachyonSensorsDef('Tachyon Sensors')
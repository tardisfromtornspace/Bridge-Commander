from bcdebug import debug
# MissionLib
# April 17, 2002
#
# by EvanLight aka sleight42
# All Rights Reserved
#
# Updated February 2004 by ftbUpdate team
# 18.04.2004, Defiant: Moved some stuff from ReturnShuttles
##############################################################

import App
import MissionLib
import string
import ftb.ShipManager
import ftb.LauncherManager
import ftb.LaunchShipHandlers

# Version etc
MODINFO = { "Author": "eMail: ftb@defiant.homedns.org",
            "Download": "http://defiant.homedns.org/~ftb/",
            "Version": "20050723",
            "License": "GPL",
            "Description": "script to Launch Shuttles"
            }
            
NO_COLLISION_MESSAGE = 192
VERBOSE=0

# Returns the Shiptype
def GetShipType(pShip):
        debug(__name__ + ", GetShipType")
        try:
                return string.split(pShip.GetScript(), '.')[1]
        except:
                return None


# not implemented yet
def IsMultiplayerHostAlone():
	debug(__name__ + ", IsMultiplayerHostAlone")
	return 1-App.g_kUtopiaModule.IsMultiplayer()


def LaunchShip(pLaunchShip):
	debug(__name__ + ", LaunchShip")
	pFTBCarrier = ftb.ShipManager.GetShip(pLaunchShip)

	if not hasattr(pFTBCarrier, "GetLaunchers"):
		debug(__name__ + ", LaunchShip No launchers: Return")
		return

	if pLaunchShip.IsCloaked() or pLaunchShip.IsDoingInSystemWarp(): # No we can't launch Ships while cloaked
		print("Sorry, can't launch while cloaked or warping")
		return

	pFTBLauncher = pFTBCarrier.GetLaunchers()[0]
	sShipName = pFTBLauncher.GetLaunchType()
	numLaunches =  pFTBLauncher.GetNumLaunches(sShipName)

	if numLaunches <= 0:
		print "Sorry can't launch: 0"
		return

	pFTBLauncher.LaunchShip(sShipName)
	if(pFTBLauncher.HasMoreLaunches(sShipName) == 0):
		pFTBLauncher.NextLaunchType()


def TurnShieldsOn(pAction, sShipName):
	debug(__name__ + ", TurnShieldsOn")
	pShip = MissionLib.GetShip(sShipName)
	if pShip:
		pShields = pShip.GetShields()
		if pShields:
			pShields.TurnOn()
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


##############################################################
# Adds the ship, specified by DisplayName, to the Friendly group
# sShipName - The display name of the ship to add to the Friendly group
def AddObjectToFriendlyGroup(sObjectName):
        debug(__name__ + ", AddObjectToFriendlyGroup")
        if not MissionLib.GetFriendlyGroup().IsNameInGroup(sObjectName):
                MissionLib.GetFriendlyGroup().AddName(sObjectName)


def AddObjectToEnemyGroup(sObjectName):
        debug(__name__ + ", AddObjectToEnemyGroup")
        if not MissionLib.GetEnemyGroup().IsNameInGroup(sObjectName):
                MissionLib.GetEnemyGroup().AddName(sObjectName)


def AddObjectToNeutralGroup(sObjectName):
        debug(__name__ + ", AddObjectToNeutralGroup")
        if not MissionLib.GetNeutralGroup().IsNameInGroup(sObjectName):
                MissionLib.GetNeutralGroup().AddName(sObjectName)


# broken in Bridge Commander? Looks like the game gives the same event type away several times.
# Fix arround that by adding an offset
def GetFTBNextEventType():
    debug(__name__ + ", GetFTBNextEventType")
    return App.Mission_GetNextEventType() #+ 222


#############################################################
#
# GetShuttleOEP(pShip) - This function is designed for use in
#                        mission coding, when you want to
#                        launch a ship from an AI ship
#                        and need to find the OEP
#                       
# Returns the first shuttle OEP found on pShip
# or None
# Taken from ShipScriptActions.LaunchObject and mutilated
#
#############################################################
def GetShuttleOEP(pShip):
	# Find any object emitter properties on the ship.
	debug(__name__ + ", GetShuttleOEP")
	pPropSet = pShip.GetPropertySet()
	pEmitterInstanceList = pPropSet.GetPropertiesByType(App.CT_OBJECT_EMITTER_PROPERTY)

	pEmitterInstanceList.TGBeginIteration()
	iNumItems = pEmitterInstanceList.TGGetNumItems()

	pLaunchProperty = None

	for i in range(iNumItems):
		pInstance = pEmitterInstanceList.TGGetNext()

		# Check to see if the property for this instance is a shuttle
		# emitter point.
		pProperty = App.ObjectEmitterProperty_Cast(pInstance.GetProperty())
		if (pProperty != None):
			# If we have the right type of OEP, bail now
			if (pProperty.GetEmittedObjectType() == App.ObjectEmitterProperty.OEP_SHUTTLE):
				pLaunchProperty = pProperty
				break

	pEmitterInstanceList.TGDoneIterating()
	pEmitterInstanceList.TGDestroy()

	return(pLaunchProperty)


# Here we Count the Shuttles in our Bay
# Basicly copied from the Shuttle Launching Framework by sleight42 (ftb.LaunchShipHandlers.AddLaunchButtons() )
def GetShuttlesInBay(sFiringShipName = None):
        debug(__name__ + ", GetShuttlesInBay")
        if not sFiringShipName:
            sFiringShipName = App.Game_GetCurrentPlayer().GetName()
        
        pCarrier = ftb.ShipManager.GetShip(MissionLib.GetShip(sFiringShipName))
        if not hasattr(pCarrier, "GetLaunchers"):
            return
        pLaunchers = pCarrier.GetLaunchers()
        numTypes = len( pLaunchers)
        numLaunches = 0
        for index in range( numTypes):
                launchType = pLaunchers[index].GetLaunchType()
                """if (string.find(str(launchType), 'Mine') == -1):
                        numLaunches = pLaunchers[index].GetNumLaunches( launchType)
                else:
                        numLaunches = 0"""

                launchType = pLaunchers[index].NextLaunchType()
                firstlaunchType = None
        
                i = 0
                while (launchType != firstlaunchType):
                        print launchType, pLaunchers[index].GetNumLaunches(launchType), firstlaunchType
                        if (launchType != firstlaunchType): #and string.find(str(launchType), 'Mine') == -1):
                                numLaunches =  numLaunches + pLaunchers[index].GetNumLaunches(launchType)
                        if (i == 0):
                                firstlaunchType = launchType
                        launchType = pLaunchers[index].NextLaunchType()
                        if ( i > 10 ):
                                # This makes sure the Game is not crashing if we have 0 Shuttles in Bay.
                                return 0
                        i = i + 1

	return numLaunches


def verbose_print(*lp):
	if VERBOSE: print lp


# Now the hard Work with the ftb begins!
def IncreaseShuttleCount(ShipType, sFiringShipName = None):
        debug(__name__ + ", IncreaseShuttleCount")
        verbose_print("Trying to increase Shuttle Count")

	if (sFiringShipName == None):
		verbose_print("Problem: No Firing Ship - Using Players Ship as default")
		sFiringShipName = MissionLib.GetPlayer()
	pShip = MissionLib.GetShip(sFiringShipName)
	pCarrier = ftb.ShipManager.GetShip(pShip)

        ShuttleCount = ShuttlesInBayOfThisType(ShipType, sFiringShipName)
        verbose_print("ShipType:", ShipType, "ShipCount1: ", ShuttleCount)

	sBay = GetFirstShuttleBayName(sFiringShipName)
	if hasattr(pCarrier, "dShuttleToBay") and pCarrier.dShuttleToBay.has_key(ShipType):
		sBay = pCarrier.dShuttleToBay[ShipType]
	launcher = ftb.LauncherManager.GetLauncher(sBay, pShip)
	if ShuttleCount == 0:
		launcher.AddLaunchable(ShipType, "ftb.friendlyAI", 1)
		launcher.SetClearToLaunch(1)
	else:
		launcher.AddLaunchable(ShipType, "ftb.friendlyAI", ShuttleCount + 1)
		launcher.SetClearToLaunch(1)

	# and finally reload the Button - yeah we fixed the damm Problem!
	ftb.LaunchShipHandlers.SetToggleLaunchButton()
	verbose_print("ShipCount2: ", ShuttlesInBayOfThisType(ShipType, sFiringShipName))


# just a split of the old GetShuttleBay()
def GetShuttleBaySize(pShip, pShuttle=None):
        debug(__name__ + ", GetShuttleBaySize")

	pBay = None
	pCarrier = ftb.ShipManager.GetShip(pShip)
	sShuttleType = GetShipType(pShuttle)
	
	if sShuttleType and hasattr(pCarrier, "dShuttleToBay") and pCarrier.dShuttleToBay.has_key(sShuttleType):
		sBay = pCarrier.dShuttleToBay[sShuttleType]
		pBay = MissionLib.GetSubsystemByName(pShip, sBay)
	else:
		pBay = FindAShuttleBay(pShip)
	if pBay:
		return pBay.GetRadius()
	return 0


# This make sure we don't destroy the other Shuttles in this Bay
# Its mostly the same like GetShuttlesInBay(), so also from the Shuttle Launching Framework by sleight42.
def ShuttlesInBayOfThisType(Type, sFiringShipName = None):
        debug(__name__ + ", ShuttlesInBayOfThisType")
        if (sFiringShipName == None):
                sFiringShipName = App.Game_GetCurrentPlayer().GetName()
        
        pCarrier = ftb.ShipManager.GetShip(MissionLib.GetShip(sFiringShipName))
        pLaunchers = pCarrier.GetLaunchers()
        numTypes = len( pLaunchers)
	numLaunches = 0
        for index in range( numTypes):
                launchType = None
                i = 0
                while (launchType != Type):
                        launchType = pLaunchers[index].NextLaunchType()
                        numLaunches =  pLaunchers[index].GetNumLaunches( launchType)
                        if ( i > 10 ):
                        # Stop crashing Stupid Game
                                return 0
                        i = i + 1

	return numLaunches


# Actually based on MissionLib().FindShuttleBay()
def FindAShuttleBay(pShip):
	debug(__name__ + ", FindAShuttleBay")
	iShipID = pShip.GetObjID()

	pPropSet = pShip.GetPropertySet()
	pHullPropInstanceList = pPropSet.GetPropertiesByType(App.CT_OBJECT_EMITTER_PROPERTY)
	
	pHullPropInstanceList.TGBeginIteration()
	iNumItems = pHullPropInstanceList.TGGetNumItems()
	
	pLaunchProperty = None
	
	for i in range(iNumItems):
		pInstance = pHullPropInstanceList.TGGetNext()

		pProperty = App.ObjectEmitterProperty_Cast(pInstance.GetProperty())
		if pProperty:
			if pProperty.GetEmittedObjectType() == App.ObjectEmitterProperty.OEP_SHUTTLE:
				sName = string.replace(pProperty.GetName().GetCString(), " OEP", "")
				return MissionLib.GetSubsystemByName(pShip, sName)
	
	pHullPropInstanceList.TGDoneIterating()
	pHullPropInstanceList.TGDestroy()
	return None


# How much Shuttles can we get in our Bay?
# Created by Sim Rex
def SetMaxShuttlesInBay(OurShipName):
    debug(__name__ + ", SetMaxShuttlesInBay")

    pCarrier = ftb.ShipManager.GetShip(MissionLib.GetShip(OurShipName))
    if hasattr(pCarrier, "GetMaxShuttles"):
        iMaxShuttles = pCarrier.GetMaxShuttles()
    else:
        iMaxShuttles = int(MissionLib.GetShip(OurShipName).GetHull().GetRadius()*4)
    return iMaxShuttles


# Created by Sim Rex
# Quote: Took far too long to work that out.. 
# It's a shame that the BC Python version doesn't have the very useful help() function...
# Would've saved me a lot of opening and closing of BC...
def GetOEPs(sFiringShipName = None):
        debug(__name__ + ", GetOEPs")
        if not sFiringShipName:
            sFiringShipName = App.Game_GetCurrentPlayer().GetName()
        
	pCarrier = ftb.ShipManager.GetShip(MissionLib.GetShip(sFiringShipName))
	if not hasattr(pCarrier, "GetLaunchers"):
            return
        pFTBLaunchers = pCarrier.GetLaunchers() 
	OEPList = [] 
	for launcher in pFTBLaunchers: 
		OEPs = launcher.GetLaunchers() 
		OEPList = OEPList + OEPs 
	return OEPList


# Just give me the name of our first Shuttle Bay plz:
def GetFirstShuttleBayName(sFiringShipName = None):
        debug(__name__ + ", GetFirstShuttleBayName")
        if not App.Game_GetCurrentPlayer().GetName():
                return
        if not sFiringShipName:
            sFiringShipName = App.Game_GetCurrentPlayer().GetName()

	ShuttleBayName = GetOEPs(sFiringShipName) #calling Sim Rex's Function
        if not ShuttleBayName:
            return
	return ShuttleBayName[0] # yes, thats the easy Version ;)


# next Shuttle Bay:
def GetNextShuttleBayName(sFiringShipName, LastBay):
	debug(__name__ + ", GetNextShuttleBayName")
	ShuttleBayNames = GetOEPs(sFiringShipName) #calling Sim Rex's Function
        if not ShuttleBayNames:
            return
        i = 0
        for i in range (len(ShuttleBayNames)):
                if (ShuttleBayNames[i] == LastBay):
                    if (i + 1 < len(ShuttleBayNames)):
                        return ShuttleBayNames[i + 1]
                    else:
                        return ShuttleBayNames[0]


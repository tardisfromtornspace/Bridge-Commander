from bcdebug import debug
# Many Modifications by Defiant <mail@defiant.homedns.org>

import App
import loadspacehelper
import MissionLib
import Mission10Menus
import DynamicMusic
import loadspacehelper
import Multiplayer.MissionShared
import Multiplayer.MissionMenusShared
import string
import Foundation
import Multiplayer.Episode.Mission4.Mission4Menus
from Custom.QBautostart.Libs.Races import Races
from Custom.MultiplayerExtra.Mission10.Mission10Systems import lStartingSets, CreateSystemMenuEntrys, iDefaultStartingSet
from Multiplayer.Episode.Mission4.Mission4 import dReplaceModel
from Custom.MultiplayerExtra.MultiplayerLib import CreateMessageStream, SendMessageToEveryone

# print("Loading multiplayer mission5)

#global variables
NonSerializedObjects = (
"g_kKillsDictionary",
"g_kDeathsDictionary",
"g_kScoresDictionary",
"g_kDamageDictionary",
"g_kTeamDictionary",
"g_kTeamScoreDictionary",
"g_kTeamKillsDictionary",
"g_pTeam1",
"g_pTeam2",
"gdShipAttrs",
)

# Global variables.  

# setup scoring objects
g_kKillsDictionary = {}
g_kDeathsDictionary = {}
g_kScoresDictionary = {}
g_kDamageDictionary = {}
g_kTeamDictionary = {}
g_kTeamScoreDictionary = {}
g_kTeamKillsDictionary = {}
g_lTeams = []
g_bEndCutsceneStarted = 0
dict_Collisions = {}
g_lFirepoints = []

# define some messages.  Start at 20 for mission specific message types
SCORE_INIT_MESSAGE = App.MAX_MESSAGE_TYPES + 20
TEAM_SCORE_MESSAGE = App.MAX_MESSAGE_TYPES + 21
TEAM_MESSAGE = App.MAX_MESSAGE_TYPES + 22
ADD_AI_TO_TEAM_MSG = App.MAX_MESSAGE_TYPES + 23
CLIENT_OBJECT_DESTROYED = App.MAX_MESSAGE_TYPES + 54
REMOVE_POINTER_FROM_SET = 190
REMOVE_TORP_MESSAGE_AT = 191
NO_COLLISION_MESSAGE = 192
DISABLE_TRACTOR_MESSAGE = 193 # not used here but exist
SUBSYSTEM_SET_CONDITION = 194
MP_SET_TRACTOR_MODE = 195
SET_SCRIPT_MSG = 196
ET_CLIENT_SCAN = 197
MP_REMOTE_CONTROL_MSG = 198
SET_SHIELD_CONDITION = 199
MP_SET_POSITION_MSG = 200
MP_SEND_PLASMA_FX = 202
PLAYER_NOW_USING_SHIP = 203
REPLACE_MODEL_MSG = 208
SET_TARGETABLE_MSG = 209
ALERT_STATE_CHANGED_MSG = 210
DELETE_OBJECT_FROM_SET_MSG = 211
SET_GET_SHIP_ATTR_MSG = 212
SET_AUTO_AI_MSG = 213
SET_STOP_AI_MSG = 214
TRACTOR_STARTED_MSG = 215
MP_SET_TARGET_MSG = 216

# Invalid team number
INVALID_TEAM = 255
curShipNum = 1
dict_Ship_to_Group = {}
dict_Probes = {}
gdShipAttrs = {}



def SendTargetChanged(pShip):
	debug(__name__ + ", SendTargetChanged")
	
	if pShip:
		pMessage, kStream = CreateMessageStream(MP_SET_TARGET_MSG)
		kStream.WriteInt(pShip.GetObjID())
		if pShip.GetTarget():
			kStream.WriteInt(pShip.GetTarget().GetObjID())
		else:
			kStream.WriteInt(0)
		SendMessageToEveryone(pMessage, kStream)


###############################################################################
#	GetWinString()
#	
#	Returns a string that describes who won
#	
#	Args:	None
#	
#	Return:	char*
###############################################################################
def GetWinString():
	debug(__name__ + ", GetWinString")
	pFBCMPDatabase = App.g_kLocalizationManager.Load("data/TGL/FBCMP.tgl")
	
	# Play the appropriate win/lose fanfare
	if g_bStarbaseDead:
		if Mission10Menus.g_iTeam == 0:
			DynamicMusic.PlayFanfare("Win")
		else:
			DynamicMusic.PlayFanfare("Lose")
	else:
		if Mission10Menus.g_iTeam == 0:
			DynamicMusic.PlayFanfare("Lose")
		else:
			DynamicMusic.PlayFanfare("Win")

	if g_bStarbaseDead:
		return pFBCMPDatabase.GetString("PlayersWin").GetCString()
	else:
		return pFBCMPDatabase.GetString("AIShipsWin").GetCString()

# Kill the Mission database
# Heavily edited by Defiant
def Terminate(pMission):
	# print("Terminating multiplayer mission 4.")
	
	debug(__name__ + ", Terminate")
	global g_lTeams, curShipNum
	global g_kKillsDictionary 
	global g_kDeathsDictionary 
	global g_kScoresDictionary 
	global g_kDamageDictionary 
	global g_kTeamDictionary 
	global g_kTeamScoreDictionary 
	global g_kTeamKillsDictionary 
        
        import Multiplayer.MissionShared
	pDatabase = Multiplayer.MissionShared.g_pDatabase

	# Delete group2.
	g_lTeams = None
        pEnemyGroup = MissionLib.GetEnemyGroup()
        pFriendlyGroup = MissionLib.GetFriendlyGroup()
        pEnemyGroup = None
        pFriendlyGroup = None
	
	# Terminate common stuff, which will handle delete of mission
	# menus as well.
	Multiplayer.MissionShared.Terminate (pMission)

	# Clear dictionaries
	for iKey in g_kKillsDictionary.keys ():
		del g_kKillsDictionary[iKey]		

	for iKey in g_kDeathsDictionary.keys ():
		del g_kDeathsDictionary[iKey]		

	for iKey in g_kScoresDictionary.keys ():
		del g_kScoresDictionary[iKey]		

	for iKey in g_kDamageDictionary.keys ():
		del g_kDamageDictionary[iKey]		

	for iKey in g_kTeamDictionary.keys ():
		del g_kTeamDictionary[iKey]		

	for iKey in g_kTeamKillsDictionary.keys ():
		del g_kTeamKillsDictionary[iKey]		

	for iKey in g_kTeamScoreDictionary.keys ():
		del g_kTeamScoreDictionary[iKey]		

	Mission10Menus.g_fYPixelOffset = 0.0
	Mission10Menus.g_fXPixelOffset = 0.0

	Mission10Menus.g_iTeam = 0
	Mission10Menus.g_iIdOfCurrentlySelectedPlayer = App.TGNetwork.TGNETWORK_INVALID_ID

	# Global pointers to user interface items
	Mission10Menus.g_pTeamButton = None
	Mission10Menus.g_pOptionsWindowBootButton = None
	Mission10Menus.g_pOptionsWindowPlayerMenu = None

        curShipNum = 1
        
        # Foundation deactivate
        if Mission10Menus.qbGameMode:
		if Mission10Menus.QBGameModeActivated:
                	Mission10Menus.qbGameMode.Deactivate()
                Mission10Menus.qbGameMode = None
        Mission10Menus.StartMissionRunOnce = 0
	Mission10Menus.QBGameModeActivated = 0
	Mission10Menus.BridgeStartOnce = 0


#Episode level stuff
def CreateMenus():
	debug(__name__ + ", CreateMenus")
	return 0


def RemoveHooks():
	debug(__name__ + ", RemoveHooks")
	return


###############################################################################
#	PreLoadAssets()
#	
#	This is called once, at the beginning of the mission before Initialize()
#	to allow us to add models to be pre loaded
#	
#	Args:	pMission	- the Mission object
#	
#	Return:	none
###############################################################################
def PreLoadAssets(pMission):
	debug(__name__ + ", PreLoadAssets")
	return


#Mission startup
def Initialize(pMission):
        # Set the difficulty level.
        debug(__name__ + ", Initialize")
        App.Game_SetDifficultyMultipliers(1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        
        # Make sure Engineering Extension is not loaded yet.
        Mission10Menus.LoadQBautostart(0)
        
        # print("Multiplayer mission start.")
	# Call common initialize routine
        #import Multiplayer.MissionShared
	#Multiplayer.MissionShared.Initialize(pMission)
	import LoadBridge
	LoadBridge.CreateCharacterMenus()
	### MissionShared start
	# Load database
	Multiplayer.MissionShared.g_pDatabase = App.g_kLocalizationManager.Load("data/TGL/Multiplayer.tgl")
	Multiplayer.MissionShared.g_pShipDatabase = App.g_kLocalizationManager.Load("data/TGL/Ships.tgl")
	Multiplayer.MissionShared.g_pSystemDatabase = App.g_kLocalizationManager.Load("data/TGL/Systems.tgl")

	#Setup event handlers
	#Multiplayer.MissionShared.SetupEventHandlers(pMission)
	
	Multiplayer.MissionShared.g_idTimeLeftTimer = App.NULL_ID
	Multiplayer.MissionShared.g_bGameOver = 0
	Multiplayer.MultiplayerMenus.g_bExitPressed = 0

	# Load string database
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Crew General.tgl")
	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pDatabase, "MiguelScan", "BridgeGeneric")
	pGame.LoadDatabaseSoundInGroup(pDatabase, "gs038", "BridgeGeneric")
	App.g_kLocalizationManager.Unload(pDatabase)
	# Now we're done.  The menu will do the work to create the ship.
	### MissionShared end

	global g_bStarbaseDead
	g_bStarbaseDead = 0

	if (App.g_kUtopiaModule.IsHost()):	
		Mission10Menus.BuildMission10Menus()

	#Setup event handlers
	SetupEventHandlers(pMission)

	if (App.g_kUtopiaModule.IsHost() and App.g_kUtopiaModule.IsClient()):
		pNetwork = App.g_kUtopiaModule.GetNetwork()
		iPlayerID = pNetwork.GetHostID()

		if (not g_kKillsDictionary.has_key(iPlayerID)):
			# Add a blank key
			global g_kKillsDictionary
			g_kKillsDictionary[iPlayerID] = 0		# No kills

		if (not g_kDeathsDictionary.has_key(iPlayerID)):
			# Add a blank key
			global g_kDeathsDictionary
			g_kDeathsDictionary[iPlayerID] = 0		# No kills

	# Initialize team scores for two teams
	for key in g_kTeamScoreDictionary.keys():
		g_kTeamScoreDictionary[key] = 0

	# Create the group of Team1 Name for the Ships AI
	global g_lTeams
	g_lTeams = []
	for iTeam in range(len(Races.keys())):
		g_lTeams.append(App.ObjectGroupWithInfo())


def ProbeLaunched(pObject, pEvent):
        debug(__name__ + ", ProbeLaunched")
        global dict_Probes

        list = []
        pProbe = App.ShipClass_Cast(pEvent.GetSource())
        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if not pProbe or not pShip:
                return
        
        pLaunchingShipID = pShip.GetNetPlayerID()

        if dict_Probes.has_key(pLaunchingShipID):
                for Probe in dict_Probes[pLaunchingShipID]:
                        list.append(Probe)
        list.append(pProbe.GetName())

        dict_Probes[pLaunchingShipID] = list
        
        pObject.CallNextHandler(pEvent)


def SendSubsystemCondition(iShipObjID, sSubsystenName, iNewCondition):
        # Setup the stream.
        # Allocate a local buffer stream.
        debug(__name__ + ", SendSubsystemCondition")
        kStream = App.TGBufferStream()
        # Open the buffer stream with a byte buffer.
        kStream.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)
        # Write relevant data to the stream.
        # First write message type.
        kStream.WriteChar(chr(SUBSYSTEM_SET_CONDITION))
        
        # send Message
        kStream.WriteInt(iShipObjID)
        for i in range(len(sSubsystenName)):
                kStream.WriteChar(sSubsystenName[i])
        # set the last char:
        kStream.WriteChar('\0')
        kStream.WriteInt(iNewCondition)

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


def DamageShip(pShip, kLocation, fRadius, fDamage):
	debug(__name__ + ", DamageShip")
	pPropSet = pShip.GetPropertySet()
        pShipSubSystemPropInstanceList = pPropSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
        iNumItems = pShipSubSystemPropInstanceList.TGGetNumItems()
	
	pShipSubSystemPropInstanceList.TGBeginIteration()
	for i in range(iNumItems):
		pInstance = pShipSubSystemPropInstanceList.TGGetNext()
		pProperty = App.SubsystemProperty_Cast(pInstance.GetProperty())
		pSubsystem = pShip.GetSubsystemByProperty(pProperty)
		fNewCondition = None
		# Get Distance between Points
		vDifference = pSubsystem.GetWorldLocation()
		vDifference.Subtract(kLocation)
		fPointDist = vDifference.Length()
                # check Radius: if they overlap => Damage
		fDamageDist = pSubsystem.GetRadius() + fRadius
		
                # Damage for the Hull works a bit different
                if pSubsystem.GetName() == pShip.GetHull().GetName():
                        fdiff = pShip.GetHull().GetRadius() - fRadius / 5.0
                        if fdiff > 0.0:
                                fDamageTodo = fdiff * fDamage
                                fNewCondition = pSubsystem.GetCondition() - fDamageTodo
                        else:
                                fNewCondition = 0.0
                        
		elif fPointDist <= fDamageDist:
			# Damage Subsystem according to distance (linear)
			fDamagePercent = (0.0 - fDamage) / (fRadius - 0.0)
			# mx + b
			fDamageTodo = fDamagePercent * fPointDist / 5.0 + fDamage
			fNewCondition = pSubsystem.GetCondition() - fDamageTodo

                if fNewCondition:
                        if not App.g_kUtopiaModule.IsHost():
                                SendSubsystemCondition(pShip.GetObjID(), pSubsystem.GetName(), fNewCondition)
                        else:
			        if fNewCondition <= 0.0:
				        pShip.DestroySystem(pSubsystem)
                                else:
			                pSubsystem.SetCondition(fNewCondition)
		
	pShipSubSystemPropInstanceList.TGDoneIterating()


def ObjectCollisionHandler(pObject, pEvent):
        # Ai Ships doesn't seem to get collision damage: this is a work around
        debug(__name__ + ", ObjectCollisionHandler")
        global dict_Collisions

	pObjectHitting	= App.ObjectClass_Cast(pEvent.GetSource())
	pObjectHit	= App.ObjectClass_Cast(pEvent.GetDestination())

        pShip1 = App.ShipClass_Cast(pObjectHitting)
        pShip2 = App.ShipClass_Cast(pObjectHit)
        
        if pShip1:
                if dict_Collisions.has_key(pShip1.GetName()):
                        for lDamagePoint in dict_Collisions[pShip1.GetName()]:
                                kLocation = lDamagePoint[0]
                                fDamage = lDamagePoint[1]
                                fRadius = pShip1.GetHull().GetRadius()
                                
				if pShip2:
                                	DamageShip(pShip2, kLocation, fRadius, fDamage)
				elif dict_Collisions.has_key(pShip1.GetName()):
                                	del dict_Collisions[pShip1.GetName()]
                if pShip2:
                        # AI AI Collisions
                        if pShip1.GetNetPlayerID() < 0 and pShip2.GetNetPlayerID() < 0:
                                if pShip1.GetHull().GetCondition() > pShip2.GetHull().GetCondition():
                                        pShip1.GetHull().SetCondition(pShip1.GetHull().GetCondition() - pShip2.GetHull().GetCondition() * 5)
                                        if pShip1.GetHull().GetCondition() <= 0.0:
                                                pShip1.DestroySystem(pShip1.GetHull())
                                        pShip2.DestroySystem(pShip2.GetHull())
                                elif pShip1.GetHull().GetCondition() < pShip2.GetHull().GetCondition():
                                        pShip2.GetHull().SetCondition(pShip2.GetHull().GetCondition() - pShip1.GetHull().GetCondition())
                                        pShip1.DestroySystem(pShip1.GetHull())
                                else:
                                        pShip1.DestroySystem(pShip1.GetHull())
                                        pShip2.DestroySystem(pShip2.GetHull())

        if pShip2:
                if not pObjectHitting:
                        # ok, we have a ship that was hit, but not a ship that is the hitter
                        # good chane, that the hitter is AI ship
                        dict_Collisions[pShip2.GetName()] = []
                        for i in range(pEvent.GetNumPoints()):
                                dict_Collisions[pShip2.GetName()].append([pEvent.GetPoint(i), pEvent.GetCollisionForce()])

	pObject.CallNextHandler(pEvent)
	

def TractorBeamOn(pObject, pEvent):
	debug(__name__ + ", TractorBeamOn")
	pTractorProjector	= App.TractorBeamProjector_Cast(pEvent.GetSource())
	pTractorSystem		= App.TractorBeamSystem_Cast(pTractorProjector.GetParentSubsystem())
	pShip 			= pTractorSystem.GetParentShip()
	pTarget 		= App.ShipClass_Cast(pEvent.GetDestination())
	
	if pShip and pTarget:
		kStream = App.TGBufferStream()
        	# Open the buffer stream with a 256 byte buffer.
        	kStream.OpenBuffer(256)
        	# Write relevant data to the stream.
        	# First write message type.
        	kStream.WriteChar(chr(TRACTOR_STARTED_MSG))

		# send Message
		kStream.WriteInt(pShip.GetObjID())
		kStream.WriteInt(pTarget.GetObjID())

        	pMessage = App.TGMessage_Create()
        	# Yes, this is a guaranteed packet
        	pMessage.SetGuaranteed(1)
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
	
	pObject.CallNextHandler(pEvent)


def TorpedoFiredPlaySound(pObject, pEvent):
	pObject.CallNextHandler(pEvent)

        pTorp = App.Torpedo_Cast(pEvent.GetDestination())
        if not pTorp:
                return
	pPlayer = MissionLib.GetPlayer()
	if not pPlayer:
		return
	pSet = pPlayer.GetContainingSet()
	if not pSet:
		return

	pcLaunchSound = pTorp.GetLaunchSound()
	if pcLaunchSound != None:
		pSound = App.g_kSoundManager.GetSound(pcLaunchSound)
		if pSound != None:
			pSound.AttachToNode(pTorp.GetNode())

			# Associate this sound with the sound region for the set we're in.
			pSoundRegion = App.TGSoundRegion_GetRegion(pSet.GetName())
			if pSoundRegion != None:
				pSoundRegion.AddSound(pSound)

			pSound.Play()


# setup any event handlers specific to this mission.
def SetupEventHandlers(pMission):
        debug(__name__ + ", SetupEventHandlers")
        if App.g_kUtopiaModule.IsHost():
                # Only hosts handling scoring.
                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WEAPON_HIT, pMission, __name__ + ".DamageEventHandler")
                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectKilledHandler")
        else:
                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectKilledHandlerClient")
        
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_NEW_PLAYER_IN_GAME, pMission, __name__ + ".NewPlayerHandler")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_NETWORK_DELETE_PLAYER, pMission, __name__ + ".DeletePlayerHandler")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_CREATED_NOTIFY, pMission, __name__ + ".ObjectCreatedHandler")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_NETWORK_NAME_CHANGE_EVENT, pMission, __name__ + ".ProcessNameChangeHandler")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_COLLISION, pMission, __name__ + ".ObjectCollisionHandler")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SET_ALERT_LEVEL, pMission, __name__ + ".AlertStateChanged")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TRACTOR_BEAM_STARTED_HITTING, pMission, __name__+ ".TractorBeamOn")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TORPEDO_ENTERED_SET, MissionLib.GetMission(), __name__+ ".TorpedoFiredPlaySound")

	# setup handler for listening for packets.
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_NETWORK_MESSAGE_EVENT, pMission, __name__ + ".ProcessMessageHandler")

        import Multiplayer.MissionShared
	pMission.AddPythonFuncHandlerForInstance(Multiplayer.MissionShared.ET_RESTART_GAME, __name__ + ".RestartGameHandler")

        if App.g_kUtopiaModule.IsHost():
                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_LAUNCH_PROBE, pMission, __name__+ ".ProbeLaunched")


def AlertStateChanged(pObject, pEvent):
	debug(__name__ + ", AlertStateChanged")
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	
	if pShip:
		kStream = App.TGBufferStream()
        	# Open the buffer stream with a 256 byte buffer.
        	kStream.OpenBuffer(256)
        	# Write relevant data to the stream.
        	# First write message type.
        	kStream.WriteChar(chr(ALERT_STATE_CHANGED_MSG))

		# send Message
		kStream.WriteInt(pShip.GetObjID())
		kStream.WriteInt(pShip.GetAlertLevel())

        	pMessage = App.TGMessage_Create()
        	# Yes, this is a guaranteed packet
        	pMessage.SetGuaranteed(1)
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

	pObject.CallNextHandler(pEvent)


def ProcessNameChangeHandler(self, pEvent):
        debug(__name__ + ", ProcessNameChangeHandler")
        import Multiplayer.MissionMenusShared
	if (Multiplayer.MissionMenusShared.g_pInfoPane != None):
		# A player's name has changed.  Rebuild the info pane.
		Mission10Menus.RebuildInfoPane()
	self.CallNextHandler(pEvent)


def ProcessMessageHandler(self, pEvent):
        debug(__name__ + ", ProcessMessageHandler")
        global g_lTeams, dict_Ship_to_Group
        import Multiplayer.MissionShared
        import Multiplayer.MissionMenusShared
	pMission = MissionLib.GetMission()
	if (pMission == None):
		# Mission is over, don't process messages.
		return

	pMessage = pEvent.GetMessage()
	if not App.IsNull(pMessage):
		# Get the data from the message
		# Open a buffer stream to read the data
		kStream = pMessage.GetBufferStream();

		cType = kStream.ReadChar();

		cType = ord(cType)

		if (cType == Multiplayer.MissionShared.MISSION_INIT_MESSAGE):
			# print("Process mission init message")

			# Read the max number of players
			Multiplayer.MissionMenusShared.g_iPlayerLimit = ord(kStream.ReadChar())

			iNum = ord (kStream.ReadChar())
			if (iNum == 255):
				Multiplayer.MissionMenusShared.g_iTimeLimit = -1
			else:
				Multiplayer.MissionMenusShared.g_iTimeLimit = iNum
				iEndTime = kStream.ReadInt()
				Multiplayer.MissionShared.CreateTimeLeftTimer(iEndTime - int(App.g_kUtopiaModule.GetGameTime()))

			iNum = ord (kStream.ReadChar ())
			if (iNum == 255):
				Multiplayer.MissionMenusShared.g_iFragLimit = -1
			else:
				Multiplayer.MissionMenusShared.g_iFragLimit = iNum

			# Systems
			iDefaultStartingSet = kStream.ReadInt()
			pSet = Mission10Menus.CreateSystemFromSpecies(iDefaultStartingSet)
			Mission10Menus.dSets[iDefaultStartingSet] = pSet
			lStartingSets = []
                        while(1):
                                iRace = kStream.ReadInt()
                                if iRace == -1:
                                        break
				iSystem = kStream.ReadInt()
				sRace = Races.keys()[iRace]
				Races[sRace].iStartingSet = iSystem
				lStartingSets.append(iSystem)
                                pSet = Mission10Menus.CreateSystemFromSpecies(iSystem)
				Mission10Menus.dSets[iSystem] = pSet
			while(1):
				iSystem = kStream.ReadInt()
				if iSystem == -1:
					break
				lStartingSets.append(iSystem)
				pSet = Mission10Menus.CreateSystemFromSpecies(iSystem)
				Mission10Menus.dSets[iSystem] = pSet

			# Ships
			# clear old settings first
			for iIndex in range(1, Multiplayer.SpeciesToShip.MAX_SHIPS):
				sShipScript = Multiplayer.SpeciesToShip.GetScriptFromSpecies(iIndex)
				sRace = GetRaceFromShipType(sShipScript)
				if Races.has_key(sRace):
					Races[sRace].SetNumFreeShips(sShipScript, 0)
			
			# get new available ships
			while(1):
				iShip = kStream.ReadInt()
				if iShip == -1:
					break
				iNum = kStream.ReadInt()
				sShipScript = Multiplayer.SpeciesToShip.GetScriptFromSpecies(iShip)
				sRace = GetRaceFromShipType(sShipScript)
				if Races.has_key(sRace):
					Races[sRace].SetNumFreeShips(sShipScript, iNum)

			# Create the system
			# print("Creating system")
			Mission10Menus.BuildMission10Menus()

			# Update info
			Mission10Menus.ResetLimitInfo()
			Mission10Menus.RebuildInfoPane()
		elif (cType == Multiplayer.MissionShared.SCORE_CHANGE_MESSAGE):
			# print("Process score change message")

			global g_kScoresDictionary

			# Read the player id of killer
			iFiringPlayerID = kStream.ReadLong()

			iKills = 0
			if (iFiringPlayerID != 0):
				# Read the kills
				iKills = kStream.ReadLong()

				# Read the firing player's score
				g_kScoresDictionary[iFiringPlayerID] = kStream.ReadLong()

			# Read the player id of killed
			iKilledPlayerID = kStream.ReadLong()

			# Read the deaths
			iDeaths = kStream.ReadLong()

			# Read the number of players
			iScoreCount = ord(kStream.ReadChar())
			# print("Received " + str (iScoreCount) + "scores")

			while (iScoreCount > 0):
				iPlayerID = kStream.ReadLong()
				if (iPlayerID != 0):
					iPlayerScore = kStream.ReadLong()

					g_kScoresDictionary [iPlayerID] = iPlayerScore
				iScoreCount = iScoreCount - 1

			UpdateScore(iFiringPlayerID, iKills, iKilledPlayerID, iDeaths)

		elif (cType == Multiplayer.MissionShared.SCORE_MESSAGE):
			# print("Process score message")

			global g_kKillsDictionary
			global g_kDeathsDictionary
			global g_kScoresDictionary


			# Read the key id.
			iKey = kStream.ReadLong()

			# Read Kills
			iKills = kStream.ReadLong()

			# Read deaths
			iDeaths = kStream.ReadLong()
			
			# Read score
			iScore = kStream.ReadLong ()
			
			g_kKillsDictionary[iKey] = iKills
			g_kDeathsDictionary[iKey] = iDeaths
			g_kScoresDictionary[iKey] = iScore

			Mission10Menus.RebuildPlayerList()

		elif (cType == Multiplayer.MissionShared.RESTART_GAME_MESSAGE):
			print("Process restart game message")
			RestartGame()
                        
		elif (cType == SCORE_INIT_MESSAGE):
			# print("Process score init message")

			global g_kKillsDictionary
			global g_kDeathsDictionary
			global g_kScoresDictionary
			global g_kTeamDictionary

			# Read the key id.
			iKey = kStream.ReadLong()

			# Read Kills
			iKills = kStream.ReadLong()

			# Read deaths
			iDeaths = kStream.ReadLong()
			
			# Read score
			iScore = kStream.ReadLong()
			
			# Read score
			iTeam = kStream.ReadChar()
			iTeam = ord(iTeam)
			
			g_kKillsDictionary[iKey] = iKills
			g_kDeathsDictionary[iKey] = iDeaths
			g_kScoresDictionary[iKey] = iScore
			g_kTeamDictionary[iKey] = iTeam

			Mission10Menus.RebuildPlayerList()

		elif (cType == TEAM_MESSAGE):
			# print("Process team message")
			global g_kTeamDictionary

			iKey = kStream.ReadLong()
			iTeam = kStream.ReadChar()
			iTeam = ord(iTeam)

			g_kTeamDictionary[iKey] = iTeam
                        
			if (App.g_kUtopiaModule.IsHost()):
				# If I'm the host, I have to forward this information to
				# everybody else so they'll know what team this player is on
				pNetwork = App.g_kUtopiaModule.GetNetwork()
				if (pNetwork):
					pCopyMessage = pMessage.Copy()
					pNetwork.SendTGMessageToGroup("NoMe", pCopyMessage)

			Mission10Menus.RebuildPlayerList()

                # Msg from Host that a new Ship has been added and belongs to a Group.
                elif (cType == ADD_AI_TO_TEAM_MSG):
                        iName = ""
                        while(1):
                                iChar = kStream.ReadChar()
                                if iChar == '\0':
                                        break
                                iName = iName + iChar
                        iValue = kStream.ReadLong()
                        
                        # check if this ship already exists
                        pShip = MissionLib.GetShip(iName)
                        if pShip:
                                pShip.SetNetPlayerID(iValue)
				if iValue < 0:
					iGroup = iValue * -1
					AddNameToGroup(g_lTeams[iGroup], pShip.GetName())
					RemoveNameFromAllGroupsBut(iGroup, pShip.GetName())
					ResetEnemyFriendlyGroups()
                        # else wait before it is created
                        else:
                                dict_Ship_to_Group[iName] = iValue
                        
                        
                        if App.g_kUtopiaModule.IsHost():
                                SendGroupInfo(iName, iValue)

                elif cType == CLIENT_OBJECT_DESTROYED:
                        # Read the player id of killer
                        ObjectDestroyed = ""
                        while(1):
                                iChar = kStream.ReadChar()
                                if iChar == '\0':
                                        break
                                ObjectDestroyed = ObjectDestroyed + iChar
                        #print(ObjectDestroyed, "has been killed (client msg)")
                        pDestroyedShip = MissionLib.GetShip(ObjectDestroyed)
                        # finally kill it
                        if pDestroyedShip:
                                pDestroyedShip.DestroySystem(pDestroyedShip.GetHull())
                
                elif cType == REMOVE_POINTER_FROM_SET:
                        ObjectRemoved = ""
                        while(1):
                                iChar = kStream.ReadChar()
                                if iChar == '\0':
                                        break
                                ObjectRemoved = ObjectRemoved + iChar
                        #print(ObjectRemoved, "Removing Pointer")
                        
                        # Host: send message to others
                        pNetwork = App.g_kUtopiaModule.GetNetwork()
                        if App.g_kUtopiaModule.IsHost() and pNetwork:
                                # Now send a message to everybody else that the score was updated.
                                # allocate the message.
                                pMessage2 = App.TGMessage_Create()
                                pMessage2.SetGuaranteed(1)		# Yes, this is a guaranteed packet
                        
                                # Setup the stream.
                                kStream2 = App.TGBufferStream()		# Allocate a local buffer stream.
                                kStream2.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
	
                                # Write relevant data to the stream.
                                # First write message type.
                                kStream2.WriteChar(chr(REMOVE_POINTER_FROM_SET))
                                        
                                for i in range(len(ObjectRemoved)):
                                        kStream2.WriteChar(ObjectRemoved[i])
                                # set the last char:
                                kStream2.WriteChar('\0')

                                # Okay, now set the data from the buffer stream to the message
                                pMessage2.SetDataFromStream(kStream2)

                                # Send the message to everybody but me.  Use the NoMe group, which
                                # is set up by the multiplayer game.
                                pNetwork.SendTGMessageToGroup("NoMe", pMessage2)
                                # We're done.  Close the buffer.
                                kStream2.CloseBuffer()
                        
                        pPointerRemoved = MissionLib.GetShip(ObjectRemoved)
                        if pPointerRemoved:
                                pPointerRemoved.GetContainingSet().RemoveObjectFromSet(ObjectRemoved)
                
                elif cType == REMOVE_TORP_MESSAGE_AT:
                        SenderHostID = kStream.ReadInt()
                        
                        kLocation = App.TGPoint3()
                        posX = kStream.ReadFloat()
                        posY = kStream.ReadFloat()
                        posZ = kStream.ReadFloat()
                        
                        kLocation.SetXYZ(posX, posY, posZ)
                        
                        minD = 10
                        pTorpminD = None
                        pPlayer = MissionLib.GetPlayer()
                        if pPlayer:
                                pSet = pPlayer.GetContainingSet()
                                lObjects = pSet.GetClassObjectList(App.CT_TORPEDO)
                                for pObject in lObjects:
                                        pTorp = App.Torpedo_GetObjectByID(None, pObject.GetObjID())
                                        vDifference = pTorp.GetWorldLocation()
                                        vDifference.Subtract(kLocation)
                                        if vDifference.Length() < minD:
                                                minD = vDifference.Length()
                                                pTorpminD = pTorp
                        
                        pNetwork = App.g_kUtopiaModule.GetNetwork()
                        if pTorpminD and pNetwork and SenderHostID != pNetwork.GetLocalID():
                                pTorpminD.SetLifetime(0.9)
                                # Host: send message to others
                                if App.g_kUtopiaModule.IsHost():
                                        # Now send a message to everybody else that the score was updated.
                                        # allocate the message.
                                        pMessage2 = App.TGMessage_Create()
                                        pMessage2.SetGuaranteed(1)		# Yes, this is a guaranteed packet
                        
                                        # Setup the stream.
                                        kStream2 = App.TGBufferStream()		# Allocate a local buffer stream.
                                        kStream2.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
	
                                        # Write relevant data to the stream.
                                        # First write message type.
                                        kStream2.WriteChar(chr(REMOVE_TORP_MESSAGE_AT))
                                        
                                        kStream2.WriteInt(SenderHostID)
                                        kStream2.WriteFloat(pTorpminD.GetWorldLocation().GetX())
                                        kStream2.WriteFloat(pTorpminD.GetWorldLocation().GetY())
                                        kStream2.WriteFloat(pTorpminD.GetWorldLocation().GetZ())

                                        # Okay, now set the data from the buffer stream to the message
                                        pMessage2.SetDataFromStream(kStream2)

                                        # Send the message to everybody but me.  Use the NoMe group, which
                                        # is set up by the multiplayer game.
                                        pNetwork.SendTGMessageToGroup("NoMe", pMessage2)
                                        # We're done.  Close the buffer.
                                        kStream2.CloseBuffer()
                        
                elif cType == NO_COLLISION_MESSAGE:
                        Object1Id = kStream.ReadInt()
                        Object2Id = kStream.ReadInt()
                        CollisionYesNo = kStream.ReadInt()
                        DisableCollisionTimer(None, Object1Id, Object2Id, CollisionYesNo, 100)
                                
                        # Host: send message to others
                        if App.g_kUtopiaModule.IsHost():
                                pNetwork = App.g_kUtopiaModule.GetNetwork()
                                # Now send a message to everybody else that the score was updated.
                                # allocate the message.
                                pMessage2 = App.TGMessage_Create()
                                pMessage2.SetGuaranteed(1)		# Yes, this is a guaranteed packet
                        
                                # Setup the stream.
                                kStream2 = App.TGBufferStream()		# Allocate a local buffer stream.
                                kStream2.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
	
                                # Write relevant data to the stream.
                                # First write message type.
                                kStream2.WriteChar(chr(NO_COLLISION_MESSAGE))
                                        
                                kStream2.WriteInt(Object1Id)
                                kStream2.WriteInt(Object2Id)
                                kStream2.WriteInt(CollisionYesNo)

                                # Okay, now set the data from the buffer stream to the message
                                pMessage2.SetDataFromStream(kStream2)
                                
                                # Send the message to everybody but me.  Use the NoMe group, which
                                # is set up by the multiplayer game.
                                pNetwork.SendTGMessageToGroup("NoMe", pMessage2)
                                # We're done.  Close the buffer.
                                kStream2.CloseBuffer()
                
                elif cType == SUBSYSTEM_SET_CONDITION:
                        ObjectId = kStream.ReadInt()
                        pShip = App.ShipClass_GetObjectByID(None, ObjectId)
                        
                        sSubsystemName = ""
                        while(1):
                                iChar = kStream.ReadChar()
                                if iChar == '\0':
                                        break
                                sSubsystemName = sSubsystemName + iChar
                                
                        iNewCondition = kStream.ReadInt()
                        
                        pSubsystem = MissionLib.GetSubsystemByName(pShip, sSubsystemName)
                        if pSubsystem:
                                if iNewCondition > 0.0:
                                        pSubsystem.SetCondition(iNewCondition)
                                else:
                                        pShip.DestroySystem(pSubsystem)
                
                elif cType == SET_SHIELD_CONDITION:
                        ObjectId = kStream.ReadInt()
                        iShield = kStream.ReadInt()
                        iNewCondition = kStream.ReadInt()
                        pShip = App.ShipClass_GetObjectByID(None, ObjectId)
                        if pShip:
                                pShields = pShip.GetShields()
                                if pShields:
                                        pShields.SetCurShields(iShield, iNewCondition)
                
                elif cType == MP_SET_TRACTOR_MODE:
                        iShipObjID = kStream.ReadInt()
                        iMode = kStream.ReadInt()
                        
                        pShip = App.ShipClass_GetObjectByID(None, iShipObjID)
                        if pShip:
                                pTractorSystem = pShip.GetTractorBeamSystem()
                                if pTractorSystem:
                                        pTractorSystem.SetMode(iMode)
                        
                        # forward Message
                        if App.g_kUtopiaModule.IsHost():
                                pNetwork = App.g_kUtopiaModule.GetNetwork()
                                # Now send a message to everybody else that the score was updated.
                                # allocate the message.
                                pMessage2 = App.TGMessage_Create()
                                pMessage2.SetGuaranteed(1)		# Yes, this is a guaranteed packet
                        
                                # Setup the stream.
                                kStream2 = App.TGBufferStream()		# Allocate a local buffer stream.
                                kStream2.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
	
                                # Write relevant data to the stream.
                                # First write message type.
                                kStream2.WriteChar(chr(MP_SET_TRACTOR_MODE))
                                        
                                kStream2.WriteInt(iShipObjID)
                                kStream2.WriteInt(iMode)

                                # Okay, now set the data from the buffer stream to the message
                                pMessage2.SetDataFromStream(kStream2)
                                
                                # Send the message to everybody but me.  Use the NoMe group, which
                                # is set up by the multiplayer game.
                                pNetwork.SendTGMessageToGroup("NoMe", pMessage2)
                                # We're done.  Close the buffer.
                                kStream2.CloseBuffer()
		
		elif cType == SET_SCRIPT_MSG:
			iShipObjID = kStream.ReadInt()
                        sShipScript = ""
                        while(1):
                                iChar = kStream.ReadChar()
                                if iChar == '\0':
                                        break
                                sShipScript = sShipScript + iChar
		
			pShip = App.ShipClass_GetObjectByID(None, iShipObjID)
			if pShip and not pShip.GetScript():
				pShip.SetScript(sShipScript)
			
			# if we are host, tell others
                        if App.g_kUtopiaModule.IsHost():
                                pNetwork = App.g_kUtopiaModule.GetNetwork()
                                # Now send a message to everybody else that the score was updated.
                                # allocate the message.
                                pMessage2 = App.TGMessage_Create()
                                pMessage2.SetGuaranteed(1)		# Yes, this is a guaranteed packet
                        
                                # Setup the stream.
                                kStream2 = App.TGBufferStream()		# Allocate a local buffer stream.
                                kStream2.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
	
                                # Write relevant data to the stream.
                                # First write message type.
                                kStream2.WriteChar(chr(SET_SCRIPT_MSG))
                                        
                                kStream2.WriteInt(iShipObjID)
                                for i in range(len(sShipScript)):
                                        kStream2.WriteChar(sShipScript[i])
                                # set the last char:
                                kStream2.WriteChar('\0')

                                # Okay, now set the data from the buffer stream to the message
                                pMessage2.SetDataFromStream(kStream2)
                                
                                # Send the message to everybody but me.  Use the NoMe group, which
                                # is set up by the multiplayer game.
                                pNetwork.SendTGMessageToGroup("NoMe", pMessage2)
                                # We're done.  Close the buffer.
                                kStream2.CloseBuffer()
                elif cType == ET_CLIENT_SCAN:
                        iShipObjID = kStream.ReadInt()
                        pShip = App.ShipClass_GetObjectByID(None, iShipObjID)
                        if pShip:
                                try:
                                        import Custom.QBautostart.CloakCounterMeasures
                                        Custom.QBautostart.CloakCounterMeasures.ShipScan(pShip)
                                except:
                                        pass

		elif cType == MP_SET_POSITION_MSG:
			iShipObjID = kStream.ReadInt()
			iUpdateAlignToVectors = kStream.ReadInt()
			
			posX = kStream.ReadFloat()
			posY = kStream.ReadFloat()
			posZ = kStream.ReadFloat()
			forwardX = kStream.ReadFloat()
			forwardY = kStream.ReadFloat()
			forwardZ = kStream.ReadFloat()
			upX = kStream.ReadFloat()
			upY = kStream.ReadFloat()
			upZ = kStream.ReadFloat()
			
			pShip = App.ShipClass_GetObjectByID(None, iShipObjID)
			kLocation = App.TGPoint3()
			kforward = App.TGPoint3()
			kup = App.TGPoint3()
			kLocation.SetXYZ(posX, posY, posZ)
			kforward.SetXYZ(forwardX, forwardY, forwardZ)
			kup.SetXYZ(upX, upY, upZ)
			if pShip:
				pShip.SetTranslate(kLocation)
				if iUpdateAlignToVectors:
					pShip.AlignToVectors(kforward, kup)
		
		elif cType == PLAYER_NOW_USING_SHIP:
        		iTeam = kStream.ReadInt()
			iSpecies = kStream.ReadInt()

			sSelectedTeam = Races.keys()[iTeam]
			sShipScript = Multiplayer.SpeciesToShip.GetScriptFromSpecies(iSpecies)
			Races[sSelectedTeam].BuildShipToPlayerShip(sShipScript)
			
			# if we are host, tell others
                        if App.g_kUtopiaModule.IsHost():
                                pNetwork = App.g_kUtopiaModule.GetNetwork()
                                # Now send a message to everybody else that the score was updated.
                                # allocate the message.
                                pMessage2 = App.TGMessage_Create()
                                pMessage2.SetGuaranteed(1)		# Yes, this is a guaranteed packet
                        
                                # Setup the stream.
                                kStream2 = App.TGBufferStream()		# Allocate a local buffer stream.
                                kStream2.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
	
        			kStream2.WriteInt(iTeam)
				kStream2.WriteInt(iSpecies)

                                # Okay, now set the data from the buffer stream to the message
                                pMessage2.SetDataFromStream(kStream2)
                                
                                # Send the message to everybody but me.  Use the NoMe group, which
                                # is set up by the multiplayer game.
                                pNetwork.SendTGMessageToGroup("NoMe", pMessage2)
                                # We're done.  Close the buffer.
                                kStream2.CloseBuffer()

		elif cType == MP_SEND_PLASMA_FX:
			iShipObjID = kStream.ReadInt()
			posX = kStream.ReadFloat()
			posY = kStream.ReadFloat()
			posZ = kStream.ReadFloat()
			iEngine = kStream.ReadInt()
			fVentTime = kStream.ReadFloat()
			
			pShip = App.ShipClass_GetObjectByID(None, iShipObjID)
			vEmitDir = App.NiPoint3(posX, posY, posZ)
			if pShip:
				try:
					from Custom.NanoFXv2.SpecialFX.PlasmaFX import CreatePlasmaFXNoEvent
					pPlasma = CreatePlasmaFXNoEvent(pShip, vEmitDir, iEngine, fVentTime)
				
					if pPlasma:
						pSequence = App.TGSequence_Create()
						pSequence.AddAction(pPlasma)
						pSequence.Play()
				
				except:
					print "No NanoFX2 found. Not creating PlasmaFX"

		elif cType == REPLACE_MODEL_MSG:
			iShipID = kStream.ReadInt()
			sNewShipScript = ""
			iLen = kStream.ReadShort()
			for i in range(iLen):
				sNewShipScript = sNewShipScript + kStream.ReadChar()
			
			SetNewModel(iShipID, sNewShipScript)

			if App.g_kUtopiaModule.IsHost():
				dReplaceModel[iShipID] = sNewShipScript
				
				# if we are host, tell others
				SentReplaceModelMessage(iShipID, sNewShipScript)

		elif cType == SET_TARGETABLE_MSG:
			iShipID = kStream.ReadInt()
			iMode = kStream.ReadInt()
			
			SetTargetableModeTimer(None, iShipID, iMode, 500)
			
			# if we are host, tell others
                        if App.g_kUtopiaModule.IsHost():				
                                pNetwork = App.g_kUtopiaModule.GetNetwork()
                                # Now send a message to everybody else that the score was updated.
                                # allocate the message.
                                pMessage2 = App.TGMessage_Create()
                                pMessage2.SetGuaranteed(1)		# Yes, this is a guaranteed packet
                        
                                # Setup the stream.
                                kStream2 = App.TGBufferStream()		# Allocate a local buffer stream.
                                kStream2.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
	
                                # Write relevant data to the stream.
                                # First write message type.
                                kStream2.WriteChar(chr(SET_TARGETABLE_MSG))
                                        
                                kStream2.WriteInt(iShipID)
                                kStream2.WriteInt(iMode)

                                # Okay, now set the data from the buffer stream to the message
                                pMessage2.SetDataFromStream(kStream2)
                                
                                # Send the message to everybody but me.  Use the NoMe group, which
                                # is set up by the multiplayer game.
                                pNetwork.SendTGMessageToGroup("NoMe", pMessage2)
                                # We're done.  Close the buffer.
                                kStream2.CloseBuffer()

		elif cType == ALERT_STATE_CHANGED_MSG:
			iShipID = kStream.ReadInt()
			iLevel = kStream.ReadInt()

			pShip = App.ShipClass_GetObjectByID(None, iShipID)
			if pShip and pShip.GetAlertLevel() != iLevel:
				pAlertEvent = App.TGIntEvent_Create()
				pAlertEvent.SetDestination(pShip)
				pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
				pAlertEvent.SetInt(iLevel)
				App.g_kEventManager.AddEvent(pAlertEvent)
				
			# if we are host, tell others
                        if App.g_kUtopiaModule.IsHost():				
                                pNetwork = App.g_kUtopiaModule.GetNetwork()
                                # Now send a message to everybody else that the score was updated.
                                # allocate the message.
                                pMessage2 = App.TGMessage_Create()
                                pMessage2.SetGuaranteed(1)		# Yes, this is a guaranteed packet
                        
                                # Setup the stream.
                                kStream2 = App.TGBufferStream()		# Allocate a local buffer stream.
                                kStream2.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
	
                                # Write relevant data to the stream.
                                # First write message type.
                                kStream2.WriteChar(chr(ALERT_STATE_CHANGED_MSG))
                                        
                                kStream2.WriteInt(iShipID)
                                kStream2.WriteInt(iLevel)

                                # Okay, now set the data from the buffer stream to the message
                                pMessage2.SetDataFromStream(kStream2)
                                
                                # Send the message to everybody but me.  Use the NoMe group, which
                                # is set up by the multiplayer game.
                                pNetwork.SendTGMessageToGroup("NoMe", pMessage2)
                                # We're done.  Close the buffer.
                                kStream2.CloseBuffer()
		
		elif cType == DELETE_OBJECT_FROM_SET_MSG:
			iShipID = kStream.ReadInt()
			
			pShip = App.ShipClass_GetObjectByID(None, iShipID)
			if pShip:
				DeleteObjectFromSet(pShip.GetContainingSet(), pShip, 1)
				
			# if we are host, tell others
                        if App.g_kUtopiaModule.IsHost():				
                                pNetwork = App.g_kUtopiaModule.GetNetwork()
                                # Now send a message to everybody else that the score was updated.
                                # allocate the message.
                                pMessage2 = App.TGMessage_Create()
                                pMessage2.SetGuaranteed(1)		# Yes, this is a guaranteed packet
                        
                                # Setup the stream.
                                kStream2 = App.TGBufferStream()		# Allocate a local buffer stream.
                                kStream2.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
	
                                # Write relevant data to the stream.
                                # First write message type.
                                kStream2.WriteChar(chr(DELETE_OBJECT_FROM_SET_MSG))
                                        
                                kStream2.WriteInt(iShipID)

                                # Okay, now set the data from the buffer stream to the message
                                pMessage2.SetDataFromStream(kStream2)
                                
                                # Send the message to everybody but me.  Use the NoMe group, which
                                # is set up by the multiplayer game.
                                pNetwork.SendTGMessageToGroup("NoMe", pMessage2)
                                # We're done.  Close the buffer.
                                kStream2.CloseBuffer()

		elif cType == SET_GET_SHIP_ATTR_MSG:
			iMode = kStream.ReadInt()
			iShipID = kStream.ReadInt()
			iShipFromID = kStream.ReadInt()
			SetGetShipAttrsTimer(None, iMode, iShipID, iShipFromID, 500)

		elif cType == SET_AUTO_AI_MSG:
			iShipID = kStream.ReadInt()
			pShip = App.ShipClass_GetObjectByID(None, iShipID)
			if pShip:
				autoAI(pShip)

		elif cType == SET_STOP_AI_MSG:
			iShipID = kStream.ReadInt()
			pShip = App.ShipClass_GetObjectByID(None, iShipID)
			if pShip:
				import AI.Player.Stay
				pShip.SetAI(AI.Player.Stay.CreateAI(pShip))

		elif cType == TRACTOR_STARTED_MSG:
			iShipID = kStream.ReadInt()
			iTargetID = kStream.ReadInt()
			pShip = App.ShipClass_GetObjectByID(None, iShipID)
			pTarget = App.ShipClass_GetObjectByID(None, iTargetID)
			if pShip:
				pTractorSystem = pShip.GetTractorBeamSystem()
				if pTractorSystem:
					sTargetName = "None"
					if pTarget:
						sTargetName = pTarget.GetName()
					print "Tractor Start %s %s" % (pShip.GetName(), sTargetName)
					pTractorSystem.StartFiring(pTarget)
				# if we are host, tell others
				if App.g_kUtopiaModule.IsHost():				
					pMessage2, kStream2 = CreateMessageStream(TRACTOR_STARTED_MSG)
					kStream2.WriteInt(iShipID)
					SendMessageToEveryone(pMessage2, kStream2)

		elif cType == MP_SET_TARGET_MSG:
			iShip1ID = kStream.ReadInt()
			iShip2ID = kStream.ReadInt()
			pShip1 = App.ShipClass_GetObjectByID(None, iShip1ID)
			pShip2 = App.ShipClass_GetObjectByID(None, iShip2ID)
			if pShip1:
				if pShip2:
					pShip1.SetTarget(pShip2.GetName())
					print "Set Target: %s %s" % (pShip1.GetName(), pShip2.GetName())
				else:
					pShip1.SetTarget(None)
					print "Set Target: %s %s" % (pShip1.GetName(), "None")
				# if we are host, tell others
				if App.g_kUtopiaModule.IsHost():				
					pMessage2, kStream2 = CreateMessageStream(MP_SET_TARGET_MSG)
					kStream2.WriteInt(iShip1ID)
					kStream2.WriteInt(iShip2ID)
					SendMessageToEveryone(pMessage2, kStream2)

		kStream.Close()


def SetGetShipAttrsTimer(pAction, iMode, iShipID, iShipFromID, iTry):
	debug(__name__ + ", SetGetShipAttrsTimer")
	pShip = App.ShipClass_GetObjectByID(None, iShipID)
	if pShip:
		if iMode == 0: # get
			MPGetShipAttributes(pShip)
		elif iMode == 1: # set
			MPSetShipAttributes(pShip, iShipFromID)
	elif iTry > 0:
		pSeq = App.TGSequence_Create()
		pSeq.AppendAction(App.TGScriptAction_Create(__name__, "SetGetShipAttrsTimer", iMode, iShipID, iShipFromID, iTry-1), 0.01)
		pSeq.Play()
	else:
		print "Was unable to set/get ship attributes"
	return 0


def SetNewModel(iShipID, sNewShipScript):
	debug(__name__ + ", SetNewModel")
	pShip = App.ShipClass_GetObjectByID(None, iShipID)

	if pShip and sNewShipScript:
		ShipScript = __import__(('ships.' + sNewShipScript))
		ShipScript.LoadModel()
		kStats = ShipScript.GetShipStats()
		pShip.SetupModel(kStats['Name'])
	else:
		print "Warning: Can not replace Model"


def SetTargetableModeTimer(pAction, iShipID, iMode, iTry):
	debug(__name__ + ", SetTargetableModeTimer")
	pShip = App.ShipClass_GetObjectByID(None, iShipID)
	if pShip:
		pShip.SetTargetable(iMode)
	elif iTry > 0:
		pSeq = App.TGSequence_Create()
		pSeq.AppendAction(App.TGScriptAction_Create(__name__, "SetTargetableModeTimer", iShipID, iMode, iTry-1), 0.01)
		pSeq.Play()
	else:
		print "Was unable to set targetable mode"
	return 0


def DisableCollisionTimer(pAction, Object1Id, Object2Id, CollisionYesNo, iTry):
        debug(__name__ + ", DisableCollisionTimer")
        pObject1 = App.DamageableObject_GetObjectByID(None, Object1Id)
        pObject2 = App.DamageableObject_GetObjectByID(None, Object2Id)
        if pObject1 and pObject2:
                pObject1.EnableCollisionsWith(pObject2, CollisionYesNo)
        elif iTry > 0:
                pSeq = App.TGSequence_Create()
                pSeq.AppendAction(App.TGScriptAction_Create(__name__, "DisableCollisionTimer", Object1Id, Object2Id, CollisionYesNo, iTry-1), 0.1)
                pSeq.Play()
        return 0


# This method is called if you are the host and a new player joins.  Use this
# method to send any relevant information about the game to the player joining.
# For example, the name of the system that the mission takes place in would
# be something the hosts decides in his menus and then sends to other players.
def InitNetwork(iToID):
	debug(__name__ + ", InitNetwork")
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	if (not pNetwork):
		# Huh?  No network?  bail.
		return

	###############################################################
	# Send mission init message with info needed to start mission
	# allocate the message.
	pMessage = App.TGMessage_Create()
	pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet
	
	# Setup the stream.
	kStream = App.TGBufferStream()		# Allocate a local buffer stream.
	kStream.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
	
	# Write relevant data to the stream.
	# First write message type.
	kStream.WriteChar(chr(Multiplayer.MissionShared.MISSION_INIT_MESSAGE))

	# Write the maximum number of players
	kStream.WriteChar(chr(Multiplayer.MissionMenusShared.g_iPlayerLimit))

	if (Multiplayer.MissionMenusShared.g_iTimeLimit == -1):
		kStream.WriteChar(chr(255))
	else:
		kStream.WriteChar(chr(Multiplayer.MissionMenusShared.g_iTimeLimit))
		kStream.WriteInt(Multiplayer.MissionShared.g_iTimeLeft + int(App.g_kUtopiaModule.GetGameTime()))

	if (Multiplayer.MissionMenusShared.g_iFragLimit == -1):
		kStream.WriteChar(chr(255))
	else:
		kStream.WriteChar(chr(Multiplayer.MissionMenusShared.g_iFragLimit))

	# write systems
	kStream.WriteInt(iDefaultStartingSet)
	lSystemsDone = []
	for iTeam in range(len(Races.keys())):
		sTeam = Races.keys()[iTeam]
		
		if hasattr(Races[sTeam], "iStartingSet"):
			kStream.WriteInt(iTeam)
			kStream.WriteInt(Races[sTeam].iStartingSet)
			lSystemsDone.append(Races[sTeam].iStartingSet)
	kStream.WriteInt(-1)
	for iSystem in lStartingSets:
		if iSystem != iDefaultStartingSet and not iSystem in lSystemsDone:
			kStream.WriteInt(iSystem)
	kStream.WriteInt(-1)

	# write ships
	for iIndex in range(1, Multiplayer.SpeciesToShip.MAX_SHIPS):
		sShipScript = Multiplayer.SpeciesToShip.GetScriptFromSpecies(iIndex)
		sRace = GetRaceFromShipType(sShipScript)
		if Races.has_key(sRace) and Races[sRace].NumFreeShips(sShipScript) > 0:
			kStream.WriteInt(iIndex)
			kStream.WriteInt(Races[sRace].NumFreeShips(sShipScript))
	kStream.WriteInt(-1)
	
	# Okay, now set the data from the buffer stream to the message
	pMessage.SetDataFromStream(kStream)

	# Send the message.
	pNetwork.SendTGMessage(iToID, pMessage)

	# We're done.  Close the buffer.
	kStream.CloseBuffer()

	###############################################################
	# Send the scores for each player in the dictionary
	# allocate the message.
	global g_kKillsDictionary
	global g_kDeathsDictionary
	global g_kScoresDictionary
	global g_kTeamDictionary
	global g_kTeamKillsDictionary
	global g_kTeamScoreDictionary


	# Construct a new dictionary containing the keys of 
	# people in the game.
	pDict = {}

	for iKey in g_kKillsDictionary.keys ():
		pDict[iKey] = 1

	for iKey in g_kDeathsDictionary.keys ():
		pDict[iKey] = 1

	for iKey in g_kScoresDictionary.keys ():
		pDict[iKey] = 1

	for iKey in g_kTeamDictionary.keys ():
		pDict[iKey] = 1
                
	# Now go through the keys in the new dictionary
	# and send that person's score around.

	for iKey in pDict.keys():
		iKills = 0
		iDeaths = 0
		iScore = 0
		iTeam = INVALID_TEAM
		
		if (g_kKillsDictionary.has_key(iKey)):
			iKills = g_kKillsDictionary[iKey]
					
		if (g_kDeathsDictionary.has_key(iKey)):
			iDeaths = g_kDeathsDictionary[iKey]
					
		if (g_kScoresDictionary.has_key(iKey)):
			iScore = g_kScoresDictionary[iKey]

		if (g_kTeamDictionary.has_key(iKey)):
			iTeam = g_kTeamDictionary[iKey]
				 
		pMessage = App.TGMessage_Create()
		pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet
		
		# Setup the stream.
		kStream = App.TGBufferStream()		# Allocate a local buffer stream.
		kStream.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
		
		# Write relevant data to the stream.
		# First write message type.
		kStream.WriteChar(chr(SCORE_INIT_MESSAGE))

		# write kills and deaths
		kStream.WriteLong(iKey)
		kStream.WriteLong(iKills)
		kStream.WriteLong(iDeaths)
		kStream.WriteLong(iScore)
		kStream.WriteChar(chr(iTeam))

		# Okay, now set the data from the buffer stream to the message
		pMessage.SetDataFromStream(kStream)

		# Send the message.
		pNetwork.SendTGMessage(iToID, pMessage)

		# We're done.  Close the buffer.
		kStream.CloseBuffer()

	# Now send the team scores
	for iTeam in g_kTeamScoreDictionary.keys():
		iScore = g_kTeamScoreDictionary[iTeam]

		iKills = 0
		if (g_kTeamKillsDictionary.has_key(iTeam)):
			iKills = g_kTeamKillsDictionary[iTeam]

		pMessage = App.TGMessage_Create()
		pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet
		
		# Setup the stream.
		kStream = App.TGBufferStream()		# Allocate a local buffer stream.
		kStream.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
		
		# Write relevant data to the stream.
		# First write message type.
		kStream.WriteChar (chr (TEAM_SCORE_MESSAGE))

		# write kills and score
		kStream.WriteChar(chr(iTeam))
		kStream.WriteLong(iKills)
		kStream.WriteLong(iScore)

		# Okay, now set the data from the buffer stream to the message
		pMessage.SetDataFromStream(kStream)

		# Send the message.
		pNetwork.SendTGMessage(iToID, pMessage)

		# We're done.  Close the buffer.
		kStream.CloseBuffer()

	return 1


def DamageEventHandler(pObject, pEvent):
	debug(__name__ + ", DamageEventHandler")
	if (pEvent.IsHullHit() == 1):
		DamageHandler(pObject, pEvent, 1)
	else:
		DamageHandler(pObject, pEvent, 0)
        pObject.CallNextHandler(pEvent)


def DamageHandler(TGObject, pEvent, bHullDamage):
        debug(__name__ + ", DamageHandler")
        import Multiplayer.Modifier
	# Damage was done.  We need to record this for scoring purposes.
	# Get the player id of the shooter.
	iHitterID = pEvent.GetFiringPlayerID()
	
	if (iHitterID == 0):
		# No player doing the hitting.  Don't record.
		return

	# Get the object id of the ship that was hit.
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	if (not pShip):
		# Don't score non-ship objects
		return 

	iHitID = pShip.GetObjID()

	iHitClass = 0
	iHitterClass = 0

	# Get the hitter's ship.
	pGame = App.MultiplayerGame_Cast(App.Game_GetCurrentGame())
	pHitterShip = pGame.GetShipFromPlayerID(iHitterID)
	if (pHitterShip):
		iHitterClass = Multiplayer.SpeciesToShip.GetClassFromSpecies(pHitterShip.GetNetType())

	iHitClass = Multiplayer.SpeciesToShip.GetClassFromSpecies(pShip.GetNetType())

	# Get the amount of damage done.
	fDamage = pEvent.GetDamage()

	# Modifify damage based on ship class
	fDamage = fDamage * Multiplayer.Modifier.GetModifier(iHitterClass, iHitClass)

	# get the team of the person who did the hitting.
	iHitterTeam = INVALID_TEAM
	if (g_kTeamDictionary.has_key(iHitterID)):
		iHitterTeam = g_kTeamDictionary[iHitterID]

	# Get the team of the ship that got hit.
	if (IsSameTeam(iHitterID, pShip.GetNetPlayerID())):
		# Same team, so penalize their score
		fDamage = -fDamage		

	# Get the dictionary that stores all the people that have hit this object.
	global g_kDamageDictionary
	pDamageByDict = None
	if (g_kDamageDictionary.has_key(iHitID)):
		# This object has been hit before.  Fetch it's damage by dictionary
		pDamageByDict = g_kDamageDictionary[iHitID]
	else:
		# Create a new dictionary since this object has not been hit by a player
		# before
		pDamageByDict = {}
		g_kDamageDictionary[iHitID] = pDamageByDict


	# Update the damage by dictinary.
	fPreviousDamageDone = 0.0
	pDamageList = None
	if (pDamageByDict.has_key(iHitterID)):
		# This player has done damage before.  Fetch previous damage done.
		# Get the list from the damage dict
		pDamageList = pDamageByDict[iHitterID]
		fPreviousDamageDone = pDamageList[bHullDamage]	# zero is shield, 1 is hull
	else:
		# This player has not done damage before.  Create a new damage list
		# to add to the damage dict.
		pDamageList = [0, 0]		# List of two elements
		pDamageByDict[iHitterID] = pDamageList

	# Add in the damage done this time.
	fPreviousDamageDone = fPreviousDamageDone + fDamage

	# Store it in the database
	pDamageList[bHullDamage] = fPreviousDamageDone


def ObjectKilledHandlerClient(pObject, pEvent):
        #print "Object Silent Killed Handler"
        
        debug(__name__ + ", ObjectKilledHandlerClient")
        pKilledObject = pEvent.GetDestination()
        if (pKilledObject.IsTypeOf(App.CT_SHIP)):
                pShip = App.ShipClass_Cast(pKilledObject)
                sShipName = pShip.GetName()
                
                if string.find(string.lower(sShipName), "firepoint") != -1:
                        return
                
                #print("Killed Ship: ", sShipName)

                # Now send a message to everybody else that the score was updated.
                # allocate the message.
                pMessage = App.TGMessage_Create()
                pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet

	        # Setup the stream.
	        kStream = App.TGBufferStream()		# Allocate a local buffer stream.
	        kStream.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
	
	        # Write relevant data to the stream.
	        # First write message type.
	        kStream.WriteChar(chr(CLIENT_OBJECT_DESTROYED))

                # Write the name of killed ship
                for i in range(len(sShipName)):
                        kStream.WriteChar(sShipName[i])
                # set the last char:
                kStream.WriteChar('\0')

	        # Okay, now set the data from the buffer stream to the message
	        pMessage.SetDataFromStream(kStream)

                # Send the message to everybody but me.  Use the NoMe group, which
                # is set up by the multiplayer game.
                pNetwork = App.g_kUtopiaModule.GetNetwork()
                if not App.IsNull(pNetwork):
                        pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)

	        # We're done.  Close the buffer.
	        kStream.CloseBuffer()
        pObject.CallNextHandler(pEvent)


def RemoveNameFromGroup(pGroup, sName):
        # Removing "This ship probably wont exist" will only increase the (in-)famous addship lag
        # since it will be added and added again.
        debug(__name__ + ", RemoveNameFromGroup")
        if pGroup and pGroup.IsNameInGroup(sName) and sName != "This ship probably wont exist":
                pGroup.RemoveName(sName)


def RemoveNameFromAllGroupsBut(iGroup, sName):
	debug(__name__ + ", RemoveNameFromAllGroupsBut")
	for i in range(len(g_lTeams)):
		if i != iGroup:
			pGroup = g_lTeams[i]
			RemoveNameFromGroup(pGroup, sName)


def AddNameToGroup(pGroup, sName):
        debug(__name__ + ", AddNameToGroup")
        if pGroup and not pGroup.IsNameInGroup(sName):
                pGroup.AddName(sName)


# This handler updates the score when an object is killed.
def ObjectKilledHandler(pObject, pEvent):
        debug(__name__ + ", ObjectKilledHandler")
        global dict_Probes, g_lFirepoints
        
        pObject.CallNextHandler(pEvent)
        
        pKilledObject = pEvent.GetDestination()
        if (pKilledObject.IsTypeOf(App.CT_SHIP)):
                pShip = App.ShipClass_Cast(pKilledObject)
                #DoKillSubtitle(None, pShip.GetName())
                pShipID = pShip.GetNetPlayerID()

                # delete all probes of this Player:
                if dict_Probes.has_key(pShipID):
                        for ProbeName in dict_Probes[pShipID]:
                                pProbe = MissionLib.GetShip(ProbeName)
                                if pProbe:
                                        pProbe.DestroySystem(pProbe.GetHull())
                        del dict_Probes[pShipID]

		# Remove ship from group 1.
                #RemoveNameFromGroup(g_pTeam1, pShip.GetName())
                # Remove ship from group 2.
                #RemoveNameFromGroup(g_pTeam2, pShip.GetName())
                
                #pFriendlies = MissionLib.GetFriendlyGroup()
		#if pFriendlies.IsNameInGroup(pShip.GetName()):
                #        RemoveNameFromGroup(pFriendlies, pShip.GetName())
                #pEnemies = MissionLib.GetEnemyGroup()
		#if pEnemies.IsNameInGroup(pShip.GetName()):
                #        RemoveNameFromGroup(pEnemies, pShip.GetName())
        
                # check to delete firepoints
		for pSet in App.g_kSetManager.GetAllSets():
			lShips = pSet.GetClassObjectList(App.CT_SHIP)
			for pObject in lShips:
				pCurShip = App.ShipClass_Cast(pObject)
				# is this a firepoint that belongs to this ship?
				if string.find(string.lower(pCurShip.GetName()), "firepoint") != -1 and string.find(string.lower(pCurShip.GetName()), string.lower(pShip.GetName())) != -1:
                                        pCurShip.DestroySystem(pCurShip.GetHull())
					pSet.RemoveObjectFromSet(pCurShip.GetName())
        
        # only the host has more work todo:
        if not App.g_kUtopiaModule.IsHost():
               return 
        import Multiplayer.MissionShared
	if (Multiplayer.MissionShared.g_bGameOver != 0):
		# If the game is over, then don't do anymore score processing
		return

	# Get the player ID of the firing object from the event
	iFiringPlayerID = pEvent.GetFiringPlayerID()

	# Get the player id of the player who got killed.  It could be AI object,
	# in which case the ID is zero.
	iShipID = App.NULL_ID

	pKilledObject = pEvent.GetDestination ()
	if (pKilledObject.IsTypeOf (App.CT_SHIP)):
		# Get the player id of the ship from the multiplayer game.
		iKilledPlayerID = pShip.GetNetPlayerID()
		iShipID = pShip.GetObjID()
			
	else:
		iKilledPlayerID = 0

	# At this point, we have the player id of the person who made the killing shot.
	# Award a frag to him.
	iKills = 0

	if (iFiringPlayerID != 0):
		# Get the previous frag count.
		global g_kKillsDictionary
		if (g_kKillsDictionary.has_key(iFiringPlayerID) == 1):
			# There is already this player is the kill table.  Get his previous kill total.
			iKills = g_kKillsDictionary[iFiringPlayerID]	
		else:
			# First kill.
			iKills = 0

		if (g_kTeamDictionary.has_key(iFiringPlayerID)):
			iTeam = g_kTeamDictionary[iFiringPlayerID]

			if not IsSameTeam(iFiringPlayerID, iKilledPlayerID):
				# Yes, enemy ship.  Award kill
				# Increment kills by one to count for this current kill.
				iKills = iKills + 1

				# Award kill to team as well.
				iTeamKills = 0
				if (g_kTeamKillsDictionary.has_key(iTeam)):
					iTeamKills = g_kTeamKillsDictionary[iTeam]

				iTeamKills = iTeamKills + 1

				g_kTeamKillsDictionary[iTeam] = iTeamKills
	#else:
	#	# Self destruct?  Collision?  Still award a team kill to the Team2 Name if appropriate.
	#	if (g_kTeamDictionary.has_key(iKilledPlayerID)):
	#		# get the team that the killed player was on.
	#		iKilledTeam = g_kTeamDictionary[iKilledPlayerID]
	#		if (iKilledTeam == 0):	# Attacking team died
	#			# award a kill to the defending team.
	#			iTeamKills = 0
	#			if g_kTeamKillsDictionary.has_key(1):
	#				iTeamKills = g_kTeamKillsDictionary[1]
	#			
	#			iTeamKills = iTeamKills + 1					
	#			g_kTeamKillsDictionary[1] = iTeamKills

	# Award a death to the person that just got killed.
	global g_kDeathsDictionary
	if (g_kDeathsDictionary.has_key(iKilledPlayerID) == 1):
		# There is already this player is the death table.  Get his previous death total.
		iDeaths = g_kDeathsDictionary[iKilledPlayerID]
	else:
		# First death
		iDeaths = 0

	# Increment Deaths by one to count for this current kill.
	iDeaths = iDeaths + 1

	# Okay, now give all the player's who damaged this object credit.
	iScoreUpdateCount = 0		# Keep track of how many players had their score changed.
	iFiringPlayerScore = 0		# Keep track of this to send the event later.
	global g_kDamageDictionary
	global g_kScoresDictionary
	global g_kTeamScoreDictionary
	global g_kTeamKillsDictionary

	pDamageByDict = None

	if (iShipID != App.NULL_ID):
		if (g_kDamageDictionary.has_key(iShipID)):
			# Okay, there are player damage points to award.
			pDamageByDict = g_kDamageDictionary[iShipID]

	if (pDamageByDict):
		# Okay, there are player damage points to award.
		pDamageByDict = g_kDamageDictionary[iShipID]

		# Loop through the player list and award score.
		for iPlayerID in pDamageByDict.keys():
			# Get shield and hull damage done by this player.
			pDamageList = pDamageByDict[iPlayerID]
			fShieldDamageDone = pDamageList[0]
			fHullDamageDone = pDamageList[1]

			# Compute damage done based on some formula.  For now
			# it is simple addition.
			fDamageDone = fShieldDamageDone + fHullDamageDone
			fDamageDone = fDamageDone / 10.0		# Reduce points by factor of 10 to keep numbers reasonable

			# Get previous score
			fScore = 0.0
			if (g_kScoresDictionary.has_key(iPlayerID)):
				fScore = g_kScoresDictionary[iPlayerID]
			
			fScore = fScore + fDamageDone

			# Count the number of non firing player scores.  This is
			# used to send the scores later.  The firing player has
			# his score sent separately, so it shouldn't to be counted.
			if (iPlayerID == iFiringPlayerID):
				iFiringPlayerScore = int(fScore)
			else:
#				# print("Counting " + str (iPlayerID))
				iScoreUpdateCount = iScoreUpdateCount + 1
											
			g_kScoresDictionary[iPlayerID] = int(fScore)

			# Update team score as well
			# Get this player's team.
			if (g_kTeamDictionary.has_key(iPlayerID)):
				iTeam = g_kTeamDictionary[iPlayerID]

				fTeamScore = 0
				if (g_kTeamScoreDictionary.has_key(iTeam)):
					fTeamScore = g_kTeamScoreDictionary[iTeam]
				
				fTeamScore = fTeamScore + fDamageDone
				g_kTeamScoreDictionary[iTeam] = int(fTeamScore)


	# Update the score
	UpdateScore(iFiringPlayerID, iKills, iKilledPlayerID, iDeaths)

	# Now send a message to everybody else that the score was updated.
	# allocate the message.
	pMessage = App.TGMessage_Create()
	pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet
	
	# Setup the stream.
	kStream = App.TGBufferStream()		# Allocate a local buffer stream.
	kStream.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
	
	# Write relevant data to the stream.
	# First write message type.
	kStream.WriteChar(chr(Multiplayer.MissionShared.SCORE_CHANGE_MESSAGE))

	# Write the player id of killer
	kStream.WriteLong(iFiringPlayerID)

	if (iFiringPlayerID != 0):
		# Write the kills
		kStream.WriteLong(iKills)

		# Write the score as a long
		kStream.WriteLong(iFiringPlayerScore)

	# Write the player id of killed
	kStream.WriteLong(iKilledPlayerID)
	
	# Write the deaths
	kStream.WriteLong(iDeaths)

	# Write out the number of score changes
	kStream.WriteChar(chr(iScoreUpdateCount))

	# Write out scores for all the players that have score changes.
	iCount = 0
	if (pDamageByDict):
		# Loop through the player list and store the score.
		for iPlayerID in pDamageByDict.keys ():
			# print("Checking " + str (iPlayerID))
			if (iPlayerID != iFiringPlayerID and iPlayerID != 0):	# firing player already has his score stored
#				# print("Writing score for " + str (iPlayerID) + " for " + str (g_kScoresDictionary [iPlayerID]) + " points.")
				kStream.WriteLong(iPlayerID)
				kStream.WriteLong(g_kScoresDictionary[iPlayerID])
				iCount = iCount + 1

	# Error condition.  Just put some filler in.
	while(iCount < iScoreUpdateCount):
		kStream.WriteLong(0)

	# Okay, now set the data from the buffer stream to the message
	pMessage.SetDataFromStream(kStream)

	# Send the message to everybody but me.  Use the NoMe group, which
	# is set up by the multiplayer game.
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	if (not App.IsNull(pNetwork)):
		pNetwork.SendTGMessageToGroup("NoMe", pMessage)

	# We're done.  Close the buffer.
	kStream.CloseBuffer()

	# Clear the damage dictionary for this object since it is now
	# dead an we don't want memory wasted storing who did damage to
	# this thing anymore.
	if (iShipID != App.NULL_ID):
		if (g_kDamageDictionary.has_key(iShipID)):
			del g_kDamageDictionary[iShipID]

	# Now send the team scores
	for iTeam in g_kTeamScoreDictionary.keys():
		iScore = g_kTeamScoreDictionary[iTeam]

		iKills = 0
		if (g_kTeamKillsDictionary.has_key(iTeam)):
			iKills = g_kTeamKillsDictionary[iTeam]

		pMessage = App.TGMessage_Create()
		pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet
		
		# Setup the stream.
		kStream = App.TGBufferStream()		# Allocate a local buffer stream.
		kStream.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
		
		# Write relevant data to the stream.
		# First write message type.
		kStream.WriteChar(chr(TEAM_SCORE_MESSAGE))

		# write kills and score
		kStream.WriteChar(chr(iTeam))
		kStream.WriteLong(iKills)
		kStream.WriteLong(iScore)

		# Okay, now set the data from the buffer stream to the message
		pMessage.SetDataFromStream(kStream)

		# Send the message.
		pNetwork.SendTGMessageToGroup("NoMe", pMessage)

		# We're done.  Close the buffer.
		kStream.CloseBuffer()

	# Check frag limit to see if game is over
	#CheckFragLimit()


# Send to all people the Group of the Ship we just have added
def SendGroupInfo(ShipName, ShipID):
	debug(__name__ + ", SendGroupInfo")
	global ADD_AI_TO_TEAM_MSG
	
	# Setup the stream.
	# Allocate a local buffer stream.
	kStream = App.TGBufferStream()
	# Open the buffer stream with a byte buffer.
	kStream.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)
	
	# Write relevant data to the stream.
	# First write message type.
	kStream.WriteChar(chr(ADD_AI_TO_TEAM_MSG))

	# Write out scores for all the players that have score changes.
	iCount = 0
	# Loop through the String
	for ichar in range(len(ShipName)):
		kStream.WriteChar(ShipName[iCount])
		iCount = iCount + 1

	# set the last char:
	kStream.WriteChar('\0')

	# Write the new Ship ID:
	kStream.WriteLong(ShipID)

	pMessage = App.TGMessage_Create()
        # Yes, this is a guaranteed packet
	pMessage.SetGuaranteed(1)
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


def TellScriptInfo(pShip):
	# Setup the stream.
	# Allocate a local buffer stream.
	debug(__name__ + ", TellScriptInfo")
	kStream = App.TGBufferStream()
	# Open the buffer stream with a byte buffer.
	kStream.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)
	
	# Write relevant data to the stream.
	# First write message type.
	kStream.WriteChar(chr(SET_SCRIPT_MSG))

	kStream.WriteInt(pShip.GetObjID())
        
        sShipScript = pShip.GetScript()
	iCount = 0
	# Loop through the String
	for ichar in range(len(sShipScript)):
		kStream.WriteChar(sShipScript[iCount])
		iCount = iCount + 1
	# set the last char:
	kStream.WriteChar('\0')

	pMessage = App.TGMessage_Create()
        # Yes, this is a guaranteed packet
	pMessage.SetGuaranteed(1)
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


def BruteForceGetShipSpecies(sShipType):
	debug(__name__ + ", BruteForceGetShipSpecies")
	for sRace in Races.keys():
		if Races[sRace].IsOurRace(sShipType):
			print "Found Race match:", sRace
			return sRace
	return None


# Species of the Ship
def GetShipSpecies(pShip):
	debug(__name__ + ", GetShipSpecies")
	ShipType = GetShipType(pShip)
        if not ShipType:
		print "Problem: No Ship type"
		return
	if not hasattr(Foundation.shipList, 'has_key'):
		print("Error, bad Foundation!")
                print("Try to update your Shuttle Launching Framework!")
		return
        if not Foundation.shipList.has_key(ShipType):
		print("Cannot get Race for ", ShipType, " - No Foundation entry!")
		return
        FdtnShip = Foundation.shipList[ShipType]
        if not FdtnShip:
		print "Problem: No Foundation ships"
		return
        if FdtnShip.GetRace():
                RaceName = FdtnShip.GetRace().name
        else:
		print "Problem: No Foundation Race for ship", FdtnShip.name
		return BruteForceGetShipSpecies(ShipType)
	
	return RaceName


def AddShipNameToGroup(pShip):
        # Lets get the Group of our Player:
        debug(__name__ + ", AddShipNameToGroup")
        pPlayer = MissionLib.GetPlayer()
        ShipName = pShip.GetName()
        if not pPlayer:
                return
        elif ShipName == pPlayer.GetName():
                return
        ShipID = 0
        iOurTeam = Mission10Menus.g_iTeam
	dAllTeams = Mission10Menus.g_dAllTeams
        pEnemyGroup = MissionLib.GetEnemyGroup()
        pFriendlyGroup = MissionLib.GetFriendlyGroup()
	sShipSpecies = GetShipSpecies(pShip)
	
	ShipID = dAllTeams[sShipSpecies] * -1
        pShip.SetNetPlayerID(ShipID)
        SendGroupInfo(ShipName, ShipID)


def CheckFragLimit():
        debug(__name__ + ", CheckFragLimit")
        import Multiplayer.MissionShared
        import Multiplayer.MissionMenusShared
	if (Multiplayer.MissionShared.g_bGameOver):
		# Don't check frag limit if game is over
		return

	iFragLimit = Multiplayer.MissionMenusShared.g_iFragLimit
	if (iFragLimit == -1):
		# There are no frag limits
		return

	bOver = 0
	if (g_kTeamKillsDictionary.has_key(1)):
		if (g_kTeamKillsDictionary[1] >= iFragLimit):
			# Yes, game is over.
			bOver = 1
	if (g_kTeamKillsDictionary.has_key(0)):
		if (g_kTeamKillsDictionary[0] >= iFragLimit):
			# Yes, game is over.
			bOver = 1

	if bOver:
		Multiplayer.MissionShared.EndGame(Multiplayer.MissionShared.END_NUM_FRAGS_REACHED)


def UpdateScore(iFiringPlayerID, iKills, iKilledPlayerID, iDeaths):
	# Set the new value in the dictionary
	debug(__name__ + ", UpdateScore")
	global g_kKillsDictionary
	global g_kDeathsDictionary

	if (iFiringPlayerID != 0):
		g_kKillsDictionary[iFiringPlayerID] = iKills

	g_kDeathsDictionary[iKilledPlayerID] = iDeaths

        # Do a little subtitle announcing the kill.
        pNetwork = App.g_kUtopiaModule.GetNetwork()
        if pNetwork:
                # Create a subtitle action to display the fact that a kill/death occurred.
                pPlayerList = pNetwork.GetPlayerList()
                pPlayer = pPlayerList.GetPlayer(iKilledPlayerID)
                if pPlayer:
                        DoKillSubtitle(iFiringPlayerID, pPlayer.GetName().GetCString())

	# Update the interface
	Mission10Menus.RebuildPlayerList()


def DoKillSubtitle(iFiringPlayerID, iKilledPlayer):
        debug(__name__ + ", DoKillSubtitle")
        pFBCMPDatabase = App.g_kLocalizationManager.Load("data/TGL/FBCMP.tgl")

        pcSubString = None
        
        pString = pFBCMPDatabase.GetString("Killed")
        pcString = pString.GetCString()
        pcSubString = pcString % (iKilledPlayer)

	if (pcSubString != None):
		# Okay, there's a subtitle to display
		pSequence = App.TGSequence_Create()
		pSubtitleAction = App.SubtitleAction_CreateC(pcSubString)
		pSubtitleAction.SetDuration(5.0)
		pSequence.AddAction(pSubtitleAction)
		pSequence.Play()

		
def NewPlayerHandler(TGObject, pEvent):
	# check if player is host and not dedicated server.  If dedicated server, don't
	# add the host in as a player.
	debug(__name__ + ", NewPlayerHandler")
	iPlayerID = pEvent.GetPlayerID()

	# Check if this player is already in the dictionary.
	global g_kKillsDictionary 
	global g_kDeathsDictionary 

	if (not g_kKillsDictionary.has_key(iPlayerID)):
		# Add a blank key
		g_kKillsDictionary[iPlayerID] = 0		# No kills

	if (not g_kDeathsDictionary.has_key (iPlayerID)):
		# Add a blank key
		g_kDeathsDictionary[iPlayerID] = 0		# No deaths

	# Rebuild the player list since a new player was added
	Mission10Menus.RebuildPlayerList()

	if MissionLib.GetPlayer():
		TellScriptInfo(MissionLib.GetPlayer())

	if App.g_kUtopiaModule.IsHost():
		for iShipID in dReplaceModel.keys():
			SentReplaceModelMessage(iShipID, dReplaceModel[iShipID])

	TGObject.CallNextHandler(pEvent)


def DeletePlayerHandler(TGObject, pEvent):
	# We only handle this event if we're still connected.  If we've been disconnected,
	# then we don't handle this event since we want to preserve the score list to display
	# as the end game dialog.

	debug(__name__ + ", DeletePlayerHandler")
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	if (pNetwork):
		if (pNetwork.GetConnectStatus() == App.TGNETWORK_CONNECTED or pNetwork.GetConnectStatus() == App.TGNETWORK_CONNECT_IN_PROGRESS):
			# We do not remove the player from the dictionary.  This way, if the
			# player rejoins, his score will be preserved.
			
			# Rebuild the player list since a player was removed.
			Mission10Menus.RebuildPlayerList()
	return


def DeleteSequence(pAction, pSet, pShipName):
        debug(__name__ + ", DeleteSequence")
        if MissionLib.GetShip(pShipName):
                pSet.RemoveObjectFromSet(pShipName)
                return 0
        print "Ship to delete %s not presend anymore" % pShipName
        return 1


def DeleteObjectFromSetTimer(pSet, pShipName, Time):
        debug(__name__ + ", DeleteObjectFromSetTimer")
        pSeq = App.TGSequence_Create()
        pAction = App.TGScriptAction_Create(__name__, "DeleteSequence", pSet, pShipName)
        pSeq.AppendAction(pAction, Time)
        pSeq.Play()


def getGroupFromShip(sShipName):
	debug(__name__ + ", getGroupFromShip")
	pFriendlys = MissionLib.GetFriendlyGroup()
	pEnemys = MissionLib.GetEnemyGroup()
	pNeutrals = MissionLib.GetNeutralGroup()
	if pFriendlys.IsNameInGroup(sShipName):
		return "friendly"
	elif pEnemys.IsNameInGroup(sShipName):
		return "enemy"
	elif pNeutrals.IsNameInGroup(sShipName):
		return "neutral"
	return None


def GetFoundationAI(pShip, sGroup):
	debug(__name__ + ", GetFoundationAI")
	if GetShipType(pShip):
		FdtnShips = Foundation.shipList
                sShipType = GetShipType(pShip)
                if FdtnShips.has_key(sShipType):
		        ship = FdtnShips[sShipType]
		        if sGroup == "friendly":
			        return ship.StrFriendlyAI()
		        elif sGroup == "enemy":
			        return ship.StrEnemyAI()
	        return None


def getGroup(sGroupName):
	debug(__name__ + ", getGroup")
	if sGroupName == "friendly":
		return MissionLib.GetFriendlyGroup()
	elif sGroupName == "enemy":
		return MissionLib.GetEnemyGroup()
	else:
		return MissionLib.GetNeutralGroup()


def autoAI(pShip):
	debug(__name__ + ", autoAI")
	if not pShip or not App.g_kUtopiaModule.IsHost():
		return
		
	if getGroupFromShip(pShip.GetName()) == "friendly":
		pFdtnAI = GetFoundationAI(pShip, "friendly")
                if not pFdtnAI:
                        return
		
		if pFdtnAI == "QuickBattleFriendlyAI":
			pShip.SetAI(CreateFriendlyAI(pShip, getGroup("enemy")))
		elif pFdtnAI == "StarbaseFriendlyAI":
			# Add the starbase itself to the attacker list -- the AI needs to have
			# *something* on the attacker list so as not to crash, but it won't
			# try to attack itself
			pEnemies = getGroup("enemy")
			#AddNameToGroup(pEnemies, pShip.GetName())
			pShip.SetAI(CreateStarbaseFriendlyAI(pShip, getGroup("enemy")))
			#RemoveNameFromGroup(pEnemies, pShip.GetName())
                else:
                        pAIModule = __import__("QuickBattle." + pFdtnAI)
                        try:
                                pShip.SetAI(pAIModule.CreateAI(pShip, getGroup("enemy")))
                        except:
                                pShip.SetAI(pAIModule.CreateAI(pShip))

	elif getGroupFromShip(pShip.GetName()) == "enemy":
		pFdtnAI = GetFoundationAI(pShip, "enemy")
                if not pFdtnAI:
                        return

                if pFdtnAI == "QuickBattleAI":
                        pShip.SetAI(CreateEnemyAI(pShip, getGroup("friendly")))
                elif pFdtnAI == "StarbaseAI":
                        # Add the starbase itself to the attacker list -- the AI needs to have
                        # *something* on the attacker list so as not to crash, but it won't
                        # try to attack itself
                        pFriendlies = getGroup("friendly")
			#AddNameToGroup(pFriendlies, pShip.GetName())
			pShip.SetAI(CreateStarbaseEnemyAI(pShip, getGroup("friendly")))
                        #RemoveNameFromGroup(pFriendlies, pShip.GetName())
                else:
                        pAIModule = __import__("QuickBattle." + pFdtnAI)
                        try:
                                pShip.SetAI(pAIModule.CreateAI(pShip, getGroup("friendly")))
                        except:
                                pShip.SetAI(pAIModule.CreateAI(pShip))


def GetShipType(pShip):
        debug(__name__ + ", GetShipType")
        if pShip and pShip.GetScript():
                return string.split(pShip.GetScript(), '.')[-1]
        return None


def ReenableCollisions(pAction, pShip):
	debug(__name__ + ", ReenableCollisions")
	pShip.SetCollisionsOn(1)
	return 0
	

def IsEscapePod(sShipScript):
	debug(__name__ + ", IsEscapePod")
	if sShipScript:
		if string.find(string.lower(sShipScript), "defpod") != -1:
			return 1
		if string.find(string.lower(sShipScript), "galaxy escape pod") != -1:
			return 1
		if string.find(string.lower(sShipScript), "escapepod") != -1:
			return 1
		if string.find(string.lower(sShipScript), "greenmisc") != -1:
			return 1
		if string.find(string.lower(sShipScript), "card pod") != -1:
			return 1
	return 0


def ObjectCreatedHandler(pObject, pEvent):
        debug(__name__ + ", ObjectCreatedHandler")
        global g_lTeams, dict_Ship_to_Group, g_kTeamDictionary, g_lFirepoints
	# We only care about ships.
	pPlayer = MissionLib.GetPlayer()
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	if pShip:
		pShip.SetCollisionsOn(0)
		pSeq = App.TGSequence_Create()
		pSeq.AppendAction(App.TGScriptAction_Create(__name__, "ReenableCollisions", pShip), 5)
		pSeq.Play()
		
                if not pShip.GetName():
                        return
                pSet = pShip.GetContainingSet()
		
		# if we have the script info, tell it the others
		if pShip.GetScript():
			TellScriptInfo(pShip)
                
                # check if this is a firepoint
                if string.find(string.lower(pShip.GetName()), "firepoint") != -1:
                        #print "New Firepoint %s was created" % pShip.GetName()
                        # ok add another check if this firepoint was created by us and really should not be Targetable
                        if pPlayer and not (pShip.GetName() == "FirePoint1" + pPlayer.GetName() and pShip.IsTargetable()):
                                pShip.SetTargetable(0)
                        
                        # if it is our firepoint
                        if pPlayer and string.find(pShip.GetName(), pPlayer.GetName()) != -1:
                                g_lFirepoints.append(pShip.GetName())
                        # delete object in next 2 seconds
                        #DeleteObjectFromSetTimer(pSet, pShip.GetName(), 2)
                        return
                        
                # check if this is a HiddenCore
                elif string.find(pShip.GetName(), "HiddenCore") != -1:
                        sNewName = string.replace(pShip.GetName(), "HiddenCore", "Asteroid")
                        pShip.SetName(sNewName)
                
                if dict_Ship_to_Group.has_key(pShip.GetName()):
                        pShip.SetNetPlayerID(dict_Ship_to_Group[pShip.GetName()])
                        del dict_Ship_to_Group[pShip.GetName()]
                else:
		        pEnemyGroup = MissionLib.GetEnemyGroup()
		        pFriendlyGroup = MissionLib.GetFriendlyGroup()
                        if not g_kTeamDictionary.has_key(pShip.GetName()):
                                if not pShip.IsPlayerShip() and (pEnemyGroup.IsNameInGroup(pShip.GetName()) or pFriendlyGroup.IsNameInGroup(pShip.GetName())) and not IsEscapePod(pShip.GetScript()):
                                        # looks like we created this Ship - inform all other Players
                                        AddShipNameToGroup(pShip)
                                        Mission10Menus.RebuildPlayerList()
                
		#iGroup = pShip.GetNetPlayerID() * -1
		sRace = GetShipSpecies(pShip)
		if sRace:
			iGroup = Races.keys().index(sRace)
			AddNameToGroup(g_lTeams[iGroup], pShip.GetName())
			RemoveNameFromAllGroupsBut(iGroup, pShip.GetName())
			ResetEnemyFriendlyGroups()
                
                # Set AI if it is not there
                if App.g_kUtopiaModule.IsHost() and pShip.GetNetPlayerID() < 0:
                        #print "Setting autoAI for", pShip.GetName()
                        autoAI(pShip)

                iPlayerID = pShip.GetNetPlayerID()
		if iPlayerID >= 0:
			# print("In object created handler is player ship")
			# A player ship just got created, we need to update the info pane
			Mission10Menus.RebuildInfoPane()

                        # Figure out if it goes in the attacker group
                        #if g_kTeamDictionary.has_key(iPlayerID):
			#        iTeam = g_kTeamDictionary[iPlayerID]
			#        if iTeam == 0:
                        #                AddNameToGroup(g_pTeam1, pShip.GetName())
                        #                RemoveNameFromGroup(g_pTeam2, pShip.GetName())
                        #        else:
                        #                AddNameToGroup(g_pTeam2, pShip.GetName())
                        #                RemoveNameFromGroup(g_pTeam1, pShip.GetName())
			#        # A new ship has entered the world.  Reset the friendly enemy group assignments
			#        ResetEnemyFriendlyGroups()

                # try NanoFX Trigger
                # replaced by Foundation Trigger!
		#if Mission10Meus.CheckActiveMutator("NanoFX v2.0 BETA"):
		#	import Custom.NanoFXv2.SpecialFX.BlinkerFX
		#	Custom.NanoFXv2.SpecialFX.BlinkerFX.CreateBlinkerFX(pShip)
		
		# Foundation Trigger stuff
                try:
		        pEvent = App.TGEvent_Create()
		        pEvent.SetEventType(Foundation.TriggerDef.ET_FND_CREATE_SHIP)
		        pEvent.SetDestination(pShip)
		        App.g_kEventManager.AddEvent(pEvent)
                except:
                        pass
		
		if pShip.GetNetPlayerID() < 0:
			sShipType = GetShipType(pShip)
			sRace = GetRaceFromShipType(sShipType)
			if sRace:
				Races[sRace].BuildShip(sShipType)	

        pObject.CallNextHandler(pEvent)


def RestartGameHandler(pObject, pEvent):
        debug(__name__ + ", RestartGameHandler")
        import Multiplayer.MissionShared
	pNetwork = App.g_kUtopiaModule.GetNetwork()

	if (not pNetwork):
		return

	# Okay, we're restarting the game.
	
	# Send Message to everybody to restart
	pMessage = App.TGMessage_Create()
	pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet
	
	# Setup the stream.
	kStream = App.TGBufferStream()		# Allocate a local buffer stream.
	kStream.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with a byte buffer.
	
	# Write relevant data to the stream.
	# First write message type.
	kStream.WriteChar(chr(Multiplayer.MissionShared.RESTART_GAME_MESSAGE))

	# Okay, now set the data from the buffer stream to the message
	pMessage.SetDataFromStream(kStream)

	# Send the message.
	pNetwork.SendTGMessage(0, pMessage)
        
        # Load new Bridge
        #Mission10Menus.LoadBridge()
        
        # Restart Engineering
        Mission10Menus.LoadQBautostart(2)


def RestartGame():
        debug(__name__ + ", RestartGame")
        global g_lTeams, curShipNum
        import Multiplayer.MissionShared
        import Multiplayer.MissionMenusShared
	# Reset scoreboard.
	# Clear dictionaries
	global g_kKillsDictionary 
	global g_kDeathsDictionary 
	global g_kScoresDictionary 
	global g_kDamageDictionary 
	global g_kTeamDictionary 
	global g_kTeamScoreDictionary 
	global g_kTeamKillsDictionary 
	global g_bEndCutsceneStarted

	for iKey in g_kKillsDictionary.keys ():
		g_kKillsDictionary[iKey] = 0	

	for iKey in g_kDeathsDictionary.keys ():
		g_kDeathsDictionary[iKey] = 0

	for iKey in g_kScoresDictionary.keys ():
		g_kScoresDictionary[iKey] = 0

	for iKey in g_kDamageDictionary.keys ():
		g_kDamageDictionary[iKey] = 0

	for iKey in g_kTeamDictionary.keys ():
		g_kTeamDictionary[iKey] = 0

	for iKey in g_kTeamKillsDictionary.keys ():
		g_kTeamKillsDictionary[iKey] = 0

	for iKey in g_kTeamScoreDictionary.keys ():
		g_kTeamScoreDictionary[iKey] = 0

	# Clear game over flag
	Multiplayer.MissionShared.g_bGameOver = 0

	# Clear ships again just in case
	Multiplayer.MissionShared.ClearShips()

	# Make sure we've killed the Ship1, even if it's exploding
	#ClearShips(1)

	# Rebuild score board
	Mission10Menus.RebuildPlayerList()

	global g_bStarbaseDead
	g_bStarbaseDead = 0

	g_bEndCutsceneStarted = 0

	# Reset time limit
	if (Multiplayer.MissionMenusShared.g_iTimeLimit != -1):
		Multiplayer.MissionShared.g_iTimeLeft = Multiplayer.MissionMenusShared.g_iTimeLimit * 60
	
	# Clear all groups.
	for pGroup in g_lTeams:
		pGroup.RemoveAllNames()

        pEnemyGroup = MissionLib.GetEnemyGroup()
        pFriendlyGroup = MissionLib.GetFriendlyGroup()
        
        pEnemyGroup.RemoveAllNames()
        pFriendlyGroup.RemoveAllNames()
        
        # we can start with a Ship with number 1 again...
        curShipNum = 1

	# Turn off the chat window and put it back where it belongs
	pTopWindow = App.TopWindow_GetTopWindow()
	pMultWindow = App.MultiplayerWindow_Cast(pTopWindow.FindMainWindow(App.MWT_MULTIPLAYER))
	pChatWindow = pMultWindow.GetChatWindow()
	pChatWindow.SetPosition(0.0, 0.0, 0)
	if pChatWindow.IsVisible():
		pMultWindow.ToggleChatWindow()

	# Treat as if ship got killed, so go to select ship screen.
	Multiplayer.MissionMenusShared.ShowShipSelectScreen()

        # Load new Bridge
        #Mission10Menus.LoadBridge()
        
        # Restart Engineering
        Mission10Menus.LoadQBautostart(2)


def ResetEnemyFriendlyGroups():
	# Go through all the ships in the world, assigned them to
	# friendly/enemy based on team assignment
	debug(__name__ + ", ResetEnemyFriendlyGroups")
	iOurTeam = Mission10Menus.g_iTeam

	# Go through player list, trying to find all the ships
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	pGame = App.MultiplayerGame_Cast(App.Game_GetCurrentGame())
	if (pNetwork and pGame):
		pMission = MissionLib.GetMission()
		pEnemyGroup = MissionLib.GetEnemyGroup()
		pFriendlyGroup = MissionLib.GetFriendlyGroup()

		# First clear the groups.  We will be readding everybody
		# so we want to start with an empty group.
                # Warning: if we clear the groups we will have problems
                # to assign ships to their correct group
		#pEnemyGroup.RemoveAllNames()
		#pFriendlyGroup.RemoveAllNames()

		pPlayerList = pNetwork.GetPlayerList()
		iNumPlayers = pPlayerList.GetNumPlayers()

		pPlayer = MissionLib.GetPlayer()
		sPlayerRace = GetShipSpecies(pPlayer)
		for sRace in Mission10Menus.g_dAllTeams.keys():
			iTeam = Mission10Menus.g_dAllTeams[sRace]
			pTeam = g_lTeams[iTeam]
			
			for sShipName in pTeam.GetNameTuple():
				if not Races.has_key(sPlayerRace):
					continue
				if sPlayerRace == sRace or Races[sPlayerRace].IsFriendlyRace(sRace):
					AddNameToGroup(pFriendlyGroup, sShipName)
					RemoveNameFromGroup(pEnemyGroup, sShipName)
				elif Races[sPlayerRace].IsEnemyRace(sRace):
					AddNameToGroup(pEnemyGroup, sShipName)
					RemoveNameFromGroup(pFriendlyGroup, sShipName)
				pShip = MissionLib.GetShip(sShipName)
				if pShip and not pShip.GetNetPlayerID() > 0:
					autoAI(pShip)


def IsSameTeam(iObj1PlayerID, iObj2PlayerID):
	# Get the team of the obj1
	debug(__name__ + ", IsSameTeam")
	if(iObj1PlayerID != 0):
		if(iObj2PlayerID != 0):
			# Okay, these are player ships.  Determine if they're
			# on the same team
			iObj1Team = INVALID_TEAM
			iObj2Team = INVALID_TEAM
								
			if (g_kTeamDictionary.has_key(iObj1PlayerID)):
				iObj1Team = g_kTeamDictionary[iObj1PlayerID]

				if (g_kTeamDictionary.has_key(iObj2PlayerID)):
					iObj2Team = g_kTeamDictionary[iObj2PlayerID]

					# Okay got both teams
					if (iObj1Team == iObj2Team):
						return 1
					else:
						return 0


def GetRaceFromShipType(sShipType):
        debug(__name__ + ", GetRaceFromShipType")
        if Foundation.shipList.has_key(sShipType):
                FdtnShip = Foundation.shipList[sShipType]
        
                if FdtnShip.GetRace():
                        return FdtnShip.GetRace().name
        return None


def InformAboutShipBuild(iTeam, iSpecies):
	debug(__name__ + ", InformAboutShipBuild")
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	
        # Now send a message to everybody else that the score was updated.
        # allocate the message.
        pMessage = App.TGMessage_Create()
	pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet
	               
        # Setup the stream.
        kStream = App.TGBufferStream()		# Allocate a local buffer stream.
        kStream.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
	
        # Write relevant data to the stream.
        # First write message type.
        kStream.WriteChar(chr(PLAYER_NOW_USING_SHIP))
                                        
        kStream.WriteInt(iTeam)
	kStream.WriteInt(iSpecies)

        # Okay, now set the data from the buffer stream to the message
        pMessage.SetDataFromStream(kStream)

        # Send the message to everybody but me.  Use the NoMe group, which
        # is set up by the multiplayer game.
        pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
        # We're done.  Close the buffer.
        kStream.CloseBuffer()


def DeleteObjectFromSet(pSet, pShip, bGotViaMP=0):
	debug(__name__ + ", DeleteObjectFromSet")
	
	pShip.SetDead()
	if pSet:
		pSet.RemoveObjectFromSet(pShip.GetName())

	if not bGotViaMP:
		pNetwork = App.g_kUtopiaModule.GetNetwork()
		
		# Now send a message to everybody else that the score was updated.
		# allocate the message.
		pMessage = App.TGMessage_Create()
		pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet
			       
		# Setup the stream.
		kStream = App.TGBufferStream()		# Allocate a local buffer stream.
		kStream.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
		
		# Write relevant data to the stream.
		# First write message type.
		kStream.WriteChar(chr(DELETE_OBJECT_FROM_SET_MSG))
						
		kStream.WriteInt(pShip.GetObjID())

		# Okay, now set the data from the buffer stream to the message
		pMessage.SetDataFromStream(kStream)

		if not App.IsNull(pNetwork):
			if App.g_kUtopiaModule.IsHost():
				pNetwork.SendTGMessageToGroup("NoMe", pMessage)
			else:
				pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
		# We're done.  Close the buffer.
		kStream.CloseBuffer()


def SentReplaceModelMessage(iShipID, sNewShipScript):
        # Setup the stream.
        # Allocate a local buffer stream.
        debug(__name__ + ", SentReplaceModelMessage")
        kStream = App.TGBufferStream()
        # Open the buffer stream with a 256 byte buffer.
        kStream.OpenBuffer(256)
        # Write relevant data to the stream.
        # First write message type.
        kStream.WriteChar(chr(REPLACE_MODEL_MSG))

	# send Message
	kStream.WriteInt(iShipID)
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


# returns ship status values, such as damage and shield status in a dictionary
def getShipAttributes(pShip):
        debug(__name__ + ", getShipAttributes")
        dict_ShipAttrs = {}
        pPropSet = pShip.GetPropertySet()
        pShipSubSystemPropInstanceList = pPropSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
        if pShipSubSystemPropInstanceList:
                iNumItems = pShipSubSystemPropInstanceList.TGGetNumItems()
                pShipSubSystemPropInstanceList.TGBeginIteration()
                for i in range(iNumItems):
                        pInstance = pShipSubSystemPropInstanceList.TGGetNext()
                        pProperty = App.SubsystemProperty_Cast(pInstance.GetProperty())
                        sName = pProperty.GetName().GetCString()
                        # bad - find a better way!
                        pSubsystem = MissionLib.GetSubsystemByName(pShip, sName)
                        dict_ShipAttrs[sName] = pSubsystem.GetConditionPercentage()
                pShipSubSystemPropInstanceList.TGDoneIterating()
        
        dict_ShipAttrs["MiscAttributes"] = {}
        # shields
        dict_ShipAttrs["MiscAttributes"]["shields"] = {}
        for iShield in range(App.ShieldClass.NUM_SHIELDS):
                dict_ShipAttrs["MiscAttributes"]["shields"][iShield] = pShip.GetShields().GetCurShields(iShield)
        
        return dict_ShipAttrs


def MPGetShipAttributes(pShip):
	debug(__name__ + ", MPGetShipAttributes")
	
	global gdShipAttrs
	
	if App.g_kUtopiaModule.IsHost():
		gdShipAttrs[pShip.GetObjID()] = getShipAttributes(pShip)
	else:
        	# Setup the stream.
        	# Allocate a local buffer stream.
        	kStream = App.TGBufferStream()
        	# Open the buffer stream with a 256 byte buffer.
        	kStream.OpenBuffer(256)
        	# Write relevant data to the stream.
        	# First write message type.
        	kStream.WriteChar(chr(SET_GET_SHIP_ATTR_MSG))

		# send Message
		kStream.WriteInt(0) # get
		kStream.WriteInt(pShip.GetObjID())
		kStream.WriteInt(0)

        	pMessage = App.TGMessage_Create()
       	 	# Yes, this is a guaranteed packet
		pMessage.SetGuaranteed(1)
        	# Okay, now set the data from the buffer stream to the message
        	pMessage.SetDataFromStream(kStream)
        	# Send the message to everybody but me.  Use the NoMe group, which
        	# is set up by the multiplayer game.
	        pNetwork = App.g_kUtopiaModule.GetNetwork()
        	if not App.IsNull(pNetwork):
                        pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
        	# We're done.  Close the buffer.
        	kStream.CloseBuffer()


def RestoreShipAttributes(pShip, dict_ShipAttrs):
        debug(__name__ + ", RestoreShipAttributes")
        for sSubsystemName in dict_ShipAttrs.keys():
                if sSubsystemName != "MiscAttributes":
                        pSubsystem = MissionLib.GetSubsystemByName(pShip, sSubsystemName)
                        if pSubsystem:
                                pSubsystem.SetConditionPercentage(dict_ShipAttrs[sSubsystemName])
        # shields
        dict_Shields = dict_ShipAttrs["MiscAttributes"]["shields"]
        for iShield in range(App.ShieldClass.NUM_SHIELDS):
                pShip.GetShields().SetCurShields(iShield, dict_Shields[iShield])


def MPSetShipAttributes(pShip, iShipFromID):
	debug(__name__ + ", MPSetShipAttributes")
		
	if App.g_kUtopiaModule.IsHost():
		if gdShipAttrs.has_key(iShipFromID):
			RestoreShipAttributes(pShip, gdShipAttrs[iShipFromID])
	else:
        	# Setup the stream.
        	# Allocate a local buffer stream.
        	kStream = App.TGBufferStream()
        	# Open the buffer stream with a 256 byte buffer.
        	kStream.OpenBuffer(256)
        	# Write relevant data to the stream.
        	# First write message type.
        	kStream.WriteChar(chr(SET_GET_SHIP_ATTR_MSG))

		# send Message
		kStream.WriteInt(1) # set
		kStream.WriteInt(pShip.GetObjID())
		kStream.WriteInt(iShipFromID)

        	pMessage = App.TGMessage_Create()
       	 	# Yes, this is a guaranteed packet
		pMessage.SetGuaranteed(1)
        	# Okay, now set the data from the buffer stream to the message
        	pMessage.SetDataFromStream(kStream)
        	# Send the message to everybody but me.  Use the NoMe group, which
        	# is set up by the multiplayer game.
	        pNetwork = App.g_kUtopiaModule.GetNetwork()
        	if not App.IsNull(pNetwork):
                        pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
        	# We're done.  Close the buffer.
        	kStream.CloseBuffer()


def CreateFriendlyAI(pShip, pEnemies):
        debug(__name__ + ", CreateFriendlyAI")
        if not pEnemies.GetNameTuple():
            pEnemies.AddName("This ship probably wont exist")
	#########################################
	# Creating CompoundAI Attack at (194, 57)
	import AI.Compound.BasicAttack
	pAttack = AI.Compound.BasicAttack.CreateAI(pShip, pEnemies, Difficulty = 1, FollowTargetThroughWarp=1, UseCloaking=1)
	# Done creating CompoundAI Attack
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (83, 155)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 12, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pAttack)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (41, 304)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pWait)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	return pAvoidObstacles


def CreateEnemyAI(pShip, pFriendlies):
        debug(__name__ + ", CreateEnemyAI")
        if not pFriendlies.GetNameTuple():
            pFriendlies.AddName("This ship probably wont exist")
	#########################################
	# Creating CompoundAI Attack at (108, 133)
	import AI.Compound.BasicAttack
	pAttack = AI.Compound.BasicAttack.CreateAI(pShip, pFriendlies, Difficulty = 1, FollowTargetThroughWarp = 1, UseCloaking = 1)
	# Done creating CompoundAI Attack
	#########################################
	#########################################
	# Creating PlainAI Turn at (237, 47)
	pTurn = App.PlainAI_Create(pShip, "Turn")
	pTurn.SetScriptModule("ManeuverLoop")
	pTurn.SetInterruptable(1)
	pScript = pTurn.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelLeft())
	# Done creating PlainAI Turn
	#########################################
	#########################################
	# Creating PlainAI Turn_2 at (353, 55)
	pTurn_2 = App.PlainAI_Create(pShip, "Turn_2")
	pTurn_2.SetScriptModule("ManeuverLoop")
	pTurn_2.SetInterruptable(1)
	pScript = pTurn_2.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelRight())
	# Done creating PlainAI Turn_2
	#########################################
	#########################################
	# Creating PlainAI Turn_3 at (429, 103)
	pTurn_3 = App.PlainAI_Create(pShip, "Turn_3")
	pTurn_3.SetScriptModule("ManeuverLoop")
	pTurn_3.SetInterruptable(1)
	pScript = pTurn_3.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelUp())
	# Done creating PlainAI Turn_3
	#########################################
	#########################################
	# Creating PlainAI Turn_4 at (448, 147)
	pTurn_4 = App.PlainAI_Create(pShip, "Turn_4")
	pTurn_4.SetScriptModule("ManeuverLoop")
	pTurn_4.SetInterruptable(1)
	pScript = pTurn_4.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelDown())
	# Done creating PlainAI Turn_4
	#########################################
	#########################################
	# Creating RandomAI FlyPointlessly at (198, 181)
	pFlyPointlessly = App.RandomAI_Create(pShip, "FlyPointlessly")
	pFlyPointlessly.SetInterruptable(1)
	# SeqBlock is at (309, 185)
	pFlyPointlessly.AddAI(pTurn)
	pFlyPointlessly.AddAI(pTurn_2)
	pFlyPointlessly.AddAI(pTurn_3)
	pFlyPointlessly.AddAI(pTurn_4)
	# Done creating RandomAI FlyPointlessly
	#########################################
	#########################################
	# Creating SequenceAI RepeatForever at (195, 224)
	pRepeatForever = App.SequenceAI_Create(pShip, "RepeatForever")
	pRepeatForever.SetInterruptable(1)
	pRepeatForever.SetLoopCount(-1)
	pRepeatForever.SetResetIfInterrupted(1)
	pRepeatForever.SetDoubleCheckAllDone(1)
	pRepeatForever.SetSkipDormant(0)
	# SeqBlock is at (295, 228)
	pRepeatForever.AddAI(pFlyPointlessly)
	# Done creating SequenceAI RepeatForever
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (30, 228)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (149, 235)
	pPriorityList.AddAI(pAttack, 1)
	pPriorityList.AddAI(pRepeatForever, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (29, 285)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pPriorityList)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (29, 332)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 12, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pAvoidObstacles)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	return pWait


def CreateStarbaseFriendlyAI(pShip, pEnemies):
        debug(__name__ + ", CreateStarbaseFriendlyAI")
        if not pEnemies.GetNameTuple():
            pEnemies.AddName("This ship probably wont exist")
	#########################################
	# Creating CompoundAI StarbaseAttack at (194, 57)
	import AI.Compound.StarbaseAttack
	pStarbaseAttack = AI.Compound.StarbaseAttack.CreateAI(pShip, pEnemies)
	# Done creating CompoundAI StarbaseAttack
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (83, 155)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 7, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pStarbaseAttack)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	return pWait


def CreateStarbaseEnemyAI(pShip, pFriendlies):
	#########################################
	# Creating CompoundAI StarbaseAttack at (194, 57)
	debug(__name__ + ", CreateStarbaseEnemyAI")
	import AI.Compound.StarbaseAttack
	pStarbaseAttack = AI.Compound.StarbaseAttack.CreateAI(pShip, pFriendlies)
	# Done creating CompoundAI StarbaseAttack
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (83, 155)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 7, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pStarbaseAttack)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	return pWait

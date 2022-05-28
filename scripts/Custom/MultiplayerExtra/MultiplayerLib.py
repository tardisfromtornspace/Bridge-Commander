from bcdebug import debug
# 2006 by Defiant - erik@bckobayashimaru.de


import App
import MissionLib
import loadspacehelper
import Multiplayer.MissionShared
import string

MP_NEW_NET_PLAYER_ID = 205
DELETE_OBJECT_FROM_SET_MSG = 211
SET_GET_SHIP_ATTR_MSG = 212
SET_AUTO_AI_MSG = 213
SET_STOP_AI_MSG = 214

NonSerializedObjects = ( "gdShipAttrs", )
gdShipAttrs = {}

def CreateMessageStream(iMessageType):
	debug(__name__ + ", CreateMessageStream")
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	pMessage = App.TGMessage_Create()
	pMessage.SetGuaranteed(1)
	kStream = App.TGBufferStream()
	kStream.OpenBuffer(256)
	kStream.WriteChar(chr(iMessageType))
	return pMessage, kStream


def SendMessageToEveryone(pMessage, kStream):
	debug(__name__ + ", SendMessageToEveryone")
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	pMessage.SetDataFromStream(kStream)
	if not App.IsNull(pNetwork):
		if App.g_kUtopiaModule.IsHost():
			pNetwork.SendTGMessageToGroup("NoMe", pMessage)
		else:
			pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage) # Host has to forward for us
	kStream.CloseBuffer()


def SendMessageToHost(pMessage, kStream):
	debug(__name__ + ", SendMessageToHost")
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	pMessage.SetDataFromStream(kStream)
	if not App.IsNull(pNetwork):
		pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
	kStream.CloseBuffer()
	
	
def SetNewNetPlayerID(pShip, iNetID):
	debug(__name__ + ", SetNewNetPlayerID")
	if pShip:
		pShip.SetNetPlayerID(iNetID)

	pMessage, kStream = CreateMessageStream(MP_NEW_NET_PLAYER_ID)
	kStream.WriteInt(pShip.GetObjID())
	kStream.WriteInt(iNetID)
	SendMessageToEveryone(pMessage, kStream)


def MPSetAutoAI(pShip):
	if not pShip:
		return
	pMessage, kStream = CreateMessageStream(SET_AUTO_AI_MSG)
	kStream.WriteInt(pShip.GetObjID())
	SendMessageToHost(pMessage, kStream)


def SetStopAI(pShip):
	if not pShip:
		return
	if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
		import AI.Player.Stay
		pShip.SetAI(AI.Player.Stay.CreateAI(pShip))
	else:
		pMessage, kStream = CreateMessageStream(SET_STOP_AI_MSG)
		kStream.WriteInt(pShip.GetObjID())
		SendMessageToHost(pMessage, kStream)
	

def GetShipType(pShip):
        debug(__name__ + ", GetShipType")
        if pShip.GetScript():
                return string.split(pShip.GetScript(), '.')[-1]
        return None


def CreatePlayerShipFromShip(pShip):
	pGame = App.Game_GetCurrentGame()
	pMultGame = App.MultiplayerGame_Cast(pGame)
	
	if not App.g_kUtopiaModule.IsMultiplayer():
		pGame.SetPlayer(pShip)
		return pShip
	
	pSet = pShip.GetContainingSet()
	pcName = pShip.GetName()
	kLocation = pShip.GetWorldLocation()
	kForward = pShip.GetWorldForwardTG()
	kUp = pShip.GetWorldUpTG()
	iShipOldID = pShip.GetObjID()
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	pcScript = GetShipType(pShip)
	
	if not pcScript:
		print "No Script Error: Return"
		return
	
	pObject = loadspacehelper.CreateShip(pcScript, None, pcName, "", 0, 1)
	
	if pObject:
		pObject.SetNetPlayerID(pNetwork.GetLocalID())

		MPGetShipAttributes(pShip)
		DeleteObjectFromSet(pSet, pShip)
		MPSetShipAttributes(pObject, iShipOldID)
		pObject.SetTranslate(kLocation)
		pObject.AlignToVectors(kForward, kUp)
			
		pSet.AddObjectToSet(pObject, pcName)
		pMultGame.SetPlayer(pObject)
		
		return pObject


def CreateShipFromShip(pShip):
	pGame = App.Game_GetCurrentGame()
	pMultGame = App.MultiplayerGame_Cast(pGame)
	
	if not App.g_kUtopiaModule.IsMultiplayer():
		return pShip
	
	pSet = pShip.GetContainingSet()
	pcName = pShip.GetName()
	kLocation = pShip.GetWorldLocation()
	kForward = pShip.GetWorldForwardTG()
	kUp = pShip.GetWorldUpTG()
	iShipOldID = pShip.GetObjID()
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	pcScript = GetShipType(pShip)
	
	if not pcScript:
		print "No Script Error: Return"
		return
	
	pObject = loadspacehelper.CreateShip(pcScript, None, pcName, "", 0, 1)
	
	if pObject:
		pObject.SetNetPlayerID(pShip.GetNetPlayerID())

		MPGetShipAttributes(pShip)
		DeleteObjectFromSet(pSet, pShip)
		MPSetShipAttributes(pObject, iShipOldID)
		pObject.SetTranslate(kLocation)
		pObject.AlignToVectors(kForward, kUp)
			
		pSet.AddObjectToSet(pObject, pcName)
		
		return pObject
		

def DeleteObjectFromSet(pSet, pShip):
	debug(__name__ + ", DeleteObjectFromSet")
	
	pShip.SetDead()
	pShip.SetDeleteMe(1)
	pSet.DeleteObjectFromSet(pShip.GetName())

	if App.g_kUtopiaModule.IsMultiplayer():
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

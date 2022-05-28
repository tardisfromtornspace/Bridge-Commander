from bcdebug import debug
import App
import MissionLib
import Lib.LibEngineering
import loadspacehelper
import string
from Libs.LibQBautostart import *

AUTO_TARGET_EXPLOSION_POINT = 1
LastUpdateTimeWeaponHit = 0
LastUpdateTimeScan = 0
FirePointName = "Unknown Explosion"
sFirePointScanDetectName = "Unknown Anomaly"
REMOVE_POINTER_FROM_SET = 190
NO_COLLISION_MESSAGE = 192
ET_CLIENT_SCAN = 197
dict_lockNoFirepoint = {}
FIREPOINT_LIVETIME = 4

MODINFO = {     "Author": "\"Defiant\" erik@vontaene.de",
                "Version": "0.1",
                "License": "BSD",
                "Description": "Help script to find and destroy cloaked ships",
                "needBridge": 0
            }

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


def InScanRane(pShip, pObject):
        debug(__name__ + ", InScanRane")
        pSensor = pShip.GetSensorSubsystem()
        if not pSensor:
                return 0
        if pSensor.GetSensorRange() > Distance(pShip, pObject) * 3:
                return 1
        return 0


def IsScimitar(pShip):
        debug(__name__ + ", IsScimitar")
        if pShip.GetScript() and string.find(string.lower(pShip.GetScript()), "scimitar") != -1:
                return 1
        return 0
        

def DetectCloakedShips(pAction, pPlayer):
        debug(__name__ + ", DetectCloakedShips")
        pSet = pPlayer.GetContainingSet()
        
        for pShip in pSet.GetClassObjectList(App.CT_SHIP):
                if pShip.IsCloaked() and chance(10) and not IsScimitar(pShip) and InScanRane(pPlayer, pShip):
                        CreateScanFirepoint(pShip)
        return 0


def CreateScanFirepoint(pShip):
        debug(__name__ + ", CreateScanFirepoint")
        pPlayer = MissionLib.GetPlayer()
        pEnemies = MissionLib.GetEnemyGroup()
        pFriendlies = MissionLib.GetFriendlyGroup()
        
        if pShip and pPlayer:                
                # check group
                if pEnemies and pEnemies.IsNameInGroup(pShip.GetName()):
                        myFirePointName = sFirePointScanDetectName + " E"
                        group = "enemy"
                elif pFriendlies and pFriendlies.IsNameInGroup(pShip.GetName()):
                        myFirePointName = sFirePointScanDetectName + " F"
                        group = "friendly"
                else:
                        myFirePointName = sFirePointScanDetectName + " N"
                        group = "neutral"
                
                pFirePoint = MissionLib.GetShip(myFirePointName)
                FirePointCoord = None
                
                # if it does not exist we have to create it first
                if not pFirePoint:
                        pFirePoint = loadspacehelper.CreateShip("Firepoint", pPlayer.GetContainingSet(), myFirePointName, None)
                        if group == "enemy" and not pEnemies.IsNameInGroup(myFirePointName):
                                pEnemies.AddName(myFirePointName)
                        elif group == "friendly" and not pFriendlies.IsNameInGroup(myFirePointName):
                                pFriendlies.AddName(myFirePointName)
                
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
                
                pFirePoint.EnableCollisionsWith(pShip, 0)
                if App.g_kUtopiaModule.IsMultiplayer():
                        MultiPlayerEnableCollisionWith(pFirePoint, pShip, 0)
                pFirePoint.SetTranslate(kLocation)
                pFirePoint.UpdateNodeOnly()
		pShip.AttachObject(pFirePoint)

		LastUpdateTimeScan = App.g_kUtopiaModule.GetGameTime()

		if AUTO_TARGET_EXPLOSION_POINT and not pPlayer.GetTarget() or isFirepoint(pPlayer.GetTarget()) != -1:
			pPlayer.SetTarget(pFirePoint.GetName())
                                
                pSeq = App.TGSequence_Create()
                pSeq.AppendAction(App.TGScriptAction_Create(__name__, "DeleteFirePointAfterScan", myFirePointName), FIREPOINT_LIVETIME)
                pSeq.Play()


def isFirepoint(pShip):
	debug(__name__ + ", isFirepoint")
	if pShip:
		return string.find(string.lower(pShip.GetName()), "firepoint")
	return -1


def DetectShipsInFrontOf(pShip):
	debug(__name__ + ", DetectShipsInFrontOf")
	sGroup = getGroupFromShip(pShip.GetName())
	lCloakedShips = GetCloakedShipsNotIn(pShip.GetContainingSet(), sGroup)
	for pCloakedShip in lCloakedShips:
		# from Conditions.ConditionFacingToward		
		vWorldDir = App.TGPoint3()
		vWorldDir.Set(App.TGPoint3_GetModelForward())
		vWorldDir.MultMatrixLeft(pShip.GetWorldRotation())

		# Find the location direction from object 1 to object 2.
		vDiffDir = pCloakedShip.GetWorldLocation()
		vDiffDir.Subtract(pShip.GetWorldLocation())
		vDiffDir.Unitize()

		# Dot product of the 2 directions...
		fDot = vWorldDir.Dot(vDiffDir)

		# 0.85 = cos(30°)
		if fDot >= 0.85 and Distance(pShip, pCloakedShip) < 1000 and not IsScimitar(pCloakedShip):
			pSeq = App.TGSequence_Create()
			pSeq.AppendAction(App.TGScriptAction_Create(__name__, "CreateScanFirepointAction", pCloakedShip), App.g_kSystemWrapper.GetRandomNumber(10))
			pSeq.Play()



def GetFriendlyShipOfSameRaceOf(sCmpRace, sGroup, pSet):
	debug(__name__ + ", GetFriendlyShipOfSameRaceOf")
	lRet = []
	
	pGroup = getGroup(sGroup)
	lpGroup = pGroup.GetActiveObjectTupleInSet(pSet)
	for ship in lpGroup:
		sShipRace = GetRaceFromShip(ship)
		if sCmpRace == sShipRace:
			lRet.append(ship)
	
	return lRet


def GetCloakedShipsNotIn(pSet, sNotGroup):
	debug(__name__ + ", GetCloakedShipsNotIn")
	lRet = []
	
	if not pSet:
		return lRet
	
	lObjects = pSet.GetClassObjectList(App.CT_SHIP)
	for pObject in lObjects:
		pShip = App.ShipClass_Cast(pObject)
		sShipGroup = getGroupFromShip(pShip.GetName())
		if sShipGroup != sNotGroup and pShip.IsCloaked():
			lRet.append(pShip)
	
	return lRet


def GetMaxDistance(lShips):
	debug(__name__ + ", GetMaxDistance")
	fMax = 0
	
	for pShip1 in lShips:
		for pShip2 in lShips:
			fDist = Distance(pShip1, pShip2)
			if fDist > fMax:
				fMax = fDist
	
	return fMax


def CreateScanFirepointAction(pAction, pShip):
	debug(__name__ + ", CreateScanFirepointAction")
	CreateScanFirepoint(pShip)
	return 0


def DecloakShipsInNet(pShip):
	# 1. get all our ships
	debug(__name__ + ", DecloakShipsInNet")
	sRace = GetRaceFromShip(pShip)
	sGroup = getGroupFromShip(pShip.GetName())
	lOurFleet = GetFriendlyShipOfSameRaceOf(sRace, sGroup, pShip.GetContainingSet())
	# 2. get cloaked ships
	lCloakedShips = GetCloakedShipsNotIn(pShip.GetContainingSet(), sGroup)
	# 3. check if they are in our net.
	# Note: we do it a very very simple way: Just find out if the distance to one of our ships is bigger then max distance of our fleet
	fMaxDistance = GetMaxDistance(lOurFleet)
	for pCloakedShip in lCloakedShips:
		fMaxDistThisShip = 0
		for pOurShip in lOurFleet:
			fDist = Distance(pOurShip, pCloakedShip)
			if fDist > fMaxDistThisShip:
				fMaxDistThisShip = fDist
		if fMaxDistThisShip and fMaxDistThisShip < fMaxDistance:
			pSeq = App.TGSequence_Create()
			pSeq.AppendAction(App.TGScriptAction_Create(__name__, "CreateScanFirepointAction", pCloakedShip), App.g_kSystemWrapper.GetRandomNumber(10))
			pSeq.Play()


def ScanInit(pObject, pEvent):
        debug(__name__ + ", ScanInit")
        pObject.CallNextHandler(pEvent)
        
        if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
                pPlayer = MissionLib.GetPlayer()
                ShipScan(pPlayer)
		sOurRace = GetRaceFromShip(pPlayer)
		if sOurRace == "Federation":
			DecloakShipsInNet(pPlayer)
		elif sOurRace == "Dominion":
			DetectShipsInFrontOf(pPlayer)
        # we are client. Inform the Server that we are scanning
        else:
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


def ShipScan(pShip):
        # Don't do it if we are cloaked
        debug(__name__ + ", ShipScan")
        if pShip.IsCloaked():
                return
                
        pSeq = App.TGSequence_Create()
        for i in range(10):
                pSeq.AppendAction(App.TGScriptAction_Create(__name__, "DetectCloakedShips", pShip), 1)
        pSeq.Play()

        
def WeaponHit(pObject, pEvent):
        debug(__name__ + ", WeaponHit")
        global LastUpdateTimeWeaponHit, dict_lockNoFirepoint
        
        # Get the ship that was hit
        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        
        pPlayer = MissionLib.GetPlayer()
        pEnemies = MissionLib.GetEnemyGroup()
        pFriendlies = MissionLib.GetFriendlyGroup()
        
        if pShip and pShip.IsCloaked() and not dict_lockNoFirepoint.has_key(pShip.GetName()):
                #print("Cloaked Ship", pShip.GetName(), "hit")
                
                # check group
                if pEnemies and pEnemies.IsNameInGroup(pShip.GetName()):
                        myFirePointName = FirePointName + " E"
                        group = "enemy"
                elif pFriendlies and pFriendlies.IsNameInGroup(pShip.GetName()):
                        myFirePointName = FirePointName + " F"
                        group = "friendly"
                else:
                        myFirePointName = FirePointName + " N"
                        group = "neutral"
                
                pFirePoint = MissionLib.GetShip(myFirePointName)
                FirePointCoord = None
                
                # if it does not exist we have to create it first
                if not pFirePoint:
                        pFirePoint = loadspacehelper.CreateShip("Firepoint", pPlayer.GetContainingSet(), myFirePointName, None)
                        if group == "enemy" and not pEnemies.IsNameInGroup(myFirePointName):
                                pEnemies.AddName(myFirePointName)
                        elif group == "friendly" and not pFriendlies.IsNameInGroup(myFirePointName):
                                pFriendlies.AddName(myFirePointName)
                
                pFirePoint = MissionLib.GetShip(myFirePointName)
                
                # reposition
                #HitNiPoint3 = pEvent.GetWorldHitPoint()
		HitNiPoint3 = pEvent.GetObjectHitPoint()
                kLocation = App.TGPoint3()
                kLocation.SetXYZ(HitNiPoint3.x, HitNiPoint3.y, HitNiPoint3.z)
                
                pFirePoint.EnableCollisionsWith(pShip, 0)
                if App.g_kUtopiaModule.IsMultiplayer():
                        MultiPlayerEnableCollisionWith(pFirePoint, pShip, 0)
                pFirePoint.SetTranslate(kLocation)
                pFirePoint.UpdateNodeOnly()
		pShip.AttachObject(pFirePoint)
                
                LastUpdateTimeWeaponHit = App.g_kUtopiaModule.GetGameTime()
		
		if AUTO_TARGET_EXPLOSION_POINT and not pPlayer.GetTarget() or isFirepoint(pPlayer.GetTarget()) != -1:
			pPlayer.SetTarget(pFirePoint.GetName())
	
                pSeq = App.TGSequence_Create()
                pSeq.AppendAction(App.TGScriptAction_Create(__name__, "DeleteFirePointAfterWeaponHit", myFirePointName), FIREPOINT_LIVETIME)
                pSeq.Play()
        
        pObject.CallNextHandler(pEvent)


def DeleteFirePointAfterWeaponHit(pAction, myFirePointName):
	debug(__name__ + ", DeleteFirePointAfterWeaponHit")
	return DeleteFirePoint(pAction, myFirePointName, LastUpdateTimeWeaponHit)


def DeleteFirePointAfterScan(pAction, myFirePointName):
	debug(__name__ + ", DeleteFirePointAfterScan")
	return DeleteFirePoint(pAction, myFirePointName, LastUpdateTimeScan)


def DeleteFirePoint(pAction, myFirePointName, LastUpdateTime):
        debug(__name__ + ", DeleteFirePoint")
        if LastUpdateTime + FIREPOINT_LIVETIME - 1 <= App.g_kUtopiaModule.GetGameTime():
                MissionLib.GetPlayer().GetContainingSet().RemoveObjectFromSet(myFirePointName)
                        
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
        

"""
This part does not work :(
def CreateTorpedo(pObject, pEvent):
        debug(__name__ + ", CreateTorpedo")
        pPlayer = MissionLib.GetPlayer()
        if not pPlayer:
                return
        print("Creating Ion search Torp for", pPlayer)
        
	pTorpSys = pPlayer.GetTorpedoSystem()
	if pTorpSys:
		# Find proper torps..
		iNumTypes = pTorpSys.GetNumAmmoTypes()
		for iType in range(iNumTypes):
			pTorpType = pTorpSys.GetAmmoType(iType)

			if (pTorpType.GetAmmoName() == "Ion finder"):
                                iNumTorps = pTorpType.GetMaxTorpedoes()
                                pTorpSys.GetProperty().SetMaxTorpedoes(iType,  iNumTorps + 1)
                                pTorpSys.LoadAmmoType(iType, 1)
        

def PrepareTorpedo(pObject, pEvent):
        debug(__name__ + ", PrepareTorpedo")
        MissionLib.CreateTimer(Lib.LibEngineering.GetEngineeringNextEventType(), __name__ + ".CreateTorpedo", App.g_kUtopiaModule.GetGameTime() + 2.0, 0, 0)


# Get the Distance between the Ship and pObject
def Distance(pShip, pObject):
	debug(__name__ + ", Distance")
	vDifference = pObject.GetWorldLocation()
	vDifference.Subtract(pShip.GetWorldLocation())

	return vDifference.Length()


def TorpedoFired(pObject, pEvent):
        debug(__name__ + ", TorpedoFired")
        pTorp = App.Torpedo_Cast(pEvent.GetSource())
        
        if not pTorp:
                pObject.CallNextHandler(pEvent)
                return
        
        if pTorp.GetModuleName() != "Tactical.Projectiles.IonFindTorp":
                pObject.CallNextHandler(pEvent)
                return
        
        pShipID = pTorp.GetParentID()
        pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShipID)
	pEnemies = MissionLib.GetEnemyGroup()
	pFriendlies = MissionLib.GetFriendlyGroup()
        pSet = pShip.GetContainingSet()
        lpEnemies = pEnemies.GetActiveObjectTupleInSet(pSet)
        lpFriendlies = pFriendlies.GetActiveObjectTupleInSet(pSet)
        #print("Ion finder Launched", pTorp.GetTargetID(), pTorp.GetPlayerID(), pSet)
        minDistance = 10000
        minDShip = None
        for pFriendly in lpFriendlies:
                if pFriendly.GetName() != pShip.GetName() and Distance(pShip, pFriendly) < minDistance:
                        minDShip = pFriendly
                        minDistance = Distance(pShip, pFriendly)
                #print ("Comp: ", pFriendly.GetName(), pShip.GetName())
        for pEnemy in lpEnemies:
                if pEnemy.GetName() != pShip.GetName() and Distance(pShip, pEnemy) < minDistance:
                        minDShip = pEnemy
                        minDistance = Distance(pShip, pEnemy)
                #print ("Comp: ", pEnemy.GetName(), pEnemy.GetName())

        #print ("Closest Ship: ", minDShip)
        if minDShip:
                pTorp.SetTarget(minDShip.GetObjID())
                #print("Ion finder Status:", pTorp.GetTargetID(), minDShip.GetName())
        
        pObject.CallNextHandler(pEvent)"""


def CloakStart(pObject, pEvent):
        debug(__name__ + ", CloakStart")
        global dict_lockNoFirepoint
        # Get the ship that is cloaking
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if pShip:
                dict_lockNoFirepoint[pShip.GetName()] = 1
        pObject.CallNextHandler(pEvent)


def CloakDone(pObject, pEvent):
        debug(__name__ + ", CloakDone")
        global dict_lockNoFirepoint
        # Get the ship that is cloaking
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if pShip and dict_lockNoFirepoint.has_key(pShip.GetName()):
                del dict_lockNoFirepoint[pShip.GetName()]
        pObject.CallNextHandler(pEvent)


def DeactivateWeaponsAction(pAction, pShip):
        debug(__name__ + ", DeactivateWeaponsAction")

	pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
	if not pShip or pShip.IsDead() or pShip.IsDying():
		return 1

	if pShip.GetPhaserSystem():
		pShip.GetPhaserSystem().TurnOff()
	if pShip.GetPulseWeaponSystem():
		pShip.GetPulseWeaponSystem().TurnOff()
	if pShip.GetTorpedoSystem():
		pShip.GetTorpedoSystem().TurnOff()

        debug(__name__ + ", DeactivateWeaponsAction Done")

        return 0


def ReactivateWeaponsAction(pAction, pShip):
        debug(__name__ + ", ReactivateWeaponsAction")

	pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
	if not pShip or pShip.IsDead() or pShip.IsDying():
		return 1

	if pShip.GetPhaserSystem():
		pShip.GetPhaserSystem().TurnOn()
	if pShip.GetPulseWeaponSystem():
		pShip.GetPulseWeaponSystem().TurnOn()
	if pShip.GetTorpedoSystem():
		pShip.GetTorpedoSystem().TurnOn()
        debug(__name__ + ", ReactivateWeaponsAction Done")

        return 0


def DeCloakStart(pObject, pEvent):
        debug(__name__ + ", DeCloakDone")
	
        # Get the ship that is decloaking
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	if pShip:
		pSeq = App.TGSequence_Create()
        	for i in range(30):
                	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "DeactivateWeaponsAction", pShip), 0.1)
		turnon = 0
		if pShip.GetPhaserSystem() and pShip.GetPhaserSystem().IsOn():
			turnon = 1
		if pShip.GetPulseWeaponSystem() and pShip.GetPulseWeaponSystem().IsOn():
			turnon = 1
		if pShip.GetTorpedoSystem() and pShip.GetTorpedoSystem().IsOn():
			turnon = 1
		if turnon:
			pSeq.AppendAction(App.TGScriptAction_Create(__name__, "ReactivateWeaponsAction", pShip), 0.1)
        	pSeq.Play()

        pObject.CallNextHandler(pEvent)


def init():
        debug(__name__ + ", init")
        global dict_lockNoFirepoint
        
        pMission = MissionLib.GetMission()
        if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WEAPON_HIT, pMission, __name__+ ".WeaponHit")
                # adding the Firepoint in the cloaking phase seems to crash the game so avoid that
                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_CLOAK_BEGINNING, pMission, __name__+ ".CloakStart")
                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_CLOAK_COMPLETED, pMission, __name__+ ".CloakDone")
        if App.g_kUtopiaModule.IsMultiplayer():
                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_DECLOAK_BEGINNING, pMission, __name__+ ".DeCloakStart")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SCAN, pMission, __name__ + ".ScanInit")
        
        dict_lockNoFirepoint = {}

        #App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TORPEDO_FIRED, pMission, __name__+ ".TorpedoFired")

        #Lib.LibEngineering.CreateMenuButton("prepare Ion search Torpedo", "Tactical", __name__ + ".PrepareTorpedo")


def Restart():
        debug(__name__ + ", Restart")
        global dict_lockNoFirepoint
        dict_lockNoFirepoint = {}

import App
import MissionLib
import loadspacehelper
import Lib.LibEngineering
import Foundation
import string


MODINFO = { "Author": "\"Defiant\" erik@bckobayashimaru.de",
            "Version": "0.1",
            "License": "BSD",
            "Description": "P D",
            "needBridge": 0
            }
            

FirePointName = "PD Firepoint"
i_FPcount = 0
dictFirePointToTorp = {}
POINT_DEFENCE_TIMER = Lib.LibEngineering.GetEngineeringNextEventType()
REMOVE_POINTER_FROM_SET = 190
REMOVE_TORP_MESSAGE_AT = 191
TorpList = []
PDRunning = 0


def MPSendRemoveTorpMessage(pTorp):
        # Now send a message to everybody else that the score was updated.
        # allocate the message.
        pMessage = App.TGMessage_Create()
        pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet
                        
        # Setup the stream.
        kStream = App.TGBufferStream()		# Allocate a local buffer stream.
        kStream.OpenBuffer(256)				# Open the buffer stream with a 256 byte buffer.
	
        # Write relevant data to the stream.
        # First write message type.
        kStream.WriteChar(chr(REMOVE_TORP_MESSAGE_AT))

        pNetwork = App.g_kUtopiaModule.GetNetwork()
        
        
        kStream.WriteInt(pNetwork.GetLocalID())
        kLocation = pTorp.GetWorldLocation()
        kStream.WriteFloat(kLocation.GetX())
        kStream.WriteFloat(kLocation.GetY())
        kStream.WriteFloat(kLocation.GetZ())

        # Okay, now set the data from the buffer stream to the message
        pMessage.SetDataFromStream(kStream)

        # Send the message to everybody but me.  Use the NoMe group, which
        # is set up by the multiplayer game.
        if not App.IsNull(pNetwork):
                if App.g_kUtopiaModule.IsHost():
                        pNetwork.SendTGMessageToGroup("NoMe", pMessage)
                else:
                        pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)

        # We're done.  Close the buffer.
        kStream.CloseBuffer()
        

def WeaponHit(pObject, pEvent):
        pShip = App.ShipClass_Cast(pEvent.GetDestination())
                
        if pShip:
                if dictFirePointToTorp.has_key(pShip.GetName()):
                        pTorp = dictFirePointToTorp[pShip.GetName()]
                        
                        # check if the torpedo still exists:
                        if App.Torpedo_GetObjectByID(None, pTorp.GetObjID()):
                                # get the World location of out Firepoint
                                kLocation = pTorp.GetWorldLocation()
                                
                                # For the Explosion Size
                                if pShip.GetPowerSubsystem():
                                        pShip.GetPowerSubsystem().GetProperty().SetPowerOutput(pTorp.GetDamage() / 10)

                                # Detach it from the Torpedo
                                if not App.g_kUtopiaModule.IsMultiplayer():
                                        pTorp.DetachObject(pShip)
                                
                                # and let the torpedo fly on our Firepoint to get destroyed
                                pTorp.SetTarget(pShip.GetObjID())
                                                                
                                # tell other clients to also move the firepoint to the ship
                                if App.g_kUtopiaModule.IsMultiplayer():
                                        MPSendRemoveTorpMessage(pTorp)
                                
                                # Let the Torp destroy the Firepoint
                                pShip.SetTranslate(kLocation)
                                pShip.UpdateNodeOnly()
                                
                                del dictFirePointToTorp[pShip.GetName()]
        
        pObject.CallNextHandler(pEvent)


# Get the Distance between two Objects
def Distance(pObject1, pObject2):
	vDifference = pObject1.GetWorldLocation()
	vDifference.Subtract(pObject2.GetWorldLocation())

	return vDifference.Length()


def GetShipType(pShip):
        return string.split(pShip.GetScript(), '.')[-1]


def ShipHasStringInName(shipfile, stringfind):
        if string.find(string.lower(shipfile), string.lower(stringfind)) == -1:
                return 0
        return 1


def ShipIsAllowedForPD(pShip):
        shipfile = GetShipType(pShip)
        if ShipHasStringInName(shipfile, "ReplicatorVessel"):
                return 1
                
        return 0


def PDStartStop(pObject, pEvent):
        global PDRunning
        
        if PDRunning == 1:
                return
        PDRunning = 1
        
        pPlayer = MissionLib.GetPlayer()
        if not pPlayer:
                return
        
        # Fed only Technology
        if ShipIsAllowedForPD(pPlayer):
                PDGetTargets(pPlayer)
                PDNextTarget(pObject, pEvent)


def PDGetTargets(pPlayer):
        global TorpList

        pSet = pPlayer.GetContainingSet()
        
        if not pSet:
                return

        lObjects = pSet.GetClassObjectList(App.CT_TORPEDO)
        
        for pObject in lObjects:
                # GetGuidanceLifeTime() > 0.0 will make sure we only Target Torpedos and no Pulse Weapons
                if Distance(pPlayer, pObject) < 600 and pObject.GetGuidanceLifeTime() > -0.01:
                        TorpList.append(pObject)
        

def PDNextTarget(pObject, pEvent):
        global dictFirePointToTorp, i_FPcount, PDRunning
        
        pPlayer = MissionLib.GetPlayer()
        
        if not pPlayer:
                return
        
        pSensorSubsystem = pPlayer.GetSensorSubsystem()
        pSet = pPlayer.GetContainingSet()
        pWeaponSystem = pPlayer.GetPhaserSystem()
        
        if not pSet or not pWeaponSystem:
                return
                
        pWeaponSystem.StopFiring()
        sThisFirePointName = FirePointName + " " + pPlayer.GetName() + " " + str(i_FPcount)
        if i_FPcount < 9:
                i_FPcount = i_FPcount + 1
        else:
                i_FPcount = 0
        
        if TorpList:
                pTorp = TorpList[0]
                del TorpList[0]
                
                # check if the torpedo still exists:
                if App.Torpedo_GetObjectByID(None, pTorp.GetObjID()):
                
                        pFirePoint = MissionLib.GetShip(sThisFirePointName)
                        # if it does not exist we have to create it first
                        if not pFirePoint:
                                pFirePoint = loadspacehelper.CreateShip("BigFirepoint", pSet, sThisFirePointName, None)
                                pFirePoint.SetTargetable(0)
                                        
                        pFirePoint = MissionLib.GetShip(sThisFirePointName)
                        if pFirePoint:
                                pTarget = App.ShipClass_GetObjectByID(None, pTorp.GetTargetID())
                                if pTarget:
                                        pFirePoint.EnableCollisionsWith(pTarget, 0)
                
                                # This should make sure that the clients in MP get the right position
                                if App.g_kUtopiaModule.IsMultiplayer():
                                        kLocation = pTorp.GetWorldLocation()
                                        pFirePoint.SetTranslate(kLocation)
                                        pFirePoint.UpdateNodeOnly()
                                else:                                
                                        # little offset, so the Torpedo doesn't destroy our firepoint
                                        kLocation = App.TGPoint3()
                                        kLocation.SetXYZ(0, 0.5, 0)
                                        pFirePoint.SetTranslate(kLocation)
                                        pFirePoint.UpdateNodeOnly()
                                        pTorp.AttachObject(pFirePoint)


                                dictFirePointToTorp[sThisFirePointName] = pTorp
                
                                vSubsystemOffset = App.TGPoint3()
                                vSubsystemOffset.SetXYZ(0, 0, 0)

                                pWeaponSystem.StartFiring(pFirePoint, vSubsystemOffset)

                                pSeq = App.TGSequence_Create()
                                pSeq.AppendAction(App.TGScriptAction_Create(__name__, "DeleteFirePoint", sThisFirePointName), 2)
                                pSeq.Play()

		        MissionLib.CreateTimer(POINT_DEFENCE_TIMER, __name__ + ".PDNextTarget", App.g_kUtopiaModule.GetGameTime() + 0.9, 0, 0)
                else:
                        PDRunning = 0
        else:
                PointDefenceRunning = 0


def DeleteFirePoint(pAction, sThisFirePointName):
        global dictFirePointToTorp
        
        if not MissionLib.GetPlayer():
                return
        MissionLib.GetPlayer().GetContainingSet().RemoveObjectFromSet(sThisFirePointName)

        if dictFirePointToTorp.has_key(sThisFirePointName):
                del dictFirePointToTorp[sThisFirePointName]
                
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
                for i in range(len(sThisFirePointName)):
                        kStream.WriteChar(sThisFirePointName[i])
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


def CheckAndDoButtonCreation():
        pPlayer = MissionLib.GetPlayer()
        
        if not pPlayer:
                return
        
        # try to get the Button
        pMenu = Lib.LibEngineering.GetBridgeMenu("Tactical")
        pButton = Lib.LibEngineering.GetButton("P D", pMenu)
        
        if not pButton and ShipIsAllowedForPD(pPlayer):
                pButton = Lib.LibEngineering.CreateMenuButton("P D", "Tactical", __name__ + ".PDStartStop")
        elif pButton and not ShipIsAllowedForPD(pPlayer):
                pMenu.DeleteChild(pButton)


def Restart():
        global PDRunning
        PDRunning = 0
        CheckAndDoButtonCreation()


def NewPlayerShip():
        global PDRunning
        PDRunning = 0
        CheckAndDoButtonCreation()
        
        
def init():
        global PDRunning
        PDRunning = 0
        pMission = MissionLib.GetMission()
        
        Lib.LibEngineering.AddKeyBind("P De", __name__ + ".PDStartStop")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WEAPON_HIT, pMission, __name__+ ".WeaponHit")

        CheckAndDoButtonCreation()

from bcdebug import debug
import App
import MissionLib
import loadspacehelper
import Lib.LibEngineering
import Foundation
import string


MODINFO = { "Author": "\"Defiant\" erik@bckobayashimaru.de",
            "Version": "0.2",
            "License": "BSD",
            "Description": "Point Defence",
            "needBridge": 0
            }
            

lShipsPDWhiteList = ["AdOberth", "Aegean", "Aegian", "AlphaWing", "Ambassador", "Ambassadortp", "AMVoyager", "AncientCity", "AncientSatellite", "Andromeda", "ArmoredVoyager", "Atlantis", "EACargoPod", "B5LordShip", "B5PsiCorpMothership", "B5Station", "B5TechnomageTransport", "B5TechnomageTransportIllusion", "B5TriadTriumviron", "Battlecrab", "Battlestar", "BrakiriCruiser", "CA8472", "C2Valdore", "C2excelsiorII", "CardHybrid", "CN_FedStarbase", "CylonBasestar", "DanielJackson", "DCMPDefiant", "Defiant", "DeltaWing", "DJEnterpriseG", "DJEnterpriseGDrive", "DJEnterpriseGSaucer", "DJEnterpriseGThunderbird", "DRA_Shuttle", "DRA_Raider", "DRA_Fighter", "DRA_Cruiser", "DRA_Carrier", "DraziSkySerpent", "DraziSunHawk", "DraziSunHawkWithSerpent", "ds9", "DyExcalibur", "EAForceOne", "EAHyperion", "EANova", "EAOmega", "EAOmegaX", "EAShadow_Hybrid", "EAStarfury", "EAStealthStarfury", "EAKestrel", "EAWorkerPod", "EchoWing", "Enterprise", "EnterpriseF", "EnterpriseJ", "Excalibur Transwarp", "Excalibur Uprated", "Excalibur", "ExcelsiorP81", "exeter", "Eximius", "Firebird", "FTBNeghvar", "Galactica", "Galaxy", "GalaxySaucer", "GalaxyStardrive", "GalaxyX", "Galor", "GQuan", "HadesBasestar", "HadesBasestar2003", "HalcyonPromise", "Hutet", "JediStarfighter", "Keldon", "KlingonImperialStarbase", "KTinga", "Kvort", "LCIntrepid", "LC_Excalibur", "LC_Excaliburtp", "LCIntrepid_warp", "LCRaptor", "lintsktinga", "MillionVoices", "MinbariNial", "MinbariSharlin", "MPneghvar", "MvamPrometheus", "MvamPrometheusDorsal", "MvamPrometheusSaucer", "MvamPrometheusVentral", "MvamVoyager", "MvamVoyagerSep", "NebulaX", "norway", "Nova", "novaII", "PaxMagellanic", "Pegasus", "PlanetExpress", "Praetor", "PsExcelsiorRefitTNG1", "pulsemine", "RomulanOutpost", "Shadow_Scout", "SigmaWalkerScienceLab", "SonaB", "Steamrunner", "Tardis", "ThirdspaceFighter", "ThirdspaceCapitalShip", "Tholian", "Thunderbolt", "TOSColDefender", "TWSB5StationUpgrade", "USSOrville", "ValdoreG", "VasKholhr", "Victory", "VOR_Cruiser", "VOR_Destroyer", "VOR_DestroyerClosed", "VOR_Fighter", "VOR_FighterOpen", "VOR_Planetkiller", "VulcanXRT55D", "Warbird", "Vorcha", "Warlock", "WCneghvar", "WCNemEntEnoyacht", "WCSonaBattleship", "XOversMinbariAshenShuumtian", "XOverAncientCityFed", "XOverAncientSatelliteFed", "Sovereign", "Nebula", "Phoenix", "USSLennox", "proximarefit", "Amredanddangerous", "TiconderogaA"]

lShipsPulseDWhiteList = ["Andromeda", "B5CargoPod", "B5PsiCorpMothership", "B5Station", "Battlestar", "BrakiriCruiser", "CylonBasestar", "DeltaWing", "DRA_Shuttle", "EAForceOne", "EAHyperion", "EANova", "EAOmega", "EAOmegaX", "EAStarfury", "EAStealthStarfury", "EAKestrel", "EchoWing", "Galactica", "GQuan", "HadesBasestar", "HadesBasestar2003", "HalcyonPromise", "MillionVoices", "MinbariSharlin", "PaxMagellanic", "Pegasus", "ThirdspaceFighter", "ThirdspaceCapitalShip", "Thunderbolt", "TOSColDefender", "TWSB5StationUpgrade", "Warlock", "XOversMinbariAshenShuumtian"]


FirePointName = "PointDefence Firepoint"
i_FPcount = 0
dictFirePointToTorp = {}
POINT_DEFENCE_TIMER = Lib.LibEngineering.GetEngineeringNextEventType()
REMOVE_POINTER_FROM_SET = 190
REMOVE_TORP_MESSAGE_AT = 191
TorpList = []
PointDefenceRunning = 0

def MPSendRemoveTorpMessage(pTorp):
        # Now send a message to everybody else that the score was updated.
        # allocate the message.
        debug(__name__ + ", MPSendRemoveTorpMessage")
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
        debug(__name__ + ", WeaponHit")
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
	debug(__name__ + ", Distance")
	vDifference = pObject1.GetWorldLocation()
	vDifference.Subtract(pObject2.GetWorldLocation())

	return vDifference.Length()


def GetShipType(pShip):
        debug(__name__ + ", GetShipType")
        return string.split(pShip.GetScript(), '.')[-1]


def ShipHasStringInName(shipfile, stringfind):
        debug(__name__ + ", ShipHasStringInName")
        if string.find(string.lower(shipfile), string.lower(stringfind)) == -1:
                return 0
        return 1


def ShipIsAllowedForPointDefence(pShip):
        debug(__name__ + ", ShipIsAllowedForPointDefence")
        shipfile = GetShipType(pShip)

	for sShip in lShipsPDWhiteList:
		if ShipHasStringInName(shipfile, sShip):
			return 1

        return 0

def ShipIsAllowedForPreferredPulseDefence(pShip):
        debug(__name__ + ", ShipIsAllowedForPreferredPulseDefence")
        global lShipsPulseDWhiteList
        shipfile = GetShipType(pShip)

	for sShip in lShipsPulseDWhiteList:
		if ShipHasStringInName(shipfile, sShip):
			return 1

        return 0


def PointDefenceStartStop(pObject, pEvent):
        debug(__name__ + ", PointDefenceStartStop")
        global PointDefenceRunning
        
        if PointDefenceRunning == 1:
                PointDefenceRunning = 0
        else:   
                PointDefenceRunning = 1
        
        pButton = GetPDButton()
        if pButton:
                if PointDefenceRunning == 1:
                        pButton.SetName(App.TGString("Point Defence: On"))
                else:   
                        pButton.SetName(App.TGString("Point Defence: Off"))
        
        pPlayer = MissionLib.GetPlayer()
        if not pPlayer:
                return
        
        # Fed only Technology
        if ShipIsAllowedForPointDefence(pPlayer) and PointDefenceRunning == 1:
                PointDefenceGetTargets(pPlayer)
                PointDefenceNextTarget(pObject, pEvent)

        #return


def PointDefenceGetTargets(pPlayer):
        debug(__name__ + ", PointDefenceGetTargets")
        global TorpList

        pSet = pPlayer.GetContainingSet()
        pFriendlies = MissionLib.GetFriendlyGroup()
        
        if not pSet:
                return

        lObjects = pSet.GetClassObjectList(App.CT_TORPEDO)

        pWeaponSystem2 = pPlayer.GetPulseWeaponSystem()

        PulseDefense = 0
        if pWeaponSystem2 and ShipIsAllowedForPreferredPulseDefence(pPlayer):
                PulseDefense = 1
        
        for pObject in lObjects:
                # GetGuidanceLifeTime() > 0.0 will make sure we only Target Torpedos and no Pulse Weapons
                pFiringShip = App.ShipClass_GetObjectByID(None, pObject.GetParentID())
		if not pFiringShip:
			return
                if Distance(pPlayer, pObject) < 600 and not pFriendlies.IsNameInGroup(pFiringShip.GetName()):
                        if pObject.GetGuidanceLifeTime() > 0.0 or (pObject.GetGuidanceLifeTime() < 0.1 and PulseDefense == 1):
                                TorpList.append(pObject)
        

def PointDefenceNextTarget(pObject, pEvent):
        debug(__name__ + ", PointDefenceNextTarget")
        global dictFirePointToTorp, i_FPcount, PointDefenceRunning
        
        pPlayer = MissionLib.GetPlayer()
        
        if not pPlayer:
                return
        
        pSensorSubsystem = pPlayer.GetSensorSubsystem()
        pSet = pPlayer.GetContainingSet()
        pWeaponSystem = pPlayer.GetPhaserSystem()

        # Alex SL Gato changes, you can use disruptors and torpedoes too
     
        if not pSet:
                return
 
        pWeaponSystem2 = pPlayer.GetPulseWeaponSystem()
        PulseDefense = 0
        if pWeaponSystem2 and (ShipIsAllowedForPreferredPulseDefence(pPlayer)):
                pWeaponSystem = pPlayer.GetPulseWeaponSystem()   
                PulseDefense = 1

        if not pWeaponSystem:
                pWeaponSystem = pPlayer.GetTorpedoSystem()
                PulseDefense = 0

        if not pWeaponSystem:
                return
                                           
        pWeaponSystem.StopFiring()
        sThisFirePointName = FirePointName + " " + pPlayer.GetName() + " " + str(i_FPcount)
        if i_FPcount < 40: # Originally 9
                i_FPcount = i_FPcount + 1
        else:
                i_FPcount = 0
        
        pSingleWeapon = pWeaponSystem.IsSingleFire()

        if TorpList:

                pTorp = TorpList[0]
                del TorpList[0]
                
                # check if the torpedo still exists:
                if App.Torpedo_GetObjectByID(None, pTorp.GetObjID()):

                        pWeaponSystem.GetProperty().SetSingleFire(1)
                
                        pFirePoint = MissionLib.GetShip(sThisFirePointName)
                        # if it does not exist we have to create it first
                        if not pFirePoint:
                                pFirePoint = loadspacehelper.CreateShip("BigFirepoint", pSet, sThisFirePointName, None)
                                pFirePoint.SetTargetable(0)
                                        
                        pFirePoint = MissionLib.GetShip(sThisFirePointName)
                        if pFirePoint:
                                pTarget = App.ShipClass_GetObjectByID(None, pTorp.GetTargetID())
                                if pTarget:
                                        if PulseDefense == 1:
                                                pFirePoint.EnableCollisionsWith(pTarget, 1) # O normally
                                        else:
                                                pFirePoint.EnableCollisionsWith(pTarget, 0) # O normally
                
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

                                if (PulseDefense == 1):
                                        # get the World location of out Firepoint
                                        kLocation = pTorp.GetWorldLocation()
                                
                                        # For the Explosion Size
                                        if pFirePoint.GetPowerSubsystem():
                                                pFirePoint.GetPowerSubsystem().GetProperty().SetPowerOutput(pTorp.GetDamage() / 10)
                                
                                        # Detach it from the Torpedo
                                        if not App.g_kUtopiaModule.IsMultiplayer():
                                                pTorp.DetachObject(pFirePoint)
                                
                                        # and let the torpedo fly on our Firepoint to get destroyed
                                        pTorp.SetTarget(pFirePoint.GetObjID())
                                                                
                                        # tell other clients to also move the firepoint to the ship
                                        if App.g_kUtopiaModule.IsMultiplayer():
                                                MPSendRemoveTorpMessage(pTorp)
                                
                                        # Let the Torp destroy the Firepoint
                                        pFirePoint.SetTranslate(kLocation)
                                        pFirePoint.UpdateNodeOnly()

                                pTime = 1 # 2
                                pTime2 = 0.9
                                if (PulseDefense == 1):
                                        pTime = 0.5
                                        pTime2 = 0.5

                                pSeq = App.TGSequence_Create()
                                pSeq.AppendAction(App.TGScriptAction_Create(__name__, "DeleteFirePoint", sThisFirePointName), pTime + 1)
                                pSeq.Play()

                                if pSingleWeapon:
                                        pWeaponSystem.GetProperty().SetSingleFire(1)
                                else:
                                        pWeaponSystem.GetProperty().SetSingleFire(0)

		        MissionLib.CreateTimer(POINT_DEFENCE_TIMER, __name__ + ".PointDefenceNextTarget", App.g_kUtopiaModule.GetGameTime() + pTime2, 0, 0)
                else:
                        PointDefenceRunning = 0
        else:
                PointDefenceRunning = 0
        if PointDefenceRunning == 0:
                pButton = GetPDButton()
                if pButton:
                        pButton.SetName(App.TGString("Point Defence: Off"))


def DeleteFirePoint(pAction, sThisFirePointName):
        debug(__name__ + ", DeleteFirePoint")
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


def GetPDButton():
        debug(__name__ + ", GetPDButton")
        pMenu = Lib.LibEngineering.GetBridgeMenu("Tactical")
        pButton = Lib.LibEngineering.GetButton("Point Defence: Off", pMenu)
        if not pButton:
                pButton = Lib.LibEngineering.GetButton("Point Defence: On", pMenu)
        return pButton


def CheckAndDoButtonCreation():
        debug(__name__ + ", CheckAndDoButtonCreation")
        pPlayer = MissionLib.GetPlayer()
        
        if not pPlayer:
                return
        
        # try to get the Button

	pMenu = Lib.LibEngineering.GetBridgeMenu("Tactical")
	pButton = GetPDButton()
	if not pButton and ShipIsAllowedForPointDefence(pPlayer):
		pButton = Lib.LibEngineering.CreateMenuButton("Point Defence: Off", "Tactical", __name__ + ".PointDefenceStartStop")
	elif pButton and not ShipIsAllowedForPointDefence(pPlayer):
		pMenu.DeleteChild(pButton)


def Restart():
        debug(__name__ + ", Restart")
        global PointDefenceRunning
        PointDefenceRunning = 0
        pButton = GetPDButton()
        if pButton:
                pButton.SetName(App.TGString("Point Defence: Off"))
        CheckAndDoButtonCreation()


def NewPlayerShip():
        debug(__name__ + ", NewPlayerShip")
        global PointDefenceRunning
        PointDefenceRunning = 0
        pButton = GetPDButton()
        if pButton:
                pButton.SetName(App.TGString("Point Defence: Off"))
        CheckAndDoButtonCreation()
        

def init():
        debug(__name__ + ", init")
        global PointDefenceRunning
        PointDefenceRunning = 0
        pMission = MissionLib.GetMission()
        
        #Lib.LibEngineering.AddKeyBind("Point Defence", __name__ + ".PointDefenceStartStop")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WEAPON_HIT, pMission, __name__+ ".WeaponHit")
	import Custom.Autoload.PointDefence
	App.g_kEventManager.AddBroadcastPythonFuncHandler(Custom.Autoload.PointDefence.ET_KEY_EVENT, MissionLib.GetMission(), __name__ + ".PointDefenceStartStop")


        CheckAndDoButtonCreation()

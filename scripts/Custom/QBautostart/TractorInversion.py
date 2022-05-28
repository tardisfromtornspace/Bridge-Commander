import App
import MissionLib
import Libs.LibEngineering


MODINFO = { "Author": "\"Defiant\" erik@bckobayashimaru.de",
            "needBridge": 0
            }

dict_Tractors = {}
DISABLE_TRACTOR_MESSAGE = 193


def TractorInversion(sShipName):
        if dict_Tractors.has_key(sShipName) and chance(20):
                pTractorProjector = dict_Tractors[sShipName]
                dis = pTractorProjector.GetDisabledPercentage()
                if pTractorProjector.GetConditionPercentage() < dis:
                        dis = pTractorProjector.GetConditionPercentage()
                dis = dis - 0.2
                if dis < 0.0:
                        dis = 0.0
                cond = dis * pTractorProjector.GetMaxCondition()
                pTractorProjector.SetCondition(cond)


def SendDisableTractorMessage(sShipName):
        # Now send a message to everybody else that the score was updated.
        # allocate the message.
        pMessage = App.TGMessage_Create()
        pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet
                        
        # Setup the stream.
        kStream = App.TGBufferStream()		# Allocate a local buffer stream.
        kStream.OpenBuffer(256)				# Open the buffer stream with a 256 byte buffer.

        # Write relevant data to the stream.
        # First write message type.
        kStream.WriteChar(chr(DISABLE_TRACTOR_MESSAGE))

        pNetwork = App.g_kUtopiaModule.GetNetwork()
        
        # Write the name of ship
        for i in range(len(sShipName)):
                kStream.WriteChar(sShipName[i])
        # set the last char:
        kStream.WriteChar('\0')

        # Okay, now set the data from the buffer stream to the message
        pMessage.SetDataFromStream(kStream)

        # Send the message to everybody but me.  Use the NoMe group, which
        # is set up by the multiplayer game.
        if not App.IsNull(pNetwork):
                pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)

        # We're done.  Close the buffer.
        kStream.CloseBuffer()
        

def ProcessMessageHandler(pObject, pEvent):                
        pMessage = pEvent.GetMessage()
        if not pMessage:
                return
        
        # Get the data from the message
        # Open a buffer stream to read the data
        kStream = pMessage.GetBufferStream();
        cType = kStream.ReadChar();
        cType = ord(cType)
        
        if cType == DISABLE_TRACTOR_MESSAGE:
                sShipName = ""
                
                while(1):
                        iChar = kStream.ReadChar()
                        if iChar == '\0':
                                break
                        sShipName = sShipName + iChar
                        
                if sShipName:
                        TractorInversion(sShipName)

        kStream.Close()

        
def PlayerTractorInversion(pObject, pEvent):
        pPlayer = MissionLib.GetPlayer()

        # Play sound - doesn't matter if we have success or not
        pSound = App.g_kSoundManager.GetSound("TractorInversion")
        if not pSound:
                pSound = App.TGSound_Create("sfx/TractorInversion.wav", "TractorInversion", 0)
        if pSound:
                pSound.Play()

        if pPlayer and App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
                SendDisableTractorMessage(pPlayer.GetName())
        elif pPlayer:
                TractorInversion(pPlayer.GetName())
        
        DisableButton()


def EnableButton(pAction, pButton):
        pButton.SetEnabled()
        return 0


def DisableButton():
        pMenu = Libs.LibEngineering.GetBridgeMenu("Tactical")
        pTechnologiesMenu = Libs.LibEngineering.GetButton("Technologies", pMenu)
	if pTechnologiesMenu:
        	pButton = Libs.LibEngineering.GetButton("Tractor inversion", pTechnologiesMenu)
        	if pButton:
                	pButton.SetDisabled()
                	pSeq = App.TGSequence_Create()
                	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "EnableButton", pButton), 20.0)
                	pSeq.Play()
        
        
def chance(iRand):
        if App.g_kSystemWrapper.GetRandomNumber(100) < iRand:
                return 1
        return 0


def CreateButton(pObject, pEvent):
        pMenu = Libs.LibEngineering.GetBridgeMenu("Tactical")
        pTechnologiesMenu = Libs.LibEngineering.GetButton("Technologies", pMenu)
	if pTechnologiesMenu:
        	Libs.LibEngineering.CreateMenuButton("Tractor inversion", "Tactical", __name__ + ".PlayerTractorInversion", 0, pTechnologiesMenu)


def TractorStop(pObject, pEvent):
        global dict_Tractors
        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        
        if pShip and dict_Tractors.has_key(pShip.GetName()):
                del dict_Tractors[pShip.GetName()]

        pObject.CallNextHandler(pEvent)

        
def TractorStart(pObject, pEvent):
        global dict_Tractors
        # Get the ship that was hit
        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        # Get the tractor beam system that fired
        pTractorProjector = App.TractorBeamProjector_Cast(pEvent.GetSource())
        
        if pShip and pTractorProjector:
                dict_Tractors[pShip.GetName()] = pTractorProjector

        pObject.CallNextHandler(pEvent)


def init():
        global dict_Tractors
        dict_Tractors = {}

        # we can not create our button  now because the Technologies menu is created after this file executed
        MissionLib.CreateTimer(Libs.LibEngineering.GetEngineeringNextEventType(), __name__ + ".CreateButton", App.g_kUtopiaModule.GetGameTime() + 5.0, 0, 0)
        pMission = MissionLib.GetMission()
        if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TRACTOR_BEAM_STARTED_HITTING, pMission, __name__+ ".TractorStart")
                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TRACTOR_BEAM_STOPPED_HITTING, pMission, __name__+ ".TractorStop")
        if App.g_kUtopiaModule.IsMultiplayer() and App.g_kUtopiaModule.IsHost():
                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_NETWORK_MESSAGE_EVENT, pMission, __name__ + ".ProcessMessageHandler")


def Restart():
        global dict_Tractors
        dict_Tractors = {}

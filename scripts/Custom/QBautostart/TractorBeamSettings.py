#########################################################################################
#	TractorBeamSettings.py 
#	
#	Tractor Beam Settings v0.1.1 or TBS by USS Sovereign -- 02/09/2005
#	
#	DESCRIPTION:
#	A simple mod that changes Tractor Modes. There are four of them.
#	Everything depends on the MaxDamage of the tractor beam properties.
#	I tested it on two ships so far; one with 80 MaxDamage setting and one with
#	500 MaxDamage setting the results were noticable. I suggest setting Tractor 
#	Beams MaxDamage to about 300 to get noticable results. It's up to you.
#
#	THE SETTINGS ARE:
#	1. Normal Tractor Mode, or default one that's comes in the game
#	2. Tow Mode, this mode actually drags the ship, it doesn't matter
#  	how fast you go. Well from my tests I concluded this. Further testing is
#	required however. Also it depends on your tractor beams MaxDamage.
#	3. Push Mode or Repulse Mode. It pushes the enemy away from you. Also
#	everything depends on the MaxDamage of your tractor beams.
#	4. Pull Mode it pulls the enemy close to you, it's like Repulse Mode only
# 	in opposite direction. It's directed at you. Also it depends on tractor
#	beams MaxDamage.
#
#	CREDITS: To Me, USS Sovereign for this script and Defiant for QBautostart.
#	His QBautostart makes making scripts much easier. Well at least for me.	
#
#	PERMISSION ISSUES: Ask before modifying and give me Credits. It's just polite!
#	
#	That's all that should go in here.
#########################################################################################


# Globals and Imports you know the drill. Same old stuff that's in every script, nothing magical here.

import App
import MissionLib
import Lib.LibEngineering
pDefaultBeamButton = None
pRepulseBeamButton = None
pTowBeamButton = None
pPullBeamButton = None
pTractorMain = None
MP_SET_TRACTOR_MODE = 195
g_dTractorModes = {}

# Thanks to Defiant, I overlooked this.  

MODINFO = {     "Author": "\"USS Sovereign\" uss882000@yahoo.co.uk",
                "License": "GPL",
                "needBridge": 0
            }

NonSerializedObjects = (
"g_dTractorModes",
)

# Push the enemy away. Bye, bye see you later. Music to my ears.
# Well it all depends on MaxDamage settings of your tractor beams. 

def SetTractorSystem(pObject, pEvent):
	global g_dTractorModes
	# Well get the properties we need ;)
	# Easy isn't it?!
		
	pPlayer = MissionLib.GetPlayer()
   	TractorSystem = pPlayer.GetTractorBeamSystem()
   	TractorMode = TractorSystem.GetMode() #unused but hey I might need it some day
        iTractorNewMode = pEvent.GetInt()
   			
   	# If not then no Repulse. Sorry no go then. 
   	# You can always get out and push.
    	if not TractorSystem:
		return

	# If Tractor Beam, then away goes the enemy or friendly it depends on what you're targeting. 
  	# If you're targeting friendly then you're pretty sneaky. But's it might be fun!
	if TractorSystem:
		TractorSystem.SetMode(iTractorNewMode)
		g_dTractorModes[pPlayer.GetObjID()] = iTractorNewMode
		if App.g_kUtopiaModule.IsMultiplayer():
			MPSendTractorBeamSettings(pPlayer, iTractorNewMode)


def TractorBeamOn(pObject, pEvent):
	pTractorProjector	= App.TractorBeamProjector_Cast(pEvent.GetSource())
	pTractorSystem		= App.TractorBeamSystem_Cast(pTractorProjector.GetParentSubsystem())
	# Get the ship that fired
	pShip = pTractorSystem.GetParentShip()
	
	if pShip and g_dTractorModes.has_key(pShip.GetObjID()):
		iTractorMode = g_dTractorModes[pShip.GetObjID()]
		pTractorSystem.SetMode(iTractorMode)
		if App.g_kUtopiaModule.IsMultiplayer():
			MPSendTractorBeamSettings(pShip, iTractorMode)
	
	pObject.CallNextHandler(pEvent)


def init():
    	global pDefaultBeamButton, pRepulseBeamButton, pTowBeamButton, pPullBeamButton, pTractorMain
        
    	# Guess what?! I'm still bored. But the script will be completed soon. Yay!!!
    	pPlayer = MissionLib.GetPlayer()
        if not pPlayer:
                return
        pPlayer = MissionLib.GetPlayer()
   	TractorSystem = pPlayer.GetTractorBeamSystem()
   	
   	# I need to clean up the script don't you think?! 
   	# OK. I'll set up the buttons and clean up later. I don't want to go to school today!!!!!
   	
   	if TractorSystem:
   		pBridge = App.g_kSetManager.GetSet('bridge')
                pMenu = Lib.LibEngineering.GetBridgeMenu("Science")
                pTractorMain = App.STMenu_CreateW(App.TGString("Tractor Modes"))
                pMenu.PrependChild(pTractorMain)
                
        	# Buttons, buttons where are you? Oh! There you are! Pretty Buttons, I must be going mad. Or I was mad before this?!
        	# Time will tell!!!
        	
        	pDefaultBeamButton = Lib.LibEngineering.CreateMenuButton("Default Mode", "Tactical", __name__ + ".SetTractorSystem", TractorSystem.TBS_TOW, pTractorMain)
        	pPullBeamButton = Lib.LibEngineering.CreateMenuButton("Pull Mode", "Tactical", __name__ + ".SetTractorSystem", TractorSystem.TBS_PULL, pTractorMain)
        	pRepulseBeamButton = Lib.LibEngineering.CreateMenuButton("Repulse Mode", "Tactical", __name__ + ".SetTractorSystem", TractorSystem.TBS_PUSH, pTractorMain)
 		pTowBeamButton = Lib.LibEngineering.CreateMenuButton("Tow Mode", "Tactical", __name__ + ".SetTractorSystem", TractorSystem.TBS_HOLD, pTractorMain)
                pTowBeamButton = Lib.LibEngineering.CreateMenuButton("Dock Mode", "Tactical", __name__ + ".SetTractorSystem", TractorSystem.TBS_DOCK_STAGE_1, pTractorMain)
		
		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TRACTOR_BEAM_STARTED_HITTING, MissionLib.GetMission(), __name__+ ".TractorBeamOn")
                
# THE END. That's all so simple script. Isn't it? Enjoy People!!!!!
# Well I find this useful when fighting enemies :)
# I mean seeing them go up and away. Isn't it fun?!
# A Note: I really hate this job (A joke). Thank you and this brings the conclusion to our broadcast!!!!!!!!!!!!!!!!!!!!


# MP support, receive is done in Mission4 (TKY)
def MPSendTractorBeamSettings(pShip, iMode):
	pNetwork = App.g_kUtopiaModule.GetNetwork()
        # Now send a message to everybody else that the score was updated.
        # allocate the message.
        pMessage = App.TGMessage_Create()
        pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet
                        
        # Setup the stream.
        kStream = App.TGBufferStream()		# Allocate a local buffer stream.
        kStream.OpenBuffer(256)				# Open the buffer stream with a 256 byte buffer.

        # Write relevant data to the stream.
        # First write message type.
        kStream.WriteChar(chr(MP_SET_TRACTOR_MODE))

        # Write our Message
        kStream.WriteInt(pShip.GetObjID())
        kStream.WriteInt(iMode)

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

from bcdebug import debug
#################################################################################################
#   A file which kills pWindow in WarpFX_GUI when exiting, it sets buttons at Mission Start     #
#   and it determines warp degradation over here.                                               #
#                                                                                               #
#   by USS Sovereign                                                                            #
#                                                                                               #
#   License: It's a part of CWS Mod. You know the drill, code borrowing needs to be credited... #
#                                                                                               #
#   Note: If you've uninstalled CWS it's safe to delete this file. It won't give you any        #
#   trouble if you haven't but it's recommended. However if you've uninstalled NanoFX you'll    #
#   notice that this file is giving you BSOD. It's cause it's importing a file which most       #
#   likely was deleted in the uninstall process.                                                #
#################################################################################################


##### Imports
import App
import Foundation
import MissionLib
from Custom.Autoload.LoadNanoFX import *
SUBSYSTEM_SET_CONDITION = 194

##### Trigger
class SovFixTrigger(Foundation.TriggerDef):
	def __init__(self, name, eventKey, dict = {}):
		debug(__name__ + ", __init__")
		Foundation.TriggerDef.__init__(self, name, eventKey, dict)

	def __call__(self, pObject, pEvent, dict = {}):
                debug(__name__ + ", __call__")
                pGame = App.Game_GetCurrentGame()
                pEpisode = pGame.GetCurrentEpisode()
		if not pEpisode:
			return
                pMission = pEpisode.GetCurrentMission()

                ##### If the user is in QBR Mode using this has lethal consequences
                if pMission.GetScript() == "Custom.QuickBattleGame.QuickBattle":
                    return
                
                try:
                    
                    import Custom.NanoFXv2.WarpFX.WarpFX_GUI
                    Custom.NanoFXv2.WarpFX.WarpFX_GUI.exiting(None, None)
                    
                except:
                    
                    print "CWS 2.0: Why am I still here on your computer?! Delete me... my name is: SovNFX2Fix.py & pyc"
                    return

#disabled by Defiant: seems to crash the game on exit
#SovFixTrigger('SovFixTrigger', App.ET_QUIT, dict = { 'modes': [ mode ] } )


##### Trigger
class SovButtonTrigger(Foundation.TriggerDef):
	def __init__(self, name, eventKey, dict = {}):
		debug(__name__ + ", __init__")
		Foundation.TriggerDef.__init__(self, name, eventKey, dict)

	def __call__(self, pObject, pEvent, dict = {}):
                debug(__name__ + ", __call__")
		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
                try:
                    import Custom.NanoFXv2.WarpFX.WarpFX_GUI
                    Custom.NanoFXv2.WarpFX.WarpFX_GUI.SetupButtons()
                except:
                    print "CWS 2.0: Why am I still here on your computer?! Delete me... my name is: SovNFX2Fix.py & pyc"
                    return

SovButtonTrigger('SovButtonTrigger', App.ET_MISSION_START, dict = { 'modes': [ mode ] } )


##### Trigger
class SovWarpDegradingTrigger(Foundation.TriggerDef):
	def __init__(self, name, eventKey, dict = {}):
		debug(__name__ + ", __init__")
		Foundation.TriggerDef.__init__(self, name, eventKey, dict)

	def __call__(self, pObject, pEvent, dict = {}):
                debug(__name__ + ", __call__")
                WarpDegrading()
                

SovWarpDegradingTrigger('SovWarpDegradingTrigger', App.ET_ENTERED_SET, dict = { 'modes': [ mode ] } )


##### Warp degradation of the players warp engines. 
def WarpDegrading():
        debug(__name__ + ", WarpDegrading")
        WarpCheck = DoWarpingCheck()

        if WarpCheck == 'Skip':
            return
    
        CurrentWarp = GetCurrentWarpSpeed()
        
        if CurrentWarp == 'Skip':
            return

        CruisingWarpSpeed = GetCruisingWarpSpeed()

        if CruisingWarpSpeed == 'Skip':
            return

        if CurrentWarp <= CruisingWarpSpeed:
            return

        TimeSpentInWarp = GetTimeSpentInWarp()

        if TimeSpentInWarp == 'Skip':
            return

        Degradation = (CurrentWarp - CruisingWarpSpeed) * TimeSpentInWarp

        Degradation = Degradation / 100
        
        SetDegradation(Degradation)


##### Warp Degradation Check
def SetDegradation(Percentage):
        debug(__name__ + ", SetDegradation")
        pPlayer = MissionLib.GetPlayer()
        pWarp = pPlayer.GetWarpEngineSubsystem()

        if pWarp:
            DegradingInProgress(pPlayer, pWarp, Percentage)


##### Warp engines degrading
def DegradingInProgress(pShip, pSubsystem, fPercentage, bIsChild = 0):
        debug(__name__ + ", DegradingInProgress")
        if (bIsChild != 0) or (pSubsystem.GetNumChildSubsystems() == 0):
                fStats = pSubsystem.GetConditionPercentage()
                PreCalculation = fStats - fPercentage
                if (PreCalculation <= 0.01):
                    SetSubsystemCondition(pShip.GetObjID(), pSubsystem, 1)
                else:
                    SetSubsystemCondition(pShip.GetObjID(), pSubsystem, (fStats - fPercentage) * pSubsystem.GetMaxCondition())

	for i in range(pSubsystem.GetNumChildSubsystems()):
		pChild = pSubsystem.GetChildSubsystem(i)

		if (pChild != None):
			DegradingInProgress(pShip, pChild, fPercentage, 1)


##### See if the player ship is actually warping
def DoWarpingCheck():
        debug(__name__ + ", DoWarpingCheck")
        pPlayer = MissionLib.GetPlayer()
        if not pPlayer:
            return 'Skip'
        pWarp = pPlayer.GetWarpEngineSubsystem()
        if not pWarp or pWarp.GetWarpState() != pWarp.WES_WARPING:
            return 'Skip'


##### Grab current warp speed of the ship
def GetCurrentWarpSpeed():
        debug(__name__ + ", GetCurrentWarpSpeed")
        try:
            
            import Custom.NanoFXv2.WarpFX.WarpFX_GUI

            fWarpSpeed = Custom.NanoFXv2.WarpFX.WarpFX_GUI.GetWarpSpeed()

            return fWarpSpeed

        except:
            
            return 'Skip'
        
##### Grab safe cruising speed of the ship
def GetCruisingWarpSpeed():
        debug(__name__ + ", GetCruisingWarpSpeed")
        try:
            import Custom.NanoFXv2.WarpFX.WarpFX_GUI

            fCruiseSpeed = Custom.NanoFXv2.WarpFX.WarpFX_GUI.ReturnCruiseSpeed()

            return fCruiseSpeed

        except:
            
            return 'Skip'


##### Grab time spent in Warp
def GetTimeSpentInWarp():
        debug(__name__ + ", GetTimeSpentInWarp")
        try:
            import Custom.NanoFXv2.WarpFX.WarpFX

            fTime = Custom.NanoFXv2.WarpFX.WarpFX.ReturnWarpTime()

            return fTime

        except:

            return 'Skip'


##### Trigger
class SovWarpResetTrigger(Foundation.TriggerDef):
	def __init__(self, name, eventKey, dict = {}):
		debug(__name__ + ", __init__")
		Foundation.TriggerDef.__init__(self, name, eventKey, dict)

	def __call__(self, pObject, pEvent, dict = {}):
                debug(__name__ + ", __call__")
                try:
                    
                    import Custom.NanoFXv2.WarpFX.WarpFX_GUI
                    Custom.NanoFXv2.WarpFX.WarpFX_GUI.ResetWarpSpeed()
                    
                except:
                    
                    return

SovWarpResetTrigger('SovWarpResetTrigger', App.ET_SET_PLAYER, dict = { 'modes': [ mode ] } )


def SetSubsystemCondition(iShipObjID, pSubsystem, iNewCondition):
	debug(__name__ + ", SetSubsystemCondition")
	if pSubsystem.IsCritical() and iNewCondition < 1:
		iNewCondition = 1
	
	pSubsystem.SetCondition(iNewCondition)
	if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
		return
        # Setup the stream.
        # Allocate a local buffer stream.
        kStream = App.TGBufferStream()
        # Open the buffer stream with a 256 byte buffer.
        kStream.OpenBuffer(256)
        # Write relevant data to the stream.
        # First write message type.
        kStream.WriteChar(chr(SUBSYSTEM_SET_CONDITION))
        
        # send Message
        kStream.WriteInt(iShipObjID)
	sSubsystenName = pSubsystem.GetName()
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
                pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
        # We're done.  Close the buffer.
        kStream.CloseBuffer()

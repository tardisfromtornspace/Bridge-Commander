from bcdebug import debug
# Based on Banbury's QuickBattle Replacement Transporter

import App
import MissionLib
import Lib.LibEngineering
from Libs.LibQBautostart import *

MODINFO = {     "Author": "\"Defiant\" mail@defiant.homedns.org",
                "Download": "http://defiant.homedns.org/~erik/STBC/Engineering/",
                "Version": "0.5.2",
                "License": "GPL",
                "Description": "Included in Engneering Extension. Well - allows you to transport.",
                "needBridge": 0
            }


def Transport(pObject, pEvent):
	# Imports
	debug(__name__ + ", Transport")
	import AI.Player.Stay
	
	# Vars
	pGame			= App.Game_GetCurrentGame()
	pEpisode		= pGame.GetCurrentEpisode()
	pMission		= pEpisode.GetCurrentMission()
	pFriendlies		= pMission.GetFriendlyGroup()
	pPlayer			= MissionLib.GetPlayer()
	pTarget			= pPlayer.GetTarget()
	pSet 			= pPlayer.GetContainingSet()
	fTime			= 10 #Shields flicker Time
	pTargetattr		= App.ShipClass_Cast(pTarget)
	iTargetIsNotFriendly	= None #an Indicator
	pBridge			= App.g_kSetManager.GetSet('bridge') 
	
	# Test if we have a Target
	if not pTarget or pTarget.GetRadius() < 0.03:
		print("No Target - no Transport")
		return
	
	# Test Distance
	if (Distance(pTarget) > 300):
		print("Target is too far away: can't Transport")
		return
        
        if App.g_kUtopiaModule.IsMultiplayer() and pTargetattr.GetNetPlayerID() >= 0:
                print("This is a Player, don't Transport")
                return
        
	# Test if our Target is friendly
	if (pFriendlies.IsNameInGroup(pTarget.GetName()) != 1):
		print("Target is not friendly...testing Shields")
		# but maybe neutral:
                if pMission.GetEnemyGroup().IsNameInGroup(pTarget.GetName()):
                    print("Neither neutral :(")
                    return
                
		iTargetIsNotFriendly	= 1
		
		# try to find an offline Shield
		if (pTargetattr.GetShields() != None):
			if (pTargetattr.GetShields().GetCurShields(App.ShieldClass.FRONT_SHIELDS) < 200):
				print ("Front Shield is Offline...beaming")
			elif (pTargetattr.GetShields().GetCurShields(App.ShieldClass.REAR_SHIELDS) < 200):
				print ("After Shield is Offline...beaming")
			elif (pTargetattr.GetShields().GetCurShields(App.ShieldClass.TOP_SHIELDS) < 200):
				print ("Top Shield is Offline...beaming")
			elif (pTargetattr.GetShields().GetCurShields(App.ShieldClass.BOTTOM_SHIELDS) < 200):
				print ("Bottom Shield is Offline...beaming")
			elif (pTargetattr.GetShields().GetCurShields(App.ShieldClass.LEFT_SHIELDS) < 200):
				print ("Left Shield is Offline...beaming")
			elif (pTargetattr.GetShields().GetCurShields(App.ShieldClass.RIGHT_SHIELDS) < 200):
				print ("Right Shield is Offline...beaming")
			else:
				print ("No offline Shield...sorry")
				return

        # Sequence
	g_pDatabase	= App.g_kLocalizationManager.Load("data/TGL/Bridge Crew General.tgl")
	pSetPlayerAction	= App.TGScriptAction_Create(__name__, "SetPlayerAction", MissionLib.GetShip(pTarget.GetName()), pPlayer.GetNetPlayerID(), pTargetattr.GetNetPlayerID())
	pFlickerShields	= App.TGScriptAction_Create("Actions.ShipScriptActions", "FlickerShields", 0, fTime)
        g_pBrex = App.CharacterClass_GetObject(pBridge, 'Engineer')
	pBrexLine		= App.CharacterAction_Create(g_pBrex, App.CharacterAction.AT_SAY_LINE, "LoweringShields", None, 0, g_pDatabase)

	# Go
	if (pTarget != None):
		MissionLib.RemoveCommandableShip(pTarget.GetName())
		MissionLib.AddCommandableShip(pPlayer.GetName())

		# Create Video Sequence
		pSequence = App.TGSequence_Create()
		
		# Flicker Player Shields when they are active
		if ( pPlayer.GetShields().IsOn() == 1 ):
			pSequence.AppendAction(pBrexLine) # Brex
			pSequence.AppendAction(pFlickerShields) # old Ship
		
		if (pFriendlies.IsNameInGroup(pTarget.GetName()) != 1):
			# Changing Target group to Friendly id it wasn't before
			pFriendlies.AddName(pTarget.GetName())
		
		# Some Video stuff
                if App.g_kSetManager.GetSet("bridge"):
		        pSequence.AppendAction(App.TGScriptAction_Create("Actions.MissionScriptActions", "ChangeToBridge"), 1)
		pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "StartCutscene"))
		pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "SetTarget", pTarget.GetName()))
		pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pSet.GetName()), 2)
		pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", pSet.GetName()))
		
		# Beam
		pSequence.AppendAction(pSetPlayerAction)
				
		# Flicker Shields on new Ships if we have to
		if ( pTargetattr.GetShields().IsOn() == 1 and iTargetIsNotFriendly != 1):
			pSequence.AppendAction(pFlickerShields)
		
		# More Video stuff
		pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "LockedView", pSet.GetName(), pTarget.GetName(), 30, 30, 15))
		pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pSet.GetName()), 6)
                if App.g_kSetManager.GetSet("bridge"):
		        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "bridge"))
		pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "SetTarget", pPlayer.GetName()))
		pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "EndCutscene"))

		# Play
		pSequence.Play()

		# AI for the old Players Ship
		pTargetattr	= App.ShipClass_Cast(pTarget)
		pTargetattr.SetAI(AI.Player.Stay.CreateAI(pTargetattr))

                # Force switch to Tactical if we have no Bridge
                if not App.g_kSetManager.GetSet("bridge"):
                        MissionLib.CreateTimer(Lib.LibEngineering.GetEngineeringNextEventType(), __name__ + ".ForceTacticalVisible", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)

	if pObject:
		pObject.CallNextHandler(pEvent)


# Beaming yeah!
def SetPlayerAction(pAction, pShip, PlayerNetID, TargetNetID):
        debug(__name__ + ", SetPlayerAction")
        import AI.Player.Stay
	
        pGame = App.Game_GetCurrentGame()
        
        pPlayerOld = pGame.GetPlayer()
	
	# Play the sound
	pSound = App.TGSound_Create("sfx/Interface/new_game3.wav", "Tr_Sound", 0)
	pSound.SetSFX(0)
	pSound.SetInterface(1)
	App.g_kSoundManager.PlaySound("Tr_Sound")
	
	# Make sure the old Player's Ship doesn't make stuipd things...
        pPlayerOld.SetAI(AI.Player.Stay.CreateAI(pPlayerOld))
        
	try:
		from Custom.MultiplayerExtra.MultiplayerLib import SetNewNetPlayerID, MPSetAutoAI, CreatePlayerShipFromShip, CreateShipFromShip, SetStopAI
		if App.g_kUtopiaModule.IsMultiplayer():
			SetNewNetPlayerID(pPlayerOld, TargetNetID)
		CreatePlayerShipFromShip(pShip)
		pPlayerOld = CreateShipFromShip(pPlayerOld)
		SetStopAI(pPlayerOld)
		#MPSetAutoAI(pPlayer)
	except ImportError:
		if not App.g_kUtopiaModule.IsMultiplayer():
			pGame.SetPlayer(pShip)
	pTacWeaponsCtrl = App.TacWeaponsCtrl_GetTacWeaponsCtrl()
	if pTacWeaponsCtrl:
		pTacWeaponsCtrl.Init()
		try:
			import Custom.Autoload.ReSet
			if Custom.Autoload.ReSet.mode.IsEnabled():
				Custom.Autoload.ReSet.oPlayerChecking.__call__(None, None, 1)
		except:
			pass
	
        # Perhaps Banbury tried here to reset the Players AI
        pPlayer = MissionLib.GetPlayer()
	if pPlayer:
		pPlayer.ClearAI()
        
	return 0


# Get the Distance between the Player and pObject
def Distance(pObject):
	debug(__name__ + ", Distance")
	pPlayer = App.Game_GetCurrentGame().GetPlayer()
	vDifference = pObject.GetWorldLocation()
	vDifference.Subtract(pPlayer.GetWorldLocation())

	return vDifference.Length()


def CreateBridgeMenuButton(pName, eType, iSubType, pCharacter):
    debug(__name__ + ", CreateBridgeMenuButton")
    pEvent = App.TGIntEvent_Create()
    pEvent.SetEventType(eType)
    pEvent.SetDestination(pCharacter)
    pEvent.SetInt(iSubType)
        
    return (App.STButton_CreateW(pName, pEvent))


def ForceTacticalVisible(pObject, pEvent):
        debug(__name__ + ", ForceTacticalVisible")
        pTopWindow = App.TopWindow_GetTopWindow()
        pTopWindow.ToggleCinematicWindow()


# The Button
def init():
	debug(__name__ + ", init")
	#if not IsMultiplayerHostAlone():
	#	return
	Lib.LibEngineering.CreateMenuButton("Transporter", "Engineer", __name__ + ".Transport")
	#Lib.LibEngineering.AddKeyBind("Transporter", __name__ + ".Transport")
	import Custom.Autoload.Transporter
	App.g_kEventManager.AddBroadcastPythonFuncHandler(Custom.Autoload.Transporter.ET_KEY_EVENT, MissionLib.GetMission(), __name__ + ".Transport")


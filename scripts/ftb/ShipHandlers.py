from bcdebug import debug
# Ship.py
# March 16, 2002
#
# by sleight42 aka Evan Light, all rights reserved
#
# Permission to redistribute this code as part of any other packaging requires
# the explicit permission of the author in advance.
##############################################################################

import App
import Registry
import MissionLib
import ftb.Ship
import Bridge.BridgeUtils
import ftb.GUIUtils
import ftb.FTB_MissionLib

shipRegistry = Registry.Registry()

def GetShip( pShip):
    debug(__name__ + ", GetShip")
    retval = None
    if pShip != None:
        retval = shipRegistry.GetName(str(pShip.GetObjID()) + pShip.GetName())
        if( retval == None):
            retval = ftb.Ship.Ship(pShip)
            shipRegistry.Register(retval, str(pShip.GetObjID()) + pShip.GetName())
    return retval

#### BEGIN EVENT HANDLERS
def FirePrimaryWeaponsOnList( pObject, pEvent):
        debug(__name__ + ", FirePrimaryWeaponsOnList")
        pShip = App.Game_GetCurrentPlayer()
        pMyShip = GetShip( pShip)
        if (pMyShip  == None):
                return
        # only fire this weapon when not in Warp
        #if pShip.GetWarpEngineSubsystem() and (pShip.GetWarpEngineSubsystem().GetWarpState() == 0):
        pMyShip.FireWeaponsOnList( pEvent.GetBool(), App.ShipClass.WG_PRIMARY)
        pObject.CallNextHandler(pEvent)

def FireSecondaryWeaponsOnList( pObject, pEvent):
        debug(__name__ + ", FireSecondaryWeaponsOnList")
        pShip = App.Game_GetCurrentPlayer()
        pMyShip = GetShip( pShip)
        if not pMyShip:
                return
        pMyShip.FireWeaponsOnList( pEvent.GetBool(), App.ShipClass.WG_SECONDARY)
        pObject.CallNextHandler(pEvent)

def FireTertiaryWeaponsOnList( pObject, pEvent):
        debug(__name__ + ", FireTertiaryWeaponsOnList")
        pShip = App.Game_GetCurrentPlayer()
        pMyShip = GetShip( pShip)
        if not pMyShip:
                return
        # only fire this weapon when not in Warp
        #if pShip.GetWarpEngineSubsystem() and (pShip.GetWarpEngineSubsystem().GetWarpState() == 0):
        pMyShip.FireWeaponsOnList( pEvent.GetBool(), App.ShipClass.WG_TERTIARY)
        pObject.CallNextHandler(pEvent)

def ClearSecondaryTargets(pObject, pEvent):
    debug(__name__ + ", ClearSecondaryTargets")
    pPlayer = App.Game_GetCurrentPlayer()
    if pPlayer:
        pMyShip = GetShip( pPlayer)
        pMyShip.ClearSecondaryTargets()	

def ToggleSecondaryTarget(pObject, pEvent):
    debug(__name__ + ", ToggleSecondaryTarget")
    pPlayer = App.Game_GetCurrentPlayer()
    if pPlayer:
        pMyShip = GetShip( pPlayer)
        #pMyShip.ToggleSecondaryTarget( GetTargetByIdx( pEvent.GetInt())) 
        if pPlayer.GetTarget():
                pMyShip.ToggleSecondaryTarget(App.ShipClass_Cast(pPlayer.GetTarget()))
#### END EVENT HANDLERS

def GetPlayerSet():
    debug(__name__ + ", GetPlayerSet")
    pGame = App.Game_GetCurrentGame()
    return pGame.GetPlayerSet()

def GetTargetByIdx( idx):
    debug(__name__ + ", GetTargetByIdx")
    retval = None
    pEnemyGroup = MissionLib.GetEnemyGroup()
    lEnemies = pEnemyGroup.GetActiveObjectTupleInSet( GetPlayerSet())
    eCounter = 0
    for pEnemy in lEnemies:
        if( eCounter == idx ):
            retval = pEnemy
            break
        eCounter = eCounter + 1
    return retval

def MissionStart():
	#### REGISTER EVENT HANDLERS
	
	#App.ET_INPUT_CLEAR_SECONDARY_TARGETS = ftb.FTB_MissionLib.GetFTBNextEventType()
	#App.ET_INPUT_TOGGLE_SECONDARY_TARGET = ftb.FTB_MissionLib.GetFTBNextEventType()

	debug(__name__ + ", MissionStart")
	
	lEventHandlerMap = (
		(App.ET_INPUT_CLEAR_SECONDARY_TARGETS, __name__ + ".ClearSecondaryTargets"),
		(App.ET_INPUT_TOGGLE_SECONDARY_TARGET, __name__ + ".ToggleSecondaryTarget"),
		(App.ET_INPUT_FIRE_TERTIARY, __name__ + ".FireTertiaryWeaponsOnList"),
		(App.ET_INPUT_FIRE_SECONDARY, __name__ + ".FireSecondaryWeaponsOnList"),
		(App.ET_INPUT_FIRE_PRIMARY,	__name__ + ".FirePrimaryWeaponsOnList"),
	)

	
	for eType, sFunc in lEventHandlerMap:
		App.g_kEventManager.AddBroadcastPythonFuncHandler( eType, App.Game_GetCurrentGame(), sFunc)

	# Buttons
	pMenu = ftb.GUIUtils.GetTacticalMenu()

	pSTMenu = App.STMenu_CreateW(App.TGString("Secondary Targetting"))
	if pSTMenu:
		pMenu.AddChild(pSTMenu)

		pTakeTargetButton = ftb.GUIUtils.CreateIntButton("take secondary Target", App.ET_INPUT_TOGGLE_SECONDARY_TARGET, MissionLib.GetMission(), 0)
		pSTMenu.PrependChild(pTakeTargetButton)

		pclearTargetsButton = ftb.GUIUtils.CreateIntButton("clear sec Targets", App.ET_INPUT_CLEAR_SECONDARY_TARGETS, MissionLib.GetMission(), 0)
		pSTMenu.PrependChild(pclearTargetsButton)


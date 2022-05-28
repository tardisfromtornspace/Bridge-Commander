#
# Advanced Technology System plugin.
# This plugin demonstrates how to use the ATS within QuickBattle Replacement.
# To use it just copy this file to the plugins folder.
# This plugin is untested and is probably unstable. Don't use it with other versions
# of ATS.
#

import App
import MissionLib
import Custom.QuickBattleGame.plugin
import Lib.QuickBattleAddon

# Size and position of the big panel in the QBR GUI
DETAILPANEL_X=0.225
DETAILPANEL_Y=0.075
DETAILPANEL_W=0.65
DETAILPANEL_H=0.825

g_pMission = None

def Initialize(pMission):
	global g_pMission
	g_pMission = pMission
	
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WEAPON_HIT, pMission, __name__ + ".WeaponHit")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_CLOAK_BEGINNING, pMission, __name__+".CloakStarted")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_DECLOAK_BEGINNING, pMission, __name__+".DecloakStarted") 

def Restart():
	pass
	
def Terminate():
	App.g_kEventManager.RemoveBroadcastHandler(App.ET_WEAPON_HIT, g_pMission, __name__ + ".WeaponHit")
	App.g_kEventManager.RemoveBroadcastHandler(App.ET_CLOAK_BEGINNING, g_pMission, __name__+".CloakStarted")
	App.g_kEventManager.RemoveBroadcastHandler(App.ET_DECLOAK_BEGINNING, g_pMission, __name__+".DecloakStarted")
			
def Version():
	return "Advanced Tech Plugin 1.0 by Banbury"
		
def WeaponHit(pObject, pEvent):
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	pSet = pShip.GetContainingSet()
	
	Lib.QuickBattleAddon.QuickBattleAddonMain(pObject, pEvent, pSet)

	if (pObject):
		pObject.CallNextHandler(pEvent)

def CloakStarted(pObject, pEvent):
	Lib.QuickBattleAddon.QuickBattleAddonMain2(pObject, pEvent)

	if (pObject):
		pObject.CallNextHandler(pEvent)

def DecloakStarted(pObject, pEvent):
	Lib.QuickBattleAddon.QuickBattleAddonMain3(pObject, pEvent)
	
	if (pObject):
		pObject.CallNextHandler(pEvent)
 
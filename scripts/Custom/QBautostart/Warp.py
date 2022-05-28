from bcdebug import debug
# Custom Warp script

import App
import MissionLib
import Lib.LibEngineering
import AI.Player.InterceptTarget

sWarpButtonName = "In-System warp"
sNavPointNameAppend = "InSystemWarpNavPoint_"
fDist = App.UtopiaModule_ConvertKilometersToGameUnits(1000)

MODINFO = {     "Author": "\"Defiant\" erik@bckobayashimaru.de",
                "Version": "0.6",
                "Description": "Custom Warp",
                "needBridge": 0
            }


def UpdateNavPointAction(pAction, pShip, pNav, bForce=0):
	debug(__name__ + ", UpdateNavPointAction")

	if pShip.IsDoingInSystemWarp() or bForce:
		pNav.SetTranslateXYZ(pShip.GetWorldLocation().GetX() + pShip.GetWorldForwardTG().GetX() * fDist, pShip.GetWorldLocation().GetY() + pShip.GetWorldForwardTG().GetY() * fDist, pShip.GetWorldLocation().GetZ() + pShip.GetWorldForwardTG().GetZ() * fDist)

		pSeq = App.TGSequence_Create()
		pSeq.AppendAction(App.TGScriptAction_Create(__name__, "UpdateNavPointAction", pShip, pNav), 1.0)
		pSeq.Play()
	
	return 0


def GetInterceptNavPoint(pShip):
	debug(__name__ + ", GetInterceptNavPoint")
	if not pShip:
		return None
	
	pSet = pShip.GetContainingSet()
	
	if not pSet:
		return None
	
	pNav = App.Waypoint_Cast(App.ObjectClass_GetObject(pSet, sNavPointNameAppend + pShip.GetName()))
	if not pNav:
		pNav = App.Waypoint_Create(sNavPointNameAppend + pShip.GetName(), pSet.GetName(), None)
		pNav.SetNavPoint(1)
	UpdateNavPointAction(None, pShip, pNav, bForce=1)
	
	return pNav


def CustomWarp(pObject, pEvent):	
	debug(__name__ + ", CustomWarp")
	pPlayer = MissionLib.GetPlayer()
	
	if pPlayer and not pPlayer.IsDoingInSystemWarp():
		pHull = pPlayer.GetHull()
		pImpulse = pPlayer.GetImpulseEngineSubsystem()
		pWarp = pPlayer.GetWarpEngineSubsystem()
		
		if pHull and pHull.GetConditionPercentage > 0.25 and pWarp and not pWarp.IsDisabled() and pImpulse and not pImpulse.IsDisabled():
			pNav = GetInterceptNavPoint(pPlayer)
			
			MissionLib.SetPlayerAI("Helm", AI.Player.InterceptTarget.CreateAI(pPlayer, pNav))
			AppendOnSound(None, pPlayer, 20)
		else:
			MissionLib.SetPlayerAI("Helm", None)
	else:
		MissionLib.SetPlayerAI("Helm", None)
		App.g_kSoundManager.PlaySound("OFF_Sound") 


def AppendOnSound(pAction, pShip, i):
	debug(__name__ + ", AppendOnSound")
	if pShip.IsDoingInSystemWarp():
		App.g_kSoundManager.PlaySound("ON_Sound")
		return 0
	
	if i > 0:
		pSeq = App.TGSequence_Create()
		pSeq.AppendAction(App.TGScriptAction_Create(__name__, "AppendOnSound", pShip, i-1), 0.5)
		pSeq.Play()
	
	return 0


def init():
	debug(__name__ + ", init")
	pButton = Lib.LibEngineering.CreateMenuButton(sWarpButtonName, "Helm", __name__ + ".CustomWarp")

	pSound = App.TGSound_Create("sfx/enter warp.wav", "ON_Sound", 0) 
	pSound.SetSFX(0) 
	pSound.SetInterface(1)
	pSound = App.TGSound_Create("sfx/exit warp.wav", "OFF_Sound", 0) 
	pSound.SetSFX(0)
	pSound.SetInterface(1)

import App
import Lib.LibEngineering

MODINFO = { "Author": "ed",
				"Download": "",
				"Version": "2.0",
				"License": "",
				"Description": "Allows custom weapons scripting to be put directly into a torpedo's script file"
				}

def WeaponHit(pObject, pEvent):
	HandleWeaponHit(pObject, pEvent)
	pObject.CallNextHandler(pEvent)

def TorpedoFired(pObject, pEvent):
	HandleTorpedoFired(pObject, pEvent)
	pObject.CallNextHandler(pEvent)

def HandleTorpedoFired(pObject, pEvent):
	try:
		pTorp=App.Torpedo_Cast(pEvent.GetSource())
		if (pTorp==None):
			return
		pScriptName=pTorp.GetModuleName()
		if (pScriptName==None):
			return
		pTorpScript=__import__(pScriptName)
		if (pTorpScript==None):
			return
		pTorpScript.WeaponFired(pObject, pEvent)
	except:
		return
	return

def HandleWeaponHit(pObject, pEvent):
	try:
		pTorp=App.Torpedo_Cast(pEvent.GetSource())
		if (pTorp==None):
			return
		pScriptName=pTorp.GetModuleName()
		if (pScriptName==None):
			return
		pTorpScript=__import__(pScriptName)
		if (pTorpScript==None):
			return
		pTorpScript.TargetHit(pObject, pEvent)
	except:
		return
	return

def init():
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TORPEDO_FIRED, pMission, __name__ + ".TorpedoFired")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WEAPON_HIT, pMission, __name__ + ".WeaponHit")
	return
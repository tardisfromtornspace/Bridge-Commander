MODINFO = { "Author": "\"MLeoDaalder\" MLeoDaalder@netscape.net", 
            "Download": "", 
            "Version": "2.0", 
            "License": "You may include this script in your mods, and you may change it for yourself, but consult me first if you want to release it to the public.", 
            "Description": "This script allows you change textures to ships and damage them while keeping the same model (so keeping the download size low)." 
            } 

import App
import Foundation

mode = Foundation.MutatorDef("Skinning And Damaging Tool")

ShipsToApply = []

def AddShipToChange(NewDict):
	global ShipsToApply
	ShipsToApply.append(NewDict)
	return 0

class SDTriggerClass(Foundation.TriggerDef):
	def __init__(self, dict = {}):
		Foundation.TriggerDef.__init__(self, "SDT Trigger", App.ET_OBJECT_CREATED, dict)

	def __call__(self, pObject, pEvent, dict = {}):
		pShipCreated = App.ShipClass_Cast(pEvent.GetDestination())
		if pShipCreated:
			pShipScript = pShipCreated.GetScript()
			if(pShipScript):
				Plug = GetPlugin(pShipCreated)
				if(Plug != 0):
					if(Plug.__dict__.has_key("SDT Entry")):
						ChangeTextures(pShipCreated, Plug.__dict__["SDT Entry"](None))

					if(Plug.__dict__.has_key("SDTEntry")):
						ChangeTextures(pShipCreated, Plug.SDTEntry)

				global ShipsToApply
				for Entry in ShipsToApply:
					if(Entry):
						if(Entry.has_key("Script")):
							if(pShipScript == Entry["Script"]):
								ChangeTextures(pShipCreated, Entry)
		return 0

SDTriggerClass(dict = {"modes": [mode]})

def ChangeTextures(pShipCreated, Entry):
	if(Entry.has_key("Textures")):
		for Tex in Entry["Textures"]:
			pShipCreated.ReplaceTexture(Tex[1], Tex[0])
			pShipCreated.RefreshReplacedTextures()
	if(Entry.has_key("Damage")):
		for damage in Entry["Damage"]:
			pShipCreated.AddObjectDamageVolume(damage[0], damage[1], damage[2], damage[3], damage[4])
			pShipCreated.DamageRefresh(1)
	if(Entry.has_key("DamageFromOther")):
		for other in Entry["DamageFromOther"]:
			pShipCreated.AddDamage(other)
			pShipCreated.DamageRefresh(1)
	if(Entry.has_key("DamageFunction")):
		Entry["DamageFunction"](pShipCreated)
		pShipCreated.DamageRefresh(1)
		

# The next functions are from my Tools.py and alterd when needed
def GetPlugin(pShip):
	pScript = pShip.GetScript()
	pScript = GetStringFromNumOn(pScript, 6)
	if(Foundation.shipList._keyList.has_key(pScript)):
		return Foundation.shipList._keyList[pScript]
	else:
		return 0

def GetStringFromNumOn(string, i):
	retval = ""
	for j in range(len(string) - i):
		retval = retval + string[j + i]
	return retval



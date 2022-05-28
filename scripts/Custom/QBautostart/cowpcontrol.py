# This script should be very easy.
# All we have todo is power down all cowps in range once we are destroyed

import App
import MissionLib
from Libs.LibQBautostart import *

lCOWPRoidScript = ["CowpAsteroid"]
lCOWPScript = ["cOWP", "owp"]

MODINFO = {     "Author": "\"Defiant\" erik@bckobayashimaru.de",
                "needBridge": 0
            }


def ObjectDestroyed(pObject, pEvent):
	pObject.CallNextHandler(pEvent)
	
        pObject = App.ObjectClass_Cast(pEvent.GetDestination())
        pShip = App.ShipClass_Cast(pObject)
	if pShip:
		sShipType = GetShipType(pShip)
		if sShipType in lCOWPRoidScript:
			pSet = pShip.GetContainingSet()
			lObjects = pSet.GetClassObjectList(App.CT_SHIP)
			lRoids = []
			for pObject in lObjects:
				if GetShipType(pObject) in lCOWPRoidScript and not (pObject.IsDead() or pObject.IsDying()):
					# we still have a asteroid doing things here. no need to switch off cowps
					return
				elif GetShipType(pObject) in lCOWPScript:
					# add them to the list so we can turn them off later
					lRoids.append(pObject)
			# turn all roids off
			for pRoid in lRoids:
				pRoid.ClearAI()
				pRoid.SetAlertLevel(App.ShipClass.GREEN_ALERT)

def init():	
	if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, MissionLib.GetMission(), __name__ + ".ObjectDestroyed")

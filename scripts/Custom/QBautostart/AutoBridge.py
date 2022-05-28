import App
import MissionLib
import LoadBridge
import Foundation
import Libs.LibEngineering
from Libs.LibQBautostart import *


MODINFO = {     "Author": "\"Defiant\" erik@bckobayashimaru.de",
                "needBridge": 0
            }

sMutatorName = "Auto switch Bridge"


def checkbridge():
	pPlayer = MissionLib.GetPlayer()
	sShipType = GetShipType(pPlayer)
	pBridgeSet = App.BridgeSet_Cast(App.g_kSetManager.GetSet("bridge"))
	
	if pPlayer and sShipType and pBridgeSet and Foundation.shipList.has_key(sShipType):
		pFoundationShip = Foundation.shipList[sShipType]
		if pFoundationShip and hasattr(pFoundationShip, "sBridge") and pBridgeSet.GetConfig() != pFoundationShip.sBridge:
			print "auto switching Bridge to", pFoundationShip.sBridge
			LoadBridge.Load(pFoundationShip.sBridge)


def init():
#	checkbridge()
	return


#def Restart():
#	checkbridge()


def NewPlayerShip():
	if Libs.LibEngineering.CheckActiveMutator(sMutatorName):
		checkbridge()

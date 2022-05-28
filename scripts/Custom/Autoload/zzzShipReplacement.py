from bcdebug import debug
# Defiant <erik@kobmaru.de>

import App
import Foundation
import StaticDefs


def GetBridge(self):
	debug(__name__ + ", GetBridge")
	sBridgeInt = App.g_kConfigMapping.GetIntValue("Unified MainMenu Mod Configuration", "QB start bridge")
	if sBridgeInt == 0:
		# not set yet
		return 'SovereignBridge'
	else:
		return Foundation.bridgeList[sBridgeInt].bridgeString

Foundation.ShipDef.GetBridge = GetBridge

sShipint = App.g_kConfigMapping.GetIntValue("Unified MainMenu Mod Configuration", "QB start ship")
if sShipint == 0:
	# not set yet
	Foundation.MutatorDef.Stock.startShipDef = Foundation.ShipDef.Sovereign
else:
	pNewStartShip = Foundation.shipList[sShipint]
	Foundation.MutatorDef.Stock.startShipDef = pNewStartShip


from bcdebug import debug
import App
import Foundation
import MissionLib
import StaticDefs
import string

if hasattr(Foundation, "ImplicitBridgeDef"):

	def GetDefaultBridge():
		debug(__name__ + ", GetDefaultBridge")
		pMission = MissionLib.GetMission()
		sScript = pMission.GetScript()
		if sScript == "QuickBattle.QuickBattle":
			sNewScript = __import__("QuickBattle.QuickBattle").qbGameMode.GetBridge()
			if sNewScript != "Ship Specific Bridge":
				return sNewScript
		elif sScript[:9] == "Maelstrom":
			if sScript[17] in ["1", "2"]:
				return "GalaxyBridge"
			else:
				return "SovereignBridge"
		return "GalaxyBridge"

	class ShipBridge(Foundation.ImplicitBridgeDef):
		def __call__(self):
			debug(__name__ + ", __call__")
			pPlayer = App.Game_GetCurrentPlayer()
			if not pPlayer:
				return GetDefaultBridge()

			sScript = pPlayer.GetScript()
			sShipScript = string.split(sScript, ".")[-1]
			print "Finding bridge for shipscript:", sShipScript
			PosPlugin1 = PosPlugin2 = None
			for shipName in Foundation.shipList._keyList.keys():
				if Foundation.shipList[shipName].shipFile == sShipScript:
					PosPlugin1 = Foundation.shipList[shipName]
					if PosPlugin1.shipPrefix + PosPlugin1.shipFile == sScript:
						PosPlugin2 = PosPlugin1
						break
			Plugin = PosPlugin1
			if PosPlugin2:
				Plugin = PosPlugin2
			if Plugin and hasattr(Plugin, "sBridge"):
				print "Found plugin", Plugin.name
				#sWantedBridge = Plugin.__dict__.get("Default Bridge", None)
				sWantedBridge = Plugin.sBridge

				if Foundation.bridgeList._keyList.has_key(sWantedBridge):
					return sWantedBridge

			return GetDefaultBridge()


	oShipBridge = ShipBridge("Ship Specific Bridge")

#Foundation.ShipDef.Galaxy.__dict__["Default Bridge"] = "GalaxyBridge"
#Foundation.ShipDef.Sovereign.__dict__["Default Bridge"] = "SovereignBridge"
#
#Foundation.ShipDef.Galor.__dict__["Default Bridge"] = "Galorbridge"
#Foundation.ShipDef.Keldon.__dict__["Default Bridge"] = "Galorbridge"
#Foundation.ShipDef.CardHybrid.__dict__["Default Bridge"] = "Galorbridge"
#
#Foundation.ShipDef.BirdOfPrey.__dict__["Default Bridge"] = "BopBridge"
#Foundation.ShipDef.Vorcha.__dict__["Default Bridge"] = "BopBridge"

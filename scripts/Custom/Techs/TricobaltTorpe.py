# TODO: 1. Create Read Me
#	2. Create a clear guide on how to add this...
#
# Start on 2:
# At the bottom of your torpedo projectile file add this (Between the """ and """):
# You can (inf act, should) add a secondary torpedo version by copying the file and adding "_P" to the end of the new file name, which will be the torpedo after the shield
"""
try:
	modTricobaltTorpe = __import__("Custom.Techs.TricobaltTorpe")
	if(modTricobaltTorpe):
		modTricobaltTorpe.oTricobaltTorpe.AddTorpedo(__name__)
except:
	print "Tricobalt Torpedo script not installed, or you are missing Foundation Tech"
"""
# You can also add your ship to an vulnerability list (do this if your ship is actually meant to have no real energy shields but you simulated them with a shield), not only the one below, in order to keep the files unaltered... just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev.
# NOTE 2: "1" means vulnerable, other values means not vulnerable
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"Tricobalt Torpedo": 1
}
"""

global lVulnerableTricoShips # Some ships immune to this blow
lVulnerableTricoShips = (
                "AlphaWing",
                "AlphaWingEscapePod",
                "AlphaWingNoEscapePod",
                "Andromeda",
                "AndromedaBattleForm",
                "AndSlipFighter",
                "AndSlipFighterMK1",
                "AndSlipFighterMK2",
                "AndSlipFighterMK3",
                "AstralQueen",
                "B5JumpgateClosed",
                "B5JumpgateOpen",
                "B5PsiCorpMothership",
                "B5RaiderBattlewagon",
                "B5RaiderBattlewagonHalfFull",
                "B5SoulHunterVessel",
                "B5Station",
                "B5TriadTriumviron",
                "B5ZephyrRaider",
                "B5ZephyrRaider2",
                "B5ZephyrRaider3",
                "B5ZephyrRaider4",
                "B5ZephyrRaider5",
                "B5ZephyrRaider6",
                "B5ZephyrRaider7",
                "B5ZephyrRaider8",
                "Battlecrab",
                "battlecrab",
                "Battlestar",
                "battlestar",
                "bluestar",
                "BrakiriCruiser",
                "DeltaWing",
                "DeltaWingEscapePod",
                "DeltaWingNoEscapePod",
                "DRA_Raider",
                "DRA_Shuttle",
                "DraziSkySerpent",
                "DraziSunHawk",
                "DraziSunHawkWithSerpent",
                "EAAchillesFreighter",
                "EAAchillesFreighterModule1",
                "EAAchillesFreighterModule2",
                "EAAchillesFreighterModule3",
                "EAAchillesFreighterModule4",
                "EAAchillesFreighterModule5",
                "EAAchillesFreighterModule6",
                "EAAchillesFreighterModule7",
                "EAAchillesFreighterModule8",
                "EAAchillesFreighterNoModules",
                "EAAsimov",
                "EACargoPod",
                "EACrewShuttle",
                "EACrewShuttleBlue",
                "EACrewShuttleRed",
                "EAExplorer",
                "EAForceOne",
                "EAHyperion",
                "EAKestrel",
                "EANova",
                "EAOmega",
                "EAOmegaX",
                "EAPsiCorpCrewShuttle",
                "EAShadow_Hybrid",
                "EAStarfury",
                "EAStarfuryEscapePod",
                "EAStarfuryNoEscapePod",
                "EAStealthStarfury",
                "EAStealthStarfuryEscapePod",
                "EAStealthStarfuryNoEscapePod",
                "EAWorkerEscapePod",
                "EAWorkerNoEscapePod",
                "EAWorkerPod",
                "EchoWing",
                "EIntrepid",
                "GQuan",
                "Galactica",
                "GalacticaClosed",
                "HadesBasestar",
                "HadesBasestar2003",
                "HalcyonPromise",
                "HiveShip",
                "MillionVoices",
                "MinbariNial",
                "MinbariSharlin",
                "Mk10Raider",
                "MkXRaider",
                "NarnFraziFighter",
                "nx01",
                "Primus",
                "SentriFighter",
                "Shadow_Fighter",
                "Shadow_Fighter1",
                "Shadow_Fighter2",
                "Shadow_Fighter3",
                "Shadow_Fighter4",
                "Shadow_Fighter5",
                "Shadow_Fighter6",
                "Shadow_Fighter7",
                "Shadow_FighterBall",
                "Shadow_Scout",
                "TENeptune",
                "ThNor",
                "Thunderbolt",
                "TOSColDefender",
                "TIEF",
                "TIEf",
                "UENeptune",
                "VOR_Fighter",
                "Vorchan",
                "Warlock",
                "WCnx01",
                "WCnxColumbia",
                "WCnxmirror",
                "WCnxmirroravenger",
                "WraithCruiser",
                "WraithDart"
                "whitestar",
                "XCV330a",
                "XCV330o",
                "XInsect",
                "yorktown",
                "ZetaWing",
                )

import App
try:
	import Foundation
	import FoundationTech

	from ftb.Tech.ATPFunctions import *
	from math import *

	class TricobaltTorpedo(FoundationTech.TechDef):
		def __init__(self, name, dict = {}):
			FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
			self.lYields = []
			self.__dict__.update(dict)
			self.lFired = []

                def IsChronTorpYield(self):
			return 1

		def OnYield(self, pShip, pInstance, pEvent, pTorp):

			pTorp.SetLifetime(0)

			try:
				imTricobaltVulnerable = pInstance.__dict__['Tricobalt Torpedo']
				if imTricobaltVulnerable == 1:
					print "This ship has no shield, the tricobalt explosion will hit it"
				else:
					return
			except:
				global lVulnerableTricoShips
				sScript     = pShip.GetScript()
				sShipScript = string.split(sScript, ".")[-1]
				if sShipScript not in lVulnerableTricoShips:
					return

			pShipID = pShip.GetObjID()

			pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))
			if not pShip:
				return

			pHitPoint = ConvertPointNiToTG(pEvent.GetWorldHitPoint())

			pVec = pTorp.GetVelocityTG()
			pVec.Scale(0.001)
			pHitPoint.Add(pVec)

			mod = pTorp.GetModuleName()

			try:
				projectile = mod + "_P"
				torpedoScript = __import__(projectile)
				mod = projectile
			except:
				mod = pTorp.GetModuleName()

			print mod

			pTempTorp = FireTorpFromPointWithVector(pHitPoint, pVec, mod, pTorp.GetTargetID(), pTorp.GetParentID(), __import__(mod).GetLaunchSpeed())
			self.lFired.append(pTempTorp.GetObjID())

		def AddTorpedo(self, path):
			FoundationTech.dYields[path] = self

	def ConvertPointNiToTG(point):
		retval = App.TGPoint3()
		retval.SetXYZ(point.x, point.y, point.z)
		return retval

	def IsInList(item, list):
		for i in list:
			if item == i:
				return 1
		return 0

	oTricobaltTorpe = TricobaltTorpedo("Tricobalt Torpedo")
	# Just a few standard torps I know of that are Phased... 
	# All but the first one, that is the first torp on my test bed ship...
	# Should be commented out on release...
	oTricobaltTorpe.AddTorpedo("Tactical.Projectiles.TricobaltTorpedo")
except:
	print "FoundationTech, or the FTB mod, or both are not installed, \nTricobalt Torpedoes are there for NOT enabled or present in your current BC installation"
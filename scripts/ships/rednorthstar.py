import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/RNS/rednorthstar.nif",
		"FilenameMed": "data/Models/Ships/RNS/rednorthstar.nif",
		"FilenameLow": "data/Models/Ships/RNS/rednorthstar.nif",
		"Name": "rednorthstar",
		"HardpointFile": "rns",
		"Species": Multiplayer.SpeciesToShip.SOVEREIGN,
		"DamageRadMod" : 0.0,
		"DamageStrMod" : 0.0,
		"pickLeafSize" : 4.0
	 }
	return kShipStats

def LoadModel(bPreLoad = 0):
	pStats = GetShipStats()

	# Create the LOD info
	if (not App.g_kLODModelManager.Contains(pStats["Name"])):
		# Params are: File Name, PickLeafSize, SwitchOut Distance,
		# Surface Damage Res, Internal Damage Res, Burn Value, Hole Value,
		# Search String for Glow, Search string for Specular, Suffix for specular
		pLODModel = App.g_kLODModelManager.Create(pStats["Name"])
		pLODModel.AddLOD(pStats["FilenameHigh"], 10, 1000.0, 0.0, 0.0, 0, 0, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameMed"],  10, 2000.0, 0.0, 0.0, 0, 0, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameLow"],  10, 4000.0, 0.0, 0.0, 0, 0, "_glow", None, None)

		if (bPreLoad == 0):
			pLODModel.Load()
		else:
			pLODModel.LoadIncremental()

def PreLoadModel():
	LoadModel(1)

def GetArmorRatio():
      return 1.0

def GetDamageStrMod():
    return 1.0

def GetDamageRadMod():
    return 1.0

def GetForcedArmor():
    return 1

def GetArmouredModel():
    return "rednorthstar"

def GetOriginalShipModel(): # Should be this script, but for more flexibility, here you can change it to never return...
    return "rednorthstar"

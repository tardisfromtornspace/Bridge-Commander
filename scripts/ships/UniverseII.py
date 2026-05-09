import App
import Multiplayer.SpeciesToShip


def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/UniverseII/UniverseII.nif",
		"FilenameMed": "data/Models/Ships/UniverseII/UniverseII.nif",
		"FilenameLow": "data/Models/ships/UniverseII/UniverseII.nif",
		"Name": "UniverseII",
		"HardpointFile": "UniverseII",
		"Species": Multiplayer.SpeciesToShip.AMBASSADOR,
		"DamageRadMod" : 0.5,
		"DamageStrMod" : 0.5,
		"pickLeafSize" : 0.25
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 10, 2000.0, 15.0, 15.0, 4500, 18500, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameMed"],  10, 4000.0, 15.0, 15.0, 4500, 18500, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameLow"],  10, 8000.0, 15.0, 30.0, 4500, 18500, "_glow", None, None)

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

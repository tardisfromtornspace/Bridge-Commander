import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/Battlecrab/battlecrab.nif",
		"FilenameMed": "data/Models/Ships/Battlecrab/battlecrab.nif",
		"FilenameLow": "data/Models/Ships/Battlecrab/battlecrab.nif",
		"Name": "B5Battlecrab",
		"HardpointFile": "B5Battlecrab",
		"Species": Multiplayer.SpeciesToShip.SOVEREIGN,
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 10, 200.0, 20.0, 20.0, 400, 2000, "_glow", None, None)
		pLODModel.AddLOD(pStats["FilenameMed"], 10, 400.0, 20.0, 20.0, 400, 2000, "_glow", None, None)
		pLODModel.AddLOD(pStats["FilenameLow"], 10, 800.0, 20.0, 20.0, 400, 2000, "_glow", None, None)

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

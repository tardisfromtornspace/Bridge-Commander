import App
import Multiplayer.SpeciesToShip


def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/Type26Shuttle/Type26Shuttle.nif",
		"FilenameMed": "data/Models/Ships/Type26Shuttle/Type26Shuttle.nif",
		"FilenameLow": "data/Models/ships/Type26Shuttle/Type26Shuttle.nif",
		"Name": "Type26Shuttle",
		"HardpointFile": "Type26Shuttle",
		"Species": Multiplayer.SpeciesToShip.AMBASSADOR
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 15, 2000.0, 15.0, 15.0, 1200, 3500, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameMed"],  15, 4000.0, 15.0, 15.0, 1200, 3500, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameLow"],  15, 8000.0, 15.0, 30.0, 1200, 3500, "_glow", None, None)

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

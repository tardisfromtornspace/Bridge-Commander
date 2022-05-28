import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/AncientCity/AncientCity.nif",
		"FilenameMed": "data/Models/Ships/AncientCity/AncientCity.nif",
		"FilenameLow": "data/Models/Ships/AncientCity/AncientCity.nif",
		"Name": "AncientCity",
		"HardpointFile": "AncientCity",
		"Species": Multiplayer.SpeciesToShip.GALAXY
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 4, 1000.0, 0.0, 0.0, 0, 0, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameMed"],  4, 1000.0, 0.0, 0.0, 0, 0, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameLow"],  4, 1000.0, 0.0, 0.0, 0, 0, "_glow", None, None)

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

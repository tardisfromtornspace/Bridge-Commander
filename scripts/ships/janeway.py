import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/Janeway/janeway.nif",
		"FilenameMed": "data/Models/Ships/Janeway/janeway.nif",
		"FilenameLow": "data/Models/Ships/Janeway/janeway.nif",
		"Name": "Janeway",
		"HardpointFile": "janeway",
		"Species": Multiplayer.SpeciesToShip.GALAXY,
		"SpecularCoef": 0.20
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 10, 1600.0, 15.0, 15.0, 15000, 100000, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameMed"],  10, 3200.0, 15.0, 15.0, 15000, 100000, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameLow"],  10, 6400.0, 15.0, 30.0, 15000, 100000, "_glow", None, "_specular")
		pLODModel.SetTextureSharePath("data/Models/SharedTextures/FedShips")

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

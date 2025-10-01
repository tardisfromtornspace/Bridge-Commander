import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/USSLennox/USSLennox.NIF",
		"FilenameMed": "data/Models/Ships/USSLennox/USSLennox.NIF",
		"FilenameLow": "data/Models/Ships/USSLennox/USSLennox.NIF",
		"Name": "USSLennox",
		"HardpointFile": "USSLennox",
		"Species": Multiplayer.SpeciesToShip.USSLENNOX
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 10, 200.0, 25.0, 25.0, 800, 1200, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameMed"],  10, 200.0, 50.0, 50.0, 1200, 2400, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameLow"],  10, 200.0, 125.0, 125.0, 2400, 5000, "_glow", None, None)

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

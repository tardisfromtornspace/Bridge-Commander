import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = { 
		"FilenameHigh": "data/Models/Ships/B5TriadTriumviron/B5TriadTriumviron.nif",
		"FilenameMed": "data/Models/Ships/B5TriadTriumviron/B5TriadTriumviron.nif",
		"FilenameLow": "data/Models/Ships/B5TriadTriumviron/B5TriadTriumviron.nif",
		"Name": "B5TriadTriumviron",
		"HardpointFile": "B5TriadTriumviron",
		"Species": Multiplayer.SpeciesToShip.SOVEREIGN
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 10,  250.0, 0.0, 0.0, 80000, 0, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameMed"],  10, 500.0, 0.0, 0.0, 80000, 0, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameLow"],  10, 1000.0, 0.0, 0.0, 80000, 0, "_glow", None, None)

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

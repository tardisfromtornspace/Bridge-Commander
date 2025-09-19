import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/models/ships/Mk10Raider/Mk10Raider.nif",
		"FilenameMed": "data/models/ships/Mk10Raider/Mk10Raider.nif",
		"FilenameLow": "data/models/ships/Mk10Raider/Mk10Raider.nif",
		"Name": "BSG2003MkXRaider",
		"HardpointFile": "BSG2003MkXraider",
		"Species": Multiplayer.SpeciesToShip.SHUTTLE
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 10, 120.0, 5.0, 5.0, 400, 900, "_glow", None, "_specular")

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)


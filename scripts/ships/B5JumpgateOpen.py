import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = { 
		"FilenameHigh": "data/Models/Ships/B5Jumpgate/B5JumpgateOpen.nif",
		"FilenameMed": "data/Models/Ships/B5Jumpgate/B5JumpgateOpen.nif",
		"FilenameLow": "data/Models/Ships/B5Jumpgate/B5JumpgateOpen.nif",
		"Name": "B5JumpgateOpen",
		"HardpointFile": "B5JumpgateOpen",
		"Species": Multiplayer.SpeciesToShip.ASTEROID
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
		pLODModel.AddLOD(pStats["FilenameLow"],  10, 5000.0, 0.0, 0.0, 80000, 0, "_glow", None, None)

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/vger/vger.nif",
		"FilenameMed": "data/Models/Ships/vger/vger.nif",
		"FilenameLow": "data/Models/Ships/vger/vger.nif",
		"Name": "vger",
		"HardpointFile": "vger",
		"Species": Multiplayer.SpeciesToShip.STARBASE220,
		"DamageRadMod" : 0.0,
		"DamageStrMod" : 0.0
	}
	return kShipStats

def LoadModel(bPreLoad = 0):
	pStats = GetShipStats()

	# Create the LOD info
	if (not App.g_kLODModelManager.Contains(pStats["Name"])):
		# Params are: File Name, PickLeafSize, SwitchOut Distance,
		# Surface Damage Res, Internal Damage Res, Burn Value, Hole Value,
		# Search String for Glow, Search string for Specular, Suffix for specular
		pLODModel = App.g_kLODModelManager.Create(pStats["Name"], 10000, 1)
		# ***FIXME: Not all 3 levels of detail need OBB trees.  PickLeafSize should be 0 for the unused ones.
		pLODModel.AddLOD(pStats["FilenameHigh"], 4, 50000.0, 300.0, 0.0, 400, 900, "_glow", None, "_Specular")
		pLODModel.AddLOD(pStats["FilenameMed"],  4, 55000.0, 300.0, 0.0, 400, 900, "_glow", None, "_Specular")
		pLODModel.AddLOD(pStats["FilenameLow"],  4, 60000.0,   0.0, 0.0, 400, 900, "_glow", None, "_Specular")
		pLODModel.SetTextureSharePath("data/Models/SharedTextures/FedBases")

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

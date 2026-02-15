import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"DamageRadMod" : 0.320,
		#"DamageStrMod" : 1.000,
		"FilenameHigh": "data/Models/Ships/PicEntG/PicEntG.nif",
		#"FilenameMed": "data/Models/Ships/PicEntG/PicEntG.nif",
		#"FilenameLow": "data/Models/ships/PicEntG/PicEntG.nif",
		"Name": "PicEntG",
		"HardpointFile": "PicEntG",
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 10, 1500.0, 0.0, 0.0, 0, 0, "_glow", None, "_specular")
		#pLODModel.AddLOD(pStats["FilenameMed"],  10, 300.0, 15.0, 15.0, 1500, 3500, "_glow", None, "_specular")
		#pLODModel.AddLOD(pStats["FilenameLow"],  10, 1500.0, 15.0, 30.0, 1500, 3500, "_glow", None, "_specular")

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

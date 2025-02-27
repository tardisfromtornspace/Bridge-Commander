import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = { 
		"FilenameHigh": "data/Models/Ships/BorgDiamond/BorgDiamond.NIF",
		"FilenameMed": "data/Models/Ships/BorgDiamond/BorgDiamond.NIF",
		"FilenameLow": "data/Models/Ships/BorgDiamond/BorgDiamond.NIF",
		"Name": "BorgDiamond",
		"HardpointFile": "BorgDiamond",
		"Species": Multiplayer.SpeciesToShip.CARDHYBRID,
		"DamageRadMod" : 0.3,
		"DamageStrMod" : 0.7,
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 10, 300.0, 15.0, 15.0, 400, 900, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameMed"],  10, 600.0, 15.0, 15.0, 400, 900, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameLow"],  10, 900.0, 15.0, 30.0, 400, 900, "_glow", None, None)

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

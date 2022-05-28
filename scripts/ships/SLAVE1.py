import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/SLAVE1/SLAVE1.nif",
		"FilenameMed": "data/Models/Ships/SLAVE1/SLAVE1.nif",
		"FilenameLow": "data/Models/Ships/SLAVE1/SLAVE1.nif",
		"Name": "SLAVE1",
		"HardpointFile": "SLAVE1",
		"Species": Multiplayer.SpeciesToShip.SOVEREIGN,
		"DamageRadMod" : 0.01,
		"DamageStrMod" : 0.01

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
		pLODModel.AddLOD(pStats["FilenameHigh"], 10,  150.0, 85.0,  85.0, 400, 900, "_glow", None, None)
		pLODModel.AddLOD(pStats["FilenameMed"], 10,  150.0, 85.0,  85.0, 400, 900, "_glow", None, None)
		pLODModel.AddLOD(pStats["FilenameLow"], 10,  150.0, 85.0,  85.0, 400, 900, "_glow", None, None)

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

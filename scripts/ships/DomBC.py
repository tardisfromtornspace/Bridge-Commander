import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/DomBC/DomBC.NIF",
		"FilenameMed": "data/Models/Ships/DomBC/DomBC.NIF",
		"FilenameLow": "data/Models/Ships/DomBC/DomBC.NIF",
		"Name": "DomBC",
		"HardpointFile": "DomBC",
		"Species": Multiplayer.SpeciesToShip.GALAXY,
		"DamageRadMod" : 0.0,
		"DamageStrMod" : 0.0,
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 10,  250.0, 50.00, 50.0, 400, 2000, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameMed"],  10,  500.0, 75.00, 100.0, 400, 2000, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameLow"],  10, 1000.0, 100.00, 150.0, 400, 2000, "_glow", None, None)

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

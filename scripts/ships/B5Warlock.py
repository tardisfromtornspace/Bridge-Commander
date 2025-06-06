import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/Warlock/Warlock.nif",
		"FilenameMed": "data/Models/Ships/Warlock/WarlockMed.nif",
		"FilenameLow": "data/Models/Ships/Warlock/WarlockLow.nif",
		"Name": "B5Warlock",
		"HardpointFile": "B5warlock",
		"Species": Multiplayer.SpeciesToShip.MARAUDER
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 10, 100.0, 50.0, 50.0, 100, 2000, "", None, "_spec")
		pLODModel.AddLOD(pStats["FilenameMed"],  10, 200.0, 50.0, 50.0, 100, 2000, "", None, "_spec")
		pLODModel.AddLOD(pStats["FilenameLow"],  10, 350.0, 50.0, 50.0, 100, 2000, "", None, None)

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

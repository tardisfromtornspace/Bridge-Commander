import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/Crossfield/crossfield.nif",
		"FilenameMed": "data/Models/Ships/Crossfield/crossfield.nif",
		"FilenameLow": "data/Models/Ships/Crossfield/crossfield.nif",
		"Name": "Crossfield",
		"HardpointFile": "crossfield",
		"Species": Multiplayer.SpeciesToShip.AKIRA
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 2, 220.0, 15.0, 15.0, 400, 900, "", None, None)
		pLODModel.AddLOD(pStats["FilenameMed"],  2, 420.0, 15.0, 15.0, 400, 900, "", None, None)
		pLODModel.AddLOD(pStats["FilenameLow"],  2, 820.0, 15.0, 30.0, 400, 900, "", None, None)

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

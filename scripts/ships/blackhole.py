import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Misc/blackhole/Blackhole.nif",
		"FilenameMed": "data/Models/Misc/blackhole/Blackhole.nif",
		"FilenameLow": "data/Models/Misc/blackhole/Blackhole.nif",
		"Name": "Blackhole",
		"HardpointFile": "blackhole",
		"Species": Multiplayer.SpeciesToShip.BLACKHOLE
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 5, 40.0, 15.0, 15.0, 4000000000.0, 5000000000.0, "", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameMed"],  5, 100.0, 15.0, 15.0, 4000000000.0, 5000000000.0, "", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameLow"],  5, 8000.0, 15.0, 30.0, 4000000000.0, 5000000000.0, "", None, None)

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

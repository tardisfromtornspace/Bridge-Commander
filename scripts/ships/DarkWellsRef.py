import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/DarkWellsRef/DarkWellsRef.nif",
		"FilenameMed": "data/Models/Ships/DarkWellsRef/DarkWellsRef.nif",
		"FilenameLow": "data/Models/Ships/DarkWellsRef/DarkWellsRef.nif",
		"Name": "DarkWellsRef",
		"HardpointFile": "DarkWellsRef",
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 10, 400.0, 15.0, 15.0, 10000, 17500, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameMed"],  10, 800.0, 15.0, 15.0, 10000, 17500, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameLow"],  10, 1600.0, 15.0, 30.0, 10000, 17500, "_glow", None, None)

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

def GetArmorRatio():
	return 1.34

def GetForcedArmor():
	return 1
import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/LintsDomBB/LintsDomBB.nif",
		"FilenameMed": "data/Models/Ships/LintsDomBB/LintsDomBB.nif",
		"FilenameLow": "data/Models/Ships/LintsDomBB/LintsDomBB.nif",
		"Name": "Dominion Battleship",
		"HardpointFile": "LintsDomBB",
		"Species": Multiplayer.SpeciesToShip.SOVEREIGN,
		"SpecularCoef": 0.7
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 10, 200.0, 15.0, 15.0, 50000, 20000, "_glow", None, "_spec")
		pLODModel.AddLOD(pStats["FilenameMed"],  10, 400.0, 15.0, 15.0, 50000, 20000, "_glow", None, "_spec")
		pLODModel.AddLOD(pStats["FilenameLow"],  10, 800.0, 15.0, 30.0, 50000, 20000, "_glow", None, "_spec")

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/StarcraftIIDominionMinotaur/DominionMinotaurFrontLeftTurret.nif",
		"FilenameMed": "data/Models/Ships/StarcraftIIDominionMinotaur/DominionMinotaurFrontLeftTurret.nif",
		"FilenameLow": "data/Models/Ships/StarcraftIIDominionMinotaur/DominionMinotaurFrontLeftTurret.nif",
		"Name": "StarcraftIIMinotaurDominionTurretFrontLeft",
		"HardpointFile": "StarcraftIIMinotaurDominionTurretFrontLeft",
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 100, 300.0, 15.0, 0.0, 2000, 0, "_GLOW", None, "_SPEC") # the burn and hole values were 2000 and 8000
		pLODModel.AddLOD(pStats["FilenameMed"],  100, 500.0, 15.0, 0.0, 2000, 0, "_GLOW", None, "_SPEC")
		pLODModel.AddLOD(pStats["FilenameLow"],  100, 700.0, 15.0, 0.0, 2000, 0, "_GLOW", None, None)

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

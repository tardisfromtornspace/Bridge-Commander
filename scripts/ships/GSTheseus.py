import App
import Multiplayer.SpeciesToShip


def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/GSTheseus/GSTheseus.nif",
		"FilenameMed": "data/Models/Ships/GSTheseus/GSTheseus.nif",
		"FilenameLow": "data/Models/ships/GSTheseus/GSTheseus.nif",
		"Name": "GSTheseus",
		"HardpointFile": "GSTheseus",
		"Species": Multiplayer.SpeciesToShip.SOVEREIGN,
		"DamageRadMod" : 0.00625, 
		"DamageStrMod" : 0.00625,
		
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 10, 200.0, 15.0, 15.0, 3500, 4250, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameMed"],  10, 400.0, 15.0, 15.0, 3500, 4250, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameLow"],  10, 800.0, 15.0, 30.0, 3500, 4250, "_glow", None, "_specular")

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
	return 0.01

def GetDamageStrMod():
	return 0.000625

def GetDamageRadMod():
	return 0.0000625

def GetForcedArmor():
	return 1
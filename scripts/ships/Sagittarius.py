import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/Sagittarius/Sagittarius.nif",
		"FilenameMed": "data/Models/Ships/Sagittarius/Sagittarius.nif",
		"FilenameLow": "data/Models/Ships/Sagittarius/Sagittarius.nif",
		"Name": "Sagittarius",
		"HardpointFile": "Sagittarius",
		"Species": Multiplayer.SpeciesToShip.SOVEREIGN,
		"DamageRadMod" : 0.0000625, 
		"DamageStrMod" : 0.000625,
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 10, 10000.0, 15.0, 15.0, 2900, 4300, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameMed"],  10, 10000.0, 15.0, 15.0, 2900, 4300, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameLow"],  10, 10000.0, 15.0, 30.0, 2900, 4300, "_glow", None, "_specular")
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
	return 0.1

def GetDamageStrMod():
	return 0.000625

def GetDamageRadMod():
	return 0.0000625

def GetForcedArmor():
	return 1



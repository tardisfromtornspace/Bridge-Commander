import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/TalynAndromedaHybrid/High/LeviathanAndromeda.nif",
		"FilenameMed": "data/Models/Ships/TalynAndromedaHybrid/High/LeviathanAndromeda.nif",
		"FilenameLow": "data/Models/Ships/TalynAndromedaHybrid/High/LeviathanAndromeda.nif",
		"Name": "AndromedaTalyn",
		"HardpointFile": "AndromedaTalyn",
		"Species": Multiplayer.SpeciesToShip.SOVEREIGN,
		"SpecularCoef": 0.5,
		"DamageRadMod" : 0.15,
		"DamageStrMod" : 0.0666
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 10, 2000.0, 15.0, 15.0, 400, 9000000, "_glow", None, None)
		pLODModel.AddLOD(pStats["FilenameMed"],  10, 4000.0, 15.0, 15.0, 400, 9000000, "_glow", None, None)
		pLODModel.AddLOD(pStats["FilenameLow"],  10, 8000.0, 15.0, 30.0, 400, 9000000, "_glow", None, None)

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

def ImImmuneToZNeutrinos(): # Immunity against Reality Bombs
      return 1
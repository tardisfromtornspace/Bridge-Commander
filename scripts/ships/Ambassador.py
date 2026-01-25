import App
import Multiplayer.SpeciesToShip


def GetShipStats():

	kShipStats = None
	pGame = App.Game_GetCurrentGame()
	if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
		kShipStats = {
			"FilenameHigh": "data/Models/Ships/Ambassador/Ambassador.nif",
			"FilenameMed": "data/Models/Ships/Ambassador/AmbassadorMed.nif",
			"FilenameLow": "data/Models/Ships/Ambassador/AmbassadorLow.nif",
			"Name": "Ambassador",
			"HardpointFile": "ambassador",
			"Species": Multiplayer.SpeciesToShip.AMBASSADOR
		}
	else:
		kShipStats = {
			"DamageRadMod" : 0.75, 
			"DamageStrMod" : 0.75,
			#"FilenameHigh": "data/Models/Ships/FedAmb_X_P81/FedAmb_X_P81_Trio.NIF",
			#"FilenameMed": "data/Models/Ships/FedAmb_X_P81/FedAmb_X_P81_Trio.NIF",
			#"FilenameLow": "data/Models/Ships/FedAmb_X_P81/FedAmb_X_P81_Trio.NIF",
			"FilenameHigh": "data/Models/Ships/DJAmbassador/DJRepublic.NIF",
			"FilenameMed": "data/Models/Ships/DJAmbassador/DJRepublic.NIF",
			"FilenameLow": "data/Models/Ships/DJAmbassador/DJRepublic.NIF",
			"Name": "AmbassadorImproved",
			"HardpointFile": "ambassador",
			"Species": Multiplayer.SpeciesToShip.AMBASSADOR
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 10, 200.0, 15.0, 15.0, 400, 900, "_glow", None, None)
		pLODModel.AddLOD(pStats["FilenameMed"],  10, 400.0, 15.0, 15.0, 400, 900, "_glow", None, None)
		pLODModel.AddLOD(pStats["FilenameLow"],  10, 800.0, 15.0, 30.0, 400, 900, "_glow", None, None)

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

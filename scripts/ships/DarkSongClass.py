import App
import Multiplayer.SpeciesToShip

def GetShipStats():
    kShipStats = {"FilenameHigh": "data/Models/Ships/DarkSongClass/DarkSongClass.nif",
                  "FilenameMed": "data/Models/Ships/DarkSongClass/DarkSongClass.nif",
                  "FilenameLow": "data/Models/Ships/DarkSongClass/DarkSongClass.nif",
                  "Name": "DarkSongClass",
                  "HardpointFile": "DarkSongClass",
                  "Species": Multiplayer.SpeciesToShip.NEBULA}
    return kShipStats


def LoadModel(bPreLoad = 0):
    pStats = GetShipStats()
    if (not App.g_kLODModelManager.Contains(pStats["Name"])):
        pLODModel = App.g_kLODModelManager.Create(pStats["Name"])
        pLODModel.AddLOD(pStats["FilenameHigh"], 10, 50.0, 15.0, 15.0, 12000, 23000, "_glow", None, None)
        pLODModel.AddLOD(pStats["FilenameMed"], 10, 150.0, 15.0, 15.0, 12000, 23000, "_glow", None, None)
        pLODModel.AddLOD(pStats["FilenameLow"], 10, 1000.0, 15.0, 30.0, 12000, 23000, "_glow", None, None)
        pLODModel.SetTextureSharePath("data/Models/SharedTextures/FedAlphaShips")
        if (bPreLoad == 0):
            pLODModel.Load()
        else:
            pLODModel.LoadIncremental()


def PreLoadModel():
    LoadModel(1)

def GetArmorRatio():
	return 0.8

def GetForcedArmor():
	return 1
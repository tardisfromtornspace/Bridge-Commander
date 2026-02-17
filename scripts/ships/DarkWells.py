import App
import Multiplayer.SpeciesToShip

def GetShipStats():
    kShipStats = {"FilenameHigh": "data/Models/Ships/DarkWells/DarkWells.nif",
                  "FilenameMed": "data/Models/Ships/DarkWells/DarkWells.nif",
                  "FilenameLow": "data/Models/Ships/DarkWells/DarkWells.nif",
                  "Name": "DarkWells",
                  "HardpointFile": "DarkWells",
                  "Species": Multiplayer.SpeciesToShip.NEBULA}
    return kShipStats


def LoadModel(bPreLoad = 0):
    pStats = GetShipStats()
    if (not App.g_kLODModelManager.Contains(pStats["Name"])):
        pLODModel = App.g_kLODModelManager.Create(pStats["Name"])
        pLODModel.AddLOD(pStats["FilenameHigh"], 10, 50.0, 15.0, 15.0, 7500, 15000, "_glow", None, "_specular")
        pLODModel.AddLOD(pStats["FilenameMed"], 10, 150.0, 15.0, 15.0, 7500, 15000, "_glow", None, "_specular")
        pLODModel.AddLOD(pStats["FilenameLow"], 10, 1000.0, 15.0, 30.0, 7500, 15000, "_glow", None, "_specular")
        pLODModel.SetTextureSharePath("data/Models/SharedTextures/FedAlphaShips")
        if (bPreLoad == 0):
            pLODModel.Load()
        else:
            pLODModel.LoadIncremental()


def PreLoadModel():
    LoadModel(1)

def GetArmorRatio():
	return 1.2

def GetForcedArmor():
	return 1
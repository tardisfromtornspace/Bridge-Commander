import App
import Multiplayer.SpeciesToShip

def GetShipStats():
    kShipStats = {"FilenameHigh": "data/Models/Ships/HGWells/HGWells.nif",
                  "FilenameMed": "data/Models/Ships/HGWells/HGWells.nif",
                  "FilenameLow": "data/Models/Ships/HGWells/HGWells.nif",
                  "Name": "HGWells",
                  "HardpointFile": "HGWells",
                  "Species": Multiplayer.SpeciesToShip.NEBULA,
                  #"DamageRadMod" : 0.525, 
                  #"DamageStrMod" : 0.0625,
                 }
    return kShipStats


def LoadModel(bPreLoad = 0):
    pStats = GetShipStats()
    if (not App.g_kLODModelManager.Contains(pStats["Name"])):
        pLODModel = App.g_kLODModelManager.Create(pStats["Name"])
        pLODModel.AddLOD(pStats["FilenameHigh"], 10, 50.0, 15.0, 15.0, 12000, 24000, "_glow", None, "_specular")
        pLODModel.AddLOD(pStats["FilenameMed"], 10, 150.0, 15.0, 15.0, 12000, 24000, "_glow", None, "_specular")
        pLODModel.AddLOD(pStats["FilenameLow"], 10, 1000.0, 15.0, 30.0, 12000, 24000, "_glow", None, "_specular")
        pLODModel.SetTextureSharePath("data/Models/SharedTextures/FedAlphaShips")
        if (bPreLoad == 0):
            pLODModel.Load()
        else:
            pLODModel.LoadIncremental()


def PreLoadModel():
    LoadModel(1)


def GetArmorRatio():
	return 1.0

#def GetDamageStrMod():
#	return 0.0625

#def GetDamageRadMod():
#	return 0.525

def GetForcedArmor():
	return 1
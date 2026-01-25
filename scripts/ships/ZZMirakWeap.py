import App
import Multiplayer

def GetShipStats():
    kShipStats = {'FilenameHigh': 'data/Models/Ships/ZZMirakWeap/ZZMirakWeap.NIF', 'Name': 'ZZMirakWeap', 'HardpointFile': 'ZZMirakWeapHP', 'Species': (Multiplayer.SpeciesToShip.MINE)}
    return kShipStats


def LoadModel(bPreLoad=0):
    pStats = GetShipStats()
    if not App.g_kLODModelManager.Contains(pStats['Name']):
        pLODModel = App.g_kLODModelManager.Create(pStats['Name'])
        pLODModel.AddLOD(pStats['FilenameHigh'], 10, 1000.0, 1.5, 1.5, 499, 500, None, None, None)
        pLODModel.SetTextureSharePath('data/Models/Ships/ZZMirakWeap/')
        if bPreLoad == 0:
            pLODModel.Load()
        else:
            pLODModel.LoadIncremental()
    return


def PreLoadModel():
    LoadModel(1)
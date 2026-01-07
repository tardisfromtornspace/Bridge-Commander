# File: Z (Python 1.5)

import App
import Multiplayer.SpeciesToShip

def GetShipStats():
    kShipStats = {
        'FilenameHigh': 'data/Models/Ships/ZZRMine/ZZRMine.NIF',
        'Name': 'ZZRMine',
        'HardpointFile': 'ZZRMineHP',
        'Species': Multiplayer.SpeciesToShip.MINE }
    return kShipStats


def LoadModel(bPreLoad = 0):
    pStats = GetShipStats()
    if not App.g_kLODModelManager.Contains(pStats['Name']):
        pLODModel = App.g_kLODModelManager.Create(pStats['Name'])
        pLODModel.AddLOD(pStats['FilenameHigh'], 10, 1000.0, 1.5, 1.5, 499, 500, None, None, None)
        pLODModel.SetTextureSharePath('data/Models/Ships/ZZRMine/')
        if bPreLoad == 0:
            pLODModel.Load()
        else:
            pLODModel.LoadIncremental()
    
    return None


def PreLoadModel():
    LoadModel(1)


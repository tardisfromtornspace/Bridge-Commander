# File: P (Python 1.5)

import App
import Multiplayer.SpeciesToShip as Multiplayer

def GetShipStats():
    kShipStats = {
        'FilenameHigh': 'data/Models/Ships/phoenix/phoenix.nif',
        'FilenameMed': 'data/Models/Ships/phoenix/phoenix.nif',
        'FilenameLow': 'data/Models/Ships/phoenix/phoenix.nif',
        'Name': 'phoenix',
        'HardpointFile': 'phoenix',
        'Species': Multiplayer.SpeciesToShip.PHOENIX }
    return kShipStats


def LoadModel(bPreLoad = 0):
    pStats = GetShipStats()
    if not App.g_kLODModelManager.Contains(pStats['Name']):
        pLODModel = App.g_kLODModelManager.Create(pStats['Name'])
        pLODModel.AddLOD(pStats['FilenameHigh'], 10, 120.0, 15.0, 15.0, 400, 900, '_glow', None, '_specular')
        pLODModel.AddLOD(pStats['FilenameMed'], 10, 300.0, 15.0, 15.0, 400, 900, '_glow', None, '_specular')
        pLODModel.AddLOD(pStats['FilenameLow'], 10, 600.0, 15.0, 30.0, 400, 900, '_glow', None, None)
        pLODModel.SetTextureSharePath('data/Models/SharedTextures/CardShips')
        if bPreLoad == 0:
            pLODModel.Load()
        else:
            pLODModel.LoadIncremental()
    


def PreLoadModel():
    LoadModel(1)


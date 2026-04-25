# File: Z (Python 1.5)

import App
import Multiplayer.SpeciesToShip

def GetShipStats():
    kShipStats = {
        'FilenameHigh': 'data/Models/Ships/ZZRepShip/ZZRepShip.nif',
        'FilenameMed': 'data/Models/Ships/ZZRepShip/ZZRepShip.nif',
        'FilenameLow': 'data/Models/Ships/ZZRepShip/ZZRepShip.nif',
        'Name': 'ZZRepShip',
        'HardpointFile': 'ZZRepShip',
        'Species': Multiplayer.SpeciesToShip.VORCHA }
    return kShipStats


def LoadModel(bPreLoad = 0):
    pStats = GetShipStats()
    if not App.g_kLODModelManager.Contains(pStats['Name']):
        pLODModel = App.g_kLODModelManager.Create(pStats['Name'])
        pLODModel.AddLOD(pStats['FilenameHigh'], 10, 50.0, 15.0, 15.0, 400, 1100, '', None, '_specular')
        pLODModel.AddLOD(pStats['FilenameMed'], 10, 100.0, 15.0, 15.0, 400, 1100, '', None, '_specular')
        pLODModel.AddLOD(pStats['FilenameLow'], 10, 750.0, 15.0, 30.0, 400, 1100, '', None, None)
        if bPreLoad == 0:
            pLODModel.Load()
        else:
            pLODModel.LoadIncremental()
    


def PreLoadModel():
    LoadModel(1)


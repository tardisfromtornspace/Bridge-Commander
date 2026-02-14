# File: Z (Python 1.5)

import App
import Multiplayer.SpeciesToShip

def GetShipStats():
    kShipStats = {
        'FilenameHigh': 'data/Models/Ships/ZZGalileoShuttle/ZZGalileoShuttle.nif',
        'FilenameMed': 'data/Models/Ships/ZZGalileoShuttle/ZZGalileoShuttle.nif',
        'FilenameLow': 'data/Models/Ships/ZZGalileoShuttle/ZZGalileoShuttle.nif',
        'Name': 'ZZGalileoShuttle',
        'HardpointFile': 'ZZGalileoShuttleHP',
        'Species': Multiplayer.SpeciesToShip.AMBASSADOR }
    return kShipStats


def LoadModel(bPreLoad = 0):
    pStats = GetShipStats()
    if not App.g_kLODModelManager.Contains(pStats['Name']):
        pLODModel = App.g_kLODModelManager.Create(pStats['Name'])
        pLODModel.AddLOD(pStats['FilenameHigh'], 10, 200.0, 15.0, 15.0, 200, 400, '_glow', None, '_specular')
        pLODModel.AddLOD(pStats['FilenameMed'], 10, 400.0, 15.0, 15.0, 200, 400, '_glow', None, '_specular')
        pLODModel.AddLOD(pStats['FilenameLow'], 10, 800.0, 15.0, 30.0, 200, 400, '_glow', None, None)
        if bPreLoad == 0:
            pLODModel.Load()
        else:
            pLODModel.LoadIncremental()
    


def PreLoadModel():
    LoadModel(1)


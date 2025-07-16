# File: Z (Python 1.5)

import App
import Multiplayer.SpeciesToShip

def GetShipStats():
    kShipStats = {
        'FilenameHigh': 'data/Models/Ships/ZZBorgSC/ZZBorgSC.nif',
        'FilenameMed': 'data/Models/Ships/ZZBorgSC/ZZBorgSC.nif',
        'FilenameLow': 'data/Models/Ships/ZZBorgSC/ZZBorgSC.nif',
        'Name': 'ZZBorgSC',
        'HardpointFile': 'ZZBorgSCHP',
        'Species': Multiplayer.SpeciesToShip.GALOR,
        "DamageRadMod" : 0.3,
        "DamageStrMod" : 0.1 }
    return kShipStats


def LoadModel(bPreLoad = 0):
    pStats = GetShipStats()
    if not App.g_kLODModelManager.Contains(pStats['Name']):
        pLODModel = App.g_kLODModelManager.Create(pStats['Name'], 10000, 1)
        pLODModel.AddLOD(pStats['FilenameHigh'], 10, 1000.0, 15.0, 15.0, 400, 9000, '_glow', None, '_specular')
        pLODModel.AddLOD(pStats['FilenameMed'], 10, 5000.0, 15.0, 15.0, 400, 9000, '_glow', None, '_specular')
        pLODModel.AddLOD(pStats['FilenameLow'], 10, 10000.0, 15.0, 30.0, 400, 9000, '_glow', None, '_specular')
        if bPreLoad == 0:
            pLODModel.Load()
        else:
            pLODModel.LoadIncremental()
    


def PreLoadModel():
    LoadModel(1)


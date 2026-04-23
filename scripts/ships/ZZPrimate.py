import App
import Multiplayer

def GetShipStats():
    kShipStats = {'FilenameHigh': 'data/Models/Ships/ZZPrimate/ZZPrimate.nif',
		  'FilenameMed': 'data/Models/Ships/ZZPrimate/ZZPrimate.nif',
		  'FilenameLow': 'data/Models/Ships/ZZPrimate/ZZPrimate.nif',
		  'Name': 'ZZPrimate',
		  'HardpointFile': 'ZZPrimate',
		  'Species': (Multiplayer.SpeciesToShip.VORCHA)}
    return kShipStats


def LoadModel(bPreLoad=0):
    pStats = GetShipStats()
    if not App.g_kLODModelManager.Contains(pStats['Name']):
        pLODModel = App.g_kLODModelManager.Create(pStats['Name'])
        pLODModel.AddLOD(pStats['FilenameHigh'], 10, 50.0, 15.0, 15.0, 440, 1100, '_glow', '_specular', '_specular')
        pLODModel.AddLOD(pStats['FilenameMed'], 10, 100.0, 15.0, 15.0, 440, 1100, '_glow', '_specular', '_specular')
        pLODModel.AddLOD(pStats['FilenameLow'], 10, 750.0, 15.0, 30.0, 440, 1100, '_glow', '_specular', '_specular')
        if bPreLoad == 0:
            pLODModel.Load()
        else:
            pLODModel.LoadIncremental()


def PreLoadModel():
    LoadModel(1)
import App
import Multiplayer.SpeciesToShip

def GetShipStats():
    kShipStats = {'FilenameHigh': 'data/Models/Ships/Birdofprey/Birdofprey.nif', 'FilenameMed': 'data/Models/Ships/Birdofprey/Birdofprey.nif', 'FilenameLow': 'data/Models/Ships/Birdofprey/Birdofprey.nif', 'Name': 'BirdofPrey', 'HardpointFile': 'CloakFireBirdOfPrey', 'Species': Multiplayer.SpeciesToShip.CLOAKFIREBIRDOFPREY}
    return kShipStats


def LoadModel(bPreLoad = 0):
    pStats = GetShipStats()
    if (not App.g_kLODModelManager.Contains(pStats['Name'])):
        pLODModel = App.g_kLODModelManager.Create(pStats['Name'])
        pLODModel.AddLOD(pStats['FilenameHigh'], 10, 40.0, 15.0, 15.0, 400, 900, '_glow', None, '_specular')
        pLODModel.AddLOD(pStats['FilenameMed'], 10, 100.0, 15.0, 15.0, 400, 900, '_glow', None, '_specular')
        pLODModel.AddLOD(pStats['FilenameLow'], 10, 500.0, 15.0, 30.0, 400, 900, '_glow', None, None)
        if (bPreLoad == 0):
            pLODModel.Load()
        else:
            pLODModel.LoadIncremental()

def PreLoadModel():
	LoadModel(1)

def GetPulseModule(pulsenum):
	if (pulsenum==1):
		return 'Tactical.Projectiles.PulseDisruptor'
	if (pulsenum==2):
		return 'Tactical.Projectiles.AdvPulseDisruptor'
	return 'End'

def GetPulseName(pulsenum):
	if (pulsenum==1):
		return 'Cannon: Std'
	if (pulsenum==2):
		return 'Cannon: Adv'
	return 'No Name'

def GetArmorRatio():
	return 0.4

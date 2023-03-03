import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = { 
		"FilenameHigh": "data/Models/Ships/WarShipIntrepid/WarShipIntrepid.nif",
		"FilenameMed": "data/Models/Ships/WarShipIntrepid/WarShipIntrepid.nif",
		"FilenameLow": "data/Models/Ships/WarShipIntrepid/WarShipIntrepid.nif",
		"Name": "WarShipIntrepid",
		"HardpointFile": "WarShipIntrepid",
		"Species": Multiplayer.SpeciesToShip.AKIRA
	}
	return kShipStats

def LoadModel(bPreLoad = 0):
	pStats = GetShipStats()

	# Create the LOD info
	if (not App.g_kLODModelManager.Contains(pStats["Name"])):
		# Params are: File Name, PickLeafSize, SwitchOut Distance,
		# Surface Damage Res, Internal Damage Res, Burn Value, Hole Value,
		# Search String for Glow, Search string for Specular, Suffix for specular
		pLODModel = App.g_kLODModelManager.Create(pStats["Name"])
		pLODModel.AddLOD(pStats["FilenameHigh"], 10,  20.0, 15.0, 15.0, 400, 900, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameMed"],  10, 100.0, 15.0, 15.0, 400, 900, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameLow"],  10, 500.0, 15.0, 30.0, 400, 900, "_glow", None, None)

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

def GetPulseModule(pulsenum):
	if (pulsenum==1):
		return 'Tactical.Projectiles.BeoPhoton'
	if (pulsenum==2):
		return 'Tactical.Projectiles.WarTorpedo'
	return 'End'

def GetPulseName(pulsenum):
	if (pulsenum==1):
		return 'Cannon: BeoPhoton'
	if (pulsenum==2):
		return 'Cannon: WAR'
	return 'No Name'

def GetArmorRatio():
	return 0.7
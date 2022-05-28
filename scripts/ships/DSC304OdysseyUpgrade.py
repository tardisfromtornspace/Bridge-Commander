import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"DamageRadMod" : 0.75, 
		"DamageStrMod" : 0.75, 
		"FilenameHigh": "data/Models/Ships/DSC304/DSC304Odyssey.nif",
		"FilenameMed": "data/Models/Ships/DSC304/DSC304Odyssey.nif",
		"FilenameLow": "data/Models/Ships/DSC304/DSC304Odyssey.nif",
		"Name": "DSC304OdysseyUpgrade",
		"HardpointFile": "DSC304OdysseyUpgrade",
		"Species": Multiplayer.SpeciesToShip.MARAUDER
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 10, 120.0, 15.0, 15.0, 400, 900, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameMed"],  10, 300.0, 15.0, 15.0, 400, 900, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameLow"],  10, 800.0, 15.0, 30.0, 400, 900, "_glow", None, "_specular")

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

def HyperdriveCustomizations():
        dict = {'TunnelTexture' : 'Hyperspace4.tga',
                'ExitSound' : 'hypexit1.wav',
                'FlashAnimation' : 'HyperdriveFlashPurple.tga',
                'EntrySound' : 'hypentry1.wav',
                'MaxSpeed' : 9.1}
        return dict

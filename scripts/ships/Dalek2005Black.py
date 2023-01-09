import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/Dalek2005/Dalek2005Black.nif",
		"FilenameMed": "data/Models/Ships/Dalek2005/Dalek2005Black.nif",
		"FilenameLow": "data/Models/Ships/Dalek2005/Dalek2005Black.nif",
		"Name": "Dalek2005Black",
		"HardpointFile": "Dalek2005Black",
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 10, 200.0, 0.0, 15.0, 0, 490, "_glow", None, None)
		pLODModel.AddLOD(pStats["FilenameMed"],  10, 400.0, 0.0, 15.0, 0, 490, "_glow", None, None)
         	pLODModel.AddLOD(pStats["FilenameLow"],  10, 800.0, 0.0, 30.0, 0, 490, "_glow", None, None)
#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

def GetArmorRatio(): # Strength of the armor, in a way
      return 0.005

def GetDamageStrMod(): # visual damage strength
	return 0.1

def GetDamageRadMod(): # visual damage radius
	return 0.1

def GetForcedArmor(): # If everyone is forced to wear it once it loads
	return 1

def GetArmouredModel(): # OPTIONAL: Select another scripts/ships/yourShip2.py with a adifferent model so when you are armored you change to this
	return "Dalek2005Black"

def GetOriginalShipModel(): # Should be the same script scripts/ships/yourShip2.py, but for more flexibility, here you can change it to never return when the armor drops
	return "Dalek2005Black"

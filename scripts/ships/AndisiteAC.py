import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/AndisiteAC/AndisiteAC.nif",
		"FilenameMed": "data/Models/Ships/AndisiteAC/AndisiteAC.nif",
		"FilenameLow": "data/Models/Ships/AndisiteAC/AndisiteAC.nif",
		"Name": "AndisiteAC",
		"HardpointFile": "AndisiteAC",
		"Species": Multiplayer.SpeciesToShip.AKIRA,
		"DamageRadMod" : 0.0,
		"DamageStrMod" : 0.0,
		"pickLeafSize" : 4.0
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 2, 120.0, 15.0, 15.0, 155000, 350000, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameMed"],  2, 300.0, 15.0, 15.0, 155000, 350000, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameLow"],  2, 600.0, 15.0, 30.0, 155000, 350000, "_glow", None, "_specular")

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
      return 0.2

def GetDamageStrMod(): # visual damage strength
	return 1.0

def GetDamageRadMod(): # visual damage radius
	return 1.0

def GetForcedArmor(): # If everyone is forced to wear it once it loads
	return 1

def GetArmouredModel(): # OPTIONAL: Select another scripts/ships/yourShip2.py with a adifferent model so when you are armored you change to this
	return "AndisiteAC"

def GetOriginalShipModel(): # Should be the same script scripts/ships/yourShip2.py, but for more flexibility, here you can change it to never return when the armor drops
	return "AndisiteAC"


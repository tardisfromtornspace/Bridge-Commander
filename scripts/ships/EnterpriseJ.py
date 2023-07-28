# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
#         EnterpriseJ.py by Alex SL Gato
#         Version 1.3.6
#         24th July 2023
#         Based on previous versions done by EnterpriseJ and WileyCoyote
#                          
#################################################################################################################

import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"DamageRadMod" : 0.00000000625, 
		"DamageStrMod" : 0.00000000625,
		#"SpecularCoef": 30.0,
		"FilenameHigh": "data/Models/Ships/EnterpriseJ/CanonEnterpriseJ.nif",
		"FilenameMed": "data/Models/Ships/EnterpriseJ/CanonEnterpriseJ.nif",
		"FilenameLow": "data/Models/Ships/EnterpriseJ/CanonEnterpriseJ.nif",
		"Name": "EnterpriseJ",
		"HardpointFile": "EnterpriseJ",
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 10, 600.0, 15.0, 15.0, 9000, 382000, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameMed"],  10, 1500.0, 15.0, 15.0, 9000, 382000, "_glow", None, None)
		pLODModel.AddLOD(pStats["FilenameLow"],  10, 1800.0, 15.0, 30.0, 9000, 382000, "_glow", None, None)

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

def GetArmorRatio():
      return 1.55

def GetDamageStrMod():
	return 0

def GetDamageRadMod():
	return 0

def GetForcedArmor():
	return 1

def GetArmouredModel():
	return "EnterpriseJArmor"

def GetOriginalShipModel(): # Should be this script, but for more flexibility, here you can change it to never return...
	return "EnterpriseJ"

def IsTachyonImmune():
	return 1

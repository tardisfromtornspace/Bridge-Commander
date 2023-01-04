import App
import Multiplayer.SpeciesToShip

# using the textures as a way to emulate the Technomage hiding as something else
# The low resolution is for when it wants to remain undetected - it'll be seen as an asteroid
# the med is for when it tries to scare us to not approach further - it'll be seen as a Giant Sword XD
# the high is for when we get too close and the technomage decides to just reveal itself.
def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/B5TechnomageTransport/B5TechnomageTransport.nif",
		"FilenameMed": "data/Models/Ships/B5TechnomageTransport/SwordIllusion.NIF",
		"FilenameLow": "data/Models/Misc/AsteroidsIllusion/asteroid.nif",
		"Name": "B5TechnomageTransportIllusion",
		"HardpointFile": "B5TechnomageTransport",
		"Species": Multiplayer.SpeciesToShip.SHUTTLE
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 10, 150.0, 0.0, 0.0, 400, 900, "_glow", None, None)
		pLODModel.AddLOD(pStats["FilenameMed"], 10, 600.0, 0.0, 0.0, 400, 900, "_glow", None, None)
		pLODModel.AddLOD(pStats["FilenameLow"],  10, 800.0, 15.0, 0.0, 400, 900, "_glow", None, None)

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

import Foundation

# Uncomment the below to enable!
Foundation.BridgeDef('Galor', 'Galorbridge', dict = {
	'modes': [ Foundation.MutatorDef.Stock ],
	'locations': {
		'SCPHelm':	[ 'data/animations/SCP_stand_h_m.nif', 'SCP_stand_h_m' ],
		'SCPTactical':	[ 'data/animations/SCP_stand_t_l.nif', 'SCP_stand_t_l' ],
		'SCPCommander':	[ 'data/animations/SCP_stand_c_m.nif', 'SCP_stand_c_m' ],
		'SCPScience':	[ 'data/animations/SCP_stand_S_S.nif', 'SCP_stand_s_s' ],
		'SCPEngineer':	[ 'data/animations/SCP_stand_e_s.nif', 'SCP_stand_e_s' ],
		'SCPGuest':	[ 'data/animations/SCP_stand_X_m.nif', 'SCP_stand_X_m' ],
		'SCPL1S':	[ 'data/animations/SCP_L1toG3_S.nif', 'SCP_L1toG3_s', 'pCharacter.SetHidden(1)' ],
		'SCPL1M':	[ 'data/animations/SCP_L1toG3_M.nif', 'SCP_L1toG3_M', 'pCharacter.SetHidden(1)' ],
		'SCPL1L':	[ 'data/animations/SCP_L1toG3_L.nif', 'SCP_L1toG3_L', 'pCharacter.SetHidden(1)' ],
		'SCPL2M':	[ 'data/animations/SCP_L2toG2_M.nif', 'SCP_L2toG2_M', 'pCharacter.SetHidden(1)' ],
		'SCPG1M':	[ 'data/animations/SCP_G1toL2_M.nif', 'SCP_G1toL2_M' ],
		'SCPG2M':	[ 'data/animations/SCP_G2toL2_M.nif', 'SCP_G2toL2_M' ],
		'SCPG3M':	[ 'data/animations/SCP_G3toL1_M.nif', 'SCP_G3toL1_M' ],
	},
	'Maps':{
		'CurrentMaps': {"lightone": "lightone"},
		'GreenMaps':{'lightone': 'data/Models/Sets/Galorbridge/High/lightone.tga'},
		'YellowMaps':{'lightone': 'data/Models/Sets/Galorbridge/High/lightone.tga'},
		'RedMaps':{'lightone': 'data/Models/Sets/Galorbridge/High/lightone_red.tga'},
},
	"bridgeSound": {
			"LiftDoor": {"volume": 0.6,"file": "sfx/Galor/door.wav", "group": "BridgeGeneric"},
			"AmbBridge": {"volume": 0.3,"file": "sfx/Galor/ambience.wav", "group": "BridgeGeneric"},
			"RedAlertSound": {"volume": 1.0,"file": "sfx/Galor/red.wav", "group": "BridgeGeneric"},
			"YellowAlertSound": {"volume": 1.0,"file": "sfx/Galor/yellow.wav", "group": "BridgeGeneric"},
			"GreenAlertSound": {"volume": 1.0,"file": "sfx/Galor/green.wav", "group": "BridgeGeneric"},
			"ViewOn": {"volume": 1.0,"file": "sfx/Galor/hail.wav", "group": "BridgeGeneric"},
			"ViewOff": {"volume": 1.0,"file": "sfx/Galor/hail.wav", "group": "BridgeGeneric"}},
	"LoadingScreen": "data/Icons/LoadingScreens/GalorLoading.tga",
} )
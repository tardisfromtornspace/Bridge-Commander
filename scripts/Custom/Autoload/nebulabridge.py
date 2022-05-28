import Foundation

Foundation.BridgeDef('Nebula', 'nebulabridge', dict = {
	'modes': [ Foundation.MutatorDef.Stock ],
	'locations': {
		'NebHelm':	[ 'data/animations/Neb_stand_h_m.nif', 'Neb_stand_h_m' ],
		'NebTactical':	[ 'data/animations/Neb_stand_t_l.nif', 'Neb_stand_t_l' ],
		'NebCommander':	[ 'data/animations/Neb_stand_c_m.nif', 'Neb_stand_c_m' ],
		'NebScience':	[ 'data/animations/Neb_stand_s_s.nif', 'Neb_stand_s_s' ],
		'NebEngineer':	[ 'data/animations/Neb_stand_e_s.nif', 'Neb_stand_e_s' ],
		'NebGuest':	[ 'data/animations/Neb_stand_X_m.nif', 'Neb_stand_X_m' ],
		'NebL1S':	[ 'data/animations/Neb_L1toG3_S.nif', 'Neb_L1toG3_s', 'pCharacter.SetHidden(1)' ],
		'NebL1M':	[ 'data/animations/Neb_L1toG3_M.nif', 'Neb_L1toG3_M', 'pCharacter.SetHidden(1)' ],
		'NebL1L':	[ 'data/animations/Neb_L1toG3_L.nif', 'Neb_L1toG3_L', 'pCharacter.SetHidden(1)' ],
		'NebL2M':	[ 'data/animations/Neb_L2toG2_M.nif', 'Neb_L2toG2_M', 'pCharacter.SetHidden(1)' ],
		'NebG1M':	[ 'data/animations/Neb_G1toL2_M.nif', 'Neb_G1toL2_M' ],
		'NebG2M':	[ 'data/animations/Neb_G2toL2_M.nif', 'Neb_G2toL2_M' ],
		'NebG3M':	[ 'data/animations/Neb_G3toL1_M.nif', 'Neb_G3toL1_M' ],
	},
	'Maps':{
		'CurrentMaps': {"Light": "Light"},
		'GreenMaps':{'Light': 'data/Models/Sets/nebulabridgev3/High/Light.tga'},
		'YellowMaps':{'Light': 'data/Models/Sets/nebulabridgev3/High/Light_yellow.tga'},
		'RedMaps':{'Light': 'data/Models/Sets/nebulabridgev3/High/Light_red.tga'},
	},
	"bridgeSound":	{"LiftDoor": {"volume": 1.0,"file": "sfx/Nebula/door.wav", "group": "BridgeGeneric"},
			"AmbBridge": {"volume": 0.1,"file": "sfx/Nebula/ambience.wav", "group": "BridgeGeneric"},
			"RedAlertSound": {"volume": 1.0,"file": "sfx/Nebula/klaxton.wav", "group": "BridgeGeneric"},
			"GreenAlertSound": {"volume": 1.0,"file": "sfx/Nebula/green.wav", "group": "BridgeGeneric"},
			"ViewOn": {"volume": 1.0,"file": "sfx/Nebula/hail.wav", "group": "BridgeGeneric"},
			"ViewOff": {"volume": 1.0,"file": "sfx/Nebula/hail.wav", "group": "BridgeGeneric"}
	},
	"LoadingScreen": "data/Icons/LoadingScreens/NebulaLoading.tga",
} )


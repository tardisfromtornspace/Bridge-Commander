import Foundation

# Uncomment the below to enable!
Foundation.BridgeDef('Excalibur', 'ExcaliburBridge', dict = {
	'modes': [ Foundation.MutatorDef.Stock ],
	'locations': {
		'ExcHelm':	[ 'data/animations/Exc_stand_h_m.nif', 'Exc_stand_h_m' ],
		'ExcTactical':	[ 'data/animations/Exc_stand_t_l.nif', 'Exc_stand_t_l' ],
		'ExcCommander':	[ 'data/animations/Exc_stand_c_m.nif', 'Exc_stand_c_m' ],
		'ExcScience':	[ 'data/animations/Exc_stand_S_S.nif', 'Exc_stand_s_s' ],
		'ExcEngineer':	[ 'data/animations/Exc_stand_e_s.nif', 'Exc_stand_e_s' ],
		'ExcGuest':	[ 'data/animations/Exc_stand_X_m.nif', 'Exc_stand_X_m' ],
		'ExcL1S':	[ 'data/animations/Exc_L1toG3_S.nif', 'Exc_L1toG3_s', 'pCharacter.SetHidden(1)' ],
		'ExcL1M':	[ 'data/animations/Exc_L1toG3_M.nif', 'Exc_L1toG3_M', 'pCharacter.SetHidden(1)' ],
		'ExcL1L':	[ 'data/animations/Exc_L1toG3_L.nif', 'Exc_L1toG3_L', 'pCharacter.SetHidden(1)' ],
		'ExcL2M':	[ 'data/animations/Exc_L2toG2_M.nif', 'Exc_L2toG2_M', 'pCharacter.SetHidden(1)' ],
		'ExcG1M':	[ 'data/animations/Exc_G1toL2_M.nif', 'Exc_G1toL2_M' ],
		'ExcG2M':	[ 'data/animations/Exc_G2toL2_M.nif', 'Exc_G2toL2_M' ],
		'ExcG3M':	[ 'data/animations/Exc_G3toL1_M.nif', 'Exc_G3toL1_M' ],
	},
	'Maps':{
		'CurrentMaps': {"sidecolumn": "sidecolumn"},
		'GreenMaps':{'sidecolumn': 'data/Models/Sets/ExcaliburBridge/High/sidecolumn.tga'},
		'YellowMaps':{'sidecolumn': 'data/Models/Sets/ExcaliburBridge/High/sidecolumn_r.tga'},
		'RedMaps':{'sidecolumn': 'data/Models/Sets/ExcaliburBridge/High/sidecolumn_r.tga'},
	},
	"bridgeSound": {
			"LiftDoor": {"volume": 1.0,"file": "sfx/exc/door.wav", "group": "BridgeGeneric"},
			"AmbBridge": {"volume": 1.0,"file": "sfx/exc/amb.wav", "group": "BridgeGeneric"},
			"RedAlertSound": {"volume": 1.0,"file": "sfx/exc/redalert.wav", "group": "BridgeGeneric"},
			"YellowAlertSound": {"volume": 1.0,"file": "sfx/exc/yellowalert.wav", "group": "BridgeGeneric"},
			"GreenAlertSound": {"volume": 1.0,"file": "sfx/exc/greenalert.wav", "group": "BridgeGeneric"},
			"ViewOn": {"volume": 1.0,"file": "sfx/exc/viewscreenon.wav", "group": "BridgeGeneric"},
			"ViewOff": {"volume": 1.0,"file": "sfx/exc/viewscreenoff.wav", "group": "BridgeGeneric"}},
	"LoadingScreen": "data/Icons/LoadingScreens/EXCLoading.tga",
} )

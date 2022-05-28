import Foundation

# Uncomment the below to enable!
Foundation.BridgeDef('Enterprise B', 'EnterpriseBbridge', dict = {
	'modes': [ Foundation.MutatorDef.Stock ],
	'locations': {
		'ENBHelm':	[ 'data/animations/ENB_stand_h_m.nif', 'ENB_stand_h_m' ],
		'ENBTactical':	[ 'data/animations/ENB_stand_t_l.nif', 'ENB_stand_t_l' ],
		'ENBCommander':	[ 'data/animations/ENB_stand_c_m.nif', 'ENB_stand_c_m' ],
		'ENBScience':	[ 'data/animations/ENB_stand_S_S.nif', 'ENB_stand_s_s' ],
		'ENBEngineer':	[ 'data/animations/ENB_stand_e_s.nif', 'ENB_stand_e_s' ],
		'ENBGuest':	[ 'data/animations/ENB_stand_X_m.nif', 'ENB_stand_X_m' ],
		'ENBL1S':	[ 'data/animations/ENB_L1toG3_S.nif', 'ENB_L1toG3_S', 'pCharacter.SetHidden(1)' ],
		'ENBL1M':	[ 'data/animations/ENB_L1toG3_M.nif', 'ENB_L1toG3_M', 'pCharacter.SetHidden(1)' ],
		'ENBL1L':	[ 'data/animations/ENB_L1toG3_L.nif', 'ENB_L1toG3_L', 'pCharacter.SetHidden(1)' ],
		'ENBL2M':	[ 'data/animations/ENB_L2toG2_M.nif', 'ENB_L2toG2_M', 'pCharacter.SetHidden(0)' ],
		'ENBL3M':	[ 'data/animations/ENB_L2toG1_M.nif', 'ENB_L2toG1_M', 'pCharacter.SetHidden(0)' ],
		'ENBG1M':	[ 'data/animations/ENB_G2toL2_M.nif', 'ENB_G2toL2_M' ],
		'ENBG2M':	[ 'data/animations/ENB_G2toL2_M.nif', 'ENB_G2toL2_M' ],
		'ENBG3M':	[ 'data/animations/ENB_G3toL1_M.nif', 'ENB_G3toL1_M' ],
	},
	"LoadingScreen": "data/Icons/LoadingScreens/TMPLoading.tga",
	"bridgeSound": {
			"LiftDoor": {"volume": 0.8,"file": "sfx/EnterpriseB/TMP-door.wav", "group": "BridgeGeneric"},
			"AmbBridge": {"volume": 0.3,"file": "sfx/EnterpriseB/TMP-ambient.wav", "group": "BridgeGeneric"},
			"RedAlertSound": {"volume": 1.0,"file": "sfx/EnterpriseB/TMP-redalert.wav", "group": "BridgeGeneric"},
			"YellowAlertSound": {"volume": 1.0,"file": "sfx/EnterpriseB/TMP-yellowalert.wav", "group": "BridgeGeneric"},
			"ViewOn": {"volume": 1.0,"file": "sfx/EnterpriseB/TMP-hail.wav", "group": "BridgeGeneric"},
			"ViewOff": {"volume": 1.0,"file": "sfx/EnterpriseB/TMP-hail.wav", "group": "BridgeGeneric"}},
} )
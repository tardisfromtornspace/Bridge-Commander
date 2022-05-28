import Foundation

# Uncomment the below to enable!
Foundation.BridgeDef('Defiant', 'defiantbridge', dict = {
	'modes': [ Foundation.MutatorDef.Stock ],
	'locations': {
		'DFHelm':	[ 'data/animations/DF_stand_h_m.nif', 'DF_stand_h_m' ],
		'DFTactical':	[ 'data/animations/DF_stand_t_l.nif', 'DF_stand_t_l' ],
		'DFCommander':	[ 'data/animations/DF_stand_c_m.nif', 'DF_stand_c_m' ],
		'DFScience':	[ 'data/animations/DF_stand_S_S.nif', 'DF_stand_s_s' ],
		'DFEngineer':	[ 'data/animations/DF_stand_e_s.nif', 'DF_stand_e_s' ],
		'DFGuest':	[ 'data/animations/DF_stand_X_m.nif', 'DF_stand_X_m' ],
		'DFL1S':	[ 'data/animations/DF_L1toG3_S.nif', 'DF_L1toG3_s', 'pCharacter.SetHidden(1)' ],
		'DFL1M':	[ 'data/animations/DF_L1toG3_M.nif', 'DF_L1toG3_M', 'pCharacter.SetHidden(1)' ],
		'DFL1L':	[ 'data/animations/DF_L1toG3_L.nif', 'DF_L1toG3_L', 'pCharacter.SetHidden(1)' ],
		'DFL2M':	[ 'data/animations/DF_L2toG2_M.nif', 'DF_L2toG2_M', 'pCharacter.SetHidden(1)' ],
		'DFG1M':	[ 'data/animations/DF_G1toL2_M.nif', 'DF_G1toL2_M' ],
		'DFG2M':	[ 'data/animations/DF_G2toL2_M.nif', 'DF_G2toL2_M' ],
		'DFG3M':	[ 'data/animations/DF_G3toL1_M.nif', 'DF_G3toL1_M' ],
	},
	'Maps':{
		'CurrentMaps': {"sidelights": "sidelights"},
		'GreenMaps':{'lightone': 'data/Models/Sets/defiantbridge/High/sidelights.tga'},
		'YellowMaps':{'lightone': 'data/Models/Sets/defiantbridge/High/sidelights_red.tga'},
		'RedMaps':{'lightone': 'data/Models/Sets/defiantbridge/High/sidelights_red.tga'},
},
	"bridgeSound": {
			"LiftDoor": {"volume": 0.6,"file": "sfx/defiant/door.wav", "group": "BridgeGeneric"},
			"AmbBridge": {"volume": 0.6,"file": "sfx/defiant/ambience.wav", "group": "BridgeGeneric"},
			"RedAlertSound": {"volume": 1.0,"file": "sfx/defiant/red.wav", "group": "BridgeGeneric"},
			"YellowAlertSound": {"volume": 1.0,"file": "sfx/defiant/yellow.wav", "group": "BridgeGeneric"},
			"GreenAlertSound": {"volume": 0.0,"file": "sfx/defiant/green.wav", "group": "BridgeGeneric"},
			"ViewOn": {"volume": 1.0,"file": "sfx/defiant/hail.wav", "group": "BridgeGeneric"},
			"ViewOff": {"volume": 1.0,"file": "sfx/defiant/hail.wav", "group": "BridgeGeneric"}
},
	"LoadingScreen": "data/Icons/LoadingScreens/DefiantLoading.tga",
} )
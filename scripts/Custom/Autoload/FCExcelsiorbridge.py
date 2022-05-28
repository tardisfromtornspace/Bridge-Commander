import Foundation

# Uncomment the below to enable!
Foundation.BridgeDef('Excelsior Refit', 'FCExcelsiorbridge', dict = {
	'modes': [ Foundation.MutatorDef.Stock ],
	'locations': {
		'EXLHelm':	[ 'data/animations/EXL_stand_h_m.nif', 'EXL_stand_h_m' ],
		'EXLTactical':	[ 'data/animations/EXL_stand_t_l.nif', 'EXL_stand_t_l' ],
		'EXLCommander':	[ 'data/animations/EXL_stand_c_m.nif', 'EXL_stand_c_m' ],
		'EXLScience':	[ 'data/animations/EXL_stand_S_S.nif', 'EXL_stand_s_s' ],
		'EXLEngineer':	[ 'data/animations/EXL_stand_e_s.nif', 'EXL_stand_e_s' ],
		'EXLGuest':	[ 'data/animations/EXL_stand_X_m.nif', 'EXL_stand_X_m' ],
		'EXLL1S':	[ 'data/animations/EXL_L1toG3_S.nif', 'EXL_L1toG3_S', 'pCharacter.SetHidden(1)' ],
		'EXLL1M':	[ 'data/animations/EXL_L1toG3_M.nif', 'EXL_L1toG3_M', 'pCharacter.SetHidden(1)' ],
		'EXLL1L':	[ 'data/animations/EXL_L1toG3_L.nif', 'EXL_L1toG3_L', 'pCharacter.SetHidden(1)' ],
		'EXLL2M':	[ 'data/animations/EXL_L2toG2_M.nif', 'EXL_L2toG2_M', 'pCharacter.SetHidden(1)' ],
		'EXLG1M':	[ 'data/animations/EXL_G1toL2_M.nif', 'EXL_G1toL2_M' ],
		'EXLG2M':	[ 'data/animations/EXL_G2toL2_M.nif', 'EXL_G2toL2_M' ],
		'EXLG3M':	[ 'data/animations/EXL_G3toL1_M.nif', 'EXL_G3toL1_M' ],
	},
	'Maps':{
		'CurrentMaps': {"spotlights": "spotlights"},
		'GreenMaps':{'spotlights': 'data/Models/Sets/FCExcelsiorBridge/High/spotlights.tga'},
		'YellowMaps':{'spotlights': 'data/Models/Sets/FCExcelsiorBridge/High/spotlights_yellow.tga'},
		'RedMaps':{'spotlights': 'data/Models/Sets/FCExcelsiorBridge/High/spotlights_red.tga'},
},
    'bridgeSound': 	{			"LiftDoor": {"volume": 1.0,"file": "sfx/ebridge/ebdoor.wav", "group": "BridgeGeneric"},
			"AmbBridge": {"volume": 0.1,"file": "sfx/ebridge/ebamb.wav", "group": "BridgeGeneric"},
			"RedAlertSound": {"volume": 1.0,"file": "sfx/ebridge/ebklaxton.wav", "group": "BridgeGeneric"},
			"YellowAlertSound": {"volume": 1.0,"file": "sfx/ebridge/ebyellow.wav", "group": "BridgeGeneric"},
			"GreenAlertSound": {"volume": 1.0,"file": "sfx/ebridge/ebgreen.wav", "group": "BridgeGeneric"},
			"ViewOn": {"volume": 1.0,"file": "sfx/ebridge/ebviewscreenon.wav", "group": "BridgeGeneric"},
			"ViewOff": {"volume": 1.0,"file": "sfx/ebridge/ebviewscreenoff.wav", "group": "BridgeGeneric"}}
#	"LoadingScreen": "data/Icons/LoadingScreens/IntrepidLoading.tga",
} )

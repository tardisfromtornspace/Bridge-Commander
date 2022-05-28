import Foundation

# Uncomment the below to enable!
Foundation.BridgeDef('Prometheus', 'prometheusbridge', dict = {
	'modes': [ Foundation.MutatorDef.Stock ],
	'locations': {
		'promHelm':	[ 'data/animations/prom_stand_h_m.nif', 'prom_stand_h_m' ],
		'promTactical':	[ 'data/animations/prom_stand_t_l.nif', 'prom_stand_t_l' ],
		'promCommander':[ 'data/animations/prom_stand_c_m.nif', 'prom_stand_c_m' ],
		'promScience':	[ 'data/animations/prom_stand_S_S.nif', 'prom_stand_s_s' ],
		'promEngineer':	[ 'data/animations/prom_stand_e_s.nif', 'prom_stand_e_s' ],
		'promGuest':	[ 'data/animations/prom_stand_X_m.nif', 'prom_stand_X_m' ],
		'promL1S':	[ 'data/animations/prom_L1toG3_S.nif', 'prom_L1toG3_s', 'pCharacter.SetHidden(1)' ],
		'promL1M':	[ 'data/animations/prom_L1toG3_M.nif', 'prom_L1toG3_M', 'pCharacter.SetHidden(1)' ],
		'promL1L':	[ 'data/animations/prom_L1toG3_L.nif', 'prom_L1toG3_L', 'pCharacter.SetHidden(1)' ],
		'promL2M':	[ 'data/animations/prom_L2toG1_M.nif', 'prom_L2toG1_M', 'pCharacter.SetHidden(1)' ],
		'promL3M':	[ 'data/animations/prom_L2toG2_M.nif', 'prom_L3toG1_M', 'pCharacter.SetHidden(1)' ],
		'promG1M':	[ 'data/animations/prom_G1toL2_M.nif', 'prom_G1toL2_M' ],
		'promG2M':	[ 'data/animations/prom_G2toL2_M.nif', 'prom_G2toL2_M' ],
		'promG3M':	[ 'data/animations/prom_G3toL1_M.nif', 'prom_G3toL1_M' ],
	},
'Maps':{
		'CurrentMaps': {"beams": "beams", "dome" : "dome"},
		'GreenMaps':{'beams': 'data/Models/Sets/prometheusbridge/High/beams.tga',
			     'dome': 'data/Models/Sets/prometheusbridge/High/dome.tga'},
		'YellowMaps':{'beams': 'data/Models/Sets/prometheusbridge/High/beams_yell.tga',
			     'dome': 'data/Models/Sets/prometheusbridge/High/dome_yell.tga'},
		'RedMaps':{'beams': 'data/Models/Sets/prometheusbridge/High/beams_red.tga',
			     'dome': 'data/Models/Sets/prometheusbridge/High/dome_red.tga'},
		"MVAMMaps": {'beams': 'data/Models/Sets/prometheusbridge/High/beams_blue.tga',
			     'dome': 'data/Models/Sets/prometheusbridge/High/dome_blue.tga'},
	},

	"bridgeSound":	{"LiftDoor": {"volume": 1.0,"file": "sfx/Prometheus/door.wav", "group": "BridgeGeneric"},
			"AmbBridge": {"volume": 0.1,"file": "sfx/Prometheus/amb.wav", "group": "BridgeGeneric"},
			"RedAlertSound": {"volume": 1.0,"file": "sfx/Prometheus/klaxton.wav", "group": "BridgeGeneric"},
			"GreenAlertSound": {"volume": 1.0,"file": "sfx/Prometheus/green.wav", "group": "BridgeGeneric"},
			"ViewOn": {"volume": 1.0,"file": "sfx/Prometheus/viewscreenon.wav", "group": "BridgeGeneric"},
			"ViewOff": {"volume": 1.0,"file": "sfx/Prometheus/viewscreenoff.wav", "group": "BridgeGeneric"}
	},
	"LoadingScreen": "data/Icons/LoadingScreens/PrometheusLoading.tga",
})
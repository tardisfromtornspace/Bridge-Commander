import Foundation
import StaticDefs

Foundation.BridgeDef('Delta Flyer', 'DFBridge', dict = {'modes': [ Foundation.MutatorDef.Stock ],
	'locations': {
		'FlyHelm':[ 'data/animations/Fly_stand_h_m.nif', 'Fly_stand_h_m' ],
		'FlyTactical':[ 'data/animations/Fly_stand_t_l.nif', 'Fly_stand_t_l' ],
		'FlyScience':[ 'data/animations/FlyOff_stand_S_S.nif', 'FlyOff_stand_s_s' ],
		'FlyEngineer':[ 'data/animations/Fly_stand_e_s.nif', 'Fly_stand_e_s' ],
		'FlyCommander':[ 'data/animations/FlyOff_stand_C_M.nif', 'FlyOff_stand_C_M' ],
	},
	'Maps':{
		'CurrentMaps': {"sideredalert" : "sideredalert"},
		'GreenMaps':{'sideredalert': 'data/Models/Sets/DFBridge/sideredalert.tga'},
		'RedMaps':{'sideredalert': [1, {1: 'data/Models/Sets/DFBridge/sideredalertRED.tga', 2: 'data/Models/Sets/DFBridge/sideredalert.tga',}]},
	},
	"bridgeSound": {
			"AmbBridge": {"volume": 0.5,"file": "sfx/Shuttles/amb.wav", "group": "BridgeGeneric"},
			"RedAlertSound": {"volume": 1.0,"file": "sfx/Shuttles/red.wav", "group": "BridgeGeneric"},
			"YellowAlertSound": {"volume": 1.0,"file": "sfx/Shuttles/green.wav", "group": "BridgeGeneric"},
	}
} )

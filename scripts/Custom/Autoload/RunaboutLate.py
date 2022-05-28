import Foundation
import StaticDefs

Foundation.BridgeDef('Runabout Late', 'RunaboutLate', dict = {'modes': [ Foundation.MutatorDef.Stock ],
	'locations': {
		'RunHelm':[ 'data/animations/Run_stand_h_m.nif', 'Run_stand_h_m' ],
		'RunTactical':[ 'data/animations/Run_stand_t_l.nif', 'Run_stand_t_l' ],
		'RunScience':[ 'data/animations/Run_stand_S_S.nif', 'Run_stand_s_s' ],
		'RunEngineer':[ 'data/animations/Run_stand_e_s.nif', 'Run_stand_e_s' ],
		'RunCommander':[ 'data/animations/Run_stand_C_M.nif', 'Run_stand_C_M' ],
	},
	'Maps':{
		'CurrentMaps': {"frontcontop": "frontcontop", "cabinlights-lm" : "cabinlights-lm", "bkwalllight-lm" : "bkwalllight-lm" },
		'GreenMaps':{'frontcontop': 'data/Models/Sets/RunaboutLate/frontcontop.tga',
			     'cabinlights-lm': 'data/Models/Sets/RunaboutLate/cabinlights-lm.tga',
			     'bkwalllight-lm': 'data/Models/Sets/RunaboutLate/bkwalllight-lm.tga'},

		'YellowMaps':{'frontcontop': 'data/Models/Sets/RunaboutLate/frontcontop.tga',
			     'cabinlights-lm': 'data/Models/Sets/RunaboutLate/cabinlights-lm.tga',
			     'bkwalllight-lm': 'data/Models/Sets/RunaboutLate/bkwalllight-lm.tga'},

		'RedMaps':{'frontcontop': 'data/Models/Sets/RunaboutLate/frontcontopRED.tga',
			   'cabinlights-lm': [1, {1: 'data/Models/Sets/RunaboutLate/cabinlights-lmR.tga', 2: 'data/Models/Sets/RunaboutLate/cabinlights-lmR2.tga'}],
			   'bkwalllight-lm': [1, {1: 'data/Models/Sets/RunaboutLate/bkwalllight-lmR.tga', 2: 'data/Models/Sets/RunaboutLate/bkwalllight-lm.tga',}]},
	},
	"bridgeSound": {
			"AmbBridge": {"volume": 0.5,"file": "sfx/Shuttles/amb.wav", "group": "BridgeGeneric"},
			"RedAlertSound": {"volume": 1.0,"file": "sfx/Shuttles/red.wav", "group": "BridgeGeneric"},
			"YellowAlertSound": {"volume": 1.0,"file": "sfx/Shuttles/green.wav", "group": "BridgeGeneric"},
	}
} )

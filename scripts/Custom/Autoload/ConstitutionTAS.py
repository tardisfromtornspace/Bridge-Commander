import Foundation

# Uncomment the below to enable!
Foundation.BridgeDef('Constitution TAS', 'ConstitutionTASbridge', dict = {
	'modes': [ Foundation.MutatorDef.Stock ],
	'locations': {
		'TOSHelm':	[ 'data/animations/TOS_seated_h_m.nif', 'TOS_seated_h_m' ],
		'TOSTactical':	[ 'data/animations/TOS_seated_t_l.nif', 'TOS_seated_t_l' ],
		'TOSCommander':	[ 'data/animations/TOS_seated_c_m.nif', 'TOS_seated_c_m' ],
		'TOSScience':	[ 'data/animations/TOS_seated_S_S.nif', 'TOS_seated_s_s' ],
		'TOSEngineer':	[ 'data/animations/TOS_seated_e_s.nif', 'TOS_seated_e_s' ],
		'TOSGuest':	[ 'data/animations/TOS_seated_X_m.nif', 'TOS_seated_X_m' ],
		'TOSL1S':	[ 'data/animations/TOS_L1toG3_S.nif', 'TOS_L1toG3_s', 'pCharacter.SetHidden(1)' ],
		'TOSL1L':	[ 'data/animations/TOS_L1toG3_L.nif', 'TOS_L1toG3_L', 'pCharacter.SetHidden(1)' ],
		'TOSL2M':	[ 'data/animations/TOS_L2toG2_M.nif', 'TOS_L2toG2_M', 'pCharacter.SetHidden(1)' ],
		'TOSL1M':	[ 'data/animations/TOS_seated_extra01.nif', 'TOS_seated_extra01', 'pCharacter.SetHidden(0)' ],
		'TOSL3M':	[ 'data/animations/TOS_seated_extra02.nif', 'TOS_seated_extra02', 'pCharacter.SetHidden(0)' ],
		'TOSL4M':	[ 'data/animations/TOS_seated_extra03.nif', 'TOS_seated_extra03', 'pCharacter.SetHidden(0)' ],
		'TOSG1M':	[ 'data/animations/TOS_G1toL2_M.nif', 'TOS_G1toL2_M' ],
		'TOSG2M':	[ 'data/animations/TOS_G2toL2_M.nif', 'TOS_G2toL2_M' ],
		'TOSG3M':	[ 'data/animations/TOS_G3toL1_M.nif', 'TOS_G3toL1_M' ]
	},
	'NumExtras':	4,
	"bridgeSound": {
			"LiftDoor": {"volume": 1.0,"file": "sfx/TOS/tosdoor.wav", "group": "BridgeGeneric"},
			"AmbBridge": {"volume": 0.3,"file": "sfx/TOS/tosbridge.wav", "group": "BridgeGeneric"},
			"RedAlertSound": {"volume": 1.0,"file": "sfx/TOS/animklax.wav", "group": "BridgeGeneric"},
			"ViewOn": {"volume": 1.0,"file": "sfx/TOS/toshail.wav", "group": "BridgeGeneric"},
			"ViewOff": {"volume": 1.0,"file": "sfx/TOS/toshail.wav", "group": "BridgeGeneric"}},
    	'Maps':{
		'CurrentMaps': {'def_alarm1': "def_alarm1",'red_alert1': "red_alert1"},
		'GreenMaps':{'def_alarm1': 'data/Models/Sets/Constitution/def_alarm1.tga','red_alert1': 'data/Models/Sets/Constitution/red_alert1.tga'},
		'YellowMaps':{'def_alarm1': 'data/Models/Sets/Constitution/def_alarm1YELLOW.tga','red_alert1': 'data/Models/Sets/Constitution/red_alert1.tga'},
		'RedMaps':{'def_alarm1': 'data/Models/Sets/Constitution/def_alarm1RED.tga','red_alert1': 'data/Models/Sets/Constitution/red_alert3.tga'},
		'NormalMaps':{'def_alarm1': 'data/Models/Sets/Constitution/def_alarm1.tga','red_alert1': 'data/Models/Sets/Constitution/red_alert1.tga'}
		},
	"LoadingScreen": "data/Icons/LoadingScreens/ConstitutionLoading.tga",
} )

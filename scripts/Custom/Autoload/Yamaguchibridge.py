import Foundation

# Uncomment the below to enable!
Foundation.BridgeDef('Ambassador', 'YamaguchiBridge', dict = {
	'modes': [ Foundation.MutatorDef.Stock ],
	'locations': {
		'AmbHelm':	[ 'data/animations/Amb_stand_h_m.nif', 'Amb_stand_h_m' ],
		'AmbTactical':	[ 'data/animations/Amb_stand_t_l.nif', 'Amb_stand_t_l' ],
		'AmbCommander':	[ 'data/animations/AmbTNG_seated_C_M.nif', 'AmbTNG_seated_c_m' ],
		'AmbScience':	[ 'data/animations/Amb_stand_S_S.nif', 'Amb_stand_s_s' ],
		'AmbEngineer':	[ 'data/animations/Amb_stand_e_s.nif', 'Amb_stand_e_s' ],
		'AmbGuest':	[ 'data/animations/Amb_stand_X_m.nif', 'Amb_stand_X_m' ],
		'AmbL1S':	[ 'data/animations/Amb_L1toG3_S.nif', 'Amb_L1toG3_s', 'pCharacter.SetHidden(1)' ],
		'AmbL1M':	[ 'data/animations/Amb_L1toG3_M.nif', 'Amb_L1toG3_M', 'pCharacter.SetHidden(1)' ],
		'AmbL1L':	[ 'data/animations/Amb_L1toG3_L.nif', 'Amb_L1toG3_L', 'pCharacter.SetHidden(1)' ],
		'AmbL2M':	[ 'data/animations/Amb_L2toG2_M.nif', 'Amb_L2toG2_M', 'pCharacter.SetHidden(1)' ],
		'AmbG1M':	[ 'data/animations/Amb_G1toL2_M.nif', 'Amb_G1toL2_M' ],
		'AmbG2M':	[ 'data/animations/Amb_G2toL2_M.nif', 'Amb_G2toL2_M' ],
		'AmbG3M':	[ 'data/animations/Amb_G3toL1_M.nif', 'Amb_G3toL1_M' ],
	},
"Maps":{
        "ShieldMaps":{
            "Front":{
                100:{"fshield_100":"Data/Models/Sets/AmbassadorBridge/High/fshield_100.tga"},
                 80:{"fshield_100":"Data/Models/Sets/AmbassadorBridge/High/fshield_80.tga"}, 
                 60:{"fshield_100":"Data/Models/Sets/AmbassadorBridge/High/fshield_60.tga"}, 
                 40:{"fshield_100":"Data/Models/Sets/AmbassadorBridge/High/fshield_40.tga"}, 
                 20:{"fshield_100":"Data/Models/Sets/AmbassadorBridge/High/fshield_20.tga"}, 
                  0:{"fshield_100": "Data/Models/Sets/AmbassadorBridge/High/fshield_00.tga"}
            },

            "Rear":{
                100:{"ashield_100":"Data/Models/Sets/AmbassadorBridge/High/ashield_100.tga"},
                 80:{"ashield_100":"Data/Models/Sets/AmbassadorBridge/High/ashield_80.tga"}, 
                 60:{"ashield_100":"Data/Models/Sets/AmbassadorBridge/High/ashield_60.tga"}, 
                 40:{"ashield_100":"Data/Models/Sets/AmbassadorBridge/High/ashield_40.tga"}, 
                 20:{"ashield_100":"Data/Models/Sets/AmbassadorBridge/High/ashield_20.tga"}, 
                  0:{"ashield_100": "Data/Models/Sets/AmbassadorBridge/High/ashield_00.tga"}
            },

            "Left":{
                100:{"lshield_100":"Data/Models/Sets/AmbassadorBridge/High/lshield_100.tga"},
                 80:{"lshield_100":"Data/Models/Sets/AmbassadorBridge/High/lshield_80.tga"}, 
                 60:{"lshield_100":"Data/Models/Sets/AmbassadorBridge/High/lshield_60.tga"}, 
                 40:{"lshield_100":"Data/Models/Sets/AmbassadorBridge/High/lshield_40.tga"}, 
                 20:{"lshield_100":"Data/Models/Sets/AmbassadorBridge/High/lshield_20.tga"}, 
                  0:{"lshield_100": "Data/Models/Sets/AmbassadorBridge/High/lshield_00.tga"}
            },

            "Right":{
                100:{"rshield_100":"Data/Models/Sets/AmbassadorBridge/High/rshield_100.tga"},
                 80:{"rshield_100":"Data/Models/Sets/AmbassadorBridge/High/rshield_80.tga"}, 
                 60:{"rshield_100":"Data/Models/Sets/AmbassadorBridge/High/rshield_60.tga"}, 
                 40:{"rshield_100":"Data/Models/Sets/AmbassadorBridge/High/rshield_40.tga"}, 
                 20:{"rshield_100":"Data/Models/Sets/AmbassadorBridge/High/rshield_20.tga"}, 
                  0:{"rshield_100": "Data/Models/Sets/AmbassadorBridge/High/rshield_00.tga"}
            },

            "Top":{
                100:{"uprshield_100":"Data/Models/Sets/AmbassadorBridge/High/uprshield_100.tga"},
                 80:{"uprshield_100":"Data/Models/Sets/AmbassadorBridge/High/uprshield_80.tga"}, 
                 60:{"uprshield_100":"Data/Models/Sets/AmbassadorBridge/High/uprshield_60.tga"}, 
                 40:{"uprshield_100":"Data/Models/Sets/AmbassadorBridge/High/uprshield_40.tga"}, 
                 20:{"uprshield_100":"Data/Models/Sets/AmbassadorBridge/High/uprshield_20.tga"}, 
                  0:{"uprshield_100": "Data/Models/Sets/AmbassadorBridge/High/uprshield_00.tga"}
            },

            "Bottom":{
                100:{"lwrshield_100":"Data/Models/Sets/AmbassadorBridge/High/lwrshield_100.tga"},
                 80:{"lwrshield_100":"Data/Models/Sets/AmbassadorBridge/High/lwrshield_80.tga"}, 
                 60:{"lwrshield_100":"Data/Models/Sets/AmbassadorBridge/High/lwrshield_60.tga"}, 
                 40:{"lwrshield_100":"Data/Models/Sets/AmbassadorBridge/High/lwrshield_40.tga"}, 
                 20:{"lwrshield_100":"Data/Models/Sets/AmbassadorBridge/High/lwrshield_20.tga"}, 
                  0:{"lwrshield_100": "Data/Models/Sets/AmbassadorBridge/High/lwrshield_00.tga"}},
        },
        "HullMaps":{
                100:{"hull_100":"Data/Models/Sets/AmbassadorBridge/High/hull_100.tga"},
                 80:{"hull_100":"Data/Models/Sets/AmbassadorBridge/High/hull_80.tga"}, 
                 60:{"hull_100":"Data/Models/Sets/AmbassadorBridge/High/hull_60.tga"}, 
                 40:{"hull_100":"Data/Models/Sets/AmbassadorBridge/High/hull_40.tga"}, 
                 20:{"hull_100":"Data/Models/Sets/AmbassadorBridge/High/hull_20.tga"}, 
                  0:{"hull_100":"Data/Models/Sets/AmbassadorBridge/High/hull_00.tga"}
        },
	'CurrentMaps': {'Map 4': "Map 4"},
	'GreenMaps':{'Map 4': 'data/Models/Sets/AmbassadorBridge/High/Map 4.tga'},
	'YellowMaps':{'Map 4': 'data/Models/Sets/AmbassadorBridge/High/Map 4.tga'},
	'RedMaps':{'Map 4': 'data/Models/Sets/AmbassadorBridge/High/Map 4_r.tga'},
		},
	"bridgeSound": {
			"LiftDoor": {"volume": 1.0,"file": "sfx/TNGAmbassador/tngdoor.wav", "group": "BridgeGeneric"},
			"AmbBridge": {"volume": 0.3,"file": "sfx/TNGAmbassador/ambienceTNG.wav", "group": "BridgeGeneric"},
			"RedAlertSound": {"volume": 1.0,"file": "sfx/TNGAmbassador/RedAlert.wav", "group": "BridgeGeneric"},
			"YellowAlertSound": {"volume": 1.0,"file": "sfx/TNGAmbassador/TNGYellow.wav", "group": "BridgeGeneric"},
			"GreenAlertSound": {"volume": 1.0,"file": "sfx/TNGAmbassador/TNGGreen.wav", "group": "BridgeGeneric"},
			"ViewOn": {"volume": 1.0,"file": "sfx/TNGAmbassador/commopenTNG.wav", "group": "BridgeGeneric"},
			"ViewOff": {"volume": 1.0,"file": "sfx/TNGAmbassador/commcloseTNG.wav", "group": "BridgeGeneric"}},
	"LoadingScreen": "data/Icons/LoadingScreens/AmbLoading.tga",
} )
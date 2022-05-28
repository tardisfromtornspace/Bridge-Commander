import Foundation

# Uncomment the below to enable!
Foundation.BridgeDef('TMP Miranda', 'TNGmirandaBridge', dict = {
	'modes': [ Foundation.MutatorDef.Stock ],
	'locations': {
		'ENAHelm':	[ 'data/animations/ENA_stand_h_m.nif', 'ENA_stand_h_m' ],
		'ENATactical':	[ 'data/animations/ENA_stand_t_l.nif', 'ENA_stand_t_l' ],
		'ENACommander':	[ 'data/animations/ENA_stand_c_m.nif', 'ENA_stand_c_m' ],
		'ENAScience':	[ 'data/animations/ENA_stand_S_S.nif', 'ENA_stand_s_s' ],
		'ENAEngineer':	[ 'data/animations/ENA_stand_e_s.nif', 'ENA_stand_e_s' ],
		'ENAGuest':	[ 'data/animations/ENA_stand_X_m.nif', 'ENA_stand_X_m' ],
		'ENAL1S':	[ 'data/animations/ENA_L1toG3_S.nif', 'ENA_L1toG3_S', 'pCharacter.SetHidden(1)' ],
		'ENAL1M':	[ 'data/animations/ENA_L1toG3_M.nif', 'ENA_L1toG3_M', 'pCharacter.SetHidden(1)' ],
		'ENAL1L':	[ 'data/animations/ENA_L1toG3_L.nif', 'ENA_L1toG3_L', 'pCharacter.SetHidden(1)' ],
		'ENAL2M':	[ 'data/animations/ENA_L2toG2_M.nif', 'ENA_L2toG2_M', 'pCharacter.SetHidden(1)' ],
		'ENAG1M':	[ 'data/animations/ENA_G1toL2_M.nif', 'ENA_G1toL2_M' ],
		'ENAG2M':	[ 'data/animations/ENA_G2toL2_M.nif', 'ENA_G2toL2_M' ],
		'ENAG3M':	[ 'data/animations/ENA_G3toL1_M.nif', 'ENA_G3toL1_M' ],
	},
	"Maps":{
        "ShieldMaps":{
            "Front":{
                100:{"fshield_100":"Data/Models/Sets/TNGMirandaBridge/High/fshield_100.tga"},
                 80:{"fshield_100":"Data/Models/Sets/TNGMirandaBridge/High/fshield_80.tga"}, 
                 60:{"fshield_100":"Data/Models/Sets/TNGMirandaBridge/High/fshield_60.tga"}, 
                 40:{"fshield_100":"Data/Models/Sets/TNGMirandaBridge/High/fshield_40.tga"}, 
                 20:{"fshield_100":"Data/Models/Sets/TNGMirandaBridge/High/fshield_20.tga"}, 
                  0:{"fshield_100": "Data/Models/Sets/TNGMirandaBridge/High/fshield_00.tga"}
            },

            "Rear":{
                100:{"ashield_100":"Data/Models/Sets/TNGMirandaBridge/High/ashield_100.tga"},
                 80:{"ashield_100":"Data/Models/Sets/TNGMirandaBridge/High/ashield_80.tga"}, 
                 60:{"ashield_100":"Data/Models/Sets/TNGMirandaBridge/High/ashield_60.tga"}, 
                 40:{"ashield_100":"Data/Models/Sets/TNGMirandaBridge/High/ashield_40.tga"}, 
                 20:{"ashield_100":"Data/Models/Sets/TNGMirandaBridge/High/ashield_20.tga"}, 
                  0:{"ashield_100": "Data/Models/Sets/TNGMirandaBridge/High/ashield_00.tga"}
            },

            "Left":{
                100:{"lshield_100":"Data/Models/Sets/TNGMirandaBridge/High/lshield_100.tga"},
                 80:{"lshield_100":"Data/Models/Sets/TNGMirandaBridge/High/lshield_80.tga"}, 
                 60:{"lshield_100":"Data/Models/Sets/TNGMirandaBridge/High/lshield_60.tga"}, 
                 40:{"lshield_100":"Data/Models/Sets/TNGMirandaBridge/High/lshield_40.tga"}, 
                 20:{"lshield_100":"Data/Models/Sets/TNGMirandaBridge/High/lshield_20.tga"}, 
                  0:{"lshield_100": "Data/Models/Sets/TNGMirandaBridge/High/lshield_00.tga"}
            },

            "Right":{
                100:{"rshield_100":"Data/Models/Sets/TNGMirandaBridge/High/rshield_100.tga"},
                 80:{"rshield_100":"Data/Models/Sets/TNGMirandaBridge/High/rshield_80.tga"}, 
                 60:{"rshield_100":"Data/Models/Sets/TNGMirandaBridge/High/rshield_60.tga"}, 
                 40:{"rshield_100":"Data/Models/Sets/TNGMirandaBridge/High/rshield_40.tga"}, 
                 20:{"rshield_100":"Data/Models/Sets/TNGMirandaBridge/High/rshield_20.tga"}, 
                  0:{"rshield_100": "Data/Models/Sets/TNGMirandaBridge/High/rshield_00.tga"}
            },

            "Top":{
                100:{"uprshield_100":"Data/Models/Sets/TNGMirandaBridge/High/uprshield_100.tga"},
                 80:{"uprshield_100":"Data/Models/Sets/TNGMirandaBridge/High/uprshield_80.tga"}, 
                 60:{"uprshield_100":"Data/Models/Sets/TNGMirandaBridge/High/uprshield_60.tga"}, 
                 40:{"uprshield_100":"Data/Models/Sets/TNGMirandaBridge/High/uprshield_40.tga"}, 
                 20:{"uprshield_100":"Data/Models/Sets/TNGMirandaBridge/High/uprshield_20.tga"}, 
                  0:{"uprshield_100": "Data/Models/Sets/TNGMirandaBridge/High/uprshield_00.tga"}
            },

            "Bottom":{
                100:{"lwrshield_100":"Data/Models/Sets/TNGMirandaBridge/High/lwrshield_100.tga"},
                 80:{"lwrshield_100":"Data/Models/Sets/TNGMirandaBridge/High/lwrshield_80.tga"}, 
                 60:{"lwrshield_100":"Data/Models/Sets/TNGMirandaBridge/High/lwrshield_60.tga"}, 
                 40:{"lwrshield_100":"Data/Models/Sets/TNGMirandaBridge/High/lwrshield_40.tga"}, 
                 20:{"lwrshield_100":"Data/Models/Sets/TNGMirandaBridge/High/lwrshield_20.tga"}, 
                  0:{"lwrshield_100": "Data/Models/Sets/TNGMirandaBridge/High/lwrshield_00.tga"}},
        },
        "HullMaps":{
                100:{"hull_100":"Data/Models/Sets/TNGMirandaBridge/High/hull_100.tga"},
                 80:{"hull_100":"Data/Models/Sets/TNGMirandaBridge/High/hull_80.tga"}, 
                 60:{"hull_100":"Data/Models/Sets/TNGMirandaBridge/High/hull_60.tga"}, 
                 40:{"hull_100":"Data/Models/Sets/TNGMirandaBridge/High/hull_40.tga"}, 
                 20:{"hull_100":"Data/Models/Sets/TNGMirandaBridge/High/hull_20.tga"}, 
                  0:{"hull_100":"Data/Models/Sets/TNGMirandaBridge/High/hull_00.tga"}
        },
	'CurrentMaps': {'front_wall1': "front_wall1", "doorwall" : "doorwall"},
	'GreenMaps':{'front_wall1': 'data/Models/Sets/TNGMirandaBridge/High/front_wall1.tga',
			      'doorwall': 'data/Models/Sets/TNGMirandaBridge/High/doorwall.tga'},
	'YellowMaps':{'front_wall1': 'data/Models/Sets/TNGMirandaBridge/High/front_wall2.tga',
			      'doorwall': 'data/Models/Sets/TNGMirandaBridge/High/doorwall2.tga'},
	'RedMaps':{'front_wall1': 'data/Models/Sets/TNGMirandaBridge/High/front_wall3.tga',
			      'doorwall': 'data/Models/Sets/TNGMirandaBridge/High/doorwall3.tga'},
		},
	"bridgeSound": {
			"LiftDoor": {"volume": 1.0,"file": "sfx/EnterpriseA/TMP-door.wav", "group": "BridgeGeneric"},
			"AmbBridge": {"volume": 0.3,"file": "sfx/EnterpriseA/TMP-ambient.wav", "group": "BridgeGeneric"},
			"RedAlertSound": {"volume": 1.0,"file": "sfx/EnterpriseA/TMP-redalert.wav", "group": "BridgeGeneric"},
			"YellowAlertSound": {"volume": 1.0,"file": "sfx/EnterpriseA/TMP-yellowalert.wav", "group": "BridgeGeneric"},
			"ViewOn": {"volume": 1.0,"file": "sfx/EnterpriseA/TMP-hail.wav", "group": "BridgeGeneric"},
			"ViewOff": {"volume": 1.0,"file": "sfx/EnterpriseA/TMP-hail.wav", "group": "BridgeGeneric"}},
	"LoadingScreen": "data/Icons/LoadingScreens/TMPLoading.tga",
} )


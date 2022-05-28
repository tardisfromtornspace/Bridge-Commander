###################################################################################
#	Galaxy Advanced Scripts                                                   #
#	Compiled by MLeo Daalder and Mark W                                       #
#                                                                                 #
###################################################################################


import Foundation

# Uncomment the below to enable!
Foundation.BridgeDef('Galaxy', 'GalaxyBridge', dict = {
	'modes': [ Foundation.MutatorDef.Stock ],
	'locations': {	},
	'ExtraObjects': {"pBridgeObject2": ["data/Models/Sets/Galaxy/galaxybackwall.nif", "data/Models/Sets/Galaxy/"]},
	'Maps':{
		'CurrentMaps': {'g_imp_pannels-state01': "g_imp_pannels-state01", "Map 13" : "Map 13", "Map 5" : "Map 5"},
		'GreenMaps':{'g_imp_pannels-state01': 'data/Models/Sets/Galaxy/g_imp_pannels-state01.tga',
			      'g_imp_redbars': 'data/Models/Sets/Galaxy/g_imp_redbars_unlit.tga',
			      'Map 5' : 'data/Models/Sets/DBridge/High/Map 5.tga',
			      'Map 13' : 'data/Models/Sets/DBridge/High/Map 13.tga',
			      'Map 27': 'data/Models/Sets/DBridge/High/Map 27.tga'},
		'YellowMaps':{'g_imp_pannels-state01': 'data/Models/Sets/Galaxy/g_imp_pannels-state02.tga',
			      'g_imp_redbars': 'data/Models/Sets/Galaxy/g_imp_redbars_unlit.tga',
			      'Map 5' : 'data/Models/Sets/DBridge/High/Map 5.tga',
			      'Map 13' : 'data/Models/Sets/DBridge/High/Map 13.tga',
			      'Map 27': 'data/Models/Sets/DBridge/High/Map 27.tga'},
		'RedMaps':{'g_imp_pannels-state01': 'data/Models/Sets/Galaxy/g_imp_pannels-state03.tga',
			   'g_imp_redbars': 'data/Models/Sets/Galaxy/g_imp_redbars.tga',
		              'Map 5' : 'data/Models/Sets/DBridge/High/Map 5r.tga',
			      'Map 13' : 'data/Models/Sets/DBridge/High/Map 13r.tga',
			      'Map 27': 'data/Models/Sets/DBridge/High/Map 27r.tga'},
		'NormalMaps':{'g_imp_redbars': 'data/Models/Sets/Galaxy/g_imp_redbars_unlit.tga'},
		},
	"Sounds": {
		"Hull": {	40: ["D Hull Sound 1"],
				20: ["D Hull Sound 2"],
			},
		"Preload":
			{
			"D Hull Sound 1": {"file": "sfx/dbridge/TNGbreach.wav"},
			"D Hull Sound 2": {"file": "Sfx/Bridge/Impacts/hullcreak1.wav"},
			},
	},
	"bridgeSound":	{
		"LiftDoor": {"volume": 1.0,"file": "sfx/dbridge/dbdoor.wav", "group": "BridgeGeneric"},
		"AmbBridge": {"volume": 0.3,"file": "sfx/dbridge/dbamb.wav", "group": "BridgeGeneric"},
		"RedAlertSound": {"volume": 1.0,"file": "sfx/dbridge/dbklaxton.wav", "group": "BridgeGeneric"},
		"GreenAlertSound": {"volume": 1.0,"file": "sfx/dbridge/dbgreen.wav", "group": "BridgeGeneric"},
		"ViewOn": {"volume": 1.0,"file": "sfx/dbridge/dbviewscreenon.wav", "group": "BridgeGeneric"},
		"ViewOff": {"volume": 1.0,"file": "sfx/dbridge/dbviewscreenoff.wav", "group": "BridgeGeneric"}
	},
	"LoadingScreen": "data/Icons/LoadingScreens/GalaxyLoading.tga",
	#"Animations": {
	#	"YellowAlert": {
	#		"XO": ["data/Animations/_dusting_uniform.NIF"],
	#	},
	#},
} )

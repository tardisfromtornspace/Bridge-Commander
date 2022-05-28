import Foundation
import StaticDefs

Foundation.BridgeDef('Sovereign', 'SovereignBridge', dict = { 	
    'modes': [ Foundation.MutatorDef.Stock ],
    'ExtraObjects': {"ModelTwo": ["data/Models/Sets/EBridge/modeltwo/sovereigntwo.NIF", "data/Models/Sets/EBridge/"]},
    'Maps':{
		'CurrentMaps': {'redalertpanel': "redalertpanel", 'front pillars': "front pillars", 'underlig': "underlig"},
		'GreenMaps':{'redalertpanel': 'data/Models/Sets/EBridge/High/redalertpanel.tga', 'front pillars': 'data/Models/Sets/EBridge/modeltwo/front pillars.tga', 'underlig': 'data/Models/Sets/EBridge/modeltwo/underlig.tga'},
		'YellowMaps':{'redalertpanel': 'data/Models/Sets/EBridge/High/redalertpanel.tga', 'front pillars': 'data/Models/Sets/EBridge/modeltwo/front pillars.tga', 'underlig': 'data/Models/Sets/EBridge/modeltwo/underlig.tga'},
		'RedMaps':{'redalertpanel': 'data/Models/Sets/EBridge/High/redalertpanelon.tga', 'front pillars': 'data/Models/Sets/EBridge/modeltwo/front pillarsr.tga', 'underlig': 'data/Models/Sets/EBridge/modeltwo/underligr.tga'},
		'NormalMaps':{'redalertpanel': 'data/Models/Sets/EBridge/High/redalertpanel.tga', 'front pillars': 'data/Models/Sets/EBridge/modeltwo/front pillars.tga', 'underlig': 'data/Models/Sets/EBridge/modeltwo/underlig.tga'}
		},
    'bridgeSound': 	{
			"LiftDoor": {"volume": 1.0,"file": "sfx/ebridge/ebdoor.wav", "group": "BridgeGeneric"},
			"AmbBridge": {"volume": 0.1,"file": "sfx/ebridge/ebamb.wav", "group": "BridgeGeneric"},
			"RedAlertSound": {"volume": 1.0,"file": "sfx/ebridge/ebklaxton.wav", "group": "BridgeGeneric"},
			"YellowAlertSound": {"volume": 1.0,"file": "sfx/ebridge/ebyellow.wav", "group": "BridgeGeneric"},
			"GreenAlertSound": {"volume": 1.0,"file": "sfx/ebridge/ebgreen.wav", "group": "BridgeGeneric"},
			"ViewOn": {"volume": 1.0,"file": "sfx/ebridge/ebviewscreenon.wav", "group": "BridgeGeneric"},
			"ViewOff": {"volume": 1.0,"file": "sfx/ebridge/ebviewscreenoff.wav", "group": "BridgeGeneric"}
			},
    "LoadingScreen": "data/Icons/LoadingScreens/SovereignLoading.tga",
})

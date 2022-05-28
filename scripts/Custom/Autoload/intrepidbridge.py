import Foundation

def GreenAlertConsole(dAnimInfo, ani):
	if dAnimInfo.get("YellowAlert::bridge::data/animations/bp/alert1.NIF played", 0) or dAnimInfo.get("RedAlert::bridge::data/animations/bp/alert1.NIF played", 0):
		dAnimInfo["YellowAlert::bridge::data/animations/bp/alert1.NIF played"] = 0
		dAnimInfo["RedAlert::bridge::data/animations/bp/alert1.NIF played"] = 0
		return 1
	return 0

def YellowRedAlertConsole(dAnimInfo, ani):
	if dAnimInfo.get("GreenAlert::bridge::data/animations/bp/alert2.NIF played", 0):
		dAnimInfo["GreenAlert::bridge::data/animations/bp/alert2.NIF played"] = 0
		return 1
	if dAnimInfo.get("YellowAlert::bridge::data/animations/bp/alert1.NIF played", 0) == 0 and dAnimInfo.get("RedAlert::bridge::data/animations/bp/alert1.NIF played", 0) == 0:
		dAnimInfo["GreenAlert::bridge::data/animations/bp/alert2.NIF played"] = 0
		return 1
	return 0

# Uncomment the below to enable!
Foundation.BridgeDef('Intrepid', 'intrepidbridge', dict = {
	'modes': [ Foundation.MutatorDef.Stock ],
	'locations': {
		# Intrepid-Bridge Locations
		'IntHelm':	[ 'data/animations/Int_stand_h_m.nif', 'Int_stand_h_m' ],
		'IntTactical':	[ 'data/animations/Int_stand_t_l.nif', 'Int_stand_t_l' ],
		'IntCommander':	[ 'data/animations/Int_stand_c_m.nif', 'Int_stand_c_m' ],
		'IntScience':	[ 'data/animations/Int_stand_S_S.nif', 'Int_stand_s_s' ],
		'IntEngineer':	[ 'data/animations/Int_seated_e_s.nif', 'Int_seated_e_s' ],
		'EBCommander1':	[ 'data/animations/EB_C1toC_M.nif', 'EB_C1toC_M' ],
		'IntGuest':	[ 'data/animations/Int_stand_X_m.nif', 'Int_stand_X_m' ],
		'IntL1S':	[ 'data/animations/Int_L1toG3_S.nif', 'Int_L1toG3_s', 'pCharacter.SetHidden(1)' ],
		'IntL1M':	[ 'data/animations/Int_L1toG3_M.nif', 'Int_L1toG3_M', 'pCharacter.SetHidden(0)' ],
		'IntL1L':	[ 'data/animations/Int_L1toG3_L.nif', 'Int_L1toG3_L', 'pCharacter.SetHidden(1)' ],
		'IntL2M':	[ 'data/animations/Int_L2toG2_M.nif', 'Int_L2toG2_M', 'pCharacter.SetHidden(1)' ],
		'IntG1M':	[ 'data/animations/Int_G1toL2_M.nif', 'Int_G1toL2_M' ],
		'IntG2M':	[ 'data/animations/Int_G2toL2_M.nif', 'Int_G2toL2_M' ],
		'IntG3M':	[ 'data/animations/Int_G3toL1_M.nif', 'Int_G3toL1_M' ],
	},

	'Animations': {
		'GreenAlert': {
			'bridge': [
				{
					"ani": "data/animations/bp/alert2.NIF", "Requirement": GreenAlertConsole,
				},
			],
		},
		'YellowAlert': {
			'bridge': [
				{
					"ani": "data/animations/bp/alert1.NIF", "Requirement": YellowRedAlertConsole,
				},
			],
		},
		'RedAlert': {
			'bridge': [
				{
					"ani": "data/animations/bp/alert1.NIF", "Requirement": YellowRedAlertConsole,
				},
			],
		},
	},

	'Maps':{
		'CurrentMaps': {"voybri8_resizedra" : "voybri8_resizedra", "capt_lcars":"capt_lcars", "doorpanel_light":"doorpanel_light"},
		'GreenMaps':{'doorpanel_light': 'data/Models/Sets/intrepidbridgev3/high/doorpanel_light.tga',
		             'voybri8_resizedra': 'data/Models/Sets/intrepidbridgev3/high/voybri8_resizedra.tga',
			     'capt_lcars': 'data/Models/Sets/intrepidbridgev3/high/capt_lcars.tga'},

		'YellowMaps':{'doorpanel_light': 'data/Models/Sets/intrepidbridgev3/high/doorpanel_light_ra.tga',
			     'voybri8_resizedra': 'data/Models/Sets/intrepidbridgev3/high/voybri8_resizedra_red.tga',
			     'capt_lcars': 'data/Models/Sets/intrepidbridgev3/high/capt_lcars.tga'},

		'RedMaps':{  'doorpanel_light': 'data/Models/Sets/intrepidbridgev3/high/doorpanel_light_ra.tga',
                             'voybri8_resizedra': 'data/Models/Sets/intrepidbridgev3/high/voybri8_resizedra_red.tga',
			     'capt_lcars': 'data/Models/Sets/intrepidbridgev3/high/capt_lcars_red.tga'},

		'NormalMaps':{'doorpanel_light': 'data/Models/Sets/intrepidbridgev3/high/doorpanel_light.tga',
			     'voybri8_resizedra': 'data/Models/Sets/intrepidbridgev3/high/voybri8_resizedra.tga',
			     'capt_lcars': 'data/Models/Sets/intrepidbridgev3/high/capt_lcars.tga'},
		},
	"bridgeSound": {
			"LiftDoor": {"volume": 0.6,"file": "sfx/Intrepid/door.wav", "group": "BridgeGeneric"},
			"AmbBridge": {"volume": 0.6,"file": "sfx/Intrepid/ambience.wav", "group": "BridgeGeneric"},
			"RedAlertSound": {"volume": 1.0,"file": "sfx/Intrepid/red.wav", "group": "BridgeGeneric"},
			"YellowAlertSound": {"volume": 1.0,"file": "sfx/Intrepid/yellow.wav", "group": "BridgeGeneric"},
			"GreenAlertSound": {"volume": 0.5,"file": "sfx/Intrepid/green.wav", "group": "BridgeGeneric"},
			"ViewOn": {"volume": 1.0,"file": "sfx/Intrepid/view_on.wav", "group": "BridgeGeneric"},
			"ViewOff": {"volume": 1.0,"file": "sfx/Intrepid/view_off.wav", "group": "BridgeGeneric"}},

	"LoadingScreen": "data/Icons/LoadingScreens/IntrepidLoading.tga",
} )


pBridgePlugin = None
try:
	pBridgePlugin = __import__("Custom.Autoload.000-Fixes20040612-LCBridgeAddon")
	if not hasattr(pBridgePlugin, "sVersion"): # Any core that doesn't have the variable doesn't appear to be supported, rather odd actually.
		Foundation.bridgeList["intrepidbridge"].Animations = {}
except:
	pass
pBridgePlugin = None

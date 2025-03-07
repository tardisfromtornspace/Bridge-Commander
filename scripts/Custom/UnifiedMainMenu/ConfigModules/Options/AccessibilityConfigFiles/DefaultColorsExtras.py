# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL LICENSE AS WELL
# DefaultColorsExtras.py
# 7th March 2025, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the AccesibilityConfig UMM option (located at scripts/Custom/UnifiedMainMenu/ConfigModules/Options/), this file must be under scripts/Custom/UnifiedMainMenu/ConfigModules/Options/AccesibilityConfigFiles
##################################
# This file takes care of listing the variable colors which are modified in other files and used instead of regular colors, like FoundationTech's Hull Gauge tech
#extraVariables = {
#	"g_pConditionColors" : {"g_pConditionColors": ["App"]},
#}
# If we were to add extra App. colors, we can also add the following, as long as those colors exist or are registered on App.py
# If they are not registered on App.py then we register them ourselves!
"""
import App
AblativeArmour = None
try:
	AblativeArmour = __import__("App")
except:
	AblativeArmour = None
if AblativeArmour != None:
	if not hasattr(AblativeArmour, "g_kMultiplayerRadioPink"): # Ok, so it is not g_kMultiplayerRadioPink - it does not exist on Appc, apparently
		import Appc
		import new
		App.g_kMultiplayerRadioPink = App.NiColorA() #App.NiColorAPtr(Appc.globals.g_kMultiplayerRadioPink)
		App.g_kMultiplayerRadioPink.r = 174.0 / 255.0
		App.g_kMultiplayerRadioPink.g = 9.0 / 255.0
		App.g_kMultiplayerRadioPink.b = 19.0 / 255.0
		App.g_kMultiplayerRadioPink.a = 1
"""

sDefaultColors = { # Colors from App.py
	# We could add it to a pre-existing category, like STButton marker colors.
	# Or maybe a new one
	"Other interface colors" : {
		"g_pConditionColors": [None, []],
	},
	"STButton base colors (some)" : {
		"g_kSTButtonColors": [None, []],
	},

	"STButton marker colors" : {
		"g_kSTButtonMarkerGray": [None, []],

	},

}

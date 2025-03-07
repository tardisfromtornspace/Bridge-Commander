# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL LICENSE AS WELL
# GalaxyChartsGalaxyMapGUIExtras.py
# 7th March 2025, by Alex SL Gato (CharaToLoki)
# Version: 1.2
# Meant to be used alongside the AccesibilityConfig UMM option (located at scripts/Custom/UnifiedMainMenu/ConfigModules/Options/), this file must be under scripts/Custom/UnifiedMainMenu/ConfigModules/Options/AccesibilityConfigFiles
##################################
# This file takes care of listing the variable colors which are modified in other files and used instead of regular colors, like FoundationTech's Hull Gauge tech
extraVariables = {
	"GCGalaxyMapGUICOLOR_PLAYER" : {"COLOR_PLAYER": ["Custom.GalaxyCharts.GalaxyMapGUI"]},
	"GCGalaxyMapGUICOLOR_REGION" : {"COLOR_REGION": ["Custom.GalaxyCharts.GalaxyMapGUI"]},
	"GCGalaxyMapGUICOLOR_SELECTED" : {"COLOR_SELECTED": ["Custom.GalaxyCharts.GalaxyMapGUI"]},
	"GCGalaxyMapGUICOLOR_HOSTILE" : {"COLOR_HOSTILE": ["Custom.GalaxyCharts.GalaxyMapGUI"]},
	"GCGalaxyMapGUICOLOR_ALLIED" : {"COLOR_ALLIED": ["Custom.GalaxyCharts.GalaxyMapGUI"]},
}
# If we were to add extra App. colors, we can also add the following, as long as those colors exist or are registered on App.py
# If they are not registered on App.py then we register them ourselves!
import App
AblativeArmour = None
try:
	AblativeArmour = __import__("Custom.GalaxyCharts.GalaxyMapGUI") #from ftb.Tech import AblativeArmour
except:
	
	AblativeArmour = None

if AblativeArmour != None:
	if hasattr(AblativeArmour, "COLOR_PLAYER"):
		App.GCGalaxyMapGUICOLOR_PLAYER = AblativeArmour.COLOR_PLAYER
	if hasattr(AblativeArmour, "COLOR_REGION"):
		App.GCGalaxyMapGUICOLOR_REGION = AblativeArmour.COLOR_REGION
	if hasattr(AblativeArmour, "COLOR_SELECTED"):
		App.GCGalaxyMapGUICOLOR_SELECTED = AblativeArmour.COLOR_SELECTED
	if hasattr(AblativeArmour, "COLOR_HOSTILE"):
		App.GCGalaxyMapGUICOLOR_HOSTILE = AblativeArmour.COLOR_HOSTILE
	if hasattr(AblativeArmour, "COLOR_ALLIED"):
		App.GCGalaxyMapGUICOLOR_ALLIED = AblativeArmour.COLOR_ALLIED

sDefaultColors = { # Colors from App.py
	# We could add it to a pre-existing category, like STButton marker colors.
	# Or maybe a new one
	"Galaxy Charts' colors" : {
		"GCGalaxyMapGUICOLOR_PLAYER": [None, []],
		"GCGalaxyMapGUICOLOR_REGION": [None, []],
		"GCGalaxyMapGUICOLOR_SELECTED": [None, []],
		"GCGalaxyMapGUICOLOR_HOSTILE": [None, []],
		"GCGalaxyMapGUICOLOR_ALLIED": [None, []],
	},
}

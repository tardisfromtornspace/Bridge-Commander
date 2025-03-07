# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL LICENSE AS WELL
# CustomTechsAlternateSubModelFTLExtras.py
# 7th March 2025, by Alex SL Gato (CharaToLoki)
# Version: 1.1
# Meant to be used alongside the AccesibilityConfig UMM option (located at scripts/Custom/UnifiedMainMenu/ConfigModules/Options/), this file must be under scripts/Custom/UnifiedMainMenu/ConfigModules/Options/AccesibilityConfigFiles
##################################
# This file takes care of listing the variable colors which are modified in other files and used instead of regular colors, like FoundationTech's Hull Gauge tech
extraVariables = {
	"AlternateSubModelFTLNormalColor" : {"NormalColor": ["Custom.Techs.AlternateSubModelFTL"]},
	"AlternateSubModelFTLHighlightedColor" : {"HighlightedColor": ["Custom.Techs.AlternateSubModelFTL"]},
	"AlternateSubModelFTLNormalColor2" : {"NormalColor2": ["Custom.Techs.AlternateSubModelFTL"]},
	"AlternateSubModelFTLHighlightedColor2" : {"HighlightedColor2": ["Custom.Techs.AlternateSubModelFTL"]},
	"AlternateSubModelFTLDisabledColor" : {"DisabledColor": ["Custom.Techs.AlternateSubModelFTL"]},
}
# If we were to add extra App. colors, we can also add the following, as long as those colors exist or are registered on App.py
# If they are not registered on App.py then we register them ourselves!
import App
AblativeArmour = None
try:
	AblativeArmour = __import__("Custom.Techs.AlternateSubModelFTL") #from ftb.Tech import AblativeArmour
except:
	
	AblativeArmour = None

if AblativeArmour != None:
	if hasattr(AblativeArmour, "NormalColor"):
		App.AlternateSubModelFTLNormalColor = AblativeArmour.NormalColor
	if hasattr(AblativeArmour, "HighlightedColor"):
		App.AlternateSubModelFTLHighlightedColor = AblativeArmour.HighlightedColor
	if hasattr(AblativeArmour, "NormalColor2"):
		App.AlternateSubModelFTLNormalColor2 = AblativeArmour.NormalColor2
	if hasattr(AblativeArmour, "HighlightedColor2"):
		App.AlternateSubModelFTLHighlightedColor2 = AblativeArmour.HighlightedColor2
	if hasattr(AblativeArmour, "DisabledColor"):
		App.AlternateSubModelFTLDisabledColor = AblativeArmour.DisabledColor

sDefaultColors = { # Colors from App.py
	# We could add it to a pre-existing category, like STButton marker colors.
	# Or maybe a new one
	"Foundation Technologies' colors" : {
		"AlternateSubModelFTLNormalColor": [None, []],
		"AlternateSubModelFTLHighlightedColor": [None, []],
		"AlternateSubModelFTLNormalColor2": [None, []],
		"AlternateSubModelFTLHighlightedColor2": [None, []],
		"AlternateSubModelFTLDisabledColor": [None, []],
	},
}

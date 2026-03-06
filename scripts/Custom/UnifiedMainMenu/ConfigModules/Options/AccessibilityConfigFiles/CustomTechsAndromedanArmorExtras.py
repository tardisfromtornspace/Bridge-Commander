# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL LICENSE AS WELL
# CustomTechsAndromedanArmorExtras.py
# 6th March 2026, by Alex SL Gato (CharaToLoki)
# Version: 1.2
# Meant to be used alongside the AccesibilityConfig UMM option (located at scripts/Custom/UnifiedMainMenu/ConfigModules/Options/), this file must be under scripts/Custom/UnifiedMainMenu/ConfigModules/Options/AccesibilityConfigFiles
##################################
# This file takes care of listing the variable colors which are modified in other files and used instead of regular colors, like FoundationTech's Hull Gauge tech
extraVariables = {
	"g_kSubsystemFillColor" : {"kEmptyColor": ["Custom.Techs.AndromedanArmor", "ftb.Tech.AndromedanArmor"]},
	"CustomTechsAndromedanArmorFill" : {"kFillColor": ["Custom.Techs.AndromedanArmor", "ftb.Tech.AndromedanArmor"]}, # A CUSTOM VALUE!
}
# If we were to add extra App. colors, we can also add the following, as long as those colors exist or are registered on App.py
# If they are not registered on App.py then we register them ourselves!
import App
AblativeArmour = None
try:
	AblativeArmour = __import__("Custom.Techs.AndromedanArmor") #from ftb.Tech import AblativeArmour
except:
	try:
		AblativeArmour = __import__("ftb.Tech.AndromedanArmor")
	except:
		AblativeArmour = None

if AblativeArmour != None:
	if hasattr(AblativeArmour, "kFillColor"):
		App.CustomTechsAndromedanArmorFill = AblativeArmour.kFillColor

sDefaultColors = { # Colors from App.py
	# We could add it to a pre-existing category, like STButton marker colors.
	# Or maybe a new one
	"Foundation Technologies' colors" : {
		"CustomTechsAndromedanArmorFill": [None, []],
	},
}

# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL LICENSE AS WELL
# DefaultExtraFileChecks.py
# 2nd March 2025, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the AccesibilityConfig UMM option (located at scripts/Custom/UnifiedMainMenu/ConfigModules/Options/), this file must be under scripts/Custom/UnifiedMainMenu/ConfigModules/Options/AccesibilityConfigFiles
##################################
# This file takes care of listing the variable colors which are modified in other files and used instead of regular colors, like FoundationTech's Hull Gauge tech
extraVariables = {
	"g_kSubsystemFillColor" : {"kHullFillColor" : "FoundationTech"}, # Variable which is also defined somewhere - attribute name - path to that file 
	"g_kSubsystemEmptyColor" : {"kHullEmptyColor" : "FoundationTech"},
}
# If we were to add extra App. colors, we can also add the following, as long as those colors exist or are registered on App.py
#sDefaultColors = { # Colors from App.py
#	# We could add it to a pre-existing category, like STButton marker colors.
#	"STButton marker colors" : {
#		"variableNameGoesHere": [None, []],
#	},
#	# Or maybe a new one
#	"Extended extra configs" : {
#		"AnotherVariableNameGoesHere": [None, []],
#	},
#}

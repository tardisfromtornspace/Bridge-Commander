# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE FOUNDATION LGPL LICENSE AS WELL
# Nanite Armor.py
# 18th March 2025, by Greystar adjust colors, fixed by Alex SL Gato (CharaToLoki), modified from Greystar's (which was likely an ftb AblativeArmour script copy)
# Meant to be used alongside ftb AblativeArmour, in fact, it requires it to work properly
##################################
#
MODINFO = { "Author": "\"ftb Team\", \"Apollo\", \"Greystar\", \"Alex SL Gato\" (andromedavirgoa@gmail.com)",
	    "Version": "0.11",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }
#
#################################################################################################################
#
import App
from bcdebug import debug
import Foundation
import FoundationTech

kEmptyColor = App.TGColorA()
kEmptyColor.SetRGBA(App.g_kSubsystemFillColor.r,App.g_kSubsystemFillColor.g,App.g_kSubsystemFillColor.b,App.g_kSubsystemFillColor.a)
kFillColor = App.TGColorA()
kFillColor.SetRGBA(40.0/255.0, 120.0/255.0, 255.0/255.0, App.g_kSubsystemFillColor.a)

AblativeArmour = None
oDiffusiveArmor = None

try:
	AblativeArmour = __import__("ftb.Tech.AblativeArmour") #from ftb.Tech import AblativeArmour
except:
	try:
		AblativeArmour = __import__("Custom.Techs.AblativeArmour")
	except:
		AblativeArmour = None

if AblativeArmour != None:
	class DiffusiveArmorDef(AblativeArmour.AblativeDef):
		def GetSystemName(self):
			debug(__name__ + ", GetSystemName")
			return "Diffusive Armor"

		def GetFillColor(self):
			global kFillColor
			return kFillColor
		
		def GetEmptyColor(self):
			global kEmptyColor
			return kEmptyColor

	oDiffusiveArmor = DiffusiveArmorDef('Diffusive Armor')
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL LICENSE AS WELL
# AccesibilityConfig.py
# 2nd March 2025, by USS Sovereign, slightly tweaked by Alex SL Gato
#
# Modify, redistribute to your liking. Just remember to give credit where due.
#################################################################################################################
# This will be the BCMM way. Trick is it requires early registration; which on BCMM case is done by importing this in FixApp.py file which is already modified on BCMM
#
MODINFO = { "Author": "\"USS Sovereign\" (mario0085), Noat (noatblok),\"Alex SL Gato\" (andromedavirgoa@gmail.com)",
	    "Version": "0.13",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }
#
#################################################################################################################
#

import App

# Alex SL gato's slight tweak, to fix certain issues - a check!
applyUpt = 1

"""
theBCMMFile = "scripts\\FontExtension.py"
pBCMMModule = None

try:
	pBCMMModule = __import__(theBCMMFile)
except:
	pBCMMModule = None
"""

if hasattr(App.g_kFontManager, "GetFontList"): #if (pBCMMModule and not hasattr(pBCMMModule, "GetFontList")) or hasattr(App.g_kFontManager, "GetFontList"):
	print "Font Extension system already implemented, skipping scripts\\FontExtension.py..."
	applyUpt = 0

registry = []
defaultFont = None
originalRegisterFont = App.TGFontManager.RegisterFont
originalSetDefaultFont = App.TGFontManager.SetDefaultFont

class Font:
	def __init__(self, name, size, file, loadMethod):
		self.name = name
		self.size = size
		self.file = file
		self.loadMethod = loadMethod

def RegisterFontOverride(_self, name, size, file, loadMethod):
	global registry, defaultFont
	registry.append(Font(name, size, file, loadMethod))
	# First registered font is default
	if len(registry) == 1:
		defaultFont = registry[0]
	return originalRegisterFont(_self, name, size, file, loadMethod)


def NewGetFontList(_self, *args):
	global registry
	# Return a copy, don't return original list
	if registry == None:
		registry = []
	return list(registry)


def SetDefaultFontOverride(_self, name, size):
	global registry, defaultFont
	for font in registry:
		if font.name == name:
			defaultFont = font
			break
	return originalSetDefaultFont(_self, name, size)


# noinspection PyUnresolvedReferences
def GetDefaultEFont(_self):
	global defaultFont
	if defaultFont:
		return Font(defaultFont.name, defaultFont.size, defaultFont.file, defaultFont.loadMethod)
	return None

if applyUpt:
	# Yes monkey patch to extend the logic, you can chain them the way you want to it will have no ill effects
	App.TGFontManager.RegisterFont = RegisterFontOverride
	App.TGFontManager.SetDefaultFont = SetDefaultFontOverride

	# New method to expose lists
	App.TGFontManager.GetFontList = NewGetFontList

	# Modified because GetDefaultFont already exists and returns an App.FontGroupPtr, while our new method throws Font and does not inherit from any FontGroup - added a new method to TGFontManager instead - Alex SL Gato
	App.TGFontManager.GetDefaultEFont = GetDefaultEFont

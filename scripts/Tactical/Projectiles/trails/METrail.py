# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# METrial.py
# This file is used as part of the Tactical.Projectiles.trails.OriBeam 1st Augut 2025 version 1.01 for extra Alpha Key Customization for templates.
# 1st August 2025
#################################################################################################################
#
MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "1.01",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }
#
#################################################################################################################
#

# Imports and global variables
import App

# This function below is there so people can customize it from their own files
def DefaultColorKeyFunc(pEffect, fSize):
	pEffect.AddColorKey(0.0, 0.5, 0.8, 1.0)

	pEffect.AddAlphaKey(0.0, 0.6)
	pEffect.AddAlphaKey(0.5, 0.5)
	pEffect.AddAlphaKey(1.0, 0.0)

	pEffect.AddSizeKey(0.05, 0.016 * fSize)
	pEffect.AddSizeKey(0.05, 0.83 * fSize)
	pEffect.AddSizeKey(0.05, 0.16 * fSize)
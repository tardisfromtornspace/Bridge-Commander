# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# LoadTextures.py
# Practically a function taken from other LoadGFX scripts like USS Sovereign's LoadGFX
# 25th March 2025
#################################################################################################################
#
MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "1.0",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }
#
#################################################################################################################
#

import App

def LoadGFX(iNumXFrames, iNumYFrames, sFile):
                fX = 0.0
                fY = 0.0

                pContainer = App.g_kTextureAnimManager.AddContainer(sFile)   
                pTrack = pContainer.AddTextureTrack(iNumXFrames * iNumYFrames)
                for index in range(iNumXFrames * iNumYFrames):
                        pTrack.SetFrame(index, fX, fY + (1.0 / iNumYFrames), fX + (1.0 / iNumXFrames), fY)
                        fX = fX + (1.0 / iNumXFrames)

                        if (fX >= 1.0):
                            fX = 0.0
                            fY = fY + (1.0 / iNumYFrames)
###############################################################################
##	Filename:	BrdgGfx.py
##
##	Nano's Bridge Gfx Dynamic Loading Version 1.0
##
##	Created:	01/28/2004 - NanoByte a.k.a Michael T. Braams
###############################################################################
import App
import Foundation

###############################################################################
## Load Nano's New Effect Textures
###############################################################################
def LoadNanoBrdgGfx():

	### Setup ###
	###
	### Load the Gfx files into BC
	LoadGfxFiles("Explosions", 8, 4)
	###

###############################################################################
## Function to load Textures into BC
###############################################################################
def LoadGfxFiles(sEffectType, iNumXFrames, iNumYFrames):

	sFolder = 'scripts/Custom/NanoFXv2/BridgeFX/Gfx/' + sEffectType
	sFileNames = Foundation.GetFileNames(sFolder, 'tga')

	for loadIndex in sFileNames:
		strFile = sFolder + '/' + loadIndex

		fX = 0.0
		fY = 0.0

		pContainer = App.g_kTextureAnimManager.AddContainer(strFile)

		### Load a Normal X * Y Frame Explosion Effect ###
		pTrack = pContainer.AddTextureTrack(iNumXFrames * iNumYFrames)

		for index in range(iNumXFrames * iNumYFrames):
			pTrack.SetFrame(index, fX, fY + (1.0 / iNumYFrames), fX + (1.0 / iNumXFrames), fY)
			fX = fX + (1.0 / iNumXFrames)

			if (fX == 1.0):
				fX = 0.0
				fY = fY + (1.0 / iNumYFrames)
		
		pTrack.SetFrame(index, fX, fY + (1.0 / iNumYFrames), fX + (1.0 / iNumXFrames), fY)
		pTrack.SetFrame(index, fX, fY + (1.0 / iNumYFrames), fX + (1.0 / iNumXFrames), fY)
		pTrack.SetFrame(index, fX, fY + (1.0 / iNumYFrames), fX + (1.0 / iNumXFrames), fY)
		pTrack.SetFrame(index, fX, fY + (1.0 / iNumYFrames), fX + (1.0 / iNumXFrames), fY)
		pTrack.SetFrame(index, fX, fY + (1.0 / iNumYFrames), fX + (1.0 / iNumXFrames), fY)
		pTrack.SetFrame(index, fX, fY + (1.0 / iNumYFrames), fX + (1.0 / iNumXFrames), fY)
		pTrack.SetFrame(index, fX, fY + (1.0 / iNumYFrames), fX + (1.0 / iNumXFrames), fY)
		pTrack.SetFrame(index, fX, fY + (1.0 / iNumYFrames), fX + (1.0 / iNumXFrames), fY)
		###
###############################################################################
## End of Loading Exp Gfx
###############################################################################
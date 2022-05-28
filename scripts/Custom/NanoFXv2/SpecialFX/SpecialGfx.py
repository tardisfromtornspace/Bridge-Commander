###############################################################################
##	Filename:	SpecialGfx.py
##
##	Special Gfx Dynamic Loading Version 1.0
##
##	Created:	03/11/2003 - NanoByte a.k.a Michael T. Braams
###############################################################################
import App
import Foundation

###############################################################################
## Load Nano's New Effect Textures
###############################################################################
def LoadNanoSpecialGfx(Icons = None):

	### Setup ###
	if(Icons is None):
		Icons = App.g_kIconManager.CreateIconGroup("EffectTextures")
		# Add group to manager.
		App.g_kIconManager.AddIconGroup(Icons)
	###
	### Load the Gfx files into BC
	LoadGfxFiles("Atmosphere", 1, 1)
	LoadGfxFiles("Blinker", 1, 1)
	LoadGfxFiles("Plasma", 8, 4)
	LoadGfxFiles("Weapon", 4, 2)
	###

###############################################################################
## Function to load Textures into BC
###############################################################################
def LoadGfxFiles(sEffectType, iNumXFrames, iNumYFrames):

	sFolder = 'scripts/Custom/NanoFXv2/SpecialFX/Gfx/' + sEffectType
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
		###
###############################################################################
## End of Loading Exp Gfx
###############################################################################
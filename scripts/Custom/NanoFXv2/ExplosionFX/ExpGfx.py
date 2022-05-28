###############################################################################
##	Filename:	ExpGfx.py
##
##	Nano's Explosion Gfx Dynamic Loading Version 1.0
##
##	Created:	03/11/2003 - NanoByte a.k.a Michael T. Braams
###############################################################################
import App
import Foundation

###############################################################################
## Load Nano's New Effect Textures
###############################################################################
def LoadNanoExpGfx():

	### Setup ###
	###
	### Load the Gfx files into BC
	LoadGfxFiles("Debris", 1, 1)
	LoadGfxFiles("ExpFlash", 4, 4)
	LoadGfxFiles("Explosions", 8, 4)
	LoadGfxFiles("Particles", 1, 1)
	LoadGfxFiles("NovaFlash", 8, 2)
	LoadGfxFiles("NovaSphere", 8, 4)
	LoadGfxFiles("NovaRing", 8, 8)
	###

###############################################################################
## Load New Damage Textures into BC
###############################################################################
def LoadNanoDamageGfx(Icons = None):

	if(Icons is None):
		Icons = App.g_kIconManager.CreateIconGroup("DamageTextures")
		App.g_kIconManager.AddIconGroup(Icons)


	sFolder = 'scripts/Custom/NanoFXv2/ExplosionFX/Gfx/Damage'
	sFileNames = Foundation.GetFileNames(sFolder, 'tga')

	for loadIndex in range(len(sFileNames)):
		strFile = sFolder + '/' + sFileNames[loadIndex]
		kTexture = Icons.LoadIconTexture(strFile)
		Icons.SetIconLocation(loadIndex, kTexture, 0, 0, 128, 128)


###############################################################################
## Function to load Textures into BC
###############################################################################
def LoadGfxFiles(sEffectType, iNumXFrames, iNumYFrames):

	sFolder = 'scripts/Custom/NanoFXv2/ExplosionFX/Gfx/' + sEffectType
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

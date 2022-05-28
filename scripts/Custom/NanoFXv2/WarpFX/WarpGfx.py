###############################################################################
##	Filename:	WarpGfx.py
##
##	Nano's Warp Gfx Dynamic Loading Version 1.0
##
##	Created:	03/31/2003 - NanoByte a.k.a Michael T. Braams
###############################################################################
import App
import Foundation

###############################################################################
## Load Nano's Warp Nacelle Effect Textures
###############################################################################
def LoadNanoWarpNacelleGfx(Icons = None):
	
	### Setup ###
	if(Icons is None):
		Icons = App.g_kIconManager.CreateIconGroup("EffectTextures")
		# Add group to manager.
		App.g_kIconManager.AddIconGroup(Icons)
	###
	kTexture = Icons.LoadIconTexture("scripts/Custom/NanoFXv2/WarpFX/Gfx/StarStreaks_Nano.tga")
	Icons.SetIconLocation(0, kTexture, 0, 0, 64, 64)
	### Load Default Space Dust Texture... for some reason effects.py doesn't load it! ###
	kTexture = Icons.LoadIconTexture("scripts/Custom/NanoFXv2/WarpFX/Gfx/SpaceDust_Nano.tga")
	Icons.SetIconLocation(10, kTexture, 0, 0, 16, 16)
	###
	### Load the Gfx files into BC
	LoadGfxFiles("NacelleFlash", 4, 4)
	###

###############################################################################
## Load Warp Flash Textures into BC
###############################################################################
def LoadNanoWarpFlashGfx(Icons = None):

	if(Icons is None):
		Icons = App.g_kIconManager.CreateIconGroup("WarpFlashTextures")
		App.g_kIconManager.AddIconGroup(Icons)

	sFolder = 'scripts/Custom/NanoFXv2/WarpFX/Gfx/WarpFlash'
	sFileNames = Foundation.GetFileNames(sFolder, 'tga')

	for loadIndex in range(len(sFileNames)):
		strFile = sFolder + '/' + sFileNames[loadIndex]
		kTexture = Icons.LoadIconTexture(strFile)
		Icons.SetIconLocation(loadIndex, kTexture, 0, 0, 64, 64)

###############################################################################
## Function to load Textures into BC
###############################################################################
def LoadGfxFiles(sEffectType, iNumXFrames, iNumYFrames):

	sFolder = 'scripts/Custom/NanoFXv2/WarpFX/Gfx/' + sEffectType
	sFileNames = Foundation.GetFileNames(sFolder, 'tga')

	for loadIndex in sFileNames:
		strFile = sFolder + '/' + loadIndex

		fX = 0.0
		fY = 0.0

		pContainer = App.g_kTextureAnimManager.AddContainer(strFile)

		### Load a Normal X * Y Frame Explosion Effect ###
		pTrack = pContainer.AddTextureTrack(iNumXFrames * iNumYFrames)

		for index in range(iNumXFrames * iNumYFrames - 1):
			pTrack.SetFrame(index, fX, fY + (1.0 / iNumYFrames), fX + (1.0 / iNumXFrames), fY)
			fX = fX + (1.0 / iNumXFrames)

			if (fX == 1.0):
				fX = 0.0
				fY = fY + (1.0 / iNumYFrames)
		###
###############################################################################
## End of Loading Warp Gfx
###############################################################################
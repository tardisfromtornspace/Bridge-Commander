###############################################################################
##	Filename:	SpecialSfx.py
##
##	SpecialFX Sound Effects Module for Loading Sounds Dynamically
##
##	Created:	09/30/2003 - NanoByte a.k.a Michael T. Braams
###############################################################################
import App
import Foundation

###############################################################################
## Get Sfx List for Game use
###############################################################################
def GetSfxList(sSoundSet):

	sFileNames = Foundation.GetFileNames('scripts/Custom/NanoFXv2/SpecialFX/Sfx/' + sSoundSet, 'wav')
	sSfxList = []

	for fileIndex in range(len(sFileNames)):
		sSfxList.append(sSoundSet + str(fileIndex))

	return sSfxList

###############################################################################
## Setup Sound Defs for SpecialFX Sounds
###############################################################################
def LoadNanoSpecialSfx(mode):

	### Plasma Rupture Sfx ###
	sFolder = 'scripts/Custom/NanoFXv2/SpecialFX/Sfx/Plasma'
	sFileNames = Foundation.GetFileNames(sFolder, 'wav')
	for loadIndex in range(len(sFileNames)):
		strFile = sFolder + '/' + sFileNames[loadIndex]
		Foundation.SoundDef(strFile, sFileNames[loadIndex], 1.0, { 'modes': [ mode ] })
	###

###############################################################################
## Get a Random Sfx, try not to repeat last 3 sounds in Recent List 
############################################################################### 
def GetRandomSound(sSfxList): 	
	
	sSound = sSfxList[ App.g_kSystemWrapper.GetRandomNumber( len(sSfxList) ) ] 	
	return sSound

###############################################################################
## End of Special Sfx
###############################################################################
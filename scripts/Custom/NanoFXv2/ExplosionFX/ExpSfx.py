###############################################################################
##	Filename:	ExpSfx.py
##
##	Explosion Sound Effects Module for Loading Sounds Dynamically
##
##	Created:	03/09/2003 - NanoByte a.k.a Michael T. Braams
###############################################################################
import App
import Foundation

###############################################################################
## Get Sfx List for Game use
###############################################################################
def GetSfxList(sSoundSet):

	sFileNames = Foundation.GetFileNames('scripts/Custom/NanoFXv2/ExplosionFX/Sfx/' + sSoundSet, 'wav')
	sSfxList = []

	for fileIndex in range(len(sFileNames)):
		sSfxList.append(sSoundSet + str(fileIndex))

	return sSfxList

###############################################################################
## Setup Sound Defs for Explosion Sounds
###############################################################################
def LoadNanoExpSfx(mode):

	### Collision Explosion Sfx ###
	sFolder = 'scripts/Custom/NanoFXv2/ExplosionFX/Sfx/ExpCollision'
	sFileNames = Foundation.GetFileNames(sFolder, 'wav')
	for loadIndex in range(len(sFileNames)):
		strFile = sFolder + '/' + sFileNames[loadIndex]
		Foundation.SoundDef(strFile, "ExpCollision" + str(loadIndex), 1.0, { 'modes': [ mode ] })
	###
	### Shield Explosion Sfx (Weapon Hit Sheild) ###
	sIndex = "1"
	sFolder = 'scripts/Custom/NanoFXv2/ExplosionFX/Sfx/ExpShield'
	sFileNames = Foundation.GetFileNames(sFolder, 'wav')
	for loadIndex in range(len(sFileNames)):
		strFile = sFolder + '/' + sFileNames[loadIndex]
		Foundation.SoundDef(strFile, "ExpShield" + str(loadIndex), 1.0), { 'modes': [ mode ] }
	###
	### Small Explosion Sfx (Weapon Hit Hull) ###
	sIndex = "1"
	sFolder = 'scripts/Custom/NanoFXv2/ExplosionFX/Sfx/ExpSmall'
	sFileNames = Foundation.GetFileNames(sFolder, 'wav')
	for loadIndex in range(len(sFileNames)):
		strFile = sFolder + '/' + sFileNames[loadIndex]
		Foundation.SoundDef(strFile, "ExpSmall" + str(loadIndex), 1.0), { 'modes': [ mode ] }
	###
	### Medium Explosion Sfx (Debris and Sparks) ###
	sIndex = "1"
	sFolder = 'scripts/Custom/NanoFXv2/ExplosionFX/Sfx/ExpMed'
	sFileNames = Foundation.GetFileNames(sFolder, 'wav')
	for loadIndex in range(len(sFileNames)):
		strFile = sFolder + '/' + sFileNames[loadIndex]
		Foundation.SoundDef(strFile, "ExpMed" + str(loadIndex), 1.0), { 'modes': [ mode ] }
	###
	### Large Explosion Sfx (Ship Destroyed) ###
	sIndex = "1"
	sFolder = 'scripts/Custom/NanoFXv2/ExplosionFX/Sfx/ExpLarge'
	sFileNames = Foundation.GetFileNames(sFolder, 'wav')
	for loadIndex in range(len(sFileNames)):
		strFile = sFolder + '/' + sFileNames[loadIndex]
		Foundation.SoundDef(strFile, "ExpLarge" + str(loadIndex), 1.0, { 'modes': [ mode ] })
	###
	### Nova Explosion Sfx (Warpcore Explosion!)###
	sIndex = "1"
	sFolder = 'scripts/Custom/NanoFXv2/ExplosionFX/Sfx/ExpNova'
	sFileNames = Foundation.GetFileNames(sFolder, 'wav')
	for loadIndex in range(len(sFileNames)):
		strFile = sFolder + '/' + sFileNames[loadIndex]
		Foundation.SoundDef(strFile, "ExpNova" + str(loadIndex), 1.0, { 'modes': [ mode ] })

###############################################################################
## Get a Random Sfx, try not to repeat last 3 sounds in Recent List 
############################################################################### 
def GetRandomSound(sSfxList):  	
	
	sSound = sSfxList[ App.g_kSystemWrapper.GetRandomNumber( len(sSfxList) ) ]  	
	return sSound

###############################################################################
## End of Exp Sfx
###############################################################################
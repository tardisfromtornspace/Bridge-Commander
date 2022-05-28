from bcdebug import debug
##############################################################################

#	Filename:	LoadTacticalSounds.py

#

#	Confidential and Proprietary, Copyright 2000 by Totally Games

#

#	This contains the code to load tactical sounds.

#

#	Created:	9/12/00 -	DLitwin

###############################################################################

import App



# Dasher42's sound plugin support

import Foundation



###############################################################################

#	LoadSounds()

#

#	Load sounds that are needed throughout the game, in tactical.

#

#	Args:	none

#

#	Return:	none

###############################################################################

def LoadSounds(mode = Foundation.MutatorDef.StockSounds):

	debug(__name__ + ", LoadSounds")
	pGame = App.Game_GetCurrentGame()



	for i in mode.sounds.values():

		pGame.LoadSound(i.fileName,	i.name,	App.TGSound.LS_3D).SetVolume(i.volume)
	
	pGame.LoadSound("scripts/Custom/NanoFXv2/WarpFX/Sfx/NanoWarpFlash.wav", "Warp Flash", 0)





###############################################################################

#	GetRandomSound

#

#	Get a random sound from the given list of sound names.  This tries

#	not to return the same sound more than once every 3 calls.

#

#	Args:	lsSoundList	- A list of sound names to choose from (such

#						  as g_lsDeathExplosions, below)

#

#	Return:	One of the sounds in lsSoundList

###############################################################################

g_dRecentSounds = {}

def GetRandomSound(lsSoundList):

	debug(__name__ + ", GetRandomSound")
	global g_dRecentSounds

	try:

		lRecent = g_dRecentSounds[lsSoundList]

	except KeyError:

		lRecent = []

		g_dRecentSounds[lsSoundList] = lRecent



	# Randomly choose a sound from lsSoundList that isn't in lRecent.

	lsAvailableSounds = list(lsSoundList[:])

	for sSound in lRecent:

		lsAvailableSounds.remove(sSound)

	if not lsAvailableSounds:

		lsAvailableSounds = lsSoundList


	irandval = 0
	if lsAvailableSounds:
		irandval = App.g_kSystemWrapper.GetRandomNumber(len(lsAvailableSounds))
	sSound = lsAvailableSounds[irandval]



	# If there's more than 1 sound in the Recent Sounds list, remove the oldest one.

	if len(lRecent) > 1:

		lRecent.pop(0)

	# Add sSound to the list.

	lRecent.append(sSound)



	return sSound



g_lsDeathExplosions = (

	"Death Explosion 1",

	"Death Explosion 2",

	"Death Explosion 3",

	"Death Explosion 4",

	"Death Explosion 5",

	"Death Explosion 6",

	"Death Explosion 7",

	"Death Explosion 8",

	"Death Explosion 9",

	"Death Explosion 10",

	)



g_lsBigDeathExplosions = (

	"Big Death Explosion 1",

	"Big Death Explosion 2",

	"Big Death Explosion 3",

	"Big Death Explosion 4",

	"Big Death Explosion 5",

	"Big Death Explosion 6",

	"Big Death Explosion 7",

	"Big Death Explosion 8",

	)



g_lsWeaponExplosions = (

	"Explosion 1",

	"Explosion 2",

	"Explosion 3",

	"Explosion 4",

	"Explosion 5",

	"Explosion 6",

	"Explosion 7",

	"Explosion 8",

	"Explosion 9",

	"Explosion 10",

	"Explosion 11",

	"Explosion 12",

	"Explosion 13",

	"Explosion 14",

	"Explosion 15",

	"Explosion 16",

	"Explosion 17",

	"Explosion 18",

	"Explosion 19",

	)



g_lsCollisionSounds = (

	"Collision 1",

	"Collision 2",

	"Collision 3",

	"Collision 4",

	"Collision 5",

	"Collision 6",

	"Collision 7",

	"Collision 8",

	)


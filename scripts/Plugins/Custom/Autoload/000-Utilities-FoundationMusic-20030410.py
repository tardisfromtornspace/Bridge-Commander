import Foundation
import string
import nt


class MusicDef:
	def __init__(self):
		self.dMain = {}		# Base songs/fanfares to use as music...
		self.dStates = {}

	def AddFolder(self, sFolder, sGroup):
		if not self.dStates.has_key(sGroup):
			self.dStates[sGroup] = []
		try:
			lFolder = nt.listdir(sFolder)
			for i in lFolder:
				sName = sFolder + '/' + i

				s = string.split(i, '.')
				name = string.join(s[:-1], '.')
				ext = string.lower(s[-1])
				if ext == 'mp3':
					self.dMain[sName] = name
					self.dStates[sGroup].append(name)
		except:
			pass


	def Add(self, obj):
		# Update from the folder's __init__.py
		try:
			self.dMain.update(obj.dMain)
			self.dStates.update(obj.dStates)
		except:
			pass

		# Now add in from the subfolders
		try:
			for i in obj.lFolders:
				s = string.split(i, '/')
				self.AddFolder(i, s[-1])
		except:
			pass


	def BuildList(self):
		# PrintDict(self.dGroups)

		lStates = []		# Special music states which are collections of pieces of music, played in random order.
		lTrans = []
		lMain = []
		bBlanked = 0

		for i in self.dMain.keys():
			lMain.append(i, self.dMain[i])

		kPtr = None
		kMaxlen = 0
		for i in self.dStates.keys():
			k = self.dStates[i]
			if len(k) > kMaxlen:
				kMaxlen = len(k)
				kPtr = k

		for i in self.dStates.keys():
			k = self.dStates[i]
			if len(k) == 0:
				k = kPtr
			if len(k) == 1:
				# This is necessary; BC crashes if there's only one element in a state list.
				if not bBlanked:
					lMain.append('Custom/Music/Blank.mp3', 'Blank')
					bBlanked = 1
				k.append('Blank')
			if i == 'Transition':
				for j in k:
					lTrans.append(j)
			else:
				lStates.append(i, k)

		return (lMain, lTrans, lStates)



	def ChangeMusic(self, pEngine):
		lStates = []		# Special music states which are collections of pieces of music, played in random order.
		lTrans = []
		lMain = []

		(lMain, lTrans, lStates) = self.BuildList()

		import DynamicMusic
		DynamicMusic.ChangeMusic(tuple(lMain), tuple(lTrans), tuple(lStates), pEngine)



	def Initialize(self, pGame, pEngine):
		lStates = []		# Special music states which are collections of pieces of music, played in random order.
		lTrans = []
		lMain = []

		(lMain, lTrans, lStates) = self.BuildList()

		import DynamicMusic
		DynamicMusic.Initialize(pGame, tuple(lMain), tuple(lTrans), tuple(lStates), pEngine)



def GetMusic(self):
	try:
		return self.music
	except:
		try:
			return self.race.music
		except:
			return Foundation.MusicDef.default


Foundation.MusicDef = MusicDef
Foundation.ShipDef.GetMusic = GetMusic


Foundation.MusicDef.default = Foundation.MusicDef()
Foundation.MusicDef.default.dMain = {
		'sfx/Music/EpisGen2.mp3':		'Starting Ambient',
		'sfx/Music/Starbase12.mp3':		'Starbase12 Ambient',
		'sfx/Music/Nebula 1.mp3':		'Nebula Ambient',
		'sfx/Music/Failure-8d.mp3':		'Lose',
		'sfx/Music/Success-12.mp3':		'Win',
		'sfx/Music/Transition 13.mp3':	'EnemyBlewUp',
		'sfx/Music/Transition 14.mp3':	'PlayerBlewUp',
		'sfx/Music/Panic-9a.mp3': 		'Panic-9a',
		'sfx/Music/Panic-9b.mp3': 		'Panic-9b',
		'sfx/Music/Panic-9c.mp3': 		'Panic-9c',
		'sfx/Music/Panic-9d.mp3': 		'Panic-9d',
		'sfx/Music/Panic-9e.mp3': 		'Panic-9e',
		'sfx/Music/Panic-9f.mp3': 		'Panic-9f',
		'sfx/Music/Panic-9g.mp3': 		'Panic-9g',
		'sfx/Music/Neutral-10i.mp3': 	'Neutral-10i',
		'sfx/Music/Neutral-10b.mp3': 	'Neutral-10b',
		'sfx/Music/Neutral-10c.mp3': 	'Neutral-10c',
		'sfx/Music/Neutral-10d.mp3': 	'Neutral-10d',
		'sfx/Music/Neutral-10e.mp3': 	'Neutral-10e',
		'sfx/Music/Neutral-10f.mp3': 	'Neutral-10f',
		'sfx/Music/Neutral-10g.mp3': 	'Neutral-10g',
		'sfx/Music/Neutral-10h.mp3': 	'Neutral-10h',
		'sfx/Music/Neutral-10a.mp3': 	'Neutral-10a',
		'sfx/Music/Confident-11a.mp3': 	'Confident-11a',
		'sfx/Music/Confident-11b.mp3': 	'Confident-11b',
		'sfx/Music/Confident-11c.mp3': 	'Confident-11c',
		'sfx/Music/Confident-11d.mp3': 	'Confident-11d',
		'sfx/Music/Confident-11e.mp3': 	'Confident-11e',
		'sfx/Music/Confident-11f.mp3': 	'Confident-11f',
		'sfx/Music/Confident-11g.mp3': 	'Confident-11g',
}

Foundation.MusicDef.default.dStates = {
	'Combat Confident': ( 'Confident-11a', 'Confident-11b', 'Confident-11c', 'Confident-11d', 'Confident-11e', 'Confident-11f', 'Confident-11g' ),
	'Combat Neutral': ( 'Neutral-10i', 'Neutral-10b', 'Neutral-10c', 'Neutral-10d', 'Neutral-10e', 'Neutral-10f', 'Neutral-10g', 'Neutral-10h', 'Neutral-10a' ),
	'Combat Panic': ( 'Panic-9a', 'Panic-9b', 'Panic-9c', 'Panic-9d', 'Panic-9e', 'Panic-9f', 'Panic-9g' ),
}


for i in Foundation.raceList._arrayList:
	Foundation.raceList[i].music = Foundation.MusicDef.default

# commented out, because it does make trouble with save/load
#MusicDef = None

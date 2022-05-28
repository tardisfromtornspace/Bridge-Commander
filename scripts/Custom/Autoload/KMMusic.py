import App
import Foundation

sMutatorName = "Alternate Nemesis Music"

dKMMusic = {
	'sfx/Music/KM/kmstarbase12.mp3':	'Starbase12 Ambient',
	'sfx/Music/KM/kmnebula1.mp3':		'Nebula Ambient',
	'sfx/Music/KM/kmpanic1.mp3': 		'Panic-9a',
	'sfx/Music/KM/kmpanic2.mp3': 		'Panic-9b',
	'sfx/Music/KM/kmpanic3.mp3': 		'Panic-9c',
	'sfx/Music/KM/kmpanic4.mp3': 		'Panic-9d',
	'sfx/Music/KM/kmneutral1.mp3': 		'Neutral-10i',
	'sfx/Music/KM/kmneutral2.mp3': 		'Neutral-10b',
	'sfx/Music/KM/kmneutral3.mp3': 		'Neutral-10c',
	'sfx/Music/KM/kmneutral4.mp3': 		'Neutral-10d',
	'sfx/Music/KM/kmneutral5.mp3': 		'Neutral-10e',
	'sfx/Music/KM/kmconfident1.mp3': 	'Confident-11a',
	'sfx/Music/KM/kmconfident2.mp3': 	'Confident-11b',
	'sfx/Music/KM/kmconfident3.mp3': 	'Confident-11c',
	'sfx/Music/KM/kmconfident4.mp3': 	'Confident-11d',
	'sfx/Music/KM/kmconfident5.mp3': 	'Confident-11e',
	'sfx/Music/KM/kmconfident6.mp3': 	'Confident-11f',
	'sfx/Music/KM/kmconfident7.mp3': 	'Confident-11g',
}

Foundation.MutatorDef(sMutatorName)

MusicDef = Foundation.MusicDef

def CheckActiveMutator(MutatorName):
	Foundation.LoadConfig()
	for i in Foundation.mutatorList._arrayList:
		fdtnMode = Foundation.mutatorList._keyList[i]
		if fdtnMode.IsEnabled() and (fdtnMode.name == MutatorName):
			return 1
	return 0

def delete_item(my_dict, my_item):
        for i in my_dict.keys():
                if my_dict[i] == my_item:
                        del my_dict[i]

def SetKMMusic():
	for key in dKMMusic.keys():
		val = dKMMusic[key]
		delete_item(MusicDef.default.dMain, val)
		MusicDef.default.dMain[key] = val

if CheckActiveMutator(sMutatorName):
	SetKMMusic()

import App
import Foundation

Foundation.Klingon.music = Foundation.MusicDef()
Foundation.Klingon.music.dMain = {
	'sfx/Music/Klingon/EpisGen2.mp3':	'Starting Ambient',
	'sfx/Music/Klingon/Starbase12.mp3':	'Starbase12 Ambient',
	'sfx/Music/Klingon/Nebula 1.mp3':	'Nebula Ambient',
	'sfx/Music/Klingon/Failure-8d.mp3':	'Lose',
	'sfx/Music/Klingon/Success-12.mp3':	'Win',
	'sfx/Music/Klingon/Transition 13.mp3':	'EnemyBlewUp',
	'sfx/Music/Klingon/Transition 14.mp3':	'PlayerBlewUp',
	'sfx/Music/Klingon/Panic-9a.mp3': 	'Panic-9a',
	'sfx/Music/Klingon/Panic-9b.mp3': 	'Panic-9b',
	'sfx/Music/Klingon/Panic-9c.mp3': 	'Panic-9c',
	'sfx/Music/Klingon/Panic-9d.mp3': 	'Panic-9d',
	'sfx/Music/Klingon/Panic-9e.mp3': 	'Panic-9e',
	'sfx/Music/Klingon/Panic-9f.mp3': 	'Panic-9f',
	'sfx/Music/Klingon/Panic-9g.mp3': 	'Panic-9g',
	'sfx/Music/Klingon/Neutral-10i.mp3': 	'Neutral-10i',
	'sfx/Music/Klingon/Neutral-10b.mp3': 	'Neutral-10b',
	'sfx/Music/Klingon/Neutral-10c.mp3': 	'Neutral-10c',
	'sfx/Music/Klingon/Neutral-10d.mp3': 	'Neutral-10d',
	'sfx/Music/Klingon/Neutral-10e.mp3': 	'Neutral-10e',
	'sfx/Music/Klingon/Neutral-10f.mp3': 	'Neutral-10f',
	'sfx/Music/Klingon/Neutral-10g.mp3': 	'Neutral-10g',
	'sfx/Music/Klingon/Neutral-10h.mp3': 	'Neutral-10h',
	'sfx/Music/Klingon/Neutral-10a.mp3': 	'Neutral-10a',
	'sfx/Music/Klingon/Confident-11a.mp3': 	'Confident-11a',
	'sfx/Music/Klingon/Confident-11b.mp3': 	'Confident-11b',
	'sfx/Music/Klingon/Confident-11c.mp3': 	'Confident-11c',
	'sfx/Music/Klingon/Confident-11d.mp3': 	'Confident-11d',
	'sfx/Music/Klingon/Confident-11e.mp3': 	'Confident-11e',
	'sfx/Music/Klingon/Confident-11f.mp3': 	'Confident-11f',
	'sfx/Music/Klingon/Confident-11g.mp3': 	'Confident-11g',
}

# collection of available titles
dict_musics = {}
dict_musics[0] = "sfx/Music/Klingon/Episode 4.mp3"
dict_musics[1] = "sfx/Music/Klingon/Episode 2.mp3"
dict_musics[2] = "sfx/Music/Klingon/EpisGen2.mp3"
dict_musics[3] = "sfx/Music/Klingon/Episode 7.mp3"

def delete_item(my_dict, my_item):
        for i in my_dict.keys():
                if my_dict[i] == my_item:
                        del my_dict[i]

# and get a random music
def GrabRandomAmbient():
	MusicMain = Foundation.Klingon.music.dMain

        # delete old first
        delete_item(MusicMain, "Starting Ambient")
        
        my_ambient_num = App.g_kSystemWrapper.GetRandomNumber(len(dict_musics))
        my_ambient = dict_musics[my_ambient_num]
        MusicMain[my_ambient] = "Starting Ambient"

# change Ambient
GrabRandomAmbient()

from bcdebug import debug
import App
from Foundation import MusicDef


# collection of available titles
dict_musics = {}
dict_musics[0] = "sfx/Music/EpisGen1.mp3"
dict_musics[1] = "sfx/Music/EpisGen2.mp3"
dict_musics[2] = "sfx/Music/EpisGen3.mp3"
dict_musics[3] = "sfx/Music/Episode 1.mp3"
dict_musics[4] = "sfx/Music/Episode 2.mp3"
dict_musics[5] = "sfx/Music/Episode 3.mp3"
dict_musics[6] = "sfx/Music/Episode 4.mp3"
dict_musics[7] = "sfx/Music/Episode 5.mp3"
dict_musics[8] = "sfx/Music/Episode 5b.mp3"
dict_musics[9] = "sfx/Music/Episode 6.mp3"
dict_musics[10] = "sfx/Music/Episode 7.mp3"
dict_musics[11] = "sfx/Music/Episode 8.mp3"


def delete_item(my_dict, my_item):
        debug(__name__ + ", delete_item")
        for i in my_dict.keys():
                if my_dict[i] == my_item:
                        del my_dict[i]


# and get a random music
def GrabRandomAmbient():
        # delete old first
        debug(__name__ + ", GrabRandomAmbient")
        delete_item(MusicDef.default.dMain, "Starting Ambient")
        
	if dict_musics:
        	my_ambient_num = App.g_kSystemWrapper.GetRandomNumber(len(dict_musics))
        	my_ambient = dict_musics[my_ambient_num]
        	MusicDef.default.dMain[my_ambient] = "Starting Ambient"

# change Ambient
GrabRandomAmbient()

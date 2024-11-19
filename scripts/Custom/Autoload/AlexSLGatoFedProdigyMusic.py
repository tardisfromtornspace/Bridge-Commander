from bcdebug import debug

import App
import Foundation

from Custom.Autoload.RaceFedProdigy import *

Foundation.FedProdigy.music = Foundation.MusicDef()

Foundation.FedProdigy.music.dMain = {
	"sfx/Music/FedProdigy/STProdigy.mp3":	"Starting Ambient",
	"sfx/Music/MainMenu/Khan.mp3":	"Starbase12 Ambient",
	"sfx/Music/MainMenu/Enterprise.mp3":	"Nebula Ambient",
	"sfx/Music/MainMenu/Kelvin.mp3":	"Lose",
	"sfx/Music/MainMenu/Search for Spock.mp3":	"Win",
	"sfx/Music/MainMenu/DS9.mp3":	                "EnemyBlewUp",
	"sfx/Music/MainMenu/firefly.mp3":	"PlayerBlewUp",
	"sfx/Music/MainMenu/Klingon.mp3": 	"Panic-9a",
	"sfx/Music/MainMenu/The Undiscovered Country.mp3": 	"Panic-9b",
	"sfx/Music/MainMenu/TOS.mp3": 	"Panic-9c",
	"sfx/Music/MainMenu/TMP.mp3": 	"Panic-9d",
	"sfx/Music/MainMenu/TNG.mp3": 	"Panic-9e",
	"sfx/Music/MainMenu/Voyager.mp3": 	"Panic-9f",
	"sfx/Music/Panic-9e.mp3": 	"Panic-9g",
	"sfx/Music/Panic-9f.mp3": 	"Panic-9h",
	"sfx/Music/Panic-9g.mp3": 	"Panic-9i",
        "sfx/Music/Neutral-10a.mp3": 	"Neutral-10a",
	"sfx/Music/Neutral-10b.mp3": 	"Neutral-10b",
	"sfx/Music/MainMenu/Ressikan Flute.mp3": 	"Neutral-10c",
	"sfx/Music/Neutral-10d.mp3": 	"Neutral-10d",
	"sfx/Music/Neutral-10e.mp3": 	"Neutral-10e",
	"sfx/Music/Neutral-10f.mp3": 	"Neutral-10f",
	"sfx/Music/Neutral-10g.mp3": 	"Neutral-10g",
	"sfx/Music/Neutral-10h.mp3": 	"Neutral-10h",
	"sfx/Music/Neutral-10i.mp3": 	"Neutral-10i",
	"sfx/Music/MainMenu/Default.mp3": 	"Confident-11a",
	"sfx/Music/Confident-11b.mp3": 	"Confident-11b",
	"sfx/Music/Confident-11c.mp3": 	"Confident-11c",
	"sfx/Music/Confident-11d.mp3": 	"Confident-11d",
	"sfx/Music/Confident-11e.mp3": 	"Confident-11e",
	"sfx/Music/Confident-11f.mp3": 	"Confident-11f",
	"sfx/Music/Confident-11g.mp3": 	"Confident-11g",
	"sfx/Music/KM/kmconfident5.mp3": 	"Confident-11h",
	"sfx/Music/KM/kmstarbase12.mp3": 	"Confident-11i",
}

Foundation.FedProdigy.music.dStates = {
	'Combat Confident': ( 'Confident-11a', 'Confident-11b', 'Confident-11c', 'Confident-11d', 'Confident-11e', 'Confident-11f', 'Confident-11g', 'Confident-11h', 'Confident-11i' ),
	'Combat Failure': ( 'Lose', 'PlayerBlewUp' ),
	'Combat Neutral': ( 'Neutral-10a', 'Neutral-10b', 'Neutral-10c', 'Neutral-10d', 'Neutral-10e', 'Neutral-10f', 'Neutral-10g', 'Neutral-10h', 'Neutral-10i' ),
	'Combat Panic': ( 'Panic-9a', 'Panic-9b', 'Panic-9c', 'Panic-9d', 'Panic-9e', 'Panic-9f', 'Panic-9g', 'Panic-9h', 'Panic-9i' ),
	
}

# collection of available titles
dict_musics = {}
dict_musics[0] = "sfx/Music/FedProdigy/STProdigy.mp3"
#dict_musics[1] = "sfx/Music/MainMenu/Khan.mp3"
#dict_musics[2] = "sfx/Music/MainMenu/Enterprise.mp3"


def delete_item(my_dict, my_item):
        for i in my_dict.keys():
                if my_dict[i] == my_item:
                        del my_dict[i]

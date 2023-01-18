from bcdebug import debug

import App
import Foundation

from Custom.Autoload.RaceDalek import *

Dalek.music = Foundation.MusicDef()

Dalek.music.dMain = {
	'sfx/Music/Dalek/Dalek2.mp3':	'Starting Ambient',
	'sfx/Music/Dalek/Davros.mp3':	'Starbase12 Ambient',
	'sfx/Music/Klingon/Nebula 1.mp3':	'Nebula Ambient',
	'sfx/Music/Dalek/LoneDalek.mp3':	'Lose',
	'sfx/Music/Dalek/DalekVictory.mp3':	'Win',
	'sfx/Music/Dalek3.mp3':	                'EnemyBlewUp',
	'sfx/Music/Dalek/LoneDalek.mp3':	'PlayerBlewUp',
	'sfx/Music/Dalek3.mp3': 	'Panic-9a',
	'sfx/Music/Dalek3.mp3': 	'Panic-9b',
	'sfx/Music/Dalek3.mp3': 	'Panic-9c',
	'sfx/Music/Dalek3.mp3': 	'Panic-9d',
	'sfx/Music/Dalek3.mp3': 	'Panic-9e',
	'sfx/Music/Dalek/DalekEvo.mp3': 'Panic-9f',
	'sfx/Music/Gallifreyan/StrCre.mp3': 	'Panic-9g',
	'sfx/Music/Gallifreyan/StrCre.mp3': 	'Panic-9h',
	'sfx/Music/Dalek/DalekEvo.mp3':         'Panic-9i',
        'sfx/Music/Gallifreyan/StrCre.mp3': 	'Neutral-10a',
	'sfx/Music/Dalek/Dalek2.mp3': 	'Neutral-10b',
	'sfx/Music/Dalek/Dalek2.mp3': 	'Neutral-10c',
	'sfx/Music/Dalek/Dalek2.mp3': 	'Neutral-10d',
	'sfx/Music/Dalek/Dalek2.mp3': 	'Neutral-10e',
	'sfx/Music/Dalek/Dalek2.mp3': 	'Neutral-10f',
	'sfx/Music/Dalek/Dalek2.mp3': 	'Neutral-10g',
	'sfx/Music/Dalek/Dalek2.mp3': 	'Neutral-10h',
	'sfx/Music/Dalek3.mp3': 	'Neutral-10i',
	'sfx/Music/Dalek3.mp3': 	'Confident-11a',
	'sfx/Music/Dalek3.mp3': 	'Confident-11b',
	'sfx/Music/Dalek3.mp3': 	'Confident-11c',
	'sfx/Music/Dalek/Dalek2.mp3': 	'Confident-11d',
	'sfx/Music/Dalek/Dalek2.mp3': 	'Confident-11e',
	'sfx/Music/Dalek/Davros.mp3': 	'Confident-11f',
	'sfx/Music/Dalek/Davros.mp3': 	'Confident-11g',
	'sfx/Music/Dalek/Dalek2.mp3': 	'Confident-11h',
	'sfx/Music/Dalek/Dalek2.mp3': 	'Confident-11i',
}

# collection of available titles
dict_musics = {}
dict_musics[0] = "sfx/Music/Dalek/Davros.mp3"
dict_musics[1] = "sfx/Music/Dalek/DalekEvo.mp3"
dict_musics[2] = "sfx/Music/Dalek/Dalek2.mp3"
dict_musics[3] = "sfx/Music/Dalek3.mp3"

def delete_item(my_dict, my_item):
        for i in my_dict.keys():
                if my_dict[i] == my_item:
                        del my_dict[i]

# and get a random music
def GrabRandomAmbient():
	MusicMain = Dalek.music.dMain

        # delete old first
        delete_item(MusicMain, "Starting Ambient")
        
        my_ambient_num = App.g_kSystemWrapper.GetRandomNumber(len(dict_musics))
        my_ambient = dict_musics[my_ambient_num]
        MusicMain[my_ambient] = "Starting Ambient"

# change Ambient
GrabRandomAmbient()

"""
def init():  # Verify it's a dalek
                pGame	        = App.Game_GetCurrentGame()
                pEpisode	= pGame.GetCurrentEpisode()
                pMission	= pEpisode.GetCurrentMission()

                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SET_PLAYER, pMission, __name__ + ".PureDalekCheck")

def PureDalekCheck(pObject = None, pEvent = None):
                debug(__name__ + ", NewPlayerButtonCheck")
                global LastShipType
                pGame           = App.Game_GetCurrentGame()
                pEpisode        = pGame.GetCurrentEpisode()
                pMission        = pEpisode.GetCurrentMission()
                pPlayer	        = MissionLib.GetPlayer()             

                # Check if we are Dalek. If not, return to normal music.
                if (GetRaceFromShip(pPlayer) == "Dalek") or (GetShipType(pPlayer) == "Dalek2005Black"):

                        print "dalek"
                else:
                        print "Not a dalek"

# Graciously sent by Defiant.
def GetRaceFromShip(pShip):
                debug(__name__ + ", GetRaceFromShip")
                ShipType = GetShipType(pShip)
                print "looking for type"
                if Foundation.shipList.has_key(ShipType):
                        print "found key"
                        FdtnShip = Foundation.shipList[ShipType]
                
                        if FdtnShip.GetRace():
                                print FdtnShip.GetRace().name
                                return FdtnShip.GetRace().name
                        print "no race found"
                print "no keys"
                return None

    
# Returns the Shiptype (from ReturnShuttles)
def GetShipType(pShip):
                debug(__name__ + ", GetShipType")
                if pShip.GetScript():
                        return string.split(pShip.GetScript(), '.')[-1]
                return None
"""

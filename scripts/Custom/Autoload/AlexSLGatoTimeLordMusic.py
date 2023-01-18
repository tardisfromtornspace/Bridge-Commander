from bcdebug import debug

import App
import Foundation

from Custom.Autoload.RaceTimeLord import *

TimeLord.music = Foundation.MusicDef()

TimeLord.music.dMain = {
	'sfx/Music/Gallifreyan/UAAA-Clockwork Tardis.mp3':	                        'Starting Ambient',
	'sfx/Music/Gallifreyan/Davros.mp3':	                                        'Starbase12 Ambient',
	'sfx/Music/Gallifreyan/UAAA-Clockwork Tardis.mp3':	                        'Nebula Ambient',
	'sfx/Music/Gallifreyan/ZZVA-The Greatest Story Never Told.mp3':	                'Lose',
	'sfx/Music/Gallifreyan/ZKAA-Hanging On The Tablaphone.mp3':	                'Win',
	'sfx/Music/Gallifreyan/ZKAA-Hanging On The Tablaphone.mp3':	                'EnemyBlewUp',
	'sfx/Music/Gallifreyan/ZZVA-The Greatest Story Never Told.mp3':	                'PlayerBlewUp',
	'sfx/Music/Gallifreyan/ZKAA-Hanging On The TablaphoneDalek3.mp3': 	        'Panic-9a',
	'sfx/Music/Gallifreyan/ZZAA-New Adventures.mp3': 	                        'Panic-9b',
	'sfx/Music/Gallifreyan/ZZTA-The Futurekind.mp3': 	                        'Panic-9c',
	'sfx/Music/Gallifreyan/ZZXA-The Master Vainglorious.mp3': 	                'Panic-9d',
	'sfx/Music/Gallifreyan/ZZZG-This is Gallifrey_ Our Childhood, Our Home.mp3': 	'Panic-9e',
	'sfx/Music/Gallifreyan/ZZZM-YANA.mp3':                                          'Panic-9f',
	'sfx/Music/Gallifreyan/60thAnniversayThemes.mp3': 	                        'Panic-9g',
	'sfx/Music/Gallifreyan/StrCre.mp3': 	                                        'Panic-9h',
	'sfx/Music/Gallifreyan/TimeWarDoctor.mp3':                                      'Panic-9i',
        'sfx/Music/Gallifreyan/StrCre.mp3': 	                                        'Neutral-10a',
	'sfx/Music/Gallifreyan/UAAA-Clockwork Tardis.mp3': 	                        'Neutral-10b',
	'sfx/Music/Gallifreyan/60thAnniversayThemes.mp3': 	                        'Neutral-10c',
	'sfx/Music/Gallifreyan/ZZVA-The Greatest Story Never Told.mp3': 	        'Neutral-10d',
	'sfx/Music/Gallifreyan/PlasticMick.mp3': 	                                'Neutral-10e',
	'sfx/Music/Gallifreyan/UAAA-Clockwork Tardis.mp3': 	                        'Neutral-10f',
	'sfx/Music/Gallifreyan/UAAA-Clockwork Tardis.mp3': 	                        'Neutral-10g',
	'sfx/Music/Gallifreyan/MAAA-A Pressing Need To Save The World.mp3': 	        'Neutral-10h',
	'sfx/Music/Gallifreyan/60thAnniversayThemes.mp3': 	                        'Neutral-10i',
	'sfx/Music/Gallifreyan/PlasticMick.mp3': 	                                'Confident-11a',
	'sfx/Music/Gallifreyan/ZZAA-New Adventures.mp3': 	                        'Confident-11b',
	'sfx/Music/Gallifreyan/UAAA-Clockwork Tardis.mp3': 	                        'Confident-11c',
	'sfx/Music/Gallifreyan/60thAnniversayThemes.mp3': 	                        'Confident-11d',
	'sfx/Music/Gallifreyan/PlasticMick.mp3': 	                                'Confident-11e',
	'sfx/Music/Gallifreyan/ZZZG-This is Gallifrey_ Our Childhood, Our Home.mp3': 	'Confident-11f',
	'sfx/Music/Gallifreyan/ZKAA-Hanging On The TablaphoneDalek3.mp3': 	        'Confident-11g',
	'sfx/Music/Gallifreyan/UAAA-Clockwork Tardis.mp3': 	                        'Confident-11h',
	'sfx/Music/Gallifreyan/MAAA-A Pressing Need To Save The World': 	        'Confident-11i',
}

# collection of available titles
dict_musics = {}
dict_musics[0]  = "sfx/Music/Gallifreyan/60thAnniversayThemes.mp3"
dict_musics[1]  = "sfx/Music/Gallifreyan/MAAA-A Pressing Need To Save The World.mp3"
dict_musics[2]  = "sfx/Music/Gallifreyan/PlasticMick.mp3"
dict_musics[3]  = "sfx/Music/Gallifreyan/StrCre.mp3"
dict_musics[4]  = "sfx/Music/Gallifreyan/TimeWarDoctor.mp3"
dict_musics[5]  = "sfx/Music/Gallifreyan/UAAA-Clockwork Tardis.mp3"
dict_musics[6]  = "sfx/Music/Gallifreyan/ZKAA-Hanging On The Tablaphone.mp3"
dict_musics[7]  = "sfx/Music/Gallifreyan/ZZAA-New Adventures.mp3"
dict_musics[8]  = "sfx/Music/Gallifreyan/ZZTA-The Futurekind.mp3"
dict_musics[9]  = "sfx/Music/Gallifreyan/ZZVA-The Greatest Story Never Told.mp3"
dict_musics[10] = "sfx/Music/Gallifreyan/ZZXA-The Master Vainglorious.mp3"
dict_musics[11] = "sfx/Music/Gallifreyan/ZZZG-This is Gallifrey_ Our Childhood, Our Home.mp3"
dict_musics[12] = "sfx/Music/Gallifreyan/ZZZM-YANA.mp3"

def delete_item(my_dict, my_item):
        for i in my_dict.keys():
                if my_dict[i] == my_item:
                        del my_dict[i]

# and get a random music
def GrabRandomAmbient():
	MusicMain = TimeLord.music.dMain

        # delete old first
        delete_item(MusicMain, "Starting Ambient")
        
        my_ambient_num = App.g_kSystemWrapper.GetRandomNumber(len(dict_musics))
        my_ambient = dict_musics[my_ambient_num]
        MusicMain[my_ambient] = "Starting Ambient"

# change Ambient
GrabRandomAmbient()

"""
def init():  # Verify it's a TimeLord
                pGame	        = App.Game_GetCurrentGame()
                pEpisode	= pGame.GetCurrentEpisode()
                pMission	= pEpisode.GetCurrentMission()

                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SET_PLAYER, pMission, __name__ + ".PureTimeLordCheck")

def PureTimeLordCheck(pObject = None, pEvent = None):
                debug(__name__ + ", NewPlayerButtonCheck")
                global LastShipType
                pGame           = App.Game_GetCurrentGame()
                pEpisode        = pGame.GetCurrentEpisode()
                pMission        = pEpisode.GetCurrentMission()
                pPlayer	        = MissionLib.GetPlayer()             

                # Check if we are Dalek. If not, return to normal music.
                if (GetRaceFromShip(pPlayer) == "TimeLord") or (GetShipType(pPlayer) == "Tardis"):

                        print "TimeLord"
                else:
                        print "Not a TimeLord"

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

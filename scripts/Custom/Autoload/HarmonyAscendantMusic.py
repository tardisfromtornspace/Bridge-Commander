from bcdebug import debug

import App
import Foundation

from Custom.Autoload.RaceHarmonyAscendant import *

oHarmonyAscendantRace.music = Foundation.MusicDef()

oHarmonyAscendantRace.music.dMain = {
	'sfx/Music/Dawn of Harmony.wav': 	'Confident-11a'
}

# collection of available titles
dict_musics = {}
dict_musics[0] = "sfx/Music/Dawn of Harmony.wav"

def delete_item(my_dict, my_item):
        for i in my_dict.keys():
                if my_dict[i] == my_item:
                        del my_dict[i]

# and get a random music
def GrabRandomAmbient():
	MusicMain = oHarmonyAscendantRace.music.dMain

        # delete old first
        delete_item(MusicMain, "Starting Ambient")
        
        my_ambient_num = App.g_kSystemWrapper.GetRandomNumber(len(dict_musics))
        my_ambient = dict_musics[my_ambient_num]
        MusicMain[my_ambient] = "Starting Ambient"

# change Ambient
GrabRandomAmbient()

"""
def init():  # Verify it's a oHarmonyAscendantRace
                pGame	        = App.Game_GetCurrentGame()
                pEpisode	= pGame.GetCurrentEpisode()
                pMission	= pEpisode.GetCurrentMission()

                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SET_PLAYER, pMission, __name__ + ".PureooHarmonyAscendantRaceCheck")

def PureooHarmonyAscendantRaceCheck(pObject = None, pEvent = None):
                debug(__name__ + ", NewPlayerButtonCheck")
                global LastShipType
                pGame           = App.Game_GetCurrentGame()
                pEpisode        = pGame.GetCurrentEpisode()
                pMission        = pEpisode.GetCurrentMission()
                pPlayer	        = MissionLib.GetPlayer()             

                # Check if we are HarmonyAscendant. If not, return to normal music.
                if (GetRaceFromShip(pPlayer) == "oHarmonyAscendantRace"):

                        print "oHarmonyAscendantRace"
                else:
                        print "Not a oHarmonyAscendantRace"

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

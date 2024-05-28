from bcdebug import debug

import App
import Foundation

from Custom.Autoload.RaceCosmosASTO import *

CosmosASTO.music = Foundation.MusicDef()

CosmosASTO.music.dMain = {
	"sfx/Music/CosmosASTO/AAAE-Cosmos Main Title.mp3":	"Starting Ambient",
	"sfx/Music/MainMenu/Khan.mp3":	"Starbase12 Ambient",
	"sfx/Music/MainMenu/Enterprise.mp3":	"Nebula Ambient",
	"sfx/Music/CosmosASTO/08. The Inquisition.mp3":	"Lose",
	"sfx/Music/CosmosASTO/AAAG-Billion Years of Evolution.mp3":	"Win",
	"sfx/Music/CosmosASTO/AAAF-S.O.T.I..mp3":	                "EnemyBlewUp",
	"sfx/Music/MainMenu/firefly.mp3":	"PlayerBlewUp",
	"sfx/Music/CosmosASTO/01-Vangelis-Pulstar.mp3": 	"Panic-9a",
	"sfx/Music/CosmosASTO/06-Saint Louis Symphony Orchestra-Holst_ The Planets - Mars.mp3": 	"Panic-9b",
	"sfx/Music/CosmosASTO/10-Swedish Radio Symphony Orchestra-Stravinsky_ The Rite of Spring.mp3": 	"Panic-9c",
	"sfx/Music/CosmosASTO/12-Vivaldi (Various)-Concerto for Mandolin & Strings in C Major.mp3": 	"Panic-9d",
	"sfx/Music/CosmosASTO/14-Synergy-Legacy.mp3": 	"Panic-9e",
	"sfx/Music/CosmosASTO/07. Revelation of Immensity.mp3": 	"Panic-9f",
	"sfx/Music/CosmosASTO/12. New Year's Eve.mp3": 	"Panic-9g",
	"sfx/Music/CosmosASTO/04. Artificial Selection.mp3": 	"Panic-9h",
	"sfx/Music/CosmosASTO/10. Theory of Evolution.mp3": 	"Panic-9i",
        "sfx/Music/MainMenu/IWar.mp3": 	"Neutral-10a",
	"sfx/Music/MainMenu/Kelvin.mp3": 	"Neutral-10b",
	"sfx/Music/MainMenu/Ressikan Flute.mp3": 	"Neutral-10c",
	"sfx/Music/CosmosASTO/01-Vangelis-Heaven & Hell, Pt. 1.mp3": 	"Neutral-10d",
	"sfx/Music/CosmosASTO/13-Vangelis-Comet 16.mp3": 	"Neutral-10e",
	"sfx/Music/CosmosASTO/06-Pachelbel (James Galway)-The Pachelbel Canon.mp3": 	"Neutral-10f",
	"sfx/Music/CosmosASTO/05. Multiverse.mp3": 	"Neutral-10g",
	"sfx/Music/CosmosASTO/11. Chance Nature of Existence.mp3": 	"Neutral-10h",
	"sfx/Music/CosmosASTO/13. Titan.mp3": 	"Neutral-10i",
	"sfx/Music/MainMenu/Default.mp3": 	"Confident-11a",
	"sfx/Music/CosmosASTO/05-Mozart (Mostly Mozart Orchestra)-Clarinet Concerto A Major - K.622.mp3": 	"Confident-11b",
	"sfx/Music/CosmosASTO/11-Godfrey Finger (Leipziger Bach-Collegium)-Sonata D-Dur Fur Trompete, Oboe, und Basso Continuo.mp3": 	"Confident-11c",
	"sfx/Music/CosmosASTO/15-Rimsky-Korsakov (Seattle Symphony)-Russian Easter Festival Overture.mp3": 	"Confident-11d",
	"sfx/Music/CosmosASTO/02. 'Come With Me'.mp3": 	"Confident-11e",
	"sfx/Music/CosmosASTO/03. 'The Cosmos Is Yours'.mp3": 	"Confident-11f",
	"sfx/Music/CosmosASTO/09. The Staggering Immensity of Time.mp3": 	"Confident-11g",
	"sfx/Music/CosmosASTO/13. 'Our Journey Is Just Beginning'.mp3": 	"Confident-11h",
	"sfx/Music/CosmosASTO/13. Cosmos A Spacetime Odyssey - DVD End Credits.mp3": 	"Confident-11i",
}

"""
CosmosASTO.music.dMain = {
	"sfx/Music/CosmosASTO/AAAE-Cosmos Main Title.mp3":	"Starting Ambient",
	"sfx/Music/MainMenu/Khan.mp3":	"Starbase12 Ambient",
	"sfx/Music/MainMenu/Enterprise.mp3":	"Nebula Ambient",
	"sfx/Music/CosmosASTO/08. The Inquisition.mp3":	"Lose",
	"sfx/Music/CosmosASTO/AAAG-Billion Years of Evolution.mp3":	"Win",
	"sfx/Music/CosmosASTO/AAAF-S.O.T.I..mp3":	                "EnemyBlewUp",
	"sfx/Music/MainMenu/firefly.mp3":	"PlayerBlewUp",
	"sfx/Music/CosmosASTO/01-Vangelis-Pulstar.mp3": 	"Panic-9a",
	"sfx/Music/CosmosASTO/06-Saint Louis Symphony Orchestra-Holst_ The Planets - Mars.mp3": 	"Panic-9b",
	"sfx/Music/CosmosASTO/10-Swedish Radio Symphony Orchestra-Stravinsky_ The Rite of Spring.mp3": 	"Panic-9c",
	"sfx/Music/CosmosASTO/12-Vivaldi (Various)-Concerto for Mandolin & Strings in C Major.mp3": 	"Panic-9d",
	"sfx/Music/CosmosASTO/14-Synergy-Legacy.mp3": 	"Panic-9e",
	"sfx/Music/CosmosASTO/07. Revelation of Immensity.mp3": 	"Panic-9f",
	"sfx/Music/CosmosASTO/12. New Year's Eve.mp3": 	"Panic-9g",
	"sfx/Music/CosmosASTO/04. Artificial Selection.mp3": 	"Panic-9h",
	"sfx/Music/CosmosASTO/10. Theory of Evolution.mp3": 	"Panic-9i",
        "sfx/Music/MainMenu/IWar.mp3": 	"Neutral-10a",
	"sfx/Music/MainMenu/Kelvin.mp3": 	"Neutral-10b",
	"sfx/Music/MainMenu/Ressikan Flute.mp3": 	"Neutral-10c",
	"sfx/Music/CosmosASTO/01-Vangelis-Heaven & Hell, Pt. 1.mp3": 	"Neutral-10d",
	"sfx/Music/CosmosASTO/13-Vangelis-Comet 16.mp3": 	"Neutral-10e",
	"sfx/Music/CosmosASTO/06-Pachelbel (James Galway)-The Pachelbel Canon.mp3": 	"Neutral-10f",
	"sfx/Music/CosmosASTO/05. Multiverse.mp3": 	"Neutral-10g",
	"sfx/Music/CosmosASTO/11. Chance Nature of Existence.mp3": 	"Neutral-10h",
	"sfx/Music/CosmosASTO/13. Titan.mp3": 	"Neutral-10i",
	"sfx/Music/MainMenu/Default.mp3": 	"Confident-11a",
	"sfx/Music/CosmosASTO/05-Mozart (Mostly Mozart Orchestra)-Clarinet Concerto A Major - K.622.mp3": 	"Confident-11b",
	"sfx/Music/CosmosASTO/11-Godfrey Finger (Leipziger Bach-Collegium)-Sonata D-Dur Fur Trompete, Oboe, und Basso Continuo.mp3": 	"Confident-11c",
	"sfx/Music/CosmosASTO/15-Rimsky-Korsakov (Seattle Symphony)-Russian Easter Festival Overture.mp3": 	"Confident-11d",
	"sfx/Music/CosmosASTO/02. 'Come With Me'.mp3": 	"Confident-11e",
	"sfx/Music/CosmosASTO/03. 'The Cosmos Is Yours'.mp3": 	"Confident-11f",
	"sfx/Music/CosmosASTO/09. The Staggering Immensity of Time.mp3": 	"Confident-11g",
	"sfx/Music/CosmosASTO/13. 'Our Journey Is Just Beginning'.mp3": 	"Confident-11h",
	"sfx/Music/CosmosASTO/13. Cosmos A Spacetime Odyssey - DVD End Credits.mp3": 	"Confident-11i",

	"sfx/Music/CosmosASTO/./01-Vangelis-Pulstar.mp3": 	"Combat Panic",
	"sfx/Music/CosmosASTO/./06-Saint Louis Symphony Orchestra-Holst_ The Planets - Mars.mp3": 	"Combat Panic",
	"sfx/Music/CosmosASTO/./10-Swedish Radio Symphony Orchestra-Stravinsky_ The Rite of Spring.mp3": 	"Combat Panic",
	"sfx/Music/CosmosASTO/./12-Vivaldi (Various)-Concerto for Mandolin & Strings in C Major.mp3": 	"Combat Panic",
	"sfx/Music/CosmosASTO/./14-Synergy-Legacy.mp3": 	"Combat Panic",
	"sfx/Music/CosmosASTO/./07. Revelation of Immensity.mp3": 	"Combat Panic",
	"sfx/Music/CosmosASTO/./12. New Year's Eve.mp3": 	"Combat Panic",
	"sfx/Music/CosmosASTO/./04. Artificial Selection.mp3": 	"Combat Panic",
	"sfx/Music/CosmosASTO/./10. Theory of Evolution.mp3": 	"Combat Panic",
	"sfx/Music/CosmosASTO/./01-Vangelis-Heaven & Hell, Pt. 1.mp3": 	"Combat Neutral",
	"sfx/Music/CosmosASTO/./13-Vangelis-Comet 16.mp3": 	"Combat Neutral",
	"sfx/Music/CosmosASTO/./06-Pachelbel (James Galway)-The Pachelbel Canon.mp3": 	"Combat Neutral",
	"sfx/Music/CosmosASTO/./05. Multiverse.mp3": 	"Combat Neutral",
	"sfx/Music/CosmosASTO/./11. Chance Nature of Existence.mp3": 	"Combat Neutral",
	"sfx/Music/CosmosASTO/./13. Titan.mp3": 	"Combat Neutral",
	"sfx/Music/CosmosASTO/./05-Mozart (Mostly Mozart Orchestra)-Clarinet Concerto A Major - K.622.mp3": 	"Combat Confident",
	"sfx/Music/CosmosASTO/./11-Godfrey Finger (Leipziger Bach-Collegium)-Sonata D-Dur Fur Trompete, Oboe, und Basso Continuo.mp3": 	"Combat Confident",
	"sfx/Music/CosmosASTO/./15-Rimsky-Korsakov (Seattle Symphony)-Russian Easter Festival Overture.mp3": 	"Combat Confident",
	"sfx/Music/CosmosASTO/./02. 'Come With Me'.mp3": 	"Combat Confident",
	"sfx/Music/CosmosASTO/./03. 'The Cosmos Is Yours'.mp3": 	"Combat Confident",
	"sfx/Music/CosmosASTO/./09. The Staggering Immensity of Time.mp3": 	"Combat Confident",
	"sfx/Music/CosmosASTO/./13. 'Our Journey Is Just Beginning'.mp3": 	"Combat Confident",
	"sfx/Music/CosmosASTO/./13. Cosmos A Spacetime Odyssey - DVD End Credits.mp3": 	"Combat Confident",

}
"""

"""
CosmosASTO.music.dMain = {
	"sfx/Music/CosmosASTO/AAAE-Cosmos Main Title.mp3":	"Starting Ambient",
	"sfx/Music/MainMenu/Khan.mp3":	"Starbase12 Ambient",
	"sfx/Music/MainMenu/Enterprise.mp3":	"Nebula Ambient",
	"sfx/Music/CosmosASTO/08. The Inquisition.mp3":	"Lose",
	"sfx/Music/CosmosASTO/AAAG-Billion Years of Evolution.mp3":	"Win",
	"sfx/Music/CosmosASTO/AAAF-S.O.T.I..mp3":	                "EnemyBlewUp",
	"sfx/Music/MainMenu/firefly.mp3":	"PlayerBlewUp",
	"sfx/Music/CosmosASTO/01-Vangelis-Pulstar.mp3": 	"Combat Panic",
	"sfx/Music/CosmosASTO/06-Saint Louis Symphony Orchestra-Holst_ The Planets - Mars.mp3": 	"Combat Panic",
	"sfx/Music/CosmosASTO/10-Swedish Radio Symphony Orchestra-Stravinsky_ The Rite of Spring.mp3": 	"Combat Panic",
	"sfx/Music/CosmosASTO/12-Vivaldi (Various)-Concerto for Mandolin & Strings in C Major.mp3": 	"Combat Panic",
	"sfx/Music/CosmosASTO/14-Synergy-Legacy.mp3": 	"Combat Panic",
	"sfx/Music/CosmosASTO/07. Revelation of Immensity.mp3": 	"Combat Panic",
	"sfx/Music/CosmosASTO/12. New Year's Eve.mp3": 	"Combat Panic",
	"sfx/Music/CosmosASTO/04. Artificial Selection.mp3": 	"Combat Panic",
	"sfx/Music/CosmosASTO/10. Theory of Evolution.mp3": 	"Combat Panic",
        "sfx/Music/MainMenu/IWar.mp3": 	"Combat Neutral",
	"sfx/Music/MainMenu/Kelvin.mp3": 	"Combat Neutral",
	"sfx/Music/MainMenu/Ressikan Flute.mp3": 	"Combat Neutral",
	"sfx/Music/CosmosASTO/01-Vangelis-Heaven & Hell, Pt. 1.mp3": 	"Combat Neutral",
	"sfx/Music/CosmosASTO/13-Vangelis-Comet 16.mp3": 	"Combat Neutral",
	"sfx/Music/CosmosASTO/06-Pachelbel (James Galway)-The Pachelbel Canon.mp3": 	"Combat Neutral",
	"sfx/Music/CosmosASTO/05. Multiverse.mp3": 	"Combat Neutral",
	"sfx/Music/CosmosASTO/11. Chance Nature of Existence.mp3": 	"Combat Neutral",
	"sfx/Music/CosmosASTO/13. Titan.mp3": 	"Combat Neutral",
	"sfx/Music/MainMenu/Default.mp3": 	"Combat Confident",
	"sfx/Music/CosmosASTO/05-Mozart (Mostly Mozart Orchestra)-Clarinet Concerto A Major - K.622.mp3": 	"Combat Confident",
	"sfx/Music/CosmosASTO/11-Godfrey Finger (Leipziger Bach-Collegium)-Sonata D-Dur Fur Trompete, Oboe, und Basso Continuo.mp3": 	"Combat Confident",
	"sfx/Music/CosmosASTO/15-Rimsky-Korsakov (Seattle Symphony)-Russian Easter Festival Overture.mp3": 	"Combat Confident",
	"sfx/Music/CosmosASTO/02. 'Come With Me'.mp3": 	"Combat Confident",
	"sfx/Music/CosmosASTO/03. 'The Cosmos Is Yours'.mp3": 	"Combat Confident",
	"sfx/Music/CosmosASTO/09. The Staggering Immensity of Time.mp3": 	"Combat Confident",
	"sfx/Music/CosmosASTO/13. 'Our Journey Is Just Beginning'.mp3": 	"Combat Confident",
	"sfx/Music/CosmosASTO/13. Cosmos A Spacetime Odyssey - DVD End Credits.mp3": 	"Combat Confident",
}
"""

CosmosASTO.music.dStates = {
	'Combat Confident': ( 'Confident-11a', 'Confident-11b', 'Confident-11c', 'Confident-11d', 'Confident-11e', 'Confident-11f', 'Confident-11g', 'Confident-11h', 'Confident-11i' ),
	'Combat Failure': ( 'Lose', 'PlayerBlewUp' ),
	'Combat Neutral': ( 'Neutral-10a', 'Neutral-10b', 'Neutral-10c', 'Neutral-10d', 'Neutral-10e', 'Neutral-10f', 'Neutral-10g', 'Neutral-10h', 'Neutral-10i' ),
	'Combat Panic': ( 'Panic-9a', 'Panic-9b', 'Panic-9c', 'Panic-9d', 'Panic-9e', 'Panic-9f', 'Panic-9g', 'Panic-9h', 'Panic-9i' ),
	
}

#myMusic = CosmosASTO.music.GetMusic() # TO-DO try to fix the music issue

#import DynamicMusic

#CosmosASTO.music.ChangeMusic(DynamicMusic.pStateMachine)

#def SetCosmosASTOMusic():
#	for key in CosmosASTO.music.dMain.keys():
#		val = dKMMusic[key]
#		delete_item(MusicDef.default.dMain, val)
#		MusicDef.default.dMain[key] = val


# collection of available titles
dict_musics = {}
dict_musics[0] = "sfx/Music/CosmosASTO/AAAE-Cosmos Main Title.mp3"
#dict_musics[1] = "sfx/Music/CosmosASTO/AAAF-S.O.T.I..mp3"
#dict_musics[2] = "sfx/Music/CosmosASTO/AAAG-Billion Years of Evolution.mp3"


def delete_item(my_dict, my_item):
        for i in my_dict.keys():
                if my_dict[i] == my_item:
                        del my_dict[i]

# and get a random music
#def GrabRandomAmbient():
#	MusicMain = CosmosASTO.music.dMain
#
#	# delete old first
#	delete_item(MusicMain, "Starting Ambient")
#        
#	my_ambient_num = App.g_kSystemWrapper.GetRandomNumber(len(dict_musics))
#	my_ambient = dict_musics[my_ambient_num]
#	MusicMain[my_ambient] = "Starting Ambient"

# change Ambient
#GrabRandomAmbient()

"""
def init():  # Verify it's a CosmosASTO
                pGame	        = App.Game_GetCurrentGame()
                pEpisode	= pGame.GetCurrentEpisode()
                pMission	= pEpisode.GetCurrentMission()

                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SET_PLAYER, pMission, __name__ + ".PureCosmosASTOCheck")

def PureCosmosASTOCheck(pObject = None, pEvent = None):
                debug(__name__ + ", NewPlayerButtonCheck")
                global LastShipType
                pGame           = App.Game_GetCurrentGame()
                pEpisode        = pGame.GetCurrentEpisode()
                pMission        = pEpisode.GetCurrentMission()
                pPlayer	        = MissionLib.GetPlayer()             

                # Check if we are CosmosASTO. If not, return to normal music.
                if (GetRaceFromShip(pPlayer) == "CosmosASTO") or (GetShipType(pPlayer) == "SOTI"):

                        print "CosmosASTO"
                else:
                        print "Not a CosmosASTO"

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

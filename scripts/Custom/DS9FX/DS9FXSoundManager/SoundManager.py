# by Sov

# Imports
import App
import DynamicMusic
import GameSoundList
import UMMMenuSoundList
import StandardMusicList

# Functions
def RegisterDS9FXSounds():
    dSounds = GameSoundList.GetSounds()
    for key, value in dSounds.items():
            pSound = App.TGSound_Create(str(value), str(key), 0)
            pSound.SetSFX(0) 
            pSound.SetInterface(1)
            pSound.SetPriority(1.0)

    dMusic = StandardMusicList.GetMusic()
    for key, value in dMusic.items():
        App.g_kMusicManager.LoadMusic(str(value), str(key), 2.0)
        DynamicMusic.dsMusicTypes[str(key)] = str(key)

def RegisterDS9FXUMMSounds():
    dSounds = UMMMenuSoundList.GetSounds()
    for key, value in dSounds.items():
            pSound = App.TGSound_Create(str(value), str(key), 0)
            pSound.SetSFX(0) 
            pSound.SetInterface(1)
            pSound.SetPriority(1.0) 

def UnloadDS9FXSounds():
    dSounds = GameSoundList.GetSounds()
    for key in dSounds.keys():
        try:
            App.g_kSoundManager.DeleteSound(str(key))
        except:
            pass

    dMusic = StandardMusicList.GetMusic()
    for key in dMusic.keys():
        try:
            App.g_kMusicManager.UnloadMusic(str(key))
        except:
            pass

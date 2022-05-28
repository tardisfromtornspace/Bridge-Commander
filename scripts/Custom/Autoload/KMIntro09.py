from bcdebug import debug
INTRO_KMOLD="data/Movies/KobMaruIntro.bik"

try:
        pMod = __import__("MainMenu.mainmenu")
        lIntroVideos = pMod.lIntroVideos

        lIntroVideos.append(INTRO_KMOLD)
except:
        pass

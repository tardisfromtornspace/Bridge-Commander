# This should make the MVAM Inifnite working in QBR and with changing ships
# the try-catch exception needs to be there and makes sure that the game doesn't fail when we don't have the mvam.

import MissionLib    
    
def Restart():
        try:
                import Custom.Sneaker.Mvam.SneakerXOMenuHandlers
        except:
                return
        pPlayer = MissionLib.GetPlayer()
        Custom.Sneaker.Mvam.SneakerXOMenuHandlers.SneakerCreateMenu(pPlayer.GetScript())

def Initialize(pMission):
    Restart()
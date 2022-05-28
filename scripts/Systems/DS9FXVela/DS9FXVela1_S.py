import App
from Custom.DS9FX.DS9FXPulsarFX import PulsarFX

def Initialize(pSet):  
    pSun = App.Sun_Create(2000.0, 2000.0, 2000.0, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
    pSet.AddObjectToSet(pSun, "Vela")

    pSun.PlaceObjectByName( "Sun" )
    pSun.UpdateNodeOnly()
    
    PulsarFX.Create(pSet, pSun, "FlashPosition", "SunBeamPosition", "Blue", 100000.0, -0.135, 70.0, 110.0, "DS9FXVelaPulsar", 0.05, 1, "WhiteLensFlare", 0.2, 0.2, 200000, 500)
    

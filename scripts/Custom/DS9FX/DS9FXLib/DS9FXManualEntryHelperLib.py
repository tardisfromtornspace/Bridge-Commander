# Code completly redesigned... WTH was I thinking... :S

# by USS Sovereign

import App
import DS9FXMenuLib
import MissionLib

Scale = 4.0
deductValue = 0.050

def StartScaling():
        global Scale
        Scale = 4.0

        PlaySound()
        ScaleWormhole(None, None)

def PlaySound():
        App.g_kSoundManager.PlaySound("DS9FXWormClose")

def ScaleWormhole(pObject, pEvent):
        global Scale

        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
                return 0

        pSet = pPlayer.GetContainingSet()

        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)

        Scale = Scale - deductValue

        if Scale <= 0.1:        
                pDS9FXWormhole.SetScale(0.01)
                pDS9FXWormhole.SetHidden(1)

                from Custom.DS9FX.DS9FXWormholeFlash.DS9FXExitWormholeFlash import StartGFX, CreateGFX       
                StartGFX()
                for i in range(1):
                        CreateGFX(pDS9FXWormhole)

                Scale = 4.0

        else:
                pDS9FXWormhole.SetScale(Scale)

                MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".ScaleWormhole", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)


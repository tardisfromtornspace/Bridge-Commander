# Intercept and set DS9FX values properly, mainly DS9FX uses Foundation Player Created Event for "mission" restart and MVAM breaks this.

# by Sov

import App

try:
        from Custom.Sneaker.Mvam import Seperation
        from Custom.Sneaker.Mvam import Reintegration
        Sep = Seperation.Seperation
        Rein = Reintegration.Reintegration
        CP = Reintegration.ChangePlayer
        bMVAM = 1        
except:
        bMVAM = 0

if bMVAM:
        def SeperationIntercept(snkMvamModule, strShip):
                try:
                        from Custom.DS9FX import DS9FXMutatorFunctions
                        DS9FXMutatorFunctions.bMVAM = 1
                except:
                        pass

                Sep(snkMvamModule, strShip)

                return 0

        def ReintegrationIntercept(snkMvamModule):
                try:
                        from Custom.DS9FX import DS9FXMutatorFunctions
                        DS9FXMutatorFunctions.bMVAM = 1
                except:
                        pass

                Rein(snkMvamModule)

                return 0               
        
        def ChangePlayerIntercept(pAction, snkMvamModule, pPlayerJunk, pMvamShips):
                try:
                        from Custom.DS9FX import DS9FXMutatorFunctions
                        DS9FXMutatorFunctions.bMVAM = 1
                except:
                        pass
                CP(pAction, snkMvamModule, pPlayerJunk, pMvamShips)
                
                return 0

        class MVAMIntercept:
                def __init__(self):
                        Seperation.Seperation = SeperationIntercept
                        Reintegration.Reintegration = ReintegrationIntercept
                        Reintegration.ChangePlayer = ChangePlayerIntercept

        InterceptMVAM = MVAMIntercept()
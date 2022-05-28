# This script will intercept the MVAM functions and attach an event onto it so that life support can do its job

# by Sov

import App

try:
        from Custom.Sneaker.Mvam import Hardpoints
        HPSep = Hardpoints.HardpointsSep
        HPRein = Hardpoints.HardpointsRein
        HPTemp = Hardpoints.HardpointsTemp
        bMVAM = 1
except:
        bMVAM = 0

if bMVAM:
        def HardpointsSep(pPlayerOriginal, pPlayer, pMvamShips):
                lShips = pMvamShips[:]
                lShips.append(pPlayer)
                iLen = len(lShips)
                for i in range(iLen):
                        iCount = iLen - i
                        try:
                                pShip = lShips[i]
                                # Fire the event
                                from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents
                                DS9FXGlobalEvents.Trigger_MVAM_Sep(pPlayerOriginal, pShip, iCount)
                        except:
                                pass

                HPSep(pPlayerOriginal, pPlayer, pMvamShips)

                return

        def HardpointsRein(pPlayerOriginal, pPlayer, pMvamShips):
                lShips = pMvamShips[:]
                lShips.append(pPlayer)
                iLen = len(lShips)          
                for i in range(iLen): 
                        if i == 0:
                                bReset = 1
                        else:
                                bReset = 0
                        try:
                                pShip = lShips[i]
                                # Fire the event
                                from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents
                                DS9FXGlobalEvents.Trigger_MVAM_Rein(pShip, pPlayerOriginal, bReset)
                        except:
                                pass

                HPRein(pPlayerOriginal, pPlayer, pMvamShips)

                return
        
        def HardpointsTemp (pShip1, pShip2):
                bReset = 1
                try:
                        from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents
                        DS9FXGlobalEvents.Trigger_MVAM_Rein(pShip2, pShip1, bReset)    
                except:
                        pass
                
                HPTemp(pShip1, pShip2)
                        
                return 

        class MVAMIntercept:
                def __init__(self):
                        Hardpoints.HardpointsSep = HardpointsSep
                        Hardpoints.HardpointsRein = HardpointsRein
                        Hardpoints.HardpointsTemp = HardpointsTemp

        InterceptMVAM = MVAMIntercept()
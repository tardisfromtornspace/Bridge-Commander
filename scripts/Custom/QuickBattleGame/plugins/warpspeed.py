##############################################################
#   From now on a generic plugin for CWS 1.0 & CWS 2.0       #
#                                                            #
#   by USS Sovereign                                         #
#                                                            #
#   License: It's a part of Change Warp Speed mod.           #              
##############################################################

import MissionLib
    
def Restart():
        try:
                import Custom.NanoFXv2.WarpFX.WarpFX_GUI

        except:
                print "CWS 2.0: Why am I still here on your computer?! Delete me... my name is: warpspeed.py & pyc"
                return

        pPlayer = MissionLib.GetPlayer()

        Custom.NanoFXv2.WarpFX.WarpFX_GUI.SetupWarpSpeedButtons(pPlayer.GetScript())

        Custom.NanoFXv2.WarpFX.WarpFX_GUI.ResetWarpSpeed()
        

def Initialize(pMission):
    Restart()

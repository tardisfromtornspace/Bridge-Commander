# This will resolve few game crashes caused by CWS, Slipstream and Hyperdrive

# by Sov

import App

TRUE = 1
FALSE = 0

bEnabled = TRUE

try:
    from Custom.Autoload import SovNFX2Fix
    bCWS = TRUE
except:
    bCWS = FALSE
try:
    from Custom.Autoload import zzzHyperdrive
    bHyper = TRUE
except:
    bHyper = FALSE
try:
    from Custom.Autoload import zzzSlipstreamMode
    bSlip = TRUE
except:
    bSlip = FALSE

if bCWS == TRUE:
    def exiting(pObject, pEvent):
        pMainWindow = App.TopWindow_GetTopWindow().FindMainWindow(App.MWT_OPTIONS)
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_EXIT_GAME, pMainWindow, __name__ + ".KillCWSProperly")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_EXIT_GAME, pMainWindow, __name__ + ".KillCWSProperly")

    def KillCWSProperly(pObject, pEvent):
        from Custom.NanoFXv2.WarpFX import WarpFX_GUI
        warp = WarpFX_GUI

        if warp.pWindow:
            warp.pWindow.KillChildren()
            pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
            pTCW.DeleteChild(warp.pWindow)
            warp.pWindow = None

        if pObject and pEvent:
            pObject.CallNextHandler(pEvent)

    class CWSFix:
        def __init__(self):
            self.bOn = bEnabled
            if self.bOn == 1:
                self.__funcoverride__()

        def __funcoverride__(self):
            from Custom.NanoFXv2.WarpFX import WarpFX_GUI
            warp = WarpFX_GUI
            warp.exiting = exiting

    CWS = CWSFix()

if bHyper == TRUE:
    def quitting():                
        pMainWindow = App.TopWindow_GetTopWindow().FindMainWindow(App.MWT_OPTIONS)
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_EXIT_GAME, pMainWindow, __name__ + ".KillHyperdriveProperly")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_EXIT_GAME, pMainWindow, __name__ + ".KillHyperdriveProperly")

    def KillHyperdriveProperly(pObject, pEvent):
        from Custom.Hyperdrive import HyperdriveModule
        Hyper = HyperdriveModule

        if not Hyper.pSupported == 1:
            return

        pGame = App.Game_GetCurrentGame()
        if pGame == None:
            return
        pEpisode = pGame.GetCurrentEpisode()
        if pEpisode == None:
            return
        pMission = pEpisode.GetCurrentMission()
        if pMission == None:
            return

        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_SET_COURSE, pMission, "Custom.Hyperdrive.HyperdriveModule.CourseSet")
        except:
            pass
        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, "Custom.Hyperdrive.HyperdriveModule.FixDarkScreen")
        except:
            pass
        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_DESTROYED, pMission, "Custom.Hyperdrive.HyperdriveModule.FixDarkScreenExplosions")
        except:
            pass
        try:
            App.g_kEventManager.RemoveBroadcastHandler(Hyper.ET_ENGAGE, pMission, "Custom.Hyperdrive.HyperdriveModule.HyperdriveStats")
        except:
            pass
        try:
            App.g_kEventManager.RemoveBroadcastHandler(Hyper.ET_UPDATE_SLIDER, pMission, "Custom.Hyperdrive.HyperdriveModule.UpdateSlider")
        except:
            pass
        try:
            App.g_kEventManager.RemoveBroadcastHandler(Hyper.ET_REFRESH, pMission, "Custom.Hyperdrive.HyperdriveModule.UpdateStats")
        except:
            pass
        try:
            App.g_kEventManager.RemoveBroadcastHandler(Hyper.ET_CLOSE, pMission, "Custom.Hyperdrive.HyperdriveModule.CloseGUI")
        except:
            pass

        if not Hyper.pPane == None:
            # Let's not cause any crashes
            pTCW = App.TacticalControlWindow_GetTacticalControlWindow()

            try:
                # Just destroy the window, we don't need it anymore.
                App.g_kFocusManager.RemoveAllObjectsUnder(Hyper.pPane)

                pTCW.DeleteChild(Hyper.pPane)

                Hyper.pPane = None

            except:
                pass

        if pObject and pEvent:
            pObject.CallNextHandler(pEvent)

    class HypFix:
        def __init__(self):
            self.bOn = bEnabled
            if self.bOn == 1:
                self.__funcoverride__()

        def __funcoverride__(self):
            from Custom.Hyperdrive import HyperdriveModule
            Hyper = HyperdriveModule
            Hyper.quitting = quitting

    Hyp = HypFix()

if bSlip == TRUE:
    def quitting():                
        pMainWindow = App.TopWindow_GetTopWindow().FindMainWindow(App.MWT_OPTIONS)
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_EXIT_GAME, pMainWindow, __name__ + ".KillSlipstreamProperly")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_EXIT_GAME, pMainWindow, __name__ + ".KillSlipstreamProperly")

    def KillSlipstreamProperly(pObject, pEvent):
        from Custom.Slipstream import SlipstreamModule
        Slip = SlipstreamModule

        if not Slip.pSupported == 1:
            return

        pGame = App.Game_GetCurrentGame()
        if pGame == None:
            return
        pEpisode = pGame.GetCurrentEpisode()
        if pEpisode == None:
            return
        pMission = pEpisode.GetCurrentMission()
        if pMission == None:
            return

        try:
            App.g_kSoundManager.StopSound("SlipstreamEngineSound")
        except:
            pass
        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_SET_COURSE, pMission, "Custom.Slipstream.SlipstreamModule.CourseSet")
        except:
            pass
        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, "Custom.Slipstream.SlipstreamModule.FixDarkScreen")
        except:
            pass
        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_DESTROYED, pMission, "Custom.Slipstream.SlipstreamModule.FixDarkScreenExplosions")
        except:
            pass
        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_MOUSE, pMission, "Custom.Slipstream.SlipstreamModule.MoveNavpoint")
        except:
            pass
        try:
            App.g_kEventManager.RemoveBroadcastHandler(Slip.ET_ENGAGE, pMission, "Custom.Slipstream.SlipstreamModule.SlipstreamStats")
        except:
            pass
        try:
            App.g_kEventManager.RemoveBroadcastHandler(Slip.ET_UPDATE_SLIDER, pMission, "Custom.Slipstream.SlipstreamModule.UpdateSlider")
        except:
            pass
        try:
            App.g_kEventManager.RemoveBroadcastHandler(Slip.ET_REFRESH, pMission, "Custom.Slipstream.SlipstreamModule.UpdateStats")
        except:
            pass
        try:
            App.g_kEventManager.RemoveBroadcastHandler(Slip.ET_CLOSE, pMission, "Custom.Slipstream.SlipstreamModule.CloseGUI")
        except:
            pass

        if not Slip.pPane == None:
            # Let's not cause any crashes
            pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
            try:
                # Just destroy the window, we don't need it anymore.
                App.g_kFocusManager.RemoveAllObjectsUnder(Slip.pPane)

                pTCW.DeleteChild(Slip.pPane)

                Slip.pPane = None

            except:
                pass

        if pObject and pEvent:
            pObject.CallNextHandler(pEvent)

    class SlipFix:
        def __init__(self):
            self.bOn = bEnabled
            if self.bOn == 1:
                self.__funcoverride__()

        def __funcoverride__(self):
            from Custom.Slipstream import SlipstreamModule
            Slip = SlipstreamModule
            Slip.quitting = quitting

    Slip = SlipFix()

if bCWS == TRUE or bHyper == TRUE or bSlip == TRUE:
    print "Fixing\Enhancing USS Sovereign's mods..."

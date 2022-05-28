# Small easter egg

# by Smbw

import App
import MissionLib
import DS9FXPrintTextLib
import DS9FXMirrorUniverse
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

iPlayerResized = 0
bNebulaCreated = 0
bPlayerInNebula = 0
ResizeTime = None

def SetupCheck():
        bInMission = DS9FXMirrorUniverse.bInMission
        if bInMission:
                return

        reload(DS9FXSavedConfig)
        if not DS9FXSavedConfig.EasterEggs == 1:
                return        

        Create_Nebula()

def Create_Nebula(pObject = None, pEvent = None):
        global bNebulaCreated, bPlayerInNebula

        if int(App.g_kSystemWrapper.GetRandomNumber(100) + 1) < 85:
                return 0

        if bNebulaCreated != 0:
                return 0

        pPlayer = App.Game_GetCurrentPlayer()
        if not pPlayer:
                return 0

        curSet = pPlayer.GetContainingSet()
        if not curSet:
                return 0

        RegionModule = curSet.GetRegionModule()
        if not RegionModule:
                return 0

        if str(RegionModule) != "Systems.DeepSpace9.DeepSpace91":
                return 0

        pSet = App.g_kSetManager.GetSet("DeepSpace91")
        if not pSet:
                return 0

        # (r, g, b, density, sensor range, inner texture, outer texture)
        pNebula = App.MetaNebula_Create(155.0 / 255.0, 90.0 / 255.0, 185.0 / 255.0, 145.0, 10.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
        if not pNebula:
                return 0

        pNebula.SetTranslateXYZ(0, 0, 0)

        # (x, y, z, size)
        x = App.g_kSystemWrapper.GetRandomNumber(1500) + 100
        y = App.g_kSystemWrapper.GetRandomNumber(1500) + 100
        z = App.g_kSystemWrapper.GetRandomNumber(1500) + 100
        s = float(App.g_kSystemWrapper.GetRandomNumber(80) + 20)

        pNebula.AddNebulaSphere(x, y, z, s)
        pSet.AddObjectToSet(pNebula, "Unknown Nebula")
        bNebulaCreated = 1

        pNavPoint = App.Waypoint_Create("Unknown Anomaly", "DeepSpace91", None)
        pNavPoint.SetStatic(1)
        pNavPoint.SetNavPoint(1)
        pNavPoint.SetTranslateXYZ(x, y, z)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.0, 1.0, 0.0)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.0, 0.0, 1.0)
        pNavPoint.AlignToVectors(kForward, kUp)
        pNavPoint.Update(0)

        pPlayer.SetTarget("Unknown Anomaly")
        ShowMessage(2)

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()

        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_NEBULA, pMission, __name__ + ".Entered_Nebula")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_EXITED_NEBULA, pMission, __name__ + ".Exited_Nebula")
        bPlayerInNebula = 0


def Remove_Nebula():
        global bNebulaCreated

        if bNebulaCreated == 0:
                return 0

        try:

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()

                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_NEBULA, pMission, __name__ + ".Entered_Nebula")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_EXITED_NEBULA, pMission, __name__ + ".Exited_Nebula")

        except:
                pass

        pSet = App.g_kSetManager.GetSet("DeepSpace91")
        if pSet:
                try:
                        pSet.DeleteObjectFromSet("Unknown Nebula")
                        pSet.DeleteObjectFromSet("Unknown Anomaly")
                except:
                        pass

        bNebulaCreated = 0
        iPlayerResized = 0
        bPlayerInNebula = 0


def Entered_Nebula(pObject, pEvent):
        global bPlayerInNebula

        pPlayer = App.Game_GetCurrentPlayer()
        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        pNebula = App.Nebula_Cast(pEvent.GetSource())

        if pPlayer and pShip:
                if pShip.GetObjID() == pPlayer.GetObjID():
                        if bPlayerInNebula != 1 and pNebula.GetName() == "Unknown Nebula":

                                bPlayerInNebula = 1
                                ChangePlayerSize()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)


def Exited_Nebula(pObject, pEvent):
        global bPlayerInNebula, iPlayerResized

        pPlayer = App.Game_GetCurrentPlayer()
        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        pNebula = App.Nebula_Cast(pEvent.GetSource())

        if pPlayer and pShip:
                if pShip.GetObjID() == pPlayer.GetObjID():
                        if bPlayerInNebula != 0 and pNebula.GetName() == "Unknown Nebula":

                                bPlayerInNebula = 0
                                if (iPlayerResized % 2) == 0 and iPlayerResized >= 2:
                                        Remove_Nebula()

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)


def ChangePlayerSize():
        global iPlayerResized, ResizeTime

        pPlayer = App.Game_GetCurrentPlayer()
        if not pPlayer:
                return 0

        pImpulseProp = pPlayer.GetImpulseEngineSubsystem().GetProperty()
        if pImpulseProp:
                MaxSpeed = pImpulseProp.GetMaxSpeed()
                MaxAccel = pImpulseProp.GetMaxAccel()

        if (iPlayerResized % 2) == 1:
                if (App.g_kUtopiaModule.GetGameTime() - 90.0) < ResizeTime:
                        return 0

                if pImpulseProp:
                        pImpulseProp.SetMaxSpeed(MaxSpeed / 25.0)
                        pImpulseProp.SetMaxAccel(MaxAccel / 25.0)

                pPlayer.SetScale(1.0)
                ShowMessage(0)

        else:
                if pImpulseProp:
                        pImpulseProp.SetMaxSpeed(MaxSpeed * 25.0)
                        pImpulseProp.SetMaxAccel(MaxAccel * 25.0)

                pPlayer.SetScale(0.015)
                ResizeTime = App.g_kUtopiaModule.GetGameTime()
                ShowMessage(1)

        iPlayerResized = iPlayerResized + 1

def ShowMessage(iMsg):
        if iMsg == 1:
                sText = "The Nebula seems to have shrunk us sir!\nLOL WOW COOL!!!\nPerhaps we should exit and re-enter it to resize ourselves."
        elif iMsg == 2:
                sText = "We have detected an unknown anomaly sir..."		
        else:
                sText = "The Nebula is nothing but trouble. But we are at least back to normal size."

        iPos = 6
        iFont = 12
        iDur = 12
        iDelay = 10
        DS9FXPrintTextLib.PrintText(sText, iPos, iFont, iDur, iDelay)
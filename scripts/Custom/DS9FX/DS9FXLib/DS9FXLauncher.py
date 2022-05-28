# This launches fighters from DS9

# by Sov

# Imports
import App
import MissionLib
import loadspacehelper
from Custom.DS9FX.DS9FXAILib import DS9FXGenericStaticEnemyAI, DS9FXGenericStaticFriendlyAI
from Custom.DS9FX.DS9FXLib import DS9FXShips, DS9FXLifeSupportLib

# Ship name
lNames = ["Verde", "Guadiana", "Lankin", "Maroni", "Kuban", "Paraguay", "Tigris"]

# Functions
def LaunchFriendly():
        DS9 = __import__("Systems.DeepSpace9.DeepSpace91")   
        DS9Set = DS9.GetSet()

        pCount = GetRnd(6, 1)

        for i in range(pCount):
                sName = lNames[i]

                pType = GetRnd(98, 1)
                if pType <= 33:
                        loadspacehelper.CreateShip(DS9FXShips.Danube1, DS9Set, sName, "", 0, 1)
                elif pType > 33 and pType <= 66:
                        loadspacehelper.CreateShip(DS9FXShips.Danube2, DS9Set, sName, "", 0, 1)
                else:
                        loadspacehelper.CreateShip(DS9FXShips.Peregrine, DS9Set, sName, "", 0, 1)

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(sName)
                pMission.GetFriendlyGroup().AddName(sName)

                pShip = MissionLib.GetShip(sName, DS9Set)
                pShip.SetCollisionsOn(0)

                pDS9 = MissionLib.GetShip("Deep_Space_9")

                pPosition = pDS9.GetWorldLocation()
                pForward = pDS9.GetWorldForwardTG()
                pUp = pDS9.GetWorldUpTG()

                pShip.AlignToVectors(pForward, pUp)
                pShip.SetTranslate(pPosition)
                pShip.UpdateNodeOnly()

                pShip.ClearAI()
                pShip = App.ShipClass_Cast(pShip)
                pShip.SetAI(DS9FXGenericStaticFriendlyAI.CreateAI(pShip))

def LaunchEnemy():
        DS9 = __import__("Systems.DeepSpace9.DeepSpace91")   
        DS9Set = DS9.GetSet()

        pCount = GetRnd(6, 1)

        for i in range(pCount):
                sName = lNames[i]

                pType = GetRnd(98, 1)
                if pType <= 33:
                        loadspacehelper.CreateShip(DS9FXShips.Danube1, DS9Set, sName, "", 0, 1)
                elif pType > 33 and pType <= 66:
                        loadspacehelper.CreateShip(DS9FXShips.Danube2, DS9Set, sName, "", 0, 1)
                else:
                        loadspacehelper.CreateShip(DS9FXShips.Peregrine, DS9Set, sName, "", 0, 1)

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(sName)
                pMission.GetEnemyGroup().AddName(sName)

                pShip = MissionLib.GetShip(sName, DS9Set)
                pShip.SetCollisionsOn(0)

                pDS9 = MissionLib.GetShip("Deep_Space_9")

                pPosition = pDS9.GetWorldLocation()
                pForward = pDS9.GetWorldForwardTG()
                pUp = pDS9.GetWorldUpTG()

                pShip.AlignToVectors(pForward, pUp)
                pShip.SetTranslate(pPosition)
                pShip.UpdateNodeOnly()

                pShip.ClearAI()
                pShip = App.ShipClass_Cast(pShip)
                pShip.SetAI(DS9FXGenericStaticEnemyAI.CreateAI(pShip))

def GetRnd(iRnd, iStatic):
        return App.g_kSystemWrapper.GetRandomNumber(iRnd) + iStatic 

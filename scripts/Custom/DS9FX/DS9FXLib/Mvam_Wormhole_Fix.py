# Deactivate MVAM in the wormhole

# by Smbw

# Revised by Sov

import App
import Bridge.BridgeUtils
try:
        from Custom.Sneaker.Mvam import Seperation, AiSeperation, Reintegration
        bInstalled = 1
except:
        bInstalled = 0

fiSeperation = None
fiAISeperation = None
fiReintegration = None

def MissionStart():
        global fiSeperation, fiAISeperation, fiReintegration, bInstalled

        if not bInstalled:
                return

        fiSeperation = Seperation.Seperation
        fiAISeperation = AiSeperation.Seperation
        fiReintegration = Reintegration.Reintegration

def Deactivate():
        global bInstalled

        if not bInstalled:
                return

        Seperation.Seperation = SeperationReplacement
        AiSeperation.Seperation = AISeperationReplacement
        Reintegration.Reintegration = ReintegrationReplacement

        pMenu = Bridge.BridgeUtils.GetBridgeMenu("XO")
        if pMenu:
                pMVAMMenu = pMenu.GetSubmenuW(App.TGString("MVAM Menu"))
                if pMVAMMenu:
                        for i in xrange(pMVAMMenu.GetNumChildren()):
                                pChild = pMVAMMenu.GetNthChild(i)
                                pButton = App.STButton_Cast(pChild)
                                if pButton:
                                        pButton.SetDisabled()

def Reactivate():
        global bInstalled

        if not bInstalled:
                return

        Seperation.Seperation = fiSeperation
        AiSeperation.Seperation = fiAISeperation
        Reintegration.Reintegration = fiReintegration

        pMenu = Bridge.BridgeUtils.GetBridgeMenu("XO")
        if pMenu:
                pMVAMMenu = pMenu.GetSubmenuW(App.TGString("MVAM Menu"))
                if pMVAMMenu:
                        for i in xrange(pMVAMMenu.GetNumChildren()):
                                pChild = pMVAMMenu.GetNthChild(i)
                                pButton = App.STButton_Cast(pChild)
                                if pButton:
                                        pButton.SetEnabled()

def SeperationReplacement(snkMvamModule = None, strShip = None):
        return None

def AISeperationReplacement(snkMvamModule, straShipInfo):
        return None

def ReintegrationReplacement(snkMvamModule = None):
        return None

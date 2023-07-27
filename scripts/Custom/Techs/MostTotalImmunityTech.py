
import App
import FoundationTech
from ftb.Tech.ATPFunctions import *
import time
import string


class TotalTorpeDef(FoundationTech.TechDef):

    def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
            return 1

    def Attach(self, pInstance):
        pInstance.lTorpDefense.append(self)


oTotalTorpeImmunity = TotalTorpeDef('Total Immunity')

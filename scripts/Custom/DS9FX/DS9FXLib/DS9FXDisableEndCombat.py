# Disables End Combat button when you are in a set which is not registered to the foundation, otherwise game crashes

import MissionLib
import DS9FXMenuLib

lSets = ["BajoranWormhole1", "GammaQuadrant1", "DS9FXKaremma1", 
         "DS9FXDosi1", "DS9FXYadera1", "DS9FXNewBajor1", "DS9FXGaia1", 
         "DS9FXKurill1", "DS9FXTrialus1", "DS9FXTRogoran1","DS9FXVandros1", 
         "DS9FXFoundersHomeworld1"]

def EvalCondition():
        pPlayer = MissionLib.GetPlayer()
        if not pPlayer:
                return

        pSet = pPlayer.GetContainingSet()
        if not pSet:
                return

        if pSet.GetName() in lSets:
                KillEndCombatButton()
        else:
                RestoreEndCombatButton()

def KillEndCombatButton():
        try:
                pEnd = DS9FXMenuLib.GetButton("End Combat", "XO")
                pRestart = DS9FXMenuLib.GetButton("Restart Combat", "XO")
                if pEnd and not pRestart.IsEnabled():
                        pEnd.SetDisabled()
        except:
                return 

def RestoreEndCombatButton():
        try:
                pEnd = DS9FXMenuLib.GetButton("End Combat", "XO")
                pRestart = DS9FXMenuLib.GetButton("Restart Combat", "XO")
                if pEnd and not pRestart.IsEnabled():
                        pEnd.SetEnabled()
        except:
                return


from bcdebug import debug
# Ship.py
# March 16, 2002
#
# by sleight42 aka Evan Light, all rights reserved
#
# Permission to redistribute this code as part of any other packaging requires
# the explicit permission of the author in advance.
##############################################################################

import App
import TacticalInterfaceHandlers

class Ship:
    def __init__(self,pShip):
        debug(__name__ + ", __init__")
        self.lSecondaryTargets = []
        self.pShip = pShip

    def __SetSecondaryTargets(self,lTargets):
        debug(__name__ + ", __SetSecondaryTargets")
        self.lSecondaryTargets = lTargets

    def GetSecondaryTargetsRef(self):
        debug(__name__ + ", GetSecondaryTargetsRef")
        return self.lSecondaryTargets

    def GetSecondaryTargets(self):
        debug(__name__ + ", GetSecondaryTargets")
        return self.lSecondaryTargets[:]

    def HasAsSecondaryTarget(self,pShip):
        debug(__name__ + ", HasAsSecondaryTarget")
        retval = 0
        for pTarget in self.lSecondaryTargets:
            if (pShip == pTarget):
                retval = 1
        return retval

    def ToggleSecondaryTarget(self,pShip):
        debug(__name__ + ", ToggleSecondaryTarget")
        if self.HasAsSecondaryTarget(pShip):
            self.lSecondaryTargets.remove(pShip)
        else:
            self.lSecondaryTargets.append(pShip)

    def ClearSecondaryTargets(self):
        #print "Clearing secondaries"
        debug(__name__ + ", ClearSecondaryTargets")
        self.lSecondaryTargets = []

    def FireWeaponsOnList(self, bFiring, eGroup):
        #TacticalInterfaceHandlers.FireWeapons( self.pShip, bFiring, eGroup)
        debug(__name__ + ", FireWeaponsOnList")
        pSystem = self.pShip.GetWeaponSystemGroup( eGroup)
        if (pSystem != None):
            pGame = App.Game_GetCurrentGame()
            if ( bFiring == 1):
                for pTarget in self.lSecondaryTargets:
                    retval = pSystem.StartFiring(pTarget, pTarget.GetTargetOffsetTG())
                    pSystem.SetForceUpdate(1) # update and fire immediately
            else:
                pSystem.StopFiring()

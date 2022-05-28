"""Something I've been meaning to fix anyways

USS Sovereign"""

import App
import Foundation
import string

TRUE = 1
FALSE = 0

# If disabled, replace TRUE with FALSE
bEnabled = TRUE

if int(Foundation.version[0:8]) >= 20030222:
        def SetupOrbitMenuFromSet(pOrbitMenu, pSet):                
                bOpenable = 0

                #debug("Setting up orbit menu from set: " + pSet.GetName())
                pPlayer = App.Game_GetCurrentPlayer()
                pSensors = None
                if pPlayer:
                        pSensors = pPlayer.GetSensorSubsystem()

                # Clear out old entries.
                pOrbitMenu.KillChildren()

                # Look for new entries.
                lPlanets = pSet.GetClassObjectList(App.CT_PLANET)
                if lPlanets:
                        for pPlanet in lPlanets:                        
                                # If this is a sun, skip it.
                                if pPlanet.IsTypeOf(App.CT_SUN):
                                        continue
                                # Suns are excluded, but not the "Class-O Planet"...
                                elif EndsWithStr("Planet", pPlanet.GetName()):
                                        continue
                                # For new DS9FX SunStreak feature
                                elif EndsWithStr("SunStreak", pPlanet.GetName()):
                                        continue
                                # For new DS9FX Pulsar feature
                                elif EndsWithStr("Pulsar", pPlanet.GetName()):
                                        continue                                

                                # Make a new button for this planet.
                                # First create an event for that button.
                                pEvent = App.TGEvent_Create()
                                pEvent.SetEventType(App.ET_ORBIT_PLANET)
                                pEvent.SetSource(pPlanet)
                                pEvent.SetDestination(pOrbitMenu)

                                # Now create the button..
                                #debug("Adding planet \"%s\" to the orbit menu" % (pPlanet.GetName()))
                                pButton = App.STButton_CreateW(pPlanet.GetDisplayName(), pEvent)
                                pOrbitMenu.AddChild(pButton, 0, 0, 0)
                                bOpenable = 1

                                # Make sure this planet is marked as Identified for the player,
                                # so the player can target it.  (All planets are automatically
                                # targetable).
                                if pSensors:
                                        pSensors.ForceObjectIdentified(pPlanet)

                if bOpenable:
                        #debug("Orbit menu is openable.")
                        pOrbitMenu.SetOpenable()
                        pOrbitMenu.SetEnabled()
                else:
                        #debug("Orbit menu is not openable.")
                        pOrbitMenu.SetNotOpenable()
                        pOrbitMenu.SetDisabled()

        def TargetNextPlanet(pObject, pEvent):
                # Get the player, and the player's set.
                pPlayer = App.Game_GetCurrentPlayer()
                if pPlayer:
                        pSet = pPlayer.GetContainingSet()
                        if pSet:
                                # Get the list of planets.
                                lPlanets = list(pSet.GetClassObjectList(App.CT_PLANET))

                                # Remove any suns from the list.  Don't want
                                # to target suns, only planets.
                                for pPlanet in lPlanets[:]:
                                        if pPlanet.IsTypeOf(App.CT_SUN):
                                                lPlanets.remove(pPlanet)

                                        # Suns are excluded, but not the "Class-O Planet"...
                                        elif EndsWithStr("Planet", pPlanet.GetName()):
                                                lPlanets.remove(pPlanet)
                                        # For new DS9FX SunStreak feature
                                        elif EndsWithStr("SunStreak", pPlanet.GetName()):
                                                lPlanets.remove(pPlanet) 
                                        # For new DS9FX Pulsar feature
                                        elif EndsWithStr("Pulsar", pPlanet.GetName()):
                                                lPlanets.remove(pPlanet)                                                  

                                if lPlanets:
                                        iIndex = -1
                                        # Check if the player's current target is
                                        # a planet in this list.
                                        pTarget = App.Planet_Cast(pPlayer.GetTarget())
                                        if pTarget:
                                                iOldIndex = 0
                                                for pPlanet in lPlanets:
                                                        if pTarget.GetObjID() == pPlanet.GetObjID():
                                                                iIndex = iOldIndex
                                                                break
                                                        iOldIndex = iOldIndex + 1

                                        # Target the next planet
                                        iIndex = (iIndex + 1) % len(lPlanets)
                                        pPlayer.SetTarget(lPlanets[iIndex].GetName())

                pObject.CallNextHandler(pEvent)

        # A custom function for BC, since I believe that str.endswith('*') is only available in 2.0 python and up...
        # Not perfect but it does the job
        def EndsWithStr(sToCheck = None, sToCompare = None):
                if sToCheck is None or sToCompare is None:
                        return FALSE

                sToCheck = str(sToCheck)
                sToCompare = str(sToCompare)

                ToCheckindex = len(sToCheck) - 1
                ToCompareindex = len(sToCompare) - 1

                if ToCheckindex <= 0 or ToCompareindex <= 0:
                        return FALSE

                EndsWithindex = string.rfind(sToCompare, sToCheck)
                if (EndsWithindex <= 0):
                        return FALSE

                compIndex = ToCompareindex
                comparisonIndex = EndsWithindex + ToCheckindex

                iResult = compIndex - comparisonIndex

                if (iResult > 0):
                        bEnds = FALSE

                elif (iResult <= 0):
                        bEnds = TRUE
        
                return bEnds

        class FoundationNanoFXNameFix:
                def __init__(self):
                        self.bOn = bEnabled
                        if self.bOn == 1:
                                self.__funcoverride__()

                def __funcoverride__(self):
                        import Bridge.HelmMenuHandlers
                        HMH = Bridge.HelmMenuHandlers
                        HMH.SetupOrbitMenuFromSet = SetupOrbitMenuFromSet

                        import TacticalInterfaceHandlers
                        TIH = TacticalInterfaceHandlers
                        TIH.TargetNextPlanet = TargetNextPlanet

        Foundation.FoundationNanoFXNameFix = FoundationNanoFXNameFix()


# This is a DS9FX related expansion which will inherit 2 functions and add a couple of lines to fire a ship repaired event, this is an addon for life support

# by Sov

import App

try:
        from Actions import ShipScriptActions
        ScriptRepair = ShipScriptActions.RepairShipFully
        bActions = 1
except:
        # If this file doesn't exist, then really something is seriously wrong with your install
        bActions = 0

try:
        from Custom.NanoFXv2.ExplosionFX import GlowFX
        NanoRepair = GlowFX.RepairShipFullyGlowFix
        bNano = 1
except:
        bNano = 0

if bActions:
        def RepairShipFully(pAction, iShipID):   
                ScriptRepair(pAction, iShipID)

                pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(iShipID))
                if pShip is None:
                        return 0

                try:
                        # Fire ship fixed event
                        from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents
                        DS9FXGlobalEvents.Trigger_Repair_Ship(pShip)
                except:
                        pass

                return 0

        class ShipActionsOverride:
                def __init__(self):
                        ShipScriptActions.RepairShipFully = RepairShipFully

        OverrideShipActions = ShipActionsOverride()

if bNano:
        def RepairShipFullyGlowFix(pAction, iShipID):
                NanoRepair(pAction, iShipID)

                pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(iShipID))
                if pShip is None:
                        return 0

                try:
                        # Fire ship fixed event
                        from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents
                        DS9FXGlobalEvents.Trigger_Repair_Ship(pShip)
                except:
                        pass

                return 0

        class GlowFXOverride:
                def __init__(self):
                        GlowFX.RepairShipFullyGlowFix = RepairShipFullyGlowFix

        OverrideGlowFX = GlowFXOverride()

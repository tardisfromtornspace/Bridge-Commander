# by USS Sovereign, 19/04/2006

# Last Modified 04/09/2007


# Imports
import App
import Foundation
import MissionLib
import Custom.Warpspace.WarpspaceModule
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import WarpspaceConfiguration


# Mutator def
mode = Foundation.MutatorDef("Warpspace Drive " + Custom.Warpspace.WarpspaceModule.VERSION)


# Activate handlers
class ActivateWarpspaceHandlers(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                Custom.Warpspace.WarpspaceModule.handlers()

ActivateWarpspaceHandlers('Warpspace Handlers Active', App.ET_MISSION_START, dict = { 'modes': [ mode ] } )


# Load trigger, using ET_FND_CREATE_PLAYER_SHIP event
class LoadWarpspaceFoundationEvent(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                Custom.Warpspace.WarpspaceModule.init()

LoadWarpspaceFoundationEvent('Warpspace Loaded', Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP, dict = { 'modes': [ mode ] } )


# Load trigger, using ET_SET_PLAYER event
# Bad workaround, I know! I need it beceause of transporter like mods.
class LoadWarpspaceAppEvent(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                Custom.Warpspace.WarpspaceModule.init()

LoadWarpspaceAppEvent('Warpspace Loaded', App.ET_SET_PLAYER, dict = { 'modes': [ mode ] } )


# Disable button
class WarpspaceDisableButton(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
                reload(WarpspaceConfiguration)
                if WarpspaceConfiguration.ArrivingAt == 1:
                    import Bridge.HelmMenuHandlers
                    Bridge.HelmMenuHandlers.g_bShowEnteringBanner = 0
                
                # Call the function only if the player is the one triggering it
                pShip = App.ShipClass_Cast(pEvent.GetDestination())
		if pShip is None:
		    return 0
		
		pPlayer = MissionLib.GetPlayer()
		if pPlayer is None:
                    return 0
                
		if pShip.GetName() == pPlayer.GetName(): 
                    Custom.Warpspace.WarpspaceModule.disablebutton()
                else:
                    return 0

WarpspaceDisableButton('Warpspace Disable Button Active', App.ET_ENTERED_SET, dict = { 'modes': [ mode ] } )


# Disable navpoint related stuff
class WarpspaceNavpointDeleted(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
                reload(WarpspaceConfiguration)
                if WarpspaceConfiguration.ArrivingAt == 1:
                    import Bridge.HelmMenuHandlers
                    Bridge.HelmMenuHandlers.g_bShowEnteringBanner = 0
                
                # Call the function only if the player is the one triggering it
                pShip = App.ShipClass_Cast(pEvent.GetDestination())
		if pShip is None:
		    return 0
		
		pPlayer = MissionLib.GetPlayer()
		if pPlayer is None:
                    return 0
                
		if pShip.GetName() == pPlayer.GetName(): 
                    Custom.Warpspace.WarpspaceModule.delnavpoint()
                else:
                    return 0

WarpspaceNavpointDeleted('Warpspace Delete Navpoint Active', App.ET_EXITED_SET, dict = { 'modes': [ mode ] } )


# Quit trigger, using ET_QUIT event
class QuitWarpspace(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                Custom.Warpspace.WarpspaceModule.quitting()

QuitWarpspace('Quitting Warpspace', App.ET_QUIT, dict = { 'modes': [ mode ] } )


# Signalize initialization
print 'Warpspace Drive ' + Custom.Warpspace.WarpspaceModule.VERSION + ' Initializing...'

# by USS Sovereign, 19/04/2006

# Last Modified 04/09/2007


# Imports
import App
import Foundation
import MissionLib
import Custom.Slipstream.SlipstreamModule
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import SlipstreamConfiguration


# Mutator def
mode = Foundation.MutatorDef("Slipstream Drive " + Custom.Slipstream.SlipstreamModule.VERSION)


# Activate handlers
class ActivateSlipstreamHandlers(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                Custom.Slipstream.SlipstreamModule.handlers()

ActivateSlipstreamHandlers('Slipstream Handlers Active', App.ET_MISSION_START, dict = { 'modes': [ mode ] } )


# Load trigger, using ET_FND_CREATE_PLAYER_SHIP event
class LoadSlipstreamFoundationEvent(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                Custom.Slipstream.SlipstreamModule.init()

LoadSlipstreamFoundationEvent('Slipstream Loaded', Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP, dict = { 'modes': [ mode ] } )


# Load trigger, using ET_SET_PLAYER event
# Bad workaround, I know! I need it beceause of transporter like mods.
class LoadSlipstreamAppEvent(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                Custom.Slipstream.SlipstreamModule.init()

LoadSlipstreamAppEvent('Slipstream Loaded', App.ET_SET_PLAYER, dict = { 'modes': [ mode ] } )


# Disable button
class SlipstreamDisableButton(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
                reload(SlipstreamConfiguration)
                if SlipstreamConfiguration.ArrivingAt == 1:
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
                    Custom.Slipstream.SlipstreamModule.disablebutton()
                else:
                    return 0

SlipstreamDisableButton('Slipstream Disable Button Active', App.ET_ENTERED_SET, dict = { 'modes': [ mode ] } )


# Disable navpoint related stuff
class SlipstreamNavpointDeleted(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
                reload(SlipstreamConfiguration)
                if SlipstreamConfiguration.ArrivingAt == 1:
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
                    Custom.Slipstream.SlipstreamModule.delnavpoint()
                else:
                    return 0

SlipstreamNavpointDeleted('Slipstream Delete Navpoint Active', App.ET_EXITED_SET, dict = { 'modes': [ mode ] } )


# Quit trigger, using ET_QUIT event
class QuitSlipstream(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                Custom.Slipstream.SlipstreamModule.quitting()

QuitSlipstream('Quitting Slipstream', App.ET_QUIT, dict = { 'modes': [ mode ] } )


# Signalize initialization
print 'Slipstream Drive ' + Custom.Slipstream.SlipstreamModule.VERSION + ' Initializing...'

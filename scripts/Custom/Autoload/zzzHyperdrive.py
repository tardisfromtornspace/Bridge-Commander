# by USS Sovereign, 19/04/2006

# Last Modified 11/8/2007

# Imports
import App
import Foundation
import Custom.Hyperdrive.HyperdriveModule

# Mutator def
mode = Foundation.MutatorDef("Stargate Hyperdrive")


# Activate handlers
class ActivateHyperdriveHandlers(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                Custom.Hyperdrive.HyperdriveModule.handlers()

ActivateHyperdriveHandlers('Hyperdrive Handlers Active', App.ET_MISSION_START, dict = { 'modes': [ mode ] } )


# Load trigger, using ET_FND_CREATE_PLAYER_SHIP event
class LoadHyperdriveFoundationEvent(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                Custom.Hyperdrive.HyperdriveModule.init()

LoadHyperdriveFoundationEvent('Hyperdrive Loaded', Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP, dict = { 'modes': [ mode ] } )


# Load trigger, using ET_SET_PLAYER event
# Bad workaround, I know! I need it beceause of transporter like mods.
class LoadHyperdriveAppEvent(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                Custom.Hyperdrive.HyperdriveModule.init()

LoadHyperdriveAppEvent('Hyperdrive Loaded', App.ET_SET_PLAYER, dict = { 'modes': [ mode ] } )


# Disable button
class HyperdriveDisableButton(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                Custom.Hyperdrive.HyperdriveModule.disablebutton()

HyperdriveDisableButton('Hyperdrive Disable Button Active', App.ET_ENTERED_SET, dict = { 'modes': [ mode ] } )


# Quit trigger, using ET_QUIT event
class QuitHyperdrive(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                Custom.Hyperdrive.HyperdriveModule.quitting()

QuitHyperdrive('Quitting Hyperdrive', App.ET_QUIT, dict = { 'modes': [ mode ] } )


# Signalize initialization
print 'Stargate Hyperdrive Drive Initializing...'


# by USS Sovereign, 19/04/2006

# Last Modified 04/09/2007


# Imports
import App
import Foundation
import MissionLib
import Custom.TimeVortex.TimeVortexModule
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import TimeVortexConfiguration


# Mutator def
mode = Foundation.MutatorDef("TimeVortex Drive " + Custom.TimeVortex.TimeVortexModule.VERSION)


# Activate handlers
class ActivateTimeVortexHandlers(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                Custom.TimeVortex.TimeVortexModule.handlers()

ActivateTimeVortexHandlers('TimeVortex Handlers Active', App.ET_MISSION_START, dict = { 'modes': [ mode ] } )


# Load trigger, using ET_FND_CREATE_PLAYER_SHIP event
class LoadTimeVortexFoundationEvent(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                Custom.TimeVortex.TimeVortexModule.init()

LoadTimeVortexFoundationEvent('TimeVortex Loaded', Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP, dict = { 'modes': [ mode ] } )


# Load trigger, using ET_SET_PLAYER event
# Bad workaround, I know! I need it beceause of transporter like mods.
class LoadTimeVortexAppEvent(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                Custom.TimeVortex.TimeVortexModule.init()

LoadTimeVortexAppEvent('TimeVortex Loaded', App.ET_SET_PLAYER, dict = { 'modes': [ mode ] } )


# Disable button
class TimeVortexDisableButton(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
                reload(TimeVortexConfiguration)
                if TimeVortexConfiguration.ArrivingAt == 1:
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
                    Custom.TimeVortex.TimeVortexModule.disablebutton()
                else:
                    return 0

TimeVortexDisableButton('TimeVortex Disable Button Active', App.ET_ENTERED_SET, dict = { 'modes': [ mode ] } )


# Disable navpoint related stuff
class TimeVortexNavpointDeleted(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
                reload(TimeVortexConfiguration)
                if TimeVortexConfiguration.ArrivingAt == 1:
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
                    Custom.TimeVortex.TimeVortexModule.delnavpoint()
                else:
                    return 0

TimeVortexNavpointDeleted('TimeVortex Delete Navpoint Active', App.ET_EXITED_SET, dict = { 'modes': [ mode ] } )


# Quit trigger, using ET_QUIT event
class QuitTimeVortex(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                Custom.TimeVortex.TimeVortexModule.quitting()

QuitTimeVortex('Quitting TimeVortex', App.ET_QUIT, dict = { 'modes': [ mode ] } )


# Signalize initialization
print 'TimeVortex Drive ' + Custom.TimeVortex.TimeVortexModule.VERSION + ' Initializing...'

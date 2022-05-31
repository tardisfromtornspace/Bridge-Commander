# by USS Sovereign, 19/04/2006

# Last Modified 04/09/2007


# Imports
import App
import Foundation
import MissionLib
import Custom.Jumpspace.JumpspaceModule
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import JumpspaceConfiguration


# Mutator def
mode = Foundation.MutatorDef("Jumpspace Drive " + Custom.Jumpspace.JumpspaceModule.VERSION)


# Activate handlers
class ActivateJumpspaceHandlers(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                Custom.Jumpspace.JumpspaceModule.handlers()

ActivateJumpspaceHandlers('Jumpspace Handlers Active', App.ET_MISSION_START, dict = { 'modes': [ mode ] } )


# Load trigger, using ET_FND_CREATE_PLAYER_SHIP event
class LoadJumpspaceFoundationEvent(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                Custom.Jumpspace.JumpspaceModule.init()

LoadJumpspaceFoundationEvent('Jumpspace Loaded', Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP, dict = { 'modes': [ mode ] } )


# Load trigger, using ET_SET_PLAYER event
# Bad workaround, I know! I need it beceause of transporter like mods.
class LoadJumpspaceAppEvent(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                Custom.Jumpspace.JumpspaceModule.init()

LoadJumpspaceAppEvent('Jumpspace Loaded', App.ET_SET_PLAYER, dict = { 'modes': [ mode ] } )


# Disable button
class JumpspaceDisableButton(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
                reload(JumpspaceConfiguration)
                if JumpspaceConfiguration.ArrivingAt == 1:
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
                    Custom.Jumpspace.JumpspaceModule.disablebutton()
                else:
                    return 0

JumpspaceDisableButton('Jumpspace Disable Button Active', App.ET_ENTERED_SET, dict = { 'modes': [ mode ] } )


# Disable navpoint related stuff
class JumpspaceNavpointDeleted(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent):
                reload(JumpspaceConfiguration)
                if JumpspaceConfiguration.ArrivingAt == 1:
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
                    Custom.Jumpspace.JumpspaceModule.delnavpoint()
                else:
                    return 0

JumpspaceNavpointDeleted('Jumpspace Delete Navpoint Active', App.ET_EXITED_SET, dict = { 'modes': [ mode ] } )


# Quit trigger, using ET_QUIT event
class QuitJumpspace(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                Custom.Jumpspace.JumpspaceModule.quitting()

QuitJumpspace('Quitting Jumpspace', App.ET_QUIT, dict = { 'modes': [ mode ] } )


# Signalize initialization
print 'Jumpspace Drive ' + Custom.Jumpspace.JumpspaceModule.VERSION + ' Initializing...'

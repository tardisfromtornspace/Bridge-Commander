# by USS Sovereign, DS9FXVortex cannot be registered or playable

# Imports
import Foundation
import App

# Ship details
abbrev = 'DS9FXVortex'
iconName = 'DS9FXVortex'
longName = 'DS9FXVortex'
shipFile = 'DS9FXVortex' 
species = App.SPECIES_GALAXY

# Ship foundation def
Foundation.ShipDef.DS9FXVortex = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

# Description, but it's not used
Foundation.ShipDef.DS9FXVortex.desc = "A plasma storm is a type of spatial disturbance that involves energetic particles in a state called plasma. Plasma storms are commonly found in places such as the Badlands. Plasma storms are relatively common occurrences. "

Foundation.ShipDef.DS9FXVortex.fCrew = "Off"

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


# by USS Sovereign, DS9FXVortex2 cannot be registered or playable

# Imports
import Foundation
import App

# Ship details
abbrev = 'DS9FXVortex2'
iconName = 'DS9FXVortex2'
longName = 'DS9FXVortex2'
shipFile = 'DS9FXVortex2' 
species = App.SPECIES_GALAXY

# Ship foundation def
Foundation.ShipDef.DS9FXVortex2 = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

# Description, but it's not used
Foundation.ShipDef.DS9FXVortex2.desc = "A plasma storm is a type of spatial disturbance that involves energetic particles in a state called plasma. Plasma storms are commonly found in places such as the Badlands. Plasma storms are relatively common occurrences. "

Foundation.ShipDef.DS9FXVortex2.fCrew = "Off"

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


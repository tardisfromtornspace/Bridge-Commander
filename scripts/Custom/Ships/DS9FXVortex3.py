# by USS Sovereign, DS9FXVortex3 cannot be registered or playable

# Imports
import Foundation
import App

# Ship details
abbrev = 'DS9FXVortex3'
iconName = 'DS9FXVortex3'
longName = 'DS9FXVortex3'
shipFile = 'DS9FXVortex3' 
species = App.SPECIES_GALAXY

# Ship foundation def
Foundation.ShipDef.DS9FXVortex3 = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

# Description, but it's not used
Foundation.ShipDef.DS9FXVortex3.desc = "A plasma storm is a type of spatial disturbance that involves energetic particles in a state called plasma. Plasma storms are commonly found in places such as the Badlands. Plasma storms are relatively common occurrences. "

Foundation.ShipDef.DS9FXVortex3.fCrew = "Off"

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


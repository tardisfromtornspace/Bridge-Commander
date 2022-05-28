# by USS Sovereign, hyperdrive tunnel cannot be registered or playable

# Imports
import Foundation
import App

# Ship details
abbrev = 'hyperdrive'
iconName = 'hyperdrive'
longName = 'hyperdrive'
shipFile = 'hyperdrive' 
species = App.SPECIES_GALAXY


# Ship foundation def
Foundation.ShipDef.hyperdrive = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

# Description, but it's not used
Foundation.ShipDef.hyperdrive.desc = 'hyperdrive'
if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


# by USS Sovereign, slipstream tunnel cannot be registered or playable

# Imports
import Foundation
import App

# Ship details
abbrev = 'slipstream'
iconName = 'slipstream'
longName = 'slipstream'
shipFile = 'slipstream' 
species = App.SPECIES_GALAXY


# Ship foundation def
Foundation.ShipDef.slipstream = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

# Description, but it's not used
Foundation.ShipDef.slipstream.desc = 'slipstream'
if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


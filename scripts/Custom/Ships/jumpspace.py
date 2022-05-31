# by USS Sovereign, jumpspace tunnel cannot be registered or playable

# Imports
import Foundation
import App

# Ship details
abbrev = 'jumpspace'
iconName = 'jumpspace'
longName = 'jumpspace'
shipFile = 'jumpspace' 
species = App.SPECIES_GALAXY


# Ship foundation def
Foundation.ShipDef.jumpspace = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

# Description, but it's not used
Foundation.ShipDef.jumpspace.desc = 'jumpspace'
if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


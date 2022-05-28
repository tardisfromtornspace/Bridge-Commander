# by USS Sovereign, DS9FXMine cannot be registered or playable

# Imports
import Foundation
import App

# Ship details
abbrev = 'DS9FXMine'
iconName = 'DS9FXMine'
longName = 'DS9FXMine'
shipFile = 'DS9FXMine' 
species = App.SPECIES_GALAXY

# Ship foundation def
Foundation.ShipDef.DS9FXMine = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

# Description, but it's not used
Foundation.ShipDef.DS9FXMine.desc = "Space mines were weapons deployed in space to inflict damage upon enemy targets."

Foundation.ShipDef.DS9FXMine.fCrew = "Off"

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


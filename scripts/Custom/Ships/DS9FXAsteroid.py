# by USS Sovereign, DS9FXAsteroid cannot be registered or playable

# Imports
import Foundation
import App

# Ship details
abbrev = 'DS9FXAsteroid'
iconName = 'DS9FXAsteroid'
longName = 'DS9FXAsteroid'
shipFile = 'DS9FXAsteroid' 
species = App.SPECIES_GALAXY

# Ship foundation def
Foundation.ShipDef.DS9FXAsteroid = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

# Description, but it's not used
Foundation.ShipDef.DS9FXAsteroid.desc = "Asteroids are also known as \"minor planets.\" They are made up of much of the same stuff as planets, but they are much smaller."

Foundation.ShipDef.DS9FXAsteroid.fCrew = 5000

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

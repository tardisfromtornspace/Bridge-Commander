# by USS Sovereign, DS9FXMissionStation

# Imports
import Foundation
import App

# Ship details
abbrev = 'DS9FXMissionStation'
iconName = 'DS9FXMissionStation'
longName = 'DS9FXMissionStation'
shipFile = 'DS9FXMissionStation' 
species = App.SPECIES_GALAXY

# Ship foundation def
Foundation.ShipDef.DS9FXMissionStation = Foundation.StarBaseDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

# Description, but it's not used
Foundation.ShipDef.DS9FXMissionStation.desc = "A space station is an artificial structure in space, often built to support life. Space stations can serve many purposes, including research, defense and starship maintenance. Depending on their purpose, they may be referred to with another term, such as a Spacelab or outpost. Space stations can be in orbit of a planet, or be completely free floating in space."
Foundation.ShipDef.DS9FXMissionStation.fCrew = 1250

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


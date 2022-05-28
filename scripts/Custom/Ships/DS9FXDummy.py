# by USS Sovereign, DS9FXDummy cannot be registered or playable

# Imports
import Foundation
import App

# Ship details
abbrev = 'DS9FXDummy'
iconName = 'DS9FXDummy'
longName = 'DS9FXDummy'
shipFile = 'DS9FXDummy' 
species = App.SPECIES_GALAXY

# Ship foundation def
Foundation.ShipDef.DS9FXDummy = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

# Description, but it's not used
Foundation.ShipDef.DS9FXDummy.desc = "A shuttlecraft is a smaller type of ship, usually capable of atmospheric transport, detachable from a larger starship's shuttlebay. Its role on starships is analogous to the use of naval helicopters on modern warships of the present day, as shuttlecraft often possess their own weapons and intelligence capabilities, and undertake a variety of missions. Additionally, many starships have shuttle bays regardless of their ship class, just as most naval ships have a helicopter landing pad and hangar.\n\nLarger classes of shuttlecraft usually have their own weapons, defenses, and communication systems, as well as emergency transporters in case of a crash. Advanced shuttles are capable of speeds of up to Warp 4."

Foundation.ShipDef.DS9FXDummy.fCrew = "Off"

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


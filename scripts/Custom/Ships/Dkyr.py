#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Dkyr"
iconName = "Dkyr"
longName = "Dkyr"
shipFile = "Dkyr"
menuGroup = 'Pre-Fed ships'
playerMenuGroup = 'Pre-Fed ships'
SubMenu = "Vulcan High Command"
species = App.SPECIES_GALAXY
Foundation.ShipDef.Dkyr = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })


Foundation.ShipDef.Dkyr.desc = "The D'kyr-type was a type of Vulcan starship operated by the High Command during the mid-22nd century. Some of these vessels were given the designation of combat cruiser in the 2150s.In 2154, a number of these starships were present at the Battle of Andoria, carrying out the ill-wishes of then – Administrator V'Las, which included not only attempting to invade Andoria – but almost going to war with Earth by trying to destroy Enterprise NX-01. Later that year, several of these combat cruisers were incorporated into an Andorian-Earth-Tellarite-Vulcan fleet, consisting of 128 ships, combined to create a sensor grid formed to detect a Romulan marauder that threatened to destabilize the entire region. Ships of this class were armed with both photonic and particle weapons, as well as deflector shield technology. Particle beam emplacements include a forward emitter, two ventral emitters, and two aft emitters."


if menuGroup:           Foundation.ShipDef.Dkyr.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Dkyr.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

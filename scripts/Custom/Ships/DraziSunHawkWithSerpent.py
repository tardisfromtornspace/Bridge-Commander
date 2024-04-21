#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "DraziSunHawkWithSerpent"
iconName = "DraziSunHawkWithSerpent"
longName = "Sun Hawk mk II"
shipFile = "DraziSunHawkWithSerpent"
species = App.SPECIES_AMBASSADOR
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "League of Non-Aligned Worlds"
SubSubMenu = "Drazi Freehold"
Foundation.ShipDef.DraziSunHawkWithSerpent = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })
Foundation.ShipDef.DraziSunHawkWithSerpent.desc = "The Sun-Hawk is a type of medium warship used as an A-Class battle cruiser by Drazi Military. The pak'ma'ra are also using Sun-Hawk class ships as transports. The Drazi Freehold uses these ships for various purposes ranging from assault missions through escort missions to patrolling duties. The Sun-Hawk is configured only for non-atmospheric combat and while the ship is not equipped with a dedicated hanger bay, a Sun-Hawk can be adapted to mount a single Sky Serpent fighter on a dorsal docking cradle. Drazi military organisation is intentionally decentralised, stemming from the idea that that they work best in smaller groups and the Sun-Hawk was built with this in mind. As a smaller and less costly ship to build in comparison to larger scale, more traditional capital ships such as the Minbari Federation's Sharlin class warcruiser or Earth Alliance's Omega class destroyer, the Sun-Hawk could be built in larger numbers and be deployed over a wider area. When missions require the firepower of a heavy cruiser, it's simple enough to organise a small task force of Sun-Hawks, who's combined tactical strength compensates for the relative weakness of a single Sun-Hawk."
Foundation.ShipDef.DraziSunHawkWithSerpent.dTechs = {
	'Gravimetric Defense': 80,
	"Tachyon Sensors": 2.5
}

if menuGroup:           Foundation.ShipDef.DraziSunHawkWithSerpent.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DraziSunHawkWithSerpent.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "BrakiriCruiser"
iconName = "BrakiriCruiser"
longName = "Brakiri Cruiser"
shipFile = "BrakiriCruiser"
species = App.SPECIES_AMBASSADOR
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "League of Non-Aligned Worlds"
SubSubMenu = "Brakiri Syndicracy"
Foundation.ShipDef.BrakiriCruiser = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })
Foundation.ShipDef.BrakiriCruiser.desc = "The Brakiri cruiser is a heavy vessel used by the Brakiri. These ships belong to one of the wealthiest and most politically stable races in the League of Non-Aligned Worlds. It is also one of the largest ships deployed by the League. The ships themselves however are inferior to those of the Earth Alliance, as is their weaponry. In keeping with the rest of Brakiri society, these ships are owned and operated by mega-corporations and thus must contribute to the Brakiri economy when not on military duty by serving as passenger liners, transports or colony ships."
Foundation.ShipDef.BrakiriCruiser.dTechs = {
	'Gravimetric Defense': 80,
	"Tachyon Sensors": 2.2
}

if menuGroup:           Foundation.ShipDef.BrakiriCruiser.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.BrakiriCruiser.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

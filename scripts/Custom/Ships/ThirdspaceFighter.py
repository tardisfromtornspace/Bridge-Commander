#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "ThirdspaceFighter"
iconName = "ThirdspaceFighter"
longName = "Thirdspace Fighter"
shipFile = "ThirdspaceFighter"
species = App.SPECIES_GALAXY
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "Thirdspace Aliens"
SubSubMenu = "Fighters"

Foundation.ShipDef.ThirdspaceFighter = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Yeah I know thirdspace aliens don't have Vree tech, but on this case I made both of them work the same way
Foundation.ShipDef.ThirdspaceFighter.dTechs = {'Breen Drainer Immune': 1, "Vree Shields": 100}

Foundation.ShipDef.ThirdspaceFighter.desc = "A Thirdspace fighter is a small vessel controlled by the Thirdspace Aliens.These ships are capable of equaling a Whitestar in firepower. The ships are small, fast, with weapons and defenses unlike anything ever seen. Starfuries could do practically nothing against them, and as quoted 'We have to hit them four times before they even notice.' There is plenty of proof to that statement. The weapons systems were based around three coiled appendages that generated a surprisingly powerful plasma burst capable of crippling a Whitestar in just two shots and destroying a starfury like it was a bug on a windshield."


if menuGroup:           Foundation.ShipDef.ThirdspaceFighter.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.ThirdspaceFighter.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

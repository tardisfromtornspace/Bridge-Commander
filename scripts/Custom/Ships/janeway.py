#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "janeway"
iconName = "janeway"
longName = "U.S.S. Voyager J"
shipFile = "janeway"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"

Foundation.ShipDef.janeway = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

Foundation.ShipDef.janeway.SubMenu = "32nd Century"
Foundation.ShipDef.janeway.CloakingSFX   = "FutureBattleCloak"
Foundation.ShipDef.janeway.DeCloakingSFX = "FutureBattleDecloak"

Foundation.ShipDef.janeway.dTechs = {
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
	'Ablative Armour': 405000,
	'ChronitonTorpe Immune': 1,
	'Multivectral Shields': 30,
	'Regenerative Shields': 50
}

Foundation.ShipDef.janeway.desc = "The USS Voyager (NCC-74656-J) was a Federation Intrepid-class starship operated by Starfleet during the late 32nd century. It was the eleventh Federation ship to bear the name Voyager with this registry. When Osyraa commandeered Discovery to enter the Federation Headquarters' protective shield and began attacking, Admiral Vance instructed Voyager to take the lead on attacking the Viridian while the rest of the fleet targeted Discovery. Voyager was then part of the Federation-Ni'Var fleet that pursued Discovery and the Viridian, and acknowledged instructions from Discovery to back to a safe distance when Discovery planned to detonate their warp core."



if menuGroup:           Foundation.ShipDef.janeway.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.janeway.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
      
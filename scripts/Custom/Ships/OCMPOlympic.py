#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "OCMPOlympic"
iconName = "OCMP"
longName = "OCMPOlympic"
shipFile = "OCMPOlympic"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.OCMPOlympic = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.OCMPOlympic.desc = "The Olympic Class is a Military Hospital ship that doubles as a Colony transport, Medical research vessel, Medical supply ship and first responder rescue vessel. The ship is armed with 75 Photon and Quantum torpedoes each. The Olympic Class is outfitted with Auto-targeting torpedoes. Ablative Armour, Reflective and Regenerative shielding. These are defensive weapons, installed to ensure the survival of the wounded. In theory, races such as the Klingons, Romulans, Cardassians, the Dominion and the Breen, will attack non-combatant ships as a means of demoralization and psychological warfare. The Olympic class can support a Crew Compliment of 357, Maximum capacity 1357."
Foundation.ShipDef.OCMPOlympic.SubMenu = "Olympic Class"
Foundation.ShipDef.OCMPOlympic.SubSubMenu = "MK I Prototype Medical EFR"
Foundation.ShipDef.OCMPOlympic.fMaxWarp = 9 + 0.0001
Foundation.ShipDef.OCMPOlympic.fCruiseWarp = 7.95 + 0.0001
Foundation.ShipDef.OCMPOlympic.fCrew = 357


Foundation.ShipDef.OCMPOlympic.dTechs = {
   "Reflector Shields": 37,
   "AutoTargeting": {"Phaser": [85,1]}
}


if menuGroup:           Foundation.ShipDef.OCMPOlympic.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.OCMPOlympic.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

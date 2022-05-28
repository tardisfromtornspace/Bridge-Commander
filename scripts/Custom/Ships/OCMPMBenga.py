#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "OCMPMBenga"
iconName = "OCMP"
longName = "OCMPM'Benga"
shipFile = "OCMPMBenga"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.OCMPMBenga = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.OCMPMBenga.desc = "The Olympic Class is a Military Hospital ship that doubles as a Colony transport, Medical research vessel, Medical supply ship and evacuation vessel. The MK II prototype ship is armed with 75 Photon and Quantum torpedoes each. The Olympic Class is outfitted with Auto-targeting torpedoes. Ablative Armour, Reflective and Regenerative shielding. These are defensive weapons, installed to ensure the survival of the wounded. In theory, races such as the Klingons, Romulans, Cardassians, the Dominion and the Breen, will attack non-combatant ships as a means of demoralization and psychological warfare. The Olympic class can support a Crew Compliment of 357, Maximum capacity 1357."
Foundation.ShipDef.OCMPMBenga.SubMenu = "Olympic Class"
Foundation.ShipDef.OCMPMBenga.SubSubMenu = "MK II Prototype Medical EVC"
Foundation.ShipDef.OCMPMBenga.fMaxWarp = 9 + 0.0001
Foundation.ShipDef.OCMPMBenga.fCruiseWarp = 7.95 + 0.0001
Foundation.ShipDef.OCMPMBenga.fCrew = 357


Foundation.ShipDef.OCMPMBenga.dTechs = {
   "Reflector Shields": 55,
   "AutoTargeting": {"Phaser": [100,1]}
}


if menuGroup:           Foundation.ShipDef.OCMPMBenga.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.OCMPMBenga.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Enterprise"
iconName = "NemesisSovereign"
longName = "USS Enterprise E"
shipFile = "Enterprise"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.Enterprise = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.Enterprise.dTechs = {
	'Breen Drainer Immune': 0,
	'Regenerative Shields': 10,
	'Multivectral Shields': 10,
	'Fed Ablative Armor': { "Plates": ["Aft Ablative Armor", "Engineering Ablative Armor", "Top Ablative Armor", "Forward Ablative Armor"]
}}

Foundation.ShipDef.Enterprise.desc = "The USS Enterprise-E is the sixth Federation Flagship with that name. A Sovereign-class starship commanded by Captain Jean-Luc Piccard, it saw service during the late 24th century."


if menuGroup:           Foundation.ShipDef.Enterprise.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Enterprise.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def USSEnterpriseEIDSwap(self):
       retval = {"Textures": [["Ent-E-dishtopbottomID_glow.tga", "Data/Models/Ships/Sovereign/Enterprise.tga"]]}
       return retval

Foundation.ShipDef.Enterprise.__dict__['SDT Entry'] = USSEnterpriseEIDSwap
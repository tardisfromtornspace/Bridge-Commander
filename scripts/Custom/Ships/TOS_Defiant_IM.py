#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "TOS_Defiant_IM"
iconName = "TOS_Defiant_IM"
longName = "USS Defiant IM"
shipFile = "TOS_Defiant_IM"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.TOS_Defiant_IM = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.TOS_Defiant_IM.desc = "Design: Interstellar Machine\nMesh: Interstellar Machine\nTextures: Interstellar Machine\nConversion to Bridge Commander by MSR1701\nHardpointing by MSR1701\n\nNamed after the ill fated Constitution Class Defiant which drifted out of phase with reality, this Defiant employs a controlled variation of this effect thanks to a mysterious alien technology. This may be the answer to the question of what happened to the cloaking device confistacted from the Romulan Battlecruiser by the crew of the U.S.S. Enterprise at the height of the Klingon-Romulan Alliance early in the twenty-third century. (CL)"
Foundation.ShipDef.TOS_Defiant_IM.SubMenu = "TOS Ships"
Foundation.ShipDef.TOS_Defiant_IM.SubSubMenu = "Defiant Type"


if menuGroup:           Foundation.ShipDef.TOS_Defiant_IM.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.TOS_Defiant_IM.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

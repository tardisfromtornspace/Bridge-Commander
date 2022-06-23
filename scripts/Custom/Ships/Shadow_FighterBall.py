#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Shadow_FighterBall"
iconName = "Shadow_FighterBall"
longName = "Fighter Deploy"
shipFile = "Shadow_FighterBall"
species = App.SPECIES_SHUTTLE
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "The Shadows"

Foundation.ShipDef.Shadow_FighterBall = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

Foundation.ShipDef.Shadow_FighterBall.dTechs = { "Phase Cloak": 10, 'Breen Drainer Immune': 1, 'Shadow Dispersive Hull': 1}

Foundation.ShipDef.Shadow_FighterBall.desc = "The Shadow Battlecrabs don't throw Fighters one by one, but in a great bundled group."
Foundation.ShipDef.Shadow_FighterBall.CloakingSFX = "shadowscream"
Foundation.ShipDef.Shadow_FighterBall.DeCloakingSFX = "shadowscream"
Foundation.ShipDef.Shadow_FighterBall.SubSubMenu = "Fighters"
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
if menuGroup:           Foundation.ShipDef.Shadow_FighterBall.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Shadow_FighterBall.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

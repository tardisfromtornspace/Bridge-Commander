#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Battlecrab"
iconName = "Battlecrab"
longName = "Shadow Battlecrab"
shipFile = "Battlecrab"
species = App.SPECIES_GALAXY
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "The Shadows"
SubSubMenu = "Capital Ships"
Foundation.ShipDef.Battlecrab = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

Foundation.ShipDef.Battlecrab.dTechs = {
	"Phase Cloak": 10,
	'Breen Drainer Immune': 1,
	'Shadow Dispersive Hull': 2,
	'Automated Destroyed System Repair': {"Time": 800.0},
	'Simulated Point Defence' : { "Distance": 40.0, "InnerDistance": 20.0, "Effectiveness": 0.02, "LimitDamage": "-1250", "Period": 2.5, "MaxNumberTorps": 1, "Phaser": {"Priority": 1}},
	"Tachyon Sensors": 0.1
}

Foundation.ShipDef.Battlecrab.desc = "The Shadow Vessel (sometimes known as Battle Crab or The Ghost) is the primary starship of the Shadows. Easily distinguished by its spiny, almost spider like shape and its constantly undulating black skin, Shadow vessels are known to have a deeply unsettling effect on sentients and can somehow project a scream like noise into the mind of any that get near it as it goes by. An extremely powerful war machine, its primary beam weapon has an energy output on par with a controlled thermonuclear reaction and can effortlessly cut through even a four mile wide space station from a range of around a dozen miles. A direct hit from this weapon is under normal circumstances sufficient to destroy almost any ship of the Young races. The Shadow vessel also possesses a weapon capable of destabilizing jump points. When fired into active hyperspace vortex it causes the formed jump point to quickly collapse, which leads to a massive shockwave that will destroy any ships caught in the blast radius. Even inactive, a Shadow Vessel is extremely dangerous. "
Foundation.ShipDef.Battlecrab.CloakingSFX = "shadowscream"
Foundation.ShipDef.Battlecrab.DeCloakingSFX = "shadowscream"

if menuGroup:           Foundation.ShipDef.Battlecrab.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Battlecrab.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

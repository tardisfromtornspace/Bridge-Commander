#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created manually by - CharaToLoki AKA Alex SL Gato                                 #
#  Date: 12.10.2024                                                                   #
#######################################################################################
#                                                                                     #
import Foundation
import App
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'AndromedaTalyn',
	'author': 'Alex SL Gato',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}
#                                                                                     #
#######################################################################################
#    
abbrev = "AndromedaTalyn"
iconName = "AndromedaTalyn"
longName = "Glorious Leviathan hybrid"
shipFile = "AndromedaTalyn"
species = App.SPECIES_SOVEREIGN
menuGroup = "Non canon X-Overs"
playerMenuGroup = "Non canon X-Overs"
SubMenu = "CharaToLokis"

#                                                                                     #
#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#

Foundation.ShipDef.AndromedaTalyn = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu }) 
Foundation.ShipDef.AndromedaTalyn.dTechs = {
	'Ablative Armour': [220000, "Armour"],
	'Alteran ZPM Shields': { "Strength": 1 },
	'Automated Destroyed System Repair': {"Time": 5.0},
	"AutoTargeting": { "Pulse": [3, 1] },
	'Borg Adaptation': 3,
	'Breen Drainer Immune': 1,
	'ChronitonTorpe Immune': 1,
	"Disabler Immunity": { "Power": 15, "Warp": 3, "Cloak": 10 },
	'Drainer Immune': 1,
	'Defensive AOE Siphoon' : { "Distance": 35.0, "Power": 10000.0, "Efficiency": 0.5, "Resistance": 1.0,},
	"Fool Targeting": {
		"Minbari Stealth": {
			"sensor": 6500
		},
		"Torvalus Shading": {
			"Distance": 30,
			"Miss": 2.5,
			"Sensor": 1500,
		}  
	},
	"GraviticLance": { "Time": 0.1, "TimeEffect": 10.0, "RadDepletionStrength": 1000, "Beams": ["Gravitic Lance", "Array 6"], "Immune": 1},
	"Inversion Beam": [0.5, 0, 0.5, 1500],
	"Phased Torpedo Immune": 1,
	"Phase Cloak": 0.1,
	"Power Drain Beam": [0.5, 0, 0.5, 1500],
        "Reflector Shields": 40,
	'Reflux Weapon': 100,
	'Regenerative Shields': 50,
	"SG Anubis SuperWeapon Ray": { "Beams": ["Array 1", "Array 2", "Array 3", "Array 4", "Array 5", "Array 6"]},
	"SG Asgard Beams Weapon": {"HullDmgMultiplier": 0.12, "ShieldDmgMultiplier": 0.12},
	"SG Ori Beams Weapon": {"HullDmgMultiplier": 0.5, "ShieldDmgMultiplier": 0.5, "Beams": ["Ori Array"]},
	'Simulated Point Defence' : { "Distance": 120.0, "InnerDistance": 15.0, "Effectiveness": 0.8, "LimitTurn": 6.0, "LimitSpeed": 350, "Period": 0.2, "MaxNumberTorps": 12, "Pulse": {"Priority": 1}},
	"Slow Start": {"Pulses": ["Nova Bomb 1", "Nova Bomb 2", "Transphasic"]},
	"SOTI Size Change": {"Scale": 1.0, "Power": 1, "Types": [App.CT_SHIELD_SUBSYSTEM]},
	"TachyonBeam": { "Time": 12.0, "TimeEffect": 2.0, "Immune": 1},
	"Tachyon Sensors": 0.1,
	"Transphasic Torpedo Immune": 1,
	"Undying Comeback": {"Damage Factor": 1.0, "Model": "AndromedaTalyn", "Boost": 25, "Energy Boost": 25.0, "Shield Boost": 25.0, "Weapon Boost": 25.0},
	'Vree Shields': 100,
}
Foundation.ShipDef.AndromedaTalyn.sBridge = 'GalaxyBridge'
Foundation.ShipDef.AndromedaTalyn.fMaxWarp = 9.99 + 0.01
Foundation.ShipDef.AndromedaTalyn.fWarpEntryDelayTime = 0.5
Foundation.ShipDef.AndromedaTalyn.bPlanetKiller = 1

#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL 
#Foundation.ShipDef.AndromedaTalyn.hasTGLName = 1
#Foundation.ShipDef.AndromedaTalyn.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:

Foundation.ShipDef.AndromedaTalyn.desc = "Originally a Peacekeeper Command Leviathan-Systems Commonwealth Glorious Heritage class hybrid of unknown origin, this vessel has harnessed some mysterious technologies and received consideable upgrades during its voyages."

#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.AndromedaTalyn.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.AndromedaTalyn.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

#                                                                                     #
#######################################################################################
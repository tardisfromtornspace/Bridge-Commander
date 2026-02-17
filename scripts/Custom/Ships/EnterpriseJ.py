from bcdebug import debug
import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'EnterpriseJ'				# Short name, no spaces, used as a preface for descriptions
iconName = 'EnterpriseJ'					# Name of icon .tga file
longName = 'U.S.S. Enterprise J (Monarch class)'					# Long name with spaces
shipFile = 'EnterpriseJ'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Fed Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Fed Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_MARAUDER			# I'm not sure how important this is.
# Thats mainly for the icon, but unused

SubMenu = "26th Century"

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'EnterpriseJ',			# The full name of your mod if applicable
	'author': 'EnterpriseJ',					# Your name here
	'version': '1.0',						# No more than one period please!  
										# I'd like to be able to do a numeric comparison.
	'sources': [ '' ],				# Source for this mod
	'comments': ''						# General info
}


Foundation.ShipDef.EnterpriseJ = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

Foundation.ShipDef.EnterpriseJ.dTechs = {
	'Adv Armor Tech': 1,
	"AutoTargeting": {"Phaser": [3, 1], "Torpedo": [2, 1], "Pulse": [2, 1] },
	'Breen Drainer Immune': 0,
	'ChronitonTorpe Immune': 1,
	'Defensive AOE Siphoon' : { "Distance": 55.0, "Power": -10000.0, "Efficiency": 0.99, "Resistance": 1.0,},
	'Drainer Immune': 1,
	'Fed Ablative Armor': {"Plates": ["Forward Ablative Armor", "Aft Ablative Armor", "Dorsal Ablative Armor", "Ventral Ablative Armor", "Hull"]},
	"Inversion Beam": [12000, 0, 0.5, 1500],
	'Multivectral Shields': 10,
	"Phased Torpedo Immune": 1,
	"Power Drain Beam": [1500, 0, 0.5, 1500],
	'Simulated Point Defence' : { "Distance": 75.0, "InnerDistance": 10.0, "Effectiveness": 0.9, "LimitTurn": 5.0, "LimitSpeed": 120, "LimitDamage": "-5000", "Period": 1.0, "MaxNumberTorps": 50, "Phaser": {"Priority": 1}},
	"TachyonBeam": {"Immune": -1},
	"Transphasic Torpedo Immune": 1,
	"Reflector Shields": 2,
	'Reflux Weapon': 3800,
	'Regenerative Shields': 75
}

Foundation.ShipDef.EnterpriseJ.sBridge = 'defiantbridge'
Foundation.ShipDef.EnterpriseJ.fMaxWarp = 9.995
Foundation.ShipDef.EnterpriseJ.fWarpEntryDelayTime = 3.5
Foundation.ShipDef.EnterpriseJ.SubMenu = SubMenu

Foundation.ShipDef.EnterpriseJ.desc = 'The USS Enterprise NCC-1701-J was a 26th century Federation Monarch-class starship operated by Starfleet in a possible future.\n\nThe Enterprise-J participated in the historic Battle of Procyon V, wherein the forces of the Federation successfully drove the Sphere-Builders back into their trans-dimensional realm.'

if menuGroup:           Foundation.ShipDef.EnterpriseJ.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.EnterpriseJ.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

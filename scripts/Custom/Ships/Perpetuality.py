#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 7/24/2002                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
import traceback
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'Perpetuality'
iconName = 'Perpetuality'
longName = 'U.S.S. Perpetuality'
shipFile = 'Perpetuality' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'Perpetuality',
	'author': 'Greystar, Hexagonal Nexul and Superjosh',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#                                                                                     #
try:
	import Custom.Autoload.RaceFutureFed29c
	Foundation.ShipDef.Perpetuality = Foundation.FutureFed29cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.Perpetuality = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()
	
Foundation.ShipDef.Perpetuality.fMaxWarp = 12 + 4.0
Foundation.ShipDef.Perpetuality.fCruiseWarp = 9.9999999999998 + 4.0
Foundation.ShipDef.Perpetuality.OverrideWarpFXColor = Foundation.ShipDef.Perpetuality.OverrideWarpFXColor
Foundation.ShipDef.Perpetuality.OverridePlasmaFXColor = Foundation.ShipDef.Perpetuality.OverridePlasmaFXColor

Foundation.ShipDef.Perpetuality.dTechs = {
	'Adv Armor Tech': 1,
	"Alternate-Warp-FTL": {
		"Setup": {
			"DrWTimeVortexDrive": {	"Core": ["Anti Thalaron Reactor", "Temporal Drive", "Temporal Cloak"], },
		},
	},
	'Automated Destroyed System Repair': {"Time": 45.0, "DoNotInterfere": 1},
	"Borg Attack Resistance": 90,
	'Breen Drainer Immune': 0,
	'ChronitonTorpe Immune': 1,
	'Digitizer Torpedo Immune': 1,
	'Drainer Immune': 1,
	"Inversion Beam": [0.5, 0, 0.5, 1500],
	'Multivectral Shields' : 26,
	"Power Drain Beam": [0.5, 0, 0.5, 1500],
	"Phase Cloak": -1, 
	'Phased Torpedo Immune': 1,
	'Reflux Weapon': 1000,
	'Regenerative Shields': 60,
	'Transphasic Torpedo Immune': 1,
	"SGReplicator Attack Resistance": 40,
	"SG Asgard Beams Weapon Immune": 2,
	"SG Ion Weapon Immune": 2,
	"SG Ori Beams Weapon Immune": 2,
	"SG Plasma Weapon Immune": 2,
	"SG Railgun Weapon Immune": 2,
	'Subatomic Disruptor Beams Weapon Immune': 1,
	"Subparticle Torpedo Immune": 1,
	'Tetraburnium Armour': 170000,
	"TimeVortex Torpedo Immune": 1,
	'Vree Shields': 55,	
}

Foundation.ShipDef.Perpetuality.SubMenu = "30th Century"

Foundation.ShipDef.Perpetuality.CloakingSFX   = "Future_cloak2"
Foundation.ShipDef.Perpetuality.DeCloakingSFX = "Future_uncloak2"                                                                                 
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.Perpetuality.hasTGLName = 1
# Foundation.ShipDef.Perpetuality.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.Perpetuality.desc = 'A Wells Class refit from the 30th century. Not much is known about this century in time, but the Perpetuality did meet with the Enterprise M while surveying in the 28th century.'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.Perpetuality.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Perpetuality.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################

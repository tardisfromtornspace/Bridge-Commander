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
abbrev = 'HGWells'
iconName = 'HGWells'
longName = 'U.S.S. Relativity G'
shipFile = 'HGWells' 
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
	'modName': 'HGWells',
	'author': '',
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
	Foundation.ShipDef.HGWells = Foundation.FutureFed29cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.HGWells = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()
	
Foundation.ShipDef.HGWells.fMaxWarp = 12 + 3.0
Foundation.ShipDef.HGWells.fCruiseWarp = 9.999999999996 + 3.0
Foundation.ShipDef.HGWells.OverrideWarpFXColor = Foundation.ShipDef.HGWells.OverrideWarpFXColor
Foundation.ShipDef.HGWells.OverridePlasmaFXColor = Foundation.ShipDef.HGWells.OverridePlasmaFXColor
Foundation.ShipDef.HGWells.dTechs = {
	'Adv Armor Tech': 1,
	"Alternate-Warp-FTL": {
		"Setup": {
			"DrWTimeVortexDrive": {	"Core": ["Tetryon Reactor", "Temporal Drive", "Temporal Shield Generator"], },
		},
	},
	'Automated Destroyed System Repair': {"Time": 45.0, "DoNotInterfere": 1},
	"Borg Attack Resistance": 85,
	'Breen Drainer Immune': 0,
	'ChronitonTorpe Immune': 1,
	'Digitizer Torpedo Immune': 1,
	'Drainer Immune': 1,
	"Inversion Beam": [0.5, 0, 0.5, 1500],
	'Multivectral Shields' : 25,
	"Power Drain Beam": [0.5, 0, 0.5, 1500],
	"Phase Cloak": -1, 
	'Phased Torpedo Immune': 1,
	"Reflector Shields": 2,
	'Reflux Weapon': 1000,
	'Regenerative Shields': 60,
	"SGReplicator Attack Resistance": 40,
	"SG Asgard Beams Weapon Immune": 2,
	"SG Ion Weapon Immune": 2,
	"SG Ori Beams Weapon Immune": 2,
	"SG Plasma Weapon Immune": 2,
	"SG Railgun Weapon Immune": 2,
	"Subatomic Disruptor Beams Weapon": [{"HullDmgMultiplier": 1000.0, "ShieldDmgMultiplier": 19000.0, "Beams": ["Subatomic Disruptor"]}, ["Subatomic_Disruptor_Beam"]],
	"Subparticle Torpedo Immune": 1,
	'Tetraburnium Armour': 110000,
	"TachyonBeam": {"Immune": -1},
	'Transphasic Torpedo Immune': 1,
	'Vree Shields': 55,	
}



Foundation.ShipDef.HGWells.SubMenu = "29th Century"

Foundation.ShipDef.HGWells.CloakingSFX   = "Future_cloak"
Foundation.ShipDef.HGWells.DeCloakingSFX = "Future_uncloak"                                                                                 
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.HGWells.hasTGLName = 1
# Foundation.ShipDef.HGWells.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.HGWells.desc = 'The USS Relativity (NCV-474439-G) is a 29th century Federation Wells-class starship operated by Starfleet. The timeship was commissioned at the University of Copernicus, and was initially under the command of Captain Braxton. The vessel was equipped with powerful sensors capable of scanning throughout spacetime, and a temporal transporter capable of beaming an individual to virtually any point in space and time.'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.HGWells.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.HGWells.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################

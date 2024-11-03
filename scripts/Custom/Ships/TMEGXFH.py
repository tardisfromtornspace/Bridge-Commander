#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback

abbrev = "TMEGXFH"
iconName = "TMEGXFH"
longName = "The Most Evil GXFH"
shipFile = "TMEGXFH"
species = App.SPECIES_GALAXY
menuGroup = "The Face of Fear"
playerMenuGroup = "The Face of Fear"

import traceback
try:
	import Custom.Autoload.RaceTMEGXFH
	Foundation.ShipDef.TMEGXFH = Foundation.TMEGXFHShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
except:
	print "Error while loading a race"
	Foundation.ShipDef.TMEGXFH = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
	traceback.print_exc()

Foundation.ShipDef.TMEGXFH.desc = "A Galaxy X Class built and modified by an evil version of Retro Badger Gaming in some unholy alternate timeline"
Foundation.ShipDef.TMEGXFH.CloakingSFX = "TMEGXFHCloak"
Foundation.ShipDef.TMEGXFH.DeCloakingSFX = "TMEGXFHDecloak"
Foundation.ShipDef.TMEGXFH.fMaxWarp = 15.0
Foundation.ShipDef.TMEGXFH.fCruiseWarp = 10
Foundation.ShipDef.TMEGXFH.OverrideWarpFXColor = Foundation.ShipDef.TMEGXFH.OverrideWarpFXColor
Foundation.ShipDef.TMEGXFH.dTechs = {
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
    'Fed Ablative Armor': { "Plates": ["Demonic Protection"]},
	'ChronitonTorpe Immune': 1,
	'Phased Torpedo Immune': 1,
	'Reflux Weapon Immune': 1,
	'TimeVortex Torpedo Immune': 1,
	"Digitizer Torpedo Immune": 1,
	"Transphasic Torpedo Immune" : 1
}

if menuGroup:           Foundation.ShipDef.TMEGXFH.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.TMEGXFH.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

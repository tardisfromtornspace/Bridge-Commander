#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback


abbrev = "Inquiry"
iconName = "Inquiry"
longName = "Inquiry"
shipFile = "Inquiry"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"

try:
	import Custom.Autoload.RaceFutureFed25c
	Foundation.ShipDef.Inquiry = Foundation.FutureFed25cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.Inquiry = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()


Foundation.ShipDef.Inquiry.desc = "No information available."
Foundation.ShipDef.Inquiry.SubMenu = "2400s"
Foundation.ShipDef.Inquiry.OverrideWarpFXColor = Foundation.ShipDef.Inquiry.OverrideWarpFXColor
Foundation.ShipDef.Inquiry.OverridePlasmaFXColor = Foundation.ShipDef.Inquiry.OverridePlasmaFXColor
Foundation.ShipDef.Inquiry.dTechs = {
	"Borg Attack Resistance": 20,
	'Breen Drainer Immune': 1,
	'Regenerative Shields': 120,
	'Multivectral Shields': 5,
	"Fed Ablative Armor": {"Plates": ["Forward Ablative Armor","Aft Ablative Armor","Port Ablative Armor","Starboard Ablative Armor","Dorsal Ablative Armor","Saucer Ablative Armor","Port Nacelle Ablative Armor","Starboard Nacelle Ablative Armor","Ventral Ablative Armor"]}
}


if menuGroup:           Foundation.ShipDef.Inquiry.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Inquiry.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

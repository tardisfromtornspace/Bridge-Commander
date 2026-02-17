#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback


abbrev = "GSEminence"
iconName = "GSEminence"
longName = "U.S.S. Enterprise F (Eminence-class Retrofit)"
shipFile = "GSEminence"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"

try:
	import Custom.Autoload.RaceFutureFed25c
	Foundation.ShipDef.GSEminence = Foundation.FutureFed25cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.GSEminence = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()


Foundation.ShipDef.GSEminence.desc = "In the 25th century, The Eminence class was becoming outdated as it was simply a Sovereign Refit with some simple reverse engineered borg technologies. It was refit in the 2420s into a far more capable vessel, boasting newly developed Nanite Regenerative Ablative Plating, Multivectoral Regenerative Adaptive Shielding, Multiflux Nadionic Slicing Arrays, as well as an Enhanced Regeneration Node and an Experimental Phase Cloak developed by Starfleet. Most of the other technologies were reverse engineered from abandoned or captured borg tech.\n\nRetrofit Heavy Tritanium Dual Hull: 33500\n\nNanite Regenerative Ablative Plating\nFore: 17500\nAft: 17500\nPort: 12500\nStar: 12500\n\nShielding Stats:\nForward: 18000, 100 Regen\nAft: 18000, 100 regen\nPort: 18000, 100 regen\nStar: 18000, 100 regen\nDorsal: 18000, 100 regen\nVentral: 18000, 100 regen\n\nPhaser damage: 1950\n\nTorpedo loadout:\nQuantum Mk.XI: 300\nAdvanced Photon Mk.XXVI: 500\nTransphasic Mk.II: 15"
Foundation.ShipDef.GSEminence.SubMenu = "2400s"
Foundation.ShipDef.GSEminence.SubSubMenu = "Borg Enhanced Ships"
Foundation.ShipDef.GSEminence.CloakingSFX = ""
Foundation.ShipDef.GSEminence.DeCloakingSFX = ""
Foundation.ShipDef.GSEminence.OverrideWarpFXColor = Foundation.ShipDef.GSEminence.OverrideWarpFXColor
Foundation.ShipDef.GSEminence.OverridePlasmaFXColor = Foundation.ShipDef.GSEminence.OverridePlasmaFXColor
Foundation.ShipDef.GSEminence.fMaxWarp = 9.9999
Foundation.ShipDef.GSEminence.fCruiseWarp = 9.875

Foundation.ShipDef.GSEminence.dTechs = {
	"Borg Attack Resistance": 30,
	"Fed Ablative Armor": {"Plates": ["Forward Nanite Regenerative Armor Plating", "Aft Nanite Regenerative Armor Plating", "Star Nanite Regenerative Armor Plating", "Port Nanite Regenerative Armor Plating"]},
	'Breen Drainer Immune': 0,
	'Drainer Immune': 1,
	'Regenerative Shields': 60,
	'Multivectral Shields': 20,
	"AutoTargeting": {"Phaser": [5, 2] },
	'Phase Cloak': 5
}


if menuGroup:           Foundation.ShipDef.GSEminence.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.GSEminence.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

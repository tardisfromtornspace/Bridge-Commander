#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "MinbariNial"
iconName = "MinbariNial"
longName = "Nial Fighter"
shipFile = "MinbariNial"
species = App.SPECIES_GALAXY
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
Foundation.ShipDef.MinbariNial = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.MinbariNial.desc = "The Nial class heavy fighter was the primary fighter of the Minbari Federation. It was manufactured at the Valeria-On-High Orbital Shipyards over Minbar. The Minbari Nial fighter is one of the strongest fighters among the younger races. It sports an array of advanced systems, firepower and manoeuvrability. Armament consists of three light neutron fusion cannons, similar to those found on a Sharlin class warcruiser, but much less powerful. Defenses include a Minbari stealth system, making a weapons lock difficult for a lot of other races. Due to the fact that the ship is designed primarily for hit-and-run attacks, it carries only a limited air supply and has no jump capability of its own. It has higher speed and more armor than any other fighter among the younger races; it is outmatched in maneuverability only by the EarthForce Starfury. However, as a Nial's armor can absorb a large number of hits from Human weapons and the stealth system makes maintaining manual target lock difficult during high speed maneuvers, this was not a major detriment."
Foundation.ShipDef.MinbariNial.SubMenu = "Minbari Federation"
Foundation.ShipDef.MinbariNial.SubSubMenu = "Fighters"
# Yeah, we know it pollycristalline armour and polarized plating are NOT the same, but it works similarly enough for our purposes 
# I have been thinking of adding an stealth system that makes fire inancurate when firing... but who needs that with Kobayashi Maru's phaser innacuracy lol.
Foundation.ShipDef.MinbariNial.dTechs = {
	'Polarized Hull Plating': { "Plates": ["PolyCrystalline Armour"]
}}


if menuGroup:           Foundation.ShipDef.MinbariNial.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.MinbariNial.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

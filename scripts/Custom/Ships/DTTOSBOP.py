import App
import Foundation
import traceback

abbrev = "DTTOSBOP"
iconName = "DTTOSBOP"
longName = "Dark Timeline TOS T'liss"
shipFile = "DTTOSBOP"
species = App.SPECIES_GALAXY
menuGroup = "Dark Timeline Ships"
playerMenuGroup = "Dark Timeline Ships"

try:
	import Custom.Autoload.RaceDTTosRom
	Foundation.ShipDef.DTTOSBOP = Foundation.DTTosRomShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.DTTOSBOP = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.DTTOSBOP.desc = "A romulan ship from the TOS era of the Dark Timeline. With the loss of their homeworld, they developed a constant cloak to keep themselves hidden away and energy dissapating armor to absorb incoming fire if need be. During this era they were developing metaplasma based weapons, which heavily drained power, but were powerful in nature."
Foundation.ShipDef.DTTOSBOP.CloakingSFX = "EnergyRefractionCloak"
Foundation.ShipDef.DTTOSBOP.DeCloakingSFX = "EnergyRefractionDecloak"
Foundation.ShipDef.DTTOSBOP.SubMenu = "Romulan Ships"
Foundation.ShipDef.DTTOSBOP.SubSubMenu = "TOS"
Foundation.ShipDef.DTTOSBOP.OverrideWarpFXColor = Foundation.ShipDef.DTTOSBOP.OverrideWarpFXColor
Foundation.ShipDef.DTTOSBOP.OverridePlasmaFXColor = Foundation.ShipDef.DTTOSBOP.OverridePlasmaFXColor
Foundation.ShipDef.DTTOSBOP.dTechs = {
   "Fed Ablative Armor": {"Plates": ["Energy Dissapating Armor"]}
}


if menuGroup:           Foundation.ShipDef.DTTOSBOP.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DTTOSBOP.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
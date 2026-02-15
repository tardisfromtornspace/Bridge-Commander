##### Created by:
##### Bridge Commander Ship Menu Creator v5.6



import App
import Foundation
import traceback


abbrev = 'AventineClass'
iconName = 'AventineClass'
longName = 'U.S.S. Esrie'
shipFile = 'AventineClass'
species = App.SPECIES_GALAXY
# SubMenu
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'

try:
	import Custom.Autoload.RaceFutureFed25c
	Foundation.ShipDef.AventineClass = Foundation.FutureFed25cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.AventineClass = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()


Foundation.ShipDef.AventineClass.desc = "Aventine Class ship, most likely entered service in the 2410s."
Foundation.ShipDef.AventineClass.SubMenu = "2400s"
# Foundation.ShipDef.AventineClass.fMaxWarp
# Foundation.ShipDef.AventineClass.fCruiseWarp
Foundation.ShipDef.AventineClass.OverrideWarpFXColor = Foundation.ShipDef.AventineClass.OverrideWarpFXColor
Foundation.ShipDef.AventineClass.OverridePlasmaFXColor = Foundation.ShipDef.AventineClass.OverridePlasmaFXColor
Foundation.ShipDef.AventineClass.dTechs = {
	"Borg Attack Resistance": 25,
   'Transphasic Torpedo Immune': 1,
   'Phased Torpedo Immune': 1,
   'Breen Drainer Immune': 1,
   'Drainer Immune': 1,
   'Multivectral Shields': 12,
   'Ablative Armour': 20000,
   "Fed Ablative Armor": {"Plates": ["Forward Ablative Armor","Aft Ablative Armor","Port Ablative Armor","Starboard Ablative Armor","Dorsal Ablative Armor","Ventral Ablative Armor"]}}


if menuGroup:           Foundation.ShipDef.AventineClass.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.AventineClass.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

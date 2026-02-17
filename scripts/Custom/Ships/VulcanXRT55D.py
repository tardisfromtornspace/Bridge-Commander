import Foundation
import App

abbrev = 'VulcanXRT55D'
iconName = 'VulcanXRT55D'
longName = "Vulcan XRT55D"
shipFile = 'VulcanXRT55D' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
species = App.SPECIES_GALAXY
SubMenu = '28th Century'

Foundation.ShipDef.VulcanXRT55D = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.VulcanXRT55D.SubSubMenu = "Vulcan/Ni'var Ships"
Foundation.ShipDef.VulcanXRT55D.fMaxWarp = 9.99
Foundation.ShipDef.VulcanXRT55D.fCruiseWarp = 9.0

Foundation.ShipDef.VulcanXRT55D.desc = "In ENT: 'Future Tense', T'Pol and Archer spot a diagram of this vessel on the display device in Daniels's quarters. Considering the similarity to the Surak class, it shouldn't be commissioned too far into the future. The label next to the ship reads: 'RetroFitted Dorsal Carrier, Design XRT-55D, Commission Date 3125'."

Foundation.ShipDef.VulcanXRT55D.dTechs = {
	'Automated Destroyed System Repair': {"Time": 45.0, "DoNotInterfere": 1},
	'Breen Drainer Immune': 0,
	"Borg Attack Resistance": 60,
	'ChronitonTorpe Immune': 1,
	"Digitizer Torpedo Immune": 1,
	'Drainer Immune': 1,
	'Fed Ablative Armor': { "Plates": ["Forward Ablative Armour", "Aft Ablative Armour", "Port Ring Ablative Armour", "Star Ring Ablative Armour", "Ventral Ring Ablative Armour"]},
	"Inversion Beam": [12000, 0, 0.5, 1500],
	'Multivectral Shields': 25,
	"Power Drain Beam": [1500, 0, 0.5, 1500],
	'Phased Torpedo Immune': 1,
	"Reflector Shields": 2,
	'Reflux Weapon': 3800,
	'Regenerative Shields': 75,
	"SGReplicator Attack Resistance": 30,
	"TachyonBeam": {"Immune": -1},
	'Transphasic Torpedo Immune': 1,
	'Vree Shields': 55,
}


if menuGroup:           Foundation.ShipDef.VulcanXRT55D.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.VulcanXRT55D.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


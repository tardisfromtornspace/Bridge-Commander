##### Created by:
##### Bridge Commander Ship Menu Creator v2.1



import App
import Foundation



abbrev = 'DalekSaucer'
iconName = 'DalekSaucer'
longName = 'Dalek Saucer'
shipFile = 'DalekSaucer'
species = App.SPECIES_GALAXY
# SubMenu
menuGroup = 'Doctor Who'
playerMenuGroup = 'Doctor Who'
SubMenu = "Dalek"


Foundation.ShipDef.DalekSaucer = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.DalekSaucer.dTechs = {
	'Adv Armor Tech': 1,
	"AutoTargeting": { "Pulse": [2, 0] },
	'Breen Drainer Immune': 0,
	'ChronitonTorpe Immune': 1,
	'Drainer Immune': 1,
	"FiveSecsGodPhaser": 1,
	"Vree Shields": 100,
	"Phased Torpedo Immune": 1,
	'Reflux Weapon': 10000,
	'Regenerative Shields': 10#,
#	"Inversion Beam": [0.5, 0, 0.5, 1500],
#	"Power Drain Beam": [0.5, 0, 0.5, {1500}]
}
Foundation.ShipDef.DalekSaucer.bPlanetKiller = 1

Foundation.ShipDef.DalekSaucer.fMaxWarp = 9.99 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.DalekSaucer.fCruiseWarp = 9.999999999 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.DalekSaucer.desc = "By the time of the Etra Prime incident, Dalek ships were dimensionally transcendental and could use chameleon circuit technology; a new generation of Dalek saucer with increased firepower was built for the Last Great Time War."


if menuGroup:           Foundation.ShipDef.DalekSaucer.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DalekSaucer.RegisterQBPlayerShipMenu(playerMenuGroup)



if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

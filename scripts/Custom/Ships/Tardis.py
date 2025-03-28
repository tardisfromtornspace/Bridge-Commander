##### Created by:
##### Bridge Commander Ship Menu Creator v2.1



import App
import Foundation
# thank you Mario
from Custom.Autoload.RaceTimeLord import *


abbrev = 'Tardis'
iconName = 'TARDIS'
longName = "The Doctor's TARDIS"
shipFile = 'Tardis'
species = App.SPECIES_GALAXY
# SubMenu
menuGroup = 'Doctor Who'
playerMenuGroup = 'Doctor Who'
SubMenu = "Gallifreyan"


Foundation.ShipDef.Tardis = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "race": TimeLord })
Foundation.ShipDef.Tardis.dTechs = {
	'Adv Armor Tech': 1,
	'Breen Drainer Immune': 0,
	'ChronitonTorpe Immune': 1,
	'Drainer Immune': 1,
	"Phased Torpedo Immune": 1,
	'TimeVortex Torpedo Immune': 1
}
Foundation.ShipDef.Tardis.bPlanetKiller = 1

Foundation.ShipDef.Tardis.fMaxWarp = 8.0 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.Tardis.fCruiseWarp = 9.999999999 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.Tardis.desc = "T.A.R.D.I.S. - Time And Relative Dimensions In Space. A TARDIS is a product of the advanced technology of the Time Lords. A properly maintained and piloted TARDIS can transport its occupants to any point in time and space. The interior of a TARDIS is much larger than its exterior. It can blend in with its surroundings using the ship�s chameleon circuit. TARDISes also possess a degree of sapience and provide their users with additional tools and abilities including a universal translation system based on telepathy. In this case, this TARDIS is an obsolete type 40 Mark III, stolen model used by the renegade Time Lord 'The Doctor'. Its chameleon circuit is broken, leaving it stuck in the shape of a 1960s-style London police box after a visit to London in 1963. Despite that, it's extremely powerful and difficult to destroy. Its weight is enough to break a planet's surface."


if menuGroup:           Foundation.ShipDef.Tardis.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Tardis.RegisterQBPlayerShipMenu(playerMenuGroup)



if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

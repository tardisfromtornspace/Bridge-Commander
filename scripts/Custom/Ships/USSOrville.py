#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "USSOrville"
iconName = "USSOrville"
longName = "USS Orville"
shipFile = "USSOrville"
species = App.SPECIES_GALAXY
menuGroup = "The Orville Ships"
playerMenuGroup = "The Orville Ships"
SubMenu = "Planetary Union Ships"
Foundation.ShipDef.USSOrville = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })
Foundation.ShipDef.USSOrville.dTechs = {'Multivectral Shields': 40}

Foundation.ShipDef.USSOrville.desc = "The USS Orville, or ECV-197, is a mid-level exploratory vessel in Planetary Union service in the early 25th century. The Orville is one of 3,000 ships in the Planetary Union, within the Union's military wing with the purpose of exploring and charting the outer reaches of the Union's home quadrant of the galaxy. The ship has a compliment of 300 crewmembers.The craft's propulsion system, the quantum drive, is based on dysonium-powered quantum engines. The drive configuration on the Orville provides the ship with speeds in excess of 10 light years per hour. The ship also features a tractor beam that can be reversed to push objects away from the ship. The walls of the ship are made of a synthetic fiber that is an artificial sort of plant system, taking in carbon dioxide breathed out by the crew, and expelling oxygen.Tasked with the exploration of space, the Orville is not built for combat or warfare, though she does have respectable armaments to deal with unexpected dangers."


if menuGroup:           Foundation.ShipDef.USSOrville.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.USSOrville.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

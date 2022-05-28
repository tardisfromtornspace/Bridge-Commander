#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "whitestar"
iconName = "whitestar"
longName = "Whitestar"
shipFile = "whitestar"
species = App.SPECIES_GALAXY
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "Interestellar Alliance"
Foundation.ShipDef.whitestar = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })


Foundation.ShipDef.whitestar.desc = "The White Star was a class of advanced warships maintained by the Rangers and utilizing Minbari and Vorlon technology and served as the backbone of the Interstellar Alliance's fleet. They were manufactured at the Valen's Eye manufacturing point in the Minbari System. The first White Star was developed in secret by the Anla'shok, under the supervision of Kosh Naranek and Chosen One Jenimer throughout 2259. These ships were built to be both maneuverable enough to engage fighters, and to have the punch to take on capital ships when operating in groups. They were used as the predominant weapons in the Shadow War between 2259 and 2261 and proved themselves to be formidable vessels, taking on vessels many times their size and winning. This incredible performance is in part due to advanced Vorlon components found in the ship such as the bio-armoured hull which is capable of learning from experience and adapting itself to better protect the ship in new engagements; this hull design also gives the ship the ability to 'heal' itself after it has been damaged. These ships are also capable of creating their own jump point into hyperspace without using a jumpgate, giving these ships tremendous flexibility on the battlefield. "


if menuGroup:           Foundation.ShipDef.whitestar.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.whitestar.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

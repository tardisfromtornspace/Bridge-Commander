#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "vger"
iconName = "vger"
longName = "V'ger"
shipFile = "vger"
species = App.SPECIES_GALAXY
menuGroup = "Other Ships"
playerMenuGroup = "Other Ships"
Foundation.ShipDef.vger = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.vger.desc = "\"Appearing in Klingon space the Giant ship V\'ger plough straight to Earth in search for it\'s creator. Captain Kirk and his crew aboard the recently refited U.S.S Enterprise must try and stop V\'ger from wiping the carbon based infestation from the creators planet.\"\n\nThis ship is not fast of nimble, but watch any target disappear if they are hit by a plasma torpedo."


if menuGroup:           Foundation.ShipDef.vger.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.vger.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

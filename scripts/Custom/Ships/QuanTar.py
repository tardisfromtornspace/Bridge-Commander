##### Created by:
##### Bridge Commander Ship Menu Creator



import App
import Foundation



abbrev = 'QuanTar'
iconName = 'QuanTar'
longName = 'QuanTar'
shipFile = 'QuanTar'
species = App.SPECIES_GALAXY
# SubMenu
menuGroup = 'Other Ships'
playerMenuGroup = 'Other Ships'


Foundation.StarBaseDef.QuanTar = Foundation.StarBaseDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


# Foundation.StarBaseDef.QuanTar.fMaxWarp
# Foundation.StarBaseDef.QuanTar.fCruiseWarp
Foundation.StarBaseDef.QuanTar.desc = 'It is Believed to mean Trrap Explosion'


if menuGroup:           Foundation.StarBaseDef.QuanTar.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.StarBaseDef.QuanTar.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.StarBaseDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.StarBaseDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

import App
import Foundation


abbrev = "WCnxmirror"
iconName = "WCnxmirror"
longName = "Mirror NX-01"
shipFile = "WCnxmirror"
species = App.SPECIES_GALAXY
menuGroup = "Terran Empire ships"
playerMenuGroup = "Terran Empire ships"
Foundation.ShipDef.WCnxmirror = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCnxmirror.desc = "The ISS Enterprise (NX-01) was a Terran NX-class battle cruiser that was in service to Starfleet in the mid-22nd century. Mirror NX-01 by WileyCoyote"
Foundation.ShipDef.WCnxmirror.SubMenu = "NX Class"


if menuGroup:           Foundation.ShipDef.WCnxmirror.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCnxmirror.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def wcmirrorentIDSwap(self):
       retval = {"Textures": [["idmapmirror_glow.tga", "Data/Models/SharedTextures/WCnx01/wcmirrorentid_glow.tga"]]}
       return retval


Foundation.ShipDef.WCnxmirror.__dict__['SDT Entry'] = wcmirrorentIDSwap


import App
import Foundation

abbrev = "WCnxmirroravenger"
iconName = "WCnxmirror"
longName = "Mirror NX-09 Avenger"
shipFile = "WCnxmirroravenger"
species = App.SPECIES_GALAXY
menuGroup = "Terran Empire ships"
playerMenuGroup = "Terran Empire ships"
Foundation.ShipDef.WCnxmirroravenger = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCnxmirroravenger.desc = "The ISS Avenger (NX-09) was a Terran NX-class battle cruiser that was in service to Starfleet in the mid-22nd century. Avenger had fought for the Terran Empire in their war against rebels in the 2150s, and was one of several vessels destroyed by the starship USS Defiant during Jonathan Archer's power struggle for the throne of the Empire. Mirror NX-09 Avenger by WileyCoyote"
Foundation.ShipDef.WCnxmirroravenger.SubMenu = "NX Class"


if menuGroup:           Foundation.ShipDef.WCnxmirroravenger.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCnxmirroravenger.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def wcmirroravengerIDSwap(self):
       retval = {"Textures": [["mirrorgrayid_glow.tga", "Data/Models/SharedTextures/WCnx01/wcmirroravengerid_glow.tga"]]}
       return retval


Foundation.ShipDef.WCnxmirroravenger.__dict__['SDT Entry'] = wcmirroravengerIDSwap

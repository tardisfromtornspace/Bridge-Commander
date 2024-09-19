#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "USSVengeanceJJ"
iconName = "USSVengeance"
longName = "USS Vengeance"
shipFile = "USSVengeanceJJ"
species = App.SPECIES_GALAXY
menuGroup =  'Fed Ships'
playerMenuGroup = 'Fed Ships'
SubMenu = 'Section 31'
Foundation.ShipDef.USSVengeanceJJ = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

Foundation.ShipDef.USSVengeanceJJ.fMaxWarp = 9.0 + 0.0001
Foundation.ShipDef.USSVengeanceJJ.fCruiseWarp = 7.6 + 0.0001

Foundation.ShipDef.USSVengeanceJJ.dTechs = {'Ablative Armour': 7500}

Foundation.ShipDef.USSVengeanceJJ.desc = "The USS Vengeance was a 23rd century Federation Dreadnought-class starship operated in secret by Starfleet via Section 31. Unlike other ships owned by the Federation and operated by Starfleet, it was created specifically for combat and was completely unmarked, with no registry number or nomenclature visible on the hull. The ship was commissioned in 2259 and it was launched from the Io Facility starbase, a spacedock in orbit of the Jovian moon Io. Its first, and only, commanding officer was Admiral Alexander Marcus. As of 2263, it was by far the largest ship operated by Starfleet."


if menuGroup:           Foundation.ShipDef.USSVengeanceJJ.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.USSVengeanceJJ.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

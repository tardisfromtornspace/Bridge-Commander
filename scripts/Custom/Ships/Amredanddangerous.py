#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Amredanddangerous"
iconName = "proximarefit"
longName = "NX Armed And Dangerous"
shipFile = "Amredanddangerous"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.Amredanddangerous = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.Amredanddangerous.desc = " Welcome to ships history database. In this submenu has the story of the Proxima Refit\nclass.\n\nThe Proxima Refit was made by the orders of Admiral Maciej Napilocki, Admiral Vladislav Goranov and Admiral Milen Petrov. These 3 admirals are captains of an Yorktown class starships and they love their Yorktown Refits, so they have decided to make an upgraded and more complicated Yorktown with several hulls. They succeded with the help of the most clever scientiest and computer simulations in the quadrant to make stronger, a piece of Constitution Refit armour and hull. They have also taken the Excelsior\'s Shield Generator and made wider the electron streams and the Shield capacity was greater but the shield emmiters overloaded in the second minute, so they made a request to Starfleet to make a more durable emmiters, and a months later the ship was almost ready. For the photon torpedoes they though about antimatter quantum space-time warping and this made the Photon Torpedo much stronger than other photons. This Photon Torpedo was the ancestor of the Quantum Torpedo. The phasers are from Constitution Refit phasers with more durable electron circuits, wider circuits and are bit stronger. The NX Armed and Dangerous was the first Proxima Refit ship in history. Later in USS Proxima, the admirals sent their children for a part of the bridge crew.sd"
Foundation.ShipDef.Amredanddangerous.SubMenu = "Proxima class"
Foundation.ShipDef.Amredanddangerous.fMaxWarp = 9.1 + 0.0001
Foundation.ShipDef.Amredanddangerous.fCruiseWarp = 7 + 0.0001
Foundation.ShipDef.Amredanddangerous.fCrew = 580
Foundation.ShipDef.Amredanddangerous.dTechs = {
	"TMPWarpStartUp": {
		"track": {
			"Fca4_glow": {
				0.0: "Data/models/ships/Proxima Class/Proxima Refit/Fca4_glow.tga", 
				1.0: "Data/models/ships/Proxima Class/Proxima Refit/Warp_Glow.tga",

	
					}
				}
			}
		}








if menuGroup:           Foundation.ShipDef.Amredanddangerous.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Amredanddangerous.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

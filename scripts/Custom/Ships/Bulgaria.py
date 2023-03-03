#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Bulgaria"
iconName = "Bulgaria"
longName = "NX-Bulgaria"
shipFile = "Bulgaria"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.Bulgaria = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.Bulgaria.desc = "USS Bulgaria NX-352 a variant of Yorktown class is the most powerful vessel of its class built in the years of 2162 to 2214. \nShe has an upgraded weapons, phasers are a little bit weaker than phasers installed in the Constitution class refit. The NX-Bulgaria is only a prototype multirole battlcruiser, hull plating is stronger than Constitution\'s hull. The ship has a long story. USS Bulgaria was built in November 2179. It came into service since March 2163 to December 2269. on stardate 2163 USS Bulgaria has been dispatched to study wormhole activity near Sector 001. When the voids - a mysterious race federation never met before - came through the wormhole, they opened fire upon the Bulgaria, during the attack, Bulgaria\'s Captain along with his first officer died in explosion on the bridge caused by torpedo hit. Lt.Cmd Goranov had to assume command of the battered cruiser, in desperate struggle to save lifes of his crew he ordered to move all anti matter from the warp drive into the containers and put them in escape pods, after launching last escape pod filled with anti matter containers crew programmed them to fly near the wormhole and then detonated them with single phaser shot. Explosion blast closed the wormhole, minutes later reinforcements came to aid outnumbered and outganned USS Bulgaria, soon the battle was over, The Voids haven\'t appeard in Federation space for centuries. The Bulgaria has been finally refited and renamed to USS-Kaspichan NCC-1123 after \ngreat captain from the little town in Bulgaria called Kaspichan. The Captain\'s name is Vladislav Goranov. The ship was given into command of Cpt. Goranov for his actions to prevent the Voids invasion on Earth. Bulgaria under new name - USS Kaspichan left drydock in 2180 with refitted weapons systems and brand new sensors aray along wih modified warp drive. USS Kaspichan served well through nearly 200 years and gone through quite a few major refits in 2214(installed prototype shields system) and 2289, in 2352 ship gone through massive refit which included reconstruction and redesigning of almost entire structure as well as updating armaments, drive and internal system with all new technology like new shields and faster, more efficient transporters."
Foundation.ShipDef.Bulgaria.SubMenu = "Yorktown Class"
Foundation.ShipDef.Bulgaria.fMaxWarp = 5.5 + 0.0001
Foundation.ShipDef.Bulgaria.fCruiseWarp = 3.2 + 0.0001
Foundation.ShipDef.Bulgaria.fCrew = 140
Foundation.ShipDef.Bulgaria.dTechs = {
	'Polarized Hull Plating': { "Plates": ["Hull"]
}}


if menuGroup:           Foundation.ShipDef.Bulgaria.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Bulgaria.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

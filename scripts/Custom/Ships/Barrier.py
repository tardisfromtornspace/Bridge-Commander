import Foundation
import App

abbrev = 'Barrier'
iconName = 'Barrier'
longName = 'Barrier Class'
shipFile = 'Barrier' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
species = App.SPECIES_GALAXY

Foundation.ShipDef.Barrier = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

Foundation.ShipDef.Barrier.fMaxWarp = 9.975
Foundation.ShipDef.Barrier.fCruiseWarp = 8.6
Foundation.ShipDef.Barrier.dTechs = { 'Breen Drainer Immune': 1, 'Ablative Armour': 9250 }

Foundation.ShipDef.Barrier.desc = "Barrier Class Federation Battle cruiser - 527m\n\nBarrier class ships are pure battle cruisers based upon the primary hull characteristics of the Sovereign class but in a more compact design, thus  resulting in a stronger hull and higher impulse speeds and maneuverability than the larger Sovereign.  Most of the interior space is devoted to  shuttle bays, propulsion systems, and weapons with little in the way of scientific capability or modularity.  The Barrier's armament is potent for a  vessel its size and is arranged to deliver devastating alpha strikes and full 360 degree phaser coverage.  Regenerative shielding and several  centimeters of Ablative Armor serve as defense, along with the vessel's surprising agility.\n\nThis ship has one unique feature: a detachable weapons pod that operates as an independent sub light Attack Wing providing the Barrier with  Multivectoral Attack Mode capabilities.  It is a formidable craft for its size, equipped with advanced targeting sensors, weapons systems, and  defenses, its sleek design gives it good handling characteristics in an atmosphere and provides fleet and base defense as well as support for ground  troops, and securing planetary and small space targets."

if menuGroup:           Foundation.ShipDef.Barrier.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Barrier.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
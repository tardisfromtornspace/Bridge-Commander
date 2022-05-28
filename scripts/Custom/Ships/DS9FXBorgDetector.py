import App
import Foundation

abbrev = "DS9FXBorgDetector"
iconName = "DS9FXBorgDetector"
longName = "Borg Detector"
shipFile = "DS9FXBorgDetector"
species = App.SPECIES_GALAXY
menuGroup = "Borg Ships"
playerMenuGroup = "Borg Ships"

Foundation.ShipDef.DS9FXBorgDetector = Foundation.BorgShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.DS9FXBorgDetector.SubMenu = "Borg Ships"
Foundation.ShipDef.DS9FXBorgDetector.fMaxWarp = 9.99 + 0.0001
Foundation.ShipDef.DS9FXBorgDetector.fCruiseWarp = 9.99 + 0.0001
Foundation.ShipDef.DS9FXBorgDetector.fCrew = 30

Foundation.ShipDef.DS9FXBorgDetector.desc = "------- DESCRIPTION -------\nThe Detector\'s function in the Collective is to explore areas of space, evaluate their importance, and report its results to the Collective. The Detector is equipped with 3 powerful forward rapid-firing energy cannons. The Detector requires minimal drones to perform its function. Altho the Borg Detector is a relatively weak Borg ship, it can easily match a Galaxy Class Federation ship.\n\n------- TACTICS -------\nThe ship is highly maneuverable, take advantage of that and avoid enemy weapons. Fire the energy cannons as much as possible as they are very effective against enemy shields and weapons. When fighting the Detector, try and avoid the cannons and concentrate on destroying them as quickly as possible as it will render the Detector powerless.\n\n------- SHIP STATS -------\n\nHull Rating: 25000\n\nShield Rating:\n     Fore - 30000 @ 50chg\n     Aft - 30000 @ 50chg\n     Dorsal - 30000 @ 50chg\n     Ventral - 30000 @ 50chg\n     Port - 30000 @ 50chg\n     Starboard - 30000 @ 50chg\n\nImpulse Engines:\n     Max Speed - 9.99\n     Max Accel - 5.9\n     Max Ang Velocity - 1.5\n     Max Ang Accel - 1.5\n\nWarp Engines:\n     Max Warp - 9.99\n     Max Cruise Warp - 9.99\n\nCrew Complement: 30\n\n------- SHIP WEAPONS -------\n\nPulse Torpedoes:\n   3xF\n     Max Chg - 6\n     Max Dmg - 700\n     Min Firing Chg - 6\n     Rechg Rate - 0.12\n     Cooldown Time - 0.6\n\n------- SYSTEMS STATS -------\n\nCortical Node:\n     Max Condition - 30000\n     Repair Complexity - 1\n     Disabled Percentage - 0.1\n     Power Output/Sec - 5875\n     Main Battery Limit - 600000\n     Backup Battery Limit - 600000\n     Main Conduit Capacity - 6875\n     Backup Battery Capacity - 1000\n\nHull:\n     Max Condition - 25000\n     Repair Complexity - 1\n     Disabled Percentage - 0.15\n\nPulse Torpedo Bays:\n   3xF\n     Max Condition - 10000\n     Repair Complexity - 1\n     Disabled Percentage - 0.5\n\nPulse Torpedo System:\n     Max Condition - 20000\n     Repair Complexity - 1\n     Disabled Percentage - 0.15\n     Normal Power/Sec - 500\n\nRepair System:\n     Max Condition - 20000\n     Repair Complexity - 1\n     Disabled Percentage - 9\n     Maximum Repair Points - 550\n     Repair Teams - 9\n\nSensor Array:\n     Max Condition - 25000\n     Repair Complexity - 1\n     Disabled Percentage - 0.15\n     Normal Power/Sec - 800\n     Max # of Probes - 50\n     Sensor Base Range - 2000\n\nShield Matrix:\n     Max Condition - 30000\n     Repair Complexity - 1\n     Disabled Percentage - 0.15\n     Normal Power/Sec - 1200\n\nTractor Beam Emitters:\n   3xF  \n     Max Condition - 3000\n     Repair Complexity - 4\n     Disabled Percentage - 0.5\n\nTractor Beam System:\n     Max Condition - 6000\n     Repair Complexity - 5\n     Disabled Percentage - 0.5\n     Normal Power/Sec - 900\n\n------- ENGINE PROPERTIES -------\n\nImpulse Engines:\n     Max Condition - 10000\n     Repair Complexity - 1\n     Disabled Percentage - 0.25\n     Normal Power/Sec - 300\n\n   Impulse 1:\n     Max Condition - 4800\n     Repair Complexity - 3\n     Disabled Percentage - 0.5\n\n   Impulse 2:\n     Max Condition - 4800\n     Repair Complexity - 3\n     Disabled Percentage - 0.5\n\nWarp Engines:\n     Max Condition - 10000\n     Repair Complexity - 3\n     Disabled Percentage - 0.5\n     Normal Power/Sec - 300"

if menuGroup:           Foundation.ShipDef.DS9FXBorgDetector.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DS9FXBorgDetector.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

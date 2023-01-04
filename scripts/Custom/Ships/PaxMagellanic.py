#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "PaxMagellanic"
iconName = "PaxMagellanic"
longName = "Pax Magellanic"
shipFile = "PaxMagellanic"
species = App.SPECIES_GALAXY
menuGroup = "Andromeda"
playerMenuGroup = "Andromeda"
SubMenu = "System´s Commonwealth"
Foundation.ShipDef.PaxMagellanic = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.PaxMagellanic.dTechs = {
	"AutoTargeting": { "Torpedo": [8, 1] },
	'Breen Drainer Immune': 1,
	'Multivectral Shields': 10,
        "Reflector Shields": 50,
	'Fed Ablative Armor': { "Plates": ["Armour"]
}}
Foundation.ShipDef.PaxMagellanic.bPlanetKiller = 1

Foundation.ShipDef.PaxMagellanic.desc = "The Pax Magellanic was a Glorious Heritage Class vessel, serial number XMC-1-913 constructed in the Newport News Orbital Shipyards above Earth. Captain Warrick, and then Lieutenant Jill Pearce were its final commanders. The first of its line, her sister Artificial Intelligence's considered the Pax to be the eldest of all the Glorious Heritage Class warships. Originally, her nickname was Maggie, but she later altered this nickname along with her avatar's appearance to Jill. During her long years of service, Magellanic saved Princess Sukarhit from a Magog attack on her first mission, receiving honors from both the Vedran Empress and the Triumvirate. During the Nietzschean Rebellion, the Magellanic was dispatched to the Herodotus system to reinforce and assist General Sky Falls in Thunder. Captain Warrick and his Lancers were dispatched to the planet but were quickly overwhelmed. In response more crewman from the Magellanic rallied to battle dropping planetside until the Pax had virtually no crew left. To avoid the Magellanic's capture, Warrick ordered the Artificial Intelligence to self-destruct. However, the Pax couldn't believe this coming from one she loved, seeing it as a betrayal. Despondent, she ejected her Slipstream Core, incinerating the planet and everyone on it. Without her FTL travel capability and main engines damaged she was left isolated in the debris of the destroyed planet. The Artificial Intelligence then made android copies of most of the original crew, using the ship's medical logs to recreate them hoping to remedy her loneliness and gain a crew to operate and maintenance her facilities. After 300 years of confinement in the singularity of a black hole, the Andromeda Ascendant arrived in the system with Captain Hunt and his crew, who hoped to salvage the ship so that his cause to resurrect the Systems Commonwealth would have another powerful warship. However, after the crew discovered Jill's secret and, the Magellanic began attacking them with her androids and they were forced to flee the ship. The Magellanic then started to fire on Andromeda, and when the Andromeda returned fire, Jill intentionally lowered her Antiproton Cannons and her other defenses so that she would be inadvertently destroyed by her sister ship. It was Jill's way of escaping her painful history. As well as her sister, its design, maneuverability, Valiant offensive missiles, Nova Bomb Torpedoes, Point Defense Lasers, Anti-Gravity Fields, Fullerene-Ablative-Reactive Armor and self-repair nanobots makes her a deadly enemy, specially at great distances."


if menuGroup:           Foundation.ShipDef.PaxMagellanic.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.PaxMagellanic.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "MillionVoices"
iconName = "MillionVoices"
longName = "Million Voices"
shipFile = "MillionVoices"
species = App.SPECIES_GALAXY
menuGroup = "Andromeda"
playerMenuGroup = "Andromeda"
SubMenu = "System´s Commonwealth"
Foundation.ShipDef.MillionVoices = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.MillionVoices.dTechs = {
	"AutoTargeting": { "Torpedo": [8, 1] },
	'Breen Drainer Immune': 1,
	'Multivectral Shields': 15,
        "Reflector Shields": 35,
	'Fed Ablative Armor': { "Plates": ["Armour"]
}}
Foundation.ShipDef.MillionVoices.bPlanetKiller = 1

Foundation.ShipDef.MillionVoices.desc = "The Million Voices, also known as Milla, was a Glorious Heritage Class warship that was captured by the Drago-Kazov Pride and brought into the Tartarus System. She was the second in command to the Wrath of Achilles while they were prisoners of the Nietzscheans. Once in the Tartarus system, she increased her Artificial gravity fields and crushed them. However, they had marooned her as well as 50 other High Guard ships in the system. The Drago-Kazov hoped to use the ships as tools. This was not to be, as their Artificial Intelligences proved too powerful to overcome. The Million Voices was one of the strongest agitators against rejoining the New Systems Commonwealth, believing that her commanders had lost the war because they had refused to listen to the Artificial Intelligences. After Dylan Hunt agreed that the Ships would have the choice to either help the new Commonwealth as equals or not after they escaped, Milla and the others consented to join. She ultimately sacrificed herself when the Drago-Kazov attempted to destroy the fleet; Milla and several other ships providing a decoy while the rest escaped. As several other Glorious Heritage Class ships, its design, maneuverability, Valiant offensive missiles, Nova Bomb Torpedoes, Point Defense Lasers, Anti-Gravity Fields, Fullerene-Ablative-Reactive Armor and self-repair nanobots makes her a deadly enemy, specially at great distances."


if menuGroup:           Foundation.ShipDef.MillionVoices.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.MillionVoices.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

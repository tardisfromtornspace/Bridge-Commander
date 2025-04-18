#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback

abbrev = "FutAOH"
iconName = "FutAOH"
longName = "Future Avenger of Harmony"
shipFile = "FutAOH"
species = App.SPECIES_GALAXY
menuGroup = "Starlight's Dithetaverse"
playerMenuGroup = "Starlight's Dithetaverse"


try:
	import Custom.Autoload.RaceFutAOH
	Foundation.ShipDef.FutAOH = Foundation.FutAOHShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.FutAOH = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.FutAOH.desc = "This is the Future Avenger of Harmony. This is based in my own storyline called Starlight's Dithetaverse (unless I expand it). Like the Sic Mvndvs circulum, it's based off of multiple levels of existence, each exponentially more powerful than the last, but that's where the story ends. There are currently about 9 discrete infinitely expanding planes of existence as well as the spaces between them. There are many races existing within the story, but the AOH is rather special. The original AOH was formed when a mysterious race later simply named the Void destroyed an entire pocket multiverse whose prime origin point was a race that lived in perfect peace, unity and harmony, but they possessed extremely powerful magic naturally fused with their biology, and thus were seen as a threat by the Void. The Void tore apart their pocket multiverse, but it had an unexpected effect of releasing their spirits, magic, sorrow and desires out into the cosmos and coalesced into a singular entity of pure magic, called the Avenger of Harmony. Its goal is to protect similar timelines to its original one, destroy injustice and wanton destruction of life wherever it can reach, and to avenge the destruction that originally created it. Over time it met many races, evolved its consciousness to work even more in unison, and moved to higher planes and higher power. Given that Starlight's Dithetaverse has its fundamentals literally based in magic and the AOH can access all of the magic potential of its current highest plane of existence as well as all the lower ones and everything in between, it's generally considered by this point to be the strongest existing thing in the entire story. This particular version is a Future Version, and there are currently plans to make at least three more that are exponentially more powerful. This version is equipped with Chaos Unity Beams, Harmony Pulses, Solunar Torpedoes, and Dusk Torpedoes. Each one has custom sounds and appearances that I designed and Greystar converted into the necessary files and textures. Any number of the ships in my story are far stronger than traditional ideas because of the sheer power and technological potential of magic. This version alone is capable of taking on a fleet of 29th century temporal borg with absolute ease. While not as strong as the Exile, it generally is matched in firepower with the kind of stuff in the circulum around the power of a Mk II Tradophian Battlecruiser."

Foundation.ShipDef.FutAOH.CloakingSFX = "FutAOHCloakOn"
Foundation.ShipDef.FutAOH.DeCloakingSFX = "FutAOHCloakOff"
Foundation.ShipDef.FutAOH.SubMenu = "Avenger of Harmony"
Foundation.ShipDef.FutAOH.OverrideWarpFXColor = Foundation.ShipDef.FutAOH.OverrideWarpFXColor
Foundation.ShipDef.FutAOH.OverridePlasmaFXColor = Foundation.ShipDef.FutAOH.OverridePlasmaFXColor
Foundation.ShipDef.FutAOH.bPlanetKiller = 1
Foundation.ShipDef.FutAOH.fMaxWarp = 15.0
Foundation.ShipDef.FutAOH.fCruiseWarp = 10

Foundation.ShipDef.FutAOH.dTechs = {
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
	'Adv Armor Tech': 1,
	'ChronitonTorpe Immune': 1,
	'Phased Torpedo Immune': 1,
	'Phase Cloak': 0,
	'Reflux Weapon Immune': 1,
	'Total Immunity': 1,
	'TimeVortex Torpedo Immune': 1,
	"Digitizer Torpedo Immune": 1,
	'Davros Reality Bomb Immune' : 1,
	"Transphasic Torpedo Immune" : 1,
    "TachyonBeam": { "Immune": 1 },
	'Automated Destroyed System Repair': {"Time": 18.0, "DoNotInterfere": 0},
	'Defensive AOE Siphoon' : { "Resistance": 5.0},
	"SG Plasma Weapon Immune": 1,
	"SGReplicator Attack Resistance": 100,
	"SG Ori Beams Weapon Immune": 1,
	"SG Ion Weapon Immune": 1,
	"SG Asgard Beams Weapon Immune": 1,
	"GraviticLance": { "Immune": 1},
	"Tachyon Sensors":  1.0,
	"Inversion Beam": [1.0, 0.0, 0.0, 0.0],
	"Power Drain Beam": [1.0, 0.0, 0.0, 0.0]
}

if menuGroup:           Foundation.ShipDef.FutAOH.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.FutAOH.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

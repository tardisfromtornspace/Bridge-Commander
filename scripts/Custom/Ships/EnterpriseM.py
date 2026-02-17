import App
import Foundation
import traceback

abbrev = "EnterpriseM"
iconName = "EnterpriseM"
longName = "U.S.S Enterprise M"
shipFile = "EnterpriseM"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"

try:
	import Custom.Autoload.RaceFutureFed28c
	Foundation.ShipDef.EnterpriseM = Foundation.FutureFed28cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.EnterpriseM = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.EnterpriseM.desc = "In 2749, the first generation of ships specifically designed for temporal investigation were constructed and launched. These were the first Timefleet Timeships put into service, with the Enterprise M being the first assigned to complete temporal missions. It was equipped with Chrono-Nadion arrays, a Subatomic Disruptor cannon and temporal phased pulses. It is equipped Type 20 Quantums, Temporal Poleron and Temporal Singularity torpedoes as well. It had a Transcendental interior housing a crew of 270 individuals, as well as having temporal shielding to protect the crew from changes to history. It had first generation Temporal Transporters, which werent as powerful as the wells, but they could get the job done. Its external hull is made of a hardened Polyduranide alloy and the internal armor is made of a charged Rodinium alloy that is tough to break through. It is equipped with a Temporal Drive, which allows it to time travel, hyper impulse engines as well as both warp and slipstream drives, which are all powered by a Chroniton Core. Ships of the Song Class were retired and decommissioned in 2783 in favor of the second generation of Timeship, the Klein Class (with the Wells Class being the third installment in the lineage). During its service, the Song Class assisted in the Temporal Cold War and even met some of its Descendants upon traveling to the 29th, 30th and 31st centuries, even meeting some of them in the past, such as the USS Relativity-G and the USS Continuum."
Foundation.ShipDef.EnterpriseM.fMaxWarp = 12 + 1.0
Foundation.ShipDef.EnterpriseM.fCruiseWarp = 9.9999993 + 1.0
Foundation.ShipDef.EnterpriseM.OverrideWarpFXColor = Foundation.ShipDef.EnterpriseM.OverrideWarpFXColor
Foundation.ShipDef.EnterpriseM.OverridePlasmaFXColor = Foundation.ShipDef.EnterpriseM.OverridePlasmaFXColor
Foundation.ShipDef.EnterpriseM.dTechs = {
	'Adv Armor Tech': 1,
	'Ablative Armour': 87500,
	"Alternate-Warp-FTL": {
		"Setup": {
			"DrWTimeVortexDrive": {	"Nacelles": ["Dorsal Drive Stabilizer", "Ventral Drive Stabilizer"], "Core": ["Chroniton Core", "Temporal Drive", "Temporal Shield Generator"], },
		},
	},
	'Automated Destroyed System Repair': {"Time": 45.0, "DoNotInterfere": 1},
	"Borg Attack Resistance": 75,
	'Breen Drainer Immune': 0,
	'ChronitonTorpe Immune': 1,
	'Digitizer Torpedo Immune': 1,
	'Drainer Immune': 1,
	"Inversion Beam": [0.5, 0, 0.5, 1500],
	'Multivectral Shields' : 25,
	"Power Drain Beam": [0.5, 0, 0.5, 1500],
	"Phase Cloak": -1, 
	'Phased Torpedo Immune': 1,
	"Reflector Shields": 2,
	'Reflux Weapon': 1000,
	'Regenerative Shields': 60,
	"SGReplicator Attack Resistance": 40,
	"SG Asgard Beams Weapon Immune": 2,
	"SG Ion Weapon Immune": 2,
	"SG Ori Beams Weapon Immune": 2,
	"SG Plasma Weapon Immune": 2,
	"SG Railgun Weapon Immune": 2,
	"Subatomic Disruptor Beams Weapon": [{"HullDmgMultiplier": 1000.0, "ShieldDmgMultiplier": 15000.0, "Beams": ["Subatomic Disruptor"]}, ["ProtoSubatomicDisruptor"]],
	"TachyonBeam": {"Immune": -1},
	'Transphasic Torpedo Immune': 1,
	'Vree Shields': 55,	
}

Foundation.ShipDef.EnterpriseM.SubMenu = "28th Century"

Foundation.ShipDef.EnterpriseM.CloakingSFX   = "ChronomaticCloak"
Foundation.ShipDef.EnterpriseM.DeCloakingSFX = "ChronomaticUncloak"


if menuGroup:           Foundation.ShipDef.EnterpriseM.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.EnterpriseM.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
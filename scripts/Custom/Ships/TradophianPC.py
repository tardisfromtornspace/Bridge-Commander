#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback

abbrev = "TradophianPC"
iconName = "TradophianPC"
longName = "Tradophian Perfected Cruiser"
shipFile = "TradophianPC"
species = App.SPECIES_GALAXY
menuGroup = "Sic Mvndvs Circulum"
playerMenuGroup = "Sic Mvndvs Circulum"


try:
	import Custom.Autoload.RaceTradophian
	Foundation.ShipDef.TradophianPC = Foundation.TradophianShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.TradophianPC = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.TradophianPC.desc = "Perfected Cruiser:\nThe Perfected Cruiser was a top-secret project commissioned by the Consolidation of Reality for one and only purpose. That purpose being to combat the threat to all realities, The Exile. Tradophians usually limit the amount of technology and weapons they use in their systems, but because of the threat the exile posed to not only the Tradophians or their allies, but to every single reality to ever exist. The construction of the Perfected Cruiser took nearly 1000 years due to all of the technology shoved into it. As The Exile used modified Tradophian Tech, modified specifically for destructive purposes, and a machine race had 157,539 years to advance the technology before The Exiles launch. Even with advanced dimensional and transcendental tech, the Perfected Cruiser has less powerful weaponry, but more powerful shields and armor due to the pure size of the systems and hull. The Perfected Cruisers mission is to hunt down and destroy the exile, no matter the cost or time. The Perfected Cruiser and The Exile had a few run-ins before the final battle. These small interactions usually ended up with one of the ships being heavily damaged, then disabling the other ship's drives and escaping to repair and gaining too much ground to catch up to without a full repair. The chase between The Exile and the Perfected Cruiser lasted for around 32,000 years before the final battle commenced, leaving The Exile destroyed and the Perfected Cruiser heavily damaged. Because of this damage, it took them another 2,300 years to repair it and get back to their home universe where the Perfected Cruiser was decommissioned and placed into a museum for remembrance of the end of the war.\n\nShields:\nThis ship is equipped with an Exotic Hypermatter shield, which is rather weak, but utilizes a certain phase of Hyper-Charged fluidic matter that absorbs almost all types of energy. While the shields are relatively weak physically speaking, the drop in stabilization of a shield face when energy is applied to it allows the shields to be almost invulnerable to anything. With each hit, the shields absorb about 90-95 percent of all incoming energy that could cause harm to it.\n\nHypermatter Shield Faces:\nFront: 175,000,000 with 5000 Charge\nRear: 175,000,000 with 5000 Charge\nPort: 175,000,000 with 5000 Charge\nStar: 175,000,000 with 5000 Charge\nDorsal: 175,000,000 with 5000 Charge\nVentral: 175,000,000 with 5000 Charge\n\nArmor:\nThe Perfected Cruiser is equipped with a special kind of transcendental material known as Calbrakium. This material is 5 times as dense as the heart of a Neutron Star. This extreme density and weight give the ship 4th and 5th dimensional protective properties. The Perfected Cruiser itself has layered 100  percent Calbrakium armor plating and the hull is also 100 percent layered Calbrakium, both of which have fluidic Transcendental properties.\n\nCalbrakium Armor: 550,000,000\nCalbrakium Hull: 375,000,000\n\nBeam Weapons:\nThe Perfected Cruiser is equipped with Mk.Infinity (HV) Riftic Type Beams. These beams manipulate sub space-time and use distortions in 3rd and 4th dimension to tear objects apart. These arrays are more powerful than the ones on the Galaxy Cruiser.\n\nBeam Weapon Damage: 15,000,000\nBeam Weapons: Tribunal beam Fore, Aft, Port, Star, Dorsal, Ventral\n\nSubspace Pulses:\nThe Perfected Cruiser also comes equipped with Hyper-subspace singularity pulse generators, which act similarly to the beam weapons, but on a much lighter scale.\n\nTotal Subspace Pulse Ports: 4\nHyper Subspace Damage: 65,000\n\nTorpedo Generator:\nThe Torpedo Generator system aboard the Tradophian ships use compressed phasing matter to generate phasing devices that output a certain yield or energy type depending on the situation.\n\nTorpedo tube number: 18\n\nBosonic Torpedo:\nThe Bosonic Torpedo was designed as a specialty torpedo on the Perfected Cruiser. Each one of these torpedoes is an overloaded Boson Core. How they work is when too much supercritical matter/energy hybrid is introduced into a Boson Core, the core becomes unstable because of the extreme build up of the Bosons charging. See when a Boson, which converts matter to energy, and back again, meets something that is neither and both matter and energy, it charges, and if you let it charge for too long, you can create some of the most powerful weapons that this universe has seen. (Comp:5,000)\n(Damage:150,000) \n\nKinetic Transcendental Neutronium Torpedo:\nThe Kinetic Transcendental Neutronium Torpedo is a kind of super powerful torpedo manufactured by the Tradophians. Basically, to put it simply, this torpedo is a 4th and 5th dimensional glob of phased neutrinos compressed into a special kind of neutronium that can rip through almost everything known, including other Tradophian ships. (Comp:2,500)\n(Damage:650000)\n\nFalse Vacuum Decay Devices:\nThe Vacuum decay devices are weapons of unimaginable power. Hence why there are only two of them. In full power, the single particle inside of them could annihilate an entire universe in 15 minutes. However, on lower setting, it generates a field of void element around the device and reduces the target and anything inside into Quarks.(Comp:20)\n(Damage:????)\n\nTimestream Cloak:\nThe Timestream Cloak on this ship isolates the ship, all of its systems and all of the crew inside from the current timeline via a Temporal Refraction Matrix hooked into a Temporal Refraction array. Once it is deactivated, the ship and everything in it are reintegrated into the timestream they are in. \n\nBoson Core:\nThe Boson Core equipped on this ship uses the well known 'Higgs Boson' particle. This particle, known for converting energy to matter and back again, is the heart of the Tradophian ships. They put a cloud of 99.9997253% pure bosons into the reactor core by first flying to the edge of the universe they are currently in. The edge of the universe is a mass of boson particles still creating and expanding the universe. They then activate a special kind of beam that they nickname the 'Boson Scoop' which locks the boson particles in a higher dimensional cage. and places them in a secondary device called the 'Foreign Neutralizing Core' This device utilizes carefully calculated and charged sub-spatial energy to clump foreign particles while keeping the boson particles intact. The particles are then fed through a higher dimensional mesh like substance, beaming all foreign particles back into space while letting the boson particles pass through. It is never 100% pure, as some particles smaller than quarks cling to the bosons. The bosons are then put in a deadlock chamber and slowly introduced into the main core. The core must be shut off during this introduction process, which usually takes a few hours, with the ships main systems running off of reserve power. The introduction process has many deadlock barriers set in place, so sabotage or critical failures are virtually impossible and reactions would instantly be neutralized and the core shut down. The core is repowered once everything is re-secured and in place and the core begins its processes. The Bosons are then exposed to extremely high pressure fluidic-dimensional energy. This energy is matter that was temporally altered to move hundreds of times the speed of light, blurring the line between matter and energy, in effect creating a supercritical state between the two. The boson particle, when exposed to this supercritical fluid, becomes supercharged as the energy on top of it is neither matter nor energy. It cannot convert either to either, so a reaction starts where the boson particle attempts to convert the fluid to both states at the same time. This causes energy to stack and overcharge the bosons. The bosons, reaching their limit, shoot off hypercharged bosonic micro radiation, which is shot through the inner solid layer of the core and into the secondary solid outer layer, which absorbs the radiation and charges up. Once the outer core reaches a critical state, it will start distributing the energy given off by the core to the main power grid. The outer core is quite a spectacle when you observe it. It will strobe through random colors on the spectrum at random intervals. A single charge of bosons can last upwards of 15000 years at a time as the drop in energy of the bosons is quite small and takes a long time until the bosons burn themselves out in this kind of environment."
Foundation.ShipDef.TradophianPC.fMaxWarp = 15.0
Foundation.ShipDef.TradophianPC.fCruiseWarp = 13.0
Foundation.ShipDef.TradophianPC.bPlanetKiller = 1
Foundation.ShipDef.TradophianPC.OverrideWarpFXColor = Foundation.ShipDef.TradophianPC.OverrideWarpFXColor
Foundation.ShipDef.TradophianPC.OverridePlasmaFXColor = Foundation.ShipDef.TradophianPC.OverridePlasmaFXColor
Foundation.ShipDef.TradophianPC.SubMenu = "Tradophian Ships"
Foundation.ShipDef.TradophianPC.CloakingSFX   = "TemporalDeintegration"
Foundation.ShipDef.TradophianPC.DeCloakingSFX = "TemporalReintegration"
Foundation.ShipDef.TradophianPC.dTechs = {
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
	"Transphasic Torpedo Immune" : 1,
	'Davros Reality Bomb Immune' : 1,
	"Vaccum Decay Protection": 1,
	'Energy Diffusing Immune': 1,
    "TachyonBeam": { "Immune": 1 },
	'Automated Destroyed System Repair': {"Time": 18.0, "DoNotInterfere": 0},
	'Defensive AOE Siphoon' : { "Resistance": 5.0},
	"SG Plasma Weapon Immune": 1,
	"SGReplicator Attack Resistance": 1,
	"SG Ori Beams Weapon Immune": 1,
	"SG Ion Weapon Immune": 1,
	"SG Asgard Beams Weapon Immune": 1,
	"GraviticLance": { "Immune": 1},
	"Tachyon Sensors":  1.0,
	"Inversion Beam": [1.0, 0.0, 0.0, 0.0],
	"Power Drain Beam": [1.0, 0.0, 0.0, 0.0],
    "SOTI Size Change": {"Scale": 1.0, "Power": 1, "Types": [App.CT_WEAPON_SYSTEM]}
	
}

if menuGroup:           Foundation.ShipDef.TradophianPC.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.TradophianPC.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

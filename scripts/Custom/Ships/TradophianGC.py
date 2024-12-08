#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback

abbrev = "TradophianGC"
iconName = "TradophianGC"
longName = "Tradophian Galaxy Cruiser"
shipFile = "TradophianGC"
species = App.SPECIES_GALAXY
menuGroup = "Sic Mvndvs Circulum"
playerMenuGroup = "Sic Mvndvs Circulum"


try:
	import Custom.Autoload.RaceTradophian
	Foundation.ShipDef.TradophianGC = Foundation.TradophianShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.TradophianGC = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.TradophianGC.desc = "Galaxy Cruiser:\nThe Tradophian Galaxy Cruiser is the oldest ship still in service in the Tradophian fleet. The ship design is several million years old in the present of the Tradophian linear calendar. The Galaxy Cruiser has been refit many times over those millions of years to better improve upon the Tradophians dimensional technology. The ship itself is Transcendental into the 5th and 6th dimensions due to the Calbrakium hull and armor (Which is 5x as dense as the heart of a neutron star), as well as dimensional and temporal dampeners. The role of this ship is Exploration. This ship is usually used to patrol galaxies at a time, but it can also fulfil universal duties as well by use of an Infinite Velocity Drive, This ship can also travel between universes via a Temporal De-Integration Matrix. This places the ships into a universal phased state by polarizing the hull with void type energy, which, unlike the Traedon Universal Tear Device, allows the Tradophian ships to phase through the higher dimensional barrier between realities like a wet object through a bubble, rather than the traedons pencil stabbed through paper. \n\nShields:\nThis ship is equipped with a Hypermatter shield, which is rather weak, but utilizes a certain phase of Hyper-Charged fluidic matter that absorbs almost all types of energy. While the shields are relatively weak physically speaking, the drop in stabilization of of a shield face when energy is applied to it allows the shields to be almost invulnerable to anything. With each hit, the shields absorb about 90-95 percent of all incoming energy that could cause harm to it.\n\nHypermatter Shield Faces:\nFront: 2,000,000 with 50 Charge\nRear: 2,000,000 with 50 Charge\nPort: 2,000,000 with 50 Charge\nStar: 2,000,000 with 50 Charge\nDorsal: 2,000,000 with 50 Charge\nVentral: 2,000,000 with 50 Charge\n\nArmor:\nThe Galaxy Cruiser is equipped with a special kind of transcendental material known as Calbrakium. This material is 5 times as dense as the heart of a Neutron Star. This extreme density and weight give the ship 4th and 5th dimensional protective properties. The Galaxy Cruiser itself has 25 percent Calbrakium armor plating and the hull is 15 percent.\n\nCalbrakium Armor: 1,000,000\nCalbrakium Hull: 750,000\n\nBeam Weapons:\nThe Galaxy Cruiser is equipped with Mk.DCCLVI (LT) Riftic Type Beams. These beams manipulate sub space-time and use distortions in 3rd and 4th dimension to tear objects apart.\n\nBeam Weapon Damage: 150,000\nBeam Weapons: Fore, Aft, Port, Star, Dorsal, Ventral\n\nSubspace Pulses:\nThe Galaxy Cruiser also comes equipped with micro-subspace singularity pulse generators, which act similarly to the beam weapons, but on a much lighter scale.\n\nTotal Subspace Pulse Ports: 15 (11 light, 4 heavy)\nLight Subspace Damage: 7,500\nHeavy Subspace Damage: 15,000\n\nTorpedo Generator:\nThe Torpedo Generator system aboard the Tradophian ships use compressed phasing matter to generate phasing devices that output a certain yield or energy type depending on the situation.\nTorpedo tube number: 2\n\nHypernova Plasma Torpedoes:\nThese torpedoes are a device capable of delivering a hit with about the force and power of a small stars supernova. They are very effective against technologically inferior ships. (Comp:1,000)\n(Damage:45,000)\n\nEnergy Diffusing Torpedoes:\nThese torpedoes are composed of an energy diffusing energy cloud put in a field. This cloud destabilizes energy shielding. The weaker the shield, the more it will drain. Under that field lies a very strong hull cutter. Weaker than the Hypernova Plasma torpedoes, but still enough to deal with weaker targets, able to slice through almost any metal. (Comp:250)\n(Damage:25,000 + shield drain)\n\nFalse Vacuum Decay Devices:\nThe Vacuum decay devices are weapons of unimaginable power. Hence why there are only two of them. In full power, the single particle inside of them could annihilate an entire universe in 15 minutes. However, on lower setting, it generates a field of void element around the device and reduces the target and anything inside intoQuarks. (Comp:2)\n(Damage:????)\n\nTimestream Cloak:\nThe Timestream Cloak on this ship isolates the ship, all of its systems and all of the crew inside from the current timeline via a Temporal Refraction Matrix hooked into a Temporal Refraction array. Once it is deactivated, the ship and everything in it are reintegrated into the timestream they are in.\n\nBoson Core:\nThe Boson Core equipped on this ship uses the well known 'Higgs Boson' particle. This particle, known for converting energy to matter and back again, is the heart of the Tradophian ships. They put a cloud of 99.9997253% pure bosons into the reactor core by first flying to the edge of the universe they are currently in. The edge of the universe is a mass of boson particles still creating and expanding the universe. They then activate a special kind of beam that they nickname the 'Boson Scoop' which locks the boson particles in a higher dimensional cage. and places them in a secondary device called the 'Foreign Neutralizing Core' This device utilizes carefully calculated and charged sub-spatial energy to clump foreign particles while keeping the boson particles intact. The particles are then fed through a higher dimensional mesh like substance, beaming all foreign particles back into space while letting the boson particles pass through. It is never 100% pure, as some particles smaller than quarks cling to the bosons. The bosons are then put in a deadlock chamber and slowly introduced into the main core. The core must be shut off during this introduction process, which usually takes a few hours, with the ships main systems running off of reserve power. The introduction process has many deadlock barriers set in place, so sabotage or critical failures are virtually impossible and reactions would instantly be neutralized and the core shut down. The core is repowered once everything is re-secured and in place and the core begins its processes. The Bosons are then exposed to extremely high pressure fluidic-dimensional energy. This energy is matter that was temporally altered to move hundreds of times the speed of light, blurring the line between matter and energy, in effect creating a supercritical state between the two. The boson particle, when exposed to this supercritical fluid, becomes supercharged as the energy on top of it is neither matter nor energy. It cannot convert either to either, so a reaction starts where the boson particle attempts to convert the fluid to both states at the same time. This causes energy to stack and overcharge the bosons. The bosons, reaching their limit, shoot off hypercharged bosonic micro radiation, which is shot through the inner solid layer of the core and into the secondary solid outer layer, which absorbs the radiation and charges up. Once the outer core reaches a critical state, it will start distributing the energy given off by the core to the main power grid. The outer core is quite a spectacle when you observe it. It will strobe through random colors on the spectrum at random intervals. A single charge of bosons can last upwards of 15000 years at a time as the drop in energy of the bosons is quite small and takes a long time until the bosons burn themselves out in this kind of environment."
Foundation.ShipDef.TradophianGC.fMaxWarp = 13.0
Foundation.ShipDef.TradophianGC.fCruiseWarp = 12.0
Foundation.ShipDef.TradophianGC.bPlanetKiller = 1
Foundation.ShipDef.TradophianGC.OverrideWarpFXColor = Foundation.ShipDef.TradophianGC.OverrideWarpFXColor
Foundation.ShipDef.TradophianGC.OverridePlasmaFXColor = Foundation.ShipDef.TradophianGC.OverridePlasmaFXColor
Foundation.ShipDef.TradophianGC.SubMenu = "Tradophian Ships"
Foundation.ShipDef.TradophianGC.CloakingSFX   = "TemporalDeintegration"
Foundation.ShipDef.TradophianGC.DeCloakingSFX = "TemporalReintegration"
Foundation.ShipDef.TradophianGC.dTechs = {
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
	'Automated Destroyed System Repair': {"Time": 19.0, "DoNotInterfere": 0},
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

if menuGroup:           Foundation.ShipDef.TradophianGC.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.TradophianGC.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

#####  Created by:StarFleet R&D 2010.02.13
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback

abbrev = "TradophianSC"
iconName = "TradophianSC"
longName = "Tradophian Stealth Cruiser"
shipFile = "TradophianSC"
species = App.SPECIES_GALAXY
menuGroup = "Sic Mvndvs Circulum"
playerMenuGroup = "Sic Mvndvs Circulum"


try:
	import Custom.Autoload.RaceTradophian
	Foundation.ShipDef.TradophianSC = Foundation.TradophianShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.TradophianSC = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.TradophianSC.desc = "Stealth Cruiser:\nThe stealth Cruiser was a ship that was engineered to excel where the Galaxy cruiser failed in terms of stealthy missions. The Stealth Cruiser is a newer ship and is still undergoing trial runs. The ship is relatively new, only being around 120,000 years old. She has been tested for so long due to the kind of technology equipped on her. Almost everything is improved on this ship, from the drive systems, to the transcendental emitters. The Stealth Cruiser has reduced shields (which regenerate faster), as well as a refractive matrix. Both help reduce hypermatter detectable emissions and Bosonic Drive residue. When the Refraction Matrix is activated, it is virtually undetectable. Not only is the ship near undetectable, but the improved drive system, it is extremely fast and maneuverable, making it able to avoid enemy fire and torpedoes. This ship has a similar, but slightly more advanced Infinite Velocity Drive and a similar Reality Phasing Device, giving it the same cross-dimensional and universal properties as the Galaxy Cruiser.\n\nShields:\nThis ship is equipped with a Hypermatter shield, which is rather weak, but utilizes a certain phase of Hyper-Charged fluidic matter that absorbs almost all types of energy. While the shields are relatively weak physically speaking, the drop in stabilization of of a shield face when energy is applied to it allows the shields to be almost invulnerable to anything. With each hit, the shields absorb about 90-95 percent of all incoming energy that could cause harm to it.\n\nHypermatter Shield Faces:\nFront: 1,000,000 with 1000 Charge\nRear: 1,000,000 with 1000 Charge\nPort: 1,000,000 with 1000 Charge\nStar: 1,000,000 with 1000  Charge\nDorsal: 1,000,000 with 1000 Charge\nVentral: 1,000,000 with 1000 Charge\n\nArmor:\nThe Stealth Cruiser is equipped with a special kind of transcendental material known as Calbrakium. This material is 5 times as dense as the heart of a Neutron Star. This extreme density and weight give the ship 4th and 5th dimensional protective properties. The Stealth Cruiser itself has 35 percent Calbrakium armor plating and the hull is 20 percent.\n\nCalbrakium Armor: 1,750,000\nCalbrakium Hull: 1,250,000\n\nBeam Weapons:\nThe Stealth Cruiser is equipped with Mk.MLXXVI (LT) Riftic Type Beams. These beams manipulate sub space-time and use distortions in 3rd and 4th dimension to tear objects apart. These arrays are more powerful than the ones on the Galaxy Cruiser.\n\nBeam Weapon Damage: 275,000\nBeam Weapons: Fore, Aft, Port, Star, Dorsal, Ventral\n\nSubspace Pulses:\nThe Stealth Cruiser also comes equipped with micro-subspace singularity pulse generators, which act similarly to the beam weapons, but on a much lighter scale.\n\nTotal Subspace Pulse Ports: 15\nLight Subspace Damage: 7,500\nHeavy Subspace Damage: 15,000\n\nTorpedo Generator:\nThe Torpedo Generator system aboard the Tradophian ships use compressed phasing matter to generate phasing devices that output a certain yield or energy type depending on the situation.\n\nTorpedo tube number: 2\n\nHypernova Plasma Torpedoes:\nThese torpedoes are a device capable of delivering a hitwith about the force and power of a small stars supernova. They are very effective against technologically inferior ships. (Comp:1,000)\n(Damage:45,000)\n\nSupercritical Matter Torpedo:\nThese torpedoes are a perfect line between energy and matter. Being in this state also causes the torpedo to be extremely volatile and fragile. They can produce quite a nasty explosion when they make contact with a target and overload. The supercritical fluid can weaken armor by either absorbing some of it, or liquifying it due to the energy part of it. They were first tested on the Stealth Cruisers when they were prototyped and may eventually replace the Hypernova Plasma Torpedoes entirely. (Comp:350)\n(Damage:60,000)\n\nFalse Vacuum Decay Devices: The Vacuum decay devices are weapons of unimaginable power. Hence why there are only two of them. In full power, the single particle inside of them could annihilate an entire universe in 15 minutes. However, on lower setting, it generates a field of void element around the device and reduces the target and anything inside intoQuarks. (Comp:2)\n(Damage:????)\n\nTimestream Cloak:\nThe Timestream Cloak on this ship isolates the ship, all of its systems and all of the crew inside from the current timeline via a Temporal Refraction Matrix hooked into a Temporal Refraction array. Once it is deactivated, the ship and everything in it are reintegrated into the timestream they are in.\n\nBoson Core:\nThe Boson Core equipped on this ship uses the well known 'Higgs Boson' particle. This particle, known for converting energy to matter and back again, is the heart of the Tradophian ships. They put a cloud of 99.9997253% pure bosons into the reactor core by first flying to the edge of the universe they are currently in. The edge of the universe is a mass of boson particles still creating and expanding the universe. They then activate a special kind of beam that they nickname the 'Boson Scoop' which locks the boson particles in a higher dimensional cage. and places them in a secondary device called the 'Foreign Neutralizing Core' This device utilizes carefully calculated and charged sub-spatial energy to clump foreign particles while keeping the boson particles intact. The particles are then fed through a higher dimensional mesh like substance, beaming all foreign particles back into space while letting the boson particles pass through. It is never 100% pure, as some particles smaller than quarks cling to the bosons. The bosons are then put in a deadlock chamber and slowly introduced into the main core. The core must be shut off during this introduction process, which usually takes a few hours, with the ships main systems running off of reserve power. The introduction process has many deadlock barriers set in place, so sabotage or critical failures are virtually impossible and reactions would instantly be neutralized and the core shut down. The core is repowered once everything is re-secured and in place and the core begins its processes. The Bosons are then exposed to extremely high pressure fluidic-dimensional energy. This energy is matter that was temporally altered to move hundreds of times the speed of light, blurring the line between matter and energy, in effect creating a supercritical state between the two. The boson particle, when exposed to this supercritical fluid, becomes supercharged as the energy on top of it is neither matter nor energy. It cannot convert either to either, so a reaction starts where the boson particle attempts to convert the fluid to both states at the same time. This causes energy to stack and overcharge the bosons. The bosons, reaching their limit, shoot off hypercharged bosonic micro radiation, which is shot through the inner solid layer of the core and into the secondary solid outer layer, which absorbs the radiation and charges up. Once the outer core reaches a critical state, it will start distributing the energy given off by the core to the main power grid. The outer core is quite a spectacle when you observe it. It will strobe through random colors on the spectrum at random intervals. A single charge of bosons can last upwards of 15000 years at a time as the drop in energy of the bosons is quite small and takes a long time until the bosons burn themselves out in this kind of environment."
Foundation.ShipDef.TradophianSC.fMaxWarp = 13.0
Foundation.ShipDef.TradophianSC.fCruiseWarp = 12.0
Foundation.ShipDef.TradophianSC.bPlanetKiller = 1
Foundation.ShipDef.TradophianSC.OverrideWarpFXColor = Foundation.ShipDef.TradophianSC.OverrideWarpFXColor
Foundation.ShipDef.TradophianSC.OverridePlasmaFXColor = Foundation.ShipDef.TradophianSC.OverridePlasmaFXColor
Foundation.ShipDef.TradophianSC.SubMenu = "Tradophian Ships"
Foundation.ShipDef.TradophianSC.CloakingSFX   = "TemporalDeintegration"
Foundation.ShipDef.TradophianSC.DeCloakingSFX = "TemporalReintegration"
Foundation.ShipDef.TradophianSC.dTechs = {
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


if menuGroup:           Foundation.ShipDef.TradophianSC.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.TradophianSC.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

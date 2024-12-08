#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback

abbrev = "TradophianBC"
iconName = "TradophianBC"
longName = "Tradophian BattleCruiser"
shipFile = "TradophianBC"
species = App.SPECIES_GALAXY
menuGroup = "Sic Mvndvs Circulum"
playerMenuGroup = "Sic Mvndvs Circulum"


try:
	import Custom.Autoload.RaceTradophian
	Foundation.ShipDef.TradophianBC = Foundation.TradophianShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.TradophianBC = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.TradophianBC.desc = "Battlecruiser:\nThe Battlecruiser was a ship to be used as a deterrent rather than an actual weapon to be used. It was a ship so powerful that even the Galaxy Cruiser or even the newer Stealth Cruiser could keep up with it in terms of power. This ship class is around half a million years old and still holds up to its name. These ships were only ever used to scare off species without combat up until the Xerohymid/Tradophian Omnidimensional War. Most species would get a scan of the weapons and defenses of the thing, if they could even penetrate the shields with scans, and retreat. The Battlecruiser was the first Tradophian ship to be built specifically for war. It was also the first ship to not only have a 100 percent pure Calbrakium and Hull, but the Battlecruiser also had layered Calbrakium armor and a layered hull. It had an advanced Hypermatter shield and a Heavy Riftic Beam array. It also is equipped with Micro Pulsar Devices which were one of the most powerful weapons created by the Tradophians. The first time a Tradophian Battlecruiser was damaged was during the Tradophian/Xerohymid War. The first recorded loss of a Battlecruiser was not much later. It was the first time that the Battlecruisers were in serious combat. They remain mostly unused to this day, keeping that same original purpose as before, however if needed and due to the war, there are quite a few more than before the war. This shows that while the Tradophians are not a warlike species, they do have the means to fight back.\n\nShields:\nThis ship is equipped with a Hypermatter shield, which is rather weak, but utilizes a certain phase of Hyper-Charged fluidic matter that absorbs almost all types of energy. While the shields are relatively weak physically speaking, the drop in stabilization of a shield face when energy is applied to it allows the shields to be almost invulnerable to anything. With each hit, the shields absorb about 90-95 percent of all incoming energy that could cause harm to it.\n\nHypermatter Shield Faces:\nFront: 7,500,000 with 150 Charge\nRear: 7,500,000 with 150 Charge\nPort: 7,500,000 with 150 Charge\nStar: 7,500,000 with 150 Charge\nDorsal: 7,500,000 with 150 Charge\nVentral: 7,500,000 with 150 Charge\n\nArmor:\nThe Battlecruiser is equipped with a special kind of transcendental material known as Calbrakium. This material is 5 times as dense as the heart of a Neutron Star. This extreme density and weight give the ship 4th and 5th dimensional protective properties. The BattleCruiser itself has layered 100  percent Calbrakium armor plating and the hull is also 100 percent layered Calbrakium.\n\nCalbrakium Armor: 25,000,000\nCalbrakium Hull: 10,000,000\n\nBeam Weapons:\nThe Battlecruiser is equipped with Mk.CMXLIII (HV) Riftic Type Beams. These beams manipulate sub space-time and use distortions in 3rd and 4th dimension to tear objects apart. These arrays are more powerful than the ones on the Galaxy Cruiser.\n\nBeam Weapon Damage: 500,000\nBeam Weapons: Fore, Aft, Port, Star, Dorsal, Ventral\n\nSubspace Pulses:\nThe Battlecruiser also comes equipped with micro-subspace singularity pulse generators, which act similarly to the beam weapons, but on a much lighter scale.\n\nTotal Subspace Pulse Ports: 32\nLight Subspace Damage: 7,500\nHeavy Subspace Damage: 15,000\n\nTorpedo Generator:\nThe Torpedo Generator system aboard the Tradophian ships use compressed phasing matter to generate phasing devices that output a certain yield or energy type depending on the situation.\n\nTorpedo tube number: 2\n\nHypernova Plasma Torpedoes:\nThese torpedoes are a device capable of delivering a hit with about the force and power of a small star's supernova. They are very effective against technologically inferior ships. (Comp:1,500) \n(Damage:45,000)\n\nEnergy Diffusing Torpedoes:\nThese torpedoes are composed of an energy diffusing energy cloud put in a field. This cloud destabilizes energy shielding.The weaker the shield, the more it will drain. Under that field lies a very strong hull cutter. Weaker than the Hypernova Plasma torpedoes, but still enough to deal with weaker targets, able to slice through almost any metal.(Comp:500)\n(Damage:25,000 + shield drain)\n\nMicropulsar Device:\nOne of the Tradophian's more deadly weapons, the Micropulsar Device utilizes a small pulsar protostar at its core to siphon off the decaying energy produced by it, These torpedoes rip through almost anything in a single hit just from that energy melting through armor like it wasn't even there, and disabling systems it contacts (Comp:750)\n(Damage:100,000)\n\nFalse Vacuum Decay Devices:\nThe Vacuum decay devices are weapons of unimaginable power. Hence why there are only two of them. In full power, the single particle inside of them could annihilate an entire universe in 15 minutes. However, on lower setting, it generates a field of void element aroundthe device and reduces the target and anything inside into Quarks.(Comp:5)\n(Damage:????)\n\nTimestream Cloak:\nThe Timestream Cloak on this ship isolates the ship, all of its systems and all of the crew inside from the current timeline via a Temporal Refraction Matrix hooked into a Temporal Refraction array. Once it is deactivated, the ship and everything in it are reintegrated into the timestream they are in.\n\nBoson Core:\nThe Boson Core equipped on this ship uses the well known 'Higgs Boson' particle. This particle, known for converting energy to matter and back again, is the heart of the Tradophian ships. They put a cloud of 99.9997253% pure bosons into the reactor core by first flying to the edge of the universe they are currently in. The edge of the universe is a mass of boson particles still creating and expanding the universe. They then activate a special kind of beam that they nickname the 'Boson Scoop' which locks the boson particles in a higher dimensional cage. and places them in a secondary device called the 'Foreign Neutralizing Core' This device utilizes carefully calculated and charged sub-spatial energy to clump foreign particles while keeping the boson particles intact. The particles are then fed through a higher dimensional mesh like substance, beaming all foreign particles back into space while letting the boson particles pass through. It is never 100% pure, as some particles smaller than quarks cling to the bosons. The bosons are then put in a deadlock chamber and slowly introduced into the main core. The core must be shut off during this introduction process, which usually takes a few hours, with the ships main systems running off of reserve power. The introduction process has many deadlock barriers set in place, so sabotage or critical failures are virtually impossible and reactions would instantly be neutralized and the core shut down. The core is repowered once everything is re-secured and in place and the core begins its processes. The Bosons are then exposed to extremely high pressure fluidic-dimensional energy. This energy is matter that was temporally altered to move hundreds of times the speed of light, blurring the line between matter and energy, in effect creating a supercritical state between the two. The boson particle, when exposed to this supercritical fluid, becomes supercharged as the energy on top of it is neither matter nor energy. It cannot convert either to either, so a reaction starts where the boson particle attempts to convert the fluid to both states at the same time. This causes energy to stack and overcharge the bosons. The bosons, reaching their limit, shoot off hypercharged bosonic micro radiation, which is shot through the inner solid layer of the core and into the secondary solid outer layer, which absorbs the radiation and charges up. Once the outer core reaches a critical state, it will start distributing the energy given off by the core to the main power grid. The outer core is quite a spectacle when you observe it. It will strobe through random colors on the spectrum at random intervals. A single charge of bosons can last upwards of 15000 years at a time as the drop in energy of the bosons is quite small and takes a long time until the bosons burn themselves out in this kind of environment."
Foundation.ShipDef.TradophianBC.fMaxWarp = 12.0
Foundation.ShipDef.TradophianBC.fCruiseWarp = 10.0
Foundation.ShipDef.TradophianBC.bPlanetKiller = 1
Foundation.ShipDef.TradophianBC.OverrideWarpFXColor = Foundation.ShipDef.TradophianBC.OverrideWarpFXColor
Foundation.ShipDef.TradophianBC.OverridePlasmaFXColor = Foundation.ShipDef.TradophianBC.OverridePlasmaFXColor
Foundation.ShipDef.TradophianBC.SubMenu = "Tradophian Ships"
Foundation.ShipDef.TradophianBC.CloakingSFX   = "TemporalDeintegration"
Foundation.ShipDef.TradophianBC.DeCloakingSFX = "TemporalReintegration"
Foundation.ShipDef.TradophianBC.dTechs = {
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

if menuGroup:           Foundation.ShipDef.TradophianBC.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.TradophianBC.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

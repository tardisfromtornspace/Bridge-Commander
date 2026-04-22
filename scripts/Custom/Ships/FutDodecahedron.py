import Foundation
import App
import traceback

abbrev = 'FutDodecahedron'
iconName = 'FutDodecahedron'
longName = 'Temporal Dodecahedron (29th C)'
shipFile = 'FutDodecahedron' 
menuGroup = 'Borg Ships'
playerMenuGroup = 'Borg Ships'
species = App.SPECIES_GALAXY

try:
	import Custom.Autoload.RaceFut29thCBorg
	Foundation.ShipDef.FutDodecahedron = Foundation.Fut29thCBorgShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.FutDodecahedron = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()


Foundation.ShipDef.FutDodecahedron.fMaxWarp = 9.995
Foundation.ShipDef.FutDodecahedron.fCruiseWarp = 8.4
Foundation.ShipDef.FutDodecahedron.SubMenu = "Future Borg"
Foundation.ShipDef.FutDodecahedron.SubSubMenu = "29th Century"
Foundation.ShipDef.FutDodecahedron.OverrideWarpFXColor = Foundation.ShipDef.FutDodecahedron.OverrideWarpFXColor
Foundation.ShipDef.FutDodecahedron.OverridePlasmaFXColor = Foundation.ShipDef.FutDodecahedron.OverridePlasmaFXColor
Foundation.ShipDef.FutDodecahedron.CloakingSFX   = "TemporalIsolationEngage"
Foundation.ShipDef.FutDodecahedron.DeCloakingSFX = "TemporalIsolationDisengage"
Foundation.ShipDef.FutDodecahedron.desc = "The year is 2597 and the Borg have begun their final invasion of every corner of the Milky Way. With their forces stretched thin between the Quadrants (via use of advanced Slipstream and Transwarp drives), the entire Milky Way decides to form a temporary alliance to hopefully finally destroy this threat that has been looming over the galaxy for hundreds of centuries. In 2614 after years of war and loss, the Milky Way Alliance finally drove the borg near the point of extinction. The Borg Queen at the time sent out one final message to the collective, 'Go into stasis and remain dormant unless you can gain an upper hand in some way'. This was broadcasted and Borg single pod ships were being launched through transwarp conduits all across the Milky Way. Most were hunted down when the Borg Queen was destroyed, and the Federation thought them to finally be extinct, but they were far from gone.\n\nIn the 29th Century, as the Temporal Cold War raged on, several Borg drones in hibernation were resurrected after falling into the derelict of a Federation Timeship. Sensing a potential upper hand in technology that they had not encountered before, a small group of dormant drones awoke from hibernation and began assimilating the new tech. It would not take them very long to get the ship up and running. This was a new race, a race with enhanced strategic capabilities. They no longer brute forced their way into a solution, they took their time to think and come up with the best strategy, and thus no Borg Queen was made in this future incarnation of the Borg. They soon began work on the development of long ranged materialatic energy assimilation weapons as part of their master plan, turning ships on their own crew and assimilating itself from the inside out. The Borg slowly began to inch their way back into the power of the universe and the Federation began to crumble under the force of the new Borg. The Borg soon decided that they may find even more technology in the future of the Federation and thus jumped into the 33rd century. When they arrived in the early 33rd century, they found that The Federation had actually regressed and banned temporal technology. This drove the borg to decide to wipe out the Federation entirely and claim the universe as their own, which in turn caused the Federation to call out to different timelines in a last ditch effort to survive. Few answered the call, but one in particular was more than willing to help. It was a mysterious dark version of the Federation who could finally stand up to the new Borg, and with their help, they were able to drive the rest of the borg away, working with Starfleet to track down and destroy any temporal Borg vessels that may have attempted incursions into history.\n\nThe Temporal pentagons used by the New Borg Empire were last ditch effort escape ships. They are extremely quick to avoid incoming phaser fire and torpedoes and act more evasive than the standard Temporal Borg ships to fulfill its role as an escape vessel, and because of this role, you will rarely see this ship in combat. It is lightly armed with only a few light phasers and light transcendental torpedoes across the hull. Because of the small hull radius, it is not fitted with any tractor beams, slicing arrays or heavy torpedo launchers as the radius is not large enough to implement that kind of technology despite being transcendental in nature. Despite the small size of this ship and the weak, regenerative nature of its shields, it has quite a strong armor compared to the other Borg ships of this time period. The armor was made out of quantum crystal nuclear phase matter and its standard hull out of neutronium. This along with the deep embedding of the systems into the hull makes this ship extremely hard to penetrate as it retreats and because of its light weapons, enemy ships would have it on low priority and that would give it ample time to escape. It was also the only known borg ship with a cloak, which allowed it to make an escape or act as a stealth scout ship."
Foundation.ShipDef.FutDodecahedron.dTechs = {
	'Adv Armor Tech EX': {"Energy Subsystems": ["Quantum Crystalline Enhanced Neutronium Superstructure"], "Armor Subsystems": ["Auto Temporal Regeneration Node"], "ArmorVincible": 0.01},
	'Borg Adaptation': 1,
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
	'Transphasic Torpedo Immune': 1,
	'ChronitonTorpe Immune': 1,
	'Phased Torpedo Immune': 1,
    "AutoTargeting": {"Phaser": [3, 1], "Torpedo": [2, 1], "Pulse": [2, 1] },
	'Automated Destroyed System Repair': {"Time": 50.0, "DoNotInterfere": 0},
	'TimeVortex Torpedo Immune': 1,
	"Digitizer Torpedo Immune": 1,
	'Defensive AOE Siphoon' : { "Resistance": 5.0},
	"SG Plasma Weapon Immune": 1,
	"SGReplicator Attack Resistance": 50,
	"SG Ori Beams Weapon Immune": 1,
	"SG Ion Weapon Immune": 1,
	"SG Asgard Beams Weapon Immune": 1,
	"GraviticLance": { "Immune": 1},
	"Tachyon Sensors":  1.0,
	"Inversion Beam": [1.0, 0.0, 0.0, 0.0],
	"Power Drain Beam": [1.0, 0.0, 0.0, 0.0],
	'Reflux Weapon Immune': 1,
	'Multivectral Shields' : 15}

if menuGroup:           Foundation.ShipDef.FutDodecahedron.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.FutDodecahedron.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


import Foundation
import App
import traceback

abbrev = 'FutCube'
iconName = 'FutCube'
longName = 'Temporal Cube (29th C)'
shipFile = 'FutCube' 
menuGroup = 'Borg Ships'
playerMenuGroup = 'Borg Ships'
species = App.SPECIES_GALAXY

try:
	import Custom.Autoload.RaceFut29thCBorg
	Foundation.ShipDef.FutCube = Foundation.Fut29thCBorgShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.FutCube = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()


Foundation.ShipDef.FutCube.fMaxWarp = 9.995
Foundation.ShipDef.FutCube.fCruiseWarp = 8.4
Foundation.ShipDef.FutCube.SubMenu = "Future Borg"
Foundation.ShipDef.FutCube.SubSubMenu = "29th Century"
Foundation.ShipDef.FutCube.OverrideWarpFXColor = Foundation.ShipDef.FutCube.OverrideWarpFXColor
Foundation.ShipDef.FutCube.OverridePlasmaFXColor = Foundation.ShipDef.FutCube.OverridePlasmaFXColor
Foundation.ShipDef.FutCube.desc = "The year is 2597 and the Borg have begun their final invasion of every corner of the Milky Way. With their forces stretched thin between the Quadrants (via use of advanced Slipstream and Transwarp drives), the entire Milky Way decides to form a temporary alliance to hopefully finally destroy this threat that has been looming over the galaxy for hundreds of centuries. In 2614 after years of war and loss, the Milky Way Alliance finally drove the borg near the point of extinction. The Borg Queen at the time sent out one final message to the collective, 'Go into stasis and remain dormant unless you can gain an upper hand in some way'. This was broadcasted and Borg single pod ships were being launched through transwarp conduits all across the Milky Way. Most were hunted down when the Borg Queen was destroyed, and the Federation thought them to finally be extinct, but they were far from gone.\n\nIn the 29th Century, as the Temporal Cold War raged on, several Borg drones in hibernation were resurrected after falling into the derelict of a Federation Timeship. Sensing a potential upper hand in technology that they had not encountered before, a small group of dormant drones awoke from hibernation and began assimilating the new tech. It would not take them very long to get the ship up and running. This was a new race, a race with enhanced strategic capabilities. They no longer brute forced their way into a solution, they took their time to think and come up with the best strategy, and thus no Borg Queen was made in this future incarnation of the Borg. They soon began work on the development of long ranged materialatic energy assimilation weapons as part of their master plan, turning ships on their own crew and assimilating itself from the inside out. The Borg slowly began to inch their way back into the power of the universe and the Federation began to crumble under the force of the new Borg. The Borg soon decided that they may find even more technology in the future of the Federation and thus jumped into the 33rd century. When they arrived in the early 33rd century, they found that The Federation had actually regressed and banned temporal technology. This drove the borg to decide to wipe out the Federation entirely and claim the universe as their own, which in turn caused the Federation to call out to different timelines in a last ditch effort to survive. Few answered the call, but one in particular were more than willing to help. It was a mysterious dark version of the Federation who could finally stand up to the new Borg, and with their help, they were able to drive the rest of the borg away, working with Starfleet to track down and destroy any temporal Borg vessels that may have attempted incursions into history.\n\nThe cubes of the New Borg Empire were comprised of a kind of Temporally charged Polydeutonic alloys making up the inner framework of the cube covered in multiple layers of near solid neutronium. It had 33 heavy Intra Gravitonic phaser arrays across its hull as well as an additional 8 Subspace Rupturing slicing beams focused with two on the top, two on the fore, two on the aft, and two on the starboard face of the cube. These Slicing Beams were quite devastating and could tear Federation Timeships apart with a single shot. Cubes of the New Borg Empire were also equipt with a Hyper Gravitonic Beam generator at the bottom of the cube which was more than capable of destroying an entire planet if the Borg were so inclined to do so. These cubes were also fitted with 16 light torpedo tubes on the hull and 5 heavy torpedo tubes one on each face except the face with the Hyper Graviton emitter, each one assigned a different yield of Transcendental Gravimetric Shockwave Torpedoes capable of tearing through transcendental protection."
Foundation.ShipDef.FutCube.dTechs = {
	'Adv Armor Tech EX': {"Energy Subsystems": ["Neutronium Superstructure"], "Armor Subsystems": ["Auto Temporal Regeneration Node"], "ArmorVincible": 0.01},
	'Borg Adaptation': 1,
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
	'Transphasic Torpedo Immune': 1,
    "AutoTargeting": {"Phaser": [3, 1], "Torpedo": [2, 1], "Pulse": [2, 1] },
	'ChronitonTorpe Immune': 1,
	'Phased Torpedo Immune': 1,
	'Reflux Weapon Immune': 1,
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
	'Multivectral Shields' : 15}

if menuGroup:           Foundation.ShipDef.FutCube.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.FutCube.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


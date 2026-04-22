import Foundation
import App
import traceback

abbrev = 'FutSphere'
iconName = 'FutSphere'
longName = 'Temporal Sphere (29th C)'
shipFile = 'FutSphere' 
menuGroup = 'Borg Ships'
playerMenuGroup = 'Borg Ships'
species = App.SPECIES_GALAXY

try:
	import Custom.Autoload.RaceFut29thCBorg
	Foundation.ShipDef.FutSphere = Foundation.Fut29thCBorgShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.FutSphere = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()


Foundation.ShipDef.FutSphere.fMaxWarp = 9.995
Foundation.ShipDef.FutSphere.fCruiseWarp = 8.4
Foundation.ShipDef.FutSphere.SubMenu = "Future Borg"
Foundation.ShipDef.FutSphere.SubSubMenu = "29th Century"
Foundation.ShipDef.FutSphere.OverrideWarpFXColor = Foundation.ShipDef.FutSphere.OverrideWarpFXColor
Foundation.ShipDef.FutSphere.OverridePlasmaFXColor = Foundation.ShipDef.FutSphere.OverridePlasmaFXColor
Foundation.ShipDef.FutSphere.desc = "The year is 2597 and the Borg have begun their final invasion of every corner of the Milky Way. With their forces stretched thin between the Quadrants (via use of advanced Slipstream and Transwarp drives), the entire Milky Way decides to form a temporary alliance to hopefully finally destroy this threat that has been looming over the galaxy for hundreds of centuries. In 2614 after years of war and loss, the Milky Way Alliance finally drove the borg near the point of extinction. The Borg Queen at the time sent out one final message to the collective, 'Go into stasis and remain dormant unless you can gain an upper hand in some way'. This was broadcasted and Borg single pod ships were being launched through transwarp conduits all across the Milky Way. Most were hunted down when the Borg Queen was destroyed, and the Federation thought them to finally be extinct, but they were far from gone.\n\nIn the 29th Century, as the Temporal Cold War raged on, several Borg drones in hibernation were resurrected after falling into the derelict of a Federation Timeship. Sensing a potential upper hand in technology that they had not encountered before, a small group of dormant drones awoke from hibernation and began assimilating the new tech. It would not take them very long to get the ship up and running. This was a new race, a race with enhanced strategic capabilities. They no longer brute forced their way into a solution, they took their time to think and come up with the best strategy, and thus no Borg Queen was made in this future incarnation of the Borg. They soon began work on the development of long ranged materialatic energy assimilation weapons as part of their master plan, turning ships on their own crew and assimilating itself from the inside out. The Borg slowly began to inch their way back into the power of the universe and the Federation began to crumble under the force of the new Borg. The Borg soon decided that they may find even more technology in the future of the Federation and thus jumped into the 33rd century. When they arrived in the early 33rd century, they found that The Federation had actually regressed and banned temporal technology. This drove the borg to decide to wipe out the Federation entirely and claim the universe as their own, which in turn caused the Federation to call out to different timelines in a last ditch effort to survive. Few answered the call, but one in particular were more than willing to help. It was a mysterious dark version of the Federation who could finally stand up to the new Borg, and with their help, they were able to drive the rest of the borg away, working with Starfleet to track down and destroy any temporal Borg vessels that may have attempted incursions into history.\n\nThe spheres of the New Borg Empire were comprised of a kind of Temporally charged Polydeutonic alloys making up the inner framework of the sphere covered in multiple layers of near solid neutronium. The Spheres were used as either scouts, or last ditch effort escape ship. For being so small, the Temporal Spheres were still quite powerful. It has 10 light torpedo tubes and had 17 phaser arrays across its hull and one heavy torpedo tube on the front"
Foundation.ShipDef.FutSphere.dTechs = {
	'Adv Armor Tech EX': {"Energy Subsystems": ["Neutronium Superstructure"], "Armor Subsystems": ["Auto Temporal Regeneration Node"], "ArmorVincible": 0.01},
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

if menuGroup:           Foundation.ShipDef.FutSphere.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.FutSphere.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


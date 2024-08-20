== Changelog ==
0.1 - first unofficial release of this tweak, for feedback

== What does this mod do ==
This mod attempts to fix some Stargate pack balance inconsistencies by adding appropiate realistic technologies for all SG races:

* SG Shields: at the moment, this tech is used to know what ships use Stargate shielding/protection and which type (excluding the Atlantis and AncientCity, already covered in https://www.gamefront.com/games/bridge-commander/file/canonical-alteran-technologies)
** This tech also works as a marker to indicate what techs it can protect itself from better or worse, from common SG shield characteristics, to technological differences.
** Despite the name, it is also used to storage some hull types, for tracing. This is because not all hulls are made equal, and some materials on the hulls may make them more or less susceptible to certain types of damage than others.

* SG Ion Weapons: this tech works by adding a customizable drain effect; while being open to adding Subscripts that may modify its behavior (please read in-script documentation about how does this work).
** This was meant to give the Asgard and Tollan Ion Weapons a significant buff, while providing Anubis a resistance without making Anubis vessels have shields 100 times stronger than normal (let's not forget a regular Ha'tak could be destroyed by a single Tollan Ion Cannon shot ignoring the shields, but Anubis shields on a regular Ha'tak could shrug a entire planetary defense grid of them, yet at most 1 Anubian Ha'tak was equal to 6 regular ones - if mod-wise we followed a mere shield increase strategy, in order to make Anubis Ha'taks capable of shrugging off the Tollan Ion cannons, they would become invincible to even Ori vessels).

* SG Plasma Weapons: the purpose of this tech was to explain why a naquadah-enhanced >1000 Megaton nuke could not deal damage to a Go'auld Ha'tak and a Ha'tak could stay 10 hours inside a sun's Corona, yet some Go'auld Death Glider's staff weapons could put the shields to strain, without performing total absurdities (before this mod, previous mods made the Go'auld death glider half-shot deal roughtly half the damage of a Ha'tak's main weapons shot, you have got to be kidding me).

* Plasma and Ion weapons base damage nerfed accordingly to deal a similar final raw damage output to what they did to shields before the mod.
** Please note that "similar" is not "equal" - actually, specially for the Asgard Ion Cannons, net shield damage has been slightly buffed, specially for the higher-end vessels' Ion weapons.
** Same has been done for certain "big" weapons such as the Flagship's cannons.
* Asgard Daniel Jackson, O'Neill and Valhalla shields and shield recharge buffed significantly (between 36% to 57%).


* Replicator adaptation: #### TO-DO #### based on my other mod, Borg Adaptation https://www.gamefront.com/games/bridge-commander/file/borg-adaptation-mod-defensive ; it is meant to be added as a modification to allow the Replicators to adapt, instead of making them a set of OP-ness that cannot adapt, they instead start a bit less overpowered, then learn and eventually make themselves far more powerful than normal.
** TO-DO
* TO-DO ALSO ADD Automated Destroyed System Repair TO THE REPLICATOR VESSELS, ESPECIALLY THEIR COMMAND CARRIER AND SPIDER



* Ha'taks and some capital ships' masses adjusted to comparable levels (since the mass difference has something to do with in-game collisions, it is the best way to simulate shield collisions in-game)
* Upgraded Ha'tak speed increased slightly.
* Buffed regular Ha'tak (Early, Variant, Refit) shields significantly.
* Nerfed regular Ha'tak hulls (Early, Variant, Refit) a bit.

#### TO-DO ----> FOR ANUBIS MOTHERSHIP, SEE IF YOU CAN DO SOMETHING LIKE THE TURRETS SCRIPT MIXED WITH TACHYONBEAM SCRIPT, BUT ONLY MOVING TWO UNCOLLIDABLE AND UNTARGETABLE BEAMS NEXT TO AN ENEMY VESSEL, TO THEN FIRE ON THE TWO CLOSEST ENEMY VESSELS TO THE OBJECTIVE ####

* Wraith given Automated System Repair #### TO-DO ####
* Wraith HP and weapons adjusted accordingly between mods #### TO-DO ####
#### ALSO TO-DO MAYBE GIVE WRAITH HULL A CERTAIN METHOD OF DAMAGE REDUCTION? ####

== Dependancies ==
All of these must be installed before installing this mod, in this order:
* Foundation + Kobayashi Maru (KM has Foundation already installed - the most recent, the better, preferably 2011.10 or latter)
* Stargate pack 3.0 or 4.0 https://www.gamefront.com/games/bridge-commander/file/stargate-ship-pack-dave975-and-dkealt
** If you want to install the Stargate multiplayer patch (for 3.0, https://www.gamefront.com/games/bridge-commander/file/sg-pack-3-0-multiplayer-patch, install the KM version of it, not the other), do it immediately after installing this one
* Ancient City mod https://www.gamefront.com/games/bridge-commander/file/ancient-city-atlantis-pack-0-9
* Wraith Cruiser https://www.gamefront.com/games/bridge-commander/file/wraith-cruiser-1-1
* Wraith Hive https://www.gamefront.com/games/bridge-commander/file/wraith-hive-ship, then https://www.gamefront.com/games/bridge-commander/file/wraith-hive-ship-mvam-darts
* Wraith SuperHive https://www.gamefront.com/games/bridge-commander/file/super-hive
* SGU Destiny with Ancient Shuttle https://www.gamefront.com/games/bridge-commander/file/sgu-destiny-with-ancient-shuttle
* "FIX-DS9FXbelow1dot2.py" file is required for the weapons to work accordingly on KM. This file can be found in several of CharaToLoki's (my) mods, including this one.
* "Automated Destroyed System Repair" and "FIX-FoundationTech20050703ShipInstanceDetach.py" from the Babylon 5 Super-Pack mod https://www.gamefront.com/games/bridge-commander/file/stbc-babylon-5-mod
*** The latter is required because "FIX-FoundationTech20050703ShipInstanceDetach" is recommended for a better and cleaner game experience, but with complex mods with complex technologies it is a must. Additionally, this pack contains a few technologies that the pack does not directly use per-se, but some ships may.
*** "Automated Destroyed System Repair" can also be downloaded from the Borg Adaptation Mod https://www.gamefront.com/games/bridge-commander/file/borg-adaptation-mod-defensive (SMALLER FILES IN TOTAL, but requires to download )
** Or from 
* Canonical Alteran Technologies (C.A.T.) https://www.gamefront.com/games/bridge-commander/file/canonical-alteran-technologies (it also has the "FIX-DS9FXbelow1dot2" file)
** If you download the multiplayer patch, you will probably have to re-install this C.A.T. mod

OPTIONAL mods (they are not required AT ALL , but have some of the techs the pack may later reference on):
** Tachyon Beam mod https://www.gamefront.com/games/bridge-commander/file/tachyon-beam-customizable-tech

Also please note that if you download the multiplayer patch AFTER installing this mod, you will probably have to re-install the mod.

== Credits ==
* Everyone involved in Foundation - without you this would have been a real pain to do (please read the separate Foundation.txt license) - Banbury, Dasher42, DigitalFriend, MLeo, Nanobyte and Sleight42, among others
* Everyone involved in KM - specifically those involved in the creation of armour and Shields.py (FoundationTechnologies) and the AdvArmorTech.py - Apollo from ATP Technologies as well.
* Dasher42 and USS Sovereign, not only for the above but for some feedback.
* Those involved with the Stargate Pack 4.0 and other Stargate packs for STBC:
** https://www.gamefront.com/games/bridge-commander/file/stargate-ship-pack-dave975-and-dkealt, https://www.gamefront.com/games/bridge-commander/file/wraith-hive-ship and https://www.gamefront.com/games/bridge-commander/file/sg-pack-3-0-multiplayer-patch by Dave975 and DKealt, among others mentioned on their readmes, and LJ.
** https://www.gamefront.com/games/bridge-commander/file/ancient-city-atlantis-pack-0-9: abt, limey, cliperkins, jb and dave (models) and icons (http://www.lostmindsinc.com/index.php?page=races)
*** Evan Light aka sleight42 for the original Carriers script.
*** Erik Novales, MRJOHN and Lost_Jedi for the original Projectiles.
** SGU Destiny and Ancient Shuttle https://www.gamefront.com/games/bridge-commander/file/sgu-destiny-with-ancient-shuttle
** Superhive mod uploaded by xxDABTxx https://www.gamefront.com/games/bridge-commander/file/super-hive
* .truncatedcake0161 for feedback on the Discord about power tweaks.
* Grey da Derg#2305 for helping with noticing bugs and their cause and finding out possible ways to tweak the hardpoints and techs.
* Alex SL Gato (aka CharaToLoki) for any new code implemented or modified - specifically the heavy modifications to the Ion and Plasma projectiles, the buffs to the Asgard Hardpoints and modifications to the Ha'tak, X301, F302, Death Glider and Needle Threader hardpoints.

Fulfilling both the SDK and LGPL licenses:
THIS MOD IS NOT SUPPORTED BY ACTIVISION

This mod falls under the GNU LESSER GENERAL PUBLIC LICENSE Version 3, 29 June 2007, both from any derivative or original work done to the mod. Everyone is permitted to copy and distribute verbatim copies of this mod. As per the LPGL license, everything in this mod is open for everybody to use, read and modify. Just do not forget to credit everyone involved and follow the LGPL license so derivatives of this code remain LGPL.


== Bugs ==
* Due to circumstances that are not from this mod, some models always have a risk of suffering bleedthrough even with shields at max (particularly notable in the BC-304 and X303 series, but also sometimes noticeable in Go'auld Ha'tak's shuttle bays) - no game performance impact.
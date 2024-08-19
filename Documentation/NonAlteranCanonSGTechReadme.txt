== Changelog ==
0.1 - first unofficial release of this tweak, for feedback

== What does this mod do ==
This mod attempts to fix some Stargate pack balance inconsistencies by adding appropiate realistic technologies for all SG races:

* SG Shields: at the moment, this tech is used to know what ships use Stargate shielding/protection and which type (excluding the Atlantis and AncientCity, already covered in https://www.gamefront.com/games/bridge-commander/file/canonical-alteran-technologies)
** This tech also works as a marker to indicate what techs it can protect itself from better or worse, from common SG shield characteristics, to technological differences.
** Despite the name, it is also used to storage some hull types, for tracing. This is because not all hulls are made equal, and some materials on the hulls may make them more or less susceptible to certain types of damage than others.

* SG Ion Weapons: this tech works by adding a customizable drain effect; while being open to adding Subscripts that may modify its behavior (please read in-script documentation about how does this work).
** This was meant to give the Asgard and Tollan Ion Weapons a significant buff, while providing Anubis a resistance without making Anubis vessels have shields 100 times stronger than normal (let's not forget a regular Ha'tak could be destroyed by a single Tollan Ion Cannon shot ignoring the shields, but Anubis shields on a regular Ha'tak could shrug a entire planetary defense grid of them, yet at most 1 Anubian Ha'tak was equal to 6 regular ones - if mod-wise we followed a mere shield increase strategy, in order to make Anubis Ha'taks capable of shrugging off the Tollan Ion cannons, they would become invincible to even Ori vessels).

* SG Plasma Weapons: #### TO-DO #### the purpose of this tech was to explain why a naquadah-enhanced >1000 Megaton nuke could not deal damage to a Go'auld Ha'tak and a Ha'tak could stay 9 hours inside a sun's Corona, yet some Go'auld Death Glider's staff weapons could put the shields to strain, without performing total absurdities (before this mod, previous mods made the Go'auld death glider half-shot deal roughtly half the damage of a Ha'tak's main weapons shot, you have got to be kidding me).
** TO-DO

* Replicator adaptation: #### TO-DO #### based on my other mod, Borg Adaptation https://www.gamefront.com/games/bridge-commander/file/borg-adaptation-mod-defensive ; it is meant to be added as a modification to allow the Replicators to adapt, instead of making them a set of OP-ness that cannot adapt, they instead start a bit less overpowered, then learn and eventually make themselves far more powerful than normal.
** TO-DO
* TO-DO ALSO ADD Automated Destroyed System Repair TO THE REPLICATOR VESSELS, ESPECIALLY THEIR COMMAND CARRIER AND SPIDER

* Plasma and Ion weapons nerfed accordingly to deal a similar raw damage output to what they did to shields before the mod. #### TO-DO ####
** Please note that "similar" is not "equal" - actually, specially for the Asgard Ion Cannons, net shield damage has been slightly buffed, specially for the higher-end vessels' Ion weapons.
* Asgard Daniel Jackson, O'Neill and Valhalla shields and shield recharge buffed significantly (between 36% to 57%).

* Ha'taks adjusted #### TO-DO ####

#### TO-DO ----> FOR ANUBIS MOTHERSHIP, SEE IF YOU CAN DO SOMETHING LIKE THE TURRETS SCRIPT MIXED WITH TACHYONBEAM SCRIPT, BUT ONLY MOVING TWO UNCOLLIDABLE AND UNTARGETABLE BEAMS NEXT TO AN ENEMY VESSEL, TO THEN FIRE ON THE TWO CLOSEST ENEMY VESSELS TO THE OBJECTIVE ####

* Wraith given Automated System Repair #### TO-DO ####
* Wraith HP and weapons adjusted accordingly between mods #### TO-DO ####

== Dependancies ==
All of these must be installed before installing this mod, in this order:
* Foundation + Kobayashi Maru (KM has Foundation already installed - the most recent, the better, preferably 2011.10 or latter)
* Stargate pack 3.0 or 4.0 https://www.gamefront.com/games/bridge-commander/file/stargate-ship-pack-dave975-and-dkealt
** If you want to install the Stargate multiplayer patch (TO-DO ADD LINK), do it immediately after installing this one
* Ancient City mod https://www.gamefront.com/games/bridge-commander/file/ancient-city-atlantis-pack-0-9
* Wraith Cruiser (TO-DO ADD LINK)
* Wraith Hive (TO-DO ADD LINK)
* Wraith SuperHive (TO-DO ADD LINK)
* SGU Destiny with Ancient Shuttle https://www.gamefront.com/games/bridge-commander/file/sgu-destiny-with-ancient-shuttle
* Either Automated Destroyed System Repair from:
** Borg Adaptation Mod https://www.gamefront.com/games/bridge-commander/file/borg-adaptation-mod-defensive
** Or from https://www.gamefront.com/games/bridge-commander/file/stbc-babylon-5-mod
*** RECOMMENDED TO DOWNLOAD the scripts/Custom/Autoload file "FIX-FoundationTech20050703ShipInstanceDetach" from https://www.gamefront.com/games/bridge-commander/file/stbc-babylon-5-mod in order to get a better and cleaner game experience.
* Canonical Alteran Technologies (C.A.T.) https://www.gamefront.com/games/bridge-commander/file/canonical-alteran-technologies
** If you download the multiplayer patch, you will probably have to re-install this C.A.T. mod

Also please note that if you download the multiplayer patch AFTER installing this mod, you will probably have to re-install this mod.

== Credits ==
* Everyone involved in Foundation - without you this would have been a real pain to do (please read the separate Foundation.txt license) - Banbury, Dasher42, DigitalFriend, MLeo, Nanobyte and Sleight42, among others
* Everyone involved in KM - specifically those involved in the creation of armour and Shields.py (FoundationTechnologies) and the AdvArmorTech.py - Apollo from ATP Technologies as well.
* Dasher42 and USS Sovereign, not only for the above but for some feedback.
* Those involved with the Stargate Pack 4.0 and other Stargate packs for STBC:
** https://www.gamefront.com/games/bridge-commander/file/stargate-ship-pack-dave975-and-dkealt by Dave975 and DKealt, among others mentioned on its readme, and LJ.
** https://www.gamefront.com/games/bridge-commander/file/ancient-city-atlantis-pack-0-9: abt, limey, cliperkins, jb and dave (models) and icons (http://www.lostmindsinc.com/index.php?page=races)
*** Evan Light aka sleight42 for the original Carriers script.
*** Erik Novales, MRJOHN and Lost_Jedi for the original Projectiles.
** SGU Destiny and Ancient Shuttle https://www.gamefront.com/games/bridge-commander/file/sgu-destiny-with-ancient-shuttle
** #### TO-DO ADD WRAITH CRUISER, HIVE AND SUPERHIVE CREDITS ####
* .truncatedcake0161 for feedback on the Discord about power tweaks.
* Grey da Derg#2305 for helping with noticing bugs and their cause and finding out possible ways to tweak the hardpoints and techs.
* Alex SL Gato (aka CharaToLoki) for any new code implemented or modified - specifically the heavy modifications to the Ion and Plasma projectiles, the buffs to the Asgard Hardpoints and modifications to the Ha'tak hardpoints.
** NOTICE: There's an Altantis HP fix on gamefront that added a cloak, but by the time I noticed I already added the cloak myself to the file

Fulfilling both the SDK and LGPL licenses:
THIS MOD IS NOT SUPPORTED BY ACTIVISION

This mod falls under the GNU LESSER GENERAL PUBLIC LICENSE Version 3, 29 June 2007, both from any derivative or original work done to the mod. Everyone is permitted to copy and distribute verbatim copies of this mod. As per the LPGL license, everything in this mod is open for everybody to use, read and modify. Just do not forget to credit everyone involved and follow the LGPL license so derivatives of this code remain LGPL.


== Bugs ==
* Due to circumstances that are not from this mod, some models always have a risk of suffering bleedthrough even with shields at max (particularly notable in the BC-304 and X303 series, but also sometimes noticeable in Go'auld Ha'tak's shuttle bays) - no game performance impact.
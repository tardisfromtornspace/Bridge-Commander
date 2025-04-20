== Changelog ==
1.1.5 - 
* Updates:
  - Updated AncientCity and Atlantis' warp speeds to provide a more accurate hyperdrive for when the entire stargate overhaul pack is added.
1.1.4 - 
* Bug fixes-updates:
  - Updated AlteranShields to 1.01, fixing a bug with strength modifier not being considered for energy calculations.
1.1.3 - 
* Bug fixes:
  - Found out that Defiant's Power system could glitch out if a ship had impulse engines but no warp engines. The new Autoload patch "FIX-DefiantsQBautostartPower1dot0.py" aims to resolve that issue.
1.1.2 - 
* Bug fixes:
  - Fixed the issue also on Drones2.
1.1.1 - 
* Bug fixes:
  - Found a weird issue with the original damage dealer that could cause a crash sometimes on certain vessels. The only known cause for this (rarely hitting a dead ship that no longer existed on the game) should be fixed.
* New features:
  - Improved Drone tactical script funcionality so Drones and Drones2 can change subsystem to hit when the player or AI swap subsystems.
1.1 - 
* New features:
  - SGRealisticHoppingTorp to 1.2 - Now if you have enough energy and divert enough power to weapons, THE DRONES WILL SWITCH TARGETS UPON DESTRUCTION OF THEM, and when no enemies are found, they are recalled to the ship, replenishing ammo.
* Bug fixes:
  - the Standard Asgard Warship (the one that looks like the O'Neill) was not included on the legacy exceptions to drones - now that is fixed
1.0.1 - Added and adjusted Aurora Cannons to be yellow - thanks @Jovan Blackman for noticing. Also removed the excessive prints.
1.0.0 - Official release
0.9.8 - Adjsuted AncientCity so it fires the drones faster, thank you Grey da Deg, Grim455, MSR1701 and .truncatedcake0161
0.9.7 - Small shield fixes on hardpoint and tech.
0.9.6 - Per request of Dasher42, I've included the SDKLicense and the Foundation license
0.9.5 - several bugfixes - drainer weapons bugs and drone crashing the game if the ship launching the drones died are now fixed
0.9 - first unofficial release of this tweak, for feedback

== What does this mod do ==
This mod makes the Atlantis and AncientCity from the Stargate pack 3.0 far more canonical by tweaking their shields and weaponry:
* Shields now follow canon configuration (shields cannot normally drop unless the Main Battery/ZPM has been depleted).
* Drones tweak:
** Power reduction by a third.
** Increased range and lifetime.
** Now they have the chance to come back and forth between ships, doing multiple strikes at the same ship before dying.
*** From 1.1 onwards, this back and forth also allos the drones to "jump" to nearby enemy ships if the ship that is firing them has enough energy available and has directed enough power to the weapons. Additionally, drones will normally be recalled when no enemies are on sight, replenishing ammo.

== Dependancies ==
All of these must be installed before installing this mod, in this order:
* Foundation + Kobayashi Maru (has Foundation already installed - the most recent, the better)
* Stargate pack 3.0 or 4.0 https://www.gamefront.com/games/bridge-commander/file/stargate-ship-pack-dave975-and-dkealt

== Credits ==
* Everyone involved in Foundation - without you this would have been a real pain to do (please read the separate Foundation.txt license) - Banbury, Dasher42, DigitalFriend, MLeo, Nanobyte and Sleight42, among others
* Everyone involved in KM - specifically those involved in the creation of armour and Shields.py (FoundationTechnologies) and the AdvArmorTech.py - Apollo from ATP Technologies as well.
* Dasher42 and USS Sovereign, not only for the above but for some feedback.
* Those involved with the Stargate Pack 4.0 and other Stargate packs for STBC: #### TO-DO CHECK THE HYPERDRIVE MOD IS THERE, ELSE LOOK FOR IT ####
** https://www.gamefront.com/games/bridge-commander/file/stargate-ship-pack-dave975-and-dkealt by Dave975 and DKealt, among others mentioned on its readme, and LJ.
** https://www.gamefront.com/games/bridge-commander/file/ancient-city-atlantis-pack-0-9: abt, limey, cliperkins, jb and dave (models) and icons (http://www.lostmindsinc.com/index.php?page=races)
*** Evan Light aka sleight42 for the original Carriers script.
*** Erik Novales, MRJOHN and Lost_Jedi for the original Projectiles.
* .truncatedcake0161 for feedback on the Discord about power tweaks.
* Grey da Derg#2305 for helping with noticing bugs and their cause.
* Grim455#4905 aka THE SCI-FI KING, for beign inquisitive and finding out possible ways to tweak the hardpoints and techs.
* @Jovan Blackman for noticing that Aurura Cannons are effectively yellow.
* Alex SL Gato (aka CharaToLoki) for any new code implemented or modified - specifically the heavy modifications to the SG Drone script.
** NOTICE: There's an Altantis HP fix on gamefront that added a cloak, but by the time I noticed I already added the cloak myself to the file

Fulfilling both the SDK and LGPL licenses:
THIS MOD IS NOT SUPPORTED BY ACTIVISION

This mod falls under the GNU LESSER GENERAL PUBLIC LICENSE Version 3, 29 June 2007, both from any derivative or original work done to the mod. Everyone is permitted to copy and distribute verbatim copies of this mod. As per the LPGL license, everything in this mod is open for everybody to use, read and modify. Just do not forget to credit everyone involved and follow the LGPL license so derivatives of this code remain LGPL.


== Bugs ==
* As stated from the Ancient City pack, these models cannot handle damage textures so they are turned off for these models only - no performance limitations.
* Due to circumstances that are not from this mod:
** Big enough ships have strange collisions that may make drones far less effective - no game performance impact.
** On some installs firing too many drones at the same time may consume memory.
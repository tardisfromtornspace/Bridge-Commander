==Changelog==
1.2.11 -
   Fixes:
   * Updated Hull Polarizer to 1.31, fixing a small issue where a polarized plate could sometimes take twice the damage.
1.2.10 -
   Fixes:
   * Updated Hull Polarizer to 1.3, fixing a small inefficiency.
1.2.9 -
   Fixes:
   * Updated Thirdspace Capital Ship to have multi-targeting and a faster-recharge Lightbringer.
   * Updated B5ThirdspaceTeleAttack projectiles to indicate name and make the multi-attack more effective.
1.2.8 -
   Bug Fixes:
   * Updated Automated Destroyed System Repair from 0.54 to 0.55, fixing a typo with DoNotInterfere configuration.
1.2.7 -
   Bug Fixes:
   * Updated Automated Destroyed System Repair from 0.53 to 0.54, fixing an issue with a missing subsystem on outlier cases.
1.2.6 -
   Bug Fixes:
   * Updated Automated Destroyed System Repair from 0.52 to 0.53, fixing an issue with a missing timer checkup on very outlier cases.
1.2.5 -
   Misc. changes:
   * Updated Simulated Point Defence from 0.91 to 0.92 - this will not make the ship target projectiles that have same parent and target ID (update for compatibility with the SG Drone weaponry from CanonicalAlteranTechnologies).
1.2.4 -
   Potential optimization Fixes:
   * Updated Turrets script to 0.999 - it is just a tiny bit cleaner.
1.2.3 -
   Bug Fixes:
   * Added autoload fix "FIX-FoundationTech20050703ShipInstanceDetach", which solves problems related with iterating lTechs when detaching and removing from such list.
1.2.2 -
   Bug Fixes:
   * Updated AutoTargeting to the 2009 version, removing the multiple-buttons issue.
1.2.1 -
   Bug Fixes:
   * Updated Fool Targeting Technology from 0.2 to 0.3, fixed small thing related with necessary update.
1.2.0 -
   Updates:
   * Updated Fool Targeting Technology from 0.1 to 0.2, following a less smelly focus. Thanks USS Sovereign!
1.1.9 -
   New Features:
   * Fool Targeting script 0.1 -> Opportunity to tune beam and torp/pulse innacuracy!
   ** From this tech, created Minbari Stealth 1.0 - it will make ships below a certain sensor range to have locking issues when attacking a ship with this sub-tech.
   * Tachyon Sensor technology 0.1 ->
   ** Pros: they have a chance to reveal cloaked vessels (at least, those which don't use a special type of cloak)
   ** Pros/Cons: more/less vulnerable to Minbari Stealth according to a pInstance value!
   Bug Fixes:
   * Updated Simulated Point Defence 0.91 to 0.92 - it is so slightly tiny bit slower, but reduces some collision issues.
   * Updated Turrets technology 0.996 to 0.997, now it changes torps and disruptor IDs on a cleaner way.
1.1.8 -
   New Features:
   * Added Simulated Point Defence 0.91 to the Babylon 5 mod, to several ships.
   Balancing:
   * Found out I forgot to properly adjust the immediate reload delay value on the Hyperions, Novas and Omegas - they should not have been spamming those heavy torpedoes as much as they did. Now that is fixed, which
   combined with having a Starfury compliment launched (with most fighters getting Simulated Point Defence), should make the battles between those last a bit longer.
1.1.7 -
   Bug Fixes:
   * Updated Turrets technology to 0.996, it should be even more clean on the console now.
1.1.6 -
   New Features:
   * Increased arc width and height of three of the Victory-class beams for better coverage.
   Bug Fixes:
   * Updated Turrets technology to 0.995.
	- Adapted script to avoid editing the singleton as much as possible.
	- Now this tech is even more stable.
	- Upon discovery that the pInstance is not calling cleanup for this tech upon Detach or DetachShip, an improvised and improved manual cleaning method has been added, that should mitigate the issue.
1.1.5 -
   New features:
   * Subtle buff to Warlock's Aegis Particle Beam cannons.
   * Made such beams a bit lighter.
1.1.4 -
   Fix to Automated Destroyed System Repair documentation, clarified as 0.51.
1.1.3 -
   New Features:
   * Whitestars and Bluestars gained Automated Destroyed System Repair... but veeeeery slow.
   Bug Fixes:
   * Updated Automated Destroyed System Repair to 0.5.
	- Bugfix about singletons.
	- Bugfix/workaround around pShip.RemoveVisibleDamage() bug that the .exe has.
1.1.2 -
   * Updated Turrets technology 0.99 -> 0.991 (now using ship's ID as a cleaner reference, and optimized code a bit)
1.1.1 -
   * Improved Jumpspace Module.
1.1.0 -
   * Updated Turrets technology 0.98 -> 0.99 (some code has been optimized, so it is less expensive to make phaser or tractor turrets)
   * Made the T-turret hardpoint properties non-targetable (to avoid the potential "destroyed model area -> destroyed system" issue)
1.0.9 -
   * Added Turrets technology 0.98 for the EAS Victory.
   * Added Automated Destroyed System repair 0.4 to the Vorlon vessels, the Shadow scout and battlecrab, and the First One vessels
   * Updated readme with an important thing I forgot to add.
1.0.8 -
   * Upgraded the Hull Polarizer script to 1.2 - now it lasts longer.
1.0.7 -
   * Upgraded the Hull Polarizer script to 1.1 - now it also protects from visible damage to an extent.
1.0.6 -
 Fixes: now that I know how to make things right, I've added some of the Techs used on the proper file, to avoid overwriting defaults:
   * The Special "Hull Polarizer"/Special field defense tech which was used as a watered-down Minbari-Earth Alliance-Vorlon PolyCrystalline Armour for the Excalibur now has its proper own file at scripts/Custom/Techs
   * Fixed random bug that made the aforementioned tech from working at full capacity even after docking with a Starbase.
   * Fixed Minbari Sharlin PolyCrystalline Armour not covering things completely.
   * Fixed that the shield techs were inside the generic shield file, now they are at scrips/Custom/Techs/B5Defences.py . Left the expanded ATPFunctions library, though.
 Licensing: 
   * Added a bit more detailed sections to the readme.
1.0.5 -
 * Licensing: by petition of Dasher42, added the SDK license and Foundation readme.
1.0.4 -
 New Features:
 * Some ships like the Victory and the Omegas gained automatic multi-targeting.
 Small Fixes on syntax use (thank you Elijah)
1.0.3 - 
 New Features:
 * Since the 1.0.2 was not approved yet, I've decided to add a mod I nearly forgot about that added more music to the battles, including Babylon 5.
1.0.2 - 
 Bug Fixes:
 * Missing Bluestar fusion beams, now fixed! Thanks to RetroBadger for finding it out!
1.0.1 - 
 Bug Fixes:
 * SkyHawk hardpoint had the shuttle Mvam hull set as critical, now it won't randomly explode.
 * Fixes to Torvalus Dark Knife hardpoint, shielding was not regenerating.
 * Fixes to projectiles B5ThirdspaceTeleAttack and B5ThirdspaceTeleAttack2, now the AI swap should be clean(er). Be careful players, that will mean friendlies will attack you.
 Extra Features:
 * Minbari Sharlin hardpoint gained another Fusion Beam Cannon, as seen in Thirdspace movie.
1.0.0 - Mod released. Verified functionality on Kobayashi Maru Mod, and both disk and GoG versions of STBC (thanks to THE SCI-FI KING and RetroBadger Gaming).

== What does this mod do + Credits ==
***Basically every other pre-existing Babylon 5 ship mod has been overhauled by Alex SL Gato to include Jumpspace Drive, usually additional weapons and techs, and to balance each other - for example we had a Minbari cruiser to the level of a Sovereign and then we had a regular Omega which crushed easily several Minbari Sharlins, that won't do.
Additionally around 60+ ships from the Babylon 5 franchise have been added***

- Most meshes and textures not present on the other mods/readmes were taken from the Celestia Motherlode or remodeled by Alex SL Gato (tardisfromtornspace) when too complex for the tools used, with Blender and Milkshape. When those tools failed, rebuilt from mostly scratch (Earth Alliance Explorer).
- Icons done by Alex SL Gato (by screenshotting the progress done in the Milkshape 3D tool).
- scripts: for the most part Alex SL Gato, except the Babylon 5 Jumpspace technology, which was adapted from the Slipstream's creator (USS Sovereign, most likely) by Alex SL Gato
- mod/ships/hardpoint: Alex SL Gato.
- Special shadow cloak/decloak sound: taken by Alex SL Gato from the Babylon 5 season 4 intro.
- Movie intro: All credit to the original visual effects artists at Foundation Imaging and Netter Digital who made television history.
- ATPFunctions: originally made by Apollo, later expanded by Alex SL Gato.
- B5Defences: originally based on Shields.py by MLeoDaalder and Dasher42, then heavily modified by Alex SL Gato.

Fulfilling both the SDK and LGPL licenses:
THIS MOD IS NOT SUPPORTED BY ACTIVISION

This mod falls under the GNU LESSER GENERAL PUBLIC LICENSE Version 3, 29 June 2007, both from any derivative or original work done to the mod. Everyone is permitted to copy and distribute verbatim copies of this mod. As per the LPGL license, everything in this mod is open for everybody to use, read and modify. Just do not forget to credit everyone involved and follow the LGPL license so derivatives of this code remain LGPL.

===Mods required===
You'll of course need Foundation, Nanofx2, Submenu v 3.0, QBAutostart and Kobayashi Maru mod, the latest version the better. 

===Installation Guide===
1º Ok, first of all, just in case, backup your STBC.

2º After that, just unzip the files into your STBC folder, say "yes" to overwrite all the files.

3º After opening your STBC go to the options and activate "The Jumpspace" in start menu, and then activate all the new incorporated mutators (this mod uses foundation, all variants of Mvam, B5 uniforms, and Jumpspace, plus point defence, redistribute shields and repair destroyed systems mod. Ensure all of those Mutators are activated when playing to get the best experience of the B5 mod).

4º It's strongly recommended to activate DS9FX so No Damage through Shields is active, but it's not necessary.

--- Why those mutators/configurations are important ---

1st: Without the jumpspace mod active, none of the Younger Races ships can leave the system (to make it more canon to the series). Oh, and don't worry, I made it so the jumpspace engines can actually be engines so you can actually use emergency repair and repair destroyed systems properly on them... unlike the Hyperdrive or Slipstream mods.

2nd Foundation is vital because for most of the Babylon 5 races, there's at least one Foundation function working to make it more canonical, with No Damage Through Shields helping considerably on overriding normal shield behaviour. Without those functions the ship defences for most babylon 5 ships are pretty weak since they'll have no defence grids, point defence, gravitational defences, polycristalline armour... just the unmodded shield which was only used as a token to make the modded defences work.
* That token shield is for the most part meant to be extremely weak and have little regeneration because:
** Canonically, most Babylon 5 races don't have a bubble energy shield like Star Trek.
** A strong bubble shield on Star Trek Bridge Commander is capable of preventing beam weapons from actually hitting the hull even with the "no damage through shields" DS9FX option inactive, unless you make them ridiculously powerful, to the point in order to make an Earth Alliance ship be capable of firing beams which can hit the hull of another Omega like in the real show, you cannot have an omega or hyperion-class level of laser power to hit through, they need to have a beam as powerful as the Ori blast beam or the original Shadow Battlecrab mod - for a reference, that old mod could insta-kill the Armoured Voyager and any normal Omega in half a second - and that won't do.
** The token shield combined with the modded techs ensures that Beams actually are the most powerful weapon in Babylon 5, instead of a random person firing pulses o torpedoes - a shield in unmodded STBC actually recovers strength even while being hit, so beams against a fast-regenerating shield become almost worthless, while torpedoes and pulses give their payload damage in a single instant.

--- Known Bugs ---
* The B5 Intro is soundless and a bit glitchy, but apart from that everything else seems fine. Just in case, it has been disabled, but if you want, you can enable the B5Intro manually in Autoload.

- if you find more bugs, report them.
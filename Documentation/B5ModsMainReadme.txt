==Changelog==
1.6.2 -
   Fixes:
   * Updated Jumpgate TravellingMethods to 0.25, now the check for ISI tractor ship should be less intensive.
1.6.1 -
   Fixes:
   * Clarified readme further, and fixed a few placeholder files.
1.6.0 -
   Fixes:
   * Updated Victory Turret options to fix a small goof while warping.
   * Updated the readme a bit to clarify install of dependencies.
   * Given a glow-up to the Warlock: buffed its particle rays and made their weapon positions look better.
1.5.9 -
   Fixes:
   * Updated Jumpgate TravellingMethods to 0.24, now the cehck for if a ship can use them or not should be slightly more efficient.
1.5.8 -
   Fixes:
   * Removed dependency code from Babylon 5 Uniforms (except newer parts), since it was pretty much downloaded from the dependency.
1.5.7 -
   Fixes:
   * Upgraded Jumpgate Travelling Method so now the vortex is synced properly.
1.5.6 -
   Fixes:
   * Upgraded Jumpgate Travelling Method to 0.12, now the drifting bug is solved and the entry vortex will generate properly.
1.5.5 -
   Fixes:
   * Removed leftover DS9FX configuration files.
1.5.4 -
   Fixes:
   * Updated Jumpgate TravellingMethod to 0.11 fixing an issue with determining if the ship could travel to a non-gate system.
1.5.3 -
   Updates:
   * Added a very simplistic Jumpgate TravellingMethod, done in a few hours. This one allows vessels close to a jumpgate to open a vortex to jumpspace and travel to another system with a jumpgate. Ships with regular jumpspace drive can also use the gates to travel to any system regardless of having a gate at the end. It uses GalaxyCharts too.
   Fixes:
   * Updated Jumpspace modules to fix a cloak no-check issue.
   * Made Jumpspace ISI methods a bit more precise.
   * Fixed that certain vessels could use warp (I thought I had fixed that years ago?)
   * Made jumpgates visible from further ranges.
1.5.2 -
   Fixes:
   * Updated Jumpspace modules to fix a cloak no-check issue.
1.5.1 -
   Fixes:
   * Updated inner documentation on TransDimensional Drive.
1.5.0 -
   Updates:
   * Removed all content by PSYCH0 and USS Sovereign, to resolve DMCA takedown.
   * In order to enforce the reasons for the DMCA takedown, modified the "scripts/Custom/Autoload/zzzJumpspaceMode" and "scripts/Custom/Jumpspace/JumpspaceModule" (both .py and .pyc) files so they are empty and thus if somebody had installed older versions with the infracting module, this will ensure that module is no longer there.
   * Created new Jumpspace Drive based on adding TravellingMethods to the scripts/Custom/TravellingMethods folder that USS Frontier's GalaxyCharts checks:
       - Jumpspace Drive - all ships with an operative jumpspace drive can use it. Phased Jumpspace will perform the same but with cloaking and Shadow sounds.
       - Quantumspace drive - twice faster than regular Jumpspace drive. At the moment, used only by Vorlons, albeit they will not use it often.
       - TransDimensional Drive - extremely fast, used by The Traveller from Sigma 359.
   * Updated MinJW to reflect the Jumpspace change.
   * Added more canonical sounds.
1.2.31 -
   Updated for legal reasons:
   * By petition and demand of USS Sovereign, removed Jumpspace Module from the entire mod.
1.2.30 -
   Fixes:
   * Fixed small goof on G'quan's technologies.
1.2.29 -
   Fixes:
   * By petition of Greystar, made something to make MinJW not deal as much damage on ships he deems so with a proper tech.
1.2.28 -
   Fixes:
   * Found out that Defiant's Power system could glitch out if a ship had impulse engines but no warp engines. The new Autoload patch "FIX-DefiantsQBautostartPower1dot0.py" aims to resolve that issue.
1.2.27 -
   Fixes:
   * Found out that UniMod's way of dealing subsystem damage was also applying to other projectiles (now fixed): B5ThirdspaceFireball, B5ThirdspaceTeleAttack, B5ThirdspaceTeleAttack2, shadowSpit and VorlonWeapon.
1.2.26 -
   Fixes:
   * Found out that UniMod's way of dealing subsystem damage for MinJW's projectile could sometimes cause crashes on certain vessels if those were already dying or nearly dead and then were hit again and a destroyed system was destroyed twice. Now that is fixed.
1.2.25 -
   Fixes:
   * Ensured the Mvam of the Battlecrab to launch fighters en-masse has no risks of shadow fighters crashing with the battlecrab.
1.2.24 -
   Updates:
   * Made the jump point 'torpedo' stop sending print data about the system they are in.
   * Made frontal Vorlon Planetkiller shield a bit stronger.
1.2.23 -
   Updates:
   * Made the jump point 'torpedo' actually perform a jump point animation upon hitting, and also its damage now depends a bit on radious too.
1.2.22 -
   Updates:
   * Made the simulated Point Defense for the Vorlon Cruiser be a bit slower but slightly more successfull, to prevent weird cases of starvation between firing the only weapon at the enemy, or firing it at a bunch of torpedoes.
1.2.21 -
   Updates:
   * Made the simulated Jump Point weapon be... well, more like a Jump-point visually. Using blue colors instead of brown ones due to torpedo flare shenanigans.
1.2.20 -
   Fixes:
   * Fixed a slight issue with Turrets script during warp, and slightly better cleanup.
1.2.19 -
   Fixes:
   * Made Tachyon Sensors a bit more robust.
   * Updated AutomaticDestroyedSystemRepair script to 0.62 to be a bit more robust.
   * Fixed that goof from the original G'Quan and Th'Nor that made the engines the engine controls and the engine control the sole actual engine.
   Updates:
   * Made G'Quan and Th'Nor visible from further distance.
1.2.18 -
   Fixes:
   * Updated AutomaticDestroyedSystemRepair script to 0.61 to fix a glowUp issue with the Breen Drainer fix. 
   Updates:
   * Given a glowup to the G'Quan and the Primus' weapon systems.
1.2.17 -
   Fixes and updates:
   * Updated AutomaticDestroyedSystemRepair script to 0.6 to fix weird edge-case issue with Breen Drainer on certain tech combinations.
1.2.16 -
   Updates:
   * Updated FoolTargeting to 0.4 to support new modes of target miss.
1.2.15 -
   Fixes:
   * Updated TachyonSensors, Turrets and SimulatedPointDefence so its configurations work regardless of MissionLib settings.
1.2.14 -
   Fixes:
   * Updated AutomaticDestroyedSystemRepairDummy so the dummy name does not trigger some defence scripts.
1.2.13 -
   Fixes:
   * Updated Turrets script to 0.9993, making turret fetching more efficient, it should impact computers even less. Also made the Body parameter optional, so if the parameter is not there, no main body model replacement is done.
1.2.12 -
   Fixes:
   * Updated Turrets script to 0.9992, fixing a same-file turret issue and covering an additional cloak situation.
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
- scripts: for the most part Alex SL Gato, except the Babylon 5 Jumpspace technologies, which was created as several TravellingMethods using the template provided by USS Frontier, creator of GalaxyCharts.
   - I was informed that the old version of Jumpspace technology, adapted from the Slipstream's Framework (by USS Sovereign) did not meet the copyright requirements and as thus it was (naturally) taken down. If you have a B5 superpack mod previous to 1.5.0, you MUST download the latest version, which will ensure that older module is removed. Please, if you find any other infringment, do not hesiste to contact me.
- mod/ships/hardpoint: Alex SL Gato.
- Special shadow cloak/decloak sound: taken by Alex SL Gato from the Babylon 5 season 4 intro.
- Movie intro and several Babylon 5 sounds: All credit to the original visual effects artists at Foundation Imaging and Netter Digital who made television history. Jumpspace noise sounds found on http://b5.cs.uwyo.edu/bab5/allsrch.cgi, which were extracted by anmolnar.
- ATPFunctions: originally made by Apollo, later expanded by Alex SL Gato.
- B5Defences: originally based on Shields.py by MLeoDaalder and Dasher42, then heavily modified by Alex SL Gato.
- Special thanks to the already present mods (most of them from https://www.gamefront.com/games/bridge-commander/category/babylon5):
  - Fighter Launchable Babylon 5 (https://www.gamefront.com/games/bridge-commander/file/fighter-launchable-b5-station): TiqHud, Brad Bowermaster, Wok, Crook, Cordanilus and MScott.
  - Thunderbolt (https://www.gamefront.com/games/bridge-commander/file/thunderbolt): TiqHud, Wok, Bravo Int.
  - Aurora Class Starfury (https://www.gamefront.com/games/bridge-commander/file/aurora-class-starfury): MadJohn, Crook and the http://www.b5tech.net team and the Homeworld mod teams.
  - Minbari Sharlin (https://www.gamefront.com/games/bridge-commander/file/minbari-sharlin-class-dreadnought): Maryam, baz1701 and limey98 and Dalek. NOTE: The one I had on my install was NOT MSR1701's version.
  - B5 Centauri Vorchan (https://www.gamefront.com/games/bridge-commander/file/b5-centauri-vorchan) and B5 Centauri Warship (latter also known as Centauri Primus, https://www.gamefront.com/games/bridge-commander/file/b5-centauri-warship): TiqHud, Wok, Jackal and Captain Russel.
  - Babylon 5 - Bluestar (https://www.gamefront.com/games/bridge-commander/file/babylon-5-bluestar) and Babylon 5 Whitestar (https://www.gamefront.com/games/bridge-commander/file/babylon-5-whitestar): Nadab Göksu, Kier Darby, Thunderchild, DamoclesX, TiqHud, aobob, junky58 and BCU people (the latest 4 are beta testers).
  - Narn - ThNor (https://www.gamefront.com/games/bridge-commander/file/narn-thnor-1): TiqHud, Wok, Lord Malek and the original Babylon 5 visual effects artists mentioned before.
  - Narn G'quan (https://www.gamefront.com/games/bridge-commander/file/narn-g-quan-1): TiqHud, stresspuppy, Queball.
  - Drakh Raider (https://www.gamefront.com/games/bridge-commander/file/drakh-raider): TiqHud, Wok, Jackal Tiger, Nadab, Lord Malek and the original Babylon 5 visual effects artists mentioned before.
  - Omega Class Destroyer (https://www.gamefront.com/games/bridge-commander/file/omega-class-destroyer): MadJohn and Spooky.
  - B5 Warlock (https://www.gamefront.com/games/bridge-commander/file/b5-warlock) and Babylon5 Victory (https://www.gamefront.com/games/bridge-commander/file/babylon5-victory): DamoclesX and Durandal.
  - Shadow Battlecrab (https://www.gamefront.com/games/bridge-commander/file/shadow-battlecrab): Sci-Fi DreamYards, Cpt. LC Amaral, Maverick, Executioner_de.
  - Centauri Sentri fighter (no hardpoints, https://www.gamefront.com/games/bridge-commander/file/centauri-sentri-fighter): Wok and Bravo Int.
  - Vorlon Fighter (no hardpoints, https://www.gamefront.com/games/bridge-commander/file/vorlon-fighter) by Wok, Jackal and the B5 Sci-fi show.
  - Babylon 5 Uniforms (https://www.gamefront.com/games/bridge-commander/file/babylon-5-uniforms) by Houliganisle, Crazyhid and MLeo. 

Fulfilling both the SDK and LGPL licenses:
THIS MOD IS NOT SUPPORTED BY ACTIVISION

This mod falls under the GNU LESSER GENERAL PUBLIC LICENSE Version 3, 29 June 2007, both from any derivative or original work done to the mod. Everyone is permitted to copy and distribute verbatim copies of this mod. As per the LPGL license, everything in this mod is open for everybody to use, read and modify. Just do not forget to credit everyone involved and follow the LGPL license so derivatives of this code remain LGPL.

===Mods required===
You'll of course need Foundation, Nanofx2, Submenu v 3.0, QBAutostart and Kobayashi Maru mod, the latest version the better. GalaxyCharts is also required, probably the GalaxyCharts Warp AI fix as well.

All the mods on https://www.gamefront.com/games/bridge-commander/category/babylon5 mentioned above, on reverse order (NONE of the ones called "Remastered") would be probably required (albeit at the time I downloaded the mods from NexusMods so the content may have been different), **but** some of them conflicted with each other due to Caps issue (i.e. EAOmega - eaomega), certain shuttle quirks and BCMMods affected certain filenames and inner files, which back when I was a newbie took me 3 years to fix, made that unadvisable. What I recommend to do is to do the following: get those mods downloaded on a temp folder, grab ONLY the data and sfx folders, make sure they follow the proper folder names, case-sensitive (i.e. they should be called "Icons", not "icon", example on the G'Quan where that bug happened), icon names, model names and sound names (some, when legally allowed, seen inside this super-pack. They are meant to be placeholders so the correct case-sensitive names work), and then, after ensuring all the files are there, copy the unzipped super-pack to another temp folder (let's call it "temp folder SuP"), then copy the data and sfx fixed folders from those mods to "temp folder SuP", and then copy the sfx and data ones from the super-pack again onto "temp folder SuP". That procedure should guarantee that all the folders and files are named properly while using those mod files and having updated ones (because when Windows OS replaces a file by another it may replace the contents, but if one was called "AAAA" and the other "aaaa" then the name of the oldest file will remain). 

For older mods like the Shadow Battlecrab mod which is stored on .BCMod format you may require of extra tools, like BCUT -> BCTools -> BCMod Unpacker (https://www.gamefront.com/games/bridge-commander/file/bridge-commander-universal-tool-bcut-v-1-8-1)

For some other mods that are inside .exe like the Omega-class, you might need to create a "fake" install - which requires of data, sfx and script folders and stbc.exe - fortunately for the Omega-class that is not the case.

Also this one, Babylon 5 uniforms https://www.gamefront.com/games/bridge-commander/file/babylon-5-uniforms, but only some elements

===Installation Guide===
STEP 0: Ok, first of all, just in case, backup your STBC.

1º Follow the steps indicated on mods required as well, skip the babylon 5 uniforms one, which we will do on the following steps. The Bluestar, Drakh Raider, Fighter Launchable Babylon 5, G'Quan, ThNor, Thunderbolt and Whitestar are not exactly required to be installed from there (as they are already on this super-pack), but welcome to give their authors more credit. 

2º Install the Babylon 5 Uniforms mod from https://www.gamefront.com/games/bridge-commander/file/babylon-5-uniforms on a temporary folder, then go to TEMPFOLDER/scripts/Custom/Autoload and remove the file "Tmp crew".

3º Unzip the files from this main mod (the ones already passed through step 2 "temp folder SuP") onto the temporary folder created in 2, say "yes" to overwrite all files.

4º After that, just move the files from the temp folder into your STBC root folder, say "yes" to overwrite all the files (data -> data, scripts -> scripts, sfx -> sfx, and so on).

5º After opening your STBC go to the options -> Customize -> Mutators and make sure that "USS Frontier's Galaxy Charts"/"Galaxy Charts" are active. Optionally, make sure "Babylon 5 Uniforms" is also active.

6º It's strongly recommended to activate DS9FX so No Damage through Shields is active, but it's not necessary.

--- Why those mutators/configurations are important ---

1st: Without the Galaxy Charts active, none of the Younger Races ships can leave the system (to make it more canon to the series). Oh, and don't worry, I made it so the jumpspace engines can actually be engines so you can actually use emergency repair and repair destroyed systems properly on them.

2nd Foundation is vital because for most of the Babylon 5 races, there's at least one Foundation function working to make it more canonical, with No Damage Through Shields helping considerably on overriding normal shield behaviour. Without those functions the ship defences for most babylon 5 ships are pretty weak since they'll have no defence grids, gravitational defences... just the unmodded shield which was only used as a token to make the modded defences work, and some extra shield-unreleted techs.
* That token shield is for the most part meant to be extremely weak and have little regeneration because:
** Canonically, most Babylon 5 races don't have a bubble energy shield like Star Trek.
** A strong bubble shield on Star Trek Bridge Commander is capable of preventing beam weapons from actually hitting the hull even with the "no damage through shields" DS9FX option inactive, unless you make them ridiculously powerful, to the point in order to make an Earth Alliance ship be capable of firing beams which can hit the hull of another Omega like in the real show, you cannot have an omega or hyperion-class level of laser power to hit through, they need to have a beam as powerful as the original Ori blast beam or the original Shadow Battlecrab mod - for a reference, that old mod could insta-kill the Armoured Voyager and any normal Omega in half a second - and even sometimes that would not be guaranteed to destroy the vessel. Naturally that won't do.
** The token shield combined with the modded techs ensures that Beams actually are the most powerful weapon in Babylon 5, instead of a random person firing pulses o torpedoes - a shield in unmodded STBC actually recovers strength even while being hit, so beams against a fast-regenerating shield become almost worthless, while torpedoes and pulses give their payload damage in a single instant.

--- Known Bugs ---
* The B5 Intro is soundless and a bit glitchy, but apart from that everything else seems fine. Just in case, it has been disabled, but if you want, you can enable the B5Intro manually in Autoload.

- if you find more bugs, report them, please.
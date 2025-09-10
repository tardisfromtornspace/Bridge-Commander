==Changelog==
1.2.2 -
   Updates:
   * Updated SimulatedPointDefence to 1.0 to allow cleaner logic and cleanup.
1.2.1 -
   Updates:
   * Added an Autoload patch that provides full customization for slipstream for GC. 
1.2.0 -
   Updates:
   * Updated readme and install guide to reflect new versions.
   * Added a finished version of BCXtreme's originally incomplete Slipstream TravellingMethod for GalaxyCharts; extending USS Sovereign's Slipstream Module functionality to AI separate ships as long as GalaxyCharts is active.
1.1.9 -
   Fixes:
   * Removed code that was not being used.
1.1.8 -
   Fixes:
   * Found out that Defiant's Power system could glitch out if a ship had impulse engines but no warp engines. The new Autoload patch "FIX-DefiantsQBautostartPower1dot0.py" aims to resolve that issue.
1.1.7 - Fixes:
   * Updated Andromeda's 'Nova Bomb' projectile to prevent a possible issue from UniMod's implementation.
1.1.6 - Fixes:
   * Updated Andromeda's ship file so holes are less pronounced, updated armour and hull regeneration to be a bit more realistic, re-updated torpedoes and "shields" to reflect this and fixing a bug.
1.1.5 - Misc. changes & Potential Bug Fixing:
   * Updated Simulated Point Defense so one of its configurations works regardless of MissionLib custom settings.
1.1.4 - Misc. changes & Bug Fixing:
   * Updated all Slipfighter Custom/Ships files so they are under a SubSubMenu.
   * Fixed an error on the original hardpoint that was preventing the Andromeda and other variant ships from actually using their torpedo launchers at max.
1.1.3 - Misc. changes:
   * Updated Simulated Point Defence from 0.91 to 0.92 - this will not make the ship target projectiles that have same parent and target ID (update for compatibility with the SG Drone weaponry from CanonicalAlteranTechnologies).
1.1.2 - Bug Fixing:
 * Updated Simulated Point Defence 0.91 to 0.92 - it is so slightly tiny bit slower, but reduces some collision issues.
1.1.1 - Features
 * Fixed battle blades color and added the two lower battle blades.
1.1.0 - Bug Fixing
 * Upgraded Simulated Point Defence to 0.91, removing a potential issue with singletons.
1.0.9 - Bug Fixing
 * Upgraded Simulated Point Defence from 0.8 to 0.9, now two possible crash causes upon heavy fire have been removed. Thank USS Sovereign for telling me how to use the debug function properly.
1.0.8 - Bug Fixing
 * Upgraded Simulated Point Defence from 0.6 to 0.8, now a lot of the weird behaviour happening before has been fixed.
1.0.7 - Bug fixing
 * Fixed Simulated Point Defence TypeError sequence issue - it didn't really cause any problems but it was flagged on the console and would have caused problems if the sequence had multiple actions.
1.0.6
* Fixed a bug with Simulated Point Defence Tech
1.0.5
* Improved the Simulated Point Defence Tech
1.0.4
* Added a total-side point-defence EXPERIMENTAL technology which allows the ships to be more realistic - only kept shields on the Andromeda to allow the reflector shield effect, everything else fully canon now with no shields.
1.0.2
* Added multi-targetting technology
1.0.1
* Updated missing ValiantMissile
1.0 Mod release. Changes compared with the original Andromeda:
* Adjusted weaponry, defenses and explosive power.
** Shields and hull are far, far weaker but now can rebound some incoming projectiles, the shields adapt a bit, the ship has (manual) Point Defence and has some Armor now, and regenerates a bit faster.
** Additionally some of their torpedoes can hit their target at lightminutes from the target.
** If necessary the Andromeda can blow a planet as well.
** No warp drive, only Slipstream engine -> DOWNLOAD SLIPSTREAM MOD IF YOU WANT TO LEAVE A SYSTEM.
** Battle blades!

== What does this mod do ==
This mod is a modification set of files for an older Androemda mod, of which I did not know which one until very recently. The older mod had mostly normal technologies, moved by warp drive and had an energy shield. This change intends to make it more canon, providing stuff like Simulated Point defence, armour and some related files. From version 1.2.0 it also includes a Slipstream extension for GalaxyCharts which is the complete version of https://www.gamefront.com/games/bridge-commander/file/slipstream-for-galaxy-charts by BCXtreme.

== Dependancies ==
All of these must be installed before installing this mod, in this order:
* Foundation + FoundationTechnologies + Kobayashi Maru + Launching framework + GalaxyCharts (KM has Foundation, FoundationTechnologies and GalaxyCharts already installed - the most recent version of KM, the better).
* Slipstream Module mod by USS Sovereign, else your ship will not travel between systems (can be found on gamefront)
* All the dependencies for this mod + the mod: https://www.gamefront.com/games/bridge-commander/file/stbc-babylon-5-mod
* All assets from the incomplete original Slipstream for GalaxyCharts from https://www.gamefront.com/games/bridge-commander/file/slipstream-for-galaxy-charts, except scripts/Custom/TravellingMethods/Slipstream.py.new, which should NOT be included on your install (so, basically the files at scripts/Custom/GalaxyCharts), by BCXtreme.
* This mod (BUT ONLY SOME PARTS, see install instructions below, step 5): https://www.gamefront.com/games/bridge-commander/file/andromeda-ascendant

== Credits ==
* Everyone involved in Foundation - without you this would have been a real pain to do (please read the separate Foundation.txt license) - Banbury, Dasher42, DigitalFriend, MLeo, Nanobyte and Sleight42, among others.
* Everyone involved in KM and GalaxyCharts - specifically those involved in the creation of armour and Shields.py (FoundationTechnologies) - Apollo from ATP Technologies as well.
* Dasher42 and USS Sovereign for reminding me of licensing.
* USS Sovereign also made the Slipstream Module, which, to clarify, remains All Rights Reserved, by USS Sovereign.
* USS Frontier for creating GalaxyCharts, which is also ALL Rights Reserved by USS Frontier. However, since GC supports Plugins it is fair to release a new TravellingMethod or patch old ones as long as the original files remain unmodified. 
* BCXtreme for the original incomplete Slipstream for Galaxy Charts. This plugin was originally released without a license, which means it defaults to All Rights Reserved. While the original readme includes the line "As far as I am concerned, anyone can take this and finish it if they want to," that grants permission to continue development — but not to relicense or attach a license such as LGPL. The absence of an explicit license means the work cannot be treated as open source.
* Probably, the people involved in one of two mods (or maybe both or neither, more than a decade passed since the time I installed the first andromeda mod and I think I may have downloaded it from somewhere that was not gamefront/filefront and the readmes had long since been overwritten by a ton of other mods having the exact same filename on the exact same folder). So just in case:
** For one of them (which was the least likely to have been downloaded, as back then I did not download "betas" that much and also some key files look too different), Ruivo, Khaliban and Darkthunder were responsible - give them many thanks, just in case it was them https://www.gamefront.com/games/bridge-commander/file/andromeda-ascendant-beta .
** For the other (which was the one I downloaded most likely and the one which I tentatively included its readme, but for some reason currently on gamefront the only contents of the file are a few images) it was MRJOHN, Khaliban, Evan Light and Chris Edmund - give them many thanks as well (and to Khaliban twice) https://www.gamefront.com/games/bridge-commander/file/andromeda-ascendant.
* Tools used: Milkshape 3D for the battle blades and battle blades form, GIMP to modify and create textures and icons when necessary, Model Property Editor to iron-out a few hardpoint issues.
* Only things I can credit myself with (CharaToLoki) are fixing certain name case-sensitive issues, fixing certain Autoload and torpedo name errors, broken links and more that were causing the original mod from breaking my install or itself (like, a decade ago, so that comes from memory only), adjusting all the scripts to canon, the new technologies implemented, and things mentioned on the changelog.

== Install guide ==
1. Ok, first of all, just in case, backup your STBC.

2. create three temp folders outside, required for the install preparation:

3. Install dependencies if those are not installed already (please read the section above about dependencies). If slipstream-for-galaxy-charts or stbc-babylon-5-mod ones are unavailable, please contact me at andromedavirgoa@gmail.com

4. Unzip this mod onto one of the temp folders. Why am I asking you do do this, instead of directly unzip onto your install folder? Because of step 5 not being possible due to mod corruption. So we will improvise...

5. Download an uncorrupted version of https://www.gamefront.com/games/bridge-commander/file/andromeda-ascendant and place it on Temp folder 1. From this one, we are going to get some files manually, the ones we require are those located for the most part at data, particularly Icons/Ships and Models/Ships, following the structure seen below. You should see the following files and folders. Such folders MUST be named the same, case sensitive (that is, if you see data/models instead of data/Models, correct the folder name to be data/Models). If the folders data/Models/Ships/Andromada/High, Med and Low do not exist, we can mitigate this by creating them with those names, copy-pasting the files from data/Models/Ships/Andromada into the new folders, and renaming the .NIF of each to AndromedaHigh.nif, AndromedaMed.nif and AndromedaLow.nif, respectively. If the file is corrupted, do not hesitate to contact gamefront staff.

      STRUCTURE: (Sorry, reason this is explained like this is because the mod had already been swapped accidentally once before. Now it should be fixed, but just in case...)
         data <--- From here, ALL NEEDED, including all its children. Make sure the folders are named properly.
           - Models
              - Ships
                - Andromada
                   - High <--- This folder should have nearly the same files as the parent, but with an AndromedaHigh.nif
                   - Med <--- This folder should have nearly the same files as the parent, but with an AndromedaMed.nif
                   - Low <--- This folder should have nearly the same files as the parent, but with an AndromedaLow.nif
                   * 1_specular.tga
                   * 2_specular.tga
                   * 3_specular.tga
                   * 4_specular.tga
                   * 5_specular.tga
                   * 6_specular.tga
                   * 7_specular.tga
                   * 8_specular.tga
                   * 9_specular.tga
                   * 10_specular.tga
                   * 031i_glow.tga
                   * Andromeda.NIF
                   * Andytxtr_01_glow.tga
                   * Andytxtr_02_glow.tga
                   * Andytxtr_03_glow.tga
                   * Andytxtr_04_glow.tga
                   * Andytxtr_05_glow.tga
                   * Andytxtr_06_glow.tga
                   * Andytxtr_07_glow.tga
                   * Andytxtr_08_glow.tga
                   * Andytxtr_09_glow.tga
                   * Andytxtr_10_glow.tga
                - AndSlipFighter  <----- We need everthing from here, not just the files mentioned below.
                       * AndSlipFighter.nif
                       * SlipFighterMK1.nif
                       * SlipFighterMK2.nif
                       * SlipFighterMK3.nif
                       * slip2_glow.tga
                       * slip3_glow.tga
                       * slip4_glow.tga
                       * slip5_glow.tga
                       * slip6_glow.tga
                       * slip7_glow.tga
                       * slip8_glow.tga
                       * slip9_glow.tga
           - Icons <--- Everything from here NEEDED.
              - Ships
                   * AndArchlike.tga
                   * Andromeda.tga
                   * AndSlipFighter.tga
         scripts
           - Custom
              - Autoload <----- From this one we need NONE, as this mod creates its own fused ones.
              - Carriers
                   * Andromeda.py <---- NEEDED
              - Ships <----- From here we would need the ones below, but they would be overwritten by ours, if they are not misnamed.
                   * AndArchlike.py
                   * Andromeda.py
                   * AndSlipFighter.py
                   * AndSlipFighterMKI.py
                   * AndSlipFighterMKII.py
                   * AndSlipFighterMKIII.py
                   * AndSlipFighter.py
           - ships
                   * AndArchlike.py       <---- NEEDED
                   * Andromeda.py         <---- Will be overwritten
                   * AndSlipFighter.py    <---- NEEDED
                   * AndSlipFighterMKI.py   <---- NEEDED
                   * AndSlipFighterMKII.py  <---- NEEDED
                   * AndSlipFighterMKIII.py  <---- NEEDED
                   * AndSlipFighter.py  <---- NEEDED
              - Hardpoints <----- From here we would need the ones below, but they would be overwritten by ours, if they are not misnamed.
                   * AndArchlike.py
                   * Andromeda.py
                   * AndSlipFighter.py

           - Tactical
              - Projectiles <----- From here we would need the ones below, but they would be overwritten by ours, if they are not misnamed.
                   * ELSMissileTube.py
                   * NovaBombTorpedo.py
                   * PM6Disruptor.py
                   * PM6LCannon.py

         sfx <--- From here everything except the fils marked as "NOT NEEDED"
           - Weapons
                   * AndromadaEngine.wav <--- NOT NEEDED
                   * IntrepidCannon.wav  <--- NOT NEEDED
                   * NovaBombTorpedo.wav
                   * ValiantMissile.wav
           * AndromadaEngine.wav

         * credits.TXT - A copy of this file is contained on our mod Documentation folder as "oldAndromedaAscendantReadme.txt". Make sure it exists and is the same (apart from name and location, done so as to prevent doc overwrite issues, do not let you happen like with me, who practically had no idea which mod was which for over a decade).

         * Several images: 1.jpg, 2.jpg and ScreenShot040.jpg - these ones are unnneeded, do what you want with them.

6. After deleting the unneeded files from Temp Folder 1, unzip this mod on Temp Folder 2.

7. Copy-paste the contents of Temp Folder 2 to Temp Folder 3, then copy-paste the contents of Temp Folder 1 (now pruned of content) onto Temp Folder 3, then copy-paste again the contents of Temp Folder 2 to Temp Folder 3. Overwrite all files when requested. Since our mod pack has teh folders named properly on case-sensitive basis, this seemingly dumb action guarantees on Windows OS that at least all common files and folders are named properly without needing to manually change each folder and file.

8. Now paste Temp Fodler 3 onto your install folder. Overwrite all files when requested.

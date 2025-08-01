== Changelog ==
0.6.5 - Updates:
  * Created new trail script for projectiles with better customization but still similar to LJ's in regards to naming to allow backwards compatibility. Do not forget to install scripts.Tactical.Projectiles.trails.OriBeam now to have these working.
0.6.4 - Updates:
  * Updated Spore Drive for more efficient tractor ISI check.
0.6.3 - Updates:
  * Updated AlternateSubModelsFTL to 0.86 to support new "IgnoreCall" parameter and to clarify documentation better.
0.6.2 - Updates:
  * Since I found out how to make GalaxyCahrts use a different set for different travel types, added a Mycelial Network TravelerSystem to GalaxyCharts and updated SporeDrive to 0.5 to reflect this.
0.6.1 - Fixes:
  * Found out that Defiant's Power system could glitch out if a ship had impulse engines but no warp engines. The new Autoload patch "FIX-DefiantsQBautostartPower1dot0.py" aims to resolve that issue.
0.6 - Updates:
  * Updated SporeDrive to 0.4, now it also has customizable additional mini-spark chances for entry and exit, and can jump closer to other vessels.
  * Updated crossfield scripts/Custom/Ships file to reflect SporeDrive 0.4 changes.
  * Updated AlternateSubModelFTL to version 0.84 to fix a small documentation error.
0.5.6 - Updates:
  * Updated SporeDrive to 0.35, now it uses a custom animation GFX and its ISI system is more precise.
0.5.5 - Updates:
  * Updated this readme properly to credit all the authors behind the High-End Protostar model.
0.5.4 - Updates:
  * Updated AlternateSubModelFTL to version 0.83 to support custom exit and entry delay subPart times.
  * Updated USS Protostar Custom script to include this new update.
  * Partially updated Protostar Model with Greystar's additions, made by LoganRolphh on sketchfab, still a W.I.P.
0.5.3 - Fixes:
  * Updated MEShields to manually cover an edge-case where a torpedo hitting behind a shield is impossible.
  * Updated Turian Frigate hardpoints so they do not repair so fast.
0.5.2 - Fixes:
  * Updated ProtoWarp, SporeDrive and MassEffect FTL to 0.32, fixing a sound issue.
0.5.1 - Updates:
  * Added properly-adjusted Turian frigate and fighter.
  * Refined the use of Simulated Point Defence for the GARDIAN system.
  * Completed readme to fully localize where each thing came from.
0.5 - Updates:
  * Added Realistic Mass Effect technology and ships for the Normandy SR-1 and Cerberus and Alliance Normandy SR-2.
0.4.8 - Updates:
  * Updated AlternateSubModelFTL to version 0.82 to support vessels which do not have any models to replace.
0.4.7 - Updates:
  * Updated scripts/Custom/Autoload/FIX-GCNormalWarpAndEnhancedWarp.py to version 20241214 to reduce as much as possible any legal issues.
0.4.6 - Updates:
  * Created scripts/Custom/Autoload/FIX-GCNormalWarpAndEnhancedWarp.py version 20241213 that fixes a pre-existing glitch that caused a crash-to-desktop for KM's BorgAttack AI during GalaxyCharts travels.
0.4.5 - Updates:
  * Removed the Updated NormalWarp and EnhancedWarp, which I did not know were All Rights Reserved and could not be modified directly.
  * Created scripts/Custom/Autoload/FIX-GCNormalWarpAndEnhancedWarp.py, which fixes NormalWarp and EnhancedWarp via monkey patching, preventing a license violation.
  * Giving extra credit to USS Sovereign for helping me notice the legal issue above and how to fix it.
0.4.4 - Updates:
  * Updated NormalWarp and EnhancedWarp to version 20241212 to fix camera issues and support warp stretchiness again when using GC.
  * Updated SporeDrive to 0.3 to grant better speeds.
  * Updated Crossfield Custom/Ships file to cap warp speed at warp 7.0 like a very-early TOS vessel.
0.4.3 - Updates:
  * Updated Crossfield, SporeDrive and Spore Drive sounds to be a bit faster.
0.4.2 - Updates:
  * Updated AlternateSubModelFTL to 0.81 to so when a ship cannot move, it says "CANNOT DO" instead of just "CANNOT".
0.4.1 - Updates:
  * Updated SporeDrive to 0.2 to allow ISI to have a customizable chance to uncloak nearby vessels without phase cloak.
0.4 - Updates:
  * Updated AlternateSubModelFTL to 0.8 to give the script intra-system-intercept (ISI) support.
  * Updated SporeDrive to 0.19 to cover ISI support.
  * Updated readmes to cover use-conditions for the script, per USS Sovereign's request (and necessary condition for use).
0.3.6 - Updates:
  * Updated AlternateSubModelFTL to 0.76 to fix a bug with hardpoints not returning to normal after FTL.
  * Updated USSProtostar and USS Discovery hardpoints so all properties now have a proper 2DPosition.
  * Updated SporeDrive to 0.16 to fix the camera rotating issue and made it so people can tow ships.
0.3.5 - Updates:
  * Updated AlternateSubModelFTL to 0.75 to support the option to only perform entry or exit FTL sequences for each part and FTL method individually.
  * Updated SporeDrive to 0.15 to cover the new update to AlternateSubModelFTL.
0.3.4 - Updates:
  * Added a fragment of the Spore Drive - still missing proper flash textures and in-system interception!
  * Updated Documentation to fill these gaps.
0.3.3 - Updates:
  * Updated AlternateSubModelFTL to 0.71, fixing a potential issue related with different MissionLib files.
0.3.2 - Updates:
  * Updated scripts/Custom/Ships file to provide the full list of parts also in-game, pending of model repalcement and position/rotation adjustment.
0.3.1 - Updates:
  * Updated ProtoWarp TravellingMethod to 0.31, providing starting sound.
  * Updated scripts/Custom/Ships file to provide a more extensive list on what moves on the Protostar (as a list to help Greystar with models).
0.3 - Updated AlternateSubModelFTL to 0.7, finally making the tech independent from SubModels as well as fixing a weird non-experimental lights bug.
0.2 - Updated AlternateSubModelFTL to 0.64, fixed the rapid-change drifting for the most part, also now Experimental is no longer ugly at the beginning.
0.1 - First unofficial release, for testing

== What does this mod do ==
This mod adds the following updates and fixes:
* A new SubModels-derivated file that supports other FTL methods (from GalaxyCharts) and mobility fix and intra-system intercept (ISI) improvements.
* Proto-Warp Travelling Method.
** An USS Protostar from Star Trek Prodigy equipped with this drive (TO-DO W.I.P.).
** An USS Prodigy from Star Trek Prodigy equipped with this drive (TO-DO not yet added).
* Spore-Drive Travelling Method with ISI.
** A modified USS Discovery (Crossfield Class) equipped with Spore drive.
* Fixed NormalWarp and EnhancedWarp travelling methods:
** Now they support the ship stretching when it goes in an out of warp!
** The camera no longer gets a stroke when a ship is warping in or out, switching to several places and then having the warp flash on our face! Now they behave properly!
** Small allowance for max warp 10.0 as some vessels might allow that speed factor with regular warp methods.
* IMPORTANT: PATCH For BorgAttack AI version "Borg AI Final - 10 July 2008", present in KM 2011.10, while using GalaxyCharts with the Warp AI fix (also present in KM), so when GC is OFF, it uses the totally unmodified BorgAttack, but while GC is on, it can use BorgAttack Warp sections without causing a crash-to-desktop after a vessel with BorgAttack follows the player after two Warp jumps.
** This PATCH is on Autoload, and it is the only patch done on this mod to this AI, done under fair use and falling under the same license as the BorgAttack file, and does not release a modified BorgAttack file named BorgAttack.py, so in case of any problems are found with this patch, the file "FIX-BorgAttackAIforGC.py" can be safely removed without causing any changes to the BorgAttack.pyc your install may have.
** scripts/AI/Compound with BasicAttack.py, BasicAtatck.pyc and BorgAttack.pyc are also added here to follow the Borg AI doc (doc/Borg AI/BORG AI FINAL - README.txt) as best as possible while distributing this fix.
All of the technologies have their own detailed instruction manuals inside the files to ensure people can use those techs easily.

== Dependencies ==
All of these must be installed before installing this mod, in this order:
* Foundation + Kobayashi Maru (KM has Foundation already installed - the most recent version of KM, the better).
* GalaxyCharts (KM has this mod already installed. Required for ProtoWarp TravellingMethod and any method you may want derived from that).
* NanoFX 2.0 beta (KM already has this installed)
** Depending on the version of KM, you may require GalaxyCharts' Warp AI fix as well: https://www.gamefront.com/games/bridge-commander/file/galaxy-charts-warp-ai-fix/
* This mod, for the ST:Discovery original Crossfield class: https://www.gamefront.com/games/bridge-commander/file/crossfield-class
* This mod, for the SSV Normandy https://www.gamefront.com/games/bridge-commander/file/normandy-sr-1
* This mod, for the SR2 Normandy and ME3 Normandy https://www.gamefront.com/games/bridge-commander/file/normandy-sr-2
* This mod, for the Turian vessels https://www.gamefront.com/games/bridge-commander/file/turian-frigate
* All the dependencies for this mod + the mod: https://www.gamefront.com/games/bridge-commander/file/stbc-babylon-5-mod
** From here, HullPolarizer is the most used, but also the file "FIX-FoundationTech20050703ShipInstanceDetach.py", which solves problems related with iterating lTechs when detaching and removing from such FoundationTech list.
* This mod, for the projectile ExtraCollisionDamageDummy, scripts.Tactical.Projectiles.trails.OriBeam version >= 1.01 and certain NanoFX 2.0 Beta fixes implemented there: https://www.gamefront.com/games/bridge-commander/file/sg1-sga-and-sgu-generic-overhaul-mod

IMPORTANT INSTALL INSTRUCTIONS: Do not copy-paste this mod's scripts/AI folder right away, first move this mod's scripts/AI folder somewhere else. You only have to install it if the following steps require so. The provided AI scripts scripts/AI/Compound/BasicAttack and BorgAttack scripts can also be found at BCC KM 2011.10 download site (https://www.bc-central.net/forums/index.php?action=downloads;sa=view;down=33).

1. Check that on scripts/AI/Compound folder you already have a BasicAttack.py, BasicAttack.pyc, BorgAttack.py and BorgAttack.pyc, and BorgAttack.py contents on the first lines have a banner saying 'Borg AI Final - 10 July 2008' 'By: jayce AKA Resistance Is Futile' and then more text explaining how it is the latest version and thus that file should not be modified. If that does not appear, you will have to install the AI provided (something which, at least on a normal KM install 2011.10, unless modified, should not happen since this BorgAttack AI is technically added as a given).

2. Enter your KM game and activate automatic test mode (or your way to view the game's console), then install the rest of the folders from this mod normally. The console will send a message about "FIX-BorgAttackAIforGC", if it says "Your install's BorgAttack AI is not the final version to patch. Skipping...", "Missing BorgAttack AI to patch. Skipping..." or "FIX-BorgAttackAIforGC: just found out that your BorgAttack AI does not have a CreateAI function... this will be patched." that means you don't have the correct BorgAttack script and then you WILL need to install the AI too, but not before removing BorgAttack.py and BorgAttack.pyc from your install's scripts/AI/Compund folder, and verifying the scripts/AI/Compund/BasicAttack.py you have is the same as AI/Compund/BasicAttack.py this mod has (who knows, you could have modified your BasicAttack.py and still be a modified version of a valid one - it would not be the first time I've seen modified BasicAttack.py that work with the latest BorgAttack AI but which were modified to warp faster or not miss torpedoes...)
** The provided AI scripts scripts/AI/Compound/BasicAttack and BorgAttack scripts can also be found at BCC KM 2011.10 download site https://www.bc-central.net/forums/index.php?action=downloads;sa=view;down=33

== Credits ==
* Everyone involved in Foundation - without you this would have been a real pain to do (please read the separate Foundation.txt license) - Banbury, Dasher42, DigitalFriend, MLeo, Nanobyte and Sleight42, among others.
* Everyone involved in KM - specifically those involved in the creation of armour and Shields.py (FoundationTechnologies) the AdvArmorTech.py, FiveSecsGodPhaser.py, TractorBeams.py - Apollo from ATP Technologies as well.
* Dasher42 for reminding me of licensing.
* USS Sovereign for some DS9FX advice regarding timers, inspired in one of DS9FX Pulsar files for improved rotations, AND MOST IMPORTANTLY, for giving me permission to adopt fragments of his Slipstream Module for Intra-System-Intercept. Those sections, while still modified to be adjusted to the script, still fall under "All Rights Reserved" so you cannot modify or repacakge them without USS Sovereign's permission!
** Again USS Sovereign for helping me notice NormalWarp and EnhancedWarp were All Rights Reserved by USS Frontier and could not be modified directly without violating such license, helping me from suffering a legal headache.
* USS Frontier for GalaxyCharts.
* The authors of https://www.gamefront.com/games/bridge-commander/file/normandy-sr-1, https://www.gamefront.com/games/bridge-commander/file/normandy-sr-2 and https://www.gamefront.com/games/bridge-commander/file/turian-frigate (apparently Bones) for the original Normandy SR-1, SR-2 (Alliance and Cerberus), and the Turian fighter and Turian Frigate, whose READMES have also been included on this mod and which seem to only fall under teh SDK license (their contact is 1701abcde@gmail.com or PM them at http://www.bc-central.com/forums if there's any issue).
** Excerpt from both readmes (in case something happens and they are lost):
*** Bioware: Mass Effect 1&2&3 ; Normandy SR1 and SR2 Mesh and Turian Fighter and Frigate.
*** Activision/Totally Games: For Bridge Commander
*** Paramount and Gene Roddenberry: For Star Trek
*** dr_mccoy 11/Bones: Model conversion, new textures for Alliance version
*** BETA TESTERS for original sr1 and sr2 mods: TiqHud, Killallewoks, FarShot and Shadowknight1
*** SPECIAL THANKS TO BRIDGE COMMANDER CENTRAL COMMUNITY AND BETA TESTERS FOR ALL FEEDBACK AND SUPPORT.
* Defiant for some scripts that drew inspiration (or were practically used as a base), particularly the original SubModels.
* jayce AKA Resistance Is Futile for the original BorgAttack.py which I patched to support GC and no GC without issue.
* WileyCoyote (michaelwileyart@gmail.com) for the Crossfield Phaser sounds (already mentioned of the Crossfield's separate readme).
* BCC Community for feedback.
* That Guy... Brian (ThatGuyBrian, trekker12@hotmail.com) - for Model Conversion of the original Protostar and Crossfield models (already mentioned on the Crossfield's separate readme), the Crossfield original HP (already mentioned on the Crossfield's separate readme), and for telling me to install Nifskope, that tool has proven to be very useful to me.
** Original Prodigy model extracted from Star Trek Prodigy: Supernova. https://drive.google.com/file/d/1BMaT2_i5KBIqZ5Am1Hr4vK-81yZQ9GsE/view
** Original Crossfield model (from the aforementioned https://www.gamefront.com/games/bridge-commander/file/crossfield-class) ported from Star Trek: Adversaries (https://store.steampowered.com/app/815040/Star_Trek_Adversaries/)
* Grey da Derg#2305 aka Greystar for Model Conversion of the High-End Protostar model and adjustments.
** High-end USS Protostar Model made by LoganRolphh on sketchfab, falls under Creative Commons - Attribution https://sketchfab.com/3d-models/star-trek-prodigy-protostar-class-93efdd42825b410a88e77ed8e4119ff8
* Spore Drive sprites taken from Star Trek Discovery images uploaded to Memory Alpha wiki (https://memory-alpha.fandom.com/wiki/File:JahSepp.jpg, https://memory-alpha.fandom.com/wiki/File:Mycelial_network.jpg) and then modified to suit BC and add transparency.
* Mass Effect FTL sounds and Mass Accelerator sounds from ME3 final space battle, taken from Gamer's Little Playground's channel https://www.youtube.com/watch?v=iEoBsKALnxE
* Thanix cannon sounds: from N7Reinas's channel https://www.youtube.com/watch?v=hByyA01r0dA recording of ME2
* Original Electric Explosion effect, modified for the Eezo field, taken from VonFrank's work in BC:Remastered.
* Original Spore Drive Effect, modified for the Spore Drive, is a modified version of the Electric Explosion Effect mentioned above, combined with Mycelial Network images taken from ST:Discovery.
* Grey da Derg#2305 aka Greystar, and 𝕟𝕒𝕣𝕣𝕠𝕨𝕔𝕨𝕪𝕗𝕖 aka Hexagonal_Nexul for the original Hardpointing/Sounds/Scripting from BC Remastered Orion (from which the Protostar ship was taken from) and an updated version.
* Original ST:Discovery torpedoes by Zambie Zan, alexandre.marques@gmail.com (already mentioned on the Crossfield's separate readme).
* Everyone else from the other mods I mentioned, which have their own readmes crediting them - please feel free to contact me (tardis#2540 on Discord, CharaToLoki on Gamefront) to correct any potential issues, thank you.
* Michael Giachinno for the ST Prodigy Intro music.
* Bonnie Gordon for the Protostar computer voice.
* Tools used: Milkshape 3D and FreeCAD for extensive modifications and adjustments to the original Andromeda Model, Nifskope to validate the textures, GIMP to modify and create textures and icons, Model Property Editor to iron.out a few hardpoint issues, Audacity to fix some sounds.
* Grey da Derg#2305, Grim455#4905 aka THE SCI-FI KING, HexagonalNexul and MSR1701 for helping with noticing bugs and their cause, and for being inquisitive and finding out possible ways to tweak the hardpoints and techs and models.
* Alex SL Gato (aka CharaToLoki) for any new code or model implemented, fixed or modified (including all the monkey patches and the icon), plus the original fusion idea I had, based on a Spore Andromeda-Talyn fusion (image provided on Documentation/AndromedaTalynOriginalSporeIdea.png), and the Spear model.

Fulfilling both the SDK and LGPL licenses:
THIS MOD IS NOT SUPPORTED BY ACTIVISION

This mod falls under the GNU LESSER GENERAL PUBLIC LICENSE Version 3, 29 June 2007, both from any derivative or original work done to the mod. Everyone is permitted to copy and distribute verbatim copies of this mod. As per the LPGL license, everything in this mod is open for everybody to use, read and modify. Just do not forget to credit everyone involved and follow the LGPL license so derivatives of this code remain LGPL.

PointDefence.py (apparently under BSD license so despite the things I make have NO merchantibility and this mod MUST NOT be sold, only freely given and shared, I need to copy this line down here): 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Fulfilling USS Sovereign's conditions:

All sections based on USS Sovereign's Slipstream module fall under All Rights Reserved. Do not modify or repackage those sections of the mod without extreme permission from the authors:
---- USS Sovereign condition: that this mod is intended to be released for KM and not for REP, RE nor REM-related mods.
---- Alex SL Gato condition: does not mind as long as USS Sovereign and he are being credited and both Mario and himself's conditions are covered.

Those sections are left clear with two text banners, from "BEGINNING OF USS SOVEREIGN'S LIMITED PERMISSION AREA" to "END OF USS SOVEREIGN'S LIMITED PERMISSION AREA", to ensure people do not accidentally copy those sections.

Fulfilling the BorgAttack conditions as best as possible (the following goes for BasicAttack and BorgAttack only):

*NOTE* This AI can replace the current Borg AI found in use in KM1.0

The python files included have been created by jayce and some assistance from Defiant with the exception of the BasicAttack AI.
The original author or modifier of this file is unknown for me (jayce) to give the proper credits. Aparently, it is necessary in order to use the BorgAttack AI in Quickbattle. It was obtain undoubtedly in one of the very many downloads of Borg vessels that I (jayce) have acquired over the the years, with most new downloads replacing the older one. The BasicAttack.py AI file was not altered in any way, so if the author sees their handywork, please contact me and claim it.

If you distribute this AI with another mod, make every attempt to list this AI version clearly in your readme file so that people can know that it's safe to override if they want to. If you distribute this AI with another mod, it must contain the entire AI and not just parts of it. Meaning if you distribute the Borg AI, it needs to contain both the BorgAttack.pyc and the BasicAttack.py together with the mod. I absolutely do not want to see any BorgAttack.py files from this AI distributed with any other mods. Period. The last thing I want to hear is how someone's AI is not working right because of an altered (.py) file. There is a reason why this AI is being released in (.pyc) form.


== Bugs ==
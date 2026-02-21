== Changelog ==
1.2.22 - Fixing:
   * Updated Gravitic Lance to 1.55, making the code cleaner and slightly better at handling exceptions
1.2.21 - Fixing:
   * Updated AdvArmourTechThree to 1.9, cleaned code a bit and fixed potential issue with lights.
1.2.20 - Fixing:
   * Updated Enterprise J files to avoid accidentally overwriting WC's EnterpriseJ
1.2.19 - Fixing:
   * Updated AdvArmourTechThree from 1.84 to 1.85, fixed conflict with DS9FX sometimes resetting visible damage.
1.2.18 - Fixing:
   * Updated FIX-AblativeArmour1dot0 Autoload script to 0.41 to provide better armour inheritance.
1.2.17 - Fixing:
   * Updated FIX-DS9FXbelow1dot2 to be a bit more agnostic towards the actual value of SpeciesToTorp.PHASEDPLASMA
1.2.16 - Fixing:
   * Updated SimulatedPointDefence to 1.0 to allow cleaner logic and cleanup.
1.2.15 - Fixing:
   * Updated AdvArmourTechThree from 1.83 to 1.84, fixed weird button bug.
1.2.14 - Fixing:
   * Updated AdvArmourTechThree from 1.82 to 1.83, fixed weird self-destruct bug.
1.2.13 - Fixing:
   * Removed code that was not being used.
1.2.12 - Fixing:
   * Updated Gravitic Lance to 1.52 to be more robust.
1.2.11 - Fixing:
   * Updated Tachyon Beam to 1.4 to be more robust.
1.2.10 - Fixing:
   * Updated hull gauge fix unrelated to this mod to be more robust.
1.2.9 - Fixing:
   * Updated Tachyon Beam tech to fix a small error.
1.2.8 - Fixing:
   * Updated the FIX-AblativeArmour1dot0 Autoload script to provide full starbase repair functionality and better armour inheritance.
1.2.7 - Fixing:
   * Fixed unrelated health gauge no-swap bug.
1.2.6 - Fixing:
   * Updated SimulatedPointDefence to prevent some MissionLib configs from preventing a proper cleanup.
1.2.5 - Fixing:
   * Updated AutomaticDestroyedSystemRepairDummy so the dummy name does not trigger some defence scripts.
1.2.4 - Bug fixing:
   * Updated GraviticLance to 1.51, fixing a typo.
1.2.3 - Bug fixing:
   * Updated GraviticLance to 1.5, fixing a typo.
1.2.2 - Bug fixing:
   * Updated AdvArmortechThree to 1.82 fix a possible missing button issue.
1.2.1 - Bug fixing:
   * Updated AdvArmortechThree to 1.81 to make it check things a bit better.
1.2.0 - Bug fixing:
   * Updated Gravitic Lance to 1.4 to correct a small issue with a timer.
1.1.9 - Bug fixing:
   * Updated Gravitic Lance to 1.3 to correct a small issue with a sequence.
1.1.8 - Bug fixing:
   * Updated Gravitic Lance to 1.2 to correct small issue with a sequence.
1.1.7 - Bug fixing:
   * Updated FIX-AblativeArmour1dot0.py to correct typo in 0.2.
1.1.6 - Bug fixing:
   * Updated FIX-AblativeArmour1dot0.py to 0.2 to fix a notable issue the original Ablative Armour had regarding singletons making the armour shared between the same ship type.
1.1.5 - Bug fixing:
   * Updated FIX-AblativeArmour1dot0.py to fix a small typo that currenctly did not affect any script, but could in the far future.
1.1.4 - Misc. changes:
   * Updated Simulated Point Defence from 0.91 to 0.92 - this will not make the ship target projectiles that have same parent and target ID (update for compatibility with the SG Drone weaponry from CanonicalAlteranTechnologies).
1.1.3 - Potential bug fixing
 * Updated AdvArmourTechThree from 1.7 to 1.8, 1.8 is a tiny bit slower but it is far better for some KM installs where for some reason 1.7 might crash. If 1.7 did not crash for you, use the 1.7 script from previous versions instead.
1.1.2 - Bug fixing
 * Upgraded AdvArmorTechThree to 1.7, eliminating the dark-glow issue.
1.1.0 to 1.1.1 - Bug fixing
 * Upgraded Simulated Point Defence from 0.91 to 0.92, reducing ship collision issues.
1.0.6 to 1.0.9 - Bug fixing
 * Refined armour even more and fixed a same-name potential issue
 * Refined Simulated Point Defense to avoid editing a singleton.
1.0.5 - Bug Fixing
 * Energy armour had a bug in an outlier condition, now it has been tackled. Thanks Grey for noticing it out!
1.0.4 - Bug Fixing
 * Upgraded Simulated Point Defence from 0.8 to 0.9, now two possible crash causes upon heavy fire have been removed. Thank USS Sovereign for telling me how to use the debug function properly.
1.0.3 - Bug Fixing
 * Upgraded Simulated Point Defence from 0.6 to 0.8, now a lot of the weird behaviour happening before has been fixed.
1.0.2 - Bug fixing
 * Fixed Simulated Point Defence TypeError sequence issue - it didn't really cause any problems but it was flagged on the console and would have caused problems if the sequence had multiple actions.
1.0.1 - Another balance update
 * Severely nerfed the shields and armour.
1.0 - Official Mod Release
 * Fix on Gravitic Lance
0.9 - Small refinement of the Simulated Point Defence script.
0.8 - Model and script fixes and balancing:
 * Blinker effects added via diffusion, we are still investigating what makes the Animations via NifSkope crash using CGSovereign model as a base, something related with TriShape and re-ordering indexes, albeit that doesn't seem to be the cause?
 * Tweaks to bussard_glow.tga to make it redder and more glowy.
 * Tweaks to deflector_glow to make it a bit more lavender.
 * Tweaks to forehull_glow to be more regular.
 * Added fix for AblativeArmour eroding itself with time due to not repairing at all.
 * Nerfed shields even further.
 * Buffed Gravitic Lance again.
 * Adjusted Siphoon effect to properly adjust to distance.
 * Added Playerside PointDefense with the Enterprise J included, RepairSystems and Redistribute shields.
0.7 - More balancing
 * Reduced adv armour battery strength.
 * Placed shuttle 2D position on its correct place.
 * Nerfed impulse speed and rotation speed and acceleration again.
 * Nerfed a bit Multivectral and Regenerative shielding chances and regeneration once again, as well as reflux weapon defense drain.
 * Removed Quad torpedo fire from this ship.
 - Still awaiting for finding Nifskope 0.9.8 to add nif-side blinkers. Experiments with tweaking nifskope 1.0.2 manage to create a decent animation and do not crash the game directly, but would still cause the game to take forever to load.
 - Asking for feedback regarding all of the above, including if the project should have nanoFX beta blinkers again or forego any blinkers.
0.6.1 - Code cleanup and extra balancing
 * Removed the misaligned shift-space on the hardpoint, found by THE SCI-FI KING, they were not causing any problems but they may make an interpreter mad.
 * Reduced max angular acceleration and speed once more 
0.6 - Balancing:
 * Nerfed shield strength
 * Nerfed Adv Energy Armour strength
 * Buffed Gravitic Lance hardpoint damaging power.
 * Removed Fed Ablative Armour due to creating a synergy with the other armours that made the ship invincible to everything except a ship colliding with it
 * Reduced max angular acceleration to avoid Breakdancing AI capable of doing the most crazy maneuvers
 * Buffed AOE Draining range for the Enterprise J and made it negative (now it powers up allies and herself, instead of draining enemy power in the area)
    - Awaiting for finding Nifskope 0.9.8 to add nif-side blinkers.
    - first unofficial release of the whole mod.
0.5 - Added Gravitic Lance to the Enterprise J - sounds thanks to Grey da Derg#2305
0.4 - Included Gravitic Lance and Tachyon Beam techs
0.3 - Added monkey patch for TractorBeams.py small error
0.2 - Added feedback - removed nanofx blinkers and glows
0.1 - first unofficial showcase of this mod, for feedback

== What does this mod do ==
This mod includes an improved Enterprise J model and icon, closer to the canon deal, plus a reinforced Hardpoint and its additional technologies, including a gravitic lance - with the exception of Slipstream.
It also includes some technology fixes to Power Drain Beam and Tractor Inversion so they can actually draw power, and a fix to AblativeArmour.py by the Foundation Technologies Team so the armour can repair like a normal subsystem; by Alex SL Gato.
If you want to fuse those monkey patches with the original file, feel free to do so, I only do the monkey patch to avoid versioning problems.

Additionally, the Milkshape 3D file for this model, as well as a diffused version with duller blinkers are located under two .zip in data/Models/Ships/EnterpriseJ/ if you want to change it yourself.

== Dependancies ==
All of these must be installed before installing this mod, in this order:
* Foundation + Kobayashi Maru (KM has Foundation already installed - the most recent version of KM, the better).
* Slipstream mod (not wholly necessary but the Enterprise J hardpoint supports slipstream).
* UNLIKE THE ORIGINAL, NanoFX is not immediately required, as I removed the blinkers.
* Tachyon Beam Technology >=1.1.5 https://www.gamefront.com/games/bridge-commander/file/tachyon-beam-customizable-tech
** 1.1.5 is already installed with this pack
** DO NOT USE LESSER VERSIONS UNLESS YOU WANT THE SHIP TO AUTOMATICALLY HAVE ALL PHASERS AS TACHYON BEAMS

== Credits ==
* Everyone involved in Foundation - without you this would have been a real pain to do (please read the separate Foundation.txt license) - Banbury, Dasher42, DigitalFriend, MLeo, Nanobyte and Sleight42, among others.
* Everyone involved in KM - specifically those involved in the creation of armour and Shields.py (FoundationTechnologies) the AdvArmorTech.py, FiveSecsGodPhaser.py, TractorBeams.py - Apollo from ATP Technologies as well.
* Dasher42 for reminding me of licensing.
* USS Sovereign for some DS9FX advice regarding timers - a LOT of tips for Alex SL Gato's DampeningAOEDefensiveField.py
* USS Sovereign and Elijah both for teaching me and helping me with the use of the tools.
* Defiant for the original PointDefence.py, which got altered later somewhere.
* LJ for inspiration to see friendly, enemy and neutral ships
* fekleyrtarg for telling me that decimation exists in Blender... albeit I ended up using FreeCad decimation instead lol.
* That Guy... Brian for telling me to install Nifskope, it has proven to be very useful to me.
* Tools used: Blender for importing the original model to Milkshape, Milkshape 3D and FreeCAD for extensive modifications and adjustments so it can run on STBC and it's the real Enterprise J and not some hybrid, Nifskope to validate the textures.
** Original Enterprise J Repaired file by chichirod on Thingiverse: https://www.thingiverse.com/thing:2792212 licensed under cc-sa (there is an extra readme on Documentation for this one, very short, CharaToLokisEnterpriseJModOriginalJModelSTLusedLICENSE.txt).
** WileyCoyote for some of the textures (specifically those regarding his Enterprise J mod https://www.gamefront.com/games/bridge-commander/file/enterprise-j-1) - their Readme has been included as well - EnterpriseJ README.txt
** Elijah for allowing a diffusing trick to allow blinkers to partially work without the proper nifskope (0.9.8)
* Grey da Derg#2305 for the gravitic lance sounds.
* 𝕟𝕒𝕣𝕣𝕠𝕨𝕔𝕨𝕪𝕗𝕖 aka Hexagonal_Nexul for the transphasic torpedo sounds and .tga; as well as for the InfinityModulator_a and InfinityModulator_b phaser sounds (which are according to Haxagonal_Nexul a strong remix and mesh of Trek Sounds').
* Grey da Derg#2305, Grim455#4905 aka THE SCI-FI KING, HexagonalNexul and MSR1701 for helping with noticing bugs and their cause, and for being inquisitive and finding out possible ways to tweak the hardpoints and techs and models.
* Alex SL Gato (aka CharaToLoki) for any new code or model implemented or modified (including all the monkey patches), plus the coiledTwistBeam1.tga texture and the icon.

Fulfilling both the SDK and LGPL licenses:
THIS MOD IS NOT SUPPORTED BY ACTIVISION

This mod falls under the GNU LESSER GENERAL PUBLIC LICENSE Version 3, 29 June 2007, both from any derivative or original work done to the mod. Everyone is permitted to copy and distribute verbatim copies of this mod. As per the LPGL license, everything in this mod is open for everybody to use, read and modify. Just do not forget to credit everyone involved and follow the LGPL license so derivatives of this code remain LGPL.

PointDefence.py (apparently under BSD license so despite the things I make have NO merchantibility and this mod MUST NOT be sold, only freely given and shared, I need to copy this line down here): 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

== Bugs ==
* Enterprise J damage is a bit wonky, nothing that causes the model to crash or performance issues or anything but aesthethically the model itself may look like it was peeled off if it takes too much damage.
* No other bugs noticed, but if you notice them, please feel free to share and report them.
== Changelog ==
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

Additionally, the Milkshape 3D file for this model is located under a .zip in data/Models/Ships/EnterpriseJ/ if you want to change it yourself.

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
* LJ for inspiration to see friendly, enemy and neutral ships
* fekleyrtarg for telling me that decimation exists in Blender... albeit I ended up using FreeCad decimation instead lol.
* That Guy... Brian for telling me to install Nifskope, it has proven to be very useful to me.
* Tools used: Blender for importing the original model to Milkshape, Milkshape 3D and FreeCAD for extensive modifications and adjustments so it can run on STBC and it's the real Enterprise J and not some hybrid, Nifskope to validate the textures.
** Original Enterprise J Repaired file by chichirod on Thingiverse: https://www.thingiverse.com/thing:2792212 licensed under cc-sa (there is an extra readme on Documentation for this one, very short, CharaToLokisEnterpriseJModOriginalJModelSTLusedLICENSE.txt).
** WileyCoyote for some of the textures (specifically those regarding his Enterprise J mod https://www.gamefront.com/games/bridge-commander/file/enterprise-j-1) - their Readme has been included as well - EnterpriseJ README.txt
* Grey da Derg#2305 for the gravitic lance sounds.
* Grey da Derg#2305, Grim455#4905 aka THE SCI-FI KING, HexagonalNexul and MSR1701 for helping with noticing bugs and their cause, and for being inquisitive and finding out possible ways to tweak the hardpoints and techs and models.
* Alex SL Gato (aka CharaToLoki) for any new code or model implemented or modified, plus the coiledTwistBeam1.tga texture, the icon.

Fulfilling both the SDK and LGPL licenses:
THIS MOD IS NOT SUPPORTED BY ACTIVISION

This mod falls under the GNU LESSER GENERAL PUBLIC LICENSE Version 3, 29 June 2007, both from any derivative or original work done to the mod. Everyone is permitted to copy and distribute verbatim copies of this mod. As per the LPGL license, everything in this mod is open for everybody to use, read and modify. Just do not forget to credit everyone involved and follow the LGPL license so derivatives of this code remain LGPL.

Also for those 
== Bugs ==
* Enterprise J damage is a bit wonky, nothing that causes the model to crash or performance issues or anything but aesthethically the model itself may look like it was peeled off if it takes too much damage.
* No other bugs noticed, but if you notice them, please feel free to share and report them.
== Changelog ==
1.4.1 - Small name expansion
1.4 - Small bugfix
1.3 - Small bugfix
1.2 - Small bugfix
1.1.5 - Small bugfix
1.1 - NEW UPDATE - Immunities can be added now within scripts/Custom/Ships/ship file!
1.0 Release of this mod

== What does this mod do ==
This mod adds a far more customizable script, based on the "FiveSecsGodPhaser", called "Tachyon Beam", which instead of destroying a target's hull after 5 seconds of contact, it will drop a target's shields for X seconds after Y seconds of exposure to N beam - with X, Y and N being customizable on the scripts/Custom/Ships ship field.

# Usage Example:  Add this to the dTechs attribute of your ShipDef, in the Ship plugin file
# but modify the values accordingly to what you want, and for actual values since the following is just a general example
# Time: seconds needed for the tachyon beam to drop the shields must be above 0. 5 by default
# TimeEffect: how many seconsd do the shields remain dropped. Must be above 0. 5 by default
# Beams: this field indicates which beams on your ship have tachyon beam properties. Don't add the field or leave it empty to consider all phasers tachyon beams
# Immune: NEW!!! Finally found how to add the immunity to another side of the party! Immune makes this ship immune to its effects. Set it to greater or lesser than 0 to be immune! negatives also make it immune without the weapon, while 1 keeps it active
"""
Foundation.ShipDef.Sovereign.dTechs = {
	"TachyonBeam": { "Time": 5.0, "TimeEffect": 5.0, "Beams": ["PhaserNsme1", "PhaserName2", "PhaserName3", "PhaserName4"], "Immune": 1}
}
"""
# As for immunities, there is another way, elgacy from 1.0 and before, directly through the Custom script, so you'll have to add these at the end of the scripts/ships script:
"""
def IsTachyonImmune():
	return 1
"""

For more details, read the licenses and readmes inside each file - I've done it that way so people can still use them if they separate, you must include it properly.

== Dependancies ==
All of these must be installed before installing this mod, in this order:
* Foundation + Kobayashi Maru (has Foundation already installed - the most recent version of KM, the better).

== Credits ==
* Everyone involved in Foundation - without you this would have been a real pain to do (please read the separate Foundation.txt license) - Banbury, Dasher42, DigitalFriend, MLeo, Nanobyte and Sleight42, among others.
** Specifically, those among FoundationTechnologies who made the Tachyon Projectile.py and the FedAblativeArmour.py (probably MLeo, Dasher42, Defiant, Apollo and Dolphi)
* Everyone involved in KM - specifically those involved in the creation of armour and Shields.py (FoundationTechnologies) and the AdvArmorTech.py - Apollo from ATP Technologies as well.
* USS Frontier for the original 5SecsGodPhaser technology.
* Grey da Derg#2305 for helping with noticing bugs and their cause.
* Grim455#4905 aka THE SCI-FI KING, for beign inquisitive and finding out possible ways to tweak the hardpoints and techs.
* Alex SL Gato (aka CharaToLoki) for any new code implemented or modified - specifically the amalgamation that is Tachyon Beam; and for making this Documentation.
* travisa. for suggesting this tech

Fulfilling both the SDK and LGPL licenses:
THIS MOD IS NOT SUPPORTED BY ACTIVISION

This mod falls under the GNU LESSER GENERAL PUBLIC LICENSE Version 3, 29 June 2007, both from any derivative or original work done to the mod. Everyone is permitted to copy and distribute verbatim copies of this mod. As per the LPGL license, everything in this mod is open for everybody to use, read and modify. Just do not forget to credit everyone involved and follow the LGPL license so derivatives of this code remain LGPL.


== Bugs ==
* No bugs noticed, but if you notice them, please feel free to share and report them
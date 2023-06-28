== Changelog ==
0.4 - first unofficial release of this mod, for feedback

== What does this mod do ==
Upon seeing the Lower Decks episode where the Cerritos is hit by a Breen Drainer weapon, and only loses some systems, Alex SL Gato made a post in Memory Alpha regarding what two options could have happened https://memory-alpha.fandom.com/f/p/4400000000003747353/
Option A: The Cerritos did not have a full Breen Drainer immunity, more of a resistance for some systems.
Option B: The constant arms race made the Breen Develop an upgraded Breen Drainer which, while did not work fully against already shielded vessels, still depowered impulse and warp engines, and drained the shields. 

This mod includes BOTH options to STBC, plus an upgraded Breen Drainer weapon.

You can include option B in any torpedo or pulse by adding these lines at the end of the projectile file (between the """ and """):

"""
try:
	sYieldName = 'Upgraded Breen Drainer Weapon'
	sFireName = None

	import FoundationTech
	import Custom.Techs.UpgradedBreenDrainer

	oFire = Custom.Techs.UpgradedBreenDrainer.oUpgradedDrainerWeapon
	FoundationTech.dOnFires[__name__] = oFire

	oYield = FoundationTech.oTechs[sYieldName]
	FoundationTech.dYields[__name__] = oYield
except:
	print "Upgraded Breen Drainer Weapon not installed, or missing FoundationTech"
"""
# You can also add your ship to an immunity list, in order to keep the files unaltered... just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"Upgraded Breen Drainer Immune": 1
}
"""
# You can also add your ship to a normal breen drainer resistance list (Option A), in order to keep the files unaltered... just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"Breen Drainer Resistance": 1
}
"""

For more details, read the licenses and readmes inside each file - I've done it that way so people can still use them if they separate, plus the addition is not automatic to the techs - you must include it properly.

== Dependancies ==
All of these must be installed before installing this mod, in this order:
* Foundation + Kobayashi Maru (KM has Foundation already installed - the most recent version of KM, the better).

== Credits ==
* Everyone involved in Foundation - without you this would have been a real pain to do (please read the separate Foundation.txt license) - Banbury, Dasher42, DigitalFriend, MLeo, Nanobyte and Sleight42, among others
* Everyone involved in KM - specifically those involved in the creation of armour and Shields.py (FoundationTechnologies) and the AdvArmorTech.py - Apollo from ATP Technologies as well.
* Dasher42 for some of the little code I could really throw an author to (specially the BreenDrain.py part about oFire and oYield, and probably the similar information in the manual).
* Erik Novales for the original QuantumTorpedo.py which got modified into the original BreenDrain.py
* Grey da Derg#2305 for helping with noticing bugs and their cause.
* Grim455#4905 aka THE SCI-FI KING, for beign inquisitive and finding out possible ways to tweak the hardpoints and techs.
* Everyone on this post for their feedback before the 28th of June 2023: https://memory-alpha.fandom.com/f/p/4400000000003747353/
* Alex SL Gato (aka CharaToLoki) for any new code implemented or modified.

Fulfilling both the SDK and LGPL licenses:
THIS MOD IS NOT SUPPORTED BY ACTIVISION

This mod falls under the GNU LESSER GENERAL PUBLIC LICENSE Version 3, 29 June 2007, both from any derivative or original work done to the mod. Everyone is permitted to copy and distribute verbatim copies of this mod. As per the LPGL license, everything in this mod is open for everybody to use, read and modify. Just do not forget to credit everyone involved and follow the LGPL license so derivatives of this code remain LGPL.


== Bugs ==
* No bugs noticed, but if you notice them, please feel free to share and report them
Modifications made by Alex SL Gato

Special Thanks to 𝕟𝕒𝕣𝕣𝕠𝕨𝕔𝕨𝕪𝕗𝕖#0007 for driving me to complete this mod for their Voyager-J mod, as well as for some help with the PhasedTorp scripts.

===Changelog===
1.0 - Mod release

===What does this mod do===
Ever wondered why Phased Torpedoes weren't working on your Kobayashi Maru? A conflicting mod related with no damage through shields made it so unless your shields were below 20% or down no additional stat or visible damage 
really happened. Even when you removed that from your Bridge Comamnder the Phased Torpedoes were a bit buggy and sometimes moved outside had This not only happened with this technology but when firing from inside the enemies' shield, 
so I decided to fix that, at least partially.

With the fixed files, now phased torpedoes can actually do its work and will not start bugging themselves.

The only steps you need to do after isntalling the files on this mod are:
* Set your torpedo type to PhasedPlasma, this will allow the torpedo to damage even from the inside once the hull or target subsystem is hit
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

* Include these lines at the end of your torpedo file, which allow the torpedo to "get through" the shield:

try:
	modPhasedTorp = __import__("Custom.Techs.PhasedTorp")
	if(modPhasedTorp):
		modPhasedTorp.oPhasedTorp.AddTorpedo(__name__)
except:
	print "Phased Torpedo script not installed, or you are missing Foundation Tech"


Additionally, I added one of my "failed" experiments with this, it ended up being some torpedo that phased through the ship and damaged the hull or desired subsystem in the process and then the torpedo had a very high chance 
of not dying, which with some tweaks could be used to come back and try to hurt the objective again. Sounds familiar? Yes, Stargate Ancient Weaponry. The mod will overwrite your current drone compliment to this nasty variant,
drones deal a third of the damage now but for the most part will attack relentlessly a ship until they are shot down, their target dies or the enemy ship is lucky and the drone hits in a wrong way and dies.

===Requirements===
FoundationTechnologies and DS9FX, having the latest version of Kobayashi Maru would be ideal.
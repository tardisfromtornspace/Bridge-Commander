Modifications made by Alex SL Gato

Special Thanks to 𝕟𝕒𝕣𝕣𝕠𝕨𝕔𝕨𝕪𝕗𝕖#0007 for driving me to complete this mod for their Voyager-J mod, as well as for some help with the PhasedTorp scripts.

===Changelog===
1.2.3 - Notable bug fix with Hopping Torpedo crashing if the ship who fired it died - thanks Grey for pointing it out!
1.2.2 - Small bug fix with Hopping Torpedo - now Drones should work normally on unshielded vessels
1.2.1 - Small bug fix with the Advanced Energy Armour 1.0
1.2 - EXTRA TECHNOLOGIES: Chroniton Torpedo, Reflux Torpedo, Tricobalt Torpedo, Advanced Energy Armour 1.0.
      BUG FIXES: Compatibility issues fix, done a "Monkey Patch" so those with DS9FX 1.1 don't crash if they download this mod. On DS9FX 1.2 I talked with Mario and the fix is planned to be there right now. For BC: rematered don't forget to manually overwrite the Stock function with this one.
1.1 - Small fix
1.0 - Mod release

===What does this mod do===
Ever wondered why Phased Torpedoes weren't working on your Kobayashi Maru? A conflicting mod related with no damage through shields made it so unless your shields were below 20% or down no additional stat or visible damage 
really happened. Even when you removed that from your Bridge Comamnder the Phased Torpedoes were a bit buggy and sometimes moved outside. This not only happened with this technology but when firing from inside the enemies' shield, 
so I decided to fix that, at least partially.

With the fixed files, now phased torpedoes can actually do its work and will not start bugging themselves.

The only steps you need to do after isntalling the files on this mod are:
* Set your torpedo type to PhasedPlasma, this will allow the torpedo to damage even from the inside once the hull or target subsystem is hit
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

* Include these lines at the end of your torpedo file, which allow the torpedo to "get through" the shield:
-----------------
try:
	modPhasedTorp = __import__("Custom.Techs.PhasedTorp")
	if(modPhasedTorp):
		modPhasedTorp.oPhasedTorp.AddTorpedo(__name__)
except:
	print "Phased Torpedo script not installed, or you are missing Foundation Tech"
------------------
* You can also add your ship to an immunity list, not only the one below, in order to keep the files unaltered... just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev
------------------
Foundation.ShipDef.Ambassador.dTechs = {
	"Phased Torpedo Immune": 1
}
------------------

Additionally, I added multiple technologies of a similar concept and use, including Transphasic Torpedo, Tricobalt Torpedo (which actually works the other way around) and one of my "failed" experiments with this, which ended up being some
torpedo that phased through the ship and damaged the hull or desired subsystem in the process and then the torpedo had a very high chance of not dying, which with some tweaks could be used to come back and try to hurt the objective
again. Sounds familiar? Yes, Stargate Ancient Weaponry. The mod will overwrite your current drone compliment to this nasty variant, drones deal a third of the damage now but for the most part will attack relentlessly a ship until 
they are shot down, their target dies or the enemy ship is lucky and the drone hits in a wrong way and dies.

Lastly, I present you the latest type of armor that will be the next revolution on armor defense: the energy ablative armor. While this mod existed before, it was limited to the Player and needed to be toggleable via the Tactical window.
This version allows any ship with the proper technology to use it and even change visible armour. Once active, the ship will stop receiving damage, all damage is redirected as an energy loss until the energy depletes.

Sample Setup:
------------------
# In scripts/Custom/ships/yourShip.py
# NOTE: replace "AMVoyager" with your abbrev
Foundation.ShipDef.AMVoyager.dTechs = {
	'Adv Armor Tech': 1
}
------------------
# In scripts/ships/yourShip.py

def GetArmorRatio(): # Strength of the armor, in a way
      return 2.5

def GetDamageStrMod(): # visual damage strength
	return 0

def GetDamageRadMod(): # visual damage radius
	return 0

def GetForcedArmor(): # If everyone is forced to wear it once it loads
	return 1

def GetArmouredModel(): # OPTIONAL: Select another scripts/ships/yourShip2.py with a adifferent model so when you are armored you change to this
	return "DiamondsArmorVoyager"

def GetOriginalShipModel(): # Should be the same script scripts/ships/yourShip2.py, but for more flexibility, here you can change it to never return when the armor drops
	return "DiamondsAMVoyager"
------------------
------------------
# In scripts/ships/Hardpopints/yourShip.py
# Add armored hull property, optional if you added GetArmorRatio above
#################################################
ArmourGenerator = App.HullProperty_Create("Armored Hull")

ArmourGenerator.SetMaxCondition(295000.000000)
ArmourGenerator.SetCritical(0)
ArmourGenerator.SetTargetable(1)
ArmourGenerator.SetPrimary(0)
ArmourGenerator.SetPosition(0.000000, 0.000000, 0.000000)
ArmourGenerator.SetPosition2D(0.000000, 0.000000)
ArmourGenerator.SetRepairComplexity(1.000000)
ArmourGenerator.SetDisabledPercentage(0.500000)
ArmourGenerator.SetRadius(0.250000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ArmourGenerator)

# on the Property load function.
	prop = App.g_kModelPropertyManager.FindByName("Armored Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
------------------

===Requirements===
FoundationTechnologies and DS9FX, having the latest version of Kobayashi Maru would be ideal.
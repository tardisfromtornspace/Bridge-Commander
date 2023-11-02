This mod was changed by narrowcwyfe and Alex SL Gato.

===Changelog===
0.9.7 - After the armour fixes, the bleedthrough is noticeably reduced, meaning that the ArmouredVoyager does not require such fast-regenerating shields. So those have been adjusted to a more regular shield.
0.9.3 - Removed some techs the ship does not use, plus a weird armour bug - thanks for Grey for noticing.
0.9.2 - Removed additional, unnecessary TimeVortex.py Tech script that was causing problems - thanks THE SCI-FI King for that
0.9.1 - By Dasher42's request, added the Foundation and SDK License
0.9 - Early beta release.
* Please notice we've decided to release this mod early so RetroBadger can see it before their own releases.
** Known issues **:
- Activating the plating with the Plating button instead of the Mvam may leave your ship in the dark for a few seconds. Visual bug, does not affect gameplay.
- There's a missing glow in one model. Visual bug, does not affect gameplay.

===What does this mod do===
This mod uses the high-texture, high quality armored voyager model and the SC4 shuttle and rehardpoints the ship.

The most noticeable changes are the addition of improved armour and fixing the transphasic torpedoes technology to work with the latest versions of Kobayashi Maru. Some changes were done on the model to add plating of higher quality. Everything else was kept original.

Additionally, it includes the extra technologies mod, in where the issues are fixed, so you don't have to do two installs for the needed technologies, and you can use the two main techs on this mod as well.

For transphasic torpedoes:
* Set your torpedo type to PhasedPlasma, this will allow the torpedo to damage even from the inside once the hull or target subsystem is hit
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

* Include these lines at the end of your torpedo file, which allow the torpedo to "get through" the shield:
-----------------
try:
	modTransphasicTorp = __import__("Custom.Techs.TransphasicTorp")
	if(modTransphasicTorp):
		modTransphasicTorp.oTransphasicTorp.AddTorpedo(__name__)
except:
	print "Transphasic Torpedo script not installed, or you are missing Foundation Tech"
------------------
* You can also add your ship to an immunity list, not only the one below, in order to keep the files unaltered... just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev
------------------
Foundation.ShipDef.Ambassador.dTechs = {
	"Transphasic Torpedo Immune": 1
}
------------------

Advanced energy ablative armor. While this mod existed before, it was limited to the Player and needed to be toggleable via the Tactical window.
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

===Credits===
- the original modders (read the adjount readme).
- narrowcwyfe, for getting the new mod into shape and fixing some issues, enuring the ship was not too powerful, and including new transphasic torpedo textures
- A fellow modder named "Tardis": for creating, fixing and applying the transphasic torpedo technology, improving and fixing the energy ablative armour tech, and ensuring the ship was not too weak against stock KM foes.
- CGI for some parts of the model - the original one looked too skinny!
- KCS for some work on model glows.
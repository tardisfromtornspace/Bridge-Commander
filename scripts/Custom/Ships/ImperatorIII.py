import Foundation
import App
# Usually you need only edit these seven lines

abbrev = 'ImperatorIII'
iconName = 'ImperatorIII'
longName = 'Imperator Mk III'
shipFile = 'ImperatorIII' 
menuGroup = 'Star Wars Fleet'
playerMenuGroup = 'Star Wars Fleet'
species = App.SPECIES_GALAXY
SubMenu = "Galactic Empire"

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.

credits = {
	'modName': 'ImperatorIII',   # The full name of your mod if applicable
	'author': 'DARKDRONE',              # Your name here
	'version': '1.0',                     # No more than one period please!
	                                      # I'd like to be able to do a numeric comparison.
	'sources': [ 'http://' ],             # Source for this mod
	'comments': ''                        # General info
}

# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, Print a #
# in front of the first line and uncomment the line with FedShipDef.

Foundation.ShipDef.ImperatorII = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile,"SubMenu": SubMenu })

# Uncomment these if you have TGL
# Foundation.ShipDef.ImperatorII.hasTGLName = 1
# Foundation.ShipDef.ImperatorII.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
Foundation.ShipDef.ImperatorII.desc = 'Approximately one year after the Battle of Yavin, a new subclass of the Imperial Star Destroyer began appearing. It is not known exactly when the first Imperator II Star Destroyers entered service, because their construction was kept top secret. Needless to say, the Rebel Alliance fleet was stunned when they first encountered a Mark II. The original Imperial Star Destroyer was considered a masterpiece, but it was not without flaws. The Imperial Navy decided that heavier firepower was needed for planetary bombardment, and that 60 ion cannons were far more than were necessary. Therefore, the Imperator II design removed forty ion cannons and replaced them with heavy turbolasers. The hyperdrive was improved, giving the Mark II an impressive x1 hyperdrive. The particle shielding was also increased, probably in response to the destruction of the Death Star and the threat of Rebel torpedo attacks. The Mark IIs were rarities for a long time, but eventually all new Star Destroyers were of this class. Once Star Destroyer construction was restarted under Grand Admiral Thrawn, it is believed that only Mark IIs were built by the remaining Imperial shipyards. The Imperator II is able to hold its own against modern New Republic warships such as the MC90, and is still used by the Imperial Navy over 20 years after the Battle of Endor.'

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:           Foundation.ShipDef.ImperatorII.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.ImperatorII.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

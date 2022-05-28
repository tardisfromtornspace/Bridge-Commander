import Foundation
import App
# Usually you need only edit these seven lines

abbrev = 'venatorII'
iconName = 'venator'
longName = 'Venator Variant'
shipFile = 'venatorII' 
menuGroup = 'Star Wars Fleet'
playerMenuGroup = 'Star Wars Fleet'
SubMenu = "Old Republic"
species = App.SPECIES_GALAXY


# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.

credits = {
	'modName': 'venator',   # The full name of your mod if applicable
	'author': 'DARKDRONE',              # Your name here
	'version': '1.0',                     # No more than one period please!
	                                      # I'd like to be able to do a numeric comparison.
	'sources': [ 'http://' ],             # Source for this mod
	'comments': ''                        # General info
}

# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, Print a #
# in front of the first line and uncomment the line with FedShipDef.

Foundation.ShipDef.venatorII = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Uncomment these if you have TGL
# Foundation.ShipDef.venatorII.hasTGLName = 1
# Foundation.ShipDef.venatorII.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
Foundation.ShipDef.venatorII.desc = "This Venator-class Star Destroyer was one of the variants done during the final days of the clone wars, with an built-in beam weapon in the hanger as additional weaponry."

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:           Foundation.ShipDef.venatorII.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.venatorII.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

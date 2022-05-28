import Foundation
import App
# Usually you need only edit these seven lines

abbrev = 'Firebird'
iconName = 'Firebird'
longName = 'Firebird'
shipFile = 'Firebird' 
menuGroup = 'R3 ships Ships'
playerMenuGroup = 'R3 ships Ships'
species = App.SPECIES_SOVEREIGN


# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.

credits = {
	'modName': 'Firebird',   # The full name of your mod if applicable
	'author': 'DARKDRONE',              # Your name here
	'version': '1.0',                     # No more than one period please!
	                                      # I'd like to be able to do a numeric comparison.
	'sources': [ 'http://' ],             # Source for this mod
	'comments': ''                        # General info
}

# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, Print a #
# in front of the first line and uncomment the line with FedShipDef.

Foundation.ShipDef.Firebird = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

# Uncomment these if you have TGL
# Foundation.ShipDef.Firebird.hasTGLName = 1
# Foundation.ShipDef.Firebird.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
Foundation.ShipDef.Firebird.desc = 'No Description Available'

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:           Foundation.ShipDef.Firebird.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Firebird.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

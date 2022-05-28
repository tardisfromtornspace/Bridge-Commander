from bcdebug import debug
import Foundation
import App
# Usually you need only edit these seven lines

abbrev = 'Nova'
iconName = 'Nova'
longName = 'Nova'
shipFile = 'Nova' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
species = App.SPECIES_GALAXY


# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.

credits = {
	'modName': 'Nova Class',   # The full name of your mod if applicable
	'author': 'Durandal',              # Your name here
	'version': '1.0',                     # No more than one period please!
	                                      # I'd like to be able to do a numeric comparison.
	'sources': [ 'http://' ],             # Source for this mod
	'comments': ''                        # General info
}

# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, Print a #
# in front of the first line and uncomment the line with FedShipDef.

Foundation.ShipDef.Nova = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.Nova.sBridge = 'novabridge'

# Uncomment these if you have TGL

Foundation.ShipDef.Nova.hasTGLName = 1
Foundation.ShipDef.Nova.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.Nova.desc = 'No Description Available'

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:           Foundation.ShipDef.Nova.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Nova.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

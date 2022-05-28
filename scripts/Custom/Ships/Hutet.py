import Foundation
import App
# Usually you need only edit these seven lines

abbrev = 'Hutet'
iconName = 'Hutet'
longName = 'Hutet'
shipFile = 'Hutet' 
menuGroup = 'Card Ships'
playerMenuGroup = 'Card Ships'
species = App.SPECIES_GALAXY


# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.

credits = {
	'modName': 'Hutet',   # The full name of your mod if applicable
	'author': 'Morpheus aka Zorg',              # Your name here
	'version': '1.0',                     # No more than one period please!
	                                      # I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.zorgspace0001.com' ],             # Source for this mod
	'comments': ''                        # General info
}

# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, Print a #
# in front of the first line and uncomment the line with FedShipDef.

Foundation.ShipDef.Hutet = Foundation.CardShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

# Uncomment these if you have TGL

Foundation.ShipDef.Hutet.hasTGLName = 1
Foundation.ShipDef.Hutet.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.Hutet.desc = 'No Description Available'

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:           Foundation.ShipDef.Hutet.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Hutet.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

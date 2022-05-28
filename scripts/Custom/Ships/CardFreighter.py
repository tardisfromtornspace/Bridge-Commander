from bcdebug import debug
import Foundation
import App
# Usually you need only edit these seven lines

abbrev = 'CardFreighter'
iconName = 'CardFreighter'
longName = 'CardFreighter'
shipFile = 'CardFreighter' 
menuGroup = 'Card Ships'
playerMenuGroup = 'Card Ships'
species = App.SPECIES_GALAXY


# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.

credits = {
}

# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, Print a #
# in front of the first line and uncomment the line with FedShipDef.

Foundation.ShipDef.CardFreighter = Foundation.CardShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

# Uncomment these if you have TGL
Foundation.ShipDef.CardFreighter.hasTGLName = 1
Foundation.ShipDef.CardFreighter.hasTGLDesc = 1
Foundation.ShipDef.CardFreighter.fMaxWarp = 7.6

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.CardFreighter.desc = 'No Description Available'

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
#if menuGroup:           Foundation.ShipDef.CardFreighter.RegisterQBShipMenu(menuGroup)
#if playerMenuGroup:     Foundation.ShipDef.CardFreighter.RegisterQBPlayerShipMenu(playerMenuGroup)

#if Foundation.shipList._keyList.has_key(longName):
#     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
#     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

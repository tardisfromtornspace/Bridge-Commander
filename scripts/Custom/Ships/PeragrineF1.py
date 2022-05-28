from bcdebug import debug
import Foundation
import App
# Usually you need only edit these seven lines

abbrev = 'PeragrineF1'
iconName = 'PeragrineF1'
longName = 'Peragrine'
shipFile = 'PeragrineF1' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
species = App.SPECIES_GALAXY
SubMenu = "Shuttles"


# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.

credits = {
	'modName': 'PeragrineF1',   # The full name of your mod if applicable
	'author': '',              # Your name here
	'version': '1.0',                     # No more than one period please!
	                                      # I'd like to be able to do a numeric comparison.
	'sources': [ 'http://' ],             # Source for this mod
	'comments': ''                        # General info
}

# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, Print a #
# in front of the first line and uncomment the line with FedShipDef.

import F_FedAttackFighterAI
Foundation.ShipDef.PeragrineF1 = F_FedAttackFighterAI.FedAttackFighterAI(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.PeragrineF1.fMaxWarp = 8.0
Foundation.ShipDef.PeragrineF1.sBridge = 'Type11Bridge'

# Uncomment these if you have TGL

Foundation.ShipDef.PeragrineF1.hasTGLName = 1
Foundation.ShipDef.PeragrineF1.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.PeragrineF1.desc = 'No Description Available'

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:           Foundation.ShipDef.PeragrineF1.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.PeragrineF1.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

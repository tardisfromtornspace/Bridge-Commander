from bcdebug import debug
import Foundation
import App

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.deltaflyer.desc = 'oundation
import App
# Usually, you need only edit these seven lines

abbrev = 'deltaflyer'
iconName = 'deltaflyer'
longName = 'Delta Flyer'
shipFile = 'deltaflyer' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
species = App.SPECIES_GALAXY
SubMenu = "Shuttles"


# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.

credits = {
	'modName': 'deltaflyer',   # The full name of your mod if applicable
	'author': 'Darkdrone, SSMike',              # Your name here
	'version': '1.0',                     # No more than one period please!
	                                      # I'd like to be able to do a numeric comparison.
	'sources': [ 'http://' ],             # Source for this mod
	'comments': ''                        # General info
}

# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, put a #
# in front of the first line and uncomment the line with FedShipDef.

Foundation.ShipDef.deltaflyer = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.deltaflyer.fMaxWarp = 8.0
Foundation.ShipDef.deltaflyer.sBridge = 'Type11Bridge'
Foundation.ShipDef.deltaflyer.hasTGLName = 1
Foundation.ShipDef.deltaflyer.hasTGLDesc = 1
Foundation.ShipDef.deltaflyer.dTechs = {
	'Breen Drainer Immune': 1,
	'Regenerative Shields': 30,
}


# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:           Foundation.ShipDef.deltaflyer.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.deltaflyer.RegisterQBPlayerShipMenu(playerMenuGroup)

# If you want to override an existing ship, uncomment and edit the following:
# Foundation.ShipDef.FTBdeltaflyer.friendlyDetails[2] = 'QBFriendlydeltaflyerDestroyed'
# Foundation.ShipDef.FTBdeltaflyer.enemyDetails[2] = 'QBEnemydeltaflyerDestroyed'


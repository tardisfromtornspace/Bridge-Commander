import Foundation
import App
# Usually you need only edit these seven lines

abbrev = 'venimp'
iconName = 'venimp'
longName = 'Venator'
shipFile = 'venimp' 
menuGroup = 'Star Wars Fleet'                  # Menu to appear under in Quick Battle
playerMenuGroup = 'Star Wars Fleet'
SubMenu = "Galactic Empire"
species = App.SPECIES_GALAXY


# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.

credits = {
	'modName': 'venimp',   # The full name of your mod if applicable
	'author': 'DARKDRONE',              # Your name here
	'version': '1.0',                     # No more than one period please!
	                                      # I'd like to be able to do a numeric comparison.
	'sources': [ 'http://' ],             # Source for this mod
	'comments': ''                        # General info
}

# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, Print a #
# in front of the first line and uncomment the line with FedShipDef.

Foundation.ShipDef.venimp = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Uncomment these if you have TGL
# Foundation.ShipDef.venimp.hasTGLName = 1
# Foundation.ShipDef.venimp.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
Foundation.ShipDef.venimp.desc = "The Venator Assault Ship, repainted after the Clone Wars to serve the new formed Empire."

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:           Foundation.ShipDef.venimp.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.venimp.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

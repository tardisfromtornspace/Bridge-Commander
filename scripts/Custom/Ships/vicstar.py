import Foundation
import App
# Usually you need only edit these seven lines

abbrev = 'vicstar'
iconName = 'vicstar'
longName = 'Victory'
shipFile = 'vicstar' 
menuGroup = 'Star Wars Fleet'
playerMenuGroup = 'Star Wars Fleet'
SubMenu = "Galactic Empire"
species = App.SPECIES_GALAXY


# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.

credits = {
	'modName': 'vicstar',   # The full name of your mod if applicable
	'author': 'DARKDRONE',              # Your name here
	'version': '1.0',                     # No more than one period please!
	                                      # I'd like to be able to do a numeric comparison.
	'sources': [ 'http://' ],             # Source for this mod
	'comments': ''                        # General info
}

# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, Print a #
# in front of the first line and uncomment the line with FedShipDef.

Foundation.ShipDef.vicstar = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Uncomment these if you have TGL
# Foundation.ShipDef.vicstar.hasTGLName = 1
# Foundation.ShipDef.vicstar.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
Foundation.ShipDef.vicstar.desc = 'Victory Star Destroyers were a group of warship designs that consisted of two main sub-classes and several modifications to these, used from planetary defense to deep space combat. Like later Star Destroyer designs, the Victory possessed the ability to enter the upper levels of a planetary atmosphere. This gave the ship a decided advantage of added precision when engaging in the ground attack operations the class was designed to carry out. '

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:           Foundation.ShipDef.vicstar.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.vicstar.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

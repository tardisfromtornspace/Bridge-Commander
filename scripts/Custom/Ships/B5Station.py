import Foundation
import App
# Usually you need only edit these seven lines

abbrev = 'B5Station'
iconName = 'B5Station'
longName = 'Babylon 5 Station'
shipFile = 'B5Station' 
menuGroup = 'Babylon 5'
playerMenuGroup = 'Babylon 5'
species = App.SPECIES_GALAXY


# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.

credits = {
	'modName': 'B5Station',   # The full name of your mod if applicable
	'author': '',              # Your name here
	'version': '1.0',                     # No more than one period please!
	                                      # I'd like to be able to do a numeric comparison.
	'sources': [ 'http://' ],             # Source for this mod
	'comments': ''                        # General info
}

# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, Print a #
# in front of the first line and uncomment the line with FedShipDef.

Foundation.ShipDef.B5Station = Foundation.KlingonShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.B5Station.dTechs = {
	'Defense Grid': 200
}
# Uncomment these if you have TGL
#Foundation.ShipDef.B5Station.hasTGLName = 1
#Foundation.ShipDef.B5Station.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
Foundation.ShipDef.B5Station.desc = 'Babylon 5 was the fifth and final space station of the Babylon Project, created by the Earth Alliance to prevent another war (after the Earth-Minbari War), by creating a place where humans and aliens can work out their differences peacefully, and made of two million five hundred thousand tons of spinning metal, located in neutral space in orbit of Epsilon III near Epsilon Eridani. Babylon 5 was built to support around 250,000 humans and aliens, though most were often in transit to and from various worlds, many others actually lived and worked on the station.'

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:           Foundation.ShipDef.B5Station.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.B5Station.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

import Foundation
import App

# Usually you need only edit these seven lines
abbrev = 'bluestar'
iconName = 'bluestar'
longName = 'Bluestar'
shipFile = 'bluestar' 
menuGroup = 'Babylon 5'
playerMenuGroup = 'Babylon 5'
SubMenu = "Interestellar Alliance"
species = App.SPECIES_GALAXY

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.

credits = {
	'modName': 'bluestar',   # The full name of your mod if applicable
	'author': '',              # Your name here
	'version': '1.0',                     # No more than one period please!
	                                      # I'd like to be able to do a numeric comparison.
	'sources': [ 'http://' ],             # Source for this mod
	'comments': ''                        # General info
}


# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, Print a #
# in front of the first line and uncomment the line with FedShipDef.

Foundation.ShipDef.bluestar = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

Foundation.ShipDef.bluestar.dTechs = {
	'Automated Destroyed System Repair': {"Time": 1800.0},
	"Fool Targeting": {
		"Minbari Stealth": {
			"Miss": 4.0,
			"Sensor": 590,
		}  
	},
	"Tachyon Sensors": 0.5
}

# Uncomment these if you have TGL
# Foundation.ShipDef.bluestar.hasTGLName = 1
# Foundation.ShipDef.bluestar.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
Foundation.ShipDef.bluestar.desc = 'The bluestar, or Snub-nose White Star is an smaller personal version of the White Star and possesses many of the same Minbari and Vorlon design features including artificial intelligence and the ability to create jump points. Built by the Interstellar Alliance, these ships were a common sight over the central planet Minbar by 2281 and in service as early as 2263. President John Sheridan piloted his personal White Star from Minbar to Babylon 5 and then Coriana VI shortly before Babylon 5´s decommissioning ceremony. His ship was later found adrift in the Coriana system, empty and with all its airlocks sealed.'

# These register the ship with the QuickBattle menus.  Don't touch them!!!

if menuGroup:           Foundation.ShipDef.bluestar.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.bluestar.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
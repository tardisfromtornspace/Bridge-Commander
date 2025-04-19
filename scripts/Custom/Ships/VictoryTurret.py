import App
import Foundation

# Usually you need only edit these seven lines
abbrev = 'VictoryTurret'
iconName = 'Victory'
longName = 'VictoryTurret'
shipFile = 'VictoryTurret' 
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "Interestellar Alliance"
species = App.SPECIES_GALAXY
SubSubMenu = "Destroyers"

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.

credits = {
	'modName': 'VictoryTurret',   # The full name of your mod if applicable
	'author': '',              # Your name here
	'version': '1.0',                     # No more than one period please!
	                                      # I'd like to be able to do a numeric comparison.
	'sources': [ 'http://' ],             # Source for this mod
	'comments': ''                        # General info
}

# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, Print a #
# in front of the first line and uncomment the line with FedShipDef.

Foundation.ShipDef.VictoryTurret = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })
Foundation.ShipDef.VictoryTurret.dTechs = {
        'Regenerative Shields': 30,
        #"AutoTargeting": { "Phaser": [3, 1] },
        'Polarized Hull Plating': { "Plates": ["PlastiCrystalline Armour"]}
}

# Uncomment these if you have TGL  
#Foundation.ShipDef.VictoryTurret.hasTGLName = 1
#Foundation.ShipDef.VictoryTurret.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
Foundation.ShipDef.VictoryTurret.desc = "The Destroyer class White Star project was a joint Earth/Minbar venture to create a larger, more-powerful warship for use by the Interstellar Alliance to complement the White Star fleet. The resulting ship class is sometimes referred to as a Victory-class destroyer after the first ship of the line. The destroyer is based on technology from the White Star fleet - being a combination of Minbari and Vorlon technology - combined with Earth tech in function and aesthetic. The two greatest applications of alien technology with human is in the artificial gravity and associated gravimetric engines of Minbari design, coupled with the powerful weapon system derived from Vorlon tech. As opposed to the Warlock class destroyer used by Earthforce - which used conventional ion drives and weak artificial gravity - the destroyer would have a full-gravity environment in which the crew could move freely as well as full gravimetric propulsion. This made the ship as maneuverable and as jump capable as a Minbari capital vessel, able to jump into and out of hyperspace repeatedly."

# These register the ship with the QuickBattle menus.  Don't touch them... unless you don't want them to be registered, which is our case.
#if menuGroup:           Foundation.ShipDef.VictoryTurret.RegisterQBShipMenu(menuGroup)
#if playerMenuGroup:     Foundation.ShipDef.VictoryTurret.RegisterQBPlayerShipMenu(playerMenuGroup)

#if Foundation.shipList._keyList.has_key(longName):
#     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
#     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
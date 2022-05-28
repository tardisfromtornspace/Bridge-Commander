from bcdebug import debug
import Foundation
import App
# Usually, you need only edit these seven lines

abbrev = 'GalaxyX'
iconName = 'GalaxyX'
longName = 'Galaxy refit'
shipFile = 'GalaxyX' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
species = App.SPECIES_GALAXY


# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.

credits = {
	'modName': 'Future Galaxy',        # The full name of your mod if applicable
	'author': '',        # Your name here
	'version': '1.0',                     # No more than one period please!
	                                      # I'd like to be able to do a numeric comparison.
	'sources': [ 'http://' ],             # Source for this mod
	'comments': ''                        # General info
}

# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, put a #
# in front of the first line and uncomment the line with FedShipDef.

Foundation.ShipDef.GalaxyX = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.GalaxyX.sBridge = 'GalaxyBridge'
Foundation.ShipDef.GalaxyX.dTechs = {
	'Breen Drainer Immune': 0,
	'Regenerative Shields': 20,
	'Multivectral Shields': 30,
}

Foundation.ShipDef.GalaxyX.desc = 'The Galaxy X-class was a type of Federation starship, in Starfleet service at the end of the 24th century, and were expected to continue in service into the 25th century. It was a dreadnought subclass of the Galaxy-class design. The Galaxy class was refitted at the turn of the 25th century, after the collapse of the Khitomer Accords in 2399 in an alternate timeline. In response to increased hostility with the Klingons, the newly redesigned ship was equipped with a phaser spinal lance, phaser cannons and a cloaking device since Starfleet was authorized to develop and implement cloaking technology on selected ships. The additional engine nacelle assembly greatly increased the ship´s speed.'

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:           Foundation.ShipDef.GalaxyX.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.GalaxyX.RegisterQBPlayerShipMenu(playerMenuGroup)



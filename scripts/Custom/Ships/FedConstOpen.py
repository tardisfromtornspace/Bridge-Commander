from bcdebug import debug
import Foundation
import App
#

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.FedConstOpen.desc = 'oundation
import App
# Usually, you need only edit these seven lines

abbrev = 'FedConstOpen'
iconName = 'FedConstOpen'
longName = 'Federation Construction Ship Open'
shipFile = 'FedConstOpen' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
species = App.SPECIES_GALAXY


# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.

credits = {
	'modName': 'FedConstOpen',   # The full name of your mod if applicable
	'author': 'Cleeve (Don Woligroski)',              # Your name here
	'version': '0.9 Beta',                     # No more than one period please!
	                                      # I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.STARYARDS.com' ],             # Source for this mod
	'comments': ''                        # General info
}

# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, put a #
# in front of the first line and uncomment the line with FedShipDef.

Foundation.ShipDef.FedConstOpen = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.FedConstOpen.hasTGLName = 1
Foundation.ShipDef.FedConstOpen.hasTGLDesc = 1

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:           Foundation.ShipDef.FedConstOpen.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.FedConstOpen.RegisterQBPlayerShipMenu(playerMenuGroup)

#Foundation.SoundDef("sfx/Weapons/PulsePhsr.wav", "PulsePhsr", 1.0)



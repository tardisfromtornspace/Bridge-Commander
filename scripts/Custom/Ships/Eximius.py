from bcdebug import debug
import Foundation
import App
#

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.Eximius.desc = 'oundation
import App
# Usually, you need only edit these seven lines

abbrev = 'Eximius'
iconName = 'Eximius'
longName = 'Eximius'
shipFile = 'Eximius' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
species = App.SPECIES_GALAXY


# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.

credits = {
	'modName': 'Eximius',   # The full name of your mod if applicable
	'author': 'Cleeve (Don Woligroski)',              # Your name here
	'version': '1.0 Beta',                     # No more than one period please!
	                                      # I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.STARYARDS.com' ],             # Source for this mod
	'comments': 'The only difference is that now the armour is activated'                        # General info
}

# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, put a #
# in front of the first line and uncomment the line with FedShipDef.

Foundation.ShipDef.Eximius = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.Eximius.hasTGLName = 1
Foundation.ShipDef.Eximius.hasTGLDesc = 1
Foundation.ShipDef.Eximius.dTechs = {
	'Breen Drainer Immune': 1,
	'Multivectral Shields': 10,
	'Fed Ablative Armor': { "Plates": ["Forward Ablative Armor", "Top Ablative Armor", "Bottom Ablative Armor", "Aft Ablative Armor"]
}}

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:           Foundation.ShipDef.Eximius.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Eximius.RegisterQBPlayerShipMenu(playerMenuGroup)

#Foundation.SoundDef("sfx/Weapons/PulsePhsr.wav", "PulsePhsr", 1.0)



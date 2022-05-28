from bcdebug import debug
import Foundation
import App

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.Defiant.desc = 'Foundation
import App

Foundation.SoundDef("sfx/Weapons/PPhaser.wav", "PPhaser", 0.7)

# Usually, you need only edit these seven lines
abbrev = 'Defiant'				# Short name, no spaces, used as a preface for descriptions
iconName = 'Defiant'					# Name of icon .tga file
longName = 'Defiant'					# Long name with spaces
shipFile = 'Defiant'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Fed Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Fed Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_MARAUDER			# I'm not sure how important this is.
# Thats mainly for the icon, but unused


# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Defiant',			# The full name of your mod if applicable
	'author': 'Defiant',					# Your name here
	'version': '0.7',						# No more than one period please!  
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://startrek.webhop.info' ],				# Source for this mod
	'comments': ''						# General info
}


Foundation.ShipDef.Defiant = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.Defiant.dTechs = { 'Fed Ablative Armor': {
	"Plates": ["Aft Ablative Armor", "Forward Ablative Armor", "Left Ablative Armor", "Right Ablative Armor"]
}}
Foundation.ShipDef.Defiant.sBridge = 'defiantbridge'
Foundation.ShipDef.Defiant.fMaxWarp = 9.5
Foundation.ShipDef.Defiant.fWarpEntryDelayTime = 2.0
Foundation.ShipDef.Defiant.hasTGLName = 1
Foundation.ShipDef.Defiant.hasTGLDesc = 1


if menuGroup:           Foundation.ShipDef.Defiant.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Defiant.RegisterQBPlayerShipMenu(playerMenuGroup)

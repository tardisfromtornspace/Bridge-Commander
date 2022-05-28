from bcdebug import debug
import Foundation
import App

#
#Foundation.ShipDef.Defiant.hasTGLName = 1
#Foundation.ShipDef.Defiant.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.Defiant.desc = 'Foundation
import App

Foundation.SoundDef("sfx/Weapons/PPhaser.wav", "PPhaser", 0.7)

# Usually, you need only edit these seven lines
abbrev = 'EnterpriseJ'				# Short name, no spaces, used as a preface for descriptions
iconName = 'EnterpriseJ'					# Name of icon .tga file
longName = 'U.S.S. Enterprise J'					# Long name with spaces
shipFile = 'EnterpriseJ'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Fed Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Fed Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_MARAUDER			# I'm not sure how important this is.
# Thats mainly for the icon, but unused


# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'EnterpriseJ',			# The full name of your mod if applicable
	'author': 'EnterpriseJ',					# Your name here
	'version': '1.1',						# No more than one period please!  
										# I'd like to be able to do a numeric comparison.
	'sources': [ '' ],				# Source for this mod
	'comments': ''						# General info
}


Foundation.ShipDef.EnterpriseJ = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.EnterpriseJ.dTechs = {
	'Breen Drainer Immune': 0,
	'Regenerative Shields': 60,
	'Multivectral Shields': 50,
	'Fed Ablative Armor': { "Plates": ["Forward Ablative Armor", "Aft Ablative Armor", "Dorsal Ablative Armor", "Ventral Ablative Armor"]
}}
Foundation.ShipDef.EnterpriseJ.sBridge = 'defiantbridge'
Foundation.ShipDef.EnterpriseJ.fMaxWarp = 9.995
Foundation.ShipDef.EnterpriseJ.fWarpEntryDelayTime = 3.5

Foundation.ShipDef.EnterpriseJ.desc = 'The USS Enterprise NCC-1701-J was a 26th century Federation Universe-class starship operated by Starfleet in a possible future. The Enterprise-J participated in the historic Battle of Procyon V, wherein the forces of the Federation successfully drove the Sphere-Builders back into their trans-dimensional realm.'

if menuGroup:           Foundation.ShipDef.EnterpriseJ.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.EnterpriseJ.RegisterQBPlayerShipMenu(playerMenuGroup)

from bcdebug import debug
import Foundation
import App


# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.DomBB.desc = 'oundation
import App

# Usually, you need only edit these seven lines
abbrev = 'DomBB'				# Short name, no spaces, used as a preface for descriptions
iconName = 'DomBB'				# Name of icon .tga file
longName = 'Dominion Battleship'				# Long name with spaces
shipFile = 'DomBB'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Dominion Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Dominion Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_SOVEREIGN	# I'm not sure how important this is.

Foundation.SoundDef("sfx/Weapons/HLB.wav", "HLB", 1.0)

Foundation.ShipDef.DomBB = Foundation.DominionShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.DomBB.dTechs = { 'Breen Drainer Immune': 1 }
Foundation.ShipDef.DomBB.fMaxWarp = 8.5
Foundation.ShipDef.DomBB.hasTGLName = 1
Foundation.ShipDef.DomBB.hasTGLDesc = 1

if menuGroup:			Foundation.ShipDef.DomBB.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.DomBB.RegisterQBPlayerShipMenu(playerMenuGroup)

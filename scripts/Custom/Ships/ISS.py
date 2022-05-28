import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'ISS'				# Short name, no spaces, used as a preface for descriptions
iconName = 'CSS'				# Name of icon .tga file
longName = 'Imperial Super Star Destroyer'				# Long name with spaces
shipFile = 'ISS'				# Name of the file in Scripts\Ships\ to use.			
menuGroup = 'Star Wars Fleet'                  # Menu to appear under in Quick Battle
playerMenuGroup = 'Star Wars Fleet'
SubMenu = "Galactic Empire"		# ...set to None if you don't want to appear here.
species = App.SPECIES_SOVEREIGN		# I'm not sure how important this is.

Foundation.ShipDef.ISD = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

Foundation.SoundDef("sfx/Weapons/ImpLaser1.wav", "ImpLaser1", 1.0)
Foundation.SoundDef("sfx/Weapons/ImpLaser2.wav", "ImpLaser2", 1.0)
Foundation.SoundDef("sfx/Weapons/ImpLaserXL.wav", "ImpLaserXL", 1.0)
Foundation.SoundDef("sfx/Weapons/ImpIon1.wav", "ImpIon1", 1.0)
Foundation.SoundDef("sfx/Weapons/ImpIon2.wav", "ImpIon2", 1.0)

Foundation.ShipDef.ISD.desc = 'The Executor Imperial Super Star Destroyer was the flagship of Darth Vader. Executor-class Star Dreadnoughts were some of the largest and most powerful Imperial starships ever created.'


if menuGroup:			Foundation.ShipDef.ISD.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.ISD.RegisterQBPlayerShipMenu(playerMenuGroup)

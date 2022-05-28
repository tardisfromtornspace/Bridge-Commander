from bcdebug import debug
import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'DyExcalibur'					# Short name, no spaces, used as a preface for descriptions
iconName = 'DyExcalibur'				# Name of icon .tga file
longName = 'Excalibur'				# Long name with spaces
shipFile = 'DyExcalibur'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Fed Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Fed Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_VORCHA		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Uss DyExcalibur',			# The full name of your mod if applicable
	'author': 'John Doe',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol and space from) the line which has a ShipDef
# you want.  A generic ship should use ShipDef.  If you want a Federation Ship
# put a # in front of the first line and uncomment the line with FedShipDef.

Foundation.ShipDef.DyExcalibur = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.DyExcalibur.dTechs = {
	'Breen Drainer Immune': 0,
	'Regenerative Shields': 10,
	'Multivectral Shields': 20
}
Foundation.ShipDef.DyExcalibur.sBridge = 'ExcaliburBridge'

# Uncomment these if you have TGL

Foundation.ShipDef.DyExcalibur.hasTGLName = 1
Foundation.ShipDef.DyExcalibur.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.DyExcalibur.desc = 'DyExcalibur'

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.DyExcalibur.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.DyExcalibur.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
	Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
	Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

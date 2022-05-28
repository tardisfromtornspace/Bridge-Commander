from bcdebug import debug
import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'ds9'					# Short name, no spaces, used as a preface for descriptions
iconName = 'CardStarbase'				# Name of icon .tga file
longName = 'Deep Space Nine'				# Long name with spaces
shipFile = 'ds9'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Bases'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Bases'		# ...set to None if you don't want to appear here.
species = App.SPECIES_CARD_STARBASE		# I'm not sure how important this is.
# ^^ Is that for the AI?


# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Bajoran Starbase Deep Space 9',			# The full name of your mod if applicable
	'author': 'Defiant',					# Your name here
	'version': '0.1',						# No more than one period please!  
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://startrek.webhop.info' ],				# Source for this mod
	'comments': ''						# General info
}

# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, put a #
# in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.ds9 = Foundation.StarBaseDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
# Foundation.ShipDef.DS9 = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
# Foundation.ShipDef.DS9 = Foundation.StarBaseDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
# Foundation.ShipDef.DS9 = Foundation.CardStarBaseDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
# Foundation.ShipDef.DS9 = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
# Foundation.ShipDef.DS9 = Foundation.CardShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
# Foundation.ShipDef.DS9 = Foundation.RomulanShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
# Foundation.ShipDef.DS9 = Foundation.KlingonShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
# Foundation.ShipDef.DS9 = Foundation.KessokShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
# Foundation.ShipDef.DS9 = Foundation.FerengiShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
# Foundation.ShipDef.DS9 = Foundation.DominionShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
# Foundation.ShipDef.DS9 = Foundation.BorgShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.ds9.hasTGLName = 1
Foundation.ShipDef.ds9.hasTGLDesc = 1
Foundation.ShipDef.ds9.dTechs = {
	'Breen Drainer Immune': 1,
	'Multivectral Shields': 5
}

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.ds9.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.ds9.RegisterQBPlayerShipMenu(playerMenuGroup)

# If you want to override an existing ship, uncomment and edit the following:  
#if Foundation.shipList._keyList.has_key(longName):
#	Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
#	Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

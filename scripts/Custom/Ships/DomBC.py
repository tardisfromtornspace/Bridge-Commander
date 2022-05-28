from bcdebug import debug
import Foundation
import App


# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.DomBC.desc = 'oundation
import App

# Usually, you need only edit these seven lines
abbrev = 'DomBC'				# Short name, no spaces, used as a preface for descriptions
iconName = 'DomBC'				# Name of icon .tga file
longName = 'Dominion Battlecruiser'				# Long name with spaces
shipFile = 'DomBC'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Dominion Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Dominion Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_SOVEREIGN		# I'm not sure how important this is.

Foundation.ShipDef.DomBC = Foundation.DominionShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.DomBC.dTechs = { 'Breen Drainer Immune': 1 }
Foundation.ShipDef.DomBC.fMaxWarp = 9.15
Foundation.ShipDef.DomBC.hasTGLName = 1
Foundation.ShipDef.DomBC.hasTGLDesc = 1

if menuGroup:			Foundation.FedShipDef.DomBC.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.FedShipDef.DomBC.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
	Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
	Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

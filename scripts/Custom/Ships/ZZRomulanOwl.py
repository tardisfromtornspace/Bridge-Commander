from bcdebug import debug
import Foundation
import App

abbrev = 'ZZRomulanOwl'
iconName = 'ZZRomulanOwl'
longName = "ZZ's CA Storm Owl Class"
shipFile = 'ZZRomulanOwl'
menuGroup = 'Romulan Ships'
playerMenuGroup = 'Romulan Ships'
species = App.SPECIES_GALAXY

# Credits and mod information.
credits = {
	'modName': 'ZZRomulanOwl',
	'author': 'Zambie Zan alexmarques400@hotmail.com',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': 'Tested in KM'
}

import F_ZZAttackDef


# This is the new class that defines your ship and links it to the AI.
class ZZRomulanOwl(Foundation.ShipDef):
	"""
	Defines a custom ship class for the Veritex.
	"""
	def __init__(self, abbrev, species, dict):
		# Set the ship's race to Federation.
		dict['race'] = Foundation.Federation
		# Call the parent class's constructor to set up the ship definition.
		Foundation.ShipDef.__init__(self, abbrev, species, dict)

	def StrFriendlyAI(self):
		"""
		Returns the string name of the AI script for a friendly ship.
		"""
		return 'ZZVeritexFAI'

	def StrEnemyAI(self):
		"""
		Returns the string name of the AI script for an enemy ship.
		"""
		return 'ZZVeritexEAI'

Foundation.ShipDef.ZZRomulanOwl = F_ZZAttackDef.ZZAttackDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})

# Set the ship's description.
Foundation.ShipDef.ZZRomulanOwl.desc = """The Storm Owl class Bird-of-Prey was a short-lived but highly influential Romulan warship design, developed in the late 23rd century as part of a new rapid-escalation doctrine.\n\nLarger and more heavily armored than earlier Birds-of-Prey, yet far more agile than later Romulan warbirds, the Storm Owl represented a transitional step in Romulan naval evolution.\n\nIt  mounted enhanced plasma torpedo arrays and devastating singularity mines that caused catastrophic destruction of a Federation outpost.\n\nThe prototype IRW T'Vrel, led the vanguard in the Tomed Incident of 2311 but the Treaty of Algeron that followed condemned the class to obscurity. Deemed too provocative, the vessels were decommissioned lest they shatter the fragile peace."""

if menuGroup:
	Foundation.ShipDef.ZZRomulanOwl.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:
	Foundation.ShipDef.ZZRomulanOwl.RegisterQBPlayerShipMenu(playerMenuGroup)

# Handle potential conflicts if the ship already exists in the list.
if Foundation.shipList._keyList.has_key(longName):
	Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
	Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def PreLoadAssets():
    pass

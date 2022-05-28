import Foundation

class RomulanStarBaseDef(Foundation.ShipDef):
	def __init__(self, abbrev, species, dict):
		dict['race'] = Foundation.Romulan
		Foundation.ShipDef.__init__(self, abbrev, species, dict)
	def StrFriendlyAI(self):
		return 'StarbaseFriendlyAI'
	def StrEnemyAI(self):
		return 'StarbaseAI'

Foundation.RomulanStarBaseDef = RomulanStarBaseDef

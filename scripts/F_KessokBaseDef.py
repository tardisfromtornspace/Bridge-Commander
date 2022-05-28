import Foundation

class KessokStarBaseDef(Foundation.ShipDef):
	def __init__(self, abbrev, species, dict):
		dict['race'] = Foundation.Kessok
		Foundation.ShipDef.__init__(self, abbrev, species, dict)
	def StrFriendlyAI(self):
		return 'StarbaseFriendlyAI'
	def StrEnemyAI(self):
		return 'StarbaseAI'

Foundation.KessokStarBaseDef = KessokStarBaseDef

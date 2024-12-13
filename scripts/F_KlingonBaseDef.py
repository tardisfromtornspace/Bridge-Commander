import Foundation

class KlingonStarBaseDef(Foundation.ShipDef):
	def __init__(self, abbrev, species, dict):
		dict['race'] = Foundation.Klingon
		Foundation.ShipDef.__init__(self, abbrev, species, dict)
	def StrFriendlyAI(self, *args):
		return 'StarbaseFriendlyAI'
	def StrEnemyAI(self, *args):
		return 'StarbaseAI'

Foundation.KlingonStarBaseDef = KlingonStarBaseDef

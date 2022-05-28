import Foundation

ShipDef = Foundation.ShipDef
Federation = Foundation.Federation

class MineDef(ShipDef):
	def __init__(self, abbrev, species, dict):
		dict['race'] = Federation
		ShipDef.__init__(self, abbrev, species, dict)

	def StrFriendlyAI(self):
		return 'MineFriendlyAttack'

	def StrEnemyAI(self):
		return 'MineAttack'

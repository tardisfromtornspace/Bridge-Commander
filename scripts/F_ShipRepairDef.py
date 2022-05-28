import Foundation

ShipDef = Foundation.ShipDef
Federation = Foundation.Federation

class ShipRepairDef(ShipDef):
	def __init__(self, abbrev, species, dict):
		dict['race'] = Federation
		ShipDef.__init__(self, abbrev, species, dict)
	def StrFriendlyAI(self):
		return 'QuickBattleAI'
	def StrEnemyAI(self):
		return 'QuickBattleFriendlyAI'
		
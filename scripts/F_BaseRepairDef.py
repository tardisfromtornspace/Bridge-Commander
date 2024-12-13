import Foundation

ShipDef = Foundation.ShipDef
Federation = Foundation.Federation

class BaseRepairDef(ShipDef):
	def __init__(self, abbrev, species, dict):
		dict['race'] = Federation
		ShipDef.__init__(self, abbrev, species, dict)

	def StrFriendlyAI(self, *args):
		return 'RepairAI'

	def StrEnemyAI(self, *args):
		return 'RepairEnemyAI'

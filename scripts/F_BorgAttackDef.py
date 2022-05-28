import Foundation

ShipDef = Foundation.ShipDef
Borg = Foundation.Borg

class BorgAttackDef(ShipDef):
	def __init__(self, abbrev, species, dict):
		dict['race'] = Borg
		ShipDef.__init__(self, abbrev, species, dict)

        def StrFriendlyAI(self):
                return 'BorgAttackFriendlyAI'

        def StrEnemyAI(self):
                return 'BorgAttackAI'

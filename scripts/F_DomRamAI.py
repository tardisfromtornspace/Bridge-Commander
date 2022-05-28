import Foundation

ShipDef = Foundation.ShipDef
Dominion = Foundation.Dominion

class DomRamAI(ShipDef):
	def __init__(self, abbrev, species, dict):
		dict['race'] = Dominion
		ShipDef.__init__(self, abbrev, species, dict)
        def StrEnemyAI(self):
                return "DomRamAI"

import Foundation

ShipDef = Foundation.ShipDef
oZZAndromedans = Foundation.RaceDef("ZZAndromedan", "ZZAndromedan")

class ZZAndromedanShipDef(ShipDef):
	def __init__(self, abbrev, species, dict):
		dict['race'] = oZZAndromedans
		Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
	def OverrideWarpFXColor(self, *args):
		return (225.0, 255.0, 0.0)
	
	def OverridePlasmaFXColor(self, *args):
		return (250.0, 185.0, 135.0)

	def StrFriendlyAI(self, *args):
		return 'ZZAndromedanAttackFriendlyAI'

	def StrEnemyAI(self, *args):
		return 'ZZAndromedanAttackAI'

Foundation.oZZAndromedans = oZZAndromedans
Foundation.ZZAndromedanShipDef = ZZAndromedanShipDef
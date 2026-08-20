import Foundation
import K_ZZAndromedanAttackDef

# Same race / FX as ZZAndromedanShipDef, but points at the Light QuickBattle AIs.
class ZZAndromedanLightShipDef(K_ZZAndromedanAttackDef.ZZAndromedanShipDef):
	def StrFriendlyAI(self, *args):
		return 'ZZAndromedanLightFriendlyAI'

	def StrEnemyAI(self, *args):
		return 'ZZAndromedanLightAI'

Foundation.ZZAndromedanLightShipDef = ZZAndromedanLightShipDef

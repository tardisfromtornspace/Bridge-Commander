from bcdebug import debug
import Foundation
ShipDef = Foundation.ShipDef
Federation = Foundation.Federation

class FedAttackLightCruiserAI(ShipDef):
	def __init__(self, abbrev, species, dict):
		debug(__name__ + ", __init__")
		dict['race'] = Federation
		ShipDef.__init__(self, abbrev, species, dict)

	def StrFriendlyAI(self):
		debug(__name__ + ", StrFriendlyAI")
		return 'FedAttackLightCruiserFriendlyAI'

	def StrEnemyAI(self):
		debug(__name__ + ", StrEnemyAI")
		return 'FedAttackLightCruiserAI'

	def GetAttackModule(self):
		debug(__name__ + ", GetAttackModule")
		return 'FedAttackLightCruiserAI'

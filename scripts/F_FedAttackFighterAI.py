import Foundation
ShipDef = Foundation.ShipDef
Federation = Foundation.Federation

class FedAttackFighterAI(ShipDef,):

    def __init__(self, abbrev, species, dict):
        dict['race'] = Federation
        ShipDef.__init__(self, abbrev, species, dict)


    def StrFriendlyAI(self):
        return 'FedAttackFighterFriendlyAI'


    def StrEnemyAI(self):
        return 'FedAttackFighterAI'

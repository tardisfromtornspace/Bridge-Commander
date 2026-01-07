# File: K (Python 1.5)

import Foundation
ShipDef = Foundation.ShipDef
Klingon = Foundation.Klingon

class ZZAttackDef(ShipDef):
    
    def __init__(self, abbrev, species, dict):
        dict['race'] = Klingon
        ShipDef.__init__(self, abbrev, species, dict)

    
    def StrFriendlyAI(self):
        return 'ZZVeritexFAI'

    
    def StrEnemyAI(self):
        return 'ZZVeritexEAI'



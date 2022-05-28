import Foundation
import StaticDefs

Foundation.BridgeDef('Type11_Cockpit', 'Type11Bridge', dict = {'modes': [ Foundation.MutatorDef.Stock ],
	'locations': {
		'T11Helm':[ 'data/animations/T11_stand_h_m.nif', 'T11_stand_h_m' ],
		'T11Tactical':[ 'data/animations/T11_stand_t_l.nif', 'T11_stand_t_l' ],
		'T11Science':[ 'data/animations/T11_stand_S_S.nif', 'T11_stand_s_s' ],
		'T11Engineer':[ 'data/animations/DF_seated_C_M.nif', 'DF_seated_C_M' ],
		'T11XO':[ 'data/animations/T1_stand_H_M.nif', 'T1_stand_H_M' ],
		'T11L1S':[ 'data/animations/T11_L1toG3_S.nif', 'T11_L1toG3_s', 'pCharacter.SetHidden(1)' ],
		'T11L1M':[ 'data/animations/T11_L1toG3_M.nif', 'T11_L1toG3_M', 'pCharacter.SetHidden(1)' ],
		'T11L1L':[ 'data/animations/T11_L1toG3_L.nif', 'T11_L1toG3_L', 'pCharacter.SetHidden(1)' ],
		'T11L2M':[ 'data/animations/T11_L2toG2_M.nif', 'T11_L2toG2_M', 'pCharacter.SetHidden(1)' ],
		'T11G1M':[ 'data/animations/T11_G1toL2_M.nif', 'T11_G1toL2_M' ],
		'T11G2M':[ 'data/animations/T11_G2toL2_M.nif', 'T11_G2toL2_M' ],
		'T11G3M':[ 'data/animations/T11_G3toL1_M.nif', 'T11_G3toL1_M' ],}
})

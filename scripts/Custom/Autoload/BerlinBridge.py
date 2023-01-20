import Foundation

# Uncomment the below to enable!
Foundation.BridgeDef('Berlin', 'BerlinBridge', dict = {
	'modes': [ Foundation.MutatorDef.Stock ],
	'locations': {
		'AmbHelm':	[ 'data/animations/Amb_stand_h_m.nif', 'Amb_stand_h_m' ],
		'AmbTactical':	[ 'data/animations/Amb_stand_t_l.nif', 'Amb_stand_t_l' ],
		'AmbCommander':	[ 'data/animations/Amb_stand_c_m.nif', 'Amb_stand_c_m' ],
		'AmbScience':	[ 'data/animations/Amb_stand_S_S.nif', 'Amb_stand_s_s' ],
		'AmbEngineer':	[ 'data/animations/Amb_stand_e_s.nif', 'Amb_stand_e_s' ],
		'AmbGuest':	[ 'data/animations/Amb_stand_X_m.nif', 'Amb_stand_X_m' ],
	}
} )
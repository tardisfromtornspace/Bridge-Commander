import Foundation

mode = Foundation.MutatorDef('Babylon 5 Uniforms')

Foundation.OverrideDef.CreateCharacter = Foundation.OverrideDef('CreateCharacter', 'Bridge.Characters.Brex.CreateCharacter', 'Bridge.Characters.B5Brex.CreateCharacter', dict = { 'modes': [ mode ] } )
Foundation.OverrideDef.CreateCharacter = Foundation.OverrideDef('CreateCharacter', 'Bridge.Characters.Miguel.CreateCharacter', 'Bridge.Characters.B5Miguel.CreateCharacter', dict = { 'modes': [ mode ] } )
Foundation.OverrideDef.CreateCharacter = Foundation.OverrideDef('CreateCharacter', 'Bridge.Characters.Felix.CreateCharacter', 'Bridge.Characters.B5Felix.CreateCharacter', dict = { 'modes': [ mode ] } )
Foundation.OverrideDef.CreateCharacter = Foundation.OverrideDef('CreateCharacter', 'Bridge.Characters.Kiska.CreateCharacter', 'Bridge.Characters.B5Kiska.CreateCharacter', dict = { 'modes': [ mode ] } )
Foundation.OverrideDef.CreateCharacter = Foundation.OverrideDef('CreateCharacter', 'Bridge.Characters.Saffi.CreateCharacter', 'Bridge.Characters.B5Saffi.CreateCharacter', dict = { 'modes': [ mode ] } )

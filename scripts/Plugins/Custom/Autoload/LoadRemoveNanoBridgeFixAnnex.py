#########################################
##
## Remove NanoFX BridgeFix Annex
##
## This file was born because NanoFX (v2 Beta) annexed 2 important lines of the BridgeFix
## causing third party bridge to suffer from the floating crew problem when NanoFXv2 was off.
##
## -MLeo
##
########################################

import Foundation

try:
	import Fixes20030217
	import Custom.Autoload.LoadNanoFX
	mode = Foundation.MutatorDef.Stock
	Foundation.OverrideDef('FixSetPosition', 'Bridge.Characters.CommonAnimations.SetPosition', 'Fixes20030217.SetPosition', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('FixLoadBridge', 'LoadBridge.Load', 'Fixes20030217.LoadBridge_Load', dict = { 'modes': [ mode ] } )
except:
	pass

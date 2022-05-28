#########################################
##
## Remove NanoFX FolderDef Annexation
##
## This file was born because NanoFX (v2 Beta) annexed another important line part of FoundationTriggers
## causing triggers depending on the newly introduced "Player created" (and "Ship Created") triggers 
## not to be called NanoFXv2 was off or not installed. For example, FoundationTech depends on this.
##
## -MLeo
##
########################################

import Foundation

try:
	Foundation.FolderDef('ship', 'ships.', { 'modes': [ Foundation.MutatorDef.Stock ] })
except:
	pass

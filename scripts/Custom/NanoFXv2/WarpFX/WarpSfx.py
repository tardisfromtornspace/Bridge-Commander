###############################################################################
##	Filename:	WarpSfx.py
##	
##	Warp Sound Effects Module for WarpFX
##	
##	Created:	10/15/2003 - NanoByte a.k.a Michael T. Braams
###############################################################################
import Foundation

###############################################################################
## Setup Sound Defs for Warp Sounds
###############################################################################
def LoadNanoWarpSfx(mode):	 	
	
	Foundation.SoundDef("scripts/Custom/NanoFXv2/WarpFX/Sfx/Borg/BorgEnterWarp.wav", "BorgEnterWarp", 1.0, { 'modes': [ mode ] })
	Foundation.SoundDef("scripts/Custom/NanoFXv2/WarpFX/Sfx/Borg/BorgExitWarp.wav", "BorgExitWarp", 1.0, { 'modes': [ mode ] })
	
	Foundation.SoundDef("scripts/Custom/NanoFXv2/WarpFX/Sfx/Cardassian/CardassianEnterWarp.wav", "CardassianEnterWarp", 1.0, { 'modes': [ mode ] })
	Foundation.SoundDef("scripts/Custom/NanoFXv2/WarpFX/Sfx/Cardassian/CardassianExitWarp.wav", "CardassianExitWarp", 1.0, { 'modes': [ mode ] })
	
	Foundation.SoundDef("scripts/Custom/NanoFXv2/WarpFX/Sfx/Default/DefaultEnterWarp.wav", "DefaultEnterWarp", 1.0, { 'modes': [ mode ] })
	Foundation.SoundDef("scripts/Custom/NanoFXv2/WarpFX/Sfx/Default/DefaultExitWarp.wav", "DefaultExitWarp", 1.0, { 'modes': [ mode ] })
	
	Foundation.SoundDef("scripts/Custom/NanoFXv2/WarpFX/Sfx/Dominion/DominionEnterWarp.wav", "DominionEnterWarp", 1.0, { 'modes': [ mode ] })
	Foundation.SoundDef("scripts/Custom/NanoFXv2/WarpFX/Sfx/Dominion/DominionExitWarp.wav", "DominionExitWarp", 1.0, { 'modes': [ mode ] })
	
	Foundation.SoundDef("scripts/Custom/NanoFXv2/WarpFX/Sfx/Federation/FederationEnterWarp.wav", "FederationEnterWarp", 1.0, { 'modes': [ mode ] })
	Foundation.SoundDef("scripts/Custom/NanoFXv2/WarpFX/Sfx/Federation/FederationExitWarp.wav", "FederationExitWarp", 1.0, { 'modes': [ mode ] })
	
	Foundation.SoundDef("scripts/Custom/NanoFXv2/WarpFX/Sfx/Ferengi/FerengiEnterWarp.wav", "FerengiEnterWarp", 1.0, { 'modes': [ mode ] })
	Foundation.SoundDef("scripts/Custom/NanoFXv2/WarpFX/Sfx/Ferengi/FerengiExitWarp.wav", "FerengiExitWarp", 1.0, { 'modes': [ mode ] })
	
	Foundation.SoundDef("scripts/Custom/NanoFXv2/WarpFX/Sfx/Kessok/KessokEnterWarp.wav", "KessokEnterWarp", 1.0, { 'modes': [ mode ] })
	Foundation.SoundDef("scripts/Custom/NanoFXv2/WarpFX/Sfx/Kessok/KessokExitWarp.wav", "KessokExitWarp", 1.0, { 'modes': [ mode ] })
	
	Foundation.SoundDef("scripts/Custom/NanoFXv2/WarpFX/Sfx/Klingon/KlingonEnterWarp.wav", "KlingonEnterWarp", 1.0, { 'modes': [ mode ] })
	Foundation.SoundDef("scripts/Custom/NanoFXv2/WarpFX/Sfx/Klingon/KlingonExitWarp.wav", "KlingonExitWarp", 1.0, { 'modes': [ mode ] })
	
	Foundation.SoundDef("scripts/Custom/NanoFXv2/WarpFX/Sfx/Romulan/RomulanEnterWarp.wav", "RomulanEnterWarp", 1.0, { 'modes': [ mode ] })
	Foundation.SoundDef("scripts/Custom/NanoFXv2/WarpFX/Sfx/Romulan/RomulanExitWarp.wav", "RomulanExitWarp", 1.0, { 'modes': [ mode ] })
	
	Foundation.SoundDef("scripts/Custom/NanoFXv2/WarpFX/Sfx/WarpFlash.wav", "NanoWarpFlash", 1.0, { 'modes': [ mode ] })
	
###############################################################################
## End of Warp Sfx
###############################################################################
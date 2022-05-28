from bcdebug import debug
###############################################################################
##	Filename:	NanoFXv2.py
##	
##	Nano's Special Effects Enhancements Version 2.0
##	
##	Updated:	09/30/2003 - NanoByte a.k.a Michael T. Braams
###############################################################################
import App
import Foundation
import Custom.NanoFXv2.NanoFX_Config
import Custom.NanoFXv2.BridgeFX.BrdgGfx
import Custom.NanoFXv2.ExplosionFX.ExpGfx
import Custom.NanoFXv2.ExplosionFX.ExpSfx
import Custom.NanoFXv2.SpecialFX.SpecialGfx
import Custom.NanoFXv2.SpecialFX.SpecialSfx
import Custom.NanoFXv2.WarpFX.WarpSfx

TRUE = 1
FALSE = 0

###############################################################################
## Setup BridgeFX (Optimizations for BC Performance, Small Preview)
###############################################################################
def SetupBridgeFX(mode):
	
	### Override Stock Definitions ###
	debug(__name__ + ", SetupBridgeFX")
	Foundation.OverrideDef('NanoBridgeHit', 'Bridge.bridgeeffects.DoHullDamage', 'Custom.NanoFXv2.BridgeFX.BrdgFX.NanoBridgeHit', dict = { 'modes': [ mode ] } )
	Custom.NanoFXv2.BridgeFX.BrdgGfx.LoadNanoBrdgGfx()
	###
	#if Custom.NanoFXv2.NanoFX_Config.bFX_Enabled == TRUE:
		#print "BridgeFX Enabled..."
		###
###############################################################################
## Setup CameraFX (Preview of Upcoming Camera Mod)
###############################################################################
def SetupCameraFX(mode):
	
	debug(__name__ + ", SetupCameraFX")
	if Custom.NanoFXv2.NanoFX_Config.cFX_Enabled == TRUE:
		### Override Stock Definitions ###
		Foundation.OverrideDef('NanoFlyByCamera', 'CameraModes.DropAndWatch', 'Custom.NanoFXv2.CameraFX.CamFX.NanoFlyByCamera', dict = { 'modes': [ mode ] } )
		Foundation.OverrideDef('NanoViewScreenZoom', 'CameraModes.ViewscreenZoomTarget', 'Custom.NanoFXv2.CameraFX.CamFX.NanoViewScreenZoom', dict = { 'modes': [ mode ] } )
		Foundation.OverrideDef('NanoFixWarpCam', 'WarpSequence.FixCamera', 'Custom.NanoFXv2.CameraFX.CamFX.NanoFixWarpCam', dict = { 'modes': [ mode ] } )
		###
		#print "CameraFX Enabled..."
		###
###############################################################################
## Setup ExplosionFX
###############################################################################
def SetupExplosionFX(mode):

	debug(__name__ + ", SetupExplosionFX")
	if Custom.NanoFXv2.NanoFX_Config.eFX_Enabled == TRUE:
		### Load Explosion Gfx ###
		Custom.NanoFXv2.ExplosionFX.ExpGfx.LoadNanoExpGfx()
		App.g_kIconManager.RegisterIconGroup("DamageTextures", "Custom.NanoFXv2.ExplosionFX.ExpGfx", "LoadNanoDamageGfx")
		###
		### Load Explosion Sfx ###
		Custom.NanoFXv2.ExplosionFX.ExpSfx.LoadNanoExpSfx(mode)
		###
		### Override Stock Definitions ###
		Foundation.OverrideDef('NanoTorpedoShieldHit', 'Effects.TorpedoShieldHit', 'Custom.NanoFXv2.ExplosionFX.ExpFX.NanoTorpedoShieldHit', dict = { 'modes': [ mode ] } )
		Foundation.OverrideDef('NanoTorpedoHullHit', 'Effects.TorpedoHullHit', 'Custom.NanoFXv2.ExplosionFX.ExpFX.NanoTorpedoHullHit', dict = { 'modes': [ mode ] } )
		Foundation.OverrideDef('NanoPhaserHullHit', 'Effects.PhaserHullHit', 'Custom.NanoFXv2.ExplosionFX.ExpFX.NanoPhaserHullHit', dict = { 'modes': [ mode ] } )
		Foundation.OverrideDef('NanoCollisionEffect', 'Effects.CollisionEffect', 'Custom.NanoFXv2.ExplosionFX.ExpFX.NanoCollisionEffect', dict = { 'modes': [ mode ] } )
		Foundation.OverrideDef('NanoDeathSeq', 'Effects.ObjectExploding', 'Custom.NanoFXv2.ExplosionFX.ExpFX.NanoDeathSeq', dict = { 'modes': [ mode ] } )
		###
		### Override Definitions for GlowFX ###
		Foundation.OverrideDef('RepairShipFullyGlowFix', 'Actions.ShipScriptActions.RepairShipFully', 'Custom.NanoFXv2.ExplosionFX.GlowFX.RepairShipFullyGlowFix', dict = { 'modes': [ mode ] } )
		###
		#print "ExplosionFX Enabled..."
		###
###############################################################################
## Setup SpecialFX
###############################################################################
def SetupSpecialFX(mode):
	
	debug(__name__ + ", SetupSpecialFX")
	import Custom.NanoFXv2.SpecialFX.AtmosphereFX
	
	if Custom.NanoFXv2.NanoFX_Config.sFX_Enabled == TRUE:
		### Load SpecialFX Gfx ###
		Custom.NanoFXv2.SpecialFX.SpecialGfx.LoadNanoSpecialGfx()
		###
		### Load Explosion Sfx ###
		Custom.NanoFXv2.SpecialFX.SpecialSfx.LoadNanoSpecialSfx(mode)
		###
		### Add Atmospheres to Planets
		Custom.NanoFXv2.SpecialFX.AtmosphereFX.OverrideStockPlanets(mode)
		###
		#print "SpecialFX Enabled..."
		###

###############################################################################
## Setup WarpFX
###############################################################################
def SetupWarpFX(mode):
	
	debug(__name__ + ", SetupWarpFX")
	if Custom.NanoFXv2.NanoFX_Config.wFX_Enabled == TRUE:
		### Load Warp Gfx ###
		App.g_kIconManager.RegisterIconGroup("EffectTextures", "Custom.NanoFXv2.WarpFX.WarpGfx", "LoadNanoWarpNacelleGfx")
		App.g_kIconManager.RegisterIconGroup("WarpFlashTextures", "Custom.NanoFXv2.WarpFX.WarpGfx", "LoadNanoWarpFlashGfx")
		###
		### Load Warp Sfx ###
		Custom.NanoFXv2.WarpFX.WarpSfx.LoadNanoWarpSfx(mode)
		###
		### Override Stock Definitions ###
		Foundation.OverrideDef('NanoWarpSeq', 'WarpSequence.SetupSequence', 'Custom.NanoFXv2.WarpFX.WarpFX.NanoWarpSeq', dict = { 'modes': [ mode ] } )
		###
		### Setup New AI
		#Foundation.OverrideDef.NanoIntercept = Foundation.OverrideDef('NanoIntercept', 'AI.PlainAI.Intercept.Intercept', 'Custom.NanoFXv2.WarpFX.AI.NanoIntercept.NanoIntercept', dict = { 'modes': [ mode ] } )
		Foundation.OverrideDef('NanoWarp', 'AI.PlainAI.Warp.Warp', 'Custom.NanoFXv2.WarpFX.AI.NanoWarp.NanoWarp', dict = { 'modes': [ mode ] } )
		Foundation.OverrideDef('NanoFollowThroughWarp', 'AI.PlainAI.FollowThroughWarp.FollowThroughWarp', 'Custom.NanoFXv2.WarpFX.AI.NanoFollowThroughWarp.NanoFollowThroughWarp', dict = { 'modes': [ mode ] } )
		###
		#print "WarpFX Enabled..."
		###
###############################################################################
## End of Loading NanoFX
###############################################################################

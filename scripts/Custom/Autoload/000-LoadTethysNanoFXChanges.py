##########################################################################
# Code added by CharaToLoki
# Patches NanoFXv2 to add the alternate atmospheres Tethys wants, without modifying core files.
# VERSION: SEE "versionPatch" below
##########################################################################
from bcdebug import debug
import traceback
import Foundation
import App

import string

TRUE = 1
FALSE = 0

versionPatch = 20260616 # Our version of the patch
# If disabled, replace TRUE with FALSE
bEnabled = FALSE

try:
	import Custom.NanoFXv2.NanoFX_Config 
	from Custom.NanoFXv2 import NanoFX_Lib
	from Custom.NanoFXv2 import NanoFX_Setup
	import Multiplayer.MissionShared

	if not NanoFX_Lib:
		print __name__, " you don't have NanoFXv2 installed"
		bEnabled = FALSE
	else:
		if not hasattr(NanoFX_Lib, "version") or NanoFX_Lib.version < versionPatch:
			bEnabled = TRUE
except:
	print "NanoFX v2 beta is not installed, or an error happened:"
	bEnabled = FALSE
	traceback.print_exc()

if bEnabled:
	print "Adding Tethys Atmospheres to NanoFX v2 BETA (version ", versionPatch, ")"

	def NewCreateAtmosphereALT(pPlanet, sNifPath = "data/Models/Environment/planet.nif", sCloudPath = "data/Models/Environment/cloud.nif", sTexturePath = "Class-M"):

		debug(__name__ + ", NewCreateAtmosphereALT")
		try:
			import Custom.NanoFXv2.NanoFX_Config 
			if Custom.NanoFXv2.NanoFX_Config.sFX_Enabled == 1:
				if Custom.NanoFXv2.NanoFX_Config.sFX_AtmosphereAltFX == "On":
					import Custom.NanoFXv2.SpecialFX.AtmosphereALT
					Custom.NanoFXv2.SpecialFX.AtmosphereALT.CreateAtmosphereALT(pPlanet, sNifPath, sTexturePath, sCloudPath)
				else:
					import Custom.NanoFXv2.SpecialFX.AtmosphereFX
					Custom.NanoFXv2.SpecialFX.AtmosphereFX.CreateAtmosphereFX(pPlanet, sNifPath, sTexturePath)
		except:
			print __name__, ".NewCreateAtmosphereALT ERROR: "
			traceback.print_exc()

	NanoFX_Lib.CreateAtmosphereALT = NewCreateAtmosphereALT

	def NewCreateAtmosphereFXALT(pPlanet, sNifPath = "data/Models/Environment/planet.nif", sTexturePath = "Class-M"):
		debug(__name__ + ", CreateAtmosphereFXALT")
		NanoFX_Lib.CreateAtmosphereALT(pPlanet, sNifPath, sNifPath, sTexturePath)
				

	NanoFX_Lib.CreateAtmosphereFX = NewCreateAtmosphereFXALT

	def NewSetupSpecialFX(mode):
	
		debug(__name__ + ", SetupSpecialFX")
		import Custom.NanoFXv2.SpecialFX.AtmosphereFX
		import Custom.NanoFXv2.SpecialFX.AtmosphereALT
	
		if Custom.NanoFXv2.NanoFX_Config.sFX_Enabled == TRUE:
			### Load SpecialFX Gfx ###
			Custom.NanoFXv2.SpecialFX.SpecialGfx.LoadNanoSpecialGfx()
			###
			### Load Explosion Sfx ###
			Custom.NanoFXv2.SpecialFX.SpecialSfx.LoadNanoSpecialSfx(mode)
			###
			### Add Atmospheres to Planets
			if Custom.NanoFXv2.NanoFX_Config.sFX_AtmosphereAltFX == "On":
				### Add Atmospheres to Planets
				Custom.NanoFXv2.SpecialFX.AtmosphereALT.OverrideStockPlanets(mode)
			elif Custom.NanoFXv2.NanoFX_Config.sFX_AtmosphereGlowFX == "On":
				### Add Atmospheres to Planets
				Custom.NanoFXv2.SpecialFX.AtmosphereFX.OverrideStockPlanets(mode)
			###
			#print "SpecialFX Enabled..."
			###

	NanoFX_Setup.SetupSpecialFX = NewSetupSpecialFX
	
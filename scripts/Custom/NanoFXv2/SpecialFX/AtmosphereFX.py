from bcdebug import debug
###############################################################################
##	Filename:	AtmoshpereFX.py
##	
##	Creates an Atmosphere around a planet
##	
##	Created:	05/17/2003 - NanoByte a.k.a Michael T. Braams
###############################################################################
import App
import Foundation
import Custom.NanoFXv2.NanoFX_Config
import Custom.NanoFXv2.NanoFX_ScriptActions

###############################################################################
## AtmosphereFX
###############################################################################
def CreateAtmosphereFX(pPlanet, sNifPath, sTexturePath):
	
	### Setup for Effect
	debug(__name__ + ", CreateAtmosphereFX")
	pSet          = pPlanet.GetContainingSet()
	fSize         = pPlanet.GetRadius()
	sName         = pPlanet.GetName()
	###
	pPlanet.SetAtmosphereRadius ((fSize * 1.15) - fSize)
	pPlanet.UpdateNodeOnly()
	###
	# lennie notes:  these layers are render-order specific!

	#0.15 1.15 1.15
	pAtmosphere1 = App.Sun_Create(fSize * 0.1, fSize * 1.05, 0.0, "scripts/Custom/NanoFXv2/SpecialFX/Gfx/Atmosphere/" + sTexturePath + "/GlowColor.tga", None)
	pSet.AddObjectToSet(pAtmosphere1, sName + " Air")
	pAtmosphere1.UpdateNodeOnly()
	pPlanet.AttachObject(pAtmosphere1)

	### Create Sphere Model Around Planet for Clouds ###
	pAtmosphere = App.Planet_Create(fSize * 1.01, sNifPath)
	pSet.AddObjectToSet(pAtmosphere, sTexturePath + " Planet")
	pAtmosphere.UpdateNodeOnly()
	pPlanet.AttachObject(pAtmosphere)

	# 0.1 1.11 0.0
	pAtmosphere2 = App.Sun_Create(fSize * 0.1, fSize * 1.0102, 0.0, "scripts/Custom/NanoFXv2/SpecialFX/Gfx/Atmosphere/" + sTexturePath + "/Clouds.tga", None)
	pSet.AddObjectToSet(pAtmosphere2, sName + " Clouds")
	pAtmosphere2.UpdateNodeOnly()
	pPlanet.AttachObject(pAtmosphere2)

	# 0.65 1.15 1.15
	pAtmosphere3 = App.Sun_Create(fSize * 0.2, fSize * 1.1, 0.0, "scripts/Custom/NanoFXv2/SpecialFX/Gfx/Atmosphere/Glow.tga", None)
	pSet.AddObjectToSet(pAtmosphere3, sName + " Glow")
	pAtmosphere3.UpdateNodeOnly()
	pPlanet.AttachObject(pAtmosphere3)	
		
def OverrideStockPlanets(mode):
	
	debug(__name__ + ", OverrideStockPlanets")
	Foundation.OverrideDef('Initialize', 'Systems.Albirea.Albirea1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Albirea.Albirea1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Albirea.Albirea2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Albirea.Albirea2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Albirea.Albirea3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Albirea.Albirea3_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Alioth.Alioth1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Alioth.Alioth1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Alioth.Alioth2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Alioth.Alioth2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Alioth.Alioth3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Alioth.Alioth3_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Alioth.Alioth4_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Alioth.Alioth4_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Alioth.Alioth5_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Alioth.Alioth5_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Alioth.Alioth6_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Alioth.Alioth6_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Alioth.Alioth7_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Alioth.Alioth7_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Alioth.Alioth8_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Alioth.Alioth8_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Artrus.Artrus1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Artrus.Artrus1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Artrus.Artrus2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Artrus.Artrus2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Artrus.Artrus3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Artrus.Artrus3_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Ascella.Ascella1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Ascella.Ascella1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Ascella.Ascella2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Ascella.Ascella2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Ascella.Ascella3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Ascella.Ascella3_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Ascella.Ascella4_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Ascella.Ascella4_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Ascella.Ascella5_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Ascella.Ascella5_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Belaruz.Belaruz2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Belaruz.Belaruz2_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Belaruz.Belaruz3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Belaruz.Belaruz3_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Belaruz.Belaruz4_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Belaruz.Belaruz4_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Beol.Beol1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Beol.Beol1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Beol.Beol2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Beol.Beol2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Beol.Beol3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Beol.Beol3_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Beol.Beol4_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Beol.Beol4_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Biranu.Biranu1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Biranu.Biranu1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Biranu.Biranu2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Biranu.Biranu2_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Cebalrai.Cebalrai1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Cebalrai.Cebalrai1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Cebalrai.Cebalrai2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Cebalrai.Cebalrai2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Cebalrai.Cebalrai3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Cebalrai.Cebalrai3_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Chambana.Chambana1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Chambana.Chambana1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Chambana.Chambana2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Chambana.Chambana2_S.Initialize', dict = { 'modes': [ mode ] } )	
	
	Foundation.OverrideDef('Initialize', 'Systems.Geble.Geble1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Geble.Geble1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Geble.Geble2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Geble.Geble2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Geble.Geble3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Geble.Geble3_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Geble.Geble4_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Geble.Geble4_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Itari.Itari1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Itari.Itari1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Itari.Itari2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Itari.Itari2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Itari.Itari3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Itari.Itari3_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Itari.Itari4_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Itari.Itari4_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Itari.Itari5_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Itari.Itari5_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Itari.Itari6_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Itari.Itari6_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Itari.Itari7_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Itari.Itari7_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Itari.Itari8_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Itari.Itari8_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Nepenthe.Nepenthe1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Nepenthe.Nepenthe1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Nepenthe.Nepenthe2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Nepenthe.Nepenthe2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Nepenthe.Nepenthe3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Nepenthe.Nepenthe3_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.OmegaDraconis.OmegaDraconis1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.OmegaDraconis.OmegaDraconis1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.OmegaDraconis.OmegaDraconis2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.OmegaDraconis.OmegaDraconis2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.OmegaDraconis.OmegaDraconis3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.OmegaDraconis.OmegaDraconis3_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.OmegaDraconis.OmegaDraconis4_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.OmegaDraconis.OmegaDraconis4_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.OmegaDraconis.OmegaDraconis5_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.OmegaDraconis.OmegaDraconis5_S.Initialize', dict = { 'modes': [ mode ] } )	
	
	Foundation.OverrideDef('Initialize', 'Systems.Ona.Ona1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Ona.Ona1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Ona.Ona2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Ona.Ona2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Ona.Ona3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Ona.Ona3_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Poseidon.Poseidon1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Poseidon.Poseidon1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Poseidon.Poseidon2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Poseidon.Poseidon2_S.Initialize', dict = { 'modes': [ mode ] } )	
	
	Foundation.OverrideDef('Initialize', 'Systems.Prendel.Prendel1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Prendel.Prendel1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Prendel.Prendel2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Prendel.Prendel2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Prendel.Prendel3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Prendel.Prendel3_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Prendel.Prendel4_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Prendel.Prendel4_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Prendel.Prendel5_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Prendel.Prendel5_S.Initialize', dict = { 'modes': [ mode ] } )	
	
	Foundation.OverrideDef('Initialize', 'Systems.Riha.Riha1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Riha.Riha1_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Savoy.Savoy1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Savoy.Savoy1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Savoy.Savoy2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Savoy.Savoy2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Savoy.Savoy3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Savoy.Savoy3_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Serris.Serris1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Serris.Serris1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Serris.Serris2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Serris.Serris2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Serris.Serris3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Serris.Serris3_S.Initialize', dict = { 'modes': [ mode ] } )
	
	#Foundation.OverrideDef('Initialize', 'Systems.Starbase12.Starbase12_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Starbase12.Starbase12_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Tevron.Tevron1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Tevron.Tevron1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Tevron.Tevron2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Tevron.Tevron2_S.Initialize', dict = { 'modes': [ mode ] } )	
	
	Foundation.OverrideDef('Initialize', 'Systems.Tezle.Tezle1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Tezle.Tezle1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Tezle.Tezle2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Tezle.Tezle2_S.Initialize', dict = { 'modes': [ mode ] } )	
	
	Foundation.OverrideDef('Initialize', 'Systems.Vesuvi.Vesuvi5_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Vesuvi.Vesuvi5_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Vesuvi.Vesuvi6_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Vesuvi.Vesuvi6_S.Initialize', dict = { 'modes': [ mode ] } )
	
	Foundation.OverrideDef('Initialize', 'Systems.Voltair.Voltair1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Voltair.Voltair1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Voltair.Voltair2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Voltair.Voltair2_S.Initialize', dict = { 'modes': [ mode ] } )	
	
	Foundation.OverrideDef('Initialize', 'Systems.XiEntrades.XiEntrades1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.XiEntrades.XiEntrades1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.XiEntrades.XiEntrades2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.XiEntrades.XiEntrades2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.XiEntrades.XiEntrades3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.XiEntrades.XiEntrades3_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.XiEntrades.XiEntrades4_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.XiEntrades.XiEntrades4_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.XiEntrades.XiEntrades5_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.XiEntrades.XiEntrades5_S.Initialize', dict = { 'modes': [ mode ] } )	
	
	Foundation.OverrideDef('Initialize', 'Systems.Yiles.Yiles1_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Yiles.Yiles1_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Yiles.Yiles2_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Yiles.Yiles2_S.Initialize', dict = { 'modes': [ mode ] } )	
	Foundation.OverrideDef('Initialize', 'Systems.Yiles.Yiles3_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Yiles.Yiles3_S.Initialize', dict = { 'modes': [ mode ] } )
	Foundation.OverrideDef('Initialize', 'Systems.Yiles.Yiles4_S.Initialize', 'Custom.NanoFXv2.SpecialFX.Systems.Yiles.Yiles4_S.Initialize', dict = { 'modes': [ mode ] } )
from bcdebug import debug
import traceback
import Foundation
import App

mode = Foundation.MutatorDef("Stock KM Regions and Systems (Course-Set Menu)")
Foundation.MutatorDef.LoadSystems = mode
mode.bBase = 1

class LoadSystemsTrigger(Foundation.TriggerDef):
	def __init__(self, name, eventKey, dict = {}):
		debug(__name__ + ", __init__")
		Foundation.TriggerDef.__init__(self, name, eventKey, dict)

	def __call__(self, pObject, pEvent, dict = {}):
		debug(__name__ + ", __call__")
		pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()

		if pMission.GetScript() == "QuickBattle.QuickBattle":

			try:
				import Systems.Starbase12.Starbase
				Systems.Starbase12.Starbase.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()
			try:
				import Systems.Belaruz.Belaruz
				Systems.Belaruz.Belaruz.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()
			try:
				import Systems.Vesuvi.Vesuvi
				Systems.Vesuvi.Vesuvi.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Albirea.Albirea
				Systems.Albirea.Albirea.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Alioth.Alioth
				Systems.Alioth.Alioth.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Artrus.Artrus
				Systems.Artrus.Artrus.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Ascella.Ascella
				Systems.Ascella.Ascella.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Beol.Beol
				Systems.Beol.Beol.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Biranu.Biranu
				Systems.Biranu.Biranu.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Chambana.Chambana
				Systems.Chambana.Chambana.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Geble.Geble
				Systems.Geble.Geble.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Itari.Itari
				Systems.Itari.Itari.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.OmegaDraconis.OmegaDraconis
				Systems.OmegaDraconis.OmegaDraconis.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Ona.Ona
				Systems.Ona.Ona.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Poseidon.Poseidon
				Systems.Poseidon.Poseidon.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Prendel.Prendel
				Systems.Prendel.Prendel.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Savoy.Savoy
				Systems.Savoy.Savoy.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Serris.Serris
				Systems.Serris.Serris.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Tevron.Tevron
				Systems.Tevron.Tevron.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Tezle.Tezle
				Systems.Tezle.Tezle.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Procyon.Procyon
				Systems.Procyon.Procyon.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Voltair.Voltair
				Systems.Voltair.Voltair.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.XiEntrades.XiEntrades
				Systems.XiEntrades.XiEntrades.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Yiles.Yiles
				Systems.Yiles.Yiles.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Badlands.Badlands
				Systems.Badlands.Badlands.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Cebalrai.Cebalrai
				Systems.Cebalrai.Cebalrai.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Sol.Sol
				Systems.Sol.Sol.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.KavisAlpha.KavisAlpha
				Systems.KavisAlpha.KavisAlpha.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Obstacles.Obstacles
				Systems.Obstacles.Obstacles.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Ross_128.Ross_128
				Systems.Ross_128.Ross_128.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.String.String
				Systems.String.String.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Banzai.Banzai
				Systems.Banzai.Banzai.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Fluid.Fluid
				Systems.Fluid.Fluid.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Hekaras.Hekaras
				Systems.Hekaras.Hekaras.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Khan.Khan
				Systems.Khan.Khan.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.SystemJ25.SystemJ25
				Systems.SystemJ25.SystemJ25.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Arcturus.Arcturus
				Systems.Arcturus.Arcturus.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Baqis.Baqis
				Systems.Baqis.Baqis.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Borealis.Borealis
				Systems.Borealis.Borealis.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.CJones.CJones
				Systems.CJones.CJones.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Kronos.Kronos
				Systems.Kronos.Kronos.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Rainbow.Rainbow
				Systems.Rainbow.Rainbow.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Tathis.Tathis
				Systems.Tathis.Tathis.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Vulcan.Vulcan
				Systems.Vulcan.Vulcan.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.ArenaA.ArenaA
				Systems.ArenaA.ArenaA.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.BriarPatch.BriarPatch
				Systems.BriarPatch.BriarPatch.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Comet.Comet
				Systems.Comet.Comet.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Pleides.Pleides
				Systems.Pleides.Pleides.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.RedGiant.RedGiant
				Systems.RedGiant.RedGiant.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Sirius_B.Sirius_B
				Systems.Sirius_B.Sirius_B.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Vatris.Vatris
				Systems.Vatris.Vatris.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Wolf359.Wolf359
				Systems.Wolf359.Wolf359.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Calufrax.Calufrax
				Systems.Calufrax.Calufrax.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Junkyard.Junkyard
				Systems.Junkyard.Junkyard.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Nepenthe.Nepenthe
				Systems.Nepenthe.Nepenthe.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Riha.Riha
				Systems.Riha.Riha.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.SmokeRing.SmokeRing
				Systems.SmokeRing.SmokeRing.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Betelgeuse.Betelgeuse
				Systems.Betelgeuse.Betelgeuse.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Canopus.Canopus
				Systems.Canopus.Canopus.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.DryDock.DryDockSystem
				Systems.DryDock.DryDockSystem.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.GasGiant.GasGiant
				Systems.GasGiant.GasGiant.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Kastra.Kastra
				Systems.Kastra.Kastra.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Nursery.Nursery
				Systems.Nursery.Nursery.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Romulus.Romulus
				Systems.Romulus.Romulus.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Vger.Vger
				Systems.Vger.Vger.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Cardassia.Cardassia
				Systems.Cardassia.Cardassia.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.DeepSpace9.DeepSpace9
				Systems.DeepSpace9.DeepSpace9.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.PsiBlackhole.PsiBlackholeSys
				Systems.PsiBlackhole.PsiBlackholeSys.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Promellian.Promellian
				Systems.Promellian.Promellian.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Romii.Romii
				Systems.Romii.Romii.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()

			try:
				import Systems.Achernar.Achernar
				Systems.Achernar.Achernar.CreateMenus()
			except:
				print __name__, "LoadSystemsTrigger.__call__ error:"
				traceback.print_exc()


LoadSystemsTrigger('LoadSystemsTrigger', Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP, dict = { 'modes': [ mode ] } )
